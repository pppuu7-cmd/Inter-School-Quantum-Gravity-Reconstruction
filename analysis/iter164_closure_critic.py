#!/usr/bin/env python3
"""Independent ITER164 closure critic.

Independent route from the operation-audit: read terminal scientific authority
and inspect the post-ITER163 code delta.  Do not consume the producer JSON and
do not infer an executable R-operation from lexical mentions.
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
    # 1. ITER153 says the endpoint contact pole is null/unknown without extra local datum.
    # 2. ITER161 names the missing unseparated open-leg endpoint R-operation.
    # 3. ITER163 explicitly remains non-distributional and names ITER164 as next gate.
    # 4. Since validated ITER163, no separate scientific Python implementation of such
    #    an operation has been added; only this prereg/audit/critic execution machinery changed.
    if not authority_ok:
        classification = "INFRASTRUCTURE_FAIL_MISSING_AUTHORITY"
    elif unexpected_post_iter163_code:
        classification = "REVIEW_REQUIRED_POST_ITER163_OPERATION_CANDIDATE"
    else:
        classification = "BLOCKED_MISSING_SOURCE_OPERATION_CRITIC"

    complete_pole_tensor_authorized = classification == "PASS_SOURCE_OPERATION_AVAILABLE_CRITIC"
    out = {
        "gate": "ITER164_INDEPENDENT_CLOSURE_CRITIC",
        "classification": classification,
        "authority_evidence": evidence,
        "authority_chain_verified": bool(authority_ok),
        "iter163_recovery_parent": ITER163_RECOVERY_PARENT,
        "changed_files_since_validated_ITER163": changed,
        "unexpected_post_ITER163_python_candidates": unexpected_post_iter163_code,
        "explicit_complete_operation_found": False,
        "complete_pole_tensor_authorized": complete_pole_tensor_authorized,
        "critic_conclusion": (
            "The authoritative chain still lacks the source-faithful unseparated open-G endpoint "
            "distributional R-operation required to assign cancelled-propagator contacts. A Laurent/pole "
            "producer would add an unstated prescription at this frontier."
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
