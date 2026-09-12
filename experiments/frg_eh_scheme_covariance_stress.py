#!/usr/bin/env python3
"""Einstein-Hilbert asymptotic-safety scheme/covariance stress test.

Two standard d=4 Einstein-Hilbert beta-function realizations are implemented in
common dimensionless coordinates (g, lambda):

1. optimized/Litim threshold functions, using the standard general EH flow
   beta_g=(2+eta)g and beta_lambda with Phi/tilde-Phi threshold functions;
2. the sharp-cutoff analytic flow quoted in the Reuter/Saueressig literature.

This script finds the positive non-Gaussian fixed point (NGFP), computes the
numerical stability matrix, critical exponents theta=-eig(J), the often-quoted
product g_* lambda_*, and the dominant right-singular direction of the local
Jacobian.

The comparison is a truncation/scheme covariance diagnostic only. Raw vectors
in coupling coordinates are not claimed to be universal observables.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import root
from scipy.special import zeta


def phi(n: float, p: int, w: float) -> float:
    return 1.0 / math.gamma(n + 1.0) / (1.0 + w) ** p


def tphi(n: float, p: int, w: float) -> float:
    return 1.0 / math.gamma(n + 2.0) / (1.0 + w) ** p


def beta_litim(x: np.ndarray) -> np.ndarray:
    g, lam = map(float, x)
    if 1.0 - 2.0 * lam <= 0.0:
        return np.array([1e6, 1e6])
    B1 = (
        20.0 * phi(1, 1, -2 * lam)
        - 72.0 * phi(2, 2, -2 * lam)
        - 16.0 * phi(1, 1, 0.0)
        - 24.0 * phi(2, 2, 0.0)
    ) / (12.0 * math.pi)
    B2 = -(
        20.0 * tphi(1, 1, -2 * lam)
        - 72.0 * tphi(2, 2, -2 * lam)
    ) / (24.0 * math.pi)
    eta = g * B1 / (1.0 - g * B2)
    bg = (2.0 + eta) * g
    bl = -(2.0 - eta) * lam + (g / (8.0 * math.pi)) * (
        40.0 * phi(2, 1, -2 * lam)
        - 32.0 * phi(2, 1, 0.0)
        - 20.0 * eta * tphi(2, 1, -2 * lam)
    )
    return np.array([bg, bl], dtype=float)


def beta_sharp(x: np.ndarray) -> np.ndarray:
    g, lam = map(float, x)
    if 1.0 - 2.0 * lam <= 0.0:
        return np.array([1e6, 1e6])
    eta = -(2.0 * g / (6.0 * math.pi + 5.0 * g)) * (
        18.0 / (1.0 - 2.0 * lam)
        + 5.0 * math.log(1.0 - 2.0 * lam)
        - float(zeta(2))
        + 6.0
    )
    bg = (2.0 + eta) * g
    bl = -(2.0 - eta) * lam - (g / math.pi) * (
        5.0 * math.log(1.0 - 2.0 * lam)
        - 2.0 * float(zeta(3))
        + 1.25 * eta
    )
    return np.array([bg, bl], dtype=float)


def find_ngfp(beta) -> np.ndarray:
    guesses = [(0.4, 0.2), (0.7, 0.2), (1.0, 0.15), (0.5, 0.3), (1.2, 0.1)]
    sols = []
    for guess in guesses:
        sol = root(beta, np.asarray(guess, float), method='hybr')
        if not sol.success:
            continue
        x = np.asarray(sol.x, float)
        if not np.all(np.isfinite(x)):
            continue
        if x[0] <= 1e-8 or not (-5.0 < x[1] < 0.499):
            continue
        if np.linalg.norm(beta(x)) > 1e-7:
            continue
        if not any(np.linalg.norm(x-y) < 1e-5 for y in sols):
            sols.append(x)
    if not sols:
        raise RuntimeError('no positive NGFP found')
    # Prefer the regular fixed point farthest from the lambda=1/2 singular wall.
    sols.sort(key=lambda x: (x[1] > 0.4, abs(x[0]) + abs(x[1])))
    return sols[0]


def jacobian(beta, x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, float)
    J = np.zeros((2, 2), float)
    for i in range(2):
        h = 2e-6 * max(1.0, abs(x[i]))
        d = np.zeros(2); d[i] = h
        J[:, i] = (beta(x + d) - beta(x - d)) / (2.0 * h)
    return J


def analyze(name: str, beta) -> dict:
    fp = find_ngfp(beta)
    J = jacobian(beta, fp)
    evals = np.linalg.eigvals(J)
    theta = -evals
    u, s, vh = np.linalg.svd(J)
    v = vh[0].astype(float)
    # Fix arbitrary sign for reproducible angle comparison.
    if v[0] < 0:
        v = -v
    return {
        'scheme': name,
        'fixed_point': {'g': float(fp[0]), 'lambda': float(fp[1]), 'g_lambda_product': float(fp[0]*fp[1])},
        'beta_residual_norm': float(np.linalg.norm(beta(fp))),
        'stability_matrix': J.tolist(),
        'critical_exponents': [
            {'real': float(z.real), 'imag': float(z.imag)} for z in theta
        ],
        'jacobian_singular_values': s.tolist(),
        'dominant_right_singular_direction_g_lambda': v.tolist(),
    }


def main() -> None:
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
    lit=analyze('optimized_Litim_EH',beta_litim)
    sharp=analyze('sharp_cutoff_EH',beta_sharp)
    v1=np.asarray(lit['dominant_right_singular_direction_g_lambda'],float)
    v2=np.asarray(sharp['dominant_right_singular_direction_g_lambda'],float)
    cos=float(np.clip(abs(np.dot(v1,v2))/(np.linalg.norm(v1)*np.linalg.norm(v2)),0,1))
    angle=float(math.degrees(math.acos(cos)))
    p1=lit['fixed_point']['g_lambda_product']; p2=sharp['fixed_point']['g_lambda_product']
    product_rel_spread=float(abs(p1-p2)/((abs(p1)+abs(p2))/2.0))
    r1=sorted(abs(x['real']) for x in lit['critical_exponents'])
    r2=sorted(abs(x['real']) for x in sharp['critical_exponents'])
    out={
        'test':'ASYMPTOTIC_SAFETY_EH_SCHEME_COVARIANCE_STRESS',
        'status':'PASS_EXECUTION',
        'litim':lit,'sharp':sharp,
        'cross_scheme':{
            'g_lambda_product_relative_spread':product_rel_spread,
            'dominant_jacobian_right_singular_direction_angle_deg':angle,
            'both_ngfp_positive_g_below_lambda_wall':bool(
                lit['fixed_point']['g']>0 and sharp['fixed_point']['g']>0 and
                lit['fixed_point']['lambda']<0.5 and sharp['fixed_point']['lambda']<0.5),
            'both_uv_relevant_real_parts_positive':bool(
                all(x['real']>0 for x in lit['critical_exponents']) and
                all(x['real']>0 for x in sharp['critical_exponents'])),
        },
        'claim_lock':(
            'Einstein-Hilbert truncation/regulator comparison only. Stability-vector coordinates are scheme/parameterization dependent and are not universal observables. '
            'This test neither proves asymptotic safety nor identifies RM-001 with an FRG eigendirection.'
        ),
        'sources':[
            'Reuter and Saueressig, Phys.Rev.D 65, 065016 (2002), sharp-cutoff Einstein-Hilbert flow.',
            'Standard Einstein-Hilbert FRG flow with optimized/Litim threshold functions as summarized in asymptotic-safety reviews.'
        ]
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out['cross_scheme'],indent=2,sort_keys=True))
    print(json.dumps({'litim_fp':lit['fixed_point'],'sharp_fp':sharp['fixed_point'],'litim_theta':lit['critical_exponents'],'sharp_theta':sharp['critical_exponents']},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
