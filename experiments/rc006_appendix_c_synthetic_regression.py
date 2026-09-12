#!/usr/bin/env python3
"""Response-blind regression for the RC-006 Appendix-C block/SVD plumbing.

Uses deterministic synthetic matrices on the exact k=12,gamma=1/3 block support.
No Eq.(29) amplitudes or target singular values enter.  It verifies block isolation,
SVD ordering, exact full-rank reconstruction, Eckart-Young rank-one residual and
phase/sign-insensitive projector reproducibility.
"""
from fractions import Fraction
from pathlib import Path
import argparse, json, math
import numpy as np
K=12; JMAX=6; GAMMA=Fraction(1,3)

def fuse(a,b):
    lo=abs(a-b); hi=min(a+b,K-a-b)
    return list(range(lo,hi+1)) if hi>=lo else []

def emap(l):
    p=Fraction(1+GAMMA,2)*l; m=Fraction(1-GAMMA,2)*l
    return None if p.denominator!=1 or m.denominator!=1 else (int(p),int(m))

def block_dims():
    src=[(l,*emap(l)) for l in range(JMAX+1) if emap(l) is not None]
    b={}
    for ia,(_,pa,ma) in enumerate(src):
      for ic,(_,pc,mc) in enumerate(src):
        for Jp in fuse(pa,pc):
          for Jm in fuse(ma,mc): b.setdefault((Jp,Jm),[]).append((ia,ic))
    return {k:len(v) for k,v in b.items()}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--seed',type=int,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    dims=block_dims(); rng=np.random.default_rng(a.seed)
    rows=[]; full_ok=True; ey_ok=True; order_ok=True; proj_ok=True
    for key,n in sorted(dims.items()):
      A=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
      U,s,Vh=np.linalg.svd(A,full_matrices=False)
      rec=(U*s)@Vh
      rel=np.linalg.norm(rec-A)/max(np.linalg.norm(A),1e-30)
      full_ok &= rel < 1e-12
      order_ok &= bool(np.all(s[:-1]+1e-14 >= s[1:]))
      A1=s[0]*np.outer(U[:,0],Vh[0,:])
      resid=np.linalg.norm(A-A1)
      tail=math.sqrt(float(np.sum(s[1:]**2)))
      # For dim=1 the exact Eckart-Young tail is mathematically zero, so a
      # relative error is undefined. Preserve the original 1e-11 relative
      # gate whenever tail is nonzero; use a strict 1e-12 absolute machine
      # residual only on the exact-zero-tail branch.
      if tail <= 1e-14:
          eyerr_abs=abs(resid-tail)
          eyerr_rel=None
          ey_pass=eyerr_abs < 1e-12
      else:
          eyerr_abs=abs(resid-tail)
          eyerr_rel=eyerr_abs/tail
          ey_pass=eyerr_rel < 1e-11
      ey_ok &= ey_pass
      p=U[:,[0]]@U[:,[0]].conj().T
      phase=np.exp(1j*0.731)
      up=U[:,[0]]*phase
      pp=up@up.conj().T
      perr=np.linalg.norm(p-pp)
      proj_ok &= perr < 1e-12
      rows.append({'Jplus':key[0],'Jminus':key[1],'dim':n,'full_reconstruction_relerr':rel,
                   'rank1_eckart_young_abs_err':eyerr_abs,
                   'rank1_eckart_young_relerr':eyerr_rel,
                   'rank1_eckart_young_zero_tail_branch':tail <= 1e-14,
                   'rank1_eckart_young_pass':bool(ey_pass),
                   'projector_phase_invariance_err':perr,
                   'singular_values':[float(x) for x in s]})
    out={'test':'RC006_APPENDIX_C_SYNTHETIC_REGRESSION','seed':a.seed,'block_count':len(rows),
         'full_reconstruction_pass':bool(full_ok),'singular_order_pass':bool(order_ok),
         'rank1_eckart_young_pass':bool(ey_ok),'projector_phase_invariance_pass':bool(proj_ok),
         'all_pass':bool(full_ok and order_ok and ey_ok and proj_ok),'blocks':rows,
         'numerical_amendment':'For mathematically zero Eckart-Young tail (dim=1), use absolute residual <1e-12; all nonzero tails retain original relative-error <1e-11 gate.',
         'claim_lock':'Response-blind numerical plumbing test only; contains no Eq.(29) amplitude and no scientific TNR result.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='blocks'},indent=2,sort_keys=True))
    if not out['all_pass']: raise SystemExit(2)
if __name__=='__main__': main()
