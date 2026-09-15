#!/usr/bin/env python3
"""ITER122 authoritative symbolic general-d curvature / defect kernels.

This script derives tree/projector kernels only. It deliberately does not
compute one-loop pole residues, B1, or any lattice comparison.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    d, Q, u = sp.symbols("d Q u", positive=True)

    # Frozen invariants: Q=q^2 and u=(q.n)^2/Q with n^2=1.
    # Linearized scalar-curvature vertex A_mn = Q delta_mn-q_m q_n.
    tr_a = (d - 1) * Q
    aa = (d - 1) * Q**2

    # Linearized tangent-Ricci vertex:
    # B_mn = 1/2[Q n_m n_n + Q u delta_mn
    #             -(q.n)(q_m n_n+q_n n_m)].
    # It obeys q_m q_n B_mn=0, so A:B=Q tr(B).
    tr_b = sp.Rational(1, 2) * Q * (1 + (d - 2) * u)
    ab = sp.simplify(Q * tr_b)

    # For symmetric tensors X,Y the de-Donder numerator gives
    # X:P:Y = X:Y-tr(X)tr(Y)/(d-2); the propagator adds 1/Q.
    k_rr = sp.factor((aa - tr_a**2 / (d - 2)) / Q)
    k_rrn = sp.factor((ab - tr_a * tr_b / (d - 2)) / Q)
    k_rtf = sp.factor(k_rrn - k_rr / d)

    expected_rr = -(d - 1) * Q / (d - 2)
    expected_rrn = -Q / (2 * (d - 2)) - Q * u / 2
    expected_rtf = Q * (sp.Rational(1, 2) / d - u / 2)

    assert sp.simplify(k_rr - expected_rr) == 0
    assert sp.simplify(k_rrn - expected_rrn) == 0
    assert sp.simplify(k_rtf - expected_rtf) == 0

    # Fourier convention: Box_perp=Box-D^2 -> -Q(1-u).
    qperp2 = Q * (1 - u)
    boxperp = -qperp2

    k_jr = sp.factor(boxperp * k_rr)
    k_js = sp.factor(boxperp * k_rrn)
    k_jtf = sp.factor(boxperp * k_rtf)

    # Trace/traceless decomposition identity.
    decomposition_residual = sp.factor(k_js - (k_jr / d + k_jtf))
    assert decomposition_residual == 0

    # Formal isotropic-substitution check only; it is not used to reduce
    # the fixed-geodesic observable before line/form-factor integration.
    iso_rtf = sp.simplify(k_rtf.subs(u, 1 / d))
    iso_jtf = sp.simplify(k_jtf.subs(u, 1 / d))
    assert iso_rtf == 0
    assert iso_jtf == 0

    # Two independent angular shapes after common Q^2 factors.
    shape_trace = sp.factor(1 - u)
    shape_tf = sp.factor((1 - u) * (u - 1 / d))
    shape_ratio = sp.simplify(shape_tf / shape_trace)
    assert sp.simplify(sp.diff(shape_ratio, u)) != 0

    d4 = {
        "K_RR": sp.factor(k_rr.subs(d, 4)),
        "K_RRn": sp.factor(k_rrn.subs(d, 4)),
        "K_RTF": sp.factor(k_rtf.subs(d, 4)),
        "K_JR": sp.factor(k_jr.subs(d, 4)),
        "K_JS": sp.factor(k_js.subs(d, 4)),
        "K_JTF": sp.factor(k_jtf.subs(d, 4)),
    }

    data = {
        "status": "PASS_SYMBOLIC_ASSERTIONS",
        "conventions": {
            "Q": "q^2",
            "u": "(q.n)^2/q^2",
            "box_perp_fourier": "-Q(1-u)",
            "propagator_numerator": (
                "1/2(delta_mr delta_ns+delta_ms delta_nr)"
                "-delta_mn delta_rs/(d-2)"
            ),
        },
        "vertices": {
            "A_mn_for_R": "Q delta_mn-q_m q_n",
            "B_mn_for_Rnn": (
                "1/2[Q n_m n_n+Q u delta_mn"
                "-(q.n)(q_m n_n+q_n n_m)]"
            ),
        },
        "general_d": {
            "K_RR": str(k_rr),
            "K_RRn": str(k_rrn),
            "K_RTF": str(k_rtf),
            "K_JR": str(k_jr),
            "K_JS": str(k_js),
            "K_JTF": str(k_jtf),
            "decomposition_residual": str(decomposition_residual),
            "isotropic_K_RTF": str(iso_rtf),
            "isotropic_K_JTF": str(iso_jtf),
            "angular_shape_trace": str(shape_trace),
            "angular_shape_traceless": str(shape_tf),
        },
        "d4": {key: str(value) for key, value in d4.items()},
        "claim_lock": (
            "Tree/projector kernels only; no loop residue, B1, EDT fit, "
            "bridge credit, or candidate-theory claim."
        ),
    }

    out_dir = Path("artifacts/iter122")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "kernels.json").write_text(
        json.dumps(data, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# ITER122 symbolic kernel output",
        "",
        "## General d",
        "",
        f"- `K_RR = {k_rr}`",
        f"- `K_RRn = {k_rrn}`",
        f"- `K_RTF = {k_rtf}`",
        f"- `K_JR = {k_jr}`",
        f"- `K_JS = {k_js}`",
        f"- `K_JTF = {k_jtf}`",
        "",
        "Exact check: `K_JS-(K_JR/d+K_JTF)=0`.",
        "",
        "Angular shapes after common factors: `(1-u)` and `(1-u)(u-1/d)`.",
        (
            "The formal substitution `u=1/d` kills the traceless shape, "
            "but is not authorized before fixed-geodesic form-factor integration."
        ),
        "",
        "## d=4",
        "",
    ]
    lines.extend(f"- `{key} = {value}`" for key, value in d4.items())
    lines.extend(
        [
            "",
            "## Claim lock",
            "",
            "No one-loop pole residue or `B_1` is computed here.",
            "",
        ]
    )
    (out_dir / "kernels.md").write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
