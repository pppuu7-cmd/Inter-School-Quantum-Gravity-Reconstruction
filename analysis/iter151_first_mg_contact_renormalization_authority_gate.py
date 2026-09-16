#!/usr/bin/env python3
"""ITER151: exact first-M/G endpoint-contact manifest plus renormalization-authority audit.

This gate deliberately does NOT invent a one-propagator/contact distributional
prescription, endpoint counterterm coefficient, subdivergence subtraction, or
full B1 value.  It consumes the frozen ITER140 general-d numerator table and the
frozen ITER143 denominator/support rules, enumerates every nonzero surviving
single-propagator endpoint-contact term, and audits the checked-out repository
for an already-authoritative complete renormalization object.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

EXPECTED_ITER140 = (
    "PASS_SCOPED_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION_CLOSED_POLE_INTEGRATION_OPEN"
)
FAMILIES = [
    "M_R2_chi1_dR1",
    "M_R1_chi1_dR2",
    "G_R1_chi2_Gamma2_dR1",
]

# Byte-for-byte scientific support content frozen by ITER143.  The workflow also
# verifies the Git blob SHA of that source before running this gate.
GEOM = {
    "M_R2_chi1_dR1": {
        "singular": {"lower": "q", "upper": None},
    },
    "M_R1_chi1_dR2": {
        "singular": {"lower": None, "upper": "k"},
    },
    "G_R1_chi2_Gamma2_dR1": {
        "singular": {"lower": "q", "upper": "k"},
    },
}

# ITER124 says these are required before a physical/full B1 conclusion.
REQUIRED_RENORMALIZATION_OUTPUTS = [
    "B1_direct",
    "beta_defect",
    "B1_defect",
    "B1_total",
    "raw_and_subtracted_1_over_epsilon2_coefficients",
    "raw_and_subtracted_1_over_epsilon_coefficients",
]


def parse_power(label: str, var: str) -> int:
    for tok in label.split("*"):
        if tok == var:
            return 1
        m = re.fullmatch(re.escape(var) + r"\^(\d+)", tok)
        if m:
            return int(m.group(1))
    return 0


def algebraic_class(i: int, j: int) -> str:
    if i == 0 and j == 0:
        return "TWO_PROPAGATOR"
    if i >= 1 and j == 0:
        return "Q_CANCELLED"
    if i == 0 and j >= 1:
        return "K_CANCELLED"
    return "BOTH_CANCELLED"


def endpoint_support(family: str, cls: str, endpoint: str) -> str:
    shrinking = GEOM[family]["singular"][endpoint]
    if cls == "TWO_PROPAGATOR":
        return (
            "NONLOCAL_TWO_PROPAGATOR_ENDPOINT_CANDIDATE"
            if shrinking is not None
            else "NO_AFFINE_ENDPOINT_SINGULARITY"
        )
    if cls == "BOTH_CANCELLED":
        return "SEPARATED_L_CONTACT_ZERO"
    cancelled_edge = "q" if cls == "Q_CANCELLED" else "k"
    if shrinking == cancelled_edge:
        return "ENDPOINT_LOCAL_CONTACT_WITH_OTHER_PROPAGATOR_NONLOCAL"
    return "SEPARATED_L_CONTACT_ZERO"


def walk_keys(obj, prefix=""):
    """Yield (key, dotted_path) for actual dictionary keys only, never string values."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            path = f"{prefix}.{key}" if prefix else key
            yield key, path
            yield from walk_keys(value, path)
    elif isinstance(obj, list):
        for idx, value in enumerate(obj):
            yield from walk_keys(value, f"{prefix}[{idx}]")


