#!/usr/bin/env python3
"""Three-channel synthetic rescue test for CEMR.

Channels:
  area/entanglement: mixes conformal geometry phi and nuisance eta;
  nuisance model: included explicitly in the joint parameter vector;
  causal channel: constrains a chosen linear combination of phi/eta, with
                  `alignment` controlling how well it targets the near-null
                  geometry-nuisance direction.

Goal: quantify how much independent causal information is needed to restore stable
geometric inference when geometry and nuisance are nearly collinear.

This is an inverse-problem benchmark only, not a physical causal-set/HRT model.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def orth(a: np.ndarray) -> np.ndarray:
    q, _ = np.linalg.qr(a)
    return q[:, : a.shape[1]]


def build(seed: int, overlap: float, n_obs: int = 30, n_modes: int = 5):
    rng = np.random.default_rng(seed)
    hp = orth(rng.normal(size=(n_obs, n_modes)))
    raw = rng.normal(size=(n_obs, n_modes))
    raw -= hp @ (hp.T @ raw)
    ho = orth(raw)
    hn = overlap * hp + np.sqrt(1.0 - overlap**2) * ho
    harea = np.concatenate([hp, hn], axis=1)
    return rng, hp, hn, harea


def stats(design: np.ndarray, sigma: np.ndarray):
    w = design / sigma[:, None]
    fisher = w.T @ w
    s = np.linalg.svd(fisher, compute_uv=False)
    positive = s[s > 1e-12 * s[0]]
    cond = float(positive[0] / positive[-1]) if len(positive) else float("inf")
    cov = np.linalg.pinv(fisher, rcond=1e-12)
    return fisher, cov, cond, s


def run(seed: int, overlap: float, alignment: float, sigma_area: float, sigma_causal: float):
    if not 0 <= alignment <= 1:
        raise ValueError("alignment must be in [0,1]")
    rng, hp, hn, harea = build(seed, overlap)
    n_modes = hp.shape[1]

    phi = np.asarray([0.18, -0.10, 0.07, 0.04, -0.03])[:n_modes]
    eta = np.asarray([0.05, -0.03, 0.02, 0.01, -0.015])[:n_modes]
    theta = np.concatenate([phi, eta])

    # The approximate dangerous direction for highly overlapping responses is
    # phi ~ -eta. Build causal rows aligned with that difference direction.
    h_target = np.concatenate([np.eye(n_modes), -np.eye(n_modes)], axis=1) / np.sqrt(2.0)

    # Orthogonal control direction that mainly measures the sum phi+eta.
    h_control = np.concatenate([np.eye(n_modes), np.eye(n_modes)], axis=1) / np.sqrt(2.0)
    hcausal = alignment * h_target + np.sqrt(1.0 - alignment**2) * h_control

    y_area = harea @ theta + rng.normal(0, sigma_area, size=harea.shape[0])
    y_causal = hcausal @ theta + rng.normal(0, sigma_causal, size=hcausal.shape[0])

    sigma_a = np.full(harea.shape[0], sigma_area)
    _, cov_area, cond_area, s_area = stats(harea, sigma_a)
    theta_area = np.linalg.pinv(harea / sigma_area, rcond=1e-12) @ (y_area / sigma_area)

    h_joint = np.vstack([harea, hcausal])
    sigma_joint = np.concatenate([sigma_a, np.full(hcausal.shape[0], sigma_causal)])
    weighted = h_joint / sigma_joint[:, None]
    y_weighted = np.concatenate([y_area, y_causal]) / sigma_joint
    _, cov_joint, cond_joint, s_joint = stats(h_joint, sigma_joint)
    theta_joint = np.linalg.pinv(weighted, rcond=1e-12) @ y_weighted

    rmse_area = float(np.sqrt(np.mean((theta_area[:n_modes] - phi) ** 2)))
    rmse_joint = float(np.sqrt(np.mean((theta_joint[:n_modes] - phi) ** 2)))
    var_area = float(np.trace(cov_area[:n_modes, :n_modes]))
    var_joint = float(np.trace(cov_joint[:n_modes, :n_modes]))

    smallest_area = float(s_area[-1])
    smallest_joint = float(s_joint[-1])

    return {
        "test": "CEMR_THREE_CHANNEL_CAUSAL_RESCUE",
        "seed": seed,
        "overlap": overlap,
        "alignment": alignment,
        "sigma_area": sigma_area,
        "sigma_causal": sigma_causal,
        "area_plus_nuisance": {
            "condition_number": cond_area,
            "smallest_fisher_singular_value": smallest_area,
            "phi_covariance_trace": var_area,
            "phi_rmse": rmse_area,
        },
        "with_causal_channel": {
            "condition_number": cond_joint,
            "smallest_fisher_singular_value": smallest_joint,
            "phi_covariance_trace": var_joint,
            "phi_rmse": rmse_joint,
        },
        "rescue": {
            "condition_improvement_factor": cond_area / cond_joint,
            "smallest_singular_value_gain": smallest_joint / smallest_area if smallest_area > 0 else float("inf"),
            "phi_variance_reduction_factor": var_area / var_joint if var_joint > 0 else float("inf"),
            "phi_rmse_improvement_factor": rmse_area / rmse_joint if rmse_joint > 0 else float("inf"),
        },
        "claim_lock": (
            "Causal rows are synthetic proxy constraints. A physical rescue claim requires "
            "a source-defined causal observable in the same regime and an independent mapping."
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--overlap", type=float, default=0.99)
    p.add_argument("--alignment", type=float, default=1.0)
    p.add_argument("--sigma-area", type=float, default=0.02)
    p.add_argument("--sigma-causal", type=float, default=0.05)
    p.add_argument("--output", type=Path)
    a = p.parse_args()
    out = run(a.seed, a.overlap, a.alignment, a.sigma_area, a.sigma_causal)
    text = json.dumps(out, indent=2, sort_keys=True)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
