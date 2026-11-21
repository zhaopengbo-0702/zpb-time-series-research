"""Command line interface for the model index and experiment runners."""

import argparse
import json
from pathlib import Path
import sys

from .registry import get_model, list_models


def build_parser():
    parser = argparse.ArgumentParser(prog='zpbts', description='Browse indexed models and run supported experiments.')
    commands = parser.add_subparsers(dest='command', required=True)
    listing = commands.add_parser('list', help='List indexed models; indexing does not imply a runnable adapter.')
    listing.add_argument('--category', help='Category ID or exact category title.')
    listing.add_argument('--search', help='Search model names, aliases, categories and descriptions.')
    listing.add_argument('--json', action='store_true', help='Print the registry entries as JSON.')
    showing = commands.add_parser('show', help='Show a model and all local implementations.')
    showing.add_argument('model', metavar='MODEL')
    showing.add_argument('--json', action='store_true', help='Print the full model record as JSON.')
    running = commands.add_parser('run', help='Run a configured experiment using an available adapter.')
    running.add_argument('config', metavar='CONFIG', type=Path)
    running.add_argument('--output', metavar='DIR', type=Path, required=True)
    comparison = commands.add_parser('compare', help='Compare saved experiment results as Markdown.')
    comparison.add_argument('directories', metavar='DIR', nargs='+', type=Path)
    return parser


def print_json(value):
    print(json.dumps(value, ensure_ascii=False, indent=2, default=str))


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        if args.command == 'list':
            entries = list_models(category=args.category, search=args.search)
            if args.json:
                print_json(entries)
            else:
                print('Model\tCategory\tImplementations\tLocal project')
                for entry in entries:
                    print('{}\t{}\t{}\t{}'.format(entry['name'], entry['category'],
                          len(entry['implementations']), entry['directory']))
                print('{} indexed models. Runnable support depends on the selected adapter.'.format(len(entries)))
        elif args.command == 'show':
            family = get_model(args.model)
            if args.json:
                print_json(family)
            else:
                print(family['name'])
                print('Category: ' + family['category'])
                print('Project: ' + family['directory'])
                if family['info'].get('summary'):
                    print('Summary: ' + family['info']['summary'])
                for index, item in enumerate(family['implementations'], 1):
                    print('\nImplementation ' + str(index))
                    print('  Core: ' + item['core'])
                    if item.get('class_name'):
                        print('  Class: ' + item['class_name'])
                    print('  Entry: ' + item['entry'])
                    print('  Directory: ' + item['directory'])
                    print('  Commit: ' + item['commit'])
                    for path in item.get('extra_cores', []):
                        print('  Additional core: ' + path)
                    for path in item.get('extra_entries', []):
                        print('  Additional entry: ' + path)
        elif args.command == 'run':
            from .experiment import run_experiment
            print_json(run_experiment(Path(args.config), Path(args.output)))
        elif args.command == 'compare':
            from .experiment import compare_results
            print(compare_results([Path(path) for path in args.directories]))
        return 0
    except (KeyError, ValueError, FileNotFoundError, OSError, ImportError, RuntimeError) as error:
        message = str(error.args[0]) if isinstance(error, KeyError) and error.args else str(error)
        print('Error: ' + message, file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
