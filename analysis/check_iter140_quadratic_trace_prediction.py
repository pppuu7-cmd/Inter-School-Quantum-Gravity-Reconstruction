#!/usr/bin/env python3
"""Check one preregistered auxiliary ITER140 quadratic-trace prediction.

Usage:
    python analysis/check_iter140_quadratic_trace_prediction.py PATH_TO_V6_SHARD.json

The shard must be one of the ten targets preregistered in
`iter140_quadratic_trace_conjecture_all_remaining.json`.
This checker is auxiliary; the frozen ITER140 aggregate remains authoritative.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
import sympy as s

if len(sys.argv) != 2:
    raise SystemExit("usage: check_iter140_quadratic_trace_prediction.py SHARD.json")

spec = json.loads(
    Path(__file__).with_name("iter140_quadratic_trace_conjecture_all_remaining.json").read_text(encoding="utf-8")
)
obs = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
D = int(obs.get("D", -1))
family = obs.get("family")

if family not in spec["families"]:
    raise SystemExit(f"family not preregistered: {family}")
fam = spec["families"][family]
if str(D) not in fam["targets"]:
    raise SystemExit(f"D={D}, family={family} is not a preregistered remaining target")

d = s.symbols("d")
expected_coeff = []
for expr in fam["trace_polynomials_by_index"]:
    p = s.sympify(expr)
    expected_coeff.append(s.factor(p.subs(d, D) / (D - 2) ** 2))
observed_coeff = [s.sympify(x) for x in obs.get("coefficients", [])]
expected_held = [s.sympify(x) for x in fam["targets"][str(D)]["heldout_predicted_direct"]]
observed_held = [s.sympify(x["direct"]) for x in obs.get("heldouts", [])]

checks = {
    "A_target_identity": D in range(3, 11) and family in spec["families"],
    "B_frozen_shard_integrity": (
        int(obs.get("basis_size", -1)) == 28
        and int(obs.get("design_rank", -1)) == 28
        and obs.get("scientific_predicates_changed") is False
        and bool(obs.get("heldouts_ok"))
    ),
    "C_all_28_coefficients_exact": (
        len(observed_coeff) == 28
        and all(s.cancel(a - b) == 0 for a, b in zip(observed_coeff, expected_coeff))
    ),
    "D_all_3_direct_heldouts_exact": (
        len(observed_held) == 3
        and all(s.cancel(a - b) == 0 for a, b in zip(observed_held, expected_held))
    ),
    "E_all_observed_heldout_reconstructions_equal": (
        len(obs.get("heldouts", [])) == 3
        and all(bool(x.get("equal")) for x in obs.get("heldouts", []))
    ),
}
ok = all(checks.values())
classification = (
    "PASS_AUX_ITER140_QUADRATIC_TRACE_BLIND_PREDICTION_CONFIRMED"
    if ok
    else "FAIL_AUX_ITER140_QUADRATIC_TRACE_BLIND_PREDICTION_MISMATCH"
)
print(json.dumps({
    "classification": classification,
    "D": D,
    "family": family,
    "checks": checks,
    "expected_coefficients": [str(x) for x in expected_coeff],
    "observed_coefficients": [str(x) for x in observed_coeff],
    "expected_heldout_direct": [str(x) for x in expected_held],
    "observed_heldout_direct": [str(x) for x in observed_held],
    "claim_ceiling": "Auxiliary prospective test only; frozen ITER140 aggregate remains authoritative."
}, indent=2))
if not ok:
    raise SystemExit(1)
