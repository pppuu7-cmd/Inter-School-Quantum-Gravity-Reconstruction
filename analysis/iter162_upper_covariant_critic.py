#!/usr/bin/env python3
"""Independent Critic for the ITER162 upper covariant reconstruction sub-result.

This Critic does not reuse the producer's design matrix or fixture generator.
It consumes only the emitted coefficient manifest, reconstructs the frozen
covariants independently, and compares against the ITER161 source-derived
upper_open_vertex on changed exact n^2=1 fixtures.

It intentionally does NOT certify a complete K-support decomposition: explicit
K factors are a sound contact-candidate subset, while full tensor-numerator
K-divisibility remains a later preregistered operation.
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction as F
from pathlib import Path

import sympy as s

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import iter161_endpoint_open_leg_factorization as i161

RESULT = Path("iter162_upper_covariant_reconstruction.json")


def dot(x, y):
    return sum((F(a) * F(b) for a, b in zip(x, y)), F(0))


def tangent(D, case):
    triples = [(20, 21, 29), (9, 40, 41), (12, 35, 37)]
    aa, bb, cc = triples[case % len(triples)]
    n = [F(0) for _ in range(D)]
    p = (case + 1) % D
    q = (case + 3) % D
    if q == p:
        q = (p + 1) % D
    n[p] = F(aa, cc)
    n[q] = F(bb, cc)
    assert dot(n, n) == 1
    return tuple(n)


def fixture(D, case):
    # Deliberately unrelated to producer RNG/design fixtures.
    q = tuple(F(((i + 2) * (case + 3)) % 7 - 3) for i in range(D))
    k = tuple(F(((i + 5) * (case + 4)) % 9 - 4) for i in range(D))
    if not any(q):
        q = (F(1),) + q[1:]
    if not any(k):
        k = (F(2),) + k[1:]
    return q, k, tangent(D, case)


def invs(q, k, n):
    return {
        "Q": dot(q, q),
        "K": dot(k, k),
        "S": dot(q, k),
        "a": dot(n, q),
        "b": dot(n, k),
    }


def scalar_from_label(label, q, k, n):
    if label == "1":
        return F(1)
    vals = invs(q, k, n)
    out = F(1)
    for piece in label.split("*"):
        if "^" in piece:
            name, power = piece.split("^")
            out *= vals[name] ** int(power)
        else:
            out *= vals[piece]
    return out


def seed(seed_name, q, k, n, a, b):
    if seed_name == "delta_ab":
        return F(a == b)
    if seed_name == "q_aq_b":
        return F(q[a]) * F(q[b])
    if seed_name == "q_(a_k_b)":
        return (F(q[a]) * F(k[b]) + F(k[a]) * F(q[b])) / 2
    if seed_name == "k_ak_b":
        return F(k[a]) * F(k[b])
    if seed_name == "q_(a_n_b)":
        return (F(q[a]) * F(n[b]) + F(n[a]) * F(q[b])) / 2
    if seed_name == "k_(a_n_b)":
        return (F(k[a]) * F(n[b]) + F(n[a]) * F(k[b])) / 2
    if seed_name == "n_an_b":
        return F(n[a]) * F(n[b])
    raise KeyError(seed_name)


def as_sym_fraction(x):
    x = F(x)
    return s.Rational(x.numerator, x.denominator)


def reconstruct_component(rows, D, q, k, n, a, b):
    d = s.symbols("d")
    total = s.Integer(0)
    for row in rows:
        coeff = s.sympify(row["coefficient_d"]).subs(d, D)
        term = seed(row["seed"], q, k, n, a, b) * scalar_from_label(row["scalar"], q, k, n)
        total += coeff * as_sym_fraction(term)
    return s.factor(total)


def main():
    if not RESULT.exists():
        raise RuntimeError("producer JSON missing")
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    rows = data["coefficients"]

    checks = {}
    checks["A_manifest_has_36_frozen_covariants"] = len(rows) == 36
    checks["B_producer_scoped_nonterminal"] = data.get("terminal_science") is False
    checks["C_no_ITER160_normalization"] = data["locks"].get("ITER160_minus525_consumed") is False
    checks["D_no_scalar28_inverse"] = data["locks"].get("inverse_28_scalar_map") is False
    checks["E_no_ITER118_solve"] = data["locks"].get("ITER118_coefficient_solve") is False
    checks["F_no_contacts_zero"] = data["locks"].get("contacts_set_zero") is False
    checks["G_support_claim_remains_prefilter_only"] = (
        "not yet promoted" in data.get("support_statement", "")
        and "full tensor-numerator divisibility" in data.get("remaining_blocker", "")
    )

    held = []
    exact_all = True
    for D in [4, 6, 8, 9, 10]:
        for case in [0, 1]:
            q, k, n = fixture(D, case + 100 * D)
            direct = i161.upper_open_vertex(q, k, n, D)
            ok = True
            for a in range(D):
                for b in range(a, D):
                    rec = reconstruct_component(rows, D, q, k, n, a, b)
                    target = as_sym_fraction(direct[a][b])
                    if s.simplify(rec - target) != 0:
                        ok = False
                        break
                if not ok:
                    break
            exact_all &= ok
            held.append({
                "D": D,
                "case": case,
                "n_squared": str(dot(n, n)),
                "all_symmetric_components_exact": bool(ok),
            })
    checks["H_independent_changed_fixtures_exact"] = exact_all

    # Independent syntactic audit: every explicit-K row really contains K as a
    # scalar factor. The converse is deliberately not asserted.
    explicit_k_sound = True
    for row in rows:
        if row.get("explicit_K_factor"):
            pieces = row["scalar"].split("*") if row["scalar"] != "1" else []
            explicit_k_sound &= any(p == "K" or p.startswith("K^") for p in pieces)
    checks["I_explicit_K_contact_candidate_subset_sound"] = explicit_k_sound

    passed = all(bool(v) for v in checks.values())
    out = {
        "gate": "ITER162_OPEN_G_ENDPOINT_DISTRIBUTIONAL_R_OPERATION_AND_POLE_TENSOR",
        "critic_verdict": (
            "PASS_CRITIC_ITER162_UPPER_COVARIANT_RECONSTRUCTION_SCOPE_SOUND"
            if passed else
            "FAIL_CRITIC_ITER162_UPPER_COVARIANT_RECONSTRUCTION"
        ),
        "checks": checks,
        "heldout": held,
        "scope": (
            "source-derived upper V_ab covariant reconstruction only; explicit-K is a certified contact-candidate "
            "subset, not a complete tensor support decomposition; no endpoint Laurent extension, ambiguity quotient, "
            "ITER118 coefficient equation, B1_total, bridge, or candidate theory"
        ),
        "next_required_operation": (
            "exact full tensor-numerator K-divisibility/support decomposition followed by the distributional Laurent "
            "extension and exact local-ambiguity quotient required by the frozen ITER162 preregistration"
        ),
    }
    Path("iter162_upper_covariant_critic.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
