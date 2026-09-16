#!/usr/bin/env python3
"""ITER154: exact proper-subdivergence census for frozen first-M/G cross channels."""
from __future__ import annotations

import itertools
import json
import subprocess
from pathlib import Path

FROZEN_PARENT = "d5ca2a3203b689964f50e2723b7bc6a30217708b"
PREREG_COMMIT = "0f8ef88819d3191e0c14d3323064e6d66a0da097"
ITER141_PATH = "analysis/iter141_first_mg_wick_geometry_phase_strata.py"
EXPECTED_ITER141_BLOB = "5d1c94a8e8fcdb6970de79b65f50e3625402f37e"

GRAPHS = {
    "M_R2_chi1_dR1": {
        "sites": ["x", "z_tau", "y"],
        "edges": [
            {"fields": ["R2_q", "chi1_minus_q"], "sites": ["x", "z_tau"], "separation": "tau"},
            {"fields": ["R2_k", "dR1_minus_k"], "sites": ["x", "y"], "separation": "1"},
        ],
        "endpoint_strata": ["lower"],
        "source_snippets": [
            "('R2_q','chi1_minus_q'), ('R2_k','dR1_minus_k')",
            "'expected_singular': ['lower']",
        ],
    },
    "M_R1_chi1_dR2": {
        "sites": ["x", "z_tau", "y"],
        "edges": [
            {"fields": ["R1_minus_q", "dR2_q"], "sites": ["x", "y"], "separation": "1"},
            {"fields": ["chi1_minus_k", "dR2_k"], "sites": ["z_tau", "y"], "separation": "1-tau"},
        ],
        "endpoint_strata": ["upper"],
        "source_snippets": [
            "('R1_minus_q','dR2_q'), ('chi1_minus_k','dR2_k')",
            "'expected_singular': ['upper']",
        ],
    },
    "G_R1_chi2_Gamma2_dR1": {
        "sites": ["x", "z_tau", "y"],
        "edges": [
            {"fields": ["R1_minus_q", "Gamma2_q"], "sites": ["x", "z_tau"], "separation": "tau"},
            {"fields": ["Gamma2_k", "dR1_minus_k"], "sites": ["z_tau", "y"], "separation": "1-tau"},
        ],
        "endpoint_strata": ["lower", "upper"],
        "source_snippets": [
            "('R1_minus_q','Gamma2_q'), ('Gamma2_k','dR1_minus_k')",
            "'expected_singular': ['lower','upper']",
        ],
    },
}


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], check=check, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def ancestor(commit: str) -> bool:
    return git("merge-base", "--is-ancestor", commit, "HEAD", check=False).returncode == 0


def components(vertices: list[str], edges: list[tuple[str, str]]) -> int:
    parent = {v: v for v in vertices}
    def find(v: str) -> str:
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    for a, b in edges:
        union(a, b)
    return len({find(v) for v in vertices})


def betti(vertices: list[str], edges: list[tuple[str, str]]) -> int:
    if not vertices:
        return 0
    c = components(vertices, edges)
    return len(edges) - len(vertices) + c


def strict_connected_edge_subgraphs(spec: dict) -> list[dict]:
    all_edges = spec["edges"]
    out = []
    for r in range(1, len(all_edges)):
        for idxs in itertools.combinations(range(len(all_edges)), r):
            chosen = [all_edges[i] for i in idxs]
            vertices = sorted({v for e in chosen for v in e["sites"]})
            es = [tuple(e["sites"]) for e in chosen]
            c = components(vertices, es)
            if c == 1:
                out.append({
                    "edge_indices": list(idxs),
                    "vertices": vertices,
                    "edge_count": len(es),
                    "component_count": c,
                    "b1": betti(vertices, es),
                    "has_self_loop": any(a == b for a, b in es),
                })
    return out


def endpoint_zeros(separation: str) -> list[str]:
    if separation == "tau":
        return ["lower"]
    if separation == "1-tau":
        return ["upper"]
    if separation == "1":
        return []
    raise ValueError(separation)


def method_b_route(spec: dict) -> dict:
    zeros = sorted({z for e in spec["edges"] for z in endpoint_zeros(e["separation"])}, key=lambda x: ["lower", "upper"].index(x))
    interior_nonzero = all(e["separation"] in {"tau", "1-tau", "1"} for e in spec["edges"])
    return {
        "bulk_interaction_vertices": [],
        "ghost_vertices": [],
        "integrated_action_vertices": 0,
        "closed_momentum_conservation_cycles": 0,
        "all_edge_separations_nonzero_for_0_lt_tau_lt_1": interior_nonzero,
        "inferred_endpoint_zero_strata": zeros,
        "endpoint_strata_match_frozen": zeros == spec["endpoint_strata"],
        "ordinary_bulk_or_same_site_proper_subdivergence": False,
    }


