#!/usr/bin/env python3
"""Synchronize pinned upstream source snapshots without executing upstream code.

Python 3.11+, standard library only. All sources are prepared and checked before
any source is replaced. --check performs read-only discovery; --stage is opt-in.
"""

import argparse
import copy
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request

from build_model_catalog import render_baselines_index, render_catalog, render_homepage


class SyncError(RuntimeError):
    def __init__(self, message, status='error'):
        super().__init__(message)
        self.status = status


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def blob_sha(content):
    return hashlib.sha1(b'blob ' + str(len(content)).encode('ascii') + b'\0' + content).hexdigest()


def safe_parts(value):
    if not isinstance(value, str) or not value or '\\' in value:
        raise SyncError('Unsafe source path: ' + repr(value))
    parts = PurePosixPath(value).parts
    if PurePosixPath(value).is_absolute() or '/'.join(parts) != value:
        raise SyncError('Unsafe source path: ' + repr(value))
    for part in parts:
        stem = part.split('.')[0].upper()
        if (part in ('.', '..') or part.lower() == '.git' or part.endswith((' ', '.'))
                or any(ord(c) < 32 or c in ':*?"<>|' for c in part)
                or stem in {'CON', 'PRN', 'AUX', 'NUL', *(f'COM{i}' for i in range(1, 10)),
                            *(f'LPT{i}' for i in range(1, 10))}):
            raise SyncError('Unsafe or nonportable source path: ' + repr(value))
    return parts


def local_path(root, value):
    target = root.joinpath(*safe_parts(value))
    current = root
    for part in safe_parts(value):
        current = current / part
        if current.is_symlink():
            raise SyncError('Symbolic link conflicts with source path: ' + value, 'conflict')
    if root not in target.resolve().parents:
        raise SyncError('Source path escapes repository: ' + value)
    return target


def validate_manifest(manifest):
    if manifest.get('schema_version') != 1 or not manifest.get('sources'):
        raise SyncError('Unsupported or empty source lock')
    seen = set()
    names = set()
    for source in manifest['sources']:
        parts = safe_parts(source['local_directory'])
        if len(parts) != 2 or parts[0] not in ('baselines', 'libraries'):
            raise SyncError('Source directory must be baselines/<name> or libraries/<name>')
        prefix = source['local_directory']
        if prefix.casefold() in seen or source['name'] in names:
            raise SyncError('Duplicate source directory or source name')
        seen.add(prefix.casefold())
        names.add(source['name'])
        if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', source['repository']):
            raise SyncError('Invalid GitHub repository identifier')
        files = source['files']
        paths = set()
        for entry in files:
            safe_parts(entry['path'])
            if not entry['path'].startswith(prefix + '/') or entry['mode'] not in ('100644', '100755'):
                raise SyncError('Invalid locked source file: ' + entry['path'])
            if entry['path'].casefold() in paths:
                raise SyncError('Duplicate or case-colliding locked file: ' + entry['path'])
            paths.add(entry['path'].casefold())
            if not re.fullmatch(r'[0-9a-f]{40}', entry['git_blob_sha1']):
                raise SyncError('Invalid blob hash: ' + entry['path'])


def check_local(root, manifest):
    conflicts = []
    for source in manifest['sources']:
        directory = local_path(root, source['local_directory'])
        expected = {entry['path'] for entry in source['files']}
        actual = set()
        if not directory.is_dir():
            conflicts.append('Missing source directory: ' + source['local_directory'])
            continue
        for parent, dirs, files in os.walk(directory, followlinks=False):
            for name in dirs + files:
                path = Path(parent) / name
                if path.is_symlink():
                    conflicts.append('Symbolic link: ' + path.relative_to(root).as_posix())
            for name in files:
                actual.add((Path(parent) / name).relative_to(root).as_posix())
        for path in sorted(actual - expected):
            conflicts.append('Additional source file: ' + path)
        for entry in source['files']:
            path = local_path(root, entry['path'])
            if not path.is_file():
                conflicts.append('Missing source file: ' + entry['path'])
                continue
            content = path.read_bytes()
            if len(content) != entry['size_bytes'] or blob_sha(content) != entry['git_blob_sha1']:
                conflicts.append('Modified source file: ' + entry['path'])
            if os.name != 'nt' and bool(path.stat().st_mode & stat.S_IXUSR) != (entry['mode'] == '100755'):
                conflicts.append('Modified executable mode: ' + entry['path'])
    if conflicts:
        raise SyncError('Local source conflicts; no files overwritten:\n' + '\n'.join(conflicts[:30]), 'conflict')


