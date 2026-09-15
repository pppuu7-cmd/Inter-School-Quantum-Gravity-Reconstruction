#!/usr/bin/env python3
"""ITER126 authoritative prototype-pole checks.

The script verifies only affine-parameter prototype residues. It does not
compute curvature F/M/G weights or B1.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    eps = sp.symbols("eps")

    # E(eps)=Beta(-1+2eps,-1+2eps), rewritten by Gamma recurrence.
    endpoint = (
        sp.gamma(1 + 2 * eps) ** 2
        / sp.gamma(1 + 4 * eps)
        * (4 * eps * (4 * eps - 1) * (4 * eps - 2))
        / ((2 * eps) ** 2 * (2 * eps - 1) ** 2)
    )
    endpoint_residue = sp.simplify(sp.limit(eps * endpoint, eps, 0))
    assert endpoint_residue == 2

    # D(eps)=2/[(a+1)(a+2)], a=-2+2eps.
    diagonal = sp.simplify(1 / (eps * (-1 + 2 * eps)))
    diagonal_residue = sp.simplify(sp.limit(eps * diagonal, eps, 0))
    assert diagonal_residue == -1

    # Fixed-cut interior check at eps=0. The integrand is rational and finite
    # on [1/4,3/4], demonstrating that the prototype pole is boundary-local.
    t = sp.symbols("t", real=True)
    finite_cut = sp.integrate(1 / (t**2 * (1 - t) ** 2), (t, sp.Rational(1, 4), sp.Rational(3, 4)))
    assert finite_cut.is_finite is not False

    data = {
        "status": "PASS_SYMBOLIC_ASSERTIONS",
        "endpoint_product": {
            "definition": "Integral_0^1 [tau(1-tau)]^(-2+2eps) dtau",
            "analytic_continuation": str(endpoint),
            "residue_at_eps_0": str(endpoint_residue),
        },
        "line_line_coincidence": {
            "definition": "Integral_0^1 dtau Integral_0^1 dsigma |tau-sigma|^(-2+2eps)",
            "analytic_continuation": str(diagonal),
            "residue_at_eps_0": str(diagonal_residue),
        },
        "finite_interior_check": {
            "interval": "[1/4,3/4]",
            "eps": "0",
            "value": str(sp.simplify(finite_cut)),
        },
        "interpretation": (
            "Prototype affine-parameter residues only; actual curvature pole weights "
            "require F/M/G numerators, counterterms, subdivergence subtraction, "
            "and the ITER124/123 projection machinery."
        ),
        "claim_lock": "No B1 value, EDT fit, bridge, or discrepancy claim.",
    }

    out = Path("artifacts/iter126")
    out.mkdir(parents=True, exist_ok=True)
    (out / "prototype_residues.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    (out / "prototype_residues.md").write_text(
        "\n".join(
            [
                "# ITER126 defect-pole prototypes",
                "",
                f"- Endpoint-product residue: `{endpoint_residue}`.",
                f"- Line-line coincidence residue: `{diagonal_residue}`.",
                f"- Finite interior cut value at eps=0: `{sp.simplify(finite_cut)}`.",
                "",
                "These are affine-parameter prototype residues, not `B_1`.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
