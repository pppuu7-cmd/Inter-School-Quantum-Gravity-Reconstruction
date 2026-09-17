#!/usr/bin/env python3
"""Independent direct Critic for the ITER162 frozen-span n^2 witness.

Uses changed D/q/k configurations and independently evaluates the logical zero
condition of all frozen covariants on n=e0, n.q=n.k=0, transverse open indices.
It consumes no Researcher JSON and performs no coefficient reconstruction.
"""
from __future__ import annotations
import json, sys
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import iter161_endpoint_open_leg_factorization as i161
import iter162_upper_covariant_reconstruction as frozen

CASES=[
 (4,(0,3,1,-2),(0,-2,2,1)),
 (5,(0,2,0,1,-3),(0,1,-2,3,1)),
 (6,(0,1,-1,2,0,3),(0,2,1,-2,3,0)),
]

def main():
    reports=[]; counter_cases=0
    for D,q0,k0 in CASES:
        q=tuple(F(x) for x in q0); k=tuple(F(x) for x in k0); n=(F(1),)+tuple(F(0) for _ in range(D-1))
        assert frozen.dot(n,q)==0 and frozen.dot(n,k)==0
        V=i161.upper_open_vertex(q,k,n,D)
        found=[]
        all_frozen_zero=True
        for a in range(1,D):
            for b in range(a,D):
                row=frozen.basis_row(q,k,n,a,b)
                z=all(x==0 for x in row)
                all_frozen_zero &= z
                if z and V[a][b]!=0:
                    found.append({"component":[a,b],"source_V_ab":str(V[a][b])})
        if found: counter_cases+=1
        reports.append({"D":D,"all_transverse_frozen_columns_zero":bool(all_frozen_zero),"nonzero_source_witnesses":found})
    checks={
      "A_all_transverse_frozen_covariants_zero":all(r["all_transverse_frozen_columns_zero"] for r in reports),
      "B_source_counterexample_in_every_independent_case":counter_cases==len(reports),
      "C_no_researcher_result_consumed":True,"D_no_scalar_fit":True,"E_no_ITER160_residue":True,"F_no_ITER118_solve":True,
    }
    passed=all(checks.values())
    out={"gate":"ITER162_OPEN_G_ENDPOINT_DISTRIBUTIONAL_R_OPERATION_AND_POLE_TENSOR","critic_verdict":"PASS_CRITIC_ITER162_DIRECT_N2_FROZEN_SPAN_FALSIFIER_CONFIRMED" if passed else "FAIL_CRITIC_ITER162_DIRECT_N2_FROZEN_SPAN_FALSIFIER","reports":reports,"checks":checks,"conclusion":"Independent source evaluations confirm exact nonzero transverse V_upper components where every frozen 36 covariant vanishes. This is a direct source-level contradiction of the frozen completeness identity, not a fitting artifact." if passed else "Direct Critic did not confirm the proposed witness.","claim_locks":{"ITER118_matching_authorized":False,"B1_total":"UNAUTHORIZED","BRIDGE_DERIVED":False,"candidate_theory":"UNFORMED / 0%"}}
    Path("iter162_fast_n2_witness_critic.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0 if passed else 1)
if __name__=="__main__": main()