class GitHub:
    def __init__(self, token=None):
        self.headers = {'User-Agent': 'zpb-time-series-upstream-sync',
                        'Accept': 'application/vnd.github+json',
                        'X-GitHub-Api-Version': '2022-11-28'}
        if token:
            self.headers['Authorization'] = 'Bearer ' + token

    def read(self, url, authenticated=True):
        for attempt in range(3):
            headers = self.headers if authenticated else {'User-Agent': self.headers['User-Agent']}
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as response:
                    return response.read()
            except urllib.error.HTTPError as error:
                retry = error.code in (429, 500, 502, 503, 504) or (
                    error.code == 403 and error.headers.get('Retry-After'))
                if not retry or attempt == 2:
                    raise SyncError(f'GitHub request failed: HTTP {error.code} for {url}') from None
            except (urllib.error.URLError, TimeoutError, OSError) as error:
                if attempt == 2:
                    raise SyncError(f'Network request failed for {url}: {type(error).__name__}') from None
            time.sleep(2 ** attempt)

    def api(self, endpoint):
        return json.loads(self.read('https://api.github.com' + endpoint))


def protective_file(path):
    name = PurePosixPath(path).name.upper()
    return name in ('LEGAL', 'LEGAL.MD', 'LEGAL.TXT') or name.startswith(
        ('LICENSE', 'LICENCE', 'NOTICE', 'COPYING', 'COPYRIGHT'))


def prepare_tree(source, tree):
    if tree.get('truncated'):
        raise SyncError('Truncated upstream tree: ' + source['name'])
    files = []
    gitlinks = []
    portable = {}
    prefix = source['local_directory']
    for entry in tree['tree']:
        parts = safe_parts(entry['path'])
        for length in range(1, len(parts) + 1):
            value = '/'.join(parts[:length])
            previous = portable.setdefault(value.casefold(), value)
            if previous != value:
                raise SyncError('Upstream paths collide on Windows: ' + value)
        if entry['type'] == 'tree':
            continue
        if entry['type'] == 'commit' and entry['mode'] == '160000':
            previous = next((item for item in source.get('gitlinks', [])
                             if item.get('upstream_path') == entry['path']
                             or item.get('path') == prefix + '/' + entry['path']), {})
            item = copy.deepcopy(previous)
            item.update(path=prefix + '/' + entry['path'], upstream_path=entry['path'],
                        commit=entry['sha'], mode='160000', status='omitted_optional')
            item.setdefault('remote_url', None)
            item.setdefault('reason', 'Dependency source is not vendored. Its remote URL is not inferred.')
            gitlinks.append(item)
        elif entry['type'] == 'blob' and entry['mode'] in ('100644', '100755'):
            files.append({'path': prefix + '/' + entry['path'], 'git_blob_sha1': entry['sha'],
                          'mode': entry['mode'], 'size_bytes': entry['size']})
        else:
            raise SyncError('Unsupported upstream file mode/type (including symlinks): ' + entry['path'])
    files.sort(key=lambda item: item['path'])
    old_legal = {item['path']: item['git_blob_sha1'] for item in source['files'] if protective_file(item['path'])}
    new_legal = {item['path']: item['git_blob_sha1'] for item in files if protective_file(item['path'])}
    if old_legal != new_legal:
        paths = sorted(path for path in old_legal.keys() | new_legal.keys()
                       if old_legal.get(path) != new_legal.get(path))
        raise SyncError('License/NOTICE/LEGAL changes need review before import: ' + ', '.join(paths), 'needs_review')
    old_links = {item['path'] for item in source.get('gitlinks', [])}
    if {item['path'] for item in gitlinks} - old_links:
        raise SyncError('New gitlink dependencies need review before import: ' + source['name'], 'needs_review')
    return files, gitlinks


