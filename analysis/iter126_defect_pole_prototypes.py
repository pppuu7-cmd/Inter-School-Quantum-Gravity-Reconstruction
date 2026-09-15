#!/usr/bin/env python3
"""ITER126: analytic-continuation checks for line endpoint/coincidence pole prototypes.

The residues are prototype geometric/parameter residues only. They are not
curvature B1 coefficients.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    eps = sp.symbols("eps")

    # Endpoint-product prototype:
    # E = Beta(-1+2eps, -1+2eps).
    # Use Gamma recurrence to rewrite in terms of Gamma near +1, which makes
    # the pole residue transparent and robust for symbolic limiting.
    endpoint = (
        sp.gamma(1 + 2 * eps) ** 2
        / sp.gamma(1 + 4 * eps)
        * (4 * eps * (4 * eps - 1) * (4 * eps - 2))
        / ((2 * eps) ** 2 * (2 * eps - 1) ** 2)
    )
    endpoint_residue = sp.simplify(sp.limit(eps * endpoint, eps, 0))
    assert endpoint_residue == 2

    # Direct analytic form of the line-line coincidence prototype:
    # D = 2/[(a+1)(a+2)], a=-2+2eps.
    diagonal = sp.simplify(1 / (eps * (-1 + 2 * eps)))
    diagonal_residue = sp.simplify(sp.limit(eps * diagonal, eps, 0))
    assert diagonal_residue == -1

    # A finite-interior sanity check: cutting away endpoints/diagonal removes
    # the eps=0 singularity for the prototype weights.
    delta = sp.symbols("delta", positive=True)
    endpoint_cut = sp.integrate(
        (sp.Symbol("t") * (1 - sp.Symbol("t"))) ** (-2 + 2 * eps),
        (sp.Symbol("t"), delta, 1 - delta),
    )
    # Do not force a complicated simplification; substituting eps=0 at fixed
    # delta is legitimate and must not contain 1/eps.
    endpoint_cut_at_zero = sp.simplify(endpoint_cut.subs(eps, 0))
    assert not endpoint_cut_at_zero.has(sp.zoo)

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
        "interpretation": (
            "Prototype affine-parameter residues only; actual curvature pole "
            "weights require F/M/G numerators, line kernels, counterterms, "
            "subdivergence subtraction, and the ITER124 projector."
        ),
        "claim_lock": "No B1 value, EDT fit, bridge, or physics discrepancy claim.",
    }

    out = Path("artifacts/iter126")
    out.mkdir(parents=True, exist_ok=True)
    (out / "prototype_residues.json").write_text(
        json.dumps(data, indent=2) + "\n", encoding="utf-8"
    )
    lines = [
        "# ITER126 defect-pole prototypes",
        "",
        f"- Endpoint-product residue: `{endpoint_residue}`.",
        f"- Line-line coincidence residue: `{diagonal_residue}`.",
        "",
        "These are affine-parameter prototype residues, not `B_1`.",
        "",
    ]
    (out / "prototype_residues.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
