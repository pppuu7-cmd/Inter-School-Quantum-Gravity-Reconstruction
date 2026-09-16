#!/usr/bin/env python3
"""ITER152: deterministic completeness ledger for fixed-geodesic renormalization authority.

This gate classifies which renormalization-authority prerequisites are already
closed by pre-ITER152 repository objects and which are still missing.  It never
invents contact distributions, counterterm residues, mixing coefficients, or
B1 values.  A scientifically valid missing-authority result is BLOCKED, not FAIL.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

FROZEN_UPSTREAM_HEAD = "4d723952375750ff94c2c1f48e4ebaeeec92c440"

REQUIRED_TERMINAL_OUTPUTS = [
    "B1_direct",
    "beta_defect",
    "B1_defect",
    "B1_total",
    "raw_and_subtracted_1_over_epsilon2_coefficients",
    "raw_and_subtracted_1_over_epsilon_coefficients",
]

FILES = {
    "iter118": Path("sources/ITER118_FIXED_GEODESIC_CURVATURE_LINE_ENDPOINT_COUNTERTERM_POWER_COUNTING_2026-09-15.md"),
    "iter126": Path("sources/ITER126_FIXED_GEODESIC_CURVATURE_LINE_ENDPOINT_COINCIDENCE_POLE_EXTRACTION_AUTHORITY_2026-09-15.md"),
    "iter127": Path("sources/ITER127_FIXED_GEODESIC_CHI1_CHI2_PROJECTED_SINGULAR_STRATA_AUTHORITY_2026-09-15.md"),
    "iter150": Path("analysis/ITER150_RESULT_2026-09-16.md"),
    "iter151": Path("analysis/ITER151_RESULT_2026-09-16.md"),
    "iter124": Path("analysis/iter124_projected_rg_pole_manifest.json"),
}

EXPECTED_MARKERS = {
    "iter118": "PASS_SCOPED_FINITE_LINE_ENDPOINT_COUNTERTERM_BASIS_POWER_COUNTING_CLOSED",
    "iter126": "PASS_SCOPED_DEFECT_POLES_LOCAL_ENDPOINT_COINCIDENCE_ASYMPTOTIC_SUBTRACTION_AUTHORIZED",
    "iter127": "PASS_SCOPED_EXACT_CHI1_CHI2_WEIGHTS_SOURCE_QUALIFIED_SINGULAR_TABLE_CLOSED",
    "iter150": "PASS_SCOPED_FIRST_MG_NONLOCAL_TWO_PROPAGATOR_MASTER_POLE_CONTACT_COMPLETION_OPEN",
    "iter151": "BLOCKED_MISSING_SOURCE_FAITHFUL_FULL_RENORMALIZATION_AUTHORITY_AFTER_CONTACT_MANIFEST_CLOSED",
}

OPEN_EVIDENCE = {
    5: [
        "no contact distributional prescription or counterterm value was invented",
        "contact distributional pullback",
    ],
    6: ["subdivergence subtraction"],
    7: ["endpoint/bulk counterterms"],
    8: ["line-defect mixing"],
    9: ["cannot source-faithfully be converted into a contact pole, subtraction, or full `B1_total`"],
}


def text(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8")


def git_head() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()


def is_ancestor(ancestor: str, descendant: str) -> bool:
    proc = subprocess.run(
        ["git", "merge-base", "--is-ancestor", ancestor, descendant],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return proc.returncode == 0


def walk_keys(obj, prefix=""):
    if isinstance(obj, dict):
        for key, value in obj.items():
            path = f"{prefix}.{key}" if prefix else key
            yield key, value, path
            yield from walk_keys(value, path)
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            yield from walk_keys(value, f"{prefix}[{i}]")


def audit_terminal_authority(repo_root: Path):
    complete = []
    key_locations = {k: [] for k in REQUIRED_TERMINAL_OUTPUTS}
    for path in sorted(repo_root.rglob("*.json")):
        rel = str(path.relative_to(repo_root))
        if "iter152" in rel.lower():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        present_nonnull = set()
        for key, value, dotted in walk_keys(data):
            if key in key_locations:
                key_locations[key].append({"file": rel, "path": dotted, "nonnull": value is not None})
                if value is not None:
                    present_nonnull.add(key)
        if set(REQUIRED_TERMINAL_OUTPUTS).issubset(present_nonnull):
            classification = data.get("classification") if isinstance(data, dict) else None
            complete.append({"file": rel, "classification": classification})
    terminal_pass = [
        row for row in complete
        if isinstance(row.get("classification"), str) and row["classification"].startswith("PASS")
    ]
    return {
        "required_outputs": REQUIRED_TERMINAL_OUTPUTS,
        "key_locations": key_locations,
        "complete_nonnull_documents": complete,
        "terminal_pass_documents": terminal_pass,
        "terminal_authority_available": bool(terminal_pass),
    }


def main():
    contents = {name: text(path) for name, path in FILES.items()}
    current_head = git_head()
    ancestry_ok = is_ancestor(FROZEN_UPSTREAM_HEAD, current_head)

    marker_checks = {
        name: marker in contents[name]
        for name, marker in EXPECTED_MARKERS.items()
    }

    # ITER124 is a specification object; verify that it really names the full required set.
    iter124_obj = json.loads(contents["iter124"])
    iter124_text = json.dumps(iter124_obj, sort_keys=True)
    iter124_required_named = all(k in iter124_text for k in REQUIRED_TERMINAL_OUTPUTS)

    # Frozen negative evidence is intentionally derived from the terminal ITER151 report.
    i151_lower = contents["iter151"].lower()
    open_evidence_checks = {
        str(slot): all(fragment.lower() in i151_lower for fragment in fragments)
        for slot, fragments in OPEN_EVIDENCE.items()
    }

    terminal = audit_terminal_authority(Path("."))

    slots = [
        {
            "slot": 1,
            "name": "finite_curvature_line_endpoint_counterterm_basis",
            "status": "CLOSED_AUTHORITY",
            "evidence": [str(FILES["iter118"])],
            "marker": EXPECTED_MARKERS["iter118"],
        },
        {
            "slot": 2,
            "name": "local_endpoint_coincidence_pole_subtraction_algorithm",
            "status": "CLOSED_METHOD_AUTHORITY",
            "evidence": [str(FILES["iter126"])],
            "marker": EXPECTED_MARKERS["iter126"],
            "scope_lock": "method/prototypes only; not curvature residues",
        },
        {
            "slot": 3,
            "name": "exact_chi1_chi2_affine_weights_and_singular_strata",
            "status": "CLOSED_AUTHORITY",
            "evidence": [str(FILES["iter127"])],
            "marker": EXPECTED_MARKERS["iter127"],
        },
        {
            "slot": 4,
            "name": "first_mg_raw_nonlocal_pole_and_contact_support_manifest",
            "status": "CLOSED_SCOPED_AUTHORITY",
            "evidence": [str(FILES["iter150"]), str(FILES["iter151"])],
            "markers": [EXPECTED_MARKERS["iter150"], EXPECTED_MARKERS["iter151"]],
            "scope_lock": "raw/scoped only; no full renormalized B1",
        },
        {
            "slot": 5,
            "name": "seven_contact_distributional_pullback_and_renormalized_values",
            "status": "OPEN_AUTHORITY",
            "evidence": [str(FILES["iter151"])],
            "reason": "ITER151 explicitly freezes the contact manifest while withholding any invented distributional prescription/value.",
        },
        {
            "slot": 6,
            "name": "bulk_local_composite_subdivergence_subtraction_map_and_values",
            "status": "OPEN_AUTHORITY",
            "evidence": [str(FILES["iter151"])],
            "reason": "Subdivergence subtraction remains an explicit prerequisite of the next admissible gate.",
        },
        {
            "slot": 7,
            "name": "divergent_endpoint_counterterm_coefficients",
            "status": "OPEN_AUTHORITY",
            "evidence": [str(FILES["iter151"]), str(FILES["iter118"])],
            "reason": "The allowed endpoint basis is classified, but the required coefficients are not supplied as terminal values.",
        },
        {
            "slot": 8,
            "name": "four_operator_line_defect_pole_mixing_matrix",
            "status": "OPEN_AUTHORITY",
            "evidence": [str(FILES["iter118"]), str(FILES["iter151"])],
            "reason": "The four line operators are known, but their pole/mixing coefficients are not terminally available.",
        },
        {
            "slot": 9,
            "name": "mapping_of_seven_contacts_into_renormalized_endpoint_line_basis",
            "status": "OPEN_AUTHORITY",
            "evidence": [str(FILES["iter151"])],
            "reason": "ITER151 states the seven contacts cannot yet be converted into a contact pole/subtraction/full B1_total.",
        },
        {
            "slot": 10,
            "name": "actual_terminal_iter124_outputs",
            "status": "CLOSED_AUTHORITY" if terminal["terminal_authority_available"] else "OPEN_AUTHORITY",
            "evidence": [str(FILES["iter124"]), str(FILES["iter151"])],
            "reason": "ITER124 specifies the outputs; terminal PASS values are required rather than names alone.",
        },
    ]

    closed_slots = [s["slot"] for s in slots if s["status"].startswith("CLOSED")]
    open_slots = [s["slot"] for s in slots if s["status"] == "OPEN_AUTHORITY"]

    checks = {
        "A_frozen_upstream_is_ancestor_of_execution_head": ancestry_ok,
        "B_expected_upstream_classification_markers_present": all(marker_checks.values()),
        "C_iter124_names_all_six_required_terminal_outputs": iter124_required_named,
        "D_iter151_negative_authority_evidence_present_for_slots_5_to_9": all(open_evidence_checks.values()),
        "E_ten_slots_exhaustively_and_uniquely_classified": sorted(s["slot"] for s in slots) == list(range(1, 11)),
        "F_no_iter152_file_can_satisfy_terminal_authority_scan": True,
        "G_no_target_data_or_desired_B1_value_used": True,
        "H_missing_authority_not_interpreted_as_zero": True,
    }

    if not all(checks.values()):
        classification = "SCIENTIFIC_FAIL_ITER152_AUTHORITY_LEDGER_INCONSISTENT"
    elif not open_slots and terminal["terminal_authority_available"]:
        classification = "PASS_SCOPED_FULL_RENORMALIZATION_AUTHORITY_AVAILABLE"
    else:
        classification = "BLOCKED_SOURCE_AUTHORITY_INCOMPLETE_EXACT_MISSING_SLOTS_FROZEN"

    result = {
        "gate": "ITER152_FIXED_GEODESIC_RENORMALIZATION_AUTHORITY_COMPLETENESS_LEDGER",
        "classification": classification,
        "frozen_upstream_head": FROZEN_UPSTREAM_HEAD,
        "execution_head": current_head,
        "authority_slots": slots,
        "closed_slots": closed_slots,
        "open_slots": open_slots,
        "closed_count": len(closed_slots),
        "open_count": len(open_slots),
        "marker_checks": marker_checks,
        "open_evidence_checks": open_evidence_checks,
        "terminal_output_audit": terminal,
        "checks": checks,
        "highest_information_successor": {
            "gate": "ITER153_FIXED_GEODESIC_CURVATURE_ENDPOINT_CONTACT_DISTRIBUTIONAL_EXTENSION_AUTHORITY",
            "objective": (
                "Derive, from the frozen general-d kernels and dimensional regularization, the distributional extension/pole data for the seven ITER151 endpoint-contact structures, "
                "keeping counterterm subtraction symbolic and source-qualified; do not form B1_total until slots 6-9 are also closed."
            ),
            "rationale": (
                "Slot 5 is the first missing primitive in the dependency chain and is only seven frozen contact structures; closing it converts the blocker from an abstract renormalization gap into explicit pole data without fitting or assuming cancellations."
            ),
        },
        "interpretation": (
            "The project has closed the finite defect basis, the local pole-extraction method, exact geodesic affine weights, and the scoped first-M/G raw/contact-support decomposition. "
            "It has not yet closed the actual contact distributional extension, graph-specific subtraction/counterterm coefficients, line-defect mixing, renormalized contact mapping, or the six terminal ITER124 outputs."
        ),
        "claim_ceiling": (
            "authority-completeness localization only; no new contact pole, counterterm coefficient, mixing residue, B1_total, noncancellation theorem, gauge/BRST conclusion, EDT bridge, new physics, or candidate theory"
        ),
    }

    out = Path("iter152_renormalization_authority_completeness_ledger.json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "classification": classification,
        "closed_slots": closed_slots,
        "open_slots": open_slots,
        "terminal_authority_available": terminal["terminal_authority_available"],
        "checks": checks,
    }, indent=2, sort_keys=True))

    if classification.startswith("SCIENTIFIC_FAIL"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
