#!/usr/bin/env python3
"""Verify the preregistered auxiliary ITER140 M_R1 D=7 blind prediction.

Usage:
    python analysis/check_iter140_mr1_d7_blind_prediction.py PATH_TO_ITER140_V6_D7_M_R1_JSON

This checker is auxiliary. It does not terminalize ITER140 or alter any frozen gate.
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("usage: check_iter140_mr1_d7_blind_prediction.py D7_SHARD.json")

pred_path = Path(__file__).with_name("iter140_mr1_d7_blind_prediction.json")
pred = json.loads(pred_path.read_text(encoding="utf-8"))
obs = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))


def Q(x: str) -> Fraction:
    return Fraction(str(x))

checks = {}
checks["A_exact_target_identity"] = (
    int(obs.get("D", -1)) == 7 and obs.get("family") == "M_R1_chi1_dR2"
)
checks["B_frozen_shard_integrity"] = (
    int(obs.get("basis_size", -1)) == 28
    and int(obs.get("design_rank", -1)) == 28
    and obs.get("scientific_predicates_changed") is False
    and bool(obs.get("heldouts_ok"))
)
expected_coeff = [Q(x) for x in pred["prediction"]["coefficients"]]
observed_coeff = [Q(x) for x in obs.get("coefficients", [])]
checks["C_all_28_coefficients_exact"] = (
    len(observed_coeff) == 28 and observed_coeff == expected_coeff
)
expected_held = {
    int(x["panel"]): Q(x["predicted_direct"])
    for x in pred["prediction"]["heldouts"]
}
observed_held = {
    int(x["panel"]): Q(x["direct"])
    for x in obs.get("heldouts", [])
}
checks["D_all_3_heldout_direct_values_exact"] = observed_held == expected_held
checks["E_all_observed_heldout_reconstructions_equal"] = all(
    bool(x.get("equal")) for x in obs.get("heldouts", [])
) and len(obs.get("heldouts", [])) == 3

ok = all(checks.values())
classification = (
    "PASS_AUX_ITER140_MR1_BLIND_D7_PREDICTION_CONFIRMED"
    if ok
    else "FAIL_AUX_ITER140_MR1_BLIND_D7_PREDICTION_MISMATCH"
)
out = {
    "classification": classification,
    "prediction_status": pred["status"],
    "checks": checks,
    "predicted_coefficients": pred["prediction"]["coefficients"],
    "observed_coefficients": obs.get("coefficients"),
    "predicted_heldout_direct": {str(k): str(v) for k, v in expected_held.items()},
    "observed_heldout_direct": {str(k): str(v) for k, v in observed_held.items()},
    "claim_ceiling": "Auxiliary D7 blind-prediction check only; frozen ITER140 aggregate remains authoritative.",
}
print(json.dumps(out, indent=2))
if not ok:
    raise SystemExit(1)
