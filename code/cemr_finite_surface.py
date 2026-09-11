#!/usr/bin/env python3
"""Synthetic finite-surface CEMR inverse problem.

The physical metric is represented as g = exp(2 phi(x)) g_bar on a 1D chart used
only as a controlled inversion laboratory. Finite codimension-2 patch areas are
modeled by positive kernels w_i(x):

    A_i = integral w_i(x) exp(2 phi(x)) dx.

This is not a spacetime solution or an HRT solver. It tests identifiability,
conditioning, nuisance absorption, and scalar-conformal incompatibility.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares


def basis(x: np.ndarray) -> np.ndarray:
    return np.column_stack(
        [
            np.ones_like(x),
            np.sin(np.pi * x),
            np.cos(np.pi * x),
            np.sin(2.0 * np.pi * x),
            np.cos(2.0 * np.pi * x),
        ]
    )


def make_kernels(x: np.ndarray, n_patches: int) -> tuple[np.ndarray, np.ndarray]:
    if n_patches < 10 or n_patches % 2:
        raise ValueError("n_patches must be even and >= 10")
    half = n_patches // 2
    centers = np.linspace(-0.9, 0.9, half)
    widths = np.linspace(0.15, 0.32, half)
    kernels = []
    orientations = []
    for center, width in zip(centers, widths):
        base = np.exp(-0.5 * ((x - center) / width) ** 2)
        for orientation in (-1.0, 1.0):
            # Known reference-geometry orientation response. The hidden
            # anisotropic scenario adds an additional unmodeled response later.
            kernel = base * (1.0 + 0.15 * orientation * x)
            kernels.append(kernel)
            orientations.append(orientation)
    return np.asarray(kernels), np.asarray(orientations)


def integrate(y: np.ndarray, x: np.ndarray) -> float:
    return float(np.trapezoid(y, x))


def forward(phi: np.ndarray, kernels: np.ndarray, x: np.ndarray) -> np.ndarray:
    scale = np.exp(2.0 * phi)
    return np.asarray([integrate(w * scale, x) for w in kernels])


def run(seed: int, scenario: str, n_grid: int = 500, n_patches: int = 18) -> dict:
    if scenario not in {"clean", "noise", "qes", "anisotropic", "wrong_class"}:
        raise ValueError(f"unknown scenario: {scenario}")

    rng = np.random.default_rng(seed)
    x = np.linspace(-1.0, 1.0, n_grid)
    B = basis(x)
    true_coeff = np.asarray([math.log(1.35), 0.12, -0.09, 0.05, 0.03])
    phi_true = B @ true_coeff
    kernels, orientations = make_kernels(x, n_patches)

    area_true = forward(phi_true, kernels, x)
    frac_sigma = 0.01
    nuisance = np.zeros_like(area_true)
    generated = area_true.copy()

    if scenario == "noise":
        frac_sigma = 0.02
    elif scenario == "qes":
        # A structured additive correction that the leading-area inversion does
        # not model. This tests whether nuisance can bias phi without producing
        # a decisive goodness-of-fit failure.
        nuisance = 0.03 * area_true * np.sin(np.linspace(0.0, np.pi, len(area_true)))
    elif scenario == "anisotropic":
        frac_sigma = 0.005
        # Hidden orientation-dependent response: impossible for one scalar
        # conformal field to reproduce once orientation pairs overlap.
        generated = area_true * (1.0 + 0.08 * orientations)
    elif scenario == "wrong_class":
        generated = area_true * (
            1.0 + 0.06 * orientations * np.linspace(-1.0, 1.0, len(area_true))
        )

    sigma = frac_sigma * area_true
    observed = generated + nuisance + rng.normal(0.0, sigma)
    if np.any(observed <= 0.0):
        raise RuntimeError("synthetic observed area became non-positive")

    def prediction(coeff: np.ndarray) -> np.ndarray:
        return forward(B @ coeff, kernels, x)

    def residual(coeff: np.ndarray) -> np.ndarray:
        pred = prediction(coeff)
        # Log residual is approximately fractional for small discrepancies.
        return np.log(pred / observed) / frac_sigma

    fit = least_squares(residual, np.zeros(B.shape[1]), max_nfev=800)
    pred = prediction(fit.x)
    chi2 = float(np.sum(residual(fit.x) ** 2))
    dof = int(len(observed) - len(fit.x))
    reduced_chi2 = chi2 / dof
    phi_fit = B @ fit.x
    phi_rmse = float(np.sqrt(np.mean((phi_fit - phi_true) ** 2)))
    omega_rmse = float(
        np.sqrt(np.mean((np.exp(phi_fit) - np.exp(phi_true)) ** 2))
    )

    jtj = fit.jac.T @ fit.jac
    condition_number = float(np.linalg.cond(jtj))

    if reduced_chi2 <= 2.0:
        compatibility = "FIT_COMPATIBLE"
    elif reduced_chi2 <= 6.0:
        compatibility = "FIT_TENSION"
    else:
        compatibility = "FIT_INCOMPATIBLE"

    # Truth-aware campaign label. This is only possible in a synthetic study.
    if phi_rmse < 0.03:
        recovery = "RECOVERED"
    elif phi_rmse < 0.08:
        recovery = "BIASED"
    else:
        recovery = "FAILED_RECOVERY"

    return {
        "test": "CEMR_FINITE_SURFACE_SYNTHETIC_INVERSION",
        "seed": seed,
        "scenario": scenario,
        "n_grid": n_grid,
        "n_patches": n_patches,
        "n_parameters": int(B.shape[1]),
        "fractional_sigma": frac_sigma,
        "solver_success": bool(fit.success),
        "solver_message": str(fit.message),
        "true_coefficients": true_coeff.tolist(),
        "fitted_coefficients": fit.x.tolist(),
        "phi_rmse": phi_rmse,
        "omega_rmse": omega_rmse,
        "chi2": chi2,
        "dof": dof,
        "reduced_chi2": reduced_chi2,
        "normal_matrix_condition_number": condition_number,
        "compatibility_verdict": compatibility,
        "truth_recovery_verdict": recovery,
        "max_fractional_area_residual": float(np.max(np.abs(pred / observed - 1.0))),
        "mean_abs_fractional_area_residual": float(np.mean(np.abs(pred / observed - 1.0))),
        "claim_lock": (
            "This is a synthetic inverse-problem stress test, not an HRT calculation, "
            "not evidence for a quantum-gravity model, and not a family-level test."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument(
        "--scenario",
        choices=["clean", "noise", "qes", "anisotropic", "wrong_class"],
        default="clean",
    )
    parser.add_argument("--n-grid", type=int, default=500)
    parser.add_argument("--n-patches", type=int, default=18)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    result = run(args.seed, args.scenario, args.n_grid, args.n_patches)
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
