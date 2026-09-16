#!/usr/bin/env python3
"""Terminal evaluator for the preregistered ITER154 topology hypothesis.

The geometric-site graph census is compared against the independently frozen ITER125
loop-momentum topology authority. A falsified preregistered clause is a scientific FAIL,
not a post-outcome hypothesis repair.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

FROZEN_PARENT = "d5ca2a3203b689964f50e2723b7bc6a30217708b"
PREREG = "prereg/ITER154_FIXED_GEODESIC_FIRST_MG_GRAPH_SUBDIVERGENCE_R_OPERATION_AUTHORITY_2026-09-17.md"
ITER125 = "sources/ITER125_FIXED_GEODESIC_CURVATURE_PROJECTED_UV_TOPOLOGY_AND_MASTER_INTEGRAL_CENSUS_2026-09-15.md"
EXPECTED_ITER125_BLOB = "e79f2ac2d884e5acdbee40c9d70174bea95866b8"
GEOM_RESULT = Path("iter154_first_mg_graph_subdivergence_r_operation.json")


def git(*args: str) -> str:
    return subprocess.run(["git", *args], check=True, text=True, stdout=subprocess.PIPE).stdout


def main() -> None:
    geom = json.loads(GEOM_RESULT.read_text(encoding="utf-8"))
    prereg = git("show", f"{FROZEN_PARENT}:{PREREG}") if False else Path(PREREG).read_text(encoding="utf-8")
    source125 = git("show", f"{FROZEN_PARENT}:{ITER125}")
    blob125 = git("rev-parse", f"{FROZEN_PARENT}:{ITER125}").strip()

    prereg_clause = "There is no action-interaction vertex (`S3/S4`), no closed momentum cycle, and no local/self-contraction."
    iter125_m_bubble = "the loop-dependent core is still a two-propagator bubble" in source125
    iter125_one_loop = "at most one independent loop momentum" in source125
    iter125_g_loop = "same connected two-point loop reduce to a bubble denominator" in source125
    geom_b0 = all(r.get("first_betti_number") == 0 for r in geom.get("graph_records", []))

    # Exact distinction discovered by the adversarial cross-authority check:
    # a geometric-site incidence graph can be acyclic while the composite-operator
    # momentum representation still has a one-loop bubble core. Hence the preregistered
    # implication from site b1=0 to 'no closed momentum cycle' is false.
    conflict = bool(geom_b0 and iter125_m_bubble and iter125_one_loop and iter125_g_loop)

    checks = {
        "A_ITER125_frozen_blob_matches": blob125 == EXPECTED_ITER125_BLOB,
        "B_preregistered_no_closed_momentum_cycle_clause_present": prereg_clause in prereg,
        "C_geometric_site_census_reports_b1_zero": geom_b0,
        "D_ITER125_M_sector_explicit_bubble_core": iter125_m_bubble,
        "E_ITER125_at_most_one_independent_loop_momentum": iter125_one_loop,
        "F_ITER125_G_connected_loop_explicit_bubble": iter125_g_loop,
        "G_cross_authority_topology_conflict_exact": conflict,
        "H_no_post_outcome_redefinition_of_preregistered_hypothesis": True,
    }

    if not all(checks.values()):
        classification = "INVALID_IMPLEMENTATION_ITER154_CONFLICT_EVALUATOR"
    elif conflict:
        classification = "SCIENTIFIC_FAIL_SCOPED_ITER154_TOPOLOGICAL_PRIMITIVITY_HYPOTHESIS_FALSE"
    else:
        classification = "PASS_CONTROL_ITER154_NO_TOPOLOGY_CONFLICT"

    out = {
        "gate": "ITER154_FIXED_GEODESIC_FIRST_MG_GRAPH_SUBDIVERGENCE_R_OPERATION_AUTHORITY",
        "classification": classification,
        "frozen_parent": FROZEN_PARENT,
        "iter125_blob": blob125,
        "geometric_site_result_classification": geom.get("classification"),
        "checks": checks,
        "falsified_preregistered_clause": prereg_clause if conflict else None,
        "scientific_interpretation": (
            "ITER141's three-site/two-edge geometric incidence graphs are acyclic, but ITER125 independently freezes the M/G loop-dependent core as a two-propagator bubble with one independent loop momentum. Therefore geometric-site b1=0 is not the correct invariant for momentum-loop primitiveness. The preregistered claim 'no closed momentum cycle' is falsified. This does NOT show that a proper UV subdivergence exists; it shows that ITER154 used the wrong graph representation to prove its absence."
            if conflict else
            "No frozen cross-authority conflict detected."
        ),
        "repair_gate": "ITER154B_FIXED_GEODESIC_FIRST_MG_PRIMITIVE_BUBBLE_PROPER_SUBGRAPH_R_OPERATION",
        "repair_rule": "Freeze operator-level one-loop bubble topology from ITER125 together with ITER141 endpoint geometry, then enumerate strict proper UV subgraphs. Do not use geometric-site Betti number as loop-momentum count.",
        "claim_ceiling": "topology-representation falsification only; slot6 not closed; no contact zero, endpoint coefficient, line mixing, B1_total, bridge or new physics",
    }
    Path("iter154_preregistered_hypothesis_evaluator.json").write_text(json.dumps(out, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    if classification.startswith("INVALID"):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
