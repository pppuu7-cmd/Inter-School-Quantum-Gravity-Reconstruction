#!/usr/bin/env python3
"""Strict same-equation assertions for Fröb chi1/chi2 source coefficients.

This v2 classifier only accepts a coefficient when it occurs in the same TeX
equation environment as the corresponding perturbative geodesic order.
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


def clean(s: str) -> str:
    s = re.sub(r"(?<!\\)%.*", "", s)
    s = re.sub(r"\s+", "", s)
    return s.replace(r"\dfrac", r"\frac")


def line_no(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def has_order(s: str, n: int) -> bool:
    pats = [
        rf"\\chi_\{{?{n}\}}?",
        rf"\\chi\^\{{[^}}]*\}}_\{{?{n}\}}?",
        rf"\\dot\{{?\\chi\}}?_\{{?{n}\}}?",
        rf"\\dot\{{\\chi\}}_\{{?{n}\}}?",
    ]
    return any(re.search(p, s) for p in pats)


def coeff_in_block(s: str, num: int, den: int, sign: int) -> bool:
    prefix = "-" if sign < 0 else r"\+?"
    pats = [
        prefix + rf"\\frac\{{{num}\}}\{{{den}\}}",
        prefix + rf"{num}/{den}",
    ]
    return any(re.search(p, s) for p in pats)


def green_kernel(s: str) -> bool:
    pats = [
        r"\\tau-\\tau'",
        r"\\tau-\\tau\^\{?\\prime\}?",
        r"\\tau-\\sigma",
        r"\\tau-\\tau_\{?1\}?",
    ]
    return any(re.search(p, s) for p in pats)


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
        for m in ENV_RE.finditer(raw):
            raw_block = m.group(0)
            s = clean(raw_block)
            if "\\chi" not in s:
                continue
            blocks.append(
                {
                    "file": str(path.relative_to(root)),
                    "line": line_no(raw, m.start()),
                    "env": m.group("env"),
                    "text": re.sub(r"\s+", " ", raw_block.strip())[:1800],
                    "norm": s,
                }
            )

    chi1_coeff = [
        b for b in blocks
        if has_order(b["norm"], 1)
        and coeff_in_block(b["norm"], 1, 2, -1)
        and "h" in b["norm"]
    ]
    chi2_coeff = [
        b for b in blocks
        if has_order(b["norm"], 2)
        and coeff_in_block(b["norm"], 3, 8, +1)
        and "h" in b["norm"]
    ]
    greens = [b for b in blocks if green_kernel(b["norm"]) and "\\int" in b["norm"]]
    chi2_nested = [
        b for b in blocks
        if has_order(b["norm"], 2)
        and has_order(b["norm"], 1)
        and "\\Gamma" in b["norm"]
    ]

    facts = {
        "same_equation_chi1_minus_half": bool(chi1_coeff),
        "same_equation_chi2_plus_three_eighths": bool(chi2_coeff),
        "same_equation_green_kernel_integral": bool(greens),
        "same_equation_chi2_references_chi1_and_gamma": bool(chi2_nested),
    }
    for k, v in facts.items():
        if not v:
            raise AssertionError(f"strict source assertion failed: {k}")

    def evidence(rows):
        return [
            {"file": r["file"], "line": r["line"], "env": r["env"], "equation": r["text"]}
            for r in rows[:3]
        ]

    result = {
        "status": "PASS_STRICT_SAME_EQUATION_SOURCE_ASSERTIONS",
        "facts": facts,
        "evidence": {
            "chi1_minus_half": evidence(chi1_coeff),
            "chi2_plus_three_eighths": evidence(chi2_coeff),
            "green_kernel": evidence(greens),
            "chi2_nesting": evidence(chi2_nested),
        },
        "claim_lock": "Strict source-equation authority only; no loop residue or B1 inference.",
    }
    (out / "strict_source_assertions.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"status": result["status"], "facts": facts}, indent=2))


if __name__ == "__main__":
    main()
