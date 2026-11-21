"""Behavior checks for the shared experiment and fair-comparison protocol."""

import copy
import csv
from datetime import datetime, timedelta
import hashlib
import json
import math
from pathlib import Path
import tempfile
import unittest

from zpbts.experiment import compare_results, run_experiment


class ExperimentTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="zpb-experiment-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.values = [float(index) for index in range(120)]
        start = datetime(2025, 1, 1)
        self.timestamps = [(start + timedelta(hours=index)).isoformat() for index in range(120)]
        self.data_path = self.root / "data.csv"
        self.write_data()
        self.config = {
            "schema_version": 1,
            "model": "NaiveMean",
            "adapter": "reference",
            "data": {
                "path": "data.csv",
                "time_column": "date",
                "columns": ["y"],
                "train_end": 72,
                "test_start": 96,
            },
            "evaluation": {"lookback": 12, "horizon": 6, "stride": 6},
            "options": {"seed": 7},
        }

    def write_data(self, values=None, timestamps=None):
        values = self.values if values is None else values
        timestamps = self.timestamps if timestamps is None else timestamps
        with self.data_path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(["date", "y", "other"])
            for index, (timestamp, value) in enumerate(zip(timestamps, values)):
                writer.writerow([timestamp, value, 2 * index + 1])

    def run_fixture(self, config=None, label="run"):
        config_path = self.root / (label + ".json")
        config_path.write_text(json.dumps(self.config if config is None else config), encoding="utf-8")
        output = self.root / label
        result = run_experiment(config_path, output)
        return result, output

    def predictions(self, output):
        with (output / "predictions.csv").open(encoding="utf-8", newline="") as stream:
            return list(csv.DictReader(stream))

    def test_run_writes_auditable_outputs_and_original_scale_metrics(self):
        result, output = self.run_fixture()
        self.assertIsInstance(result, dict)
        for name in ("config.json", "metrics.json", "predictions.csv"):
            self.assertTrue((output / name).is_file(), name)
        saved = json.loads((output / "metrics.json").read_text(encoding="utf-8"))
        self.assertEqual(result, saved)
        self.assertEqual(result["model"], "NaiveMean")
        self.assertEqual(result["adapter"], "reference")
        protocol = result["protocol"]
        expected_fields = {
            "dataset_sha256", "time_column", "columns", "train_end", "test_start", "row_count",
            "lookback", "horizon", "stride", "origins", "metric_scale", "history_policy",
        }
        self.assertTrue(expected_fields.issubset(protocol))
        self.assertEqual(protocol["dataset_sha256"], hashlib.sha256(self.data_path.read_bytes()).hexdigest())
        self.assertEqual(protocol["columns"], ["y"])
        self.assertEqual(protocol["row_count"], 120)
        self.assertEqual(protocol["metric_scale"], "original")
        self.assertEqual(protocol["history_policy"], "observed_rolling_frozen_fit")
        self.assertEqual(len(protocol["origins"]), 4)
        predictions = self.predictions(output)
        self.assertEqual(len(predictions), 24)
        required = {"origin_timestamp", "target_timestamp", "horizon", "column", "y_true", "y_pred"}
        self.assertTrue(required.issubset(predictions[0]))
        for row in predictions:
            self.assertEqual(row["column"], "y")
            self.assertLess(datetime.fromisoformat(row["origin_timestamp"]),
                            datetime.fromisoformat(row["target_timestamp"]))
            self.assertGreaterEqual(datetime.fromisoformat(row["target_timestamp"]),
                                    datetime.fromisoformat(self.timestamps[96]))
            self.assertLessEqual(datetime.fromisoformat(row["target_timestamp"]),
                                 datetime.fromisoformat(self.timestamps[-1]))
        errors = [float(row["y_pred"]) - float(row["y_true"]) for row in predictions]
        mae = sum(abs(value) for value in errors) / len(errors)
        mse = sum(value * value for value in errors) / len(errors)
        self.assertAlmostEqual(result["metrics"]["mae"], mae)
        self.assertAlmostEqual(result["metrics"]["mse"], mse)
        self.assertAlmostEqual(result["metrics"]["rmse"], math.sqrt(mse))
        self.assertAlmostEqual(result["metrics"]["mase"], mae)  # train first differences are exactly 1.

    def test_test_targets_do_not_influence_first_forecast(self):
        first, first_output = self.run_fixture(label="before")
        changed = self.values[:]
        changed[96:] = [value + 10000 for value in changed[96:]]
        self.write_data(values=changed)
        second, second_output = self.run_fixture(label="after")
        self.assertNotEqual(first["protocol"]["dataset_sha256"], second["protocol"]["dataset_sha256"])
        first_predictions = self.predictions(first_output)
        second_predictions = self.predictions(second_output)
        for left, right in zip(first_predictions[:6], second_predictions[:6]):
            self.assertEqual(float(left["y_pred"]), float(right["y_pred"]))
            self.assertNotEqual(float(left["y_true"]), float(right["y_true"]))

    def test_validation_gap_does_not_enter_fit(self):
        _, before = self.run_fixture(label="before_gap")
        changed = self.values[:]
        changed[72:96] = [1000000.0] * 24
        self.write_data(values=changed)
        _, after = self.run_fixture(label="after_gap")
        for left, right in zip(self.predictions(before), self.predictions(after)):
            self.assertEqual(float(left["y_pred"]), float(right["y_pred"]))

    def test_invalid_timestamps_are_rejected(self):
        cases = {}
        duplicate = self.timestamps[:]
        duplicate[40] = duplicate[39]
        cases["duplicate"] = duplicate
        out_of_order = self.timestamps[:]
        out_of_order[40], out_of_order[41] = out_of_order[41], out_of_order[40]
        cases["out_of_order"] = out_of_order
        malformed = self.timestamps[:]
        malformed[40] = "not-a-time"
        cases["malformed"] = malformed
        for label, timestamps in cases.items():
            with self.subTest(label=label):
                self.write_data(timestamps=timestamps)
                with self.assertRaises(ValueError):
                    self.run_fixture(label="bad_time_" + label)

    def test_nonfinite_values_are_rejected(self):
        for label, invalid in [("nan", float("nan")), ("positive_infinity", float("inf")),
                               ("negative_infinity", float("-inf"))]:
            with self.subTest(label=label):
                changed = self.values[:]
                changed[98] = invalid
                self.write_data(values=changed)
                with self.assertRaises(ValueError):
                    self.run_fixture(label=label)

    def test_overlapping_splits_and_impossible_windows_are_rejected(self):
        mutations = [
            ("train overlaps test", {"data": {"train_end": 100, "test_start": 96}}),
            ("no full train window", {"data": {"train_end": 10}}),
            ("no full test horizon", {"evaluation": {"horizon": 30}}),
            ("nonpositive stride", {"evaluation": {"stride": 0}}),
        ]
        for index, (label, mutation) in enumerate(mutations):
            with self.subTest(label=label):
                config = copy.deepcopy(self.config)
                for section, values in mutation.items():
                    config[section].update(values)
                with self.assertRaises(ValueError):
                    self.run_fixture(config, label="bad_split_" + str(index))

    def test_compare_accepts_same_protocol(self):
        first, first_output = self.run_fixture(label="compare_first")
        second, second_output = self.run_fixture(label="compare_second")
        self.assertEqual(first["protocol"], second["protocol"])
        markdown = compare_results([first_output, second_output])
        self.assertIsInstance(markdown, str)
        self.assertIn("NaiveMean", markdown)
        self.assertIn("|", markdown)

    def test_compare_rejects_changed_protocol(self):
        result, output = self.run_fixture(label="comparison_base")
        protocol_changes = {
            "dataset_sha256": "0" * 64,
            "time_column": "another_timestamp",
            "columns": ["other"],
            "train_end": 71,
            "test_start": 97,
            "lookback": 11,
            "horizon": 3,
            "stride": 3,
            "origins": [97, 103, 109, 115],
            "metric_scale": "standardized",
            "history_policy": "refit_on_test",
            "mase_period": 2,
            "missing_policy": "interpolate",
        }
        for index, (field, changed) in enumerate(protocol_changes.items()):
            with self.subTest(field=field):
                altered = copy.deepcopy(result)
                altered["protocol"][field] = changed
                target = self.root / ("different_protocol_" + str(index))
                target.mkdir()
                (target / "metrics.json").write_text(json.dumps(altered), encoding="utf-8")
                with self.assertRaises(ValueError):
                    compare_results([output, target])


if __name__ == "__main__":
    unittest.main()
