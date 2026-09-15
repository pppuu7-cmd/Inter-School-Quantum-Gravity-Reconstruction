#!/usr/bin/env python3
"""Validate ITER128 singular-degree / Taylor-jet arithmetic."""

from __future__ import annotations

import json
from pathlib import Path

TABLE = Path("analysis/iter128_local_singular_degree_table.json")


def main() -> None:
    data = json.loads(TABLE.read_text(encoding="utf-8"))
    rows = data["canonical_rows"]
    assert rows

    for row in rows:
        n = row["derivatives"]["N"]
        props = row["propagators"]
        base = 2 if props == 1 else 4
        assert row["m_raw"] == base + n, row["id"]
        assert row["m_eff"] == row["m_raw"] - row["source_suppression_s"], row["id"]
        assert row["jet_order"] == row["m_eff"] - 1, row["id"]
        assert row["jet_order"] >= 0, row["id"]

    by_id = {r["id"]: r for r in rows}
    assert by_id["R1_to_Gamma1_lower_endpoint"]["jet_order"] == 4
    assert by_id["R1_to_Gamma1_upper_endpoint"]["jet_order"] == 3
    assert by_id["Gamma1_to_Gamma1_diagonal_unsuppressed"]["jet_order"] == 3
    assert by_id["dGamma1_to_Gamma1_diagonal_green_suppressed"]["jet_order"] == 3
    assert by_id["R1_to_BoxPerpR_genuine_defect_endpoint"]["jet_order"] == 7

    ceiling = data["global_residual_defect_ceiling"]
    assert ceiling["max_single_propagator_N"] == 6
    assert ceiling["max_single_propagator_m"] == 8
    assert ceiling["max_one_variable_jet_order"] == 7

    out = Path("artifacts/iter128")
    out.mkdir(parents=True, exist_ok=True)
    summary = {
        "status": "PASS_TABLE_ARITHMETIC",
        "canonical_rows": len(rows),
        "max_canonical_jet": max(r["jet_order"] for r in rows),
        "global_residual_one_variable_jet_ceiling": ceiling["max_one_variable_jet_order"],
        "two_propagator_formula": data["two_propagator_rule"]["formula"],
        "claim_lock": data["claim_lock"],
    }
    (out / "validation.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