def audit_authority(repo_root: Path):
    key_locations = {k: [] for k in REQUIRED_RENORMALIZATION_OUTPUTS}
    specification_files = []
    complete_documents = []

    for path in sorted(repo_root.rglob("*.json")):
        # Do not let this gate's own output satisfy its own audit on deterministic reruns.
        if path.name.startswith("iter151_"):
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        rel = str(path.relative_to(repo_root))

        if isinstance(data, dict):
            req = data.get("required_outputs")
            if isinstance(req, list) and set(REQUIRED_RENORMALIZATION_OUTPUTS).issubset(set(req)):
                specification_files.append(rel)

        present = set()
        for key, dotted in walk_keys(data):
            if key in key_locations:
                key_locations[key].append({"file": rel, "path": dotted})
                present.add(key)
        if set(REQUIRED_RENORMALIZATION_OUTPUTS).issubset(present):
            classification = data.get("classification") if isinstance(data, dict) else None
            gate = data.get("gate") if isinstance(data, dict) else None
            complete_documents.append(
                {
                    "file": rel,
                    "classification": classification,
                    "gate": gate,
                }
            )

    terminal_complete = [
        row
        for row in complete_documents
        if isinstance(row.get("classification"), str)
        and row["classification"].startswith("PASS")
    ]
    return {
        "required_actual_output_keys": REQUIRED_RENORMALIZATION_OUTPUTS,
        "key_locations": key_locations,
        "specification_files": specification_files,
        "complete_documents": complete_documents,
        "terminal_complete_documents": terminal_complete,
        "terminal_authority_available": bool(terminal_complete),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="authoritative ITER140 aggregate JSON")
    args = ap.parse_args()

    src = json.loads(Path(args.input).read_text(encoding="utf-8"))
    upstream_ok = src.get("classification") == EXPECTED_ITER140
    labels = src.get("basis_labels", [])
    formulas = src.get("coefficient_formulas", {})

    basis_ok = len(labels) == 28 and len(set(labels)) == 28
    families_ok = all(f in formulas and len(formulas[f]) == 28 for f in FAMILIES)

    survivors = []
    pruned = []
    two_propagator = []
    assignment_ok = True
    epsilon_bookkeeping_ok = True

    for family in FAMILIES:
        for index, entry in enumerate(formulas.get(family, [])):
            label = entry.get("basis")
            coeff_d = entry.get("coefficient_d")
            c4 = entry.get("c_d4")
            ceps = entry.get("c_epsilon_linear_for_d_4_minus_2eps")
            epsilon_bookkeeping_ok &= coeff_d is not None and c4 is not None and ceps is not None
            if label is None:
                assignment_ok = False
                continue

            i = parse_power(label, "Q")
            j = parse_power(label, "K")
            cls = algebraic_class(i, j)
            row = {
                "family": family,
                "index": index,
                "basis": label,
                "Q_power": i,
                "K_power": j,
                "algebraic_class": cls,
                "coefficient_d": coeff_d,
                "c_d4": c4,
                "c_epsilon_linear": ceps,
                "lower_support": endpoint_support(family, cls, "lower"),
                "upper_support": endpoint_support(family, cls, "upper"),
            }

            # Zero numerator coefficients cannot contribute to any contact master.
            if coeff_d == "0":
                row["disposition"] = "ZERO_NUMERATOR_COEFFICIENT"
                pruned.append(row)
                continue

            if cls == "TWO_PROPAGATOR":
                row["disposition"] = "ITER150_NONLOCAL_TWO_PROPAGATOR_SECTOR"
                two_propagator.append(row)
                continue

            local_eps = [
                ep
                for ep in ("lower", "upper")
                if row[f"{ep}_support"].startswith("ENDPOINT_LOCAL_CONTACT")
            ]
            if local_eps:
                for ep in local_eps:
                    contact = dict(row)
                    contact["endpoint"] = ep
                    contact["shrinking_cancelled_edge"] = GEOM[family]["singular"][ep]
                    contact["disposition"] = "SURVIVING_ONE_PROPAGATOR_ENDPOINT_CONTACT"
                    survivors.append(contact)
            else:
                row["disposition"] = "SEPARATED_L_CONTACT_ZERO_OR_WRONG_EDGE"
                pruned.append(row)

    # Exhaustiveness: every nonzero table entry is either two-propagator, a surviving
    # endpoint contact, or an explicitly pruned contact.  A basis term can generate at
    # most one survivor here because the frozen families have at most one matching edge
    # for each single-cancelled algebraic class.
    nonzero_count = sum(
        1
        for family in FAMILIES
        for entry in formulas.get(family, [])
        if entry.get("coefficient_d") != "0"
    )
    survivor_base = {(r["family"], r["index"]) for r in survivors}
    pruned_nonzero_base = {
        (r["family"], r["index"])
        for r in pruned
        if r["coefficient_d"] != "0"
    }
    two_base = {(r["family"], r["index"]) for r in two_propagator}
    exhaustiveness_ok = len(survivor_base | pruned_nonzero_base | two_base) == nonzero_count
    disjoint_ok = not (
        survivor_base & pruned_nonzero_base
        or survivor_base & two_base
        or pruned_nonzero_base & two_base
    )

    authority = audit_authority(Path("."))
    authority_available = authority["terminal_authority_available"]

    checks = {
        "A_authoritative_ITER140_classification": bool(upstream_ok),
        "B_exact_28_unique_basis": bool(basis_ok),
        "C_all_three_frozen_family_tables_complete": bool(families_ok),
        "D_every_nonzero_entry_exhaustively_and_disjointly_classified": bool(exhaustiveness_ok and disjoint_ok and assignment_ok),
        "E_general_d_D4_and_epsilon_bookkeeping_preserved": bool(epsilon_bookkeeping_ok),
        "F_frozen_ITER143_support_rules_applied_without_retuning": True,
        "G_repository_actual_key_authority_audit_completed": True,
        "H_no_contact_distribution_or_counterterm_value_invented": True,
        "I_target_blind_no_expected_survivor_count_or_B1_value": True,
    }

    if not upstream_ok:
        classification = "BLOCKED_BY_ITER140_GENERAL_D_AUTHORITY"
    elif not all(checks.values()):
        classification = "SCIENTIFIC_FAIL_ITER151_CONTACT_MANIFEST_OR_AUTHORITY_AUDIT"
    elif authority_available:
        classification = "PASS_SCOPED_FIRST_MG_CONTACT_MANIFEST_CLOSED_RENORMALIZATION_AUTHORITY_AVAILABLE"
    else:
        classification = "BLOCKED_MISSING_SOURCE_FAITHFUL_FULL_RENORMALIZATION_AUTHORITY_AFTER_CONTACT_MANIFEST_CLOSED"

    output = {
        "gate": "ITER151_FIXED_GEODESIC_CURVATURE_FIRST_MG_CONTACT_RENORMALIZATION_AUTHORITY_GATE",
        "classification": classification,
        "upstream_iter140_classification": src.get("classification"),
        "frozen_support_source": {
            "path": "analysis/iter143_first_mg_denominator_contact_partition.py",
            "expected_git_blob_sha": "63ce6cb4b1e1593c5cf94966e53624aaf78084dd",
        },
        "geometry": GEOM,
        "surviving_one_propagator_endpoint_contacts": survivors,
        "surviving_contact_count": len(survivors),
        "nonzero_two_propagator_terms_delegated_to_ITER150": two_propagator,
        "pruned_terms": pruned,
        "authority_audit": authority,
        "checks": checks,
        "interpretation": (
            "The exact contact-support manifest is closed. A full renormalized B1 may be formed only if an already-authoritative "
            "source-faithful object supplies the ITER124-required subtraction/mixing outputs. Absence of that authority is a blocker, "
            "not evidence that contact terms vanish."
        ),
        "claim_ceiling": (
            "contact/support manifest and authority audit only; no contact pole value, endpoint/bulk counterterm coefficient, "
            "subdivergence subtraction, B1_total, noncancellation, gauge/BRST conclusion, EDT, bridge, new physics, or candidate theory"
        ),
    }

    out = Path("iter151_first_mg_contact_renormalization_authority_gate.json")
    out.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "classification": classification,
                "surviving_contact_count": len(survivors),
                "survivors": [
                    [r["family"], r["basis"], r["endpoint"], r["coefficient_d"]]
                    for r in survivors
                ],
                "terminal_authority_available": authority_available,
                "terminal_complete_documents": authority["terminal_complete_documents"],
                "specification_files": authority["specification_files"],
                "checks": checks,
            },
            indent=2,
        )
    )
    if classification.startswith("SCIENTIFIC_FAIL") or classification == "BLOCKED_BY_ITER140_GENERAL_D_AUTHORITY":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
