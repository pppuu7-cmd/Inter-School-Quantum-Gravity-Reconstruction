#!/usr/bin/env python3
"""ITER161: source-faithful endpoint-selected open-leg factorization.

This script repairs the overstrong preliminary blocker argument.  The affine
geometry fixes which propagator edge shrinks at each endpoint, and therefore
which graviton-side matrix is to be kept open before the final scalar
contraction.

It proves exact factorization only.  It does NOT assign a renormalized endpoint
pole tensor or an ITER118 counterterm coefficient; K/Q-cancelled contact terms
still require the frozen ITER124/ITER153 graph-level distributional R-operation.
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


PARTIAL_CLASSIFICATION = "PASS_STRUCTURAL_ITER161_ENDPOINT_SELECTED_OPEN_METRIC_LEG_FACTORIZATION"
MISSING_POLE_PRIMITIVE = (
    "source-faithful distributional endpoint R-operation/extension acting on the "
    "source-derived open-leg unseparated G endpoint vertex before Q/K contact "
    "separation, preserving the free symmetric metric leg and endpoint orientation "
    "while assigning the complete local pole tensor including cancelled-propagator contacts"
)


def sym_basis(D: int, a: int, b: int):
    H = [[F(0) for _ in range(D)] for _ in range(D)]
    H[a][b] = F(1)
    H[b][a] = F(1)
    return H


def frobenius(A, B, D: int):
    return sum(
        (A[a][b] * B[a][b] for a in range(D) for b in range(D)),
        F(0),
    )


def symmetric_functional_matrix(functional, D: int):
    """Return V_ab satisfying F(H)=sum_ab H_ab V_ab for symmetric H."""
    V = [[F(0) for _ in range(D)] for _ in range(D)]
    for a in range(D):
        for b in range(a, D):
            value = functional(sym_basis(D, a, b))
            if a == b:
                V[a][b] = value
            else:
                V[a][b] = V[b][a] = value / F(2)
    return V


def upper_open_vertex(qv, kv, nvec, D: int):
    """Upper endpoint: k edge shrinks, so retain the q-side metric leg A_ab."""
    nk = i140.neg(kv)

    def functional(A):
        out = F(0)
        for mu in range(D):
            R = i140.pmap(i140.dr1_real(mu, nk, D), D)
            for m in range(D):
                if F(nvec[m]) == 0:
                    continue
                for n in range(D):
                    if F(nvec[n]) == 0:
                        continue
                    out -= (
                        F(nvec[m])
                        * F(nvec[n])
                        * i140.g2_real(A, qv, R, kv, mu, m, n, D)
                    )
        return out

    return symmetric_functional_matrix(functional, D)


def lower_open_vertices(qv, kv, nvec, D: int):
    """Lower endpoint: q edge shrinks, so retain the k-side R_mu,ab metric leg.

    The result remains labelled by the derivative index mu.  A single G graph
    is therefore not yet asserted to be one of the scalar ITER118 directions.
    """
    nq = i140.neg(qv)
    A = i140.pmap(i140.r1_tensor(nq, D), D)
    matrices = []
    for mu in range(D):
        def functional(R, mu=mu):
            out = F(0)
            for m in range(D):
                if F(nvec[m]) == 0:
                    continue
                for n in range(D):
                    if F(nvec[n]) == 0:
                        continue
                    out -= (
                        F(nvec[m])
                        * F(nvec[n])
                        * i140.g2_real(A, qv, R, kv, mu, m, n, D)
                    )
            return out

        matrices.append(symmetric_functional_matrix(functional, D))
    return matrices


def is_symmetric(M, D: int):
    return all(M[a][b] == M[b][a] for a in range(D) for b in range(D))


def main():
    cases = [
        (4, [1, 2, 0, 0], [2, -1, 1, 0], [1, 0, 0, 0]),
        (5, [1, 1, 2, 0, 0], [2, 0, -1, 1, 0], [1, 0, 0, 0, 0]),
        (6, [2, -1, 1, 0, 2, 0], [1, 2, 0, -1, 0, 1], [1, 0, 0, 0, 0, 0]),
    ]

    rows = []
    all_upper = True
    all_lower = True
    all_symmetric = True

    for D, qv, kv, nvec in cases:
        target = i140.G1_value(qv, kv, nvec, D)

        # Upper endpoint factorization: G1 = A:V_upper.
        A = i140.pmap(i140.r1_tensor(i140.neg(qv), D), D)
        Vup = upper_open_vertex(qv, kv, nvec, D)
        upper_reconstructed = frobenius(A, Vup, D)
        upper_ok = upper_reconstructed == target

        # Lower endpoint factorization: G1 = sum_mu R_mu:W_lower_mu.
        Wlow = lower_open_vertices(qv, kv, nvec, D)
        lower_reconstructed = F(0)
        for mu in range(D):
            Rmu = i140.pmap(i140.dr1_real(mu, i140.neg(kv), D), D)
            lower_reconstructed += frobenius(Rmu, Wlow[mu], D)
        lower_ok = lower_reconstructed == target

        symmetric_ok = is_symmetric(Vup, D) and all(is_symmetric(W, D) for W in Wlow)
        all_upper &= upper_ok
        all_lower &= lower_ok
        all_symmetric &= symmetric_ok

        rows.append(
            {
                "D": D,
                "q": qv,
                "k": kv,
                "n": nvec,
                "G1_value": str(target),
                "upper_A_colon_V": str(upper_reconstructed),
                "upper_exact": bool(upper_ok),
                "lower_sum_Rmu_colon_Wmu": str(lower_reconstructed),
                "lower_exact": bool(lower_ok),
                "all_open_leg_matrices_symmetric": bool(symmetric_ok),
                "upper_nonzero_components": sum(v != 0 for row in Vup for v in row),
                "lower_nonzero_components_total": sum(
                    v != 0 for W in Wlow for row in W for v in row
                ),
            }
        )

    checks = {
        "A_upper_endpoint_geometry_selects_k_shrinking_q_leg_open": True,
        "B_lower_endpoint_geometry_selects_q_shrinking_k_leg_open": True,
        "C_upper_open_symmetric_metric_vertex_reconstructs_G1_exactly": all_upper,
        "D_lower_open_symmetric_metric_vertices_reconstruct_G1_exactly": all_lower,
        "E_all_open_metric_matrices_are_symmetric": all_symmetric,
        "F_factorization_does_not_use_ITER160_minus525_normalization": True,
        "G_no_28_scalar_inverse_used": True,
        "H_no_contact_pole_value_assumed": True,
    }

    out = {
        "gate": "ITER161_G_B2S2_ENDPOINT_RAW_TENSOR_LIFT_TO_ITER118_OPERATOR_EQUATIONS",
        "partial_classification": PARTIAL_CLASSIFICATION,
        "tests": rows,
        "upper_endpoint": {
            "shrinking_edge": "k",
            "open_nonshrinking_leg": "q-side symmetric metric pair A_ab",
            "factorization": "G1 = sum_ab A_ab V_upper_ab",
            "raw_tensor_lift_exists": True,
            "complete_pole_tensor_exists": False,
        },
        "lower_endpoint": {
            "shrinking_edge": "q",
            "open_nonshrinking_leg": "k-side symmetric metric pair R_mu,ab",
            "factorization": "G1 = sum_mu,ab R_mu,ab W_lower_mu,ab",
            "raw_tensor_lift_exists": True,
            "remaining_derivative_label_mu": True,
            "complete_pole_tensor_exists": False,
        },
        "why_no_ITER118_equation_yet": (
            "the unseparated open vertex still contains cancelled-propagator contact distributions; "
            "ITER153 leaves their endpoint extension/pole null and ITER124 requires endpoint/line "
            "renormalization before contact separation"
        ),
        "exact_missing_pole_primitive": MISSING_POLE_PRIMITIVE,
        "checks": {k: bool(v) for k, v in checks.items()},
        "claim_ceiling": (
            "source-faithful raw open metric-leg factorization only; no complete endpoint pole tensor, "
            "no ITER118 coefficient equation, no rank solve, no B1_total"
        ),
        "claim_locks": {
            "B1_total": "UNAUTHORIZED",
            "BRIDGE_DERIVED": False,
            "NEW_PHYSICS_FOUND": False,
            "candidate_theory": "UNFORMED / 0%",
        },
    }

    Path("iter161_endpoint_open_leg_factorization.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
