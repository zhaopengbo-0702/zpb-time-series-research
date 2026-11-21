#!/usr/bin/env python3
"""Offline behavior tests for upstream synchronization (standard library only)."""

import argparse
import contextlib
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tarfile
import tempfile
import unittest
from unittest import mock

import sync_upstreams as sync
import build_model_catalog as catalog_builder


def blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()


def commit_sha(label):
    return hashlib.sha1(label.encode('ascii')).hexdigest()


def archive_bytes(files, extra=None):
    stream = io.BytesIO()
    with tarfile.open(fileobj=stream, mode='w:gz') as archive:
        for path, (content, mode) in files.items():
            member = tarfile.TarInfo('snapshot/' + path)
            member.size = len(content)
            member.mode = 0o755 if mode == '100755' else 0o644
            archive.addfile(member, io.BytesIO(content))
        if extra:
            member = tarfile.TarInfo(extra)
            member.size = 6
            archive.addfile(member, io.BytesIO(b'escape'))
    return stream.getvalue()


class FakeGitHub:
    """Only serves fixture metadata and tarballs; never touches the network."""

    def __init__(self, manifest, updates=None):
        self.sources = {source['repository']: source for source in manifest['sources']}
        self.updates = updates or {}
        self.api_calls = []
        self.downloads = []

    def api(self, endpoint):
        self.api_calls.append(endpoint)
        for repository, source in self.sources.items():
            prefix = '/repos/' + repository
            update = self.updates.get(source['name'])
            if endpoint == prefix:
                return {'default_branch': 'main'}
            if endpoint == prefix + '/git/ref/heads/main':
                return {'object': {'sha': update['commit'] if update else source['commit']}}
            if update and endpoint == prefix + '/git/trees/' + update['commit'] + '?recursive=1':
                return {'truncated': False, 'tree': [
                    {'path': path, 'type': 'blob', 'mode': mode, 'sha': blob_sha(data), 'size': len(data)}
                    for path, (data, mode) in update['files'].items()
                ]}
        raise AssertionError('Unexpected API request: ' + endpoint)

    def read(self, url, authenticated=True):
        self.downloads.append((url, authenticated))
        for repository, source in self.sources.items():
            update = self.updates.get(source['name'])
            if update and url == 'https://codeload.github.com/' + repository + '/tar.gz/' + update['commit']:
                if update.get('download_error'):
                    raise sync.SyncError('Fixture download failed')
                return update.get('archive', archive_bytes(update['files']))
        raise AssertionError('Unexpected archive request: ' + url)


class SynchronizationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='zpb-sync-test-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.original_files = {}
        self.manifest = {'schema_version': 1, 'source_count': 7, 'original_file_count': 28, 'sources': []}
        for index in range(7):
            name = 'Source' + str(index)
            prefix = ('libraries/' if index == 6 else 'baselines/') + name
            files = {
                'LICENSE': (b'Fixture license; retained unchanged.\n', '100644'),
                'model.py': (b'value = 1\r\n', '100644'),
                'old.txt': (b'obsolete\n', '100644'),
                'run.sh': (b'#!/bin/sh\nexit 0\n', '100644'),
            }
            source = {'name': name, 'repository': 'fixture/' + name, 'url': 'https://github.com/fixture/' + name,
                      'local_directory': prefix, 'commit': commit_sha(name + '-old'),
                      'default_branch_at_import': 'main', 'gitlinks': [], 'files': []}
            for relative, (data, mode) in files.items():
                path = prefix + '/' + relative
                target = self.root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                source['files'].append({'path': path, 'git_blob_sha1': blob_sha(data),
                                        'mode': mode, 'size_bytes': len(data)})
            self.original_files[name] = files
            self.manifest['sources'].append(source)
        (self.root / 'sources.lock.json').write_text(json.dumps(self.manifest, indent=2) + '\n', encoding='utf-8')
        for relative, data in {
            '.gitignore': b'*.bin\n', '.gitattributes': b'* -text\n',
            'research/notes/my-idea.md': b'Personal research stays intact.\n',
            'experiments/run-001.md': b'Original experiment record.\n',
            'docs/upstream-status.md': b'# Initial status\n',
            'docs/upstream-sync-history.md': b'# Initial history\n',
        }.items():
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Offline Test')
        self.git('config', 'user.email', 'offline@example.invalid')
        self.git('config', 'core.autocrlf', 'false')
        self.git('config', 'core.filemode', 'false')
        self.git('add', '-f', '.')
        self.git('commit', '-q', '-m', 'Fixture snapshot')

    def git(self, *arguments):
        result = subprocess.run(['git', '-C', str(self.root), *arguments], capture_output=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr.decode('utf-8', 'replace'))
        return result.stdout

    def snapshot(self):
        return {path.relative_to(self.root).as_posix(): path.read_bytes()
                for path in self.root.rglob('*') if path.is_file()
                and '.git' not in path.relative_to(self.root).parts}

    def args(self, **overrides):
        values = dict(root=self.root, check=False, stage=False, output_json=None)
        values.update(overrides)
        return argparse.Namespace(**values)

    def update(self, index=0):
        name = 'Source' + str(index)
        files = copy.deepcopy(self.original_files[name])
        files['model.py'] = (b'value = 2\n', '100644')
        files.pop('old.txt')
        files['cache/generated.bin'] = (b'\x00\xffverified upstream bytes\r\n', '100644')
        files['run.sh'] = (files['run.sh'][0], '100755')
        return {'commit': commit_sha(name + '-new'), 'files': files}

    def invoke(self, updates=None, **options):
        client = FakeGitHub(self.manifest, updates)
        with mock.patch.object(sync, 'GitHub', return_value=client):
            report = sync.synchronize(self.args(**options))
        return report, client

    def assert_unchanged(self, before, index):
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.git('ls-files', '--stage', '-z'), index)

    def test_update_preserves_raw_bytes_deletes_old_files_and_stages_ignored_file_and_mode(self):
        before = self.snapshot()
        update = self.update()
        report, client = self.invoke({'Source0': update}, stage=True)
        prefix = 'baselines/Source0/'
        self.assertEqual(report['status'], 'updated')
        self.assertEqual(report['source_count'], 7)
        self.assertEqual(len(client.downloads), 1)
        self.assertFalse((self.root / prefix / 'old.txt').exists())
        for relative, (data, mode) in update['files'].items():
            path = prefix + relative
            self.assertEqual((self.root / path).read_bytes(), data)
            self.assertEqual(self.git('show', ':' + path), data)
            staged = self.git('ls-files', '--stage', '--', path).decode().split()
            self.assertEqual(staged[0], mode)
            self.assertEqual(staged[1], blob_sha(data))
        self.assertEqual(self.git('check-ignore', '--no-index', prefix + 'cache/generated.bin').strip(),
                         (prefix + 'cache/generated.bin').encode())
        lock = json.loads((self.root / 'sources.lock.json').read_text(encoding='utf-8'))
        self.assertEqual(lock['sources'][0]['commit'], update['commit'])
        self.assertEqual(lock['original_file_count'], 28)
        self.assertIn(update['commit'][:12], (self.root / 'docs/upstream-status.md').read_text(encoding='utf-8'))
        self.assertIn(update['commit'][:12], (self.root / 'docs/upstream-sync-history.md').read_text(encoding='utf-8'))
        for path, data in before.items():
            if not path.startswith(prefix) and path not in {'sources.lock.json', 'docs/upstream-status.md', 'docs/upstream-sync-history.md'}:
                self.assertEqual((self.root / path).read_bytes(), data, path)
        source = report['sources'][0]
        self.assertEqual((source['added'], source['deleted'], source['modified'], source['mode_changed']), (1, 1, 1, 1))

    def test_no_change_makes_no_files_or_git_diff(self):
        before, index = self.snapshot(), self.git('ls-files', '--stage', '-z')
        report, client = self.invoke(stage=True)
        self.assertEqual(report['status'], 'up_to_date')
        self.assertFalse(report['changed'])
        self.assertEqual(client.downloads, [])
        self.assertFalse(any('/git/trees/' in call for call in client.api_calls))
        self.assert_unchanged(before, index)
        self.assertEqual(self.git('status', '--porcelain'), b'')

    def test_modified_or_additional_local_source_file_refuses_without_network_or_overwrite(self):
        for kind in ('modified', 'additional'):
            with self.subTest(kind=kind):
                path = self.root / ('baselines/Source0/model.py' if kind == 'modified' else 'baselines/Source0/private-notes.txt')
                original = path.read_bytes() if path.exists() else None
                path.write_bytes(b'My uncommitted work\n')
                before, index = self.snapshot(), self.git('ls-files', '--stage', '-z')
                with mock.patch.object(sync, 'GitHub') as client_class:
                    with self.assertRaises(sync.SyncError) as caught:
                        sync.synchronize(self.args(stage=True))
                    self.assertEqual(caught.exception.status, 'conflict')
                    client_class.assert_not_called()
                self.assert_unchanged(before, index)
                if original is None:
                    path.unlink()
                else:
                    path.write_bytes(original)

    def test_second_source_download_or_hash_failure_leaves_all_seven_sources_unchanged(self):
        for failure in ('download', 'hash'):
            with self.subTest(failure=failure):
                updates = {'Source' + str(i): self.update(i) for i in range(7)}
                if failure == 'download':
                    updates['Source1']['download_error'] = True
                else:
                    corrupt = copy.deepcopy(updates['Source1']['files'])
                    corrupt['model.py'] = (b'corrupt bytes\n', '100644')
                    updates['Source1']['archive'] = archive_bytes(corrupt)
                before, index = self.snapshot(), self.git('ls-files', '--stage', '-z')
                with self.assertRaises(sync.SyncError):
                    self.invoke(updates, stage=True)
                self.assert_unchanged(before, index)

    def test_archive_traversal_is_rejected_before_import(self):
        update = self.update()
        update['archive'] = archive_bytes(update['files'], extra='snapshot/../escaped.txt')
        before, index = self.snapshot(), self.git('ls-files', '--stage', '-z')
        with self.assertRaises(sync.SyncError):
            self.invoke({'Source0': update}, stage=True)
        self.assert_unchanged(before, index)
        self.assertFalse((self.root / 'escaped.txt').exists())

    def test_license_change_requires_review_without_import(self):
        update = self.update()
        update['files']['LICENSE'] = (b'Different license terms\n', '100644')
        before, index = self.snapshot(), self.git('ls-files', '--stage', '-z')
        client = FakeGitHub(self.manifest, {'Source0': update})
        with mock.patch.object(sync, 'GitHub', return_value=client):
            with self.assertRaises(sync.SyncError) as caught:
                sync.synchronize(self.args(stage=True))
        self.assertEqual(caught.exception.status, 'needs_review')
        self.assertEqual(client.downloads, [])
        self.assert_unchanged(before, index)

    def test_check_discovers_changes_without_archive_tempdir_or_writes(self):
        before, index = self.snapshot(), self.git('ls-files', '--stage', '-z')
        with mock.patch.object(sync.tempfile, 'TemporaryDirectory', side_effect=AssertionError('check created tempdir')):
            report, client = self.invoke({'Source0': self.update()}, check=True)
        self.assertEqual(report['status'], 'updates_available')
        self.assertTrue(report['changed'])
        self.assertEqual(report['source_count'], 7)
        self.assertEqual(client.downloads, [])
        self.assert_unchanged(before, index)

    def test_check_cli_rejects_report_path_without_creating_file(self):
        path = self.root / 'forbidden-report.json'
        with mock.patch.object(sys, 'argv', ['sync_upstreams.py', '--root', str(self.root), '--check', '--output-json', str(path)]):
            with contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as caught:
                    sync.main()
        self.assertEqual(caught.exception.code, 2)
        self.assertFalse(path.exists())

    def test_staged_personal_source_change_is_preserved_when_worktree_matches_lock(self):
        path = self.root / 'baselines/Source0/model.py'
        original = path.read_bytes()
        path.write_bytes(b'Personal staged model\n')
        self.git('add', '--', 'baselines/Source0/model.py')
        path.write_bytes(original)
        before, index = self.snapshot(), self.git('ls-files', '--stage', '-z')
        with self.assertRaises(sync.SyncError) as caught:
            self.invoke({'Source0': self.update()}, stage=True)
        self.assertEqual(caught.exception.status, 'conflict')
        self.assert_unchanged(before, index)
        self.assertEqual(self.git('show', ':baselines/Source0/model.py'), b'Personal staged model\n')

    def test_upstream_file_directory_transitions_are_imported_and_staged(self):
        first = self.update()
        content, mode = first['files'].pop('old.txt', (b'new nested file\n', '100644'))
        first['files']['old.txt/nested.py'] = (content, mode)
        first['files'].pop('run.sh')
        first['files']['run.sh/nested.py'] = (b'nested = 1\n', '100644')
        report, _ = self.invoke({'Source0': first}, stage=True)
        self.assertEqual(report['status'], 'updated')
        self.assertEqual(self.git('show', ':baselines/Source0/old.txt/nested.py'), content)
        self.git('commit', '-q', '-m', 'File to directory transition')
        self.manifest = json.loads((self.root / 'sources.lock.json').read_text(encoding='utf-8'))
        second_files = copy.deepcopy(first['files'])
        second_files.pop('old.txt/nested.py')
        second_files.pop('run.sh/nested.py')
        second_files['old.txt'] = (b'File restored\n', '100644')
        second_files['run.sh'] = (b'#!/bin/sh\nexit 1\n', '100755')
        second = {'commit': commit_sha('Source0-newer'), 'files': second_files}
        report, _ = self.invoke({'Source0': second}, stage=True)
        self.assertEqual(report['status'], 'updated')
        self.assertEqual(self.git('show', ':baselines/Source0/old.txt'), b'File restored\n')
        self.assertEqual(self.git('ls-files', '--stage', '--', 'baselines/Source0/run.sh').split()[0], b'100755')
        self.assertFalse((self.root / 'baselines/Source0/old.txt/nested.py').exists())

    def test_new_library_model_is_automatically_cataloged_and_staged_without_metadata(self):
        self.manifest['sources'][6]['name'] = 'Time-Series-Library'
        (self.root / 'sources.lock.json').write_text(json.dumps(self.manifest, indent=2) + '\n', encoding='utf-8')
        homepage_prefix = '# My research homepage\n\nPersonal introduction stays.\n\n'
        homepage_suffix = '\n\nMy custom experiment links stay.\n'
        (self.root / 'README.md').write_text(
            homepage_prefix + '<!-- MODEL_CATALOG_START -->\nOld catalog.\n<!-- MODEL_CATALOG_END -->' + homepage_suffix,
            encoding='utf-8')
        self.git('add', '--', 'sources.lock.json', 'README.md')
        self.git('commit', '-q', '-m', 'Identify the library fixture')
        update = self.update(6)
        update['files']['models/NewModel.py'] = (b'class Model:\n    pass\n', '100644')
        update['files']['models/__init__.py'] = (b'', '100644')
        report, _ = self.invoke({'Time-Series-Library': update}, stage=True)
        self.assertEqual(report['status'], 'updated')
        catalog = (self.root / 'docs/model-catalog.md').read_text(encoding='utf-8')
        self.assertIn('| NewModel |', catalog)
        self.assertIn('../libraries/Source6/models/NewModel.py', catalog)
        self.assertIn('待分类', catalog)
        self.assertNotIn('| __init__ |', catalog)
        self.assertEqual(self.git('show', ':docs/model-catalog.md'), catalog.encode('utf-8'))
        self.assertIn(b'docs/model-catalog.md', self.git('show', ':baselines/README.md'))
        homepage = (self.root / 'README.md').read_text(encoding='utf-8')
        self.assertTrue(homepage.startswith(homepage_prefix))
        self.assertTrue(homepage.endswith(homepage_suffix))
        self.assertIn('NewModel', homepage)
        self.assertIn('待分类', homepage)
        self.assertIn('libraries/Source6/models/NewModel.py', homepage)
        self.assertNotIn('Old catalog.', homepage)
        self.assertEqual(self.git('show', ':README.md'), (self.root / 'README.md').read_bytes())

    def test_sync_without_homepage_does_not_create_it(self):
        self.assertFalse((self.root / 'README.md').exists())
        report, _ = self.invoke({'Source0': self.update()}, stage=True)
        self.assertEqual(report['status'], 'updated')
        self.assertFalse((self.root / 'README.md').exists())
        self.assertEqual(self.git('ls-files', '--', 'README.md'), b'')

    def test_homepage_without_catalog_markers_is_not_rewritten(self):
        original = b'# Custom homepage\r\n\r\nKeep the exact bytes.\r\n'
        (self.root / 'README.md').write_bytes(original)
        self.git('add', '--', 'README.md')
        self.git('commit', '-q', '-m', 'Custom homepage without generated section')
        report, _ = self.invoke({'Source0': self.update()}, stage=True)
        self.assertEqual(report['status'], 'updated')
        self.assertEqual((self.root / 'README.md').read_bytes(), original)
        self.assertEqual(self.git('show', ':README.md'), original)
        self.assertNotIn('README.md', self.git('diff', '--cached', '--name-only').decode().splitlines())

    def test_homepage_details_give_independent_and_library_models_equal_rows(self):
        def source(name, directory, paths):
            return {'name': name, 'local_directory': directory, 'url': 'https://github.com/fixture/' + name, 'files': [
                {'path': directory + '/' + path} for path in paths]}

        manifest = {'sources': [
            source('EMAformer', 'baselines/EMAformer', ['model/EMAformer.py', 'run.py']),
            source('Time-LLM', 'baselines/Time-LLM', ['models/TimeLLM.py', 'run_main.py']),
            source('Time-Series-Library', 'libraries/Time-Series-Library', [
                'models/Autoformer.py', 'models/KANAD.py', 'models/EMAformer.py', 'models/__init__.py',
                'run.py', 'scripts/long_term_forecast/ETT_script/Autoformer_ETTh1.sh',
                'scripts/anomaly_detection/PSM/KANAD.sh']),
        ]}
        metadata = {
            'categories': [
                {'id': 'embedding', 'title': '嵌入增强'},
                {'id': 'decomposition', 'title': '分解建模'},
                {'id': 'language', 'title': '语言模型'},
                {'id': 'anomaly', 'title': '异常检测'},
            ],
            'models': {
                'EMAformer': {'category': 'embedding', 'summary': 'Channel and phase embeddings.'},
                'Autoformer': {'category': 'decomposition', 'summary': 'Decomposition and autocorrelation.'},
                'Time-LLM': {'category': 'language', 'summary': 'Language model reprogramming.'},
                'KANAD': {'category': 'anomaly', 'summary': 'Anomaly detector.'},
            },
        }
        metadata_path = self.root / 'tools/model_categories.json'
        metadata_path.parent.mkdir(parents=True, exist_ok=True)
        metadata_path.write_text(json.dumps(metadata, ensure_ascii=False), encoding='utf-8')
        details = catalog_builder.render_homepage_details(self.root, manifest)
        rows = [line for line in details.splitlines() if line.startswith('| ') and not re.match(r'^\|\s*:?-', line)]
        model_rows = {}
        for name in ('EMAformer', 'Time-LLM', 'Autoformer', 'KANAD'):
            matches = [line for line in rows if line.split('|')[1].strip() == name]
            self.assertEqual(len(matches), 1, (name, details))
            model_rows[name] = matches[0]
        self.assertEqual(len(rows), 5, details)  # One header, four peer model rows.
        self.assertEqual(len({len(re.split(r'(?<!\\)\|', line)) for line in rows}), 1, details)
        self.assertNotIn('__init__', details)
        self.assertIn('baselines/EMAformer/model/EMAformer.py', model_rows['EMAformer'])
        self.assertIn('libraries/Time-Series-Library/models/EMAformer.py', model_rows['EMAformer'])
        self.assertIn('baselines/Time-LLM/models/TimeLLM.py', model_rows['Time-LLM'])
        self.assertIn('libraries/Time-Series-Library/models/Autoformer.py', model_rows['Autoformer'])
        self.assertIn('libraries/Time-Series-Library/models/KANAD.py', model_rows['KANAD'])

    def test_new_upstream_model_updates_homepage_details_and_keeps_custom_text(self):
        self.manifest['sources'][6]['name'] = 'Time-Series-Library'
        (self.root / 'sources.lock.json').write_text(json.dumps(self.manifest, indent=2) + '\n', encoding='utf-8')
        before_details = '# Personal page\n\nMy motivation stays.\n\n<!-- MODEL_DETAILS_START -->'
        after_details = '<!-- MODEL_DETAILS_END -->\n\nMy experiment links stay.\n'
        (self.root / 'README.md').write_text(before_details + '\nOutdated details.\n' + after_details, encoding='utf-8')
        self.git('add', '--', 'sources.lock.json', 'README.md')
        self.git('commit', '-q', '-m', 'Homepage details fixture')
        update = self.update(6)
        update['files']['models/NewPeerModel.py'] = (b'class Model:\n    pass\n', '100644')
        report, _ = self.invoke({'Time-Series-Library': update}, stage=True)
        self.assertEqual(report['status'], 'updated')
        homepage = (self.root / 'README.md').read_text(encoding='utf-8')
        self.assertTrue(homepage.startswith(before_details))
        self.assertTrue(homepage.endswith(after_details))
        self.assertIn('| NewPeerModel |', homepage)
        self.assertIn('libraries/Source6/models/NewPeerModel.py', homepage)
        self.assertIn('方法说明待补充', homepage)
        self.assertNotIn('Outdated details.', homepage)
        self.assertEqual(self.git('show', ':README.md'), (self.root / 'README.md').read_bytes())

    @unittest.skipIf(os.name == 'nt', 'Windows does not expose POSIX executable bits')
    def test_local_executable_mode_change_is_a_conflict(self):
        path = self.root / 'baselines/Source0/run.sh'
        path.chmod(0o755)
        before, index = self.snapshot(), self.git('ls-files', '--stage', '-z')
        with self.assertRaises(sync.SyncError) as caught:
            self.invoke({'Source0': self.update()}, stage=True)
        self.assertEqual(caught.exception.status, 'conflict')
        self.assert_unchanged(before, index)
        self.assertTrue(path.stat().st_mode & 0o100)


if __name__ == '__main__':
    unittest.main(verbosity=2)
