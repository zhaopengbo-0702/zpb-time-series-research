#!/usr/bin/env python3
"""Build an offline model catalog from pinned sources and public model APIs."""

import argparse
import html
import hashlib
import json
import posixpath
from pathlib import Path, PurePosixPath
import re
from urllib.parse import quote


INDEPENDENT = {
    'EMAformer': ('EMAformer', 'model/EMAformer.py', 'run.py'),
    'Pyraformer': ('Pyraformer', 'pyraformer/Pyraformer_LR.py', 'long_range_main.py'),
    'Informer2020': ('Informer', 'models/model.py', 'main_informer.py'),
    'Autoformer': ('Autoformer', 'models/Autoformer.py', 'run.py'),
    'ETSformer': ('ETSformer', 'models/etsformer/model.py', 'run.py'),
    'Time-LLM': ('Time-LLM', 'models/TimeLLM.py', 'run_main.py'),
}
UNCATEGORIZED = {'id': 'unclassified', 'title': '待分类',
                 'description': '已收录但尚未填写主分类的模型；源码入口保留在这里。'}


def read_json(path, default):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default


def read_profiles(root):
    profiles = {}
    fields = ('intuition', 'mechanism', 'use_cases', 'limitations', 'reading_tip')
    for path in sorted((Path(root) / 'tools/model_profiles').glob('*.json')):
        entries = read_json(path, {})
        for name, profile in entries.items():
            if name in profiles:
                raise ValueError('Duplicate model profile: ' + name)
            if not isinstance(profile, dict) or any(not isinstance(profile.get(field), str)
                                                   or not profile[field].strip() for field in fields):
                raise ValueError('Incomplete model profile: ' + name)
            profiles[name] = profile
    return profiles


def source_path(source, relative):
    if not isinstance(relative, str) or '\\' in relative or relative.startswith('/'):
        raise ValueError('Invalid inventory path: ' + repr(relative))
    parts = PurePosixPath(relative.rstrip('/')).parts
    if not parts or any(part in ('.', '..') for part in parts):
        raise ValueError('Invalid inventory path: ' + relative)
    result = source['local_directory'] + '/' + '/'.join(parts)
    known = {entry['path'] for entry in source['files']}
    if result not in known and not any(path.startswith(result + '/') for path in known):
        raise ValueError('Inventory points outside tracked source: ' + result)
    return result + ('/' if relative.endswith('/') else '')


def default_entry(source):
    known = {entry['path'] for entry in source['files']}
    prefix = source['local_directory'] + '/'
    for relative in ('run.py', 'README.md', 'README.rst', 'README.ipynb', 'README'):
        if prefix + relative in known:
            return prefix + relative
    return source['local_directory'] + '/'


def slug(value):
    """Use readable safe directory names with a deterministic Unicode fallback."""
    result = re.sub(r'[^A-Za-z0-9._-]+', '-', value).strip('.-').lower()
    return result or 'model-' + hashlib.sha1(value.encode('utf-8')).hexdigest()[:8]


