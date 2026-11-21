"""Forecast contracts and real CPU source-model training checks."""

import importlib.util
import os
from pathlib import Path
import sys
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from zpbts.adapters import adapter_metadata, fit_predict, fit_predict_with_metadata, predict, _fit_scaler


class ReferenceForecastTests(unittest.TestCase):
    def test_reference_forecasts_have_exact_expected_values(self):
        train = np.array([[1., 10.], [2., 20.], [3., 30.], [4., 40.]])
        np.testing.assert_allclose(predict('NaiveMean', train, 3), np.tile([2.5, 25.], (3, 1)))
        np.testing.assert_allclose(predict('NaiveSeasonal', train, 3, {'seasonal_period': 2}), [[3., 30.], [4., 40.], [3., 30.]])
        np.testing.assert_allclose(predict('NaiveDrift', train, 2), [[5., 50.], [6., 60.]])
        self.assertEqual(adapter_metadata('NaiveMean')['implementation'], 'workspace_reference')

    def test_mean_fits_training_only_while_seasonal_uses_each_observed_context(self):
        train = np.arange(12., dtype=float).reshape(6, 2)
        contexts = np.array([[[100., 200.], [300., 400.]], [[500., 600.], [700., 800.]]])
        before = contexts.copy()
        forecasts = fit_predict('NaiveMean', train, contexts, 2)
        np.testing.assert_allclose(forecasts, np.broadcast_to(train.mean(0), (2, 2, 2)))
        np.testing.assert_array_equal(fit_predict('NaiveSeasonal', train, contexts, 1), contexts[:, -1:, :])
        np.testing.assert_array_equal(contexts, before)
        mean, scale = _fit_scaler(train)
        np.testing.assert_allclose(mean, train.mean(0, keepdims=True))
        np.testing.assert_allclose(scale, train.std(0, keepdims=True))

    def test_invalid_values_and_shapes_fail_explicitly(self):
        with self.assertRaises(ValueError):
            predict('NaiveMean', [[float('nan')]], 2)
        with self.assertRaises(ValueError):
            predict('NaiveSeasonal', [[1.], [2.]], 2, {'seasonal_period': 3})
        with self.assertRaises(ValueError):
            fit_predict('NaiveMean', np.ones((5, 2)), np.ones((2, 3, 1)), 2)
        with self.assertRaises(ValueError):
            predict('NaiveMean', [[1.]], 0)


class TorchSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.python = os.environ.get('ZPBTS_TEST_TORCH_PYTHON', sys.executable)
        if cls.python == sys.executable and importlib.util.find_spec('torch') is None:
            raise unittest.SkipTest('Set ZPBTS_TEST_TORCH_PYTHON to an interpreter with torch for real source tests')

    def options(self):
        return {'adapter': 'torch_source', 'lookback': 8, 'epochs': 5, 'batch_size': 16,
                'learning_rate': 0.02, 'seed': 23, 'device': 'cpu', 'd_model': 8, 'e_layers': 1,
                'moving_avg': 3, 'python_executable': self.python}

    def test_real_dlinear_and_tsmixer_train_once_and_return_original_unit_forecasts(self):
        time = np.arange(72, dtype=float)
        train = np.column_stack([10. + time / 7., 200. + np.sin(time / 4.) * 8.])
        contexts = np.stack([train[-8:], train[-8:] + [30., 100.]])
        for model in ('DLinear', 'TSMixer'):
            with self.subTest(model=model):
                prediction, metadata = fit_predict_with_metadata(model, train, contexts, 3, self.options())
                self.assertEqual(prediction.shape, (2, 3, 2))
                self.assertTrue(np.isfinite(prediction).all())
                self.assertGreater(metadata['optimization_steps'], 0)
                self.assertEqual(metadata['train_observations'], len(train))
                self.assertEqual(metadata['training_windows'], len(train) - 8 - 3 + 1)
                self.assertEqual(len(metadata['epoch_train_mse_standardized']), 5)
                self.assertLess(metadata['epoch_train_mse_standardized'][-1], metadata['epoch_train_mse_standardized'][0])
                np.testing.assert_allclose(metadata['normalization_mean'], train.mean(0))
                np.testing.assert_allclose(metadata['normalization_scale'], train.std(0))
                self.assertTrue(metadata['core'].endswith('/models/' + model + '.py'))
                self.assertEqual(len(metadata['source_commit']), 40)
                self.assertEqual(Path(metadata['model_class_module']).resolve(), (ROOT / metadata['core']).resolve())
                # No contexts or targets beyond train were used to fit scaling.
                changed, changed_metadata = fit_predict_with_metadata(model, train, contexts[:1], 3, self.options())
                np.testing.assert_allclose(changed[0], prediction[0], atol=1e-6)
                self.assertEqual(changed_metadata['normalization_mean'], metadata['normalization_mean'])
                self.assertEqual(changed_metadata['epoch_train_mse_standardized'], metadata['epoch_train_mse_standardized'])

    def test_source_selection_and_training_length_fail_before_launch(self):
        with self.assertRaises(ValueError):
            adapter_metadata('DLinear', {**self.options(), 'source_directory': '_sources/source-08'})
        with self.assertRaises(ValueError):
            fit_predict('DLinear', np.ones((8, 2)), np.ones((1, 8, 2)), 3, self.options())


if __name__ == '__main__':
    unittest.main(verbosity=2)
