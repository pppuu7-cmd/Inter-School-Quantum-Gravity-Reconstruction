#!/usr/bin/env python3
"""Classify exact chi1/chi2 geodesic structure in arXiv:1706.01891 source.

The classifier is intentionally structural. It records exact short equation
blocks and machine-checkable properties needed for ITER127, without importing
matter-scalar residues into the curvature calculation.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ENV_RE = re.compile(
    r"\\begin\{(?P<env>equation\*?|align\*?|alignat\*?|gather\*?|multline\*?)\}"
    r"(?P<body>.*?)"
    r"\\end\{(?P=env)\}",
    re.S,
)


def strip_comments(text: str) -> str:
    out = []
    for line in text.splitlines():
        m = re.search(r"(?<!\\)%", line)
        out.append(line[: m.start()] if m else line)
    return "\n".join(out)


def compact(block: str, limit: int = 2200) -> str:
    return re.sub(r"\s+", " ", block).strip()[:limit]


def line_no(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def has_order(block: str, order: int) -> bool:
    pats = [
        rf"\\chi_\{{?{order}\}}?",
        rf"\\chi\^\{{?[^}}]*\}}?_\{{?{order}\}}?",
        rf"\\chi_\{{?\({order}\)\}}?",
        rf"chi_\{{?{order}\}}?",
    ]
    return any(re.search(p, block) for p in pats)


def tau_green_kernel(block: str) -> bool:
    # Accept common TeX renderings of (tau-tau') or (tau-sigma).
    pats = [
        r"\\tau\s*-\s*\\tau\s*\^?\{?\\prime\}?",
        r"\\tau\s*-\s*\\tau'",
        r"\\tau\s*-\s*\\sigma",
        r"\\tau\s*-\s*\\tau_1",
    ]
    return any(re.search(p, block) for p in pats)


def initial_condition(block: str, order: int) -> bool:
    order_pat = rf"\\chi_\{{?{order}\}}?"
    zero_pat = r"(?:0\)|\(0\)|\|_\{?0\}?|_\{?\tau=0\}?)"
    return bool(re.search(order_pat, block) and re.search(zero_pat, block))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    root = Path(args.source_dir)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    blocks = []
    for path in sorted(root.rglob("*.tex")):
        raw = path.read_text(encoding="utf-8", errors="replace")
        text = strip_comments(raw)
        for m in ENV_RE.finditer(text):
            b = m.group(0)
            if "\\chi" not in b and "chi_" not in b:
                continue
            blocks.append(
                {
                    "file": str(path.relative_to(root)),
                    "line": line_no(text, m.start()),
                    "env": m.group("env"),
                    "text": compact(b),
                    "order1": has_order(b, 1),
                    "order2": has_order(b, 2),
                    "integrals": b.count("\\int"),
                    "gamma": "\\Gamma" in b,
                    "green_kernel": tau_green_kernel(b),
                    "chi1_initial": initial_condition(b, 1),
                    "chi2_initial": initial_condition(b, 2),
                }
            )

    first = [b for b in blocks if b["order1"]]
    second = [b for b in blocks if b["order2"]]

    # Structural source facts required for ITER127.
    facts = {
        "has_chi1_equation": bool(first),
        "has_chi2_equation": bool(second),
        "chi1_has_line_integral": any(b["integrals"] >= 1 for b in first),
        "chi2_has_line_integral": any(b["integrals"] >= 1 for b in second),
        "chi2_references_chi1": any(
            b["order2"] and has_order(b["text"], 1) for b in blocks
        ),
        "source_has_geodesic_green_kernel": any(b["green_kernel"] for b in blocks),
        "source_has_gamma_in_chi_blocks": any(b["gamma"] for b in blocks),
        "has_chi1_initial_condition_block": any(b["chi1_initial"] for b in first),
        "has_chi2_initial_condition_block": any(b["chi2_initial"] for b in second),
        "max_integrals_in_chi1_block": max([b["integrals"] for b in first] or [0]),
        "max_integrals_in_chi2_block": max([b["integrals"] for b in second] or [0]),
    }

    # Required minimum: exact source must expose both perturbative orders, line
    # integration, Christoffel/geodesic structure, and the Green-kernel pattern.
    required_true = [
        "has_chi1_equation",
        "has_chi2_equation",
        "chi1_has_line_integral",
        "chi2_has_line_integral",
        "source_has_gamma_in_chi_blocks",
    ]
    for key in required_true:
        if not facts[key]:
            raise AssertionError(f"missing required exact-source fact: {key}")

    result = {
        "status": "PASS_STRUCTURAL_SOURCE_CLASSIFICATION",
        "facts": facts,
        "chi1_blocks": first[:6],
        "chi2_blocks": second[:6],
        "claim_lock": (
            "Structural exact-source classification only. Coefficients not "
            "explicitly present in these blocks are not reconstructed from memory."
        ),
    }
    (out / "geodesic_structure.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# ITER127 exact geodesic structure classification",
        "",
        f"Status: **{result['status']}**",
        "",
        "## Structural facts",
        "",
    ]
    lines += [f"- `{k}` = `{v}`" for k, v in facts.items()]
    lines += ["", "## Claim lock", "", result["claim_lock"], ""]
    (out / "geodesic_structure.md").write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps({"status": result["status"], "facts": facts}, indent=2))


if __name__ == "__main__":
    main()
