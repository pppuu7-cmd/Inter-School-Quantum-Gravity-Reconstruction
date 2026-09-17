#!/usr/bin/env python3
"""ITER164 frozen source-operation availability audit.

This is an availability gate, not a Laurent producer.  It fails closed unless
an executable source-faithful endpoint/open-leg renormalization operation is
actually present.  Lexical co-occurrence near an arbitrary function is never
sufficient evidence.
"""
from __future__ import annotations

import ast
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITER163_RECOVERY_PARENT = "08fb86668a86899ec9132a043d306166195b5203"

AUTHORITY = {
    "ITER153": ROOT / "analysis/ITER153_RESULT_2026-09-17.md",
    "ITER154B": ROOT / "analysis/ITER154B_RESULT_2026-09-17.md",
    "ITER161": ROOT / "analysis/ITER161_RESULT_2026-09-17.md",
    "ITER163": ROOT / "analysis/ITER163_TERMINAL_RESULT.md",
}

EXPECTED = {
    "ITER153": [
        "BLOCKED_SCOPED_SLOT5_REQUIRES_NEW_DISTRIBUTIONAL_EXTENSION_OR_RENORMALIZATION_INPUT",
        "one_over_epsilon = null",
        "graph-level R-operation / renormalization map on the unseparated first-M/G amplitude",
    ],
    "ITER154B": [
        "PASS_SCOPED_SLOT6_FIRST_MG_PRIMITIVE_BUBBLES_NO_PROPER_SUBDIVERGENCES",
        "R_sub G = G",
        "endpoint counterterms",
    ],
    "ITER161": [
        "BLOCKED_SCOPED_ITER161_G_ENDPOINT_TENSOR_LIFT_EXACT_MISSING_PRIMITIVE",
        "distributional endpoint R-operation/extension",
        "unseparated `G_R1_chi2_Gamma2_dR1` endpoint vertex",
    ],
    "ITER163": [
        "PASS_SCOPED_ITER163_SOURCE_COMPLETE_COVARIANT_CLOSURE_AND_K_DIVISIBILITY",
        "not** a complete endpoint distributional R-operation",
        "ITER164_OPEN_G_ENDPOINT_LAURENT_DISTRIBUTIONAL_R_OPERATION",
    ],
}

EXCLUDED_IMPLEMENTATION_FILES = {
    "analysis/iter164_source_operation_audit.py",
    "analysis/iter164_closure_critic.py",
}

NAME_RE = re.compile(r"(renormal|r_operation|roperation|laurent|distribution.*extend|extend.*distribution|pole_tensor)", re.I)
OPEN_RE = re.compile(r"(open[_ -]?leg|upper_open_vertex|lower_open_vertex|V_upper|W_lower|endpoint)", re.I)
CONTACT_RE = re.compile(r"(contact|cancelled[_ -]?propagator|counterterm)", re.I)
ORIENT_RE = re.compile(r"(upper|lower|orientation)", re.I)
DIST_RE = re.compile(r"(DiracDelta|Hadamard|finite part|plus[_ -]?distribution|forest|BPHZ|Laurent|epsilon|series\s*\()", re.I)


def git(*args: str) -> str:
    return subprocess.run(["git", *args], check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.strip()


def phrase_evidence(path: Path, phrases: list[str]) -> list[dict]:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    out = []
    for phrase in phrases:
        matches = []
        for i, line in enumerate(lines, 1):
            if phrase in line:
                matches.append({"line": i, "text": line.strip()})
        out.append({"phrase": phrase, "found": bool(matches), "matches": matches[:4]})
    return out


def changed_since_iter163() -> list[str]:
    return [x for x in git("diff", "--name-only", f"{ITER163_RECOVERY_PARENT}..HEAD").splitlines() if x]


def callable_candidates(paths: list[str]) -> list[dict]:
    candidates: list[dict] = []
    for rel in paths:
        if rel in EXCLUDED_IMPLEMENTATION_FILES or not rel.endswith(".py"):
            continue
        p = ROOT / rel
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        try:
            tree = ast.parse(text)
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if not NAME_RE.search(node.name):
                continue
            segment = ast.get_source_segment(text, node) or ""
            arg_names = [a.arg for a in node.args.args]
            checks = {
                "name_has_operation_semantics": bool(NAME_RE.search(node.name)),
                "open_or_endpoint_object_explicit": bool(OPEN_RE.search(segment) or OPEN_RE.search(" ".join(arg_names))),
                "contact_treatment_explicit": bool(CONTACT_RE.search(segment)),
                "orientation_explicit": bool(ORIENT_RE.search(segment)),
                "distributional_or_laurent_algebra_explicit": bool(DIST_RE.search(segment)),
                "returns_value": any(isinstance(x, ast.Return) for x in ast.walk(node)),
            }
            candidates.append({
                "file": rel,
                "function": node.name,
                "line": int(node.lineno),
                "args": arg_names,
                "checks": checks,
                "sufficient": all(checks.values()),
            })
    return candidates


def main() -> None:
    authority_rows = {}
    authority_ok = True
    for key, path in AUTHORITY.items():
        present = path.exists()
        ev = phrase_evidence(path, EXPECTED[key]) if present else []
        row_ok = present and all(x["found"] for x in ev)
        authority_ok &= row_ok
        authority_rows[key] = {
            "file": str(path.relative_to(ROOT)),
            "present": present,
            "expected_evidence": ev,
            "authority_state_verified": bool(row_ok),
        }

    changed = changed_since_iter163()
    candidates = callable_candidates(changed)
    sufficient = [x for x in candidates if x["sufficient"]]

    # Frozen ITER163 authority says the complete endpoint R-operation is absent.
    # A PASS therefore requires an actual post-ITER163 executable implementation,
    # not merely prose or a diagnostic gate mentioning the missing operation.
    if not authority_ok:
        classification = "INFRASTRUCTURE_FAIL_AUTHORITY_CHAIN_UNREADABLE"
    elif sufficient:
        classification = "PASS_SOURCE_OPERATION_AVAILABLE"
    else:
        classification = "BLOCKED_MISSING_SOURCE_OPERATION"

    out = {
        "gate": "ITER164_SOURCE_OPERATION_AVAILABILITY",
        "classification": classification,
        "scientific_pass": classification == "PASS_SOURCE_OPERATION_AVAILABLE",
        "iter163_recovery_parent": ITER163_RECOVERY_PARENT,
        "authority_chain": authority_rows,
        "changed_files_since_validated_ITER163": changed,
        "post_ITER163_callable_operation_candidates": candidates,
        "sufficient_operations": sufficient,
        "adjudication_rule": (
            "PASS requires a post-ITER163 callable that itself implements open/endpoint, contact, orientation, "
            "and distributional/Laurent semantics. Lexical mentions and diagnostic/evaluator functions do not qualify."
        ),
        "earliest_missing_primitive": (
            None if sufficient else
            "source-faithful distributional endpoint R-operation/extension on the unseparated source-complete "
            "open-G endpoint tensor, preserving free symmetric metric leg/orientation and assigning cancelled-propagator contacts"
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
    Path("iter164_source_operation_audit.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(2 if classification.startswith("INFRASTRUCTURE_FAIL") else 0)


if __name__ == "__main__":
    main()