def model_inventory(root, manifest):
    """Return dictionaries for families, implementations and per-source counts.

    Canonical names from model_inventory.json determine merging. Variants are
    never merged by fuzzy matching; all source implementations stay accessible.
    """
    root = Path(root)
    metadata = read_json(root / 'tools/model_categories.json', {})
    public_inventory = read_json(root / 'tools/model_inventory.json', {'sources': {}})
    categories = metadata.get('categories', [])
    details = metadata.get('models', {})
    configurations = public_inventory.get('sources', {})
    profiles = read_profiles(root)
    if not isinstance(categories, list) or not isinstance(details, dict) or not isinstance(configurations, dict):
        raise ValueError('Invalid model category/inventory metadata')
    families, counts, labels = {}, {}, {}
    valid_categories = {item['id'] for item in categories}

    def append(name, source, core, entry, class_name=None):
        info = details.get(name, {})
        category = info.get('category', 'unclassified')
        if category not in valid_categories:
            category = 'unclassified'
        family = families.setdefault(name, {'implementations': [], 'category': category, 'info': info,
                                            'profile': profiles.get(name)})
        implementation = {'source': source['name'],
                          'directory': source['local_directory'], 'core': core, 'entry': entry,
                          'commit': source['commit']}
        if class_name:
            implementation['class_name'] = class_name
        key = (source['name'], core, class_name)
        existing = {(item['source'], item['core'], item.get('class_name'))
                    for item in family['implementations']}
        if key not in existing:
            family['implementations'].append(implementation)
            counts[source['name']] = counts.get(source['name'], 0) + 1

    for source in manifest['sources']:
        name = source['name']
        configuration = configurations.get(name, {})
        labels[name], counts[name] = source['local_directory'].split('/')[-1], 0
        prefix = source['local_directory']
        known = {entry['path'] for entry in source['files']}
        if name in INDEPENDENT:
            canonical, core, entry = INDEPENDENT[name]
            append(canonical, source, source_path(source, core), source_path(source, entry))
            if name == 'Pyraformer':
                item = families[canonical]['implementations'][-1]
                if prefix + '/pyraformer/Pyraformer_SS.py' in known:
                    item['extra_cores'] = [prefix + '/pyraformer/Pyraformer_SS.py']
                if prefix + '/single_step_main.py' in known:
                    item['extra_entries'] = [prefix + '/single_step_main.py']
            continue
        if name in ('Time-Series-Library', 'TimeSeriesLibrary-ZJ'):
            model_prefix = prefix + '/models/'
            for entry in source['files']:
                path = entry['path']
                tail = path[len(model_prefix):] if path.startswith(model_prefix) else ''
                if tail and '/' not in tail and tail.endswith('.py') and tail != '__init__.py':
                    append(tail[:-3], source, path, default_entry(source))
            continue
        for item in configuration.get('models', []):
            core = source_path(source, item['path'])
            entry = source_path(source, item['entry']) if item.get('entry') else default_entry(source)
            append(item['name'], source, core, entry, class_name=item.get('class_name'))
    used_paths = {}
    for name, family in families.items():
        directory = 'models/' + slug(family['category']) + '/' + slug(name)
        if directory in used_paths and used_paths[directory] != name:
            directory += '-' + hashlib.sha1(name.encode('utf-8')).hexdigest()[:8]
        used_paths[directory] = name
        family['directory'] = directory
        family['implementations'].sort(key=lambda item: (item['directory'], item['core'], item.get('class_name', '')))
        for index, implementation in enumerate(family['implementations'], 1):
            implementation['label'] = '实现' + str(index)
    ordered = categories + ([] if any(item['id'] == 'unclassified' for item in categories) else [UNCATEGORIZED])
    return {'metadata': metadata, 'categories': ordered, 'details': details,
            'families': families, 'source_counts': counts, 'source_labels': labels,
            'family_count': len(families),
            'implementation_count': sum(len(item['implementations']) for item in families.values()),
            'independent_count': sum(name in INDEPENDENT for name in counts)}


def href(target, prefix=''):
    return target if target.startswith(('https://', 'http://')) else prefix + quote(target, safe='/#')


def anchor(label, target, prefix='', title=None):
    # A nonbreaking joiner between letters prevents narrow GitHub table cells
    # from stacking Chinese link labels vertically; paths stay in the title.
    text = '&#8288;'.join(html.escape(character) if character != ' ' else '&nbsp;'
                         for character in str(label))
    description = ' title="' + html.escape(str(title), quote=True) + '"' if title else ''
    return '<a href="' + html.escape(href(target, prefix), quote=True) + '"' + description + '>' + text + '</a>'


def markdown_link(label, target, prefix=''):
    return '[' + label + '](' + href(target, prefix) + ')'


def primary_implementation(family):
    return family['implementations'][0]


def group_families(inventory):
    return [(category, sorted(((name, family) for name, family in inventory['families'].items()
                              if family['category'] == category['id']), key=lambda item: item[0].casefold()))
            for category in inventory['categories']]


def neutral_summary(value):
    value = re.sub(r'(?i)(?:Time-Series-Library|TimeSeriesLibrary|NeuralForecast|PyTorch Forecasting|TSLib|tsai|Darts)', '', value)
    value = value.replace('库内', '').replace('原版', '').replace('原项目', '').replace('库的', '')
    return re.sub(r'\s+', ' ', value).strip(' ，、；;')


def render_table(inventory, families, prefix=''):
    rows = ['<table>', '<thead><tr>',
            '<th width="100" align="left">模型</th>',
            '<th width="220" align="left">主要思路</th>',
            '<th width="110" align="left">源码</th>',
            '<th width="130" align="left">核心模型</th>',
            '<th width="120" align="left">运行入口</th>',
            '<th width="100" align="left">论文 / 项目</th>', '</tr></thead>', '<tbody>']
    for name, family in families:
        info = family['info']
        model_page = family['directory'] + '/README.md'
        display = anchor(name, model_page, prefix)
        if info.get('aliases'):
            display += '<br><sub>' + html.escape(' / '.join(info['aliases'])) + '</sub>'
        summary = html.escape(neutral_summary(info.get('summary', '方法说明见模型源码及项目文档。')))
        core_links, references = [], []
        for item in family['implementations']:
            label = item['label']
            core_title = item['core'] + (' :: ' + item['class_name'] if item.get('class_name') else '')
            core_links.append(anchor(label, item['core'], prefix, core_title))
            for path in item.get('extra_cores', []):
                core_links.append(anchor(label + '·单步', path, prefix, path))
        if info.get('paper_url'):
            references.append(anchor('相关论文' if info.get('paper_note') else '论文', info['paper_url'],
                                     title=info.get('paper_note', '模型论文')))
        references.append(anchor('项目', model_page, prefix))
        values = [display, summary, anchor('实现索引', model_page + '#实现', prefix),
                  '<br>'.join(core_links), anchor('运行方式', model_page + '#运行方式', prefix),
                  '<br>'.join(references)]
        rows += ['<tr>'] + ['<td align="left">' + value + '</td>' for value in values] + ['</tr>']
    rows += ['</tbody>', '</table>']
    return '\n'.join(rows)


