#!/usr/bin/env python3
"""ITER148 parallel implementation: one frozen tau production shard."""
from __future__ import annotations
import json, sys
from pathlib import Path
import sympy as s
import iter148_m3_full_invariant_bubble_reduced_numerator as base

j=int(sys.argv[1])
if j<0 or j>8: raise SystemExit('tau index must be 0..8')
t=s.Rational(j,8)
selected,A=base.design_panels(); Ainv=A.inv(method='DM'); n0=(s.Integer(1),0,0,0)
ys=s.Matrix([base.numerator_fast(q,k,n0,t)[0] for q,k in selected])
coeff=list(Ainv*ys)
held_seed=[
  ((1,2,-1,3),(2,-1,1,4),(1,0,0,0)),
  ((2,1,3,-2),(-1,2,4,1),(0,1,0,0)),
  ((-2,3,1,2),(3,-1,2,-2),(0,0,1,0)),
]
held=[]; held_ok=True
for idx,(q0,k0,nv0) in enumerate(held_seed):
    q=tuple(map(s.Integer,q0)); k=tuple(map(s.Integer,k0)); nv=tuple(map(s.Integer,nv0))
    direct=base.numerator_fast(q,k,nv,t)[0]
    recon=sum(c*v for c,v in zip(coeff,base.basis_values(q,k,nv)))
    eq=base.exact_zero(direct-recon); held_ok &= eq
    held.append({'panel':idx,'direct':str(direct),'invariant':str(recon),'equal':bool(eq)})
out={'tau_index':j,'tau':str(t),'basis_size':len(base.BASIS),'design_rank':A.rank(),
     'coefficients':[str(x) for x in coeff],'training_heldouts':held,'training_heldouts_ok':bool(held_ok)}
Path(f'iter148_tau_{j}.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'tau_index':j,'tau':str(t),'design_rank':A.rank(),'heldouts_ok':bool(held_ok)}))
if not held_ok or A.rank()!=45: raise SystemExit(1)