def describe_change(source, commit, branch, files):
    old = {item['path']: item for item in source['files']}
    new = {item['path']: item for item in files}
    added = sorted(new.keys() - old.keys())
    deleted = sorted(old.keys() - new.keys())
    modified = sorted(path for path in old.keys() & new.keys()
                      if old[path]['git_blob_sha1'] != new[path]['git_blob_sha1'])
    modes = sorted(path for path in old.keys() & new.keys() if old[path]['mode'] != new[path]['mode'])
    changed = sorted(set(added + deleted + modified + modes))
    return {'name': source['name'], 'repository': source['repository'],
            'local_directory': source['local_directory'], 'old_commit': source['commit'],
            'new_commit': commit, 'branch': branch, 'file_count': len(files),
            'updated': commit != source['commit'], 'added': len(added), 'modified': len(modified),
            'deleted': len(deleted), 'mode_changed': len(modes),
            'changed_files': changed, 'changed_file_count': len(changed)}


def unpack_archive(content, source, files, destination):
    expected = {item['path'][len(source['local_directory']) + 1:]: item for item in files}
    seen = set()
    root_prefix = None
    lfs = []
    with tarfile.open(fileobj=io.BytesIO(content), mode='r:gz') as archive:
        for member in archive:
            if member.issym() or member.islnk() or not (member.isdir() or member.isfile()):
                raise SyncError('Unsupported tar entry: ' + member.name)
            name = member.name.rstrip('/')
            parts = safe_parts(name)
            if root_prefix is None:
                root_prefix = parts[0]
            if parts[0] != root_prefix:
                raise SyncError('Archive has multiple roots')
            if member.isdir():
                continue
            relative = '/'.join(parts[1:])
            if relative not in expected or relative in seen:
                raise SyncError('Unexpected or duplicate archived file: ' + relative)
            data = archive.extractfile(member).read()
            entry = expected[relative]
            if len(data) != entry['size_bytes'] or blob_sha(data) != entry['git_blob_sha1']:
                raise SyncError('Upstream archive/blob mismatch: ' + relative)
            target = destination.joinpath(*safe_parts(relative))
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            if data.startswith(b'version https://git-lfs.github.com/spec/v1\n'):
                lfs.append({'path': entry['path'], 'status': 'pointer_only',
                            'pointer': data.decode('ascii')})
            seen.add(relative)
    if seen != set(expected):
        raise SyncError('Archive is missing upstream blobs: ' + source['name'])
    return lfs


def status_document(manifest, changes, checked_at):
    rows = ['# 上游源码同步状态', '', f'最近一次有更新的同步时间（UTC）：`{checked_at}`。', '',
            '本页由 `tools/sync_upstreams.py` 在实际导入新提交时生成；无更新检查不改写本页。', '',
            '| 来源 | 本地目录 | 已导入提交 | 原始文件数 | 本次变更文件数 |',
            '| --- | --- | --- | ---: | ---: |']
    by_name = {item['name']: item for item in changes}
    for source in manifest['sources']:
        item = by_name[source['name']]
        directory = source['local_directory']
        rows.append(f"| {source['name']} | [{directory}](../{directory}/) | "
                    f"[`{source['commit'][:12]}`]({source['url']}/commit/{source['commit']}) | "
                    f"{len(source['files'])} | {item['changed_file_count']} |")
    rows += ['', f"合计 {len(manifest['sources'])} 个来源、{manifest['original_file_count']} 个原始文件。",
             '', '变更文件数按新增、内容修改、删除或模式变化的路径去重计算。原始文件哈希见 [sources.lock.json](../sources.lock.json)。']
    for source in manifest['sources']:
        if source['name'] != 'Time-Series-Library':
            continue
        prefix = source['local_directory'] + '/models/'
        models = [entry['path'] for entry in source['files'] if entry['path'].startswith(prefix)
                  and '/' not in entry['path'][len(prefix):] and entry['path'].endswith('.py')
                  and PurePosixPath(entry['path']).name != '__init__.py']
        rows += ['', f'## Time-Series-Library 当前模型文件（{len(models)} 个）', '',
                 '以下列表由当前来源锁直接生成，每次实际同步时随源码更新。', '']
        rows += [f'- [{PurePosixPath(path).name}](../{path})' for path in sorted(models, key=str.casefold)]
    rows.append('')
    return '\n'.join(rows)


