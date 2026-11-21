"""Runnable forecast adapters; source models execute in an isolated process.

Reference adapters are workspace NumPy implementations of simple forecasts.
The torch_source adapter trains the selected, unmodified local model source.
"""

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import random
import subprocess
import sys
import tempfile
from types import SimpleNamespace

import numpy as np


REFERENCE_MODELS = ('NaiveMean', 'NaiveSeasonal', 'NaiveDrift')
TORCH_SOURCE_MODELS = ('DLinear', 'TSMixer')


def _root(options):
    return Path(options.get('repository_root', Path(__file__).resolve().parents[1])).resolve()


def _canonical(model_name, choices):
    matches = [name for name in choices if name.casefold() == str(model_name).casefold()]
    if not matches:
        raise ValueError('Unsupported model for this adapter: ' + str(model_name))
    return matches[0]


def _positive_integer(value, label, minimum=1):
    if isinstance(value, bool) or not isinstance(value, (int, np.integer)) or value < minimum:
        raise ValueError(label + ' must be an integer >= ' + str(minimum))
    return int(value)


def _matrix(value, label):
    array = np.asarray(value, dtype=np.float64)
    if array.ndim != 2 or min(array.shape) < 1 or not np.isfinite(array).all():
        raise ValueError(label + ' must be a nonempty finite [time, channels] array')
    return array


def _validate_inputs(train, contexts, horizon):
    train = _matrix(train, 'train')
    contexts = np.asarray(contexts, dtype=np.float64)
    horizon = _positive_integer(horizon, 'horizon')
    if (contexts.ndim != 3 or min(contexts.shape) < 1 or contexts.shape[2] != train.shape[1]
            or not np.isfinite(contexts).all()):
        raise ValueError('contexts must be finite [origins, lookback, channels] with the training channel count')
    return train, contexts, horizon


def _fit_scaler(train):
    """Fit only the supplied training segment, never forecast contexts/targets."""
    mean = np.mean(train, axis=0, keepdims=True)
    scale = np.std(train, axis=0, keepdims=True)
    scale = np.where(scale < 1e-8, 1.0, scale)
    return mean, scale


def _reference(model_name, train, contexts, horizon, options):
    name = _canonical(model_name, REFERENCE_MODELS)
    if name == 'NaiveMean':
        return np.broadcast_to(train.mean(axis=0), (len(contexts), horizon, train.shape[1])).copy()
    if name == 'NaiveSeasonal':
        period = _positive_integer(options.get('seasonal_period', options.get('period', 1)), 'seasonal_period')
        if period > contexts.shape[1]:
            raise ValueError('seasonal_period must not exceed the available context length')
        positions = np.arange(horizon) % period
        return contexts[:, -period:, :][:, positions, :].copy()
    if contexts.shape[1] < 2:
        raise ValueError('NaiveDrift needs at least two context observations')
    slope = (contexts[:, -1, :] - contexts[:, 0, :]) / (contexts.shape[1] - 1)
    return contexts[:, -1:, :] + np.arange(1, horizon + 1)[None, :, None] * slope[:, None, :]


def _source_record(model_name, options):
    name = _canonical(model_name, TORCH_SOURCE_MODELS)
    root = _root(options)
    directory = str(options.get('source_directory', '_sources/source-07')).replace('\\', '/')
    if directory != '_sources/source-07':
        raise ValueError('The tested torch_source models currently use _sources/source-07')
    from zpbts.registry import get_model
    family = get_model(name, root=root)
    core = directory + '/models/' + name + '.py'
    matches = [item for item in family['implementations']
               if item['directory'] == directory and item['core'] == core]
    if len(matches) != 1:
        raise ValueError('Selected source implementation does not match the local model registry')
    record = matches[0]
    if not (root / core).is_file():
        raise FileNotFoundError('Missing local model source: ' + core)
    return name, record, root


def adapter_metadata(model_name, options=None):
    """Describe the runnable implementation without importing torch."""
    options = dict(options or {})
    adapter = options.get('adapter', 'reference')
    if adapter == 'reference':
        name = _canonical(model_name, REFERENCE_MODELS)
        return {'adapter': 'reference', 'model': name, 'implementation': 'workspace_reference',
                'core': 'zpbts/adapters.py', 'source_commit': None,
                'note': 'Workspace NumPy reference forecast; does not execute an indexed upstream implementation.'}
    if adapter != 'torch_source':
        raise ValueError('Unknown adapter: ' + str(adapter))
    name, record, _ = _source_record(model_name, options)
    return {'adapter': 'torch_source', 'model': name, 'implementation': dict(record),
            'core': record['core'], 'source_directory': record['directory'],
            'source_commit': record['commit'], 'device': options.get('device', 'cpu'),
            'normalization': 'Per-channel mean/std fitted on train only; predictions returned in original units.'}


