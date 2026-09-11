#!/usr/bin/env python3
"""Synthetic information-gain benchmark for BH-002 CEMR.

This code does NOT model a physical HRT or causal-set experiment. It asks a narrower
inverse-problem question: if area/entanglement data mix conformal-scale modes with
light-cone/shear modes, does an independent causal channel that constrains the latter
improve rank, conditioning, and conformal-parameter recovery?
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def make_problem(seed: int, degeneracy: float, n_modes: int = 5, n_area: int = 24):
    if not 0.0 <= degeneracy < 1.0:
        raise ValueError("degeneracy must be in [0,1)")
    rng = np.random.default_rng(seed)

    # Orthonormal-ish conformal sensitivity block.
    a = rng.normal(size=(n_area, n_modes))
    qa, _ = np.linalg.qr(a)
    h_phi = qa[:, :n_modes]

    # The nonconformal/light-cone sensitivity becomes nearly parallel to the
    # conformal sensitivity as degeneracy -> 1, creating an area-only ambiguity.
    b = rng.normal(size=(n_area, n_modes))
    qb, _ = np.linalg.qr(b - h_phi @ (h_phi.T @ b))
    h_q = degeneracy * h_phi + np.sqrt(max(1.0 - degeneracy**2, 0.0)) * qb[:, :n_modes]

    h_area = np.concatenate([h_phi, h_q], axis=1)

    # Causal channel observes only q/light-cone modes in this proxy.
    h_causal = np.concatenate([np.zeros((n_modes, n_modes)), np.eye(n_modes)], axis=1)

    true_phi = np.array([0.18, -0.10, 0.07, 0.04, -0.03])[:n_modes]
    true_q = np.array([0.08, -0.05, 0.03, -0.02, 0.01])[:n_modes]
    theta = np.concatenate([true_phi, true_q])
    return rng, h_area, h_causal, theta


def stable_rank(a: np.ndarray, rtol: float = 1e-10) -> int:
    s = np.linalg.svd(a, compute_uv=False)
    return int(np.sum(s > rtol * s[0])) if len(s) else 0


def fisher_stats(h: np.ndarray, sigma: float) -> dict:
    f = h.T @ h / sigma**2
    s = np.linalg.svd(f, compute_uv=False)
    rank = stable_rank(f)
    positive = s[s > 1e-12 * s[0]] if len(s) else np.asarray([])
    cond = float(positive[0] / positive[-1]) if len(positive) else float("inf")
    cov = np.linalg.pinv(f, rcond=1e-12)
    return {"fisher": f, "rank": rank, "condition_number": cond, "covariance": cov}


def run(seed: int, degeneracy: float, sigma_area: float, sigma_causal: float) -> dict:
    rng, h_area, h_causal, theta_true = make_problem(seed, degeneracy)
    n_modes = h_causal.shape[0]

    y_area = h_area @ theta_true + rng.normal(0.0, sigma_area, size=h_area.shape[0])
    y_causal = h_causal @ theta_true + rng.normal(0.0, sigma_causal, size=h_causal.shape[0])

    area_stats = fisher_stats(h_area, sigma_area)
    h_joint = np.vstack([h_area / sigma_area, h_causal / sigma_causal])
    y_joint = np.concatenate([y_area / sigma_area, y_causal / sigma_causal])
    joint_stats = fisher_stats(h_joint, 1.0)

    theta_area = np.linalg.pinv(h_area, rcond=1e-12) @ y_area
    theta_joint = np.linalg.pinv(h_joint, rcond=1e-12) @ y_joint

    phi_true = theta_true[:n_modes]
    phi_area = theta_area[:n_modes]
    phi_joint = theta_joint[:n_modes]

    phi_rmse_area = float(np.sqrt(np.mean((phi_area - phi_true) ** 2)))
    phi_rmse_joint = float(np.sqrt(np.mean((phi_joint - phi_true) ** 2)))

    area_phi_var = float(np.trace(area_stats["covariance"][:n_modes, :n_modes]))
    joint_phi_var = float(np.trace(joint_stats["covariance"][:n_modes, :n_modes]))
    variance_gain = area_phi_var / joint_phi_var if joint_phi_var > 0 else float("inf")
    rmse_gain = phi_rmse_area / phi_rmse_joint if phi_rmse_joint > 0 else float("inf")

    return {
        "test": "CEMR_CAUSAL_CHANNEL_INFORMATION_GAIN",
        "seed": seed,
        "degeneracy": degeneracy,
        "sigma_area": sigma_area,
        "sigma_causal": sigma_causal,
        "n_parameters": int(h_area.shape[1]),
        "area_only": {
            "fisher_rank": area_stats["rank"],
            "condition_number": area_stats["condition_number"],
            "phi_covariance_trace": area_phi_var,
            "phi_rmse": phi_rmse_area,
        },
        "joint_area_plus_causal": {
            "fisher_rank": joint_stats["rank"],
            "condition_number": joint_stats["condition_number"],
            "phi_covariance_trace": joint_phi_var,
            "phi_rmse": phi_rmse_joint,
        },
        "information_gain": {
            "rank_gain": int(joint_stats["rank"] - area_stats["rank"]),
            "phi_variance_reduction_factor": variance_gain,
            "phi_rmse_improvement_factor": rmse_gain,
        },
        "interpretation_lock": (
            "The causal block is an abstract independent light-cone/shear constraint. "
            "A physical CEMR claim requires a source-defined causal observable and a "
            "same-regime mapping to the entanglement data."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--degeneracy", type=float, default=0.99)
    parser.add_argument("--sigma-area", type=float, default=0.02)
    parser.add_argument("--sigma-causal", type=float, default=0.05)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    result = run(args.seed, args.degeneracy, args.sigma_area, args.sigma_causal)
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
