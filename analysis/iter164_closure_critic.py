#!/usr/bin/env python3
"""Independent ITER164 closure critic.

Independent route from the operation-audit: read terminal/source authority and
inspect the post-ITER163 scientific-code delta.  Do not consume producer JSON
and do not confuse general extension theorems with an executable source-level
open-G endpoint R-operation.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITER163_RECOVERY_PARENT = "08fb86668a86899ec9132a043d306166195b5203"

AUTHORITY_ASSERTIONS = [
    (
        "analysis/ITER153_RESULT_2026-09-17.md",
        [
            "BLOCKED_SCOPED_SLOT5_REQUIRES_NEW_DISTRIBUTIONAL_EXTENSION_OR_RENORMALIZATION_INPUT",
            "one_over_epsilon = null",
            "extra local renormalization datum is required",
        ],
    ),
    (
        "sources/ITER153_DISTRIBUTION_PULLBACK_EXTENSION_AUTHORITY_2026-09-17.md",
        [
            "repository already supplies the raw seven-contact manifest and a general local-extension formalism",
            "What is not supplied is a source-qualified **graph-level R-operation/renormalization map",
            "A missing source-qualified line distribution/R-operation is `BLOCKED_SCOPED`",
        ],
    ),
    (
        "analysis/ITER161_RESULT_2026-09-17.md",
        [
            "BLOCKED_SCOPED_ITER161_G_ENDPOINT_TENSOR_LIFT_EXACT_MISSING_PRIMITIVE",
            "remaining single primitive",
            "distributional endpoint R-operation/extension",
        ],
    ),
    (
        "analysis/ITER163_TERMINAL_RESULT.md",
        [
            "PASS_SCOPED_ITER163_SOURCE_COMPLETE_COVARIANT_CLOSURE_AND_K_DIVISIBILITY",
            "not** a complete endpoint distributional R-operation",
            "ITER164_OPEN_G_ENDPOINT_LAURENT_DISTRIBUTIONAL_R_OPERATION",
        ],
    ),
    (
        "sources/ITER162_DISTRIBUTIONAL_EXTENSION_AUTHORITY_CANDIDATE_2026-09-17.md",
        [
            "AUTHORITY_CANDIDATE_ONLY — NOT YET APPLIED TO THE OPEN-G ENDPOINT TENSOR",
            "does **not** by itself establish that the current source-derived unseparated open-G endpoint tensor satisfies all hypotheses",
            "NAVIGATOR / MATHEMATICAL_EXTENSION_THEOREM_CANDIDATE",
        ],
    ),
]

KNOWN_ITER164_IMPLEMENTATION = {
    "analysis/ITER164_PREREG.md",
    "analysis/iter164_source_operation_audit.py",
    "analysis/iter164_closure_critic.py",
    ".github/workflows/isqgr-iter164-source-operation-availability.yml",
}


def git(*args: str) -> str:
    return subprocess.run(["git", *args], check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.strip()


def line_matches(rel: str, phrases: list[str]) -> dict:
    p = ROOT / rel
    if not p.exists():
        return {"file": rel, "present": False, "phrases": []}
    lines = p.read_text(encoding="utf-8", errors="ignore").splitlines()
    rows = []
    for phrase in phrases:
        found = [{"line": i, "text": line.strip()} for i, line in enumerate(lines, 1) if phrase in line]
        rows.append({"phrase": phrase, "found": bool(found), "matches": found[:3]})
    return {"file": rel, "present": True, "phrases": rows}


def main() -> None:
    evidence = [line_matches(rel, phrases) for rel, phrases in AUTHORITY_ASSERTIONS]
    authority_ok = all(
        row["present"] and all(x["found"] for x in row["phrases"])
        for row in evidence
    )

    changed = [x for x in git("diff", "--name-only", f"{ITER163_RECOVERY_PARENT}..HEAD").splitlines() if x]
    unexpected_post_iter163_code = [
        x for x in changed
        if x.endswith(".py") and x not in KNOWN_ITER164_IMPLEMENTATION
    ]

    # Independent logical closure test:
    # 1. General scaling-degree extension theory exists, but ITER153 explicitly says
    #    it does not supply the graph-level unseparated open-G map.
    # 2. ITER161 names that map as the remaining primitive.
    # 3. ITER163 closes source tensor structure only and names ITER164 next.
    # 4. The stored DFKR/EG authority remains candidate-only until the open-G
    #    hypotheses, ambient-to-affine map and ambiguity basis are constructed.
    # 5. No separate post-ITER163 scientific Python implementation has been added.
    if not authority_ok:
        classification = "INFRASTRUCTURE_FAIL_MISSING_AUTHORITY"
    elif unexpected_post_iter163_code:
        classification = "REVIEW_REQUIRED_POST_ITER163_OPERATION_CANDIDATE"
    else:
        classification = "BLOCKED_MISSING_SOURCE_OPERATION_CRITIC"

    out = {
        "gate": "ITER164_INDEPENDENT_CLOSURE_CRITIC",
        "classification": classification,
        "authority_evidence": evidence,
        "authority_chain_verified": bool(authority_ok),
        "iter163_recovery_parent": ITER163_RECOVERY_PARENT,
        "changed_files_since_validated_ITER163": changed,
        "unexpected_post_ITER163_python_candidates": unexpected_post_iter163_code,
        "general_extension_theory_present": True,
        "general_extension_theory_is_source_operation": False,
        "explicit_complete_operation_found": False,
        "complete_pole_tensor_authorized": False,
        "critic_conclusion": (
            "The repository contains general distribution-extension authority but still lacks the source-faithful "
            "unseparated open-G endpoint R-operation required to preserve orientation/free metric leg and assign "
            "cancelled-propagator contacts. A Laurent/pole producer would add an unstated prescription at this frontier."
            if classification == "BLOCKED_MISSING_SOURCE_OPERATION_CRITIC" else
            "No terminal scientific conclusion: authority or post-ITER163 code requires adjudication."
        ),
        "locks": {
            "contacts_set_zero": False,
            "ITER160_minus525_consumed": False,
            "ITER118_MATCHING_AUTHORIZED": False,
            "B1_total": "UNAUTHORIZED",
            "BRIDGE_DERIVED": False,
            "candidate_theory": "UNFORMED / 0%",
        },
    }
    Path("iter164_closure_critic.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(2 if classification.startswith("INFRASTRUCTURE_FAIL") else 0)


if __name__ == "__main__":
    main()
