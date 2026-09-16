#!/usr/bin/env python3
"""Independent adversarial critic for ITER153.

The critic rederives contact derivative orders and checks the blocker logic without
importing the ITER153 implementation module.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

RESULT = Path("iter153_endpoint_contact_distributional_extension_authority.json")
SOURCE = Path("analysis/iter153_endpoint_contact_distributional_extension_authority.py")
PREREG = Path("prereg/ITER153_FIXED_GEODESIC_CURVATURE_ENDPOINT_CONTACT_DISTRIBUTIONAL_EXTENSION_AUTHORITY_2026-09-17.md")

EXPECTED = [
    (1, "b^2*Q*S", "Q", "lower", -1, 1),
    (2, "a^2*K*S", "K", "upper", +1, 1),
    (3, "a^2*K^2", "K", "upper", +1, 2),
    (4, "a*b*K*S", "K", "upper", +1, 2),
    (5, "K*S^2", "K", "upper", -1, 2),
    (6, "a^2*K*S", "K", "upper", -1, 1),
    (7, "a*b*K*S", "K", "upper", -1, 2),
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
    if cancelled == "Q":
        return q - 2
    return k - 2


def main() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    src = SOURCE.read_text(encoding="utf-8")
    prereg = PREREG.read_text(encoding="utf-8")
    rows = data.get("contacts", [])

    expected_ids = [x[0] for x in EXPECTED]
    got_ids = [r.get("id") for r in rows]
    manifest_exact = got_ids == expected_ids and len(rows) == 7

    order_checks = []
    metadata_checks = []
    for exp, row in zip(EXPECTED, rows):
        cid, basis, cancelled, endpoint, phase_sign, order = exp
        derived = independent_order(basis, cancelled)
        order_checks.append(
            cid == row.get("id")
            and basis == row.get("basis")
            and cancelled == row.get("cancelled_propagator_factor")
            and derived == order == row.get("cancelled_momentum_polynomial_degree")
        )
        expected_map = "F(s)=+L*s*n" if phase_sign < 0 else "F(s)=-L*s*n"
        method_a = row.get("method_A_microlocal", {})
        method_b = row.get("method_B_transverse_mollifier", {})
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

    poles_unauthorized_not_zero = all(
        r.get("pole_data", {}).get("one_over_epsilon") is None
        and r.get("pole_data", {}).get("one_over_epsilon2") is None
        and r.get("pole_data", {}).get("absence_is_zero") is False
        for r in rows
    )
    all_blocked = all(
        r.get("classification") == "BLOCKED_SCOPED_REQUIRES_NEW_LOCAL_EXTENSION_INPUT"
        and r.get("resolved_for_slot5") is False
        for r in rows
    )
    controls_ok = all(
        c.get("accepted") is False and bool(c.get("rejection_reasons"))
        for c in data.get("controls", [])
    ) and len(data.get("controls", [])) == 7

    # Adversarial point: Hörmander failure is only used to remove the canonical
    # pullback license; the result must not overclaim universal impossibility.
    interpretation = data.get("interpretation", "")
    no_overclaim = (
        "not a universal theorem" in interpretation
        and "not a derived zero" in interpretation
    )

    # Prototype values may occur only as forbidden-control text, never as pole output.
    no_prototype_promotion = poles_unauthorized_not_zero and "prototype_residue" in src

    # Preregistration must have frozen the same decision boundary before implementation.
    prereg_logic = all(
        phrase in prereg
        for phrase in [
            "BLOCKED_SCOPED_SLOT5_REQUIRES_NEW_DISTRIBUTIONAL_EXTENSION_OR_RENORMALIZATION_INPUT",
            "Failure of that sufficient criterion does not by itself authorize assigning a value",
            "Absence of authority is `BLOCKED`, not zero",
        ]
    )

    checks = {
        "A_exact_seven_contact_ids_and_order": bool(manifest_exact),
        "B_independent_cancelled_momentum_orders_match": all(order_checks) and [independent_order(x[1], x[2]) for x in EXPECTED] == [1, 1, 2, 2, 2, 1, 2],
        "C_endpoint_phase_line_map_and_L_scale_match_frozen_geometry": all(metadata_checks),
        "D_wavefront_blocker_not_overclaimed_as_universal_nonexistence": no_overclaim,
        "E_missing_poles_are_null_not_zero": poles_unauthorized_not_zero,
        "F_all_seven_scoped_blocked_consistently": all_blocked,
        "G_controls_rejected": controls_ok,
        "H_ITER126_prototype_residues_not_promoted": no_prototype_promotion,
        "I_preregistered_decision_boundary_preserved": prereg_logic,
        "J_slot5_not_falsely_closed": data.get("slot5_closed") is False and data.get("unresolved_contact_ids") == expected_ids,
    }

    classification = (
        "PASS_CRITIC_ITER153_SCOPED_BLOCKER_LOGIC_SOUND"
        if all(checks.values())
        else "FAIL_CRITIC_ITER153_REQUIRES_REPAIR"
    )
    out = {
        "critic": "ITER153_ADVERSARIAL_DISTRIBUTIONAL_CRITIC",
        "classification": classification,
        "independent_orders": [independent_order(x[1], x[2]) for x in EXPECTED],
        "checks": checks,
        "critic_conclusion": (
            "The terminal blocker is appropriately narrow: the seven frozen contacts are ambient delta-derivative distributions after denominator cancellation, the ordinary line pullback lacks canonical microlocal authorization, and the independent transverse regulator diagnostic exposes an extra local renormalization datum. The result correctly leaves contact pole coefficients undefined rather than zero."
            if all(checks.values())
            else "At least one preregistered blocker/control/provenance check failed; do not promote ITER153."
        ),
    }
    Path("iter153_adversarial_critic.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
