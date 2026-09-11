#!/usr/bin/env python3
"""Synthetic regression tests for CEMR local conformal consistency."""

import unittest

from cemr_local_consistency import evaluate


class TestCEMRLocalConsistency(unittest.TestCase):
    def test_consistent_common_conformal_factor(self):
        # D=4, G=1, Omega=2 -> A_obs/A_ref = Omega^2 = 4.
        # Since A_obs=4 G S, choose S=A_ref.
        payload = {
            "dimension": 4,
            "G_N": 1.0,
            "sigma_G_N": 0.005,
            "patches": [
                {"id": "x", "reference_area": 1.0, "entropy": 1.0,
                 "sigma_reference_area": 0.01, "sigma_entropy": 0.01},
                {"id": "y", "reference_area": 2.0, "entropy": 2.0,
                 "sigma_reference_area": 0.02, "sigma_entropy": 0.02},
                {"id": "z", "reference_area": 3.0, "entropy": 3.0,
                 "sigma_reference_area": 0.03, "sigma_entropy": 0.03},
            ],
        }
        result = evaluate(payload)
        self.assertEqual(result["status"], "PASS_LOCAL")
        self.assertAlmostEqual(result["common_omega_estimate"], 2.0, places=12)
        self.assertAlmostEqual(result["chi2"], 0.0, places=12)

    def test_orientation_dependent_scale_is_incompatible(self):
        payload = {
            "dimension": 4,
            "G_N": 1.0,
            "sigma_G_N": 0.001,
            "patches": [
                {"id": "x", "reference_area": 1.0, "entropy": 1.0,
                 "sigma_reference_area": 0.002, "sigma_entropy": 0.002},
                {"id": "y", "reference_area": 2.0, "entropy": 2.0,
                 "sigma_reference_area": 0.004, "sigma_entropy": 0.004},
                {"id": "z", "reference_area": 3.0, "entropy": 4.5,
                 "sigma_reference_area": 0.006, "sigma_entropy": 0.006},
            ],
        }
        result = evaluate(payload)
        self.assertEqual(result["status"], "INCOMPATIBLE_LOCAL")
        self.assertGreater(result["reduced_chi2"], 4.0)

    def test_requires_at_least_two_patches(self):
        with self.assertRaises(ValueError):
            evaluate({
                "dimension": 4,
                "G_N": 1.0,
                "patches": [{"reference_area": 1.0, "entropy": 1.0}],
            })


if __name__ == "__main__":
    unittest.main()
