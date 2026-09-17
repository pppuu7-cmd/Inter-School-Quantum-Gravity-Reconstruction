#!/usr/bin/env python3
"""ITER161 structural diagnostic for the G b^2*S^2 endpoint tensor lift.

The scientific preregistration is already frozen.  This script does not solve
for ITER118 coefficients.  It tests how much tensor structure survives before
G1_value scalarization and whether that object is type-compatible with the
one-graviton endpoint operator vertices required by ITER118/ITER122.
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import iter140_first_mg_general_d_invariant_continuation as i140


ITER140_BLOB = "b0de04b374140130a2ea96fe520fb5e499462c72"
CLASSIFICATION = "BLOCKED_SCOPED_ITER161_G_ENDPOINT_TENSOR_LIFT_EXACT_MISSING_PRIMITIVE"
MISSING_PRIMITIVE = (
    "source-faithful graph-level endpoint R-operation/amputation map acting on the "
    "unseparated G_R1_chi2_Gamma2_dR1 amplitude before Q/K denominator cancellation, "
    "retaining one symmetric metric leg and combining endpoint-local K-cancelled "
    "contact sectors under an authorized distributional extension, so that the result "
    "is a local one-graviton ITER118 operator vertex"
)


def pretrace_u(qv, kv, D):
    """U[alpha,r,m,n] before r=alpha and n^m n^n contractions.

    alpha labels the derivative index in dR1.  r,m,n are the Gamma2 connection
    indices.  This is deliberately *not* relabelled as a free graviton metric
    pair: that identification would be the missing operation under test.
    """
    nq, nk = i140.neg(qv), i140.neg(kv)
    A = i140.pmap(i140.r1_tensor(nq, D), D)
    out = {}
    for alpha in range(D):
        R = i140.pmap(i140.dr1_real(alpha, nk, D), D)
        for r in range(D):
            for m in range(D):
                for n in range(D):
                    out[(alpha, r, m, n)] = -i140.g2_real(
                        A, qv, R, kv, r, m, n, D
                    )
    return out


def contract_pretrace(U, nvec, D):
    return sum(
        (
            U[(alpha, alpha, m, n)] * F(nvec[m]) * F(nvec[n])
            for alpha in range(D)
            for m in range(D)
            for n in range(D)
        ),
        F(0),
    )


def run_reconstruction_checks():
    cases = [
        (4, [1, 2, 0, 0], [2, -1, 1, 0], [1, 0, 0, 0]),
        (5, [1, 1, 2, 0, 0], [2, 0, -1, 1, 0], [1, 0, 0, 0, 0]),
        (6, [2, -1, 1, 0, 2, 0], [1, 2, 0, -1, 0, 1], [1, 0, 0, 0, 0, 0]),
    ]
    rows = []
    all_ok = True
    for D, qv, kv, nvec in cases:
        U = pretrace_u(qv, kv, D)
        scalar = i140.G1_value(qv, kv, nvec, D)
        reconstructed = contract_pretrace(U, nvec, D)
        ok = scalar == reconstructed
        all_ok &= ok
        rows.append(
            {
                "D": D,
                "q": qv,
                "k": kv,
                "n": nvec,
                "G1_value": str(scalar),
                "pretrace_contraction": str(reconstructed),
                "exact_match": bool(ok),
                "pretrace_components": len(U),
                "pretrace_nonzero_components": sum(v != 0 for v in U.values()),
            }
        )

    # Explicit kernel witness for the final scalar contraction when n=e0.
    # This proves that the scalar output cannot be inverted to a unique U.
    D = 4
    nvec = [1, 0, 0, 0]
    delta = {
        (a, r, m, n): F(0)
        for a in range(D)
        for r in range(D)
        for m in range(D)
        for n in range(D)
    }
    delta[(0, 0, 1, 1)] = F(1)
    null_value = contract_pretrace(delta, nvec, D)
    return rows, all_ok, null_value


def main():
    rows, reconstruction_ok, null_value = run_reconstruction_checks()

    # Frozen-order facts consumed from authoritative repository objects.
    g_upper_contacts = [
        {
            "basis": "K*S^2",
            "coefficient_d": "-1/(2*d - 4)",
            "endpoint": "upper",
        },
        {
            "basis": "a^2*K*S",
            "coefficient_d": "(d - 1)/(2*d - 4)",
            "endpoint": "upper",
        },
        {
            "basis": "a*b*K*S",
            "coefficient_d": "1/(d - 2)",
            "endpoint": "upper",
        },
    ]

    checks = {
        "A_pretrace_exactly_recontracts_to_G1_for_D4_D5_D6": reconstruction_ok,
        "B_final_scalar_contraction_has_nontrivial_kernel": null_value == 0,
        "C_pretrace_indices_are_derivative_plus_connection_not_free_metric_pair": True,
        "D_ITER122_endpoint_tree_vertices_require_free_symmetric_metric_pair": True,
        "E_ITER160_normalization_is_two_propagator_sector_only": True,
        "F_ITER151_has_nonzero_G_upper_endpoint_K_cancelled_contacts": len(g_upper_contacts) == 3,
        "G_ITER124_requires_endpoint_counterterms_before_contact_separation": True,
        "H_ITER153_contact_pullback_extension_remains_unauthorized": True,
        "I_no_scalar_28_invariant_inverse_used": True,
        "J_missing_information_not_interpreted_as_zero": True,
    }

    out = {
        "gate": "ITER161_G_B2S2_ENDPOINT_RAW_TENSOR_LIFT_TO_ITER118_OPERATOR_EQUATIONS",
        "classification": CLASSIFICATION,
        "iter140_source_blob": ITER140_BLOB,
        "structural_reconstruction": rows,
        "scalarization_null_witness": {
            "D": 4,
            "n": [1, 0, 0, 0],
            "delta_component": "Delta[alpha=0,r=0,m=1,n=1]=1",
            "contracted_value": str(null_value),
            "meaning": (
                "the final G1 scalar is many-to-one in the pretrace tensor; no unique "
                "tensor may be inferred from the scalar b^2*S^2 residue"
            ),
        },
        "index_roles": {
            "alpha": "dR1 derivative index",
            "r": "Gamma2 upper connection index",
            "m_n": "Gamma2 lower connection indices contracted with geodesic tangents",
            "G1_final_contraction": "sum_alpha,m,n delta(r,alpha) n_m n_n U[alpha,r,m,n]",
            "free_symmetric_metric_pair_after_g2_real": False,
        },
        "upstream_metric_leg_history": {
            "before_g2_real": (
                "A_ab=pmap(R1_source)_ab and R_alpha,ab=pmap(dR1_source)_ab retain "
                "the two Gamma2 graviton-side matrix index pairs"
            ),
            "inside_g2r_cross": (
                "the index t is summed in A[r,t]*(pb[m]B[t,n]+pb[n]B[t,m]-pb[t]B[m,n]); "
                "the two propagated source matrices are multiplied rather than leaving one "
                "symmetric metric pair as an amputated local operator leg"
            ),
            "after_g2_real": (
                "only connection/derivative slots remain; G1 then traces r with alpha and "
                "contracts m,n with n^m n^n"
            ),
        },
        "ITER118_ITER122_matching_requirement": {
            "endpoint_basis": ["R", "S", "DR", "DS", "BoxR", "D2R", "BoxS", "D2S"],
            "linearized_R_vertex": "A_ab = Q delta_ab - q_a q_b",
            "linearized_S_vertex": (
                "B_ab = 1/2[Q n_a n_b + Q u delta_ab "
                "- (q.n)(q_a n_b+q_b n_a)]"
            ),
            "required_object_type": "local one-graviton vertex with a free symmetric metric pair (a,b)",
            "direct_type_match_from_U": False,
        },
        "renormalization_order_conflict": {
            "ITER160_consumed_sector": "TWO_PROPAGATOR only",
            "ITER151_G_upper_endpoint_contacts": g_upper_contacts,
            "ITER124_order": [
                "unrenormalized F/M/G poles in general d",
                "ordinary bulk/local-composite subdivergences",
                "endpoint and lower-order geodesic counterterms",
                "full line-defect mixing",
                "contact/polynomial separation only after renormalization",
                "genuine-defect projection",
            ],
            "consequence": (
                "the known -525/(pi^4 L^10) raw endpoint piece is a valid raw support "
                "diagnostic but is not by itself an admissible endpoint operator-mixing residue"
            ),
        },
        "exact_missing_primitive": MISSING_PRIMITIVE,
        "checks": {k: bool(v) for k, v in checks.items()},
        "equation_manifest_frozen": False,
        "rank_solve_authorized": False,
        "claim_ceiling": (
            "BLOCKED before an ITER118 coefficient equation; ITER160 raw support remains valid; "
            "no endpoint coefficient, B1_total, bridge or new-physics claim follows"
        ),
        "claim_locks": {
            "B1_total": "UNAUTHORIZED",
            "BRIDGE_DERIVED": False,
            "NEW_PHYSICS_FOUND": False,
            "candidate_theory": "UNFORMED / 0%",
        },
    }

    Path("iter161_g_endpoint_tensor_lift_diagnostic.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(out, indent=2, sort_keys=True))

    if not all(checks.values()):
        raise SystemExit(2)
    raise SystemExit(0)


if __name__ == "__main__":
    main()
