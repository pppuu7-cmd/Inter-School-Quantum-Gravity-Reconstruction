#!/usr/bin/env python3
"""Finite-surface inverse problem for BH-002 / CEMR.

Scope
-----
This is a deliberately controlled Stage-I calculation.  The codimension-two
surfaces are fixed in a reference geometry; they are NOT re-extremized after
changing the conformal factor.  It therefore tests conformal-scale
identifiability and incompatibility, not the full RT/QES inverse problem.

In D=4 the physical area of a fixed surface is

    A[Omega] = integral_Sigma Omega(x,y)^2 dA_bar.

We parameterize

    log Omega = theta0 + theta1*x + theta2*y + theta3*x*y

and fit redundant finite-area observations in log space.  Four scenarios are
implemented:

* clean_calibrated       -- calibrated areas, scalar conformal model is true;
* global_scale_nuisance  -- add an unknown global log-area calibration beta;
                            this is exactly degenerate with theta0;
* channel_anisotropy     -- inject +/- epsilon channel distortion that cannot
                            be represented by a scalar conformal factor when
                            the same geometric surface is measured in both
                            channels;
* channel_profiled       -- fit an explicit channel nuisance alpha and test
                            whether the apparent conformal inconsistency closes.

The code is fail-closed: a rank-deficient inverse problem is reported as
BLOCKED_NONIDENTIFIABLE rather than interpreted as evidence against CEMR.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import least_squares


SCENARIOS = {
    "clean_calibrated",
    "global_scale_nuisance",
    "channel_anisotropy",
    "channel_profiled",
}

# The Jacobian is obtained by finite differences inside scipy. Exact analytic
# degeneracies therefore acquire tiny numerical singular values. We treat a
# direction as unresolved when its singular value is below 1e-8 of the leading
# one. This is deliberately much looser than machine epsilon but still eight
# orders of magnitude below the resolved directions in the registered system.
# It is a numerical identifiability tolerance, not a fit-quality threshold.
RANK_REL_TOL = 1.0e-8


@dataclass(frozen=True)
class Surface:
    name: str
    x0: float
    x1: float
    y0: float
    y1: float
    channel: int


@dataclass
class FitSummary:
    scenario: str
    seed: int
    epsilon: float
    sigma_log_area: float
    theta_true: list[float]
    theta_fit: list[float]
    nuisance_fit: float | None
    chi2: float
    dof: int
    reduced_chi2: float | None
    jacobian_rank: int
    n_parameters: int
    singular_values: list[float]
    condition_number: float | None
    max_abs_theta_error: float
    classification: str
    notes: list[str]


THETA_TRUE = np.array([0.18, 0.11, -0.07, 0.04], dtype=float)

# Deliberately redundant geometry. Each base rectangle is observed twice with
# opposite channel labels. A genuine scalar conformal factor predicts the same
# geometric area for both copies; a channel-dependent distortion cannot be
# absorbed by changing Omega.
_BASE_RECTS = [
    ("q_sw", -1.00, -0.15, -1.00, -0.20),
    ("q_se", 0.10, 1.00, -1.00, -0.15),
    ("q_nw", -1.00, -0.10, 0.15, 1.00),
    ("q_ne", 0.15, 1.00, 0.10, 1.00),
    ("h_mid", -0.80, 0.75, -0.25, 0.20),
    ("v_mid", -0.20, 0.25, -0.85, 0.80),
    ("diag_a", -0.85, 0.35, -0.70, 0.35),
    ("diag_b", -0.30, 0.90, -0.25, 0.85),
    ("wide_s", -0.95, 0.95, -0.90, -0.45),
    ("wide_n", -0.95, 0.95, 0.45, 0.90),
    ("west", -0.90, -0.45, -0.95, 0.95),
    ("east", 0.45, 0.90, -0.95, 0.95),
]


def surfaces() -> list[Surface]:
    out: list[Surface] = []
    for name, x0, x1, y0, y1 in _BASE_RECTS:
        out.append(Surface(f"{name}_minus", x0, x1, y0, y1, -1))
        out.append(Surface(f"{name}_plus", x0, x1, y0, y1, +1))
    return out


def log_omega(theta: np.ndarray, x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return theta[0] + theta[1] * x + theta[2] * y + theta[3] * x * y


def finite_area(theta: np.ndarray, surface: Surface, order: int = 18) -> float:
    """Gauss-Legendre quadrature for int exp(2 log Omega) dx dy."""
    gx, wx = leggauss(order)
    gy, wy = leggauss(order)
    xs = 0.5 * (surface.x1 - surface.x0) * gx + 0.5 * (surface.x1 + surface.x0)
    ys = 0.5 * (surface.y1 - surface.y0) * gy + 0.5 * (surface.y1 + surface.y0)
    xg, yg = np.meshgrid(xs, ys, indexing="ij")
    weights = np.outer(wx, wy)
    integrand = np.exp(2.0 * log_omega(theta, xg, yg))
    jac = 0.25 * (surface.x1 - surface.x0) * (surface.y1 - surface.y0)
    value = jac * float(np.sum(weights * integrand))
    if not np.isfinite(value) or value <= 0.0:
        raise ValueError("non-positive or non-finite conformal area")
    return value


def generate_observations(
    scenario: str,
    seed: int,
    epsilon: float,
    sigma_log_area: float,
) -> tuple[list[Surface], np.ndarray]:
    if scenario not in SCENARIOS:
        raise ValueError(f"unknown scenario: {scenario}")
    if sigma_log_area <= 0:
        raise ValueError("sigma_log_area must be positive")
    ss = surfaces()
    rng = np.random.default_rng(seed)
    logs: list[float] = []
    for s in ss:
        true_log_area = math.log(finite_area(THETA_TRUE, s))
        injected = 0.0
        if scenario in {"channel_anisotropy", "channel_profiled"}:
            injected = epsilon * float(s.channel)
        noise = float(rng.normal(0.0, sigma_log_area))
        logs.append(true_log_area + injected + noise)
    return ss, np.asarray(logs, dtype=float)


def _predicted_log_areas(params: np.ndarray, ss: Iterable[Surface], scenario: str) -> np.ndarray:
    theta = params[:4]
    nuisance = float(params[4]) if len(params) == 5 else 0.0
    pred: list[float] = []
    for s in ss:
        value = math.log(finite_area(theta, s))
        if scenario == "global_scale_nuisance":
            value += nuisance
        elif scenario == "channel_profiled":
            value += nuisance * float(s.channel)
        pred.append(value)
    return np.asarray(pred, dtype=float)


def _numerical_rank_and_condition(jac: np.ndarray) -> tuple[int, np.ndarray, float | None]:
    svals = np.linalg.svd(jac, compute_uv=False)
    if len(svals) == 0:
        return 0, svals, None
    tol = RANK_REL_TOL * svals[0]
    rank = int(np.sum(svals > tol))
    if svals[-1] <= tol:
        cond = None
    else:
        cond = float(svals[0] / svals[-1])
    return rank, svals, cond


def fit_scenario(
    scenario: str,
    seed: int = 20260912,
    epsilon: float = 0.05,
    sigma_log_area: float = 0.003,
) -> FitSummary:
    ss, observed_log = generate_observations(scenario, seed, epsilon, sigma_log_area)
    npar = 5 if scenario in {"global_scale_nuisance", "channel_profiled"} else 4
    x0 = np.zeros(npar, dtype=float)

    def residual(params: np.ndarray) -> np.ndarray:
        return (_predicted_log_areas(params, ss, scenario) - observed_log) / sigma_log_area

    result = least_squares(
        residual,
        x0,
        method="trf",
        xtol=1e-12,
        ftol=1e-12,
        gtol=1e-12,
        max_nfev=2500,
    )
    if not np.all(np.isfinite(result.x)) or not np.all(np.isfinite(result.fun)):
        raise RuntimeError("non-finite inverse solution")

    rank, svals, cond = _numerical_rank_and_condition(np.asarray(result.jac, dtype=float))
    chi2 = float(np.dot(result.fun, result.fun))
    dof = int(len(observed_log) - rank)
    reduced = chi2 / dof if dof > 0 else None
    theta_fit = np.asarray(result.x[:4], dtype=float)
    theta_error = float(np.max(np.abs(theta_fit - THETA_TRUE)))
    nuisance = float(result.x[4]) if npar == 5 else None

    notes: list[str] = [
        "Stage-I fixed-surface calculation; no extremal-surface backreaction.",
        "Absolute scale is interpretable only in the calibrated scenario.",
        f"Numerical Jacobian rank uses relative singular-value tolerance {RANK_REL_TOL:.1e}.",
    ]

    # Classification is intentionally structural before goodness-of-fit.
    if rank < npar:
        classification = "BLOCKED_NONIDENTIFIABLE"
        notes.append("Jacobian is rank deficient; no physical rejection is authorized.")
    elif scenario == "channel_anisotropy" and reduced is not None and reduced > 9.0:
        classification = "INCOMPATIBLE_SCALAR_CONFORMAL_SCOPED"
        notes.append("Duplicated surfaces disagree beyond the scalar conformal model.")
    elif reduced is not None and reduced <= 4.0:
        classification = "PASS_SCOPED"
    else:
        classification = "TENSION_SCOPED"

    if scenario == "global_scale_nuisance":
        notes.append(
            "Expected exact degeneracy: log-area response to theta0 is 2*theta0, "
            "so an unknown global log-area calibration cannot be separated from theta0."
        )
    if scenario == "channel_profiled":
        notes.append("Channel nuisance is explicitly profiled rather than attributed to geometry.")

    return FitSummary(
        scenario=scenario,
        seed=int(seed),
        epsilon=float(epsilon),
        sigma_log_area=float(sigma_log_area),
        theta_true=THETA_TRUE.tolist(),
        theta_fit=theta_fit.tolist(),
        nuisance_fit=nuisance,
        chi2=chi2,
        dof=dof,
        reduced_chi2=float(reduced) if reduced is not None else None,
        jacobian_rank=rank,
        n_parameters=npar,
        singular_values=[float(v) for v in svals],
        condition_number=cond,
        max_abs_theta_error=theta_error,
        classification=classification,
        notes=notes,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", required=True, choices=sorted(SCENARIOS))
    parser.add_argument("--seed", type=int, default=20260912)
    parser.add_argument("--epsilon", type=float, default=0.05)
    parser.add_argument("--sigma-log-area", type=float, default=0.003)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    summary = fit_scenario(
        args.scenario,
        seed=args.seed,
        epsilon=args.epsilon,
        sigma_log_area=args.sigma_log_area,
    )
    payload = json.dumps(asdict(summary), indent=2, sort_keys=True)
    print(payload)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
