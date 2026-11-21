"""Read the complete local model registry without importing model dependencies."""

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
from typing import Optional


def repository_root(root: Optional[Path] = None) -> Path:
    return Path(root).resolve() if root is not None else Path(__file__).resolve().parents[1]


def _inventory(root: Optional[Path] = None):
    resolved = repository_root(root)
    generator_path = resolved / 'tools' / 'build_model_catalog.py'
    lock_path = resolved / 'sources.lock.json'
    if not generator_path.is_file() or not lock_path.is_file():
        raise FileNotFoundError('Model registry requires sources.lock.json and tools/build_model_catalog.py')
    specification = importlib.util.spec_from_file_location('_zpbts_catalog', generator_path)
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    manifest = json.loads(lock_path.read_text(encoding='utf-8'))
    return module.model_inventory(resolved, manifest)


def list_models(category: Optional[str] = None, search: Optional[str] = None,
                root: Optional[Path] = None):
    """List all indexed families, regardless of runnable adapter availability."""
    inventory = _inventory(root)
    titles = {item['id']: item['title'] for item in inventory['categories']}
    query = search.casefold() if search else None
    selected_category = category.casefold() if category else None
    result = []
    for name, family in sorted(inventory['families'].items(), key=lambda item: item[0].casefold()):
        title = titles.get(family['category'], family['category'])
        if selected_category and selected_category not in (family['category'].casefold(), title.casefold()):
            continue
        aliases = family['info'].get('aliases', [])
        searchable = ' '.join([name, family['category'], title, family['info'].get('summary', ''), *aliases])
        if query and query not in searchable.casefold():
            continue
        result.append({'name': name, 'category': family['category'], 'category_title': title,
                       'directory': family['directory'], 'info': deepcopy(family['info']),
                       'implementations': deepcopy(family['implementations'])})
    return result


def get_model(name: str, root: Optional[Path] = None):
    """Return one complete family; accept a unique case-insensitive name/alias."""
    inventory = _inventory(root)
    families = inventory['families']
    canonical = name if name in families else None
    if canonical is None:
        query = name.casefold()
        candidates = [candidate for candidate, family in families.items()
                      if query == candidate.casefold()
                      or query in {alias.casefold() for alias in family['info'].get('aliases', [])}]
        if len(candidates) == 1:
            canonical = candidates[0]
        elif len(candidates) > 1:
            raise ValueError('Ambiguous model alias: ' + name + '; use ' + ', '.join(candidates))
    if canonical is None:
        raise KeyError('Unknown model: ' + name)
    family = deepcopy(families[canonical])
    family['name'] = canonical
    return family


def list_categories(root: Optional[Path] = None):
    inventory = _inventory(root)
    result = []
    for category in inventory['categories']:
        count = sum(family['category'] == category['id'] for family in inventory['families'].values())
        if count:
            result.append({**category, 'model_count': count})
    return result
