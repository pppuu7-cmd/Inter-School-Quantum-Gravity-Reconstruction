#!/usr/bin/env python3
import argparse,json
from pathlib import Path

def krange(l):
    return max(abs(l[0]-l[1]),abs(l[2]-l[3])), min(l[0]+l[1],l[2]+l[3])

def allowed(l,tk):
    lo,hi=krange(l)
    return lo<=tk<=hi and ((tk-lo)%2==0)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    rows=[]
    for D in range(4):
        ls=list(range(2,2*(1+D)+1,2))
        dvd2_ltriples=0; dvd2_k_terms=0
        for l1 in ls:
          for l2 in ls:
           for l3 in ls:
            dvd2_ltriples += 1
            A=(l1,l2,l3,2); B=(2,l3,l2,l1)
            lo=max(krange(A)[0],krange(B)[0]); hi=min(krange(A)[1],krange(B)[1])
            for tk in range(lo,hi+1):
                if tk%2==0 and allowed(A,tk) and allowed(B,tk): dvd2_k_terms+=1
        dvd3_total=0; dvd3_admissible=0
        for l1 in ls:
         for l2 in ls:
          for l3 in ls:
           for l4 in ls:
            dvd3_total += 1
            A=(2,2,l3,l4); B=(l1,l2,l3,l4); C=(2,2,l2,l1)
            if allowed(A,2) and allowed(B,2) and allowed(C,2): dvd3_admissible += 1
        rows.append({'D':D,'l_values_physical':[x/2 for x in ls],
                     'dvd2_l_triples':dvd2_ltriples,'dvd2_admissible_k_terms':dvd2_k_terms,
                     'dvd3_l_quadruples':dvd3_total,'dvd3_fixed_k1_admissible_terms':dvd3_admissible,
                     'same_support_cardinality':dvd2_k_terms==dvd3_admissible})
    special_only=(rows[0]['same_support_cardinality'] and any(not r['same_support_cardinality'] for r in rows[1:]))
    out={'test':'LORENTZIAN_EPRL_DVD_AUXILIARY_SUPPORT_COMBINATORICS',
         'rows':rows,'dl0_equal_support_cardinality_only':special_only,
         'classification':'DVD_SUPPORTS_STRUCTURALLY_DIVERGE_BEYOND_DL0' if special_only else 'DVD_SUPPORT_COMBINATORICS_INCONCLUSIVE',
         'claim_lock':'Pure SU(2) admissibility/support-count audit under the frozen symmetric boundary. No B4 values, amplitudes, convergence, refinement, continuum, bridge or novelty claim.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
