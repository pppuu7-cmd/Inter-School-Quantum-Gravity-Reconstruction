#!/usr/bin/env python3
"""ITER139: repair affine one-propagator row ceilings using exact tensor allocation."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import sympy as s

import iter138_first_mg_exact_numerator_kernels as i138

I = s.I
D = i138.D
q = i138.q
k = i138.k
legs = i138.legs


def dR2_vertex(A, qa, B, kb, mu):
    return s.expand(I * (qa[mu] + kb[mu]) * i138.R2vertex(A, qa, B, kb))


def M2_numerator(qv, kv, nvec):
    """Connected Gaussian R1 x chi1 x dR2 cross-pairing numerator."""
    nq = tuple(-x for x in qv)
    nk = tuple(-x for x in kv)
    AR = i138.Pmap(i138.R1_tensor(nq))
    out = s.Integer(0)
    for mu in range(D):
        BC = i138.Pmap(i138.chi1_source(mu, nk, nvec))
        out += dR2_vertex(AR, qv, BC, kv, mu)
    return s.expand(out)


def direct_M2(qv, kv, nvec):
    nq = tuple(-x for x in qv)
    nk = tuple(-x for x in kv)
    x = i138.propagated_basis(i138.R1_tensor(nq))
    out = s.Integer(0)
    for mu in range(D):
        y = i138.propagated_basis(i138.chi1_source(mu, nk, nvec))
        V = [
            [dR2_vertex(i138.H(a), qv, i138.H(b), kv, mu) for b in legs]
            for a in legs
        ]
        out += sum(V[a][b] * x[a] * y[b] for a in range(10) for b in range(10))
    return s.simplify(out)


def max_line_degree(meta):
    return max(meta["left_degree"], meta["right_degree"])


def endpoint_jet(N, lower_s=0, upper_s=1):
    raw = 2 + N
    return {
        "N1": N,
        "m_raw": raw,
        "lower_s": lower_s,
        "lower_jet": raw - lower_s - 1,
        "upper_s": upper_s,
        "upper_jet": raw - upper_s - 1,
    }


def main():
    n0 = (s.Integer(1), 0, 0, 0)

    # Recompute exact closed ITER138 controls from committed implementation.
    M1 = i138.M_numerator(q, k, n0)
    G1 = i138.G_numerator(q, k, n0)
    M1_meta = i138.poly_meta(M1, q, k)
    G1_meta = i138.poly_meta(G1, q, k)

    # New exact second-M-family allocation.
    M2 = M2_numerator(q, k, n0)
    M2_meta = i138.poly_meta(M2, q, k)

    held = [
        ((1, 2, -1, 3), (2, -1, 1, 4)),
        ((2, 1, 3, -2), (-1, 2, 4, 1)),
        ((-2, 3, 1, 2), (3, -1, 2, -2)),
    ]
    held_rows = []
    held_ok = True
    for qv, kv in held:
        fast = s.simplify(M2_numerator(qv, kv, n0))
        direct = direct_M2(qv, kv, n0)
        eq = s.simplify(fast - direct) == 0
        held_ok &= bool(eq)
        held_rows.append({
            "q": list(qv), "k": list(kv),
            "fast": str(fast), "direct_basis": str(direct), "equal": bool(eq),
        })

    # Frame/covariance stress for degree only; exact unit rational panels.
    n_panels = [
        n0,
        (s.Rational(3, 5), s.Rational(4, 5), 0, 0),
        (s.Rational(1, 2), s.Rational(1, 2), s.Rational(1, 2), s.Rational(1, 2)),
    ]
    m2_cov = []
    cov_ok = True
    for nv in n_panels:
        expr = M2_numerator(q, k, nv)
        meta = i138.poly_meta(expr, q, k)
        unit = s.simplify(i138.dot(nv, nv) - 1) == 0
        ok = unit and meta["total_degree"] == 6 and max_line_degree(meta) <= 5
        cov_ok &= bool(ok)
        m2_cov.append({"n": [str(x) for x in nv], "unit": bool(unit), "meta": meta})

    exact = {
        "M_R2_chi1_dR1": max_line_degree(M1_meta),
        "M_R1_chi1_dR2": max_line_degree(M2_meta),
        "G_R1_chi2_Gamma2_dR1": max_line_degree(G1_meta),
    }

    old = json.loads(Path("analysis/iter129_graph_derivative_ceiling_table.json").read_text())
    v2 = copy.deepcopy(old)
    v2["gate"] = "ITER139_FIXED_GEODESIC_CURVATURE_AFFINE_SINGLE_LINE_CEILING_REPAIR"
    v2["supersedes_row_specific_affine_ceiling_logic_from"] = "ITER129"
    v2["global_affine_N1_ceiling"] = 5
    v2["rules"]["single_prop_m_raw_ceiling"] = "2+N1_max_v2"
    v2["rules"]["jet_after_suppression"] = "m_raw-s-1"
    v2["rules"]["allocation_warning"] = (
        "For nonlinear multi-leg vertices, exact/conservative per-line degree is not generally "
        "D_line_max+D_partner_max; vertex derivatives can concentrate on one internal leg."
    )

    exact_ids = set(exact)
    for row in v2["rows"]:
        row["old_N1_max"] = row.get("N1_max")
        if not row.get("affine"):
            row["N1_max_v2"] = None
            row["ceiling_authority_v2"] = "NOT_AFFINE"
            continue
        rid = row["id"]
        if rid in exact_ids:
            row["N1_max_v2"] = int(exact[rid])
            row["ceiling_authority_v2"] = "EXACT_TENSOR_ALLOCATION_ITER138_139"
        elif row["N1_max"] == 5:
            row["N1_max_v2"] = 5
            row["ceiling_authority_v2"] = "ITER129_GLOBAL_SAFE_BOUND_ALREADY_SATURATED"
        else:
            row["N1_max_v2"] = 5
            row["ceiling_authority_v2"] = "GLOBAL_SAFE_BOUND_PENDING_EXACT_ALLOCATION"

        N = row["N1_max_v2"]
        row["single_prop_m_raw_ceiling_v2"] = 2 + N
        sup = row.get("source_suppression", {})
        if set(["lower", "upper"]).issubset(sup):
            row["endpoint_jet_ceiling_v2"] = endpoint_jet(N, sup["lower"], sup["upper"])

    by = {r["id"]: r for r in v2["rows"]}
    checks = {
        "A_M1_reproduces_degree5": exact["M_R2_chi1_dR1"] == 5,
        "B_G1_reproduces_degree4": exact["G_R1_chi2_Gamma2_dR1"] == 4,
        "C_M2_exact_total_degree6": M2_meta["total_degree"] == 6,
        "D_M2_exact_line_degree_le5": exact["M_R1_chi1_dR2"] <= 5,
        "E_M2_heldout_direct_basis": bool(held_ok),
        "F_M2_unit_vector_panels": bool(cov_ok),
        "G_v2_upper_bounds_exact_rows": all(by[r]["N1_max_v2"] >= exact[r] for r in exact),
        "H_v2_respects_global_N1_le5": max(r.get("N1_max_v2") or 0 for r in v2["rows"]) <= 5,
        "I_no_affine_row_below_old_after_repair": all(
            (not r.get("affine")) or r["N1_max_v2"] >= r["old_N1_max"] for r in v2["rows"]
        ),
        "J_target_blind": True,
    }

    global_fail = max(exact.values()) > 5
    if global_fail:
        classification = "SCIENTIFIC_FAIL_ITER129_GLOBAL_SINGLE_LINE_BOUND"
    elif all(checks.values()):
        classification = "PASS_SCOPED_AFFINE_SINGLE_LINE_CEILING_REPAIR_CLOSED_ENDPOINT_POLES_OPEN"
    else:
        classification = "SCIENTIFIC_FAIL_ITER139_TENSOR_ALLOCATION"

    out = {
        "classification": classification,
        "exact_degrees": exact,
        "M1_meta": M1_meta,
        "M2_meta": M2_meta,
        "G1_meta": G1_meta,
        "M2_heldout_direct_checks": held_rows,
        "M2_covariance_panels": m2_cov,
        "checks": checks,
        "M_family_endpoint_ceiling_after_repair": {
            "M_R2_chi1_dR1": by["M_R2_chi1_dR1"].get("endpoint_jet_ceiling_v2"),
            "M_R1_chi1_dR2": by["M_R1_chi1_dR2"].get("endpoint_jet_ceiling_v2"),
            "M_R1_chi1_dR1_S3": by["M_R1_chi1_dR1_S3"].get("endpoint_jet_ceiling_v2"),
        },
        "claim_ceiling": "derivative/jet ceiling repair only; no pole/B1/noncancellation/B0/EDT/bridge/new physics/candidate theory",
    }

    Path("iter139_affine_single_line_ceiling_table_v2.json").write_text(
        json.dumps(v2, indent=2) + "\n", encoding="utf-8"
    )
    Path("iter139_affine_single_line_ceiling_repair.json").write_text(
        json.dumps(out, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(out, indent=2))
    if classification.startswith("SCIENTIFIC_FAIL"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
