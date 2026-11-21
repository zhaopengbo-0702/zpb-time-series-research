#!/usr/bin/env python3
"""Build an offline model catalog from pinned sources and public model APIs."""

import argparse
import html
import json
from pathlib import Path, PurePosixPath
from urllib.parse import quote


INDEPENDENT = {
    'EMAformer': ('EMAformer', 'model/EMAformer.py', 'run.py'),
    'Pyraformer': ('Pyraformer', 'pyraformer/Pyraformer_LR.py', 'long_range_main.py'),
    'Informer2020': ('Informer', 'models/model.py', 'main_informer.py'),
    'Autoformer': ('Autoformer', 'models/Autoformer.py', 'run.py'),
    'ETSformer': ('ETSformer', 'models/etsformer/model.py', 'run.py'),
    'Time-LLM': ('Time-LLM', 'models/TimeLLM.py', 'run_main.py'),
}
SOURCE_LABELS = {'Time-Series-Library': 'TSLib', 'TimeSeriesLibrary-ZJ': 'ZJ',
                 'tsai': 'tsai', 'neuralforecast': 'NF',
                 'pytorch-forecasting': 'PF', 'darts': 'Darts'}
UNCATEGORIZED = {'id': 'unclassified', 'title': '待分类',
                 'description': '已收录但尚未填写主分类的模型；源码入口保留在这里。'}


def read_json(path, default):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default


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
    if not isinstance(categories, list) or not isinstance(details, dict) or not isinstance(configurations, dict):
        raise ValueError('Invalid model category/inventory metadata')
    families, counts, labels = {}, {}, {}
    valid_categories = {item['id'] for item in categories}

    def append(name, source, core, entry, label, class_name=None, note=None, kind='library'):
        info = details.get(name, {})
        category = info.get('category', 'unclassified')
        if category not in valid_categories:
            category = 'unclassified'
        family = families.setdefault(name, {'implementations': [], 'category': category, 'info': info})
        implementation = {'source': source['name'], 'label': label,
                          'directory': source['local_directory'], 'core': core, 'entry': entry,
                          'project': source.get('url', 'https://github.com/' + source['repository']),
                          'kind': kind}
        if class_name:
            implementation['class_name'] = class_name
        if note:
            implementation['note'] = note
        key = (source['name'], core, class_name)
        existing = {(item['source'], item['core'], item.get('class_name'))
                    for item in family['implementations']}
        if key not in existing:
            family['implementations'].append(implementation)
            counts[source['name']] = counts.get(source['name'], 0) + 1

    for source in manifest['sources']:
        name = source['name']
        configuration = configurations.get(name, {})
        label = SOURCE_LABELS.get(name, configuration.get('label', '原版'))
        labels[name], counts[name] = label, 0
        prefix = source['local_directory']
        known = {entry['path'] for entry in source['files']}
        if name in INDEPENDENT:
            canonical, core, entry = INDEPENDENT[name]
            append(canonical, source, source_path(source, core), source_path(source, entry),
                   '原版', kind='independent')
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
                    append(tail[:-3], source, path, default_entry(source), label)
            continue
        for item in configuration.get('models', []):
            core = source_path(source, item['path'])
            entry = source_path(source, item['entry']) if item.get('entry') else default_entry(source)
            append(item['name'], source, core, entry, label,
                   class_name=item.get('class_name'), note=item.get('note'))
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
    return next((item for item in family['implementations'] if item['kind'] == 'independent'),
                family['implementations'][0])


def group_families(inventory):
    return [(category, sorted(((name, family) for name, family in inventory['families'].items()
                              if family['category'] == category['id']), key=lambda item: item[0].casefold()))
            for category in inventory['categories']]


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
        display = html.escape(name)
        if info.get('aliases'):
            display += '<br><sub>' + html.escape(' / '.join(info['aliases'])) + '</sub>'
        summary = html.escape(info.get('summary', '当前公开实现；方法说明见模型源码及项目文档。'))
        source_links, core_links, entry_links, references = [], [], [], []
        source_seen, entry_seen = set(), set()
        implementation_counts = {}
        implementation_indexes = {}
        superscript = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')
        for item in family['implementations']:
            implementation_counts[item['source']] = implementation_counts.get(item['source'], 0) + 1
        for item in family['implementations']:
            label = item['label']
            title = item['directory'] + ('; ' + item['note'] if item.get('note') else '')
            if item['source'] not in source_seen:
                source_links.append(anchor(label, item['directory'] + '/', prefix, title))
                source_seen.add(item['source'])
            core_title = item['core'] + (' :: ' + item['class_name'] if item.get('class_name') else '')
            implementation_indexes[item['source']] = implementation_indexes.get(item['source'], 0) + 1
            core_label = label + (str(implementation_indexes[item['source']]).translate(superscript)
                                  if implementation_counts[item['source']] > 1 else '')
            core_links.append(anchor(core_label, item['core'], prefix, core_title))
            if (item['source'], item['entry']) not in entry_seen:
                entry_links.append(anchor(label, item['entry'], prefix,
                                          item['entry'] + '; 具体参数与任务按对应实现配置'))
                entry_seen.add((item['source'], item['entry']))
            for path in item.get('extra_cores', []):
                core_links.append(anchor('原版·单步', path, prefix, path))
            for path in item.get('extra_entries', []):
                entry_links.append(anchor('原版·单步', path, prefix, path))
        if info.get('paper_url'):
            references.append(anchor('论文', info['paper_url'], title=info.get('paper_note', '模型论文')))
        if info.get('original_upstream_url'):
            references.append(anchor('原项目', info['original_upstream_url']))
        else:
            projects = {}
            for item in family['implementations']:
                projects.setdefault(item['project'], item['label'])
            references.extend(anchor(label + '项目', url) for url, label in projects.items())
        values = [display, summary, '<br>'.join(source_links), '<br>'.join(core_links),
                  '<br>'.join(entry_links), '<br>'.join(references) or '见项目文档']
        rows += ['<tr>'] + ['<td align="left">' + value + '</td>' for value in values] + ['</tr>']
    rows += ['</tbody>', '</table>']
    return '\n'.join(rows)


