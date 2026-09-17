#!/usr/bin/env python3
"""ITER162 source-derived upper open-tensor covariant reconstruction.

Prospectively consumes only the frozen ITER161 source-faithful upper_open_vertex
and the ITER162 36-column covariant span.  It does not use the ITER160 -525
residue, does not invert the scalar 28-invariant map, and does not solve ITER118.

The exact D dependence is reconstructed from D=4..8 after multiplying by the
single (D-2) denominator that is structurally present in upper_open_vertex
through exactly one pmap on the k-side R source.  D=9,10 and independent full-D
fixtures are held out.
"""
from __future__ import annotations

import json
import random
import sys
from fractions import Fraction as F
from pathlib import Path

import sympy as s

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import iter161_endpoint_open_leg_factorization as i161

SEEDS = [
    ("delta_ab", 0, 0),
    ("q_aq_b", 2, 0),
    ("q_(a_k_b)", 2, 0),
    ("k_ak_b", 2, 0),
    ("q_(a_n_b)", 1, 1),
    ("k_(a_n_b)", 1, 1),
    ("n_an_b", 0, 2),
]
VARS = [("Q", 2, 0), ("K", 2, 0), ("S", 2, 0), ("a", 1, 1), ("b", 1, 1)]


def exponent_solutions(target_deg, target_tan):
    out = []
    for eQ in range(3):
        for eK in range(3):
            for eS in range(3):
                for ea in range(5):
                    for eb in range(5):
                        es = (eQ, eK, eS, ea, eb)
                        deg = sum(e * v[1] for e, v in zip(es, VARS))
                        tan = sum(e * v[2] for e, v in zip(es, VARS))
                        if deg == target_deg and tan == target_tan:
                            out.append(es)
    return out


def monomial_label(es):
    parts = []
    for e, (name, _, _) in zip(es, VARS):
        if e:
            parts.append(name if e == 1 else f"{name}^{e}")
    return "*".join(parts) if parts else "1"


def columns():
    out = []
    for seed, d, t in SEEDS:
        for es in exponent_solutions(4 - d, 2 - t):
            out.append({
                "seed": seed,
                "exponents": es,
                "scalar": monomial_label(es),
                "explicit_K_factor": es[1] > 0,
            })
    assert len(out) == 36
    return out

COLS = columns()


def dot(x, y):
    return sum((F(a) * F(b) for a, b in zip(x, y)), F(0))


def scalar_value(es, q, k, n):
    vals = (dot(q, q), dot(k, k), dot(q, k), dot(n, q), dot(n, k))
    z = F(1)
    for e, v in zip(es, vals):
        z *= v ** e
    return z


def seed_value(seed, q, k, n, a, b):
    if seed == "delta_ab":
        return F(a == b)
    if seed == "q_aq_b":
        return F(q[a]) * F(q[b])
    if seed == "q_(a_k_b)":
        return (F(q[a]) * F(k[b]) + F(k[a]) * F(q[b])) / 2
    if seed == "k_ak_b":
        return F(k[a]) * F(k[b])
    if seed == "q_(a_n_b)":
        return (F(q[a]) * F(n[b]) + F(n[a]) * F(q[b])) / 2
    if seed == "k_(a_n_b)":
        return (F(k[a]) * F(n[b]) + F(n[a]) * F(k[b])) / 2
    if seed == "n_an_b":
        return F(n[a]) * F(n[b])
    raise KeyError(seed)


def basis_row(q, k, n, a, b):
    return [seed_value(c["seed"], q, k, n, a, b) * scalar_value(c["exponents"], q, k, n) for c in COLS]


def to_s(x):
    x = F(x)
    return s.Rational(x.numerator, x.denominator)


def deterministic_fixtures(D, seed, count):
    rng = random.Random(seed)
    out = []
    while len(out) < count:
        q = tuple(rng.randint(-3, 3) for _ in range(D))
        k = tuple(rng.randint(-3, 3) for _ in range(D))
        n = tuple(rng.randint(-2, 2) for _ in range(D))
        if not any(q) or not any(k) or not any(n):
            continue
        if q == k or tuple(-x for x in q) == k:
            continue
        out.append((q, k, n))
    return out


def design_4d():
    fixtures = deterministic_fixtures(4, 16220260917, 14)
    rows = []
    keys = []
    for fi, (q, k, n) in enumerate(fixtures):
        for a in range(4):
            for b in range(a, 4):
                rows.append([to_s(x) for x in basis_row(q, k, n, a, b)])
                keys.append((fi, a, b))
    M = s.Matrix(rows)
    piv = M.T.rref()[1]
    if len(piv) != 36:
        raise RuntimeError(f"frozen 36-column span design rank {len(piv)} != 36")
    sel = list(piv[:36])
    A = s.Matrix([rows[i] for i in sel])
    if A.rank() != 36:
        raise RuntimeError("selected exact design is singular")
    return fixtures, keys, sel, A


def pad4(v, D):
    return tuple(v) + (0,) * (D - 4)


def solve_coefficients(D, fixtures, keys, sel, Ainv):
    needed = sorted(set(keys[i][0] for i in sel))
    V = {}
    for fi in needed:
        q4, k4, n4 = fixtures[fi]
        V[fi] = i161.upper_open_vertex(pad4(q4, D), pad4(k4, D), pad4(n4, D), D)
    y = []
    for i in sel:
        fi, a, b = keys[i]
        y.append(to_s(V[fi][a][b]))
    return [s.factor(x) for x in (Ainv * s.Matrix(y))]


