#!/usr/bin/env python3
"""ITER140 v4 shard: one exact integer-D contraction/reconstruction payload."""
from __future__ import annotations
import json, sys
from pathlib import Path
import sympy as s
import iter140_first_mg_general_d_invariant_continuation as frozen
import iter140_first_mg_general_d_invariant_continuation_v2 as fast
import iter138_first_mg_exact_numerator_kernels as i138
import iter139_affine_single_line_ceiling_repair as i139

D=int(sys.argv[1])
labels=frozen.basis_labels(); selected,A=frozen.design_panels(); Ainv=A.inv(method='DM')
nvec=tuple([1]+[0]*(D-1)); fam={}
for name,fn in fast.FAMILIES.items():
    ys=s.Matrix([fast.to_sym(fn(fast.pad(q3,D),fast.pad(k3,D),nvec,D)) for q3,k3 in selected])
    fam[name]=list(Ainv*ys)
held_seed=[
  ((1,2,-1,3),(2,-1,1,4)),
  ((2,1,3,-2),(-1,2,4,1)),
  ((-2,3,1,2),(3,-1,2,-2)),
]
held=[]; held_ok=True
for idx,(q4,k4) in enumerate(held_seed):
    qv=tuple(list(q4[:min(4,D)])+[0]*max(0,D-4)); kv=tuple(list(k4[:min(4,D)])+[0]*max(0,D-4))
    bvals=fast.basis_values_full(qv,kv); row={'panel':idx,'q':list(qv),'k':list(kv),'basis_values':[str(x) for x in bvals]}
    for name,fn in fast.FAMILIES.items():
        direct=fast.to_sym(fn(qv,kv,nvec,D)); recon=sum(c*v for c,v in zip(fam[name],bvals)); eq=bool(direct==recon)
        held_ok &= eq; row[name]={'direct':str(direct),'reconstructed':str(recon),'equal':eq}
    held.append(row)
d4_rows=[]; d4_ok=True
if D==4:
    n4=(s.Integer(1),0,0,0)
    for q4,k4 in held_seed:
        generic={n:fast.to_sym(fn(q4,k4,(1,0,0,0),4)) for n,fn in fast.FAMILIES.items()}
        authority={
          'M_R2_chi1_dR1':s.sympify(i138.M_numerator(q4,k4,n4)),
          'M_R1_chi1_dR2':s.sympify(i139.M2_numerator(q4,k4,n4)),
          'G_R1_chi2_Gamma2_dR1':s.sympify(i138.G_numerator(q4,k4,n4)),
        }
        rr={}
        for name in fast.FAMILIES:
            eq=bool(s.cancel(generic[name]-authority[name])==0); d4_ok &= eq
            rr[name]={'generic_D4':str(generic[name]),'authority_D4':str(authority[name]),'equal':eq}
        d4_rows.append(rr)
out={
 'D':D,'basis_size':len(frozen.BASIS),'design_rank':A.rank(),
 'coefficients':{name:[str(x) for x in fam[name]] for name in fam},
 'integer_D_heldouts':held,'integer_D_heldouts_ok':bool(held_ok),
 'D4_cross_authority':d4_rows,'D4_cross_authority_ok':bool(d4_ok),
}
Path(f'iter140_D{D}.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'D':D,'heldouts_ok':held_ok,'D4_cross_ok':d4_ok,'basis_size':len(frozen.BASIS),'design_rank':A.rank()}))
if not held_ok or (D==4 and not d4_ok): raise SystemExit(1)
