#!/usr/bin/env python3
"""Build the complete, categorized model catalog from the pinned source lock."""

import argparse
import json
from pathlib import Path, PurePosixPath
import re


INDEPENDENT = {
    'EMAformer': ('model/EMAformer.py', 'run.py'),
    'Pyraformer': ('pyraformer/Pyraformer_LR.py', 'long_range_main.py'),
    'Informer2020': ('models/model.py', 'main_informer.py'),
    'Autoformer': ('models/Autoformer.py', 'run.py'),
    'ETSformer': ('models/etsformer/model.py', 'run.py'),
    'Time-LLM': ('models/TimeLLM.py', 'run_main.py'),
}
ALIASES = {'Informer2020': 'Informer', 'Time-LLM': 'Time-LLM'}
TASK_DIRECTORIES = {
    'long_term_forecast': '长期预测', 'short_term_forecast': '短期预测',
    'imputation': '缺失补全', 'anomaly_detection': '异常检测',
    'classification': '分类', 'exogenous_forecast': '外生变量预测',
}


def link(label, path):
    # Paths originate in the validated source lock; protect Markdown separators.
    safe_label = str(label).replace('|', '\\|').replace('\n', ' ')
    return f'[{safe_label}](../{path})'


def model_inventory(root, manifest):
    """Collect every model once, irrespective of its imported source."""
    root = Path(root)
    metadata_path = root / 'tools' / 'model_categories.json'
    metadata = json.loads(metadata_path.read_text(encoding='utf-8')) if metadata_path.exists() else {}
    categories = metadata.get('categories', [])
    details = metadata.get('models', {})
    if not isinstance(categories, list) or not isinstance(details, dict):
        raise ValueError('Invalid tools/model_categories.json structure')
    families = {}
    library = next((source for source in manifest['sources'] if source['name'] == 'Time-Series-Library'), None)
    library_count = 0
    if library:
        prefix = library['local_directory'] + '/models/'
        for entry in library['files']:
            path = entry['path']
            tail = path[len(prefix):] if path.startswith(prefix) else ''
            if not tail or '/' in tail or not tail.endswith('.py') or tail == '__init__.py':
                continue
            name = tail[:-3]
            families.setdefault(name, {})['library'] = path
            library_count += 1
    independent_count = 0
    for source in manifest['sources']:
        if source['name'] not in INDEPENDENT:
            continue
        independent_count += 1
        name = ALIASES.get(source['name'], source['name'])
        item = families.setdefault(name, {})
        known = {entry['path'] for entry in source['files']}
        core, training = INDEPENDENT[source['name']]
        item['independent'] = source['local_directory']
        item['independent_name'] = source['name']
        item['independent_url'] = source.get('url', 'https://github.com/' + source['repository'])
        item['core'] = source['local_directory'] + '/' + core if source['local_directory'] + '/' + core in known else None
        item['training'] = source['local_directory'] + '/' + training if source['local_directory'] + '/' + training in known else None
    return metadata, categories, details, families, library, library_count, independent_count


