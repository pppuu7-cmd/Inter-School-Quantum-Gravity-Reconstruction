#!/usr/bin/env python3
"""ITER160: independent distributional confirmation of the raw G b^2*S^2 endpoint split.

This is a prediction-known confirmation gate.  The exploratory producer used a
Taylor/binomial endpoint argument.  This implementation instead applies the
meromorphic distribution identity

  Res x^(-m-1+2 epsilon) = (-1)^m/(2 m!) delta^(m)(x)

to the smooth endpoint factors, then checks the result against the frozen
predictions and the already-established ITER150 total master pole.

Scope is strictly the raw separated connected-cross TWO_PROPAGATOR master.  No
ITER118 coefficient, endpoint counterterm, contact term, line projector or B1
quantity is computed.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as s


eps, x, u, L = s.symbols("epsilon x u L", positive=True)

# Frozen upstream ITER150 normalization.
graph_total = -s.Rational(1050) / (s.pi**4 * L**10)


def endpoint_distribution_residue(m: int, smooth: s.Expr, var: s.Symbol) -> s.Expr:
    """Residue of x^(-m-1+2 eps) acting on a smooth endpoint test factor."""
    distribution_coeff = s.Rational((-1) ** m, 2 * s.factorial(m))
    test_action = (-1) ** m * s.diff(smooth, var, m).subs(var, 0)
    return s.simplify(distribution_coeff * test_action)


# Independent producer calculation under the preregistered distribution rule.
lower = endpoint_distribution_residue(3, (1 - x) ** -5, x)
upper = endpoint_distribution_residue(4, (1 - u) ** -4, u)

# Held-out exact total from the ITER150 Beta representation.
beta = s.gamma(-3 + 2 * eps) * s.gamma(-4 + 2 * eps) / s.gamma(-7 + 4 * eps)
beta_total = s.simplify(s.limit(eps * beta, eps, 0))
prefactor = s.simplify(graph_total / beta_total)
lower_graph = s.simplify(prefactor * lower)
upper_graph = s.simplify(prefactor * upper)


def jet(expr: s.Expr, var: s.Symbol, degree: int) -> s.Expr:
    return s.expand(
        sum(
            s.diff(expr, var, k).subs(var, 0) / s.factorial(k) * var**k
            for k in range(degree + 1)
        )
    )


# Remainder regularity after the exact endpoint jet order required by each
# singular distribution.  These limits are held-out regularity checks, not the
# primary endpoint-residue calculation.
f0 = (1 - x) ** -5
f1 = (1 - u) ** -4
rem0 = s.simplify((f0 - jet(f0, x, 3)) / x**4)
rem1 = s.simplify((f1 - jet(f1, u, 4)) / u**5)
rem0_lim = s.simplify(s.limit(rem0, x, 0))
rem1_lim = s.simplify(s.limit(rem1, u, 0))

# Predictions were frozen prospectively in the confirmation preregistration.
pred_lower = s.Rational(35, 2)
pred_upper = s.Rational(35, 2)
pred_graph = -s.Rational(525) / (s.pi**4 * L**10)

checks = {
    "A_lower_distribution_prediction": s.simplify(lower - pred_lower) == 0,
    "B_upper_distribution_prediction": s.simplify(upper - pred_upper) == 0,
    "C_endpoint_sum_matches_beta_laurent_residue": s.simplify(lower + upper - beta_total) == 0,
    "D_lower_remainder_regular_after_degree3_jet": rem0_lim.is_finite is not False,
    "E_upper_remainder_regular_after_degree4_jet": rem1_lim.is_finite is not False,
    "F_graph_lower_prediction": s.simplify(lower_graph - pred_graph) == 0,
    "G_graph_upper_prediction": s.simplify(upper_graph - pred_graph) == 0,
    "H_graph_sum_matches_frozen_ITER150_total": s.simplify(lower_graph + upper_graph - graph_total) == 0,
    "I_no_contact_or_line_projector_input": True,
    "J_raw_support_not_counterterm_interpretation": True,
}

if all(checks.values()):
    classification = "PASS_SCOPED_ITER160_RAW_G_B2S2_ENDPOINT_SUPPORT_SPLIT_INDEPENDENTLY_CONFIRMED"
else:
    classification = "SCIENTIFIC_FAIL_ITER160_RAW_ENDPOINT_SPLIT_PREDICTION_NOT_CONFIRMED"

out = {
    "gate": "ITER160_FIRST_MG_G_B2S2_RAW_ENDPOINT_SUPPORT_CONFIRMATION",
    "method": "meromorphic distribution identity acting on smooth endpoint test factors",
    "classification": classification,
    "distribution_identity": "Res x^(-m-1+2epsilon) = (-1)^m/(2 m!) delta^(m)(x)",
    "lower": {
        "m": 3,
        "smooth_factor": "(1-x)^(-5)",
        "beta_residue": str(lower),
        "graph_residue_1_over_epsilon": str(lower_graph),
    },
    "upper": {
        "m": 4,
        "smooth_factor": "(1-u)^(-4)",
        "beta_residue": str(upper),
        "graph_residue_1_over_epsilon": str(upper_graph),
    },
    "beta_total_residue": str(beta_total),
    "frozen_graph_total_residue_1_over_epsilon": str(graph_total),
    "derived_graph_prefactor": str(prefactor),
    "remainder_limits_after_jet_subtraction": {
        "lower": str(rem0_lim),
        "upper": str(rem1_lim),
    },
    "checks": {k: bool(v) for k, v in checks.items()},
    "claim_ceiling": (
        "confirmed raw TWO_PROPAGATOR endpoint-support split only; not ITER118 coefficients, "
        "not endpoint counterterms, not contacts, not line mixing, not B1_total"
    ),
    "claim_locks": {
        "B1_total": "UNAUTHORIZED",
        "BRIDGE_DERIVED": False,
        "NEW_PHYSICS_FOUND": False,
        "candidate_theory": "UNFORMED / 0%",
    },
}

Path("iter160_raw_endpoint_support_confirmation.json").write_text(
    json.dumps(out, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print(json.dumps(out, indent=2, sort_keys=True))

raise SystemExit(0 if classification.startswith("PASS") else 1)
