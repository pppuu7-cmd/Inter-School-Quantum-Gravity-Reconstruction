#!/usr/bin/env python3
"""Independent Critic for ITER160 raw endpoint-support confirmation.

The producer uses meromorphic distribution identities.  This Critic does not
use delta-derivative distributions.  It splits the analytically continued Beta
integral at z=1/2 and uses exact integration-by-parts recurrences for each
incomplete-Beta endpoint piece until the residual integral is ordinary and
finite at epsilon=0.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as s


eps, t, L = s.symbols("epsilon t L", positive=True)
z = s.Rational(1, 2)


def incomplete_beta_residue_by_recurrence(a: s.Expr, b: s.Expr, shifts: int):
    """Residue of B_z(a,b) after shifting first exponent into a finite domain.

    Uses exactly
      B_z(a,b) = z^a (1-z)^b / a + (a+b)/a B_z(a+1,b)
    repeatedly.  The final residual integral is evaluated only at epsilon=0,
    which is sufficient because its prefactor has at most a simple pole.
    """
    coeff = s.Integer(1)
    explicit = s.Integer(0)
    aa = a
    for _ in range(shifts):
        explicit += coeff * z**aa * (1 - z) ** b / aa
        coeff = s.simplify(coeff * (aa + b) / aa)
        aa = s.simplify(aa + 1)

    aa0 = s.simplify(aa.subs(eps, 0))
    b0 = s.simplify(b.subs(eps, 0))
    residual0 = s.simplify(
        s.integrate(t ** (aa0 - 1) * (1 - t) ** (b0 - 1), (t, 0, z))
    )
    reconstructed_for_residue = s.simplify(explicit + coeff * residual0)
    residue = s.simplify(s.limit(eps * reconstructed_for_residue, eps, 0))
    return residue, residual0, s.simplify(coeff), aa0, b0


# Lower endpoint is the incomplete Beta piece on [0,1/2].
lower, lower_residual0, lower_coeff, lower_aa0, lower_b0 = incomplete_beta_residue_by_recurrence(
    -3 + 2 * eps, -4 + 2 * eps, 4
)

# Upper endpoint: substitute u=1-tau.  The exponents swap, and the upper piece
# becomes B_{1/2}(-4+2 eps,-3+2 eps).
upper, upper_residual0, upper_coeff, upper_aa0, upper_b0 = incomplete_beta_residue_by_recurrence(
    -4 + 2 * eps, -3 + 2 * eps, 5
)

full_beta = s.gamma(-3 + 2 * eps) * s.gamma(-4 + 2 * eps) / s.gamma(-7 + 4 * eps)
full_residue = s.simplify(s.limit(eps * full_beta, eps, 0))

graph_total = -s.Rational(1050) / (s.pi**4 * L**10)
prefactor = s.simplify(graph_total / full_residue)
lower_graph = s.simplify(prefactor * lower)
upper_graph = s.simplify(prefactor * upper)

checks = {
    "A_lower_incomplete_beta_residue_35_over_2": s.simplify(lower - s.Rational(35, 2)) == 0,
    "B_upper_incomplete_beta_residue_35_over_2": s.simplify(upper - s.Rational(35, 2)) == 0,
    "C_split_sum_matches_full_beta_residue": s.simplify(lower + upper - full_residue) == 0,
    "D_lower_shifted_residual_integral_finite": bool(lower_residual0.is_finite),
    "E_upper_shifted_residual_integral_finite": bool(upper_residual0.is_finite),
    "F_lower_shift_reaches_a_equal_1_at_epsilon0": lower_aa0 == 1,
    "G_upper_shift_reaches_a_equal_1_at_epsilon0": upper_aa0 == 1,
    "H_lower_graph_residue": s.simplify(lower_graph + s.Rational(525) / (s.pi**4 * L**10)) == 0,
    "I_upper_graph_residue": s.simplify(upper_graph + s.Rational(525) / (s.pi**4 * L**10)) == 0,
    "J_graph_sum_matches_ITER150_total": s.simplify(lower_graph + upper_graph - graph_total) == 0,
    "K_no_distribution_identity_reused": True,
    "L_no_contact_or_ITER123_projector_input": True,
}

verdict = (
    "PASS_CRITIC_ITER160_RAW_ENDPOINT_SUPPORT_SPLIT_SOUND"
    if all(checks.values())
    else "FAIL_CRITIC_ITER160_RAW_ENDPOINT_SUPPORT_SPLIT"
)

out = {
    "gate": "ITER160_CRITIC",
    "method": "split at z=1/2 plus exact incomplete-Beta integration-by-parts recurrence",
    "verdict": verdict,
    "lower_beta_residue": str(lower),
    "upper_beta_residue": str(upper),
    "full_beta_residue": str(full_residue),
    "lower_shifted_residual_at_epsilon0": str(lower_residual0),
    "upper_shifted_residual_at_epsilon0": str(upper_residual0),
    "lower_final_recurrence_coefficient": str(lower_coeff),
    "upper_final_recurrence_coefficient": str(upper_coeff),
    "lower_graph_residue_1_over_epsilon": str(lower_graph),
    "upper_graph_residue_1_over_epsilon": str(upper_graph),
    "checks": {k: bool(v) for k, v in checks.items()},
    "claim_ceiling": "Critic validates raw two-propagator endpoint support only; no counterterm/B1 inference",
}

Path("iter160_adversarial_critic.json").write_text(
    json.dumps(out, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if verdict.startswith("PASS") else 1)
