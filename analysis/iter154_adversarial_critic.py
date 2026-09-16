#!/usr/bin/env python3
"""Independent adversarial critic for ITER154."""
from __future__ import annotations

import json
from pathlib import Path

RESULT = Path("iter154_first_mg_graph_subdivergence_r_operation.json")

EXPECTED = {
    "M_R2_chi1_dR1": {"degrees":[2,1,1], "strata":["lower"]},
    "M_R1_chi1_dR2": {"degrees":[1,1,2], "strata":["upper"]},
    "G_R1_chi2_Gamma2_dR1": {"degrees":[1,2,1], "strata":["lower","upper"]},
}


def main() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    rows = data.get("graph_records", [])
    checks_rows = []
    for row in rows:
        fam = row["family"]
        sites = row["sites"]
        edges = [e["sites"] for e in row["wick_edges"]]
        degree = {v:0 for v in sites}
        for a,b in edges:
            degree[a] += 1
            degree[b] += 1
        degree_vector = [degree[v] for v in sites]
        # Independent tree criterion: connected graph with E=V-1 and no self-loop.
        connected_tree = row["connected_components"] == 1 and len(edges) == len(sites)-1 and all(a != b for a,b in edges)
        proper = row["strict_proper_connected_edge_subgraphs"]
        proper_single_edges = len(proper) == 2 and all(p["edge_count"] == 1 and p["b1"] == 0 and not p["has_self_loop"] for p in proper)
        # No interior collision: only tau or 1-tau vanish, and only at the frozen boundary.
        allowed_sep = all(e["separation"] in {"tau","1-tau","1"} for e in row["wick_edges"])
        checks_rows.append(
            fam in EXPECTED
            and connected_tree
            and degree_vector == EXPECTED[fam]["degrees"]
            and row["first_betti_number"] == 0
            and proper_single_edges
            and allowed_sep
            and row["frozen_endpoint_singular_strata"] == EXPECTED[fam]["strata"]
            and row["slot6_subtraction_operator"] == "IDENTITY_R_sub_G_equals_G"
            and row["slot6_proper_subdivergence_counterterm_insertions"] == []
            and row["endpoint_defect_renormalization_still_required"] is True
        )

    controls = data.get("controls", [])
    required_reasons = {
        "triangle_cycle":"SYNTHETIC_CYCLE_NOT_IN_FROZEN_GRAPH",
        "S3_import":"IMPORTED_BULK_ACTION_INTERACTION",
        "self_pairing":"IMPORTED_LOCAL_SELF_PAIRING_OUTSIDE_ITER141_SCOPE",
        "endpoint_as_bulk":"ENDPOINT_COLLAPSE_MISCLASSIFIED_AS_SLOT6_BULK_SUBDIVERGENCE",
        "drop_edge":"FROZEN_WICK_EDGE_DROPPED",
        "changed_family":"CHANGED_FROZEN_FAMILY_SET",
        "import_F_sector":"BROADER_F_SECTOR_CENSUS_IMPORTED_INTO_FIRST_MG_CROSS_SCOPE",
        "contact_zero":"SLOT6_DERIVED_ZERO_ILLEGALLY_PROMOTED_TO_CONTACT_POLE_ZERO",
        "B1_total":"UNAUTHORIZED_B1_TOTAL_FORMATION",
    }
    controls_ok = len(controls) == len(required_reasons) and all(
        c["name"] in required_reasons
        and c["accepted"] is False
        and required_reasons[c["name"]] in c["rejection_reasons"]
        for c in controls
    )

    checks = {
        "A_exact_three_family_scope": [r["family"] for r in rows] == list(EXPECTED.keys()),
        "B_independent_tree_degree_and_subgraph_census": len(checks_rows) == 3 and all(checks_rows),
        "C_no_action_ghost_or_same_site_vertices": all(not r["action_interaction_vertices"] and not r["ghost_vertices"] and not r["same_site_self_pairing"] for r in rows),
        "D_endpoint_strata_not_erased": all(r["endpoint_defect_renormalization_still_required"] for r in rows),
        "E_derived_zero_scope_only_slot6": data.get("derived_zero_scope") == "proper ordinary bulk/local-composite subdivergence insertions only; not endpoint/contact/line/full-graph poles",
        "F_all_negative_controls_rejected_for_specific_reason": controls_ok,
        "G_slot6_scoped_closed_not_B1": data.get("slot6_closed_for_scoped_cross_families") is True and "B1_total" in data.get("claim_ceiling", ""),
    }
    classification = "PASS_CRITIC_ITER154_SCOPED_SUBDIVERGENCE_ZERO_SOUND" if all(checks.values()) else "FAIL_CRITIC_ITER154_REQUIRES_REPAIR"
    out = {
        "critic":"ITER154_ADVERSARIAL_GRAPH_SUBDIVERGENCE_CRITIC",
        "classification":classification,
        "checks":checks,
        "conclusion": "The derived zero is topological and narrowly scoped: the three frozen connected-cross graphs are two-edge trees, so their proper ordinary bulk/local-composite subdivergence forest is empty. Endpoint/defect UV singularities remain and are not set to zero." if all(checks.values()) else "Do not promote ITER154 until critic failures are repaired.",
    }
    Path("iter154_adversarial_critic.json").write_text(json.dumps(out, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    if not all(checks.values()):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
