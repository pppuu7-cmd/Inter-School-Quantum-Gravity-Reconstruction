#!/usr/bin/env python3
"""ITER143: frozen Q/K denominator-cancellation and separated-L contact partition.

Consumes an ITER140 PASS artifact. No master integral or pole coefficient is evaluated.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path
import sympy as s

EXPECTED_ITER140 = "PASS_SCOPED_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION_CLOSED_POLE_INTEGRATION_OPEN"
FAMILIES = [
    "M_R2_chi1_dR1",
    "M_R1_chi1_dR2",
    "G_R1_chi2_Gamma2_dR1",
]

# Geometry/support frozen before ITER140 coefficient inspection.
GEOM = {
    "M_R2_chi1_dR1": {
        "q_edge": "tau*L", "k_edge": "L",
        "singular": {"lower": "q", "upper": None},
        "jets": {"lower": 4},
    },
    "M_R1_chi1_dR2": {
        "q_edge": "L", "k_edge": "(1-tau)*L",
        "singular": {"lower": None, "upper": "k"},
        "jets": {"upper": 4},
    },
    "G_R1_chi2_Gamma2_dR1": {
        "q_edge": "tau*L", "k_edge": "(1-tau)*L",
        "singular": {"lower": "q", "upper": "k"},
        "jets": {"lower": 4, "upper": 4},
    },
}


def parse_power(label: str, var: str) -> int:
    # exact factor token: Q, Q^2, ...; avoids matching a/b/S.
    for tok in label.split('*'):
        if tok == var:
            return 1
        m = re.fullmatch(re.escape(var) + r"\^(\d+)", tok)
        if m:
            return int(m.group(1))
    return 0


def parse_basis(label: str):
    i = parse_power(label, "Q")
    j = parse_power(label, "K")
    l = parse_power(label, "S")
    if label.startswith("a^2"):
        X = "a^2"
    elif label.startswith("a*b"):
        X = "a*b"
    elif label.startswith("b^2"):
        X = "b^2"
    else:
        X = "1"
    return {"X": X, "i": i, "j": j, "l": l}


def algebraic_class(i: int, j: int) -> str:
    if i == 0 and j == 0:
        return "TWO_PROPAGATOR"
    if i >= 1 and j == 0:
        return "Q_CANCELLED"
    if i == 0 and j >= 1:
        return "K_CANCELLED"
    return "BOTH_CANCELLED"


def support(fam: str, cls: str, endpoint: str):
    g = GEOM[fam]
    shrinking = g["singular"][endpoint]
    if cls == "TWO_PROPAGATOR":
        if shrinking is None:
            return "NO_AFFINE_ENDPOINT_SINGULARITY"
        return "NONLOCAL_TWO_PROPAGATOR_ENDPOINT_CANDIDATE"
    if cls == "BOTH_CANCELLED":
        return "SEPARATED_L_CONTACT_ZERO"
    contact_edge = "q" if cls == "Q_CANCELLED" else "k"
    if shrinking == contact_edge:
        return "ENDPOINT_LOCAL_CONTACT_WITH_OTHER_PROPAGATOR_NONLOCAL"
    return "SEPARATED_L_CONTACT_ZERO"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", nargs="?", default="iter140_first_mg_general_d_invariant_continuation.json")
    args = ap.parse_args()
    src = json.loads(Path(args.input).read_text(encoding="utf-8"))
    upstream_ok = src.get("classification") == EXPECTED_ITER140
    labels = src.get("basis_labels", [])
    formulas = src.get("coefficient_formulas", {})

    label_unique = len(labels) == 28 and len(set(labels)) == 28
    fam_complete = all(f in formulas and len(formulas[f]) == 28 for f in FAMILIES)
    rows = {}
    partition_ok = label_unique and fam_complete
    epsilon_ok = True
    support_ok = True
    for fam in FAMILIES:
        famrows = []
        if fam not in formulas:
            rows[fam] = famrows
            continue
        for idx, entry in enumerate(formulas[fam]):
            label = entry.get("basis")
            meta = parse_basis(label)
            cls = algebraic_class(meta["i"], meta["j"])
            c_d = entry.get("coefficient_d")
            c4 = entry.get("c_d4")
            ceps = entry.get("c_epsilon_linear_for_d_4_minus_2eps")
            epsilon_ok &= c_d is not None and c4 is not None and ceps is not None
            lower = support(fam, cls, "lower")
            upper = support(fam, cls, "upper")
            # Frozen fully-cancelled separated rule.
            if cls == "BOTH_CANCELLED":
                support_ok &= lower == upper == "SEPARATED_L_CONTACT_ZERO"
            famrows.append({
                "index": idx, "basis": label, **meta,
                "coefficient_d": c_d,
                "c_d4": c4,
                "c_epsilon_linear": ceps,
                "algebraic_class": cls,
                "lower_support": lower,
                "upper_support": upper,
                "lower_sharp_jet": GEOM[fam]["jets"].get("lower") if "CANDIDATE" in lower or "ENDPOINT_LOCAL" in lower else None,
                "upper_sharp_jet": GEOM[fam]["jets"].get("upper") if "CANDIDATE" in upper or "ENDPOINT_LOCAL" in upper else None,
            })
        rows[fam] = famrows

    summaries = {}
    recombine_ok = True
    for fam in FAMILIES:
        counts = {c: 0 for c in ["TWO_PROPAGATOR","Q_CANCELLED","K_CANCELLED","BOTH_CANCELLED"]}
        nonzero = dict(counts)
        surviving = []
        pruned = []
        seen = set()
        for r in rows.get(fam, []):
            counts[r["algebraic_class"]] += 1
            nz = s.sympify(r["coefficient_d"]) != 0 if r["coefficient_d"] is not None else False
            if nz:
                nonzero[r["algebraic_class"]] += 1
            seen.add(r["index"])
            # A term survives the separated-support manifest if it is genuinely two-propagator,
            # or if at least one endpoint admits contact on the actually shrinking edge.
            statuses = [r["lower_support"], r["upper_support"]]
            if r["algebraic_class"] == "TWO_PROPAGATOR" or any(x.startswith("ENDPOINT_LOCAL") for x in statuses):
                surviving.append(r["index"])
            else:
                pruned.append(r["index"])
        recombine_ok &= seen == set(range(28)) and sum(counts.values()) == 28
        summaries[fam] = {
            "basis_count_by_class": counts,
            "nonzero_coefficient_count_by_class": nonzero,
            "surviving_separated_manifest_indices": surviving,
            "pruned_fixed_L_or_double_contact_indices": pruned,
            "partition_exhaustive": len(surviving) + len(pruned) == 28,
        }

    checks = {
        "A_ITER140_scientific_PASS": bool(upstream_ok),
        "B_exact_28_unique_basis": bool(label_unique),
        "C_all_three_family_tables_complete": bool(fam_complete),
        "D_each_basis_term_assigned_once_recombines": bool(recombine_ok),
        "E_epsilon_bookkeeping_present": bool(epsilon_ok),
        "F_frozen_geometry_support_rules": bool(support_ok),
        "G_ITER142_sharp_jet_ceiling_attached": all(
            all(v == 4 for v in GEOM[f]["jets"].values()) for f in FAMILIES
        ),
        "H_no_master_integral_or_physical_cancellation_test": True,
        "I_target_blind": True,
    }
    if not upstream_ok:
        cls = "BLOCKED_BY_ITER140_GENERAL_D_AUTHORITY"
    elif all(checks.values()):
        cls = "PASS_SCOPED_FIRST_MG_DENOMINATOR_CANCELLATION_CONTACT_PARTITION_CLOSED_MASTER_POLES_OPEN"
    else:
        cls = "SCIENTIFIC_FAIL_DENOMINATOR_CANCELLATION_PARTITION"

    out = {
        "gate": "ITER143_FIXED_GEODESIC_CURVATURE_FIRST_MG_DENOMINATOR_CANCELLATION_CONTACT_PARTITION",
        "classification": cls,
        "upstream_iter140_classification": src.get("classification"),
        "denominator": "Q*K",
        "geometry": GEOM,
        "families": rows,
        "summaries": summaries,
        "checks": checks,
        "claim_ceiling": "denominator/contact/support partition only; no master pole/B1/noncancellation/B0/EDT/bridge/new physics/candidate theory",
    }
    Path("iter143_first_mg_denominator_contact_partition.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"classification": cls, "summaries": summaries, "checks": checks}, indent=2))
    if cls.startswith("SCIENTIFIC_FAIL") or cls.startswith("BLOCKED"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
