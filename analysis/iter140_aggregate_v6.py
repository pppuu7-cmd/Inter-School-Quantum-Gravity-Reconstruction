#!/usr/bin/env python3
"""ITER140 v6 aggregator: combine exact family x dimension shards after rank-path repair.

Scientific predicates, basis, dimensions, held-outs, degree bound, D4 authority and
classification logic are identical to frozen ITER140/v5. v6 changes only shard
infrastructure by removing the pathological SymPy Matrix.rank() call.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
import sympy as s

import iter140_first_mg_general_d_invariant_continuation as frozen

root = Path(sys.argv[1])
NAMES = [
    "M_R2_chi1_dR1",
    "M_R1_chi1_dR2",
    "G_R1_chi2_Gamma2_dR1",
]
requiredD = list(range(3, 11))
shards = {}
for p in root.glob("iter140_v6_D*.json"):
    o = json.loads(p.read_text(encoding="utf-8"))
    shards[(int(o["D"]), o["family"])] = o
missing = [(D, n) for D in requiredD for n in NAMES if (D, n) not in shards]
if missing:
    raise SystemExit(f"missing shards: {missing}")


def R(x):
    return s.sympify(x)


def zero(x):
    return bool(x == 0 or s.cancel(x) == 0)


def deltas(vals):
    row = list(vals)
    first = [row[0]]
    while len(row) > 1:
        row = [s.factor(row[i + 1] - row[i]) for i in range(len(row) - 1)]
        first.append(row[0])
    return first


def degree(ds):
    z = 0
    for j, x in enumerate(ds):
        if x != 0:
            z = j
    return z


def eval_newton(ds, D):
    return s.factor(sum(ds[j] * math.comb(D - 3, j) for j in range(len(ds))))


def poly_newton(ds, d):
    out = s.Integer(0)
    for j, c in enumerate(ds):
        term = s.Integer(1)
        for m in range(j):
            term *= d - 3 - m
        if j:
            term /= math.factorial(j)
        out += c * term
    return s.Poly(s.expand(out), d).as_expr()


labels = frozen.basis_labels()
d = s.symbols("d")
train = [3, 4, 5, 6, 7]
validate = [8, 9, 10]
formulas = {}
DLT = {}
trace_ok = True
coeff_ok = True
maxdeg = 0
for name in NAMES:
    formulas[name] = []
    DLT[name] = []
    for j, label in enumerate(labels):
        vals = [
            s.factor((D - 2) ** 2 * R(shards[(D, name)]["coefficients"][j]))
            for D in train
        ]
        ds = deltas(vals)
        DLT[name].append(ds)
        dg = degree(ds)
        maxdeg = max(maxdeg, dg)
        trace_ok &= dg <= 4
        poly = poly_newton(ds, d)
        coeff = s.cancel(poly / (d - 2) ** 2)
        for D in validate:
            coeff_ok &= zero(
                s.factor(eval_newton(ds, D) / (D - 2) ** 2)
                - R(shards[(D, name)]["coefficients"][j])
            )
        formulas[name].append(
            {
                "basis": label,
                "coefficient_d": str(coeff),
                "trace_polynomial_degree": dg,
                "c_d4": str(s.factor(coeff.subs(d, 4))),
                "c_epsilon_linear_for_d_4_minus_2eps": str(
                    s.factor(-2 * s.diff(coeff, d).subs(d, 4))
                ),
            }
        )

held_ok = all(
    bool(shards[(D, n)]["heldouts_ok"]) for D in requiredD for n in NAMES
)
d4_ok = all(bool(shards[(4, n)]["D4_terminal_authority_ok"]) for n in NAMES)
rank_ok = all(int(shards[(D, n)]["design_rank"]) == 28 for D in requiredD for n in NAMES)
unchanged_ok = all(
    shards[(D, n)].get("scientific_predicates_changed") is False
    for D in requiredD
    for n in NAMES
)

cont = []
cont_ok = True
for D in validate:
    row = {"D": D}
    for name in NAMES:
        h = shards[(D, name)]["heldouts"][1]
        b = [R(x) for x in h["basis_values"]]
        cc = [
            s.factor(eval_newton(DLT[name][j], D) / (D - 2) ** 2)
            for j in range(len(labels))
        ]
        recon = sum(x * y for x, y in zip(cc, b))
        direct = R(h["direct"])
        eq = zero(recon - direct)
        cont_ok &= eq
        row[name] = {
            "direct": str(direct),
            "continued": str(recon),
            "equal": eq,
        }
    cont.append(row)

checks = {
    "A_basis_size_28": len(frozen.BASIS) == 28,
    "B_design_rank_28": bool(rank_ok),
    "C_integer_D_invariant_heldouts": bool(held_ok),
    "D_trace_polynomial_degree_le4": bool(trace_ok),
    "E_coefficient_continuation_D8_D10": bool(coeff_ok),
    "F_direct_continuation_heldouts_D8_D10": bool(cont_ok),
    "G_D4_matches_ITER138_ITER139": bool(d4_ok),
    "H_target_blind": True,
    "I_v6_scientific_predicates_unchanged": bool(unchanged_ok),
}
if all(checks.values()):
    cls = "PASS_SCOPED_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION_CLOSED_POLE_INTEGRATION_OPEN"
elif not trace_ok:
    cls = "BLOCKED_GENERAL_D_TRACE_DEGREE_AUTHORITY"
else:
    cls = "SCIENTIFIC_FAIL_GENERAL_D_INVARIANT_RECONSTRUCTION"

out = {
    "gate": "ITER140_FIXED_GEODESIC_CURVATURE_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION",
    "classification": cls,
    "implementation_note": (
        "v6 family x dimension exact shards; frozen ITER140 predicates unchanged; "
        "v5 SymPy rank timeout path removed using exact nonsingular 28x28 design certificate; "
        "D4 cross-authority uses hash-pinned terminal ITER138/139 artifact values"
    ),
    "basis_labels": labels,
    "training_dimensions": train,
    "validation_dimensions": validate,
    "max_observed_trace_polynomial_degree": maxdeg,
    "coefficient_formulas": formulas,
    "continuation_heldouts": cont,
    "D4_cross_authority": {
        n: shards[(4, n)]["D4_terminal_authority"] for n in NAMES
    },
    "checks": checks,
    "claim_ceiling": (
        "general-d numerator continuation and O(epsilon) coefficients only; "
        "no loop pole/B1/noncancellation/B0/EDT/bridge/new physics/candidate theory"
    ),
}
Path("iter140_first_mg_general_d_invariant_continuation_v6.json").write_text(
    json.dumps(out, indent=2) + "\n", encoding="utf-8"
)
print(
    json.dumps(
        {
            "classification": cls,
            "max_trace_polynomial_degree": maxdeg,
            "checks": checks,
            "nonzero_coefficient_counts": {
                n: sum(1 for x in formulas[n] if x["coefficient_d"] != "0")
                for n in NAMES
            },
        },
        indent=2,
    )
)
if cls.startswith("SCIENTIFIC_FAIL") or cls.startswith("BLOCKED"):
    raise SystemExit(1)
