#!/usr/bin/env python3
"""ITER162 source-derived upper open-tensor covariant reconstruction.

Consumes only the frozen ITER161 source-faithful upper_open_vertex and the
ITER162 36-column covariant span. It does not use the ITER160 -525 residue,
does not invert the scalar 28-invariant map, and does not solve ITER118.

ITER143 freezes n^2=1. The Researcher solve uses n=e0, which is a legitimate
unit-tangent frame by covariance and keeps the microscopic exact Fraction engine
fast. Exact rank 36 is required on this domain. Independent q/k fixtures outside
the solve verify every symmetric component in every D=4..10. A separate Critic
uses a different axis for its coefficient solve and rotated rational unit tangents
for covariance held-outs.

The exact D dependence is reconstructed from D=4..8 after multiplying by the
single (D-2) denominator structurally present through one pmap on the k-side R
source. D=9,10 are held out from the D interpolation.
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


def axis_tangent(D: int, axis: int = 0):
    n = [F(0) for _ in range(D)]
    n[axis % D] = F(1)
    assert dot(n, n) == 1
    return tuple(n)


def scalar_value(es, q, k, n):
    assert dot(n, n) == 1
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


def deterministic_fixtures(D, seed, count, axis=0):
    rng = random.Random(seed)
    out = []
    n = axis_tangent(D, axis)
    while len(out) < count:
        q = tuple(F(rng.randint(-3, 3)) for _ in range(D))
        k = tuple(F(rng.randint(-3, 3)) for _ in range(D))
        if not any(q) or not any(k):
            continue
        if q == k or tuple(-x for x in q) == k:
            continue
        out.append((q, k, n))
    return out


def design_4d():
    fixtures = deterministic_fixtures(4, 16220260917, 8, axis=0)
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
        raise RuntimeError(f"frozen 36-column span design rank {len(piv)} != 36 on n=e0, n^2=1 domain")
    sel = list(piv[:36])
    A = s.Matrix([rows[i] for i in sel])
    if A.rank() != 36:
        raise RuntimeError("selected exact design is singular")
    return fixtures, keys, sel, A


def pad4(v, D):
    return tuple(v) + (F(0),) * (D - 4)


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


def verify_changed_fixtures(D, coeffs, seed, count=2):
    tests = deterministic_fixtures(D, seed, count, axis=0)
    rows = []
    all_ok = True
    for case, (q, k, n) in enumerate(tests):
        direct = i161.upper_open_vertex(q, k, n, D)
        ok = True
        for a in range(D):
            for b in range(a, D):
                rec = eval_tensor(coeffs, q, k, n, a, b)
                if s.simplify(rec - to_s(direct[a][b])) != 0:
                    ok = False
                    break
            if not ok:
                break
        all_ok &= ok
        rows.append({"D": D, "case": case, "n_squared": str(dot(n, n)), "all_symmetric_components_exact": bool(ok)})
    return bool(all_ok), rows


def main():
    fixtures, keys, sel, A = design_4d()
    Ainv = A.inv(method="DM")

    train = [4, 5, 6, 7, 8]
    validate = [9, 10]
    all_dims = train + validate
    byD = {D: solve_coefficients(D, fixtures, keys, sel, Ainv) for D in all_dims}

    # Overdetermined exact verification outside the coefficient solve.
    over_rows = []
    over_ok = True
    for D in all_dims:
        ok, rows = verify_changed_fixtures(D, byD[D], 16281000000 + D, count=2)
        over_ok &= ok
        over_rows.extend(rows)

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

    nonzero = [x for x in formulas if s.sympify(x["coefficient_d"]) != 0]
    explicit_k = [x for x in nonzero if x["explicit_K_factor"]]
    no_explicit_k = [x for x in nonzero if not x["explicit_K_factor"]]

    checks = {
        "A_frozen_basis_column_count_36": len(COLS) == 36,
        "B_exact_design_rank_36_on_axis_unit_tangent_domain": A.rank() == 36,
        "C_overdetermined_changed_qk_fixtures_exact_D4_to_D10": over_ok,
        "D_single_pmap_denominator_interpolation_degree_le_4": interpolation_ok and max_scaled_degree <= 4,
        "E_heldout_D9_D10_coefficients_exact": interpolation_ok,
        "F_all_solve_fixtures_obey_ITER143_n2_eq_1": all(dot(n, n) == 1 for _, _, n in fixtures),
        "G_ITER160_minus525_not_consumed": True,
        "H_no_inverse_28_scalar_map": True,
        "I_no_ITER118_solve": True,
        "J_no_contacts_set_zero": True,
    }

    out = {
        "gate": "ITER162_OPEN_G_ENDPOINT_DISTRIBUTIONAL_R_OPERATION_AND_POLE_TENSOR",
        "classification": "PARTIAL_ITER162_SOURCE_DERIVED_UPPER_COVARIANT_TENSOR_RECONSTRUCTION",
        "implementation_history": {
            "first_run": "FAILED_INVALID_HELDOUT_DOMAIN_NONUNIT_N",
            "repair_1": "ENFORCE_FROZEN_ITER143_N2_EQ_1",
            "repair_2": "EXECUTION_ONLY_AXIS_UNIT_TANGENT_RESEARCHER_FRAME_WITH_INDEPENDENT_ROTATED_CRITIC",
        },
        "basis_column_count": len(COLS),
        "basis_exact_rank": int(A.rank()),
        "design_selected_row_count": len(sel),
        "design_available_row_count": len(fixtures) * 10,
        "D_train": train,
        "D_validate": validate,
        "single_structural_denominator": "d-2",
        "max_scaled_coefficient_polynomial_degree": max_scaled_degree,
        "nonzero_source_coefficients": len(nonzero),
        "nonzero_explicit_K_factor_coefficients": len(explicit_k),
        "nonzero_without_explicit_K_factor": len(no_explicit_k),
        "support_statement": (
            "This producer reconstructs V_upper only. Complete frozen-span K-divisibility is certified by a separate exact quotient job; "
            "distributional Laurent extension remains downstream."
        ),
        "coefficients": formulas,
        "overdetermined_heldout": over_rows,
        "checks": {k: bool(v) for k, v in checks.items()},
        "terminal_science": False,
        "remaining_blocker": (
            "consume the independent K-divisibility certificate, then construct the complete distributional Laurent extension, "
            "full allowed local pole-ambiguity span, and exact quotient P_open/A_local"
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
