#!/usr/bin/env python3
"""Synthetic nuisance-identifiability audit for CEMR.

Linearized observation model:
    y = H_phi phi + H_n eta + noise
where phi is geometric conformal-scale information and eta is a QES/generalized-
entropy-like nuisance contribution. `overlap` controls how parallel the nuisance
response is to the geometric response.

This is an inverse-problem benchmark only. H_n is not a physical QES calculation.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def orthonormal_columns(a: np.ndarray) -> np.ndarray:
    q, _ = np.linalg.qr(a)
    return q[:, : a.shape[1]]


def make_design(seed: int, overlap: float, n_obs: int = 30, n_modes: int = 5):
    if not 0.0 <= overlap < 1.0:
        raise ValueError("overlap must be in [0,1)")
    rng = np.random.default_rng(seed)
    h_phi = orthonormal_columns(rng.normal(size=(n_obs, n_modes)))

    raw = rng.normal(size=(n_obs, n_modes))
    raw = raw - h_phi @ (h_phi.T @ raw)
    h_orth = orthonormal_columns(raw)
    h_n = overlap * h_phi + np.sqrt(1.0 - overlap**2) * h_orth
    return rng, h_phi, h_n


def fit(design: np.ndarray, y: np.ndarray, sigma: float):
    theta = np.linalg.pinv(design, rcond=1e-12) @ y
    resid = (design @ theta - y) / sigma
    chi2 = float(resid @ resid)
    dof = max(1, design.shape[0] - design.shape[1])
    fisher = design.T @ design / sigma**2
    cov = np.linalg.pinv(fisher, rcond=1e-12)
    s = np.linalg.svd(fisher, compute_uv=False)
    positive = s[s > 1e-12 * s[0]]
    cond = float(positive[0] / positive[-1]) if len(positive) else float("inf")
    return theta, chi2 / dof, cov, cond


def run(seed: int, overlap: float, nuisance_snr: float, sigma: float = 0.02):
    rng, h_phi, h_n = make_design(seed, overlap)
    n_modes = h_phi.shape[1]
    phi_true = np.asarray([0.18, -0.10, 0.07, 0.04, -0.03])[:n_modes]
    eta_dir = np.asarray([0.5, -0.3, 0.2, 0.1, -0.15])[:n_modes]
    eta_dir = eta_dir / np.linalg.norm(eta_dir)

    # Choose eta so RMS nuisance response is nuisance_snr * sigma.
    unit_response = h_n @ eta_dir
    eta_scale = nuisance_snr * sigma / np.sqrt(np.mean(unit_response**2))
    eta_true = eta_scale * eta_dir

    y_clean = h_phi @ phi_true + h_n @ eta_true
    y = y_clean + rng.normal(0.0, sigma, size=h_phi.shape[0])

    # Geometry-only fit: ignores nuisance.
    phi_only, chi2_only, cov_only, cond_only = fit(h_phi, y, sigma)

    # Joint fit: attempts to separate geometry and nuisance.
    h_joint = np.concatenate([h_phi, h_n], axis=1)
    theta_joint, chi2_joint, cov_joint, cond_joint = fit(h_joint, y, sigma)
    phi_joint = theta_joint[:n_modes]
    eta_joint = theta_joint[n_modes:]

    rmse_only = float(np.sqrt(np.mean((phi_only - phi_true) ** 2)))
    rmse_joint = float(np.sqrt(np.mean((phi_joint - phi_true) ** 2)))
    eta_rmse = float(np.sqrt(np.mean((eta_joint - eta_true) ** 2)))

    geom_var_only = float(np.trace(cov_only))
    geom_var_joint = float(np.trace(cov_joint[:n_modes, :n_modes]))
    inflation = geom_var_joint / geom_var_only if geom_var_only > 0 else float("inf")

    return {
        "test": "CEMR_NUISANCE_IDENTIFIABILITY",
        "seed": seed,
        "overlap": overlap,
        "nuisance_snr": nuisance_snr,
        "sigma": sigma,
        "geometry_only": {
            "reduced_chi2": chi2_only,
            "phi_rmse": rmse_only,
            "condition_number": cond_only,
            "geometry_covariance_trace": geom_var_only,
        },
        "joint_geometry_nuisance": {
            "reduced_chi2": chi2_joint,
            "phi_rmse": rmse_joint,
            "eta_rmse": eta_rmse,
            "condition_number": cond_joint,
            "geometry_covariance_trace": geom_var_joint,
            "geometry_variance_inflation_factor": inflation,
        },
        "bias_reduction_factor": rmse_only / rmse_joint if rmse_joint > 0 else float("inf"),
        "identifiability_warning": bool(cond_joint > 1e3 or inflation > 100.0),
        "claim_lock": (
            "Synthetic nuisance basis only. Physical QES/generalized-entropy corrections "
            "must be derived from the same realization before CEMR interpretation."
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--overlap", type=float, default=0.8)
    p.add_argument("--nuisance-snr", type=float, default=1.0)
    p.add_argument("--sigma", type=float, default=0.02)
    p.add_argument("--output", type=Path, default=None)
    a = p.parse_args()
    result = run(a.seed, a.overlap, a.nuisance_snr, a.sigma)
    text = json.dumps(result, indent=2, sort_keys=True)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
