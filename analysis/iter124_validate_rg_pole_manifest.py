#!/usr/bin/env python3
"""Validate the frozen ITER124 projected RG/pole calculation contract."""

from __future__ import annotations

import json
from pathlib import Path


MANIFEST = Path("analysis/iter124_projected_rg_pole_manifest.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))

    require(data["regularization"]["dimension"] == "d=4-2 epsilon", "wrong dimension")
    require(data["projector"]["u_points"] == ["0", "1/2"], "projector points changed")
    require(data["projector"]["general_d_determinant"] == "1/4", "projector determinant changed")
    require(data["projector"]["take_d_to_4_after_pole_projection"], "premature d=4 specialization")

    sectors = data["sectors"]
    for key in ["F", "M", "G", "endpoint", "line"]:
        require(key in sectors, f"missing sector {key}")

    genuine = sectors["line"]["genuine_representatives"]
    require(genuine == ["int Box_perp R", "int Box_perp R_nn"], "genuine defect basis changed")

    retained = sectors["line"]["retain_during_renormalization"]
    for op in ["int R", "int R_nn", "int Box_perp R", "int Box_perp R_nn"]:
        require(op in retained, f"missing retained line operator {op}")

    order = data["subtraction_order"]
    require(len(order) == 6, "subtraction sequence changed")
    require("subdivergences" in order[1], "bulk subdivergences not second")
    require("line-defect mixing matrix" in order[3], "line mixing not renormalized before projection")
    require("contact/polynomial" in order[4], "contact split occurs at wrong stage")
    require("project genuine-defect poles" in order[5], "projector not last in subtraction chain")

    outputs = set(data["required_outputs"])
    for required in ["B1_direct", "beta_defect", "B1_defect", "B1_total"]:
        require(required in outputs, f"missing RG output {required}")

    checks = set(data["consistency_checks"])
    for required in [
        "gauge_or_BRST_consistency",
        "field_redefinition_invariance",
        "trace_traceless_decomposition",
        "two_point_projector_validation_subset",
        "higher_pole_renormalization_consistency",
        "EDT_target_independence",
    ]:
        require(required in checks, f"missing consistency check {required}")

    stops = data["stopping_rules"]
    require("B1_total_nonzero" in stops, "missing nonzero stopping rule")
    require("B1_total_zero" in stops, "missing zero stopping rule")
    require("gauge_or_field_redefinition_failure" in stops, "missing failure stopping rule")

    out = Path("artifacts/iter124")
    out.mkdir(parents=True, exist_ok=True)
    summary = {
        "status": "PASS_MANIFEST_VALIDATION",
        "sector_count": 5,
        "genuine_defect_rank": 2,
        "projector_points": data["projector"]["u_points"],
        "required_rg_outputs": sorted(outputs),
        "consistency_check_count": len(checks),
        "claim_lock": data["claim_lock"],
    }
    (out / "manifest_validation.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
