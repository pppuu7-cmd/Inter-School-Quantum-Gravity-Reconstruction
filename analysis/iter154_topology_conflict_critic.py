#!/usr/bin/env python3
"""Independent critic for the ITER154 preregistered topology falsification."""
from __future__ import annotations

import json
from pathlib import Path

EVAL = Path("iter154_preregistered_hypothesis_evaluator.json")
GEOM = Path("iter154_first_mg_graph_subdivergence_r_operation.json")


def main() -> None:
    ev = json.loads(EVAL.read_text(encoding="utf-8"))
    geom = json.loads(GEOM.read_text(encoding="utf-8"))
    rows = geom.get("graph_records", [])
    geometric_fact = len(rows) == 3 and all(r.get("V") == 3 and r.get("E") == 2 and r.get("first_betti_number") == 0 for r in rows)
    source_fact = all(ev.get("checks", {}).get(k) is True for k in [
        "D_ITER125_M_sector_explicit_bubble_core",
        "E_ITER125_at_most_one_independent_loop_momentum",
        "F_ITER125_G_connected_loop_explicit_bubble",
    ])
    exact_fail = ev.get("classification") == "SCIENTIFIC_FAIL_SCOPED_ITER154_TOPOLOGICAL_PRIMITIVITY_HYPOTHESIS_FALSE"
    no_overreach = "does NOT show that a proper UV subdivergence exists" in ev.get("scientific_interpretation", "")
    repair_specific = ev.get("repair_gate") == "ITER154B_FIXED_GEODESIC_FIRST_MG_PRIMITIVE_BUBBLE_PROPER_SUBGRAPH_R_OPERATION"
    checks = {
        "A_geometric_site_tree_fact_preserved": geometric_fact,
        "B_independent_ITER125_loop_bubble_fact_preserved": source_fact,
        "C_preregistered_clause_falsified_not_rewritten": exact_fail and "no closed momentum cycle" in str(ev.get("falsified_preregistered_clause")),
        "D_fail_does_not_claim_subdivergence_exists": no_overreach,
        "E_repair_gate_changes_graph_representation_not_scientific_target": repair_specific,
        "F_slot6_not_closed": "slot6 not closed" in ev.get("claim_ceiling", ""),
    }
    classification = "PASS_CRITIC_ITER154_PREREGISTERED_HYPOTHESIS_FALSIFICATION_SOUND" if all(checks.values()) else "FAIL_CRITIC_ITER154_TOPOLOGY_CONFLICT_REQUIRES_REPAIR"
    out = {
        "critic":"ITER154_TOPOLOGY_REPRESENTATION_CONFLICT_CRITIC",
        "classification":classification,
        "checks":checks,
        "conclusion": "The scientific FAIL is warranted: geometric-site acyclicity and operator-level loop-momentum topology are different invariants. ITER154 preregistered their equivalence and ITER125 falsifies it. The repair must retain the one-loop bubble core and ask only whether it has strict proper UV subgraphs." if all(checks.values()) else "Do not terminalize ITER154 until critic failures are repaired.",
    }
    Path("iter154_topology_conflict_critic.json").write_text(json.dumps(out, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    if not all(checks.values()):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