def render_homepage_models(root, manifest):
    inventory = model_inventory(root, manifest)
    rows = [f"当前 **{inventory['family_count']} 个模型家族**、**{inventory['implementation_count']} 个实现入口**。点击模型名称先阅读介绍，再选择实现。", '',
            '| 分类 | 全部模型 |', '| --- | --- |']
    for category, families in group_families(inventory):
        if not families:
            continue
        names = [markdown_link(name, family['directory'] + '/README.md') for name, family in families]
        title = markdown_link(category['title'], 'docs/model-catalog.md#category-' + category['id'])
        rows.append('| ' + title + ' | ' + ' · '.join(names) + ' |')
    return '\n'.join(rows) + '\n'


def render_homepage_details(root, manifest):
    inventory = model_inventory(root, manifest)
    families = sorted(inventory['families'].items(), key=lambda item: item[0].casefold())
    return (f"共 **{inventory['family_count']} 个模型家族**，每个模型一行，所有来源使用相同六个字段。"
            '名称进入中文介绍页，介绍后的全部实现并列保留；悬停短链接可查看完整路径或类名。\n\n'
            + render_table(inventory, families) + '\n\n'
            '运行入口指向该实现的命令脚本或使用文档；支持任务与参数以对应源码为准。'
            '系列论文和加载变体的区别见论文链接的悬停说明。\n')


def render_catalog(root, manifest):
    inventory = model_inventory(root, manifest)
    rows = ['# 统一模型目录', '',
            f"共 **{inventory['family_count']} 个模型家族**、**{inventory['implementation_count']} 个实现入口**。每个模型在 `models/` 下拥有相同层级的项目目录。", '',
            '点击模型名称先看中文介绍，理解核心思路、适用问题和局限后，再进入源码。按主要建模机制分类，同名家族归入同一模型目录，命名变体分别保留。', '',
            '## 分类入口', '']
    for category, families in group_families(inventory):
        if families:
            rows.append(f"- [{category['title']}](#category-{category['id']})（{len(families)}）")
    for category, families in group_families(inventory):
        if not families:
            continue
        rows += ['', f'<a id="category-{category["id"]}"></a>', '', f'## {category["title"]}', '',
                 category.get('description', ''), '', render_table(inventory, families, '../')]
    rows += ['', '## 使用说明', '',
             '进入模型项目后查看实现索引与运行方式。每份实现保留完整内部目录、依赖和使用说明，参数与任务按对应配置选择。', '',
             '[完整模型库与教程](../README.md#完整模型库与教程)', '']
    return '\n'.join(rows)


def render_baselines_index():
    return '# 模型统一入口\n\n打开 [分类模型目录](../docs/model-catalog.md)，按模型名称查找同级项目目录。\n'


def relative_link(label, target, directory):
    path, separator, fragment = target.partition('#')
    relative = posixpath.relpath(path, directory)
    if target.endswith('/'):
        relative += '/'
    if separator:
        relative += '#' + fragment
    return markdown_link(label, relative)