def history_document(previous, changes, checked_at):
    rows = [previous.rstrip() if previous else '# 上游同步记录', '', f'## {checked_at}', '',
            '| 来源 | 原提交 | 新提交 | 新增 | 内容修改 | 删除 | 模式变化 |',
            '| --- | --- | --- | ---: | ---: | ---: | ---: |']
    for item in changes:
        if item['updated']:
            url = 'https://github.com/' + item['repository']
            rows.append(f"| {item['name']} | `{item['old_commit'][:12]}` | "
                        f"[`{item['new_commit'][:12]}`]({url}/commit/{item['new_commit']}) | "
                        f"{item['added']} | {item['modified']} | {item['deleted']} | {item['mode_changed']} |")
    return '\n'.join(rows) + '\n'


def git(root, arguments, data=None):
    result = subprocess.run(['git', '-C', str(root), *arguments], input=data, capture_output=True,
                            env=dict(os.environ, GIT_LITERAL_PATHSPECS='1'), timeout=60)
    if result.returncode:
        raise SyncError('Git operation failed: ' + result.stderr.decode('utf-8', 'replace')[:500])
    return result.stdout


def remove_empty_parents(path, boundary):
    while path != boundary and boundary in path.parents:
        try:
            path.rmdir()
        except OSError:
            break
        path = path.parent


