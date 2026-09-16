#!/usr/bin/env python3
"""Independent adversarial critic for ITER153.

Rederives contact orders and independently checks that raw scaleless DR zeros are
not promoted through the frozen ITER124 R-operation/contact-split ordering.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

RESULT = Path("iter153_endpoint_contact_distributional_extension_authority.json")
SOURCE = Path("analysis/iter153_endpoint_contact_distributional_extension_authority.py")
PREREG = Path("prereg/ITER153_FIXED_GEODESIC_CURVATURE_ENDPOINT_CONTACT_DISTRIBUTIONAL_EXTENSION_AUTHORITY_2026-09-17.md")
ITER124 = Path("analysis/iter124_projected_rg_pole_manifest.json")

EXPECTED = [
    (1, "b^2*Q*S", "Q", "lower", -1, 1),
    (2, "a^2*K*S", "K", "upper", +1, 1),
    (3, "a^2*K^2", "K", "upper", +1, 2),
    (4, "a*b*K*S", "K", "upper", +1, 2),
    (5, "K*S^2", "K", "upper", -1, 2),
    (6, "a^2*K*S", "K", "upper", -1, 1),
    (7, "a*b*K*S", "K", "upper", -1, 2),
]
EXPECTED_ORDER = [
    "generate unrenormalized F/M/G poles in general d",
    "subtract bulk ghost and local-composite subdivergences",
    "add endpoint and lower-order geodesic counterterms",
    "renormalize full line-defect mixing matrix including simple and higher poles",
    "separate contact/polynomial structures only after renormalization",
    "project genuine-defect poles at u=0 and u=1/2 in general d",
]


def token_exp(label: str, tok: str) -> int:
    m = re.search(rf"(?:^|\*){re.escape(tok)}(?:\^(\d+))?(?:\*|$)", label)
    return int(m.group(1) or 1) if m else 0


def independent_order(label: str, cancelled: str) -> int:
    q = k = 0
    if label.startswith("a^2*"):
        q += 2
    elif label.startswith("b^2*"):
        k += 2
    elif label.startswith("a*b*"):
        q += 1
        k += 1
    q += 2 * token_exp(label, "Q") + token_exp(label, "S")
    k += 2 * token_exp(label, "K") + token_exp(label, "S")
    return q - 2 if cancelled == "Q" else k - 2


def main() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    src = SOURCE.read_text(encoding="utf-8")
    prereg = PREREG.read_text(encoding="utf-8")
    iter124 = json.loads(ITER124.read_text(encoding="utf-8"))
    rows = data.get("contacts", [])

    expected_ids = [x[0] for x in EXPECTED]
    manifest_exact = [r.get("id") for r in rows] == expected_ids and len(rows) == 7
    order_checks = []
    metadata_checks = []
    method_c_checks = []
    for exp, row in zip(EXPECTED, rows):
        cid, basis, cancelled, endpoint, phase_sign, order = exp
        derived = independent_order(basis, cancelled)
        order_checks.append(cid == row.get("id") and basis == row.get("basis") and cancelled == row.get("cancelled_propagator_factor") and derived == order == row.get("cancelled_momentum_polynomial_degree"))
        method_a = row.get("method_A_microlocal", {})
        method_b = row.get("method_B_transverse_mollifier", {})
        expected_map = "F(s)=+L*s*n" if phase_sign < 0 else "F(s)=-L*s*n"
        metadata_checks.append(
            endpoint == row.get("endpoint")
            and phase_sign == row.get("phase_sign_in_shrinking_momentum")
            and row.get("line_embedding") == expected_map
            and row.get("line_scale_jacobian_symbol") == "L"
            and method_a.get("n_dot_witness") == 0
            and method_a.get("normal_subspace_dimension_d4") == 3
            and method_a.get("wf_intersects_normal_set") is True
            and method_a.get("canonical_hormander_pullback_authorized") is False
            and method_b.get("codimension") == 3
            and method_b.get("transverse_factor_diverges") is True
            and method_b.get("longitudinal_component_nonzero") is True
        )
        method_c = row.get("method_C_raw_dimreg_scaleless", {})
        method_c_checks.append(
            method_c.get("raw_factorized_dimreg_value") == "0"
            and method_c.get("raw_factorized_one_over_epsilon") == "0"
            and method_c.get("renormalized_contact_pole_inferred_from_raw_zero") is False
            and method_c.get("frozen_ITER124_order_blocks_pre_subtraction_promotion") is True
            and row.get("pole_data", {}).get("one_over_epsilon") is None
            and row.get("pole_data", {}).get("absence_is_zero") is False
        )

    actual_order = iter124.get("subtraction_order", [])
    iter124_exact = actual_order == EXPECTED_ORDER
    contact_i = actual_order.index(EXPECTED_ORDER[4]) if iter124_exact else -1
    ordering_sound = iter124_exact and all(i < contact_i for i in [1, 2, 3])
    poles_unauthorized_not_zero = all(
        r.get("pole_data", {}).get("one_over_epsilon") is None
        and r.get("pole_data", {}).get("one_over_epsilon2") is None
        and r.get("pole_data", {}).get("absence_is_zero") is False
        for r in rows
    )
    all_blocked = all(r.get("classification") == "BLOCKED_SCOPED_REQUIRES_NEW_LOCAL_EXTENSION_INPUT" and r.get("resolved_for_slot5") is False for r in rows)
    controls_ok = len(data.get("controls", [])) == 7 and all(c.get("accepted") is False and bool(c.get("rejection_reasons")) for c in data.get("controls", []))
    interpretation = data.get("interpretation", "")
    no_overclaim = "not a universal theorem" in interpretation and "not the renormalized contact pole" in interpretation
    no_prototype_promotion = poles_unauthorized_not_zero and "prototype_residue" in src
    prereg_logic = all(phrase in prereg for phrase in [
        "BLOCKED_SCOPED_SLOT5_REQUIRES_NEW_DISTRIBUTIONAL_EXTENSION_OR_RENORMALIZATION_INPUT",
        "Failure of that sufficient criterion does not by itself authorize assigning a value",
        "Absence of authority is `BLOCKED`, not zero",
    ])
    blocker_specific = "graph-level R-operation" in str(data.get("blocking_primitive", "")) and "unseparated first-M/G amplitude" in str(data.get("blocking_primitive", ""))

    checks = {
        "A_exact_seven_contact_ids_and_order": bool(manifest_exact),
        "B_independent_cancelled_momentum_orders_match": all(order_checks) and [independent_order(x[1], x[2]) for x in EXPECTED] == [1, 1, 2, 2, 2, 1, 2],
        "C_endpoint_phase_line_map_and_L_scale_match_frozen_geometry": all(metadata_checks),
        "D_wavefront_blocker_not_overclaimed_as_universal_nonexistence": no_overclaim,
        "E_missing_renormalized_poles_are_null_not_zero": poles_unauthorized_not_zero,
        "F_all_seven_scoped_blocked_consistently": all_blocked,
        "G_controls_rejected": controls_ok,
        "H_ITER126_prototype_residues_not_promoted": no_prototype_promotion,
        "I_preregistered_decision_boundary_preserved": prereg_logic,
        "J_slot5_not_falsely_closed": data.get("slot5_closed") is False and data.get("unresolved_contact_ids") == expected_ids,
        "K_frozen_ITER124_order_independently_verified": ordering_sound and data.get("frozen_ITER124_subtraction_order") == EXPECTED_ORDER,
        "L_raw_scaleless_DR_zero_not_promoted": all(method_c_checks),
        "M_new_blocking_primitive_is_graph_R_operation_not_generic_audit": blocker_specific,
    }

    classification = "PASS_CRITIC_ITER153_SCOPED_BLOCKER_LOGIC_SOUND" if all(checks.values()) else "FAIL_CRITIC_ITER153_REQUIRES_REPAIR"
    out = {
        "critic": "ITER153_ADVERSARIAL_DISTRIBUTIONAL_CRITIC",
        "classification": classification,
        "independent_orders": [independent_order(x[1], x[2]) for x in EXPECTED],
        "frozen_ITER124_order_verified": ordering_sound,
        "checks": checks,
        "critic_conclusion": (
            "The blocker is now localized beyond a generic authority absence. The seven cancelled sectors have raw factorized scaleless DR zeros, but ITER124 independently requires bulk/local, endpoint, and line-mixing renormalization before contact separation. Together with the failed canonical line pullback and transverse-regulator divergence, this prevents promoting the raw zeros to renormalized contact poles. The minimal successor primitive is the graph-level R-operation on the unseparated first-M/G amplitude."
            if all(checks.values())
            else "At least one preregistered blocker/control/order/provenance check failed; do not promote ITER153."
        ),
    }
    Path("iter153_adversarial_critic.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
