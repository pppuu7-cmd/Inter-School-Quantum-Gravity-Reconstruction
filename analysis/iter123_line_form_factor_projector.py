#!/usr/bin/env python3
"""ITER123: exact straight-line form factor and two-point defect projector.

No loop amplitude is evaluated. The script only verifies the kinematic
extraction formulas once a UV pole has already been reduced to the genuine
defect basis.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    z, u = sp.symbols("z u", real=True)
    rho0, rho1 = sp.symbols("rho0 rho1")

    # Centered line form factor normalized by the segment length l:
    # Phi(z)=F(z)/l=2 sin(z/2)/z, with Phi(0)=1 by continuity.
    phi = 2 * sp.sin(z / 2) / z
    phi0 = sp.limit(phi, z, 0)
    assert sp.simplify(phi0 - 1) == 0

    # d=4 trace and traceless angular shapes from ITER122.
    f0 = 1 - u
    f1 = (1 - u) * (u - sp.Rational(1, 4))
    amp = sp.expand(rho0 * f0 + rho1 * f1)

    u0 = sp.Rational(0)
    u1 = sp.Rational(1, 2)
    matrix = sp.Matrix(
        [
            [sp.simplify(f0.subs(u, u0)), sp.simplify(f1.subs(u, u0))],
            [sp.simplify(f0.subs(u, u1)), sp.simplify(f1.subs(u, u1))],
        ]
    )
    det = sp.simplify(matrix.det())
    assert det == sp.Rational(1, 4)

    a0, a1 = sp.symbols("a0 a1")
    solution = sp.simplify(matrix.inv() * sp.Matrix([a0, a1]))
    rho0_rec = sp.simplify(solution[0])
    rho1_rec = sp.simplify(solution[1])

    assert sp.simplify(rho0_rec - (a0 / 2 + a1)) == 0
    assert sp.simplify(rho1_rec - (-2 * a0 + 4 * a1)) == 0

    # Direct substitution check.
    direct0 = sp.simplify(amp.subs(u, u0))
    direct1 = sp.simplify(amp.subs(u, u1))
    assert sp.simplify(rho0_rec.subs({a0: direct0, a1: direct1}) - rho0) == 0
    assert sp.simplify(rho1_rec.subs({a0: direct0, a1: direct1}) - rho1) == 0

    # Exceptional Box_perp kinematics.
    assert sp.simplify(f0.subs(u, 1)) == 0
    assert sp.simplify(f1.subs(u, 1)) == 0

    data = {
        "status": "PASS_SYMBOLIC_ASSERTIONS",
        "line_form_factor": {
            "centered_F_over_l": str(phi),
            "z_to_zero_limit": str(phi0),
            "endpoint_anchored_relation": "F_[0,l] = exp(i z/2) F_centered",
            "zeros": "z=2*pi*k, k nonzero integer",
        },
        "d4_shapes": {
            "f0_trace": str(f0),
            "f1_traceless": str(f1),
        },
        "kinematic_points": {
            "u0": str(u0),
            "u1": str(u1),
            "matrix": str(matrix),
            "determinant": str(det),
        },
        "reconstruction": {
            "rho0": str(rho0_rec),
            "rho1": str(rho1_rec),
            "meaning": "a0,a1 are amplitudes after dividing known Q^2 and centered line form factor",
        },
        "claim_lock": "Projector only; no loop pole, B1, EDT fit, or bridge claim.",
    }

    out = Path("artifacts/iter123")
    out.mkdir(parents=True, exist_ok=True)
    (out / "projector.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# ITER123 line form-factor / kinematic projector",
        "",
        f"- Centered normalized form factor: `Phi(z)={phi}`, `Phi(0)={phi0}`.",
        "- Endpoint-anchored and centered segments differ only by `exp(i z/2)`.",
        f"- d=4 shape matrix at `u=0,1/2`: `{matrix}`.",
        f"- Determinant: `{det}`.",
        f"- Reconstruction: `rho0={rho0_rec}`, `rho1={rho1_rec}`.",
        "- `u=1` is exceptional because `Box_perp` kills both shapes.",
        "- Avoid nonzero zeros `z=2*pi*k` of the centered line factor.",
        "",
        "Claim lock: no UV pole amplitude is evaluated.",
        "",
    ]
    (out / "projector.md").write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
