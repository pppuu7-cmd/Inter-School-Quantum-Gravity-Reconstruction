#!/usr/bin/env python3
"""Fast exact scientific witness against the frozen ITER162 36-column span.

Set n=e0 and choose q0=k0=0, so a=n.q=b=n.k=0. For any open tensor component
V_ij with i,j != 0, every one of the prospectively frozen 36 covariants vanishes:
- tangent-neutral seeds require scalar tangent count two, hence a/b factors;
- q_(a n_b), k_(a n_b), n_a n_b vanish when neither free index is 0.
Thus the frozen span predicts V_ij=0 identically on this submanifold.
A single exact nonzero source-derived V_ij is a basis-independent counterexample,
with no coefficient fit, rank threshold, scalar inversion, or residue input.
"""
from __future__ import annotations
import json, sys
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import iter161_endpoint_open_leg_factorization as i161
import iter162_upper_covariant_reconstruction as basis

CASES=[
 (4,(0,1,2,0),(0,2,-1,1)),
 (4,(0,2,-1,3),(0,-1,2,2)),
 (5,(0,1,2,-1,0),(0,2,1,0,-2)),
]

def main():
    rows=[]; witness_count=0
    for D,q0,k0 in CASES:
        q=tuple(F(x) for x in q0); k=tuple(F(x) for x in k0); n=(F(1),)+tuple(F(0) for _ in range(D-1))
        assert basis.dot(n,q)==0 and basis.dot(n,k)==0
        V=i161.upper_open_vertex(q,k,n,D)
        per=[]
        for a in range(1,D):
            for b in range(a,D):
                frozen=[basis.basis_row(q,k,n,a,b)[j] for j in range(len(basis.COLS))]
                all_zero=all(x==0 for x in frozen)
                source=V[a][b]
                if all_zero and source!=0: witness_count+=1
                per.append({"component":[a,b],"all_36_frozen_columns_zero":bool(all_zero),"source_V_ab":str(source),"is_counterexample":bool(all_zero and source!=0)})
        rows.append({"D":D,"q":[str(x) for x in q],"k":[str(x) for x in k],"a_n_dot_q":"0","b_n_dot_k":"0","components":per})
    checks={
      "A_all_tested_non_n_components_have_frozen_span_zero":all(x["all_36_frozen_columns_zero"] for r in rows for x in r["components"]),
      "B_at_least_one_exact_nonzero_source_counterexample":witness_count>0,
      "C_counterexample_repeated_across_multiple_cases":sum(any(x["is_counterexample"] for x in r["components"]) for r in rows)>=2,
      "D_no_fit_or_scalar_inverse":True,"E_no_ITER160_residue":True,"F_no_ITER118_solve":True,
    }
    passed=all(checks.values())
    out={"gate":"ITER162_OPEN_G_ENDPOINT_DISTRIBUTIONAL_R_OPERATION_AND_POLE_TENSOR","classification":"SCIENTIFIC_FAIL_ITER162_FROZEN_TENSOR_COVARIANCE_OR_SUPPORT_IDENTITY_FALSE" if passed else "INCONCLUSIVE_ITER162_FAST_N2_WITNESS","witness_count":witness_count,"cases":rows,"checks":checks,"failed_identity":"Frozen 36-column span is complete for source-derived V_upper_ab under its explicit tangent-count construction.","mechanism":"Internal contraction of the two microscopic tangent vectors can produce n^2=1 times tangent-neutral open-tensor covariants, which survive when a=b=0 and free indices are transverse to n; the frozen 36 span vanishes there.","post_outcome_repair_authorized":False,"claim_locks":{"ITER118_matching_authorized":False,"B1_total":"UNAUTHORIZED","BRIDGE_DERIVED":False,"candidate_theory":"UNFORMED / 0%"}}
    Path("iter162_fast_n2_witness.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0 if passed else 1)
if __name__=="__main__": main()