def _torch_options(options, lookback):
    values = {'lookback': lookback,
              'epochs': _positive_integer(options.get('epochs', 5), 'epochs'),
              'batch_size': _positive_integer(options.get('batch_size', 32), 'batch_size'),
              'learning_rate': float(options.get('learning_rate', 0.001)),
              'seed': int(options.get('seed', 2021)),
              'device': options.get('device', 'cpu'),
              'moving_avg': _positive_integer(options.get('moving_avg', 25), 'moving_avg'),
              'd_model': _positive_integer(options.get('d_model', 32), 'd_model'),
              'e_layers': _positive_integer(options.get('e_layers', 2), 'e_layers'),
              'dropout': float(options.get('dropout', 0.0)),
              'threads': _positive_integer(options.get('threads', 1), 'threads')}
    if not np.isfinite(values['learning_rate']) or values['learning_rate'] <= 0:
        raise ValueError('learning_rate must be finite and positive')
    if not 0 <= values['dropout'] < 1:
        raise ValueError('dropout must be in [0, 1)')
    if values['moving_avg'] % 2 != 1:
        raise ValueError('moving_avg must be odd')
    if values['device'] not in ('cpu', 'cuda', 'cuda:0'):
        raise ValueError('device must be cpu or a single cuda:0 device')
    return values


def fit_predict_with_metadata(model_name, train, contexts, horizon, options=None):
    """Fit once on train; predict each observed historical context independently.

    contexts may contain observations from a later rolling evaluation segment.
    They are never used for fitting the scaler or model parameters.
    """
    options = dict(options or {})
    train, contexts, horizon = _validate_inputs(train, contexts, horizon)
    metadata = adapter_metadata(model_name, options)
    if metadata['adapter'] == 'reference':
        return _reference(model_name, train, contexts, horizon, options), metadata
    name, record, root = _source_record(model_name, options)
    lookback = _positive_integer(options.get('lookback', contexts.shape[1]), 'lookback')
    if lookback != contexts.shape[1]:
        raise ValueError('lookback must equal contexts.shape[1]')
    if len(train) < lookback + horizon:
        raise ValueError('Training segment must contain at least lookback + horizon observations')
    values = _torch_options(options, lookback)
    python = str(options.get('python_executable', sys.executable))
    timeout = float(options.get('timeout_seconds', 600))
    if not np.isfinite(timeout) or timeout <= 0:
        raise ValueError('timeout_seconds must be finite and positive')
    with tempfile.TemporaryDirectory(prefix='zpbts-model-') as temporary:
        temporary = Path(temporary)
        inputs, output, configuration = temporary / 'inputs.npz', temporary / 'output.npz', temporary / 'config.json'
        np.savez(inputs, train=train, contexts=contexts)
        config = {'model': name, 'horizon': horizon, 'repository_root': str(root),
                  'implementation': record, 'options': values, 'inputs': str(inputs), 'output': str(output)}
        configuration.write_text(json.dumps(config), encoding='utf-8')
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', OMP_NUM_THREADS=str(values['threads']),
                   MKL_NUM_THREADS=str(values['threads']))
        if values['device'] == 'cpu':
            env['CUDA_VISIBLE_DEVICES'] = ''
        try:
            result = subprocess.run([python, '-B', str(Path(__file__).resolve()), '--worker', str(configuration)],
                                    cwd=root / record['directory'], env=env, capture_output=True,
                                    text=True, encoding='utf-8', errors='replace', timeout=timeout)
        except subprocess.TimeoutExpired as error:
            raise RuntimeError('Source-model training exceeded timeout_seconds') from error
        if result.returncode:
            raise RuntimeError('Source-model worker failed: ' + (result.stderr or result.stdout).strip()[-5000:])
        with np.load(output, allow_pickle=False) as data:
            predictions = data['predictions'].copy()
            diagnostics = json.loads(str(data['diagnostics'].item()))
    if predictions.shape != (len(contexts), horizon, train.shape[1]) or not np.isfinite(predictions).all():
        raise RuntimeError('Source-model worker returned invalid forecast shape or nonfinite values')
    metadata.update(diagnostics)
    metadata['resolved_training_options'] = values
    return predictions, metadata


def fit_predict(model_name, train, contexts, horizon, options=None):
    return fit_predict_with_metadata(model_name, train, contexts, horizon, options)[0]