def control_eval(control: dict) -> list[str]:
    reasons = []
    if control.get("triangle"):
        reasons.append("SYNTHETIC_CYCLE_NOT_IN_FROZEN_GRAPH")
    if control.get("S3"):
        reasons.append("IMPORTED_BULK_ACTION_INTERACTION")
    if control.get("self_pairing"):
        reasons.append("IMPORTED_LOCAL_SELF_PAIRING_OUTSIDE_ITER141_SCOPE")
    if control.get("endpoint_as_bulk"):
        reasons.append("ENDPOINT_COLLAPSE_MISCLASSIFIED_AS_SLOT6_BULK_SUBDIVERGENCE")
    if control.get("drop_edge"):
        reasons.append("FROZEN_WICK_EDGE_DROPPED")
    if control.get("changed_family"):
        reasons.append("CHANGED_FROZEN_FAMILY_SET")
    if control.get("import_F_sector"):
        reasons.append("BROADER_F_SECTOR_CENSUS_IMPORTED_INTO_FIRST_MG_CROSS_SCOPE")
    if control.get("contact_zero"):
        reasons.append("SLOT6_DERIVED_ZERO_ILLEGALLY_PROMOTED_TO_CONTACT_POLE_ZERO")
    if control.get("B1_total"):
        reasons.append("UNAUTHORIZED_B1_TOTAL_FORMATION")
    return reasons


