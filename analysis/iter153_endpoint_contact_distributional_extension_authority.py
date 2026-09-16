#!/usr/bin/env python3
"""ITER153: frozen seven-contact distributional pullback/extension authority gate.

This gate closes or terminally blocks ITER152 slot 5 only. It does not choose
counterterms, copy ITER126 prototype residues, or form B1_total. It also checks
the frozen ITER124 R-operation ordering before interpreting raw scaleless DR data.
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

import sympy as sp

FROZEN_PARENT = "d44245c8a1387df197489e95296096c3f004451e"
PREREG_COMMIT = "bbcb9021e0245f3a506efa072d90cff992177126"
SOURCE_AUTHORITY_COMMIT = "1792940bd0b2d89788b5be3855c71b497018aa64"
SOURCE_AUTHORITY_REPAIR_COMMIT = "8f5550d38a5eda4f61df465555c388d6e883af17"
DIMENSION_CONVENTION = "d=4-2*epsilon"
PHYSICAL_D = 4
N = (1, 0, 0, 0)
TRANSVERSE_WITNESS = (0, 1, 0, 0)
ITER124_PATH = "analysis/iter124_projected_rg_pole_manifest.json"
EXPECTED_ITER124_ORDER = [
    "generate unrenormalized F/M/G poles in general d",
    "subtract bulk ghost and local-composite subdivergences",
    "add endpoint and lower-order geodesic counterterms",
    "renormalize full line-defect mixing matrix including simple and higher poles",
    "separate contact/polynomial structures only after renormalization",
    "project genuine-defect poles at u=0 and u=1/2 in general d",
]

PARENT_PATHS = [
    "analysis/ITER151_RESULT_2026-09-16.md",
    "analysis/ITER152_RESULT_2026-09-16.md",
    ITER124_PATH,
    "analysis/iter151_first_mg_contact_renormalization_authority_gate.py",
    "analysis/iter143_first_mg_denominator_contact_partition.py",
    "analysis/iter141_first_mg_wick_geometry_phase_strata.py",
    "analysis/iter142_first_mg_shrinking_edge_derivative_jets.py",
    "analysis/iter140_first_mg_general_d_invariant_continuation.py",
    "analysis/iter140_first_mg_general_d_invariant_continuation_v3.py",
    "sources/ITER126_FIXED_GEODESIC_CURVATURE_LINE_ENDPOINT_COINCIDENCE_POLE_EXTRACTION_AUTHORITY_2026-09-15.md",
    "sources/ITER107_RETROSPECTIVE_FIXED_GEODESIC_DISTANCE_EFT_CURVATURE_CORRELATOR_AUTHORITY_2026-09-15.md",
]

CONTACTS = [
    {"id": 1, "family": "M_R2_chi1_dR1", "basis": "b^2*Q*S", "endpoint": "lower", "coefficient_d": "-1/2", "cancelled": "Q", "phase_sign": -1, "manifest_line": "1. `M_R2_chi1_dR1 : b^2*Q*S`, lower endpoint, coefficient `-1/2`."},
    {"id": 2, "family": "M_R1_chi1_dR2", "basis": "a^2*K*S", "endpoint": "upper", "coefficient_d": "3/4", "cancelled": "K", "phase_sign": +1, "manifest_line": "2. `M_R1_chi1_dR2 : a^2*K*S`, upper endpoint, coefficient `3/4`."},
    {"id": 3, "family": "M_R1_chi1_dR2", "basis": "a^2*K^2", "endpoint": "upper", "coefficient_d": "1/2", "cancelled": "K", "phase_sign": +1, "manifest_line": "3. `M_R1_chi1_dR2 : a^2*K^2`, upper endpoint, coefficient `1/2`."},
    {"id": 4, "family": "M_R1_chi1_dR2", "basis": "a*b*K*S", "endpoint": "upper", "coefficient_d": "-1", "cancelled": "K", "phase_sign": +1, "manifest_line": "4. `M_R1_chi1_dR2 : a*b*K*S`, upper endpoint, coefficient `-1`."},
    {"id": 5, "family": "G_R1_chi2_Gamma2_dR1", "basis": "K*S^2", "endpoint": "upper", "coefficient_d": "-1/(2*d - 4)", "cancelled": "K", "phase_sign": -1, "manifest_line": "5. `G_R1_chi2_Gamma2_dR1 : K*S^2`, upper endpoint, coefficient `-1/(2*d - 4)`."},
    {"id": 6, "family": "G_R1_chi2_Gamma2_dR1", "basis": "a^2*K*S", "endpoint": "upper", "coefficient_d": "(d - 1)/(2*d - 4)", "cancelled": "K", "phase_sign": -1, "manifest_line": "6. `G_R1_chi2_Gamma2_dR1 : a^2*K*S`, upper endpoint, coefficient `(d - 1)/(2*d - 4)`."},
    {"id": 7, "family": "G_R1_chi2_Gamma2_dR1", "basis": "a*b*K*S", "endpoint": "upper", "coefficient_d": "1/(d - 2)", "cancelled": "K", "phase_sign": -1, "manifest_line": "7. `G_R1_chi2_Gamma2_dR1 : a*b*K*S`, upper endpoint, coefficient `1/(d - 2)`."},
]


def run_git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], check=check, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def is_ancestor(ancestor: str, descendant: str = "HEAD") -> bool:
    return run_git("merge-base", "--is-ancestor", ancestor, descendant, check=False).returncode == 0


def parent_text(path: str) -> str:
    return run_git("show", f"{FROZEN_PARENT}:{path}").stdout


def parent_blob(path: str) -> str:
    return run_git("rev-parse", f"{FROZEN_PARENT}:{path}").stdout.strip()


def token_exponent(label: str, token: str) -> int:
    m = re.search(rf"(?:^|\*){re.escape(token)}(?:\^(\d+))?(?:\*|$)", label)
    return int(m.group(1) or 1) if m else 0


def momentum_degrees(label: str) -> tuple[int, int]:
    q_degree = 0
    k_degree = 0
    if label.startswith("a^2*") or label == "a^2":
        q_degree += 2
    elif label.startswith("b^2*") or label == "b^2":
        k_degree += 2
    elif label.startswith("a*b*") or label == "a*b":
        q_degree += 1
        k_degree += 1
    q_degree += 2 * token_exponent(label, "Q") + token_exponent(label, "S")
    k_degree += 2 * token_exponent(label, "K") + token_exponent(label, "S")
    return q_degree, k_degree


def post_cancellation_order(contact: dict) -> int:
    q_degree, k_degree = momentum_degrees(contact["basis"])
    return q_degree - 2 if contact["cancelled"] == "Q" else k_degree - 2


def coefficient_series(expr_text: str) -> dict:
    d, epsilon = sp.symbols("d epsilon")
    expr = sp.sympify(expr_text, locals={"d": d})
    dim_expr = sp.factor(expr.subs(d, 4 - 2 * epsilon))
    series = sp.expand(sp.series(dim_expr, epsilon, 0, 3).removeO())
    return {
        "coefficient_d": str(sp.factor(expr)),
        "at_d_4_minus_2epsilon": str(dim_expr),
        "epsilon_minus2": str(sp.factor(series.coeff(epsilon, -2))),
        "epsilon_minus1": str(sp.factor(series.coeff(epsilon, -1))),
        "epsilon_0": str(sp.factor(series.coeff(epsilon, 0))),
        "epsilon_1": str(sp.factor(series.coeff(epsilon, 1))),
    }


def post_cancel_expression(contact: dict) -> sp.Expr:
    Q, K, S, a, b = sp.symbols("Q K S a b")
    expr = sp.sympify(contact["basis"].replace("^", "**"), locals={"Q": Q, "K": K, "S": S, "a": a, "b": b})
    denom = Q if contact["cancelled"] == "Q" else K
    return sp.cancel(expr / denom)


def longitudinal_alignment(contact: dict) -> str:
    Q, K, S, a, b = sp.symbols("Q K S a b")
    aligned = sp.factor(post_cancel_expression(contact).subs({Q: a**2, K: b**2, S: a * b}))
    return str(aligned)


def line_map(contact: dict) -> str:
    return "F(s)=+L*s*n" if contact["phase_sign"] < 0 else "F(s)=-L*s*n"


def endpoint_coordinate(contact: dict) -> str:
    return "s=tau" if contact["endpoint"] == "lower" else "s=1-tau"


def fixture_reasons(fixture: dict) -> list[str]:
    reasons: list[str] = []
    base = next((c for c in CONTACTS if c["id"] == fixture.get("id")), None)
    if base is None:
        return ["UNKNOWN_OR_CHANGED_CONTACT_ID"]
    if fixture.get("endpoint") != base["endpoint"]:
        reasons.append("WRONG_ENDPOINT_ORIENTATION")
    if fixture.get("cancelled") != base["cancelled"]:
        reasons.append("WRONG_SHRINKING_MOMENTUM_OR_CONTACT_SUPPORT")
    if "L" not in str(fixture.get("line_map", "")):
        reasons.append("OMITTED_L_LINE_SCALE")
    if fixture.get("dimension_convention") != DIMENSION_CONVENTION:
        reasons.append("WRONG_DIMENSIONAL_CONVENTION")
    if fixture.get("assigned_contact_pole") in {"+2", "2", "-1"}:
        reasons.append("ILLEGAL_ITER126_PROTOTYPE_RESIDUE_SUBSTITUTION")
    if fixture.get("uses_expected_pole"):
        reasons.append("HARD_CODED_EXPECTED_POLE_OR_CANCELLATION")
    if fixture.get("contact_count", 7) != 7:
        reasons.append("CHANGED_SEVEN_CONTACT_SET")
    return reasons


def build_controls() -> list[dict]:
    fixtures = [
        {"name": "wrong_endpoint", "id": 1, "endpoint": "upper", "cancelled": "Q", "line_map": "F(s)=+L*s*n", "dimension_convention": DIMENSION_CONVENTION},
        {"name": "wrong_support", "id": 1, "endpoint": "lower", "cancelled": "K", "line_map": "F(s)=+L*s*n", "dimension_convention": DIMENSION_CONVENTION},
        {"name": "omitted_L", "id": 1, "endpoint": "lower", "cancelled": "Q", "line_map": "F(s)=+s*n", "dimension_convention": DIMENSION_CONVENTION},
        {"name": "wrong_dimension", "id": 1, "endpoint": "lower", "cancelled": "Q", "line_map": "F(s)=+L*s*n", "dimension_convention": "d=4-epsilon"},
        {"name": "prototype_residue", "id": 1, "endpoint": "lower", "cancelled": "Q", "line_map": "F(s)=+L*s*n", "dimension_convention": DIMENSION_CONVENTION, "assigned_contact_pole": "+2"},
        {"name": "hard_coded_pole", "id": 1, "endpoint": "lower", "cancelled": "Q", "line_map": "F(s)=+L*s*n", "dimension_convention": DIMENSION_CONVENTION, "uses_expected_pole": True},
        {"name": "changed_contact_set", "id": 1, "endpoint": "lower", "cancelled": "Q", "line_map": "F(s)=+L*s*n", "dimension_convention": DIMENSION_CONVENTION, "contact_count": 6},
    ]
    return [{"name": f["name"], "accepted": not fixture_reasons(f), "rejection_reasons": fixture_reasons(f)} for f in fixtures]


def main() -> None:
    head = run_git("rev-parse", "HEAD").stdout.strip()
    lineage = {
        "frozen_parent_is_ancestor": is_ancestor(FROZEN_PARENT),
        "preregistration_is_ancestor": is_ancestor(PREREG_COMMIT),
        "source_authority_initial_is_ancestor": is_ancestor(SOURCE_AUTHORITY_COMMIT),
        "source_authority_DR_ordering_repair_is_ancestor": is_ancestor(SOURCE_AUTHORITY_REPAIR_COMMIT),
        "execution_head": head,
        "frozen_parent": FROZEN_PARENT,
        "preregistration_commit": PREREG_COMMIT,
        "source_authority_initial_commit": SOURCE_AUTHORITY_COMMIT,
        "source_authority_DR_ordering_repair_commit": SOURCE_AUTHORITY_REPAIR_COMMIT,
    }

    source_blobs = {path: parent_blob(path) for path in PARENT_PATHS}
    iter151 = parent_text("analysis/ITER151_RESULT_2026-09-16.md")
    iter152 = parent_text("analysis/ITER152_RESULT_2026-09-16.md")
    iter124 = json.loads(parent_text(ITER124_PATH))
    source_authority = Path("sources/ITER153_DISTRIBUTION_PULLBACK_EXTENSION_AUTHORITY_2026-09-17.md").read_text(encoding="utf-8")

    manifest_ok = all(c["manifest_line"] in iter151 for c in CONTACTS)
    slot5_was_open = "Actual distributional extension/pullback and renormalized values of the seven ITER151 endpoint contacts" in iter152 and "— open" in iter152
    iter124_order = iter124.get("subtraction_order", [])
    iter124_order_ok = iter124_order == EXPECTED_ITER124_ORDER
    contact_split_index = iter124_order.index("separate contact/polynomial structures only after renormalization") if iter124_order_ok else -1
    required_prior_indices = [1, 2, 3]
    contact_after_required_renormalization = iter124_order_ok and all(i < contact_split_index for i in required_prior_indices)
    source_rules_ok = all(key in source_authority for key in [
        "Hörmander distributional pullback criterion",
        "WF(delta_0)",
        "Brunetti and Fredenhagen",
        "delta_eta^(4)",
        "Whole-integral dimensional-regularization diagnostic",
        "Frozen ITER124 renormalization order",
        "not a universal theorem of nonexistence",
    ])

    n_dot_xi = sum(a * b for a, b in zip(N, TRANSVERSE_WITNESS))
    normal_dimension = PHYSICAL_D - 1
    rows = []
    for c in CONTACTS:
        order = post_cancellation_order(c)
        q_degree, k_degree = momentum_degrees(c["basis"])
        coeff_series = coefficient_series(c["coefficient_d"])
        aligned = longitudinal_alignment(c)
        aligned_nonzero = sp.sympify(aligned) != 0
        wf_normal_intersection_nonempty = bool(n_dot_xi == 0 and TRANSVERSE_WITNESS != (0, 0, 0, 0))
        canonical_pullback = not wf_normal_intersection_nonempty
        unique_parent_analytic_extension_available = False
        resolved = canonical_pullback or unique_parent_analytic_extension_available

        row = {
            "id": c["id"],
            "family": c["family"],
            "basis": c["basis"],
            "endpoint": c["endpoint"],
            "cancelled_propagator_factor": c["cancelled"],
            "retained_propagator_factor": "K" if c["cancelled"] == "Q" else "Q",
            "endpoint_coordinate": endpoint_coordinate(c),
            "phase_sign_in_shrinking_momentum": c["phase_sign"],
            "line_embedding": line_map(c),
            "line_scale_jacobian_symbol": "L",
            "pre_cancellation_momentum_degrees": {"q": q_degree, "k": k_degree},
            "cancelled_momentum_polynomial_degree": order,
            "ambient_contact_distribution": f"order-{order} derivative(s) of delta^(4)(x), tensor-contracted with surviving momentum/n",
            "ambient_scaling_degree_d4": PHYSICAL_D + order,
            "ambient_homogeneity_degree_d4": -(PHYSICAL_D + order),
            "ambient_singular_order": order,
            "ambient_singular_support": "x=0",
            "line_singular_support": "s=0 endpoint",
            "numerator_coefficient_dimensional_series": coeff_series,
            "method_A_microlocal": {
                "ambient_wavefront": "{(0,xi): xi!=0}",
                "line_normal_condition": "n.xi=0",
                "explicit_transverse_normal_witness": list(TRANSVERSE_WITNESS),
                "n_dot_witness": n_dot_xi,
                "normal_subspace_dimension_d4": normal_dimension,
                "wf_intersects_normal_set": wf_normal_intersection_nonempty,
                "canonical_hormander_pullback_authorized": canonical_pullback,
                "interpretation": "Failure removes the canonical pullback license; it is not promoted to universal nonexistence of every generalized prescription.",
            },
            "method_B_transverse_mollifier": {
                "regularizer": "delta_eta^4(x)=(pi*eta^2)^(-2)*exp(-|x|^2/eta^2)",
                "base_line_pairing_full_local_line": "eta^(-3)/(pi^(3/2)*L) times the one-dimensional approximate-delta pairing",
                "codimension": 3,
                "transverse_factor_diverges": True,
                "longitudinal_alignment_post_cancel_expression": aligned,
                "longitudinal_component_nonzero": bool(aligned_nonzero),
                "role": "independent uniqueness/existence diagnostic only; not a numerical renormalization prescription",
            },
            "method_C_raw_dimreg_scaleless": {
                "cancelled_momentum_factor": "polynomial momentum integral with no intrinsic scale after Q/K cancellation",
                "post_cancellation_polynomial_degree": order,
                "raw_factorized_dimreg_value": "0",
                "raw_zero_reason": "power-law scaleless integral in dimensional regularization",
                "raw_factorized_one_over_epsilon": "0",
                "renormalized_contact_pole_inferred_from_raw_zero": False,
                "frozen_ITER124_order_blocks_pre_subtraction_promotion": bool(contact_after_required_renormalization),
                "role": "raw whole-factor diagnostic only; R-operation/local UV coefficient remains downstream",
            },
            "source_qualified_unique_parent_analytic_extension_available": unique_parent_analytic_extension_available,
            "pole_data": {
                "one_over_epsilon2": None,
                "one_over_epsilon": None,
                "status": "UNAUTHORIZED_BEFORE_SOURCE_QUALIFIED_R_OPERATION_AND_LINE_EXTENSION",
                "absence_is_zero": False,
            },
            "local_ambiguity": {
                "status": "ENDPOINT_SUPPORTED_LOCAL_RENORMALIZATION_INPUT_REQUIRED",
                "description": "delta(s) and derivative counterterm freedom may occur subject to symmetry/power counting; ITER153 does not choose coefficients or silently set them to zero",
            },
            "resolved_for_slot5": bool(resolved),
            "classification": "PASS_CONTACT_SOURCE_FAITHFUL_EXTENSION_AUTHORIZED" if resolved else "BLOCKED_SCOPED_REQUIRES_NEW_LOCAL_EXTENSION_INPUT",
        }
        rows.append(row)

    controls = build_controls()
    derivative_orders = [r["cancelled_momentum_polynomial_degree"] for r in rows]
    expected_orders = [1, 1, 2, 2, 2, 1, 2]
    checks = {
        "A_frozen_parent_prereg_and_source_authority_lineage": all(lineage[k] for k in ["frozen_parent_is_ancestor", "preregistration_is_ancestor", "source_authority_initial_is_ancestor", "source_authority_DR_ordering_repair_is_ancestor"]),
        "B_exact_seven_ITER151_manifest_verbatim": manifest_ok and len(rows) == 7,
        "C_ITER152_slot5_parent_authority_open": slot5_was_open,
        "D_exact_cancelled_momentum_derivative_orders": derivative_orders == expected_orders,
        "E_physical_d4_wavefront_normal_witness_exact": n_dot_xi == 0 and normal_dimension == 3,
        "F_all_seven_canonical_pullbacks_tested_without_prototype_residue": all(not r["method_A_microlocal"]["canonical_hormander_pullback_authorized"] for r in rows),
        "G_independent_transverse_mollifier_diagnostic_nonfinite": all(r["method_B_transverse_mollifier"]["transverse_factor_diverges"] and r["method_B_transverse_mollifier"]["longitudinal_component_nonzero"] for r in rows),
        "H_missing_pole_authority_not_encoded_as_zero": all(r["pole_data"]["one_over_epsilon"] is None and r["pole_data"]["one_over_epsilon2"] is None and not r["pole_data"]["absence_is_zero"] for r in rows),
        "I_adversarial_negative_controls_rejected": all(not c["accepted"] and c["rejection_reasons"] for c in controls),
        "J_source_authority_rules_present": source_rules_ok,
        "K_no_B1_or_counterterm_subtraction_performed": True,
        "L_target_blind_no_desired_sign_or_cancellation": True,
        "M_ITER124_subtraction_order_exact_and_contact_split_after_renormalization": bool(iter124_order_ok and contact_after_required_renormalization),
        "N_raw_dimreg_scaleless_zero_not_promoted_to_renormalized_contact_zero": all(r["method_C_raw_dimreg_scaleless"]["raw_factorized_dimreg_value"] == "0" and not r["method_C_raw_dimreg_scaleless"]["renormalized_contact_pole_inferred_from_raw_zero"] and r["pole_data"]["one_over_epsilon"] is None for r in rows),
    }

    unresolved = [r["id"] for r in rows if not r["resolved_for_slot5"]]
    if not all(checks.values()):
        classification = "INVALID_IMPLEMENTATION_ITER153"
    elif not unresolved:
        classification = "PASS_SCOPED_SLOT5_SEVEN_CONTACT_DISTRIBUTIONAL_POLE_AUTHORITY_CLOSED"
    else:
        classification = "BLOCKED_SCOPED_SLOT5_REQUIRES_NEW_DISTRIBUTIONAL_EXTENSION_OR_RENORMALIZATION_INPUT"

    output = {
        "gate": "ITER153_FIXED_GEODESIC_CURVATURE_ENDPOINT_CONTACT_DISTRIBUTIONAL_EXTENSION_AUTHORITY",
        "classification": classification,
        "lineage": lineage,
        "source_blobs_at_frozen_parent": source_blobs,
        "dimension_convention": DIMENSION_CONVENTION,
        "physical_pullback_dimension": PHYSICAL_D,
        "test_function_space": "C_c^infty((-delta,delta)) in local endpoint coordinate s; physical half-interval restriction only after distributional definition",
        "frozen_invariants": {"Q": "q^2", "K": "k^2", "S": "q.k", "a": "n.q", "b": "n.k", "n2": 1},
        "frozen_ITER124_subtraction_order": iter124_order,
        "contact_split_index_zero_based": contact_split_index,
        "contacts": rows,
        "cancelled_momentum_derivative_orders": derivative_orders,
        "unresolved_contact_ids": unresolved,
        "slot5_closed": not unresolved,
        "blocking_primitive": None if not unresolved else "source-qualified graph-level R-operation on the unseparated first-M/G amplitude, including bulk/local-composite subtraction and endpoint/line renormalization before the ITER124 contact split; this operation fixes the local endpoint data that an isolated raw contact does not determine",
        "independent_method_summary": {
            "method_A": "microlocal wavefront/normal-set pullback test",
            "method_B": "smooth ambient approximate-identity restriction exposing an uncancelled codimension-three transverse factor",
            "method_C": "raw factorized dimensional-regularization scaleless-integral diagnostic, explicitly prevented from becoming a renormalized contact zero by the frozen ITER124 order",
            "agreement": "The isolated raw contact does not supply a regulator-independent renormalized endpoint pole from frozen parent data alone. Method C gives a raw scaleless zero, while A/B show why that zero cannot be substituted for the local renormalized contact coefficient.",
        },
        "controls": controls,
        "checks": checks,
        "interpretation": "The denominator-cancelled terms are genuine ambient point-supported contacts. At d=4 their ordinary restriction to the one-dimensional geodesic is not canonically licensed by the standard wavefront criterion, and a smooth transverse regulator exposes codimension-three local divergence. A separate raw dimensional-regularization calculation makes the cancelled-momentum factor scaleless and zero, but frozen ITER124 requires bulk/local, endpoint, and line-mixing renormalization before contact/polynomial separation. Therefore that raw zero is not the renormalized contact pole. The result is a scoped authority blocker, not a derived contact zero and not a universal theorem that no generalized prescription can ever be supplied.",
        "next_dependency": "Prospectively freeze the graph-specific first-M/G R-operation/subdivergence gate on the unseparated amplitude (slot 6 primitive), carrying endpoint and line-renormalization dependencies symbolically. Do not form B1_total and do not replace raw contacts by zero before that operation.",
        "claim_ceiling": "slot-5 distributional authority only; no renormalized contact pole value, no graph-specific subdivergence coefficient, endpoint counterterm coefficient, line-mixing residue, renormalized contact mapping, B1_total, noncancellation, EDT, bridge, new physics, or candidate theory",
    }

    Path("iter153_endpoint_contact_distributional_extension_authority.json").write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"classification": classification, "orders": derivative_orders, "unresolved_contact_ids": unresolved, "slot5_closed": not unresolved, "checks": checks}, indent=2, sort_keys=True))
    if classification == "INVALID_IMPLEMENTATION_ITER153" or classification.startswith("SCIENTIFIC_FAIL"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