def predict(model_name, history, horizon, options=None):
    options = dict(options or {})
    history = _matrix(history, 'history')
    default = min(96, max(2, len(history) // 2)) if options.get('adapter') == 'torch_source' else len(history)
    lookback = _positive_integer(options.get('lookback', default), 'lookback')
    if lookback > len(history):
        raise ValueError('lookback exceeds history length')
    return fit_predict(model_name, history, history[-lookback:][None, :, :], horizon, options)[0]


def predict_torch_source(model_name, history, horizon, options=None):
    return predict(model_name, history, horizon, {**dict(options or {}), 'adapter': 'torch_source'})


def _verify_source_python(root, directory, commit):
    manifest = json.loads((root / 'sources.lock.json').read_text(encoding='utf-8'))
    matches = [source for source in manifest['sources'] if source['local_directory'] == directory]
    if len(matches) != 1 or matches[0]['commit'] != commit:
        raise ValueError('Source commit differs from the selected model registry record')
    for entry in matches[0]['files']:
        if not entry['path'].endswith('.py'):
            continue
        path = root / entry['path']
        content = path.read_bytes()
        digest = hashlib.sha1(b'blob ' + str(len(content)).encode('ascii') + b'\0' + content).hexdigest()
        if digest != entry['git_blob_sha1']:
            raise ValueError('Source Python file differs from the pinned snapshot: ' + entry['path'])


def _worker(configuration):
    import torch
    config = json.loads(Path(configuration).read_text(encoding='utf-8'))
    root, record, options = Path(config['repository_root']), config['implementation'], config['options']
    _verify_source_python(root, record['directory'], record['commit'])
    directory = root / record['directory']
    sys.path.insert(0, str(directory))
    # A fresh subprocess prevents models/layers/utils imports from another source.
    specification = importlib.util.spec_from_file_location('_zpbts_source_model', root / record['core'])
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    random.seed(options['seed'])
    np.random.seed(options['seed'])
    torch.manual_seed(options['seed'])
    torch.set_num_threads(options['threads'])
    if options['device'] != 'cpu' and not torch.cuda.is_available():
        raise ValueError('Requested CUDA device is unavailable')
    device = torch.device(options['device'])
    if device.type == 'cuda':
        torch.cuda.manual_seed_all(options['seed'])
    torch.use_deterministic_algorithms(True)
    with np.load(config['inputs'], allow_pickle=False) as inputs:
        train, contexts = inputs['train'], inputs['contexts']
    mean, scale = _fit_scaler(train)
    train_tensor = torch.from_numpy(((train - mean) / scale).astype(np.float32))
    context_tensor = torch.from_numpy(((contexts - mean) / scale).astype(np.float32))
    lookback, horizon = options['lookback'], config['horizon']

    class Windows(torch.utils.data.Dataset):
        def __len__(self):
            return len(train_tensor) - lookback - horizon + 1

        def __getitem__(self, index):
            return (train_tensor[index:index + lookback],
                    train_tensor[index + lookback:index + lookback + horizon])

    generator = torch.Generator().manual_seed(options['seed'])
    loader = torch.utils.data.DataLoader(Windows(), batch_size=options['batch_size'],
                                         shuffle=True, generator=generator, num_workers=0)
    namespace = SimpleNamespace(task_name='long_term_forecast', seq_len=lookback, pred_len=horizon,
                                enc_in=train.shape[1], moving_avg=options['moving_avg'],
                                d_model=options['d_model'], e_layers=options['e_layers'], dropout=options['dropout'])
    model = module.Model(namespace).float().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=options['learning_rate'])
    criterion = torch.nn.MSELoss()
    steps, losses = 0, []
    for _ in range(options['epochs']):
        model.train()
        total, samples = 0.0, 0
        for features, targets in loader:
            optimizer.zero_grad(set_to_none=True)
            forecasts = model(features.to(device), None, None, None)
            loss = criterion(forecasts, targets.to(device))
            if not torch.isfinite(loss):
                raise ValueError('Nonfinite training loss')
            loss.backward()
            optimizer.step()
            total += loss.item() * len(features)
            samples += len(features)
            steps += 1
        losses.append(total / samples)
    model.eval()
    outputs = []
    with torch.no_grad():
        for start in range(0, len(context_tensor), options['batch_size']):
            outputs.append(model(context_tensor[start:start + options['batch_size']].to(device), None, None, None).cpu().numpy())
    predictions = np.concatenate(outputs, axis=0).astype(np.float64) * scale + mean
    diagnostics = {'train_observations': len(train), 'training_windows': len(Windows()),
                   'optimization_steps': steps, 'epoch_train_mse_standardized': losses,
                   'normalization_mean': mean.reshape(-1).tolist(), 'normalization_scale': scale.reshape(-1).tolist(),
                   'torch_version': torch.__version__, 'python_executable': sys.executable,
                   'model_class_module': str(Path(module.__file__).resolve()), 'seed': options['seed']}
    np.savez(config['output'], predictions=predictions, diagnostics=np.array(json.dumps(diagnostics)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--worker', required=True)
    _worker(parser.parse_args().worker)