def render_model_readme(name, family, inventory):
    directory = family['directory']
    info = family['info']
    category = next(item for item in inventory['categories'] if item['id'] == family['category'])
    rows = ['# ' + name, '', neutral_summary(info.get('summary', '方法说明见下方核心模型及使用文档。')), '',
            '**类别：** ' + category['title'], '',
            relative_link('返回分类目录', 'docs/model-catalog.md#category-' + family['category'], directory), '']
    profile = family.get('profile')
    if profile:
        for title, field in [('这是什么', 'intuition'), ('核心思路', 'mechanism'), ('适用问题', 'use_cases'),
                             ('局限与边界', 'limitations'), ('阅读建议', 'reading_tip')]:
            rows += ['## ' + title, '', neutral_summary(profile[field]), '']
    else:
        rows += ['## 模型介绍', '', '介绍尚在整理，完整生成时会校验全部模型介绍是否齐全。', '']
    rows += ['## 阅读材料', '']
    if info.get('paper_url'):
        rows.append(markdown_link('相关论文' if info.get('paper_note') else '模型论文', info['paper_url']))
    else:
        rows.append('可从下方实现的本地使用说明继续阅读。')
    if info.get('paper_note'):
        rows += ['', neutral_summary(info['paper_note'])]
    rows += ['',
            '<a id="实现"></a>', '', '## 实现', '',
            '| 实现 | 核心模型 | 模型类 | 完整目录 |', '| --- | --- | --- | --- |']
    for item in family['implementations']:
        core = relative_link('核心文件', item['core'], directory)
        for path in item.get('extra_cores', []):
            core += ' · ' + relative_link('单步核心', path, directory)
        rows.append('| ' + item['label'] + ' | ' + core + ' | `'
                    + item.get('class_name', 'Model') + '` | '
                    + relative_link('查看', item['directory'] + '/', directory) + ' |')
    rows += ['', '<a id="运行方式"></a>', '', '## 运行方式', '',
             '选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。', '']
    for item in family['implementations']:
        entries = [relative_link('入口与使用说明', item['entry'], directory)]
        entries += [relative_link('单步入口', path, directory) for path in item.get('extra_entries', [])]
        rows.append('- ' + item['label'] + '：' + ' · '.join(entries))
    rows += ['', relative_link('完整模型库与教程', 'README.md#完整模型库与教程', directory), '']
    return '\n'.join(rows)


def model_record(name, family):
    return {'schema_version': 1, 'name': name, 'category': family['category'],
            'directory': family['directory'],
            'summary': neutral_summary(family['info'].get('summary', '')),
            'paper_url': family['info'].get('paper_url'),
            'profile': family.get('profile'),
            'implementations': [{key: value for key, value in item.items() if key != 'source'}
                                for item in family['implementations']]}


def replace_generated_block(previous, key, content):
    start = '<!-- ' + key + '_START -->'
    end = '<!-- ' + key + '_END -->'
    if start not in previous and end not in previous:
        return previous
    if previous.count(start) != 1 or previous.count(end) != 1 or previous.index(start) > previous.index(end):
        raise ValueError('Invalid homepage model catalog markers')
    begin = previous.index(start) + len(start)
    finish = previous.index(end)
    return previous[:begin] + '\n\n' + content + '\n' + previous[finish:]


def render_homepage(root, manifest, previous):
    previous = replace_generated_block(previous, 'MODEL_CATALOG', render_homepage_models(root, manifest))
    return replace_generated_block(previous, 'MODEL_DETAILS', render_homepage_details(root, manifest))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--allow-missing-profiles', action='store_true',
                        help='Permit partial profile generation while authoring; final builds require complete profiles.')
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = read_json(root / 'sources.lock.json', {})
    inventory = model_inventory(root, manifest)
    missing = sorted(name for name, family in inventory['families'].items() if not family.get('profile'))
    if missing and not args.allow_missing_profiles:
        raise ValueError('Missing model profiles (' + str(len(missing)) + '): ' + ', '.join(missing))
    outputs = {'docs/model-catalog.md': render_catalog(root, manifest)}
    for name, family in inventory['families'].items():
        outputs[family['directory'] + '/README.md'] = render_model_readme(name, family, inventory)
        outputs[family['directory'] + '/model.json'] = json.dumps(model_record(name, family), ensure_ascii=False, indent=2) + '\n'
    rows = ['# 模型项目', '', markdown_link('按类别查找全部模型', 'docs/model-catalog.md', '../'), '']
    for category, families in group_families(inventory):
        if families:
            rows += ['## ' + category['title'], '']
            rows += ['- ' + markdown_link(name, family['directory'] + '/README.md', '../') for name, family in families]
            rows.append('')
            category_directory = 'models/' + slug(category['id'])
            category_rows = ['# ' + category['title'], '', category.get('description', ''), '']
            category_rows += ['- ' + relative_link(name, family['directory'] + '/README.md', category_directory)
                              for name, family in families]
            category_rows += ['', relative_link('全部模型', 'docs/model-catalog.md', category_directory), '']
            outputs[category_directory + '/README.md'] = '\n'.join(category_rows)
    outputs['models/README.md'] = '\n'.join(rows)
    homepage = root / 'README.md'
    if homepage.exists():
        outputs['README.md'] = render_homepage(root, manifest, homepage.read_bytes().decode('utf-8'))
    for relative, content in outputs.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content.encode('utf-8'))
    print(f"Generated {inventory['family_count']} families and {inventory['implementation_count']} implementations")


if __name__ == '__main__':
    main()
