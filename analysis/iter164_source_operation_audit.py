#!/usr/bin/env python3
"""ITER164 frozen source-operation availability audit.

Availability gate only.  It inventories the complete tracked repository and
fails closed unless an executable, source-faithful, orientation-preserving
endpoint/open-leg renormalization operation is actually present.  Lexical
co-occurrence is evidence for inventory only, never scientific PASS evidence.
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
DIAGNOSTIC_NAME_RE = re.compile(r"^(main|.*(?:audit|critic|check|test|fixture|reason|control|scan|search).*)$", re.I)
OP_NAME_RE = re.compile(r"(renormal|r_operation|roperation|laurent|extend|extension|subtract|pole)", re.I)
SOURCE_RE = re.compile(r"(ITER163|21[-_ ]term|source[-_ ]complete|open[_ -]?leg|upper_open_vertex|lower_open_vertex|V_upper|W_lower)", re.I)
ENDPOINT_RE = re.compile(r"endpoint", re.I)
CONTACT_RE = re.compile(r"(contact|cancelled[_ -]?propagator|counterterm|polynomial[-_ ]support)", re.I)
ORIENT_RE = re.compile(r"(upper|lower|orientation|tau|1\s*-\s*tau)", re.I)
DIST_RE = re.compile(r"(DiracDelta|delta\^|delta_|Hadamard|finite part|plus[_ -]?distribution|forest|BPHZ|scaling degree|Laurent|epsilon|series\s*\()", re.I)
OUTPUT_RE = re.compile(r"(one_over_epsilon|1/epsilon|pole[_ -]?tensor|residue|extended[_ -]?distribution|local[_ -]?distribution|delta[_ -]?derivative)", re.I)

INVENTORY_PATTERNS = {
    "distributional_extension": r"distributional.*(extension|extend)|(extension|extend).*distributional",
    "r_operation": r"R-operation|r_operation|R_sub|forest|BPHZ",
    "laurent_pole": r"Laurent|one_over_epsilon|1/epsilon|pole tensor|pole_tensor",
    "contact_counterterm": r"cancelled-propagator|cancelled_propagator|contact|endpoint counterterm|counterterm",
    "finite_part_plus_distribution": r"Hadamard|finite part|plus-distribution|plus_distribution",
}


def run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, check=check, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def git(*args: str, check: bool = True) -> str:
    return run("git", *args, check=check).stdout.strip()


def phrase_evidence(path: Path, phrases: list[str]) -> list[dict]:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    out = []
    for phrase in phrases:
        matches = [{"line": i, "text": line.strip()} for i, line in enumerate(lines, 1) if phrase in line]
        out.append({"phrase": phrase, "found": bool(matches), "matches": matches[:4]})
    return out


def changed_since_iter163() -> list[str]:
    return [x for x in git("diff", "--name-only", f"{ITER163_RECOVERY_PARENT}..HEAD").splitlines() if x]


def tracked_python() -> list[str]:
    return sorted(x for x in git("ls-files", "*.py").splitlines() if x and x not in EXCLUDED_IMPLEMENTATION_FILES)


def lexical_inventory() -> dict:
    out = {}
    for key, pattern in INVENTORY_PATTERNS.items():
        cp = run("git", "grep", "-n", "-I", "-E", pattern, "--", "analysis", "sources", check=False)
        rows = []
        for raw in cp.stdout.splitlines()[:80]:
            parts = raw.split(":", 2)
            if len(parts) == 3:
                rel, lineno, text = parts
                rows.append({"file": rel, "line": int(lineno), "text": text.strip()})
        out[key] = {"match_count_capped": len(rows), "matches": rows}
    return out


def callable_candidates(paths: list[str]) -> list[dict]:
    candidates = []
    for rel in paths:
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
            segment = ast.get_source_segment(text, node) or ""
            arg_names = [a.arg for a in node.args.args]
            joined = segment + "\n" + " ".join(arg_names)
            # Record only functions with at least some operation/distribution semantics.
            if not (OP_NAME_RE.search(node.name) or DIST_RE.search(joined) or OUTPUT_RE.search(joined)):
                continue
            checks = {
                "not_diagnostic_named": not bool(DIAGNOSTIC_NAME_RE.search(node.name)),
                "operation_semantics": bool(OP_NAME_RE.search(node.name) or DIST_RE.search(joined)),
                "source_complete_open_object_explicit": bool(SOURCE_RE.search(joined)),
                "endpoint_explicit": bool(ENDPOINT_RE.search(joined)),
                "contact_treatment_explicit": bool(CONTACT_RE.search(joined)),
                "orientation_explicit": bool(ORIENT_RE.search(joined)),
                "distributional_or_laurent_algebra_explicit": bool(DIST_RE.search(joined)),
                "pole_or_extended_output_explicit": bool(OUTPUT_RE.search(joined)),
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
    pyfiles = tracked_python()
    candidates = callable_candidates(pyfiles)
    sufficient = [x for x in candidates if x["sufficient"]]

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
        "tracked_python_file_count": len(pyfiles),
        "repository_lexical_inventory": lexical_inventory(),
        "executable_operation_candidates": candidates,
        "sufficient_operations": sufficient,
        "adjudication_rule": (
            "Inventory is repository-wide. PASS requires a non-diagnostic callable that itself exposes the validated "
            "source-complete open object, endpoint/contact/orientation handling, distributional/Laurent algebra, and "
            "an explicit pole/extended-distribution output. Lexical co-occurrence is never sufficient."
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
    print(json.dumps({k: v for k, v in out.items() if k not in {"repository_lexical_inventory", "executable_operation_candidates"}}, indent=2, sort_keys=True))
    print(json.dumps({"candidate_count": len(candidates), "sufficient_count": len(sufficient)}, sort_keys=True))
    raise SystemExit(2 if classification.startswith("INFRASTRUCTURE_FAIL") else 0)


if __name__ == "__main__":
    main()