def apply_updates(root, original_bytes, old_manifest, new_manifest, prepared, changes, stage):
    # Everything needed for rollback is read before the first mutation.
    touched = {'sources.lock.json', 'docs/upstream-status.md', 'docs/upstream-sync-history.md',
               'docs/model-catalog.md', 'baselines/README.md', 'README.md'}
    for item in changes:
        if item['updated']:
            touched.update(item['changed_files'])
    backups = {}
    for value in touched:
        path = local_path(root, value)
        backups[value] = (path.read_bytes(), stat.S_IMODE(path.stat().st_mode)) if path.is_file() else None
    index_path = None
    index_backup = None
    if stage:
        index_path = Path(git(root, ['rev-parse', '--git-path', 'index']).decode().strip())
        if not index_path.is_absolute():
            index_path = root / index_path
        index_backup = index_path.read_bytes() if index_path.exists() else None
    old_by_name = {source['name']: source for source in old_manifest['sources']}
    try:
        for source in new_manifest['sources']:
            if source['name'] not in prepared:
                continue
            old = old_by_name[source['name']]
            new_paths = {entry['path'] for entry in source['files']}
            boundary = local_path(root, source['local_directory'])
            for entry in old['files']:
                if entry['path'] not in new_paths:
                    path = local_path(root, entry['path'])
                    path.unlink()
                    remove_empty_parents(path.parent, boundary)
            source_files = {entry['path']: entry for entry in source['files']}
            for value in next(item for item in changes if item['name'] == source['name'])['changed_files']:
                if value not in source_files:
                    continue
                path = local_path(root, value)
                relative = value[len(source['local_directory']) + 1:]
                data = prepared[source['name']].joinpath(*safe_parts(relative)).read_bytes()
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
                if os.name != 'nt':
                    path.chmod(0o755 if source_files[value]['mode'] == '100755' else 0o644)
        now = new_manifest['last_synced_at_utc']
        status = local_path(root, 'docs/upstream-status.md')
        status.parent.mkdir(parents=True, exist_ok=True)
        status.write_text(status_document(new_manifest, changes, now), encoding='utf-8', newline='\n')
        history = local_path(root, 'docs/upstream-sync-history.md')
        previous = backups['docs/upstream-sync-history.md']
        history.write_text(history_document(previous[0].decode('utf-8') if previous else '', changes, now),
                           encoding='utf-8', newline='\n')
        local_path(root, 'docs/model-catalog.md').write_text(render_catalog(root, new_manifest),
                                                         encoding='utf-8', newline='\n')
        index = local_path(root, 'baselines/README.md')
        index.parent.mkdir(parents=True, exist_ok=True)
        index.write_text(render_baselines_index(), encoding='utf-8', newline='\n')
        homepage_backup = backups['README.md']
        if homepage_backup:
            local_path(root, 'README.md').write_bytes(render_homepage(
                root, new_manifest, homepage_backup[0].decode('utf-8')).encode('utf-8'))
        local_path(root, 'sources.lock.json').write_text(
            json.dumps(new_manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
        check_local(root, new_manifest)
        if stage:
            # Only generated files pass through git-add. Upstream files use raw
            # blobs so ignored paths and executable modes survive, and upstream
            # .gitattributes cannot invoke clean filters or change source bytes.
            generated = ['sources.lock.json', 'docs/upstream-status.md', 'docs/upstream-sync-history.md',
                         'docs/model-catalog.md', 'baselines/README.md']
            if local_path(root, 'README.md').is_file():
                generated.append('README.md')
            git(root, ['add', '-f', '-A', '--pathspec-from-file=-', '--pathspec-file-nul'],
                b'\0'.join(path.encode('utf-8') for path in generated) + b'\0')
            entries = []
            for source in new_manifest['sources']:
                if source['name'] not in prepared:
                    continue
                new_paths = {entry['path'] for entry in source['files']}
                for entry in old_by_name[source['name']]['files']:
                    if entry['path'] not in new_paths:
                        entries.append(('0 ' + '0' * 40 + '\t' + entry['path']).encode('utf-8'))
            for source in new_manifest['sources']:
                if source['name'] not in prepared:
                    continue
                for entry in source['files']:
                    data = local_path(root, entry['path']).read_bytes()
                    sha = git(root, ['hash-object', '-w', '--stdin'], data).decode().strip()
                    if sha != entry['git_blob_sha1']:
                        raise SyncError('Git raw blob mismatch: ' + entry['path'])
                    entries.append((entry['mode'] + ' ' + sha + '\t' + entry['path']).encode('utf-8'))
            if entries:
                git(root, ['update-index', '-z', '--index-info'], b'\0'.join(entries) + b'\0')
    except Exception:
        # Delete newly introduced files first, so file/directory transitions restore cleanly.
        for value in sorted(touched, key=lambda value: value.count('/'), reverse=True):
            path = local_path(root, value)
            if path.is_file():
                path.unlink()
                remove_empty_parents(path.parent, root)
        for value, backup in backups.items():
            if backup is not None:
                path = local_path(root, value)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(backup[0])
                if os.name != 'nt':
                    path.chmod(backup[1])
        if index_path is not None:
            if index_backup is None:
                index_path.unlink(missing_ok=True)
            else:
                index_path.write_bytes(index_backup)
        raise


def synchronize(args):
    root = args.root.resolve()
    lock_path = local_path(root, 'sources.lock.json')
    original_bytes = lock_path.read_bytes()
    manifest = json.loads(original_bytes)
    validate_manifest(manifest)
    check_local(root, manifest)
    if args.stage:
        git(root, ['rev-parse', '--show-toplevel'])
        for source in manifest['sources']:
            if git(root, ['diff', '--cached', '--name-only', '-z', '--', source['local_directory']]):
                raise SyncError('Source directory has staged changes: ' + source['local_directory'], 'conflict')
    client = GitHub(os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN'))
    updated_manifest = copy.deepcopy(manifest)
    changes = []
    prepared = {}
    checked_at = utc_now()
    # Read-only checks never create a temporary directory or download archives.
    temporary = None if args.check else tempfile.TemporaryDirectory(prefix='zpb-upstream-sync-')
    try:
        for index, source in enumerate(manifest['sources']):
            repo = client.api('/repos/' + source['repository'])
            branch = repo['default_branch']
            ref = client.api('/repos/' + source['repository'] + '/git/ref/heads/' + urllib.parse.quote(branch, safe=''))
            commit = ref['object']['sha']
            if not re.fullmatch(r'[0-9a-f]{40}', commit):
                raise SyncError('Invalid upstream commit: ' + source['name'])
            if commit == source['commit']:
                changes.append(describe_change(source, commit, branch, source['files']))
                continue
            tree = client.api('/repos/' + source['repository'] + '/git/trees/' + commit + '?recursive=1')
            files, gitlinks = prepare_tree(source, tree)
            changes.append(describe_change(source, commit, branch, files))
            if args.check:
                continue
            destination = Path(temporary.name) / str(index)
            destination.mkdir()
            archive_url = 'https://codeload.github.com/' + source['repository'] + '/tar.gz/' + commit
            content = client.read(archive_url, authenticated=False)
            lfs = unpack_archive(content, source, files, destination)
            new_source = updated_manifest['sources'][index]
            new_source.update(commit=commit, last_synced_branch=branch,
                              snapshot_url=source['url'] + '/tree/' + commit,
                              archive_url=archive_url, archive_sha256=hashlib.sha256(content).hexdigest(),
                              files=files, file_count=len(files), gitlinks=gitlinks, lfs_pointers=lfs,
                              last_synced_at_utc=checked_at)
            if 'notes' in new_source:
                new_source.setdefault('notes_at_import', copy.deepcopy(new_source['notes']))
                new_source['notes'] = ['Historical import notes are retained in notes_at_import. Current dependency and file state is recorded in gitlinks, lfs_pointers and files.']
            new_source['notice_files'] = [entry['path'] for entry in files
                                          if PurePosixPath(entry['path']).name.upper().startswith('NOTICE')]
            prepared[source['name']] = destination
        changed = any(item['updated'] for item in changes)
        report = {'status': 'updates_available' if args.check and changed else 'up_to_date',
                  'changed': changed, 'checked_at_utc': checked_at, 'check_only': args.check,
                  'source_count': len(changes), 'original_file_count': sum(item['file_count'] for item in changes),
                  'changed_file_count': sum(item['changed_file_count'] for item in changes), 'sources': changes}
        if changed and not args.check:
            # A user edit during downloads must be detected before replacement.
            if lock_path.read_bytes() != original_bytes:
                raise SyncError('Source lock changed during preparation; no update applied', 'conflict')
            check_local(root, manifest)
            updated_manifest.update(source_count=len(updated_manifest['sources']),
                                    original_file_count=sum(len(source['files']) for source in updated_manifest['sources']),
                                    last_synced_at_utc=checked_at)
            apply_updates(root, original_bytes, manifest, updated_manifest, prepared, changes, args.stage)
            report['status'] = 'updated'
        return report
    finally:
        if temporary is not None:
            temporary.cleanup()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--check', action='store_true', help='read-only upstream discovery; do not download or stage')
    parser.add_argument('--stage', action='store_true', help='stage synchronized files, exact blobs and Git modes')
    parser.add_argument('--output-json', metavar='PATH', help='write JSON report; use - for JSON on stdout')
    args = parser.parse_args()
    if args.check and (args.stage or args.output_json not in (None, '-')):
        parser.error('--check cannot stage or write a report file; use --output-json -')
    try:
        report = synchronize(args)
        exit_code = 0
    except (SyncError, OSError, ValueError, KeyError, TypeError, tarfile.TarError, subprocess.SubprocessError) as error:
        report = {'status': getattr(error, 'status', 'error'), 'changed': False,
                  'check_only': args.check, 'error': str(error)}
        exit_code = 2
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
    if args.output_json and args.output_json != '-':
        destination = Path(args.output_json)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(encoded, encoding='utf-8', newline='\n')
    if args.output_json == '-':
        print(encoded, end='')
    else:
        print(report['status'] + (': ' + report['error'] if 'error' in report else
              f"; {report['source_count']} sources; {report['changed_file_count']} changed files"))
    return exit_code


if __name__ == '__main__':
    sys.exit(main())