def eval_tensor(coeffs, q, k, n, a, b):
    row = basis_row(q, k, n, a, b)
    return s.factor(sum(c * to_s(v) for c, v in zip(coeffs, row)))


def main():
    fixtures, keys, sel, A = design_4d()
    Ainv = A.inv(method="DM")

    train = [4, 5, 6, 7, 8]
    validate = [9, 10]
    all_dims = train + validate
    byD = {D: solve_coefficients(D, fixtures, keys, sel, Ainv) for D in all_dims}

    d = s.symbols("d")
    formulas = []
    max_scaled_degree = 0
    interpolation_ok = True
    for j, c in enumerate(COLS):
        pts = [(D, s.factor((D - 2) * byD[D][j])) for D in train]
        poly = s.factor(s.interpolate(pts, d))
        degree = int(s.Poly(s.expand(poly), d).degree()) if poly != 0 else 0
        max_scaled_degree = max(max_scaled_degree, degree)
        coeff_d = s.factor(poly / (d - 2))
        valid = all(s.simplify(coeff_d.subs(d, D) - byD[D][j]) == 0 for D in validate)
        interpolation_ok &= bool(valid and degree <= 4)
        formulas.append({
            "seed": c["seed"],
            "scalar": c["scalar"],
            "explicit_K_factor": c["explicit_K_factor"],
            "coefficient_d": str(coeff_d),
            "scaled_polynomial_degree": degree,
            "heldout_D9_D10_equal": bool(valid),
        })

    held_rows = []
    heldout_ok = True
    for D in all_dims:
        q, k, n = deterministic_fixtures(D, 16290000000 + D, 1)[0]
        direct = i161.upper_open_vertex(q, k, n, D)
        coeffD = [s.factor(s.sympify(x["coefficient_d"]).subs(d, D)) for x in formulas]
        dim_ok = True
        for a in range(D):
            for b in range(a, D):
                rec = eval_tensor(coeffD, q, k, n, a, b)
                if s.simplify(rec - to_s(direct[a][b])) != 0:
                    dim_ok = False
                    break
            if not dim_ok:
                break
        heldout_ok &= dim_ok
        held_rows.append({"D": D, "all_symmetric_components_exact": bool(dim_ok)})

    nonzero = [x for x in formulas if s.sympify(x["coefficient_d"]) != 0]
    local = [x for x in nonzero if x["explicit_K_factor"]]
    nonlocal_cols = [x for x in nonzero if not x["explicit_K_factor"]]

    checks = {
        "A_frozen_basis_column_count_36": len(COLS) == 36,
        "B_exact_design_rank_36": A.rank() == 36,
        "C_single_pmap_denominator_interpolation_degree_le_4": interpolation_ok and max_scaled_degree <= 4,
        "D_heldout_D9_D10_coefficients_exact": interpolation_ok,
        "E_independent_fullD_tensor_fixtures_exact": heldout_ok,
        "F_ITER160_minus525_not_consumed": True,
        "G_no_inverse_28_scalar_map": True,
        "H_no_ITER118_solve": True,
        "I_no_contacts_set_zero": True,
    }

    out = {
        "gate": "ITER162_OPEN_G_ENDPOINT_DISTRIBUTIONAL_R_OPERATION_AND_POLE_TENSOR",
        "classification": "PARTIAL_ITER162_SOURCE_DERIVED_UPPER_COVARIANT_TENSOR_RECONSTRUCTION_AND_K_SUPPORT_SPLIT",
        "basis_column_count": len(COLS),
        "basis_exact_rank": int(A.rank()),
        "design_selected_row_count": len(sel),
        "D_train": train,
        "D_validate": validate,
        "single_structural_denominator": "d-2",
        "max_scaled_coefficient_polynomial_degree": max_scaled_degree,
        "nonzero_source_coefficients": len(nonzero),
        "nonzero_explicit_K_divisible_coefficients": len(local),
        "nonzero_genuine_kernel_coefficients": len(nonlocal_cols),
        "support_statement": (
            "Because the prospectively frozen 36 covariants have exact full rank, the representation is unique. "
            "The explicit-K subspace therefore gives an exact source-derived contact-candidate split; the remaining "
            "non-K columns are genuine V_upper/K kernel information before external-source contraction."
        ),
        "coefficients": formulas,
        "heldout": held_rows,
        "checks": {k: bool(v) for k, v in checks.items()},
        "terminal_science": False,
        "remaining_blocker": (
            "construct the complete distributional Laurent extension of the unseparated open tensor and the full "
            "allowed local pole-ambiguity span, then compute the exact quotient P_open/A_local"
        ),
        "locks": {
            "ITER160_minus525_consumed": False,
            "inverse_28_scalar_map": False,
            "ITER118_coefficient_solve": False,
            "contacts_set_zero": False,
            "B1_total": "UNAUTHORIZED",
            "BRIDGE_DERIVED": False,
            "candidate_theory": "UNFORMED / 0%",
        },
    }
    Path("iter162_upper_covariant_reconstruction.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({k: v for k, v in out.items() if k != "coefficients"}, indent=2, sort_keys=True))
    raise SystemExit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
