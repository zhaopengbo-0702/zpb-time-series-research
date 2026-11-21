"""One data/split/metric contract shared by forecasting adapters."""

import csv
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import time

import numpy as np

from .registry import get_model

ROOT = Path(__file__).resolve().parents[1]


def _integer(value, name, minimum=1):
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(name + ' must be an integer >= ' + str(minimum))
    return value


def _keys(value, allowed, name):
    if not isinstance(value, dict) or set(value) - set(allowed):
        raise ValueError('Invalid or unknown fields in ' + name)


def _load_data(path, time_column, columns):
    raw = path.read_bytes()
    with path.open(encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames or []
        if len(fields) != len(set(fields)) or any(c not in fields for c in [time_column] + columns):
            raise ValueError('CSV requires unique headers and the configured columns')
        rows = list(reader)
    if not rows:
        raise ValueError('CSV is empty')
    try:
        stamps = [row[time_column] for row in rows]
        dates = [datetime.fromisoformat(s.replace('Z', '+00:00')) for s in stamps]
        if any(a >= b for a, b in zip(dates, dates[1:])):
            raise ValueError('CSV times must be strictly increasing and unique')
        values = np.asarray([[float(row[c]) for c in columns] for row in rows], dtype=np.float64)
    except (TypeError, KeyError, OverflowError) as exc:
        raise ValueError('Invalid CSV timestamp or value') from exc
    if not np.isfinite(values).all():
        raise ValueError('CSV values must be finite; preprocess missing values explicitly')
    return stamps, values, hashlib.sha256(raw).hexdigest()


def _scores(actual, predicted, train, period):
    error = predicted - actual
    denominator = np.abs(actual) + np.abs(predicted)
    smape = np.divide(200 * np.abs(error), denominator,
                      out=np.zeros_like(error), where=denominator != 0)
    scale = np.abs(train[period:] - train[:-period]).mean(axis=0)
    scaled = np.divide(np.abs(error), scale, out=np.full_like(error, np.nan), where=scale > 0)
    # A constant training series has no MASE denominator; retain null, not a fabricated zero.
    mase = float(scaled.mean()) if np.isfinite(scaled).all() else None
    return dict(mae=float(np.abs(error).mean()), mse=float(np.square(error).mean()),
                rmse=float(np.sqrt(np.square(error).mean())), smape=float(smape.mean()), mase=mase)


def _write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')


def run_experiment(config_path, output_dir):
    """Fit once on train; forecast fixed test origins using observed past contexts."""
    from .adapters import fit_predict_with_metadata

    config_path, output_dir = Path(config_path).resolve(), Path(output_dir).resolve()
    config = json.loads(config_path.read_text(encoding='utf-8'))
    _keys(config, {'schema_version', 'model', 'adapter', 'data', 'evaluation', 'options'}, 'config')
    if config.get('schema_version') != 1:
        raise ValueError('schema_version must be 1')
    family = get_model(config['model'])
    if not family:
        raise ValueError('Unknown model: ' + str(config['model']))
    model = family.get('name', config['model'])
    data, evaluation = config['data'], config['evaluation']
    _keys(data, {'path', 'time_column', 'columns', 'train_end', 'test_start'}, 'data')
    _keys(evaluation, {'lookback', 'horizon', 'stride', 'mase_period'}, 'evaluation')
    columns, time_column = data['columns'], data['time_column']
    if (not isinstance(columns, list) or not columns or any(not isinstance(c, str) for c in columns)
            or len(columns) != len(set(columns)) or time_column in columns):
        raise ValueError('columns must be distinct numeric target column names')
    stamps, values, digest = _load_data(config_path.parent / data['path'], time_column, columns)
    train_end = _integer(data['train_end'], 'train_end')
    test_start = _integer(data['test_start'], 'test_start')
    lookback = _integer(evaluation['lookback'], 'lookback', 2)
    horizon = _integer(evaluation['horizon'], 'horizon')
    stride = _integer(evaluation['stride'], 'stride')
    period = _integer(evaluation.get('mase_period', 1), 'mase_period')
    if not lookback <= train_end <= test_start < len(values) or train_end <= period:
        raise ValueError('Require lookback <= train_end <= test_start < row_count and train_end > mase_period')
    origins = list(range(test_start, len(values) - horizon + 1, stride))
    if not origins:
        raise ValueError('Test split has no complete forecast horizon')
    options = dict(config.get('options', {}))
    adapter = config.get('adapter', 'reference')
    supported_options = {'seed', 'period', 'seasonal_period'} if adapter == 'reference' else {
        'seed', 'source_directory', 'python_executable', 'timeout_seconds', 'epochs',
        'batch_size', 'learning_rate', 'device', 'moving_avg', 'd_model', 'e_layers', 'dropout', 'threads'}
    if set(options) - supported_options:
        raise ValueError('Unknown adapter options: ' + ', '.join(sorted(set(options) - supported_options)))
    options['adapter'] = adapter
    options['lookback'] = lookback
    options.setdefault('seed', 7)
    _integer(options['seed'], 'seed', 0)
    if output_dir.exists() and any(output_dir.iterdir()):
        raise ValueError('Output directory must be empty: ' + str(output_dir))
    contexts = np.stack([values[o - lookback:o] for o in origins])
    truth = np.stack([values[o:o + horizon] for o in origins])
    train = values[:train_end].copy()
    started = time.perf_counter()
    predictions, metadata = fit_predict_with_metadata(model, train, contexts, horizon, options)
    predicted = np.asarray(predictions, dtype=np.float64)
    seconds = time.perf_counter() - started
    if predicted.shape != truth.shape or not np.isfinite(predicted).all():
        raise ValueError('Adapter returned invalid forecast shape or non-finite values')
    protocol = dict(dataset_sha256=digest, time_column=time_column, columns=columns,
                    train_end=train_end, test_start=test_start, row_count=len(values),
                    lookback=lookback, horizon=horizon, stride=stride, origins=origins,
                    metric_scale='original', history_policy='observed_rolling_frozen_fit',
                    mase_period=period, missing_policy='reject')
    protocol_id = hashlib.sha256(json.dumps(protocol, sort_keys=True).encode()).hexdigest()
    try:
        revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, stderr=subprocess.DEVNULL).decode().strip()
        dirty = bool(subprocess.check_output(['git', 'status', '--porcelain'], cwd=ROOT, stderr=subprocess.DEVNULL).strip())
    except (OSError, subprocess.CalledProcessError):
        revision, dirty = None, None
    code_hashes = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in sorted((ROOT / 'zpbts').glob('*.py'))}
    result = dict(schema_version=1, model=model, adapter=adapter, protocol=protocol,
                  protocol_id=protocol_id, implementation=metadata, seed=options['seed'],
                  options=options, metrics=_scores(truth, predicted, train, period),
                  metrics_by_column={c: _scores(truth[..., i:i+1], predicted[..., i:i+1], train[:, i:i+1], period)
                                     for i, c in enumerate(columns)},
                  metrics_by_horizon={str(h + 1): _scores(truth[:, h:h+1], predicted[:, h:h+1], train, period)
                                      for h in range(horizon)},
                  forecast_count=int(truth.size), fit_seconds=seconds,
                  environment=dict(python=platform.python_version(), numpy=np.__version__,
                                   repository_commit=revision, repository_dirty=dirty, workspace_code_sha256=code_hashes))
    output_dir.mkdir(parents=True, exist_ok=True)
    saved = json.loads(json.dumps(config))
    saved['data']['path'] = os.path.relpath((config_path.parent / data['path']).resolve(), output_dir).replace('\\', '/')
    _write_json(output_dir / 'config.json', saved)
    _write_json(output_dir / 'metrics.json', result)
    with (output_dir / 'predictions.csv').open('w', encoding='utf-8', newline='') as handle:
        writer = csv.writer(handle)
        writer.writerow(['origin_timestamp', 'target_timestamp', 'horizon', 'column', 'y_true', 'y_pred'])
        for n, origin in enumerate(origins):
            for h in range(horizon):
                for c, column in enumerate(columns):
                    writer.writerow([stamps[origin - 1], stamps[origin + h], h + 1, column,
                                     truth[n, h, c], predicted[n, h, c]])
    return result


def compare_results(directories):
    """Compare scores only when full evaluation protocols match."""
    if not directories:
        raise ValueError('At least one result directory is required')
    results = [json.loads((Path(p) / 'metrics.json').read_text(encoding='utf-8')) for p in directories]
    if any(r['protocol'] != results[0]['protocol'] for r in results[1:]):
        raise ValueError('Cannot compare results with different evaluation protocols')
    lines = ['| Model | Adapter | Seed | MAE | MSE | RMSE | sMAPE (%) | MASE |',
             '| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    for result in sorted(results, key=lambda r: r['metrics']['mae']):
        m = result['metrics']
        values = [result['model'], result['adapter'], str(result['seed'])]
        values += ['undefined' if m[k] is None else format(m[k], '.6f') for k in ['mae', 'mse', 'rmse', 'smape', 'mase']]
        lines.append('| ' + ' | '.join(values) + ' |')
    return '\n'.join(lines) + '\n'