def render_homepage_models(root, manifest):
    inventory = model_inventory(root, manifest)
    rows = [f"当前 **{inventory['family_count']} 个模型家族**、**{inventory['implementation_count']} 个实现入口**。每个模型名称直接链接到源码。", '',
            '| 分类 | 全部模型 |', '| --- | --- |']
    for category, families in group_families(inventory):
        if not families:
            continue
        names = [markdown_link(name, primary_implementation(family)['core']) for name, family in families]
        title = markdown_link(category['title'], 'docs/model-catalog.md#category-' + category['id'])
        rows.append('| ' + title + ' | ' + ' · '.join(names) + ' |')
    return '\n'.join(rows) + '\n'


def render_homepage_details(root, manifest):
    inventory = model_inventory(root, manifest)
    families = sorted(inventory['families'].items(), key=lambda item: item[0].casefold())
    return (f"共 **{inventory['family_count']} 个模型家族**，每个模型一行，所有来源使用相同六个字段。"
            '同一模型的各库实现全部并列保留；悬停短链接可查看完整路径或类名。\n\n'
            + render_table(inventory, families) + '\n\n'
            '运行入口指向该实现的命令脚本或使用文档；支持任务与参数以对应源码为准。'
            '系列论文和加载变体的区别见论文链接的悬停说明。\n')


def render_catalog(root, manifest):
    inventory = model_inventory(root, manifest)
    rows = ['# 统一模型目录', '',
            f"共 **{inventory['family_count']} 个模型家族**、**{inventory['implementation_count']} 个实现入口**。其中保留 {inventory['independent_count']} 个独立原版项目，其余实现来自完整收录的时间序列库。", '',
            '同名家族合并为一行，每个来源实现单独给出源码、核心文件与运行入口；变体按公开模型清单分别列出。', '',
            inventory['metadata'].get('classification_policy', '按主要建模机制分类，交叉机制写入模型简介。'), '',
            '## 分类入口', '']
    for category, families in group_families(inventory):
        if families:
            rows.append(f"- [{category['title']}](#category-{category['id']})（{len(families)}）")
    rows += ['', '## 来源与实现数量', '', '| 来源 | 模型实现入口数 | 源码位置 |', '| --- | ---: | --- |']
    by_name = {source['name']: source for source in manifest['sources']}
    for name, count in inventory['source_counts'].items():
        source = by_name[name]
        rows.append('| ' + name + ' | ' + str(count) + ' | '
                    + markdown_link(inventory['source_labels'][name], source['local_directory'] + '/', '../') + ' |')
    for category, families in group_families(inventory):
        if not families:
            continue
        rows += ['', f'<a id="category-{category["id"]}"></a>', '', f'## {category["title"]}', '',
                 category.get('description', ''), '', render_table(inventory, families, '../')]
    rows += ['', '## 任务、参数与来源', '',
             '任务支持由每份实现的模型分支和实验配置决定。源码列进入库根目录，核心模型列进入具体文件，运行入口列进入命令脚本或使用文档。不同库的同名模型可能采用不同数据处理和训练默认值。', '',
             '公开模型清单见 [model_inventory.json](../tools/model_inventory.json)，分类与论文信息见 [model_categories.json](../tools/model_categories.json)。来源提交和完整文件范围见 [来源记录](upstream-sources.md) 与 [sources.lock.json](../sources.lock.json)。', '']
    return '\n'.join(rows)


def render_baselines_index():
    return ('# 模型统一入口\n\n'
            '打开 [分类模型目录](../docs/model-catalog.md)，按模型家族查找全部来源实现。同名模型的独立原版与各库实现放在同一行，使用相同字段。\n\n'
            '本目录保留六个独立原版项目；完整时间序列库位于 [libraries/](../libraries/)。\n')


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
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = read_json(root / 'sources.lock.json', {})
    outputs = {'docs/model-catalog.md': render_catalog(root, manifest),
               'baselines/README.md': render_baselines_index()}
    homepage = root / 'README.md'
    if homepage.exists():
        outputs['README.md'] = render_homepage(root, manifest, homepage.read_bytes().decode('utf-8'))
    for relative, content in outputs.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content.encode('utf-8'))
    inventory = model_inventory(root, manifest)
    print(f"Generated {inventory['family_count']} families and {inventory['implementation_count']} implementations")


if __name__ == '__main__':
    main()
