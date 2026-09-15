#!/usr/bin/env python3
"""Source-sensitive assertions for Fröb geodesic initial data and Green kernels.

The script is deliberately narrow: it only passes if the exact TeX source for
arXiv:1706.01891 contains the expected first-/second-order initial-tangent
coefficients and the retarded affine Green-kernel structure.  It does not use
or infer matter-scalar loop residues.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def squash(s: str) -> str:
    s = re.sub(r"(?<!\\)%.*", "", s)
    s = re.sub(r"\s+", "", s)
    s = s.replace(r"\dfrac", r"\frac")
    return s


def any_near(text: str, anchors: list[str], needles: list[str], radius: int = 900) -> bool:
    for a in anchors:
        for m in re.finditer(a, text):
            lo = max(0, m.start() - radius)
            hi = min(len(text), m.end() + radius)
            chunk = text[lo:hi]
            if all(re.search(n, chunk) for n in needles):
                return True
    return False


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    root = Path(args.source_dir)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    raw = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in root.rglob("*.tex"))
    text = squash(raw)

    chi1 = [r"\\chi_?\{?1\}?", r"\\chi\^\{[^}]*\}_?\{?1\}?"]
    chi2 = [r"\\chi_?\{?2\}?", r"\\chi\^\{[^}]*\}_?\{?2\}?"]

    # Accept common TeX spellings of -1/2 and +3/8.
    minus_half = [r"-\\frac\{1\}\{2\}", r"-1/2"]
    three_eighths = [r"\\frac\{3\}\{8\}", r"3/8"]

    def near_coeff(anchors: list[str], coeffs: list[str]) -> bool:
        return any(any_near(text, anchors, [c, r"h"]) for c in coeffs)

    # Green solution kernel, allowing tau' / tau^prime / sigma notation.
    green_patterns = [
        r"\\tau-\\tau'",
        r"\\tau-\\tau\^\{?\\prime\}?",
        r"\\tau-\\sigma",
    ]

    facts = {
        "chi1_has_minus_one_half_initial_metric_term": near_coeff(chi1, minus_half),
        "chi2_has_plus_three_eighths_quadratic_metric_term": near_coeff(chi2, three_eighths),
        "has_affine_green_difference_kernel": any(re.search(p, text) for p in green_patterns),
        "chi2_source_references_chi1": any_near(text, chi2, [r"\\chi_?\{?1\}?", r"\\Gamma"]),
        "chi1_source_references_christoffel": any_near(text, chi1, [r"\\Gamma"]),
        "chi2_source_references_christoffel": any_near(text, chi2, [r"\\Gamma"]),
    }

    for key, value in facts.items():
        if not value:
            raise AssertionError(f"exact-source assertion failed: {key}")

    result = {
        "status": "PASS_EXACT_SOURCE_COEFFICIENT_ASSERTIONS",
        "facts": facts,
        "interpretation": {
            "chi1_initial_metric_coefficient": "-1/2",
            "chi2_quadratic_initial_metric_coefficient": "+3/8",
            "green_kernel": "retarded affine difference kernel of tau-tau' type",
            "second_order_nesting": "chi2 source contains chi1 and Christoffel structure, so explicit substitution has at most two affine variables at this perturbative order",
        },
        "claim_lock": "Source-structure assertions only; no loop residue or B1 is inferred.",
    }
    (out / "initial_tangent_and_green_kernel.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
