#!/usr/bin/env python3
"""Verify original source bytes against sources.lock.json (standard library only)."""

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import sys


def repository_path(root, value):
    """Reject lock paths outside this repository rather than following them."""
    relative = PurePosixPath(value)
    if relative.is_absolute() or '..' in relative.parts or '\\' in value:
        raise ValueError('Unsafe path in source lock: ' + value)
    target = root.joinpath(*relative.parts)
    resolved_root = root.resolve()
    resolved_target = target.resolve()
    if resolved_root != resolved_target and resolved_root not in resolved_target.parents:
        raise ValueError('Path escapes repository: ' + value)
    return target


def git_blob_sha1(content):
    return hashlib.sha1(b'blob ' + str(len(content)).encode('ascii') + b'\0' + content).hexdigest()


def extended_root(value):
    root = value.resolve()
    if os.name == 'nt' and not str(root).startswith('\\\\?\\'):
        text = str(root)
        return Path('\\\\?\\UNC\\' + text[2:] if text.startswith('\\\\') else '\\\\?\\' + text)
    return root


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1],
                        help='repository directory (default: parent of tools/)')
    parser.add_argument('--strict', action='store_true',
                        help='also fail when unlisted files exist inside an imported source directory')
    args = parser.parse_args()
    root = extended_root(args.root)
    try:
        manifest = json.loads((root / 'sources.lock.json').read_text(encoding='utf-8'))
        if manifest['schema_version'] != 1:
            raise ValueError('Unsupported sources.lock.json schema version')
        checked = 0
        missing = []
        changed = []
        extra = []
        omitted = []
        for source in manifest['sources']:
            expected = set()
            source_directory = repository_path(root, source['local_directory'])
            for entry in source['files']:
                path = repository_path(root, entry['path'])
                if source_directory not in path.parents:
                    raise ValueError('File is outside its imported source directory: ' + entry['path'])
                if entry['path'] in expected:
                    raise ValueError('Duplicate locked path: ' + entry['path'])
                expected.add(entry['path'])
                if not path.is_file():
                    missing.append(entry['path'])
                    continue
                if path.is_symlink():
                    raise ValueError('Unexpected symbolic link: ' + entry['path'])
                content = path.read_bytes()
                checked += 1
                if len(content) != entry['size_bytes'] or git_blob_sha1(content) != entry['git_blob_sha1']:
                    changed.append(entry['path'])
            actual = {p.relative_to(root).as_posix() for p in source_directory.rglob('*') if p.is_file()}
            source_extra = sorted(actual - expected)
            extra.extend(source_extra)
            omitted.extend(source.get('gitlinks', []))
            source_changed = sum(value.startswith(source['local_directory'] + '/') for value in changed)
            source_missing = sum(value.startswith(source['local_directory'] + '/') for value in missing)
            print('{}: {} locked files; {} changed, {} missing, {} extra'.format(
                source['name'], len(expected), source_changed, source_missing, len(source_extra)))
        for label, paths in [('MISSING', missing), ('CHANGED', changed), ('EXTRA', extra)]:
            for path in paths:
                print('{} {}'.format(label, path))
        for dependency in omitted:
            print('OPTIONAL GITLINK {} @ {}: {}'.format(
                dependency['path'], dependency['commit'], dependency['status']))
        failed = bool(missing or changed or (args.strict and extra))
        print('{}: {} original files read. Git modes are recorded in the lock; filesystem executable bits are not checked.'.format(
            'FAIL' if failed else 'PASS', checked))
        if extra and not args.strict:
            print('Additional source files are listed above; use --strict to treat them as failures.')
        return 1 if failed else 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print('ERROR: {}'.format(error), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
