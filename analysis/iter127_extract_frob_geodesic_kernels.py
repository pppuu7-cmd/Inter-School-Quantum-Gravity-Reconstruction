#!/usr/bin/env python3
"""Extract short equation-only geodesic-kernel snippets from arXiv:1706.01891.

The extractor preserves hashes and locations but deliberately avoids copying
large prose blocks. It is source transport/authority tooling, not a physics
coefficient calculation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def strip_comments(text: str) -> str:
    out = []
    for line in text.splitlines():
        # Conservative TeX comment stripping; escaped percent is rare in equations.
        m = re.search(r"(?<!\\)%", line)
        if m:
            line = line[: m.start()]
        out.append(line)
    return "\n".join(out)


def equation_blocks(text: str):
    envs = r"equation\*?|align\*?|alignat\*?|gather\*?|multline\*?|split"
    pat = re.compile(
        rf"\\begin\{{(?P<env>{envs})\}}(?P<body>.*?)\\end\{{(?P=env)\}}",
        re.S,
    )
    for m in pat.finditer(text):
        yield m.start(), m.group("env"), m.group(0)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def normalize_math(s: str, limit: int = 1600) -> str:
    s = re.sub(r"\n\s*", "\n", s.strip())
    return s[:limit]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-dir", required=True)
    ap.add_argument("--archive", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    src = Path(args.source_dir)
    archive = Path(args.archive)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    tex_files = sorted(src.rglob("*.tex"))
    inventory = []
    candidates = []

    # Patterns are intentionally broad because notation can differ slightly.
    strong = [r"\\chi[_^{]", r"\\dot\{?\\chi", r"chi_1", r"chi_2"]
    context = [r"geodesic", r"Christoffel", r"\\Gamma"]

    for path in tex_files:
        raw = path.read_text(encoding="utf-8", errors="replace")
        text = strip_comments(raw)
        rel = str(path.relative_to(src))
        inventory.append({"path": rel, "sha256": sha256(path), "bytes": path.stat().st_size})

        for off, env, block in equation_blocks(text):
            score = 0
            for p in strong:
                if re.search(p, block, re.I):
                    score += 4
            for p in context:
                if re.search(p, block, re.I):
                    score += 1
            if score:
                candidates.append(
                    {
                        "score": score,
                        "file": rel,
                        "line": line_number(text, off),
                        "environment": env,
                        "math": normalize_math(block),
                        "has_integral": "\\int" in block,
                        "has_chi": "\\chi" in block or "chi_" in block,
                        "has_gamma": "\\Gamma" in block,
                    }
                )

    candidates.sort(key=lambda x: (-x["score"], x["file"], x["line"]))

    # Keep a small equation-only evidence set. Dedupe exact math blocks.
    selected = []
    seen = set()
    for c in candidates:
        key = c["math"]
        if key in seen:
            continue
        seen.add(key)
        selected.append(c)
        if len(selected) >= 8:
            break

    result = {
        "arxiv_id": "1706.01891",
        "archive_sha256": sha256(archive),
        "tex_inventory": inventory,
        "selected_equation_count": len(selected),
        "selected_equations": selected,
        "pattern_summary": {
            "candidate_equation_count": len(candidates),
            "selected_with_integral": sum(1 for x in selected if x["has_integral"]),
            "selected_with_chi": sum(1 for x in selected if x["has_chi"]),
            "selected_with_gamma": sum(1 for x in selected if x["has_gamma"]),
        },
        "claim_lock": (
            "Exact-source equation extraction only; no matter-scalar residue is "
            "transferred to curvature and no B1/EDT claim is made."
        ),
    }

    (out / "source_authority.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# ITER127 exact-source equation evidence",
        "",
        f"Archive SHA256: `{result['archive_sha256']}`",
        f"TeX files: `{len(inventory)}`",
        f"Candidate equation environments: `{len(candidates)}`",
        f"Selected short equation environments: `{len(selected)}`",
        "",
    ]
    for i, c in enumerate(selected, 1):
        lines.extend(
            [
                f"## Equation evidence {i}",
                f"Source: `{c['file']}:{c['line']}`; env `{c['environment']}`; score `{c['score']}`.",
                "```tex",
                c["math"],
                "```",
                "",
            ]
        )
    lines.extend(["## Claim lock", "", result["claim_lock"], ""])
    (out / "source_authority.md").write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps({
        "archive_sha256": result["archive_sha256"],
        "tex_files": len(inventory),
        "candidate_equations": len(candidates),
        "selected_equations": len(selected),
    }, indent=2))


if __name__ == "__main__":
    main()