def render_catalog(root, manifest):
    metadata, categories, details, families, library, library_count, independent_count = model_inventory(root, manifest)
    grouped = {}
    valid_categories = {category['id'] for category in categories}
    for name, item in families.items():
        info = details.get(name, {})
        category = info.get('category', 'unclassified')
        if category not in valid_categories:
            category = 'unclassified'
        grouped.setdefault(category, []).append((name, item, info))
    ordered = categories + [{'id': 'unclassified', 'title': '待分类',
                              'description': '上游新增或尚未填写分类的模型仍完整列在这里，后续可补充分类说明。'}]
    rows = ['# 统一模型目录', '',
            f'当前共 **{len(families)} 个模型家族**，含 {independent_count} 个独立原版入口和 '
            f'Time-Series-Library 的全部 {library_count} 个模型文件。同名模型合并为同一行，分别链接独立原版与库内实现。', '',
            '目录根据 [sources.lock.json](../sources.lock.json) 与 [分类元数据](../tools/model_categories.json) 生成。'
            '分类用于查找源码；每个模型的任务支持仍由其 `forward()`、依赖和具体实验脚本决定。', '',
            '## 按方法类别查找', '']
    if metadata.get('classification_policy'):
        rows[-2:-2] = [metadata['classification_policy'], '']
    for category in ordered:
        if grouped.get(category['id']):
            rows.append(f"- [{category['title']}](#category-{category['id']})（{len(grouped[category['id']])}）")
    for category in ordered:
        items = grouped.get(category['id'], [])
        if not items:
            continue
        rows += ['', f'<a id="category-{category["id"]}"></a>', '', f'## {category["title"]}', '']
        if category.get('description'):
            rows += [category['description'], '']
        rows += ['| 模型 | 特点与源码定位 | 独立原版 | 库内实现 | 任务与脚本入口 |',
                 '| --- | --- | --- | --- | --- |']
        for name, item, info in sorted(items, key=lambda value: value[0].casefold()):
            independent = link(item['independent_name'], item['independent'] + '/') if item.get('independent') else '—'
            if item.get('core'):
                independent += ' · ' + link('核心文件', item['core'])
            implementation = link(PurePosixPath(item['library']).name, item['library']) if item.get('library') else '—'
            scripts = []
            if item.get('training'):
                scripts.append(link('原版入口', item['training']))
            if item.get('library') and library:
                requested = info.get('script_paths', [])
                if requested:
                    scripts.extend(link(PurePosixPath(path).name or '脚本', library['local_directory'] + '/' + path)
                                   for path in requested)
                else:
                    scripts.append(link('库内任务脚本', library['local_directory'] + '/scripts/'))
            summary = info.get('summary', '分类与特点待补充；点击源码查看当前实现。')
            displayed_name = name + (' / ' + ' / '.join(info['aliases']) if info.get('aliases') else '')
            rows.append('| ' + displayed_name + ' | ' + summary.replace('|', '\\|').replace('\n', ' ') + ' | '
                        + independent + ' | ' + implementation + ' | ' + (' · '.join(scripts) or '—') + ' |')
    rows += ['', '## 按任务查实验入口', '']
    if library:
        prefix = library['local_directory']
        known = {entry['path'] for entry in library['files']}
        rows += [f'库的统一入口为 {link("run.py", prefix + "/run.py")}。实际脚本目录如下；目录存在不代表全部模型支持该任务。', '']
        for directory, label in TASK_DIRECTORIES.items():
            path = prefix + '/scripts/' + directory + '/'
            if any(value.startswith(path) for value in known):
                rows.append('- ' + link(label, path))
        zero_shot = prefix + '/scripts/long_term_forecast/ETT_script/LTSM.sh'
        if zero_shot in known:
            rows += ['', '零样本预测示例：' + link('LTSM.sh', zero_shot)
                     + '。这是脚本名；具体模型与参数以脚本当前内容为准，预训练权重由模型接口另外加载。']
    rows += ['', '## 独立原版与库内实现怎么选', '',
             '读论文原实现、对照原作者实验时，从“独立原版”进入；使用库内统一实验接口时，从“库内实现”进入。'
             '两个入口都保留原始文件，目录没有移动或拆成新的伪原版仓库。', '',
             '完整来源提交、文件数和最近同步状态见 [上游状态](upstream-status.md)；'
             '阅读关键文件的顺序见 [源码导航](model-guide.md)。', '']
    return '\n'.join(rows)


def render_baselines_index():
    return ('# 模型统一入口\n\n'
            '打开 [分类模型目录](../docs/model-catalog.md)，按模型家族查找全部独立原版与库内实现。'
            '同名模型的两个入口在同一行，可直接对照。\n\n'
            '本目录保留各独立模型的固定提交源码；完整 Time-Series-Library 位于 '
            '[libraries/Time-Series-Library](../libraries/Time-Series-Library/)。\n')


def render_homepage_models(root, manifest):
    """Show every family at the same level on the repository homepage."""
    catalog = render_catalog(root, manifest)
    current = None
    groups = []
    for line in catalog.splitlines():
        match = re.fullmatch(r'<a id="category-([^"]+)"></a>', line)
        if match:
            current = {'id': match.group(1), 'title': None, 'models': []}
            groups.append(current)
        elif current and current['title'] is None and line.startswith('## '):
            current['title'] = line[3:]
        elif current and line.startswith('| ') and not line.startswith(('| 模型 |', '| --- |')):
            cells = line.split(' | ')
            if len(cells) < 5:
                continue
            name = cells[0][2:].split(' / ')[0]
            independent_links = re.findall(r'\]\(\.\./([^)]+)\)', cells[2])
            library_links = re.findall(r'\]\(\.\./([^)]+)\)', cells[3])
            target = (independent_links[-1] if independent_links else library_links[0] if library_links
                      else 'docs/model-catalog.md#category-' + current['id'])
            current['models'].append(f'[{name}]({target})')
    count = sum(len(group['models']) for group in groups)
    rows = [f'当前 **{count} 个模型家族**，按主要建模机制分类。每个模型名称都直接链接到源码。', '',
            '| 分类 | 全部模型 |', '| --- | --- |']
    for group in groups:
        if group['models']:
            title = f'[{group["title"]}](docs/model-catalog.md#category-{group["id"]})'
            rows.append('| ' + title + ' | ' + ' · '.join(group['models']) + ' |')
    return '\n'.join(rows) + '\n'


