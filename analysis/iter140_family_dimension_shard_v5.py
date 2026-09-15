#!/usr/bin/env python3
"""ITER140 v5 shard: one exact family in one integer dimension.

Scientific predicates are identical to frozen ITER140. D=4 authority is checked
against hash-pinned successful ITER138/139 terminal artifact values, avoiding any
re-execution of their expensive symbolic tensor paths.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
import sympy as s
import iter140_first_mg_general_d_invariant_continuation as frozen
import iter140_first_mg_general_d_invariant_continuation_v2 as fast

D=int(sys.argv[1]); family=sys.argv[2]
if D not in range(3,11): raise SystemExit('D must be 3..10')
if family not in fast.FAMILIES: raise SystemExit(f'unknown family {family}')
fn=fast.FAMILIES[family]
labels=frozen.basis_labels(); selected,A=frozen.design_panels(); Ainv=A.inv(method='DM')
nvec=tuple([1]+[0]*(D-1))
ys=s.Matrix([fast.to_sym(fn(fast.pad(q3,D),fast.pad(k3,D),nvec,D)) for q3,k3 in selected])
coeff=list(Ainv*ys)
held_seed=[
  ((1,2,-1,3),(2,-1,1,4)),
  ((2,1,3,-2),(-1,2,4,1)),
  ((-2,3,1,2),(3,-1,2,-2)),
]
held=[]; held_ok=True
for idx,(q4,k4) in enumerate(held_seed):
    qv=tuple(list(q4[:min(4,D)])+[0]*max(0,D-4)); kv=tuple(list(k4[:min(4,D)])+[0]*max(0,D-4))
    bvals=fast.basis_values_full(qv,kv)
    direct=fast.to_sym(fn(qv,kv,nvec,D)); recon=sum(c*v for c,v in zip(coeff,bvals)); eq=bool(direct==recon)
    held_ok &= eq
    held.append({'panel':idx,'q':list(qv),'k':list(kv),'basis_values':[str(x) for x in bvals],
                 'direct':str(direct),'reconstructed':str(recon),'equal':eq})

authority_ok=True; authority_rows=[]
if D==4:
    manifest=json.loads(Path('analysis/iter140_d4_terminal_authority_manifest.json').read_text())
    for idx,row in enumerate(held):
        expected=s.sympify(manifest['panels'][idx][family]); observed=s.sympify(row['direct'])
        eq=bool(observed==expected); authority_ok &= eq
        authority_rows.append({'panel':idx,'observed':str(observed),'terminal_authority':str(expected),'equal':eq})

out={'D':D,'family':family,'basis_size':len(frozen.BASIS),'design_rank':A.rank(),
     'coefficients':[str(x) for x in coeff],
     'heldouts':held,'heldouts_ok':bool(held_ok),
     'D4_terminal_authority':authority_rows,'D4_terminal_authority_ok':bool(authority_ok),
     'authority_manifest':'analysis/iter140_d4_terminal_authority_manifest.json'}
name=family.replace('/','_')
Path(f'iter140_v5_D{D}_{name}.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'D':D,'family':family,'heldouts_ok':held_ok,'D4_authority_ok':authority_ok,'design_rank':A.rank()}),flush=True)
if not held_ok or (D==4 and not authority_ok): raise SystemExit(1)