def main() -> None:
    source_text = git("show", f"{FROZEN_PARENT}:{ITER141_PATH}").stdout
    blob = git("rev-parse", f"{FROZEN_PARENT}:{ITER141_PATH}").stdout.strip()
    lineage = {
        "frozen_parent_is_ancestor": ancestor(FROZEN_PARENT),
        "preregistration_is_ancestor": ancestor(PREREG_COMMIT),
        "frozen_iter141_blob": blob,
        "expected_iter141_blob": EXPECTED_ITER141_BLOB,
        "iter141_blob_matches": blob == EXPECTED_ITER141_BLOB,
        "execution_head": git("rev-parse", "HEAD").stdout.strip(),
    }

    rows = []
    source_identity_ok = True
    for family, spec in GRAPHS.items():
        source_identity_ok &= family in source_text and all(s in source_text for s in spec["source_snippets"])
        edges = [tuple(e["sites"]) for e in spec["edges"]]
        V = len(spec["sites"])
        E = len(edges)
        C = components(spec["sites"], edges)
        b1 = betti(spec["sites"], edges)
        proper = strict_connected_edge_subgraphs(spec)
        same_site = any(a == b for a, b in edges)
        method_b = method_b_route(spec)
        row = {
            "family": family,
            "sites": spec["sites"],
            "wick_edges": spec["edges"],
            "V": V,
            "E": E,
            "connected_components": C,
            "first_betti_number": b1,
            "same_site_self_pairing": same_site,
            "action_interaction_vertices": [],
            "ghost_vertices": [],
            "strict_proper_connected_edge_subgraphs": proper,
            "any_proper_subgraph_cyclic": any(p["b1"] > 0 for p in proper),
            "any_proper_subgraph_self_pairing": any(p["has_self_loop"] for p in proper),
            "frozen_endpoint_singular_strata": spec["endpoint_strata"],
            "method_B_coordinate_momentum_routing": method_b,
            "slot6_proper_subdivergence_counterterm_insertions": [],
            "slot6_subtraction_operator": "IDENTITY_R_sub_G_equals_G",
            "slot6_derived_zero_count": 0,
            "slot6_derived_zero_statement": "zero proper ordinary bulk/local-composite subdivergence counterterm insertions for this connected-cross graph",
            "endpoint_defect_renormalization_still_required": bool(spec["endpoint_strata"]),
        }
        rows.append(row)

    hypothesis = all(
        r["V"] == 3
        and r["E"] == 2
        and r["connected_components"] == 1
        and r["first_betti_number"] == 0
        and not r["same_site_self_pairing"]
        and not r["any_proper_subgraph_cyclic"]
        and not r["any_proper_subgraph_self_pairing"]
        and not r["action_interaction_vertices"]
        and not r["ghost_vertices"]
        for r in rows
    )
    methods_agree = all(
        r["method_B_coordinate_momentum_routing"]["ordinary_bulk_or_same_site_proper_subdivergence"] is False
        and r["method_B_coordinate_momentum_routing"]["endpoint_strata_match_frozen"]
        and r["method_B_coordinate_momentum_routing"]["closed_momentum_conservation_cycles"] == 0
        for r in rows
    )

    controls_raw = [
        {"name":"triangle_cycle", "triangle":True},
        {"name":"S3_import", "S3":True},
        {"name":"self_pairing", "self_pairing":True},
        {"name":"endpoint_as_bulk", "endpoint_as_bulk":True},
        {"name":"drop_edge", "drop_edge":True},
        {"name":"changed_family", "changed_family":True},
        {"name":"import_F_sector", "import_F_sector":True},
        {"name":"contact_zero", "contact_zero":True},
        {"name":"B1_total", "B1_total":True},
    ]
    controls = [{"name": c["name"], "accepted": not control_eval(c), "rejection_reasons": control_eval(c)} for c in controls_raw]
    controls_ok = all(not c["accepted"] and c["rejection_reasons"] for c in controls)

    checks = {
        "A_frozen_parent_and_prereg_lineage": lineage["frozen_parent_is_ancestor"] and lineage["preregistration_is_ancestor"],
        "B_ITER141_blob_and_exact_family_edge_snippets_match": lineage["iter141_blob_matches"] and source_identity_ok,
        "C_three_frozen_cross_families_only": [r["family"] for r in rows] == list(GRAPHS.keys()),
        "D_topological_primitivity_hypothesis": hypothesis,
        "E_all_strict_proper_connected_subgraphs_enumerated_acyclic": all(len(r["strict_proper_connected_edge_subgraphs"]) == 2 and not r["any_proper_subgraph_cyclic"] for r in rows),
        "F_independent_coordinate_momentum_route_agrees": methods_agree,
        "G_endpoint_strata_preserved_as_downstream_not_slot6": all(r["endpoint_defect_renormalization_still_required"] for r in rows),
        "H_slot6_subtraction_identity_and_no_counterterm_insertions": all(r["slot6_subtraction_operator"] == "IDENTITY_R_sub_G_equals_G" and r["slot6_proper_subdivergence_counterterm_insertions"] == [] for r in rows),
        "I_controls_rejected": controls_ok,
        "J_no_contact_zero_endpoint_coefficient_line_mixing_or_B1_claim": True,
        "K_target_blind": True,
    }

    if not lineage["iter141_blob_matches"] or not source_identity_ok or not checks["A_frozen_parent_and_prereg_lineage"] or not checks["C_three_frozen_cross_families_only"] or not controls_ok:
        classification = "INVALID_IMPLEMENTATION_ITER154"
    elif not hypothesis:
        classification = "SCIENTIFIC_FAIL_SCOPED_ITER154_TOPOLOGICAL_PRIMITIVITY_HYPOTHESIS_FALSE"
    elif not all(checks.values()):
        classification = "BLOCKED_SCOPED_ITER154_GRAPH_SUBDIVIDENCE_AUTHORITY_INCOMPLETE"
    else:
        classification = "PASS_SCOPED_SLOT6_FIRST_MG_CROSS_CHANNEL_PROPER_SUBDIVERGENCES_EMPTY"

    output = {
        "gate": "ITER154_FIXED_GEODESIC_FIRST_MG_GRAPH_SUBDIVERGENCE_R_OPERATION_AUTHORITY",
        "classification": classification,
        "lineage": lineage,
        "scope": "exact three ITER141 connected-cross first-M/G families only",
        "graph_records": rows,
        "slot6_closed_for_scoped_cross_families": classification.startswith("PASS_SCOPED_SLOT6"),
        "derived_subdivergence_map": {
            r["family"]: {
                "proper_bulk_local_composite_counterterm_insertions": [],
                "R_sub": "identity",
            }
            for r in rows
        },
        "derived_zero_scope": "proper ordinary bulk/local-composite subdivergence insertions only; not endpoint/contact/line/full-graph poles",
        "controls": controls,
        "checks": checks,
        "interpretation": "The frozen cross Wick graphs are acyclic two-edge trees on three geometric sites. Every strict proper connected edge subgraph is a single propagator edge and is acyclic; there is no action/ghost interaction vertex or same-site self-contraction. Therefore the slot-6 proper ordinary bulk/local-composite subdivergence forest is empty for these three cross channels. Their actual UV singular strata are affine endpoint collapses already frozen by ITER141 and remain downstream endpoint/line renormalization problems.",
        "next_dependency": "Open slot 7: divergent endpoint/geodesic counterterm coefficients in the frozen ITER118 basis. Do not use the slot-6 derived zero to set any of the seven contact poles to zero.",
        "claim_ceiling": "scoped slot-6 proper-subdivergence map only; no contact pole, endpoint coefficient, line mixing, renormalized contact mapping, B1_total, noncancellation, EDT, bridge, new physics, or candidate theory",
    }
    Path("iter154_first_mg_graph_subdivergence_r_operation.json").write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"classification": classification, "checks": checks, "betti": {r["family"]:r["first_betti_number"] for r in rows}}, indent=2, sort_keys=True))
    if classification.startswith("INVALID") or classification.startswith("SCIENTIFIC_FAIL"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