def render_homepage_details(root, manifest):
    """Keep the same six fields for every model, with compact link labels."""
    _, categories, details, families, library, _, _ = model_inventory(root, manifest)
    titles = {category['id']: category['title'] for category in categories}
    rows = [f'共 **{len(families)} 个模型**，按名称排序，每个模型一行。分类见上表；各行使用相同字段，'
            '有多个实现时同时列出。悬停在链接上可查看完整文件路径。', '',
            '| 模型 | 主要思路 | 源码 | 核心模型 | 运行入口 | 论文&nbsp;/&nbsp;项目 |',
            '| :--- | :--- | :---: | :---: | :---: | :---: |']

    def compact(label, target, hint=None):
        hint = (hint or target).replace('"', "'")
        return f'[{label}]({target} "{hint}")'

    for name, item in sorted(families.items(), key=lambda value: value[0].casefold()):
        info = details.get(name, {})
        sources, models, entries = [], [], []
        if item.get('independent'):
            sources.append(compact('原项目', item['independent'] + '/'))
            if item.get('core'):
                models.append(compact('原版模型', item['core']))
            if item.get('training'):
                entries.append(compact('原版入口', item['training']))
            if name == 'Pyraformer':
                original = next(s for s in manifest['sources'] if s['name'] == 'Pyraformer')
                tracked = {entry['path'] for entry in original['files']}
                single_model = item['independent'] + '/pyraformer/Pyraformer_SS.py'
                single_entry = item['independent'] + '/single_step_main.py'
                if single_model in tracked:
                    models.append(compact('单步模型', single_model))
                if single_entry in tracked:
                    entries.append(compact('单步入口', single_entry))
        if item.get('library') and library:
            sources.append(compact('TSLib', library['local_directory'] + '/'))
            models.append(compact('库内模型', item['library']))
            entries.append(compact('库内入口', library['local_directory'] + '/run.py',
                                   '按任务选择参数；查看库内 scripts 目录'))
        references = []
        if info.get('paper_url'):
            references.append(compact('论文', info['paper_url'], info.get('paper_note') or '模型论文'))
        project = info.get('original_upstream_url') or item.get('independent_url') or (library or {}).get('url')
        if project:
            references.append(compact('项目', project))
        display_name = {'Nonstationary_Transformer': 'Nonstationary<br>Transformer',
                        'TemporalFusionTransformer': 'Temporal Fusion<br>Transformer'}.get(name, name)
        values = [display_name, info.get('summary', '方法说明待补充，源码已完整收录。'),
                  '<br>'.join(sources) or '—', '<br>'.join(models) or '—',
                  '<br>'.join(entries) or '见源码', '&nbsp;·&nbsp;'.join(references) or '见源码']
        rows.append('| ' + ' | '.join(str(value).replace('|', '\\|').replace('\n', ' ') for value in values) + ' |')
    rows += ['', '原项目与库内入口对应不同实现；运行参数和支持任务见各自源码。'
             '系列论文与当前预训练权重的差异已放入论文链接的悬停说明。', '']
    return '\n'.join(rows)


def replace_generated_block(previous, key, content):
    start = f'<!-- {key}_START -->'
    end = f'<!-- {key}_END -->'
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
    manifest = json.loads((root / 'sources.lock.json').read_text(encoding='utf-8'))
    catalog = root / 'docs' / 'model-catalog.md'
    catalog.parent.mkdir(parents=True, exist_ok=True)
    catalog.write_bytes(render_catalog(root, manifest).encode('utf-8'))
    baseline_index = root / 'baselines' / 'README.md'
    baseline_index.parent.mkdir(parents=True, exist_ok=True)
    baseline_index.write_bytes(render_baselines_index().encode('utf-8'))
    homepage = root / 'README.md'
    if homepage.exists():
        previous = homepage.read_bytes().decode('utf-8')
        homepage.write_bytes(render_homepage(root, manifest, previous).encode('utf-8'))
    print('Updated model catalog, baseline index and homepage model block')


if __name__ == '__main__':
    main()
