#!/usr/bin/env python3
"""ITER122: symbolic general-d linearized curvature / genuine-defect kernels.

This script deliberately stops at tree/projector kernels.  It does not evaluate
one-loop pole residues or infer B1.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    d, Q, u = sp.symbols("d Q u", positive=True)

    # Frozen invariants: Q=q^2, u=(q.n)^2/Q, n^2=1.
    # Linearized scalar-curvature vertex:
    #   A_mn = Q delta_mn - q_m q_n.
    trA = (d - 1) * Q
    AA = (d - 1) * Q**2

    # Linearized R_nn vertex:
    #   B_mn = 1/2[Q n_m n_n + (q.n)^2 delta_mn
    #              -(q.n)(q_m n_n+q_n n_m)].
    # Its invariant contractions with A are sufficient for A P B.
    trB = sp.Rational(1, 2) * Q * (1 + (d - 2) * u)
    AB = sp.simplify(Q * trB)  # q_m q_n B_mn=0, hence A:B=Q trB.

    # De-Donder numerator acts on symmetric tensors as
    # X:P:Y = X:Y - tr(X)tr(Y)/(d-2); propagator contributes 1/Q.
    K_RR = sp.factor((AA - trA**2 / (d - 2)) / Q)
    K_RRn = sp.factor((AB - trA * trB / (d - 2)) / Q)
    K_RTF = sp.factor(K_RRn - K_RR / d)

    expected_RR = -(d - 1) * Q / (d - 2)
    expected_RRn = -Q / (2 * (d - 2)) - Q * u / 2
    expected_RTF = Q * (sp.Rational(1, 2) / d - u / 2)

    assert sp.simplify(K_RR - expected_RR) == 0
    assert sp.simplify(K_RRn - expected_RRn) == 0
    assert sp.simplify(K_RTF - expected_RTF) == 0

    # Fourier convention: Box_perp=Box-D^2 -> -(Q-(q.n)^2).
    qperp2 = Q * (1 - u)
    boxperp_multiplier = -qperp2

    K_JR = sp.factor(boxperp_multiplier * K_RR)
    K_JS = sp.factor(boxperp_multiplier * K_RRn)
    K_JTF = sp.factor(boxperp_multiplier * K_RTF)

    # Exact trace/traceless decomposition check.
    decomposition_check = sp.factor(K_JS - (K_JR / d + K_JTF))
    assert decomposition_check == 0

    # Formal isotropic angular substitution; recorded only as a check.
    iso_RTF = sp.simplify(K_RTF.subs(u, 1 / d))
    iso_JTF = sp.simplify(K_JTF.subs(u, 1 / d))
    assert iso_RTF == 0
    assert iso_JTF == 0

    # Two angular shapes after removing common Q^2 factors.
    shape_trace = sp.factor(1 - u)
    shape_tf = sp.factor((1 - u) * (u - 1 / d))
    # They are not proportional for symbolic u: ratio depends on u.
    ratio = sp.simplify(shape_tf / shape_trace)
    assert sp.diff(ratio, u) != 0

    d4 = {
        "K_RR": sp.factor(K_RR.subs(d, 4)),
        "K_RRn": sp.factor(K_RRn.subs(d, 4)),
        "K_RTF": sp.factor(K_RTF.subs(d, 4)),
        "K_JR": sp.factor(K_JR.subs(d, 4)),
        "K_JS": sp.factor(K_JS.subs(d, 4)),
        "K_JTF": sp.factor(K_JTF.subs(d, 4)),
    }

    formulas = {
        "conventions": {
            "Q": "q^2",
            "u": "(q.n)^2/q^2",
            "box_perp_fourier": "-Q(1-u)",
            "propagator_numerator": "1/2(delta_mr delta_ns+delta_ms delta_nr)-delta_mn delta_rs/(d-2)",
        },
        "vertices": {
            "A_mn_for_R": "Q delta_mn - q_m q_n",
            "B_mn_for_Rnn": "1/2[Q n_m n_n + Q u delta_mn - sqrt(Q u)(q_m n_n+q_n n_m)]",
        },
        "general_d": {
            "K_RR": str(K_RR),
            "K_RRn": str(K_RRn),
            "K_RTF": str(K_RTF),
            "K_JR": str(K_JR),
            "K_JS": str(K_JS),
            "K_JTF": str(K_JTF),
            "decomposition_residual": str(decomposition_check),
            "isotropic_K_RTF": str(iso_RTF),
            "isotropic_K_JTF": str(iso_JTF),
            "angular_shape_trace": str(shape_trace),
            "angular_shape_traceless": str(shape_tf),
        },
        "d4": {k: str(v) for k, v in d4.items()},
        "claim_lock": "Tree/projector kernels only; no loop residue, B1, EDT fit, or bridge claim.",
    }

    out_dir = Path("artifacts/iter122")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "kernels.json").write_text(json.dumps(formulas, indent=2) + "\n", encoding="utf-8")

    md = f"""# ITER122 symbolic kernel output\n\n"
    md += "## General d\n\n"
    md += f"- `K_RR = {K_RR}`\n"
    md += f"- `K_RRn = {K_RRn}`\n"
    md += f"- `K_RTF = {K_RTF}`\n"
    md += f"- `K_JR = {K_JR}`\n"
    md += f"- `K_JS = {K_JS}`\n"
    md += f"- `K_JTF = {K_JTF}`\n\n"
    md += "Exact check: `K_JS - (K_JR/d + K_JTF) = 0`.\n\n"
    md += "Angular shapes after common factors: `(1-u)` and `(1-u)(u-1/d)`.\n"
    md += "The formal substitution `u=1/d` kills the traceless shape, but is **not** authorized before fixed-geodesic form-factor integration.\n\n"
    md += "## d=4\n\n"
    for k, v in d4.items():
        md += f"- `{k} = {v}`\n"
    md += "\n## Claim lock\n\nNo one-loop pole residue or `B_1` is computed here.\n"
    (out_dir / "kernels.md").write_text(md, encoding="utf-8")

    print(json.dumps(formulas, indent=2))


if __name__ == "__main__":
    main()
