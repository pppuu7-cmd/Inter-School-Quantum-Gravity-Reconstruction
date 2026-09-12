#!/usr/bin/env python3
"""RC-006 Appendix-C first-step block/SVD feasibility audit, k=12 EPRL integer sector.

No Eq.(29) amplitudes are used.  This prospectively enumerates the block support
needed by Appendix-C Eq.(C1)-(C3): pairs of fine EPRL edge sectors are grouped
by coarse (J+,J-) fusion blocks, and dense matrix-size/memory bounds are reported.
It is an implementation-feasibility prerequisite only.
"""
from fractions import Fraction
import argparse, json
from pathlib import Path

K=12; JMAX=K//2; GAMMA=Fraction(1,3)

def fuse(a,b):
    lo=abs(a-b); hi=min(a+b,K-a-b)
    return list(range(lo,hi+1)) if hi>=lo else []

def emap(l):
    jp=Fraction(1+GAMMA,2)*l; jm=Fraction(1-GAMMA,2)*l
    if jp.denominator!=1 or jm.denominator!=1: return None
    return (int(jp),int(jm))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    source=[{'l':l,'p':emap(l)[0],'m':emap(l)[1]} for l in range(JMAX+1) if emap(l) is not None]
    blocks={}
    for ia,A in enumerate(source):
      for ic,C in enumerate(source):
        for Jp in fuse(A['p'],C['p']):
          for Jm in fuse(A['m'],C['m']):
            key=(Jp,Jm)
            blocks.setdefault(key,[]).append((ia,ic))
    rows=[]
    for key,pairs in sorted(blocks.items()):
      n=len(pairs)
      rows.append({
        'Jplus':key[0],'Jminus':key[1],
        'fine_pair_dimension':n,
        'square_initial_matrix_elements_upper_bound':n*n,
        'dense_complex128_bytes_upper_bound':16*n*n,
        'simplicity_diagonal':key[0]==key[1],
        'pairs':[list(x) for x in pairs],
      })
    total_elems=sum(r['square_initial_matrix_elements_upper_bound'] for r in rows)
    maxdim=max((r['fine_pair_dimension'] for r in rows),default=0)
    nonsimple=sum(not r['simplicity_diagonal'] for r in rows)
    out={
      'test':'RC006_APPENDIX_C_FIRST_STEP_BLOCK_FEASIBILITY',
      'source':'arXiv:1609.02429 Appendix C Eq.(C1)-(C3)',
      'k':K,'gamma':'1/3','initial_eprl_edge_sectors':source,
      'coarse_block_count':len(rows),
      'non_simple_block_count':nonsimple,
      'max_initial_fine_pair_dimension_per_block':maxdim,
      'sum_square_matrix_elements_upper_bound':total_elems,
      'dense_complex128_memory_upper_bound_bytes':16*total_elems,
      'feasibility_gate_pass':bool(rows and maxdim>0 and 16*total_elems < 512*1024*1024),
      'frozen_feasibility_gate':'enumeration nonempty and naive first-step dense complex128 upper bound < 512 MiB',
      'permission_if_pass':'Authorize implementation work for Appendix-C C1/C2 on the minimal k=12 EPRL-intertwiner sector after Eq.(29) amplitude itself is source-faithfully mapped; does not authorize scientific TNR claims.',
      'claim_lock':'Support/memory planning only; no Eq.(29) amplitude, contraction value, singular spectrum, RG flow, refinement, continuum, bridge, or new physics.',
      'blocks':rows,
    }
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='blocks'},indent=2,sort_keys=True))
    if not out['feasibility_gate_pass']: raise SystemExit(2)

if __name__=='__main__': main()
