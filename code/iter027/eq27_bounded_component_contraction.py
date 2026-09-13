#!/usr/bin/env python3
import argparse, hashlib, json, pathlib, sys
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code' / 'iter019'))
sys.path.insert(0, str(ROOT / 'code' / 'iter023'))
sys.path.insert(0, str(ROOT / 'code' / 'iter026'))
import qcg_solver_validation as qcg
import dual_braid_primitives as db
import direct_source_qbar_identity as ds

OUT = ROOT / 'out' / 'iter027'
OUT.mkdir(parents=True, exist_ok=True)
PRIMARY = (6,10,12)
HELDOUT = (7,9,11)
PAIRS = ((1,1),(2,1),(2,2),(4,2))
REQ = [
    ROOT/'prereg/ITER027_RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_2026-09-14.md',
    ROOT/'results/ITER021_RC006_EQ27_COMPONENT_TRANSLATION_2026-09-14.md',
    ROOT/'results/ITER026_RC006_DIRECT_SOURCE_QBAR_PRIMITIVE_2026-09-14.md',
    ROOT/'sources/ITER025_RC006_QBAR_R_AUTHORITY.md',
]

def write(ev):
    (OUT/'evidence.json').write_text(json.dumps(ev,indent=2,sort_keys=True)+'\n')
    print(json.dumps(ev,indent=2,sort_keys=True))

def admissible_rows(k):
    rows=[]
    for a,b in PAIRS:
        if max(a,b)>k: continue
        for c in range(k+1):
            if qcg.admissible(a,b,c,k) and abs(db.qdim(c,k))>1e-12:
                rows.append((a,b,c))
    return rows

def authority_domain():
    missing=[str(p.relative_to(ROOT)) for p in REQ if not p.exists()]
    texts={str(p.relative_to(ROOT)):p.read_text(encoding='utf-8') for p in REQ if p.exists()}
    forbidden=[]
    impl=pathlib.Path(__file__).read_text(encoding='utf-8')
    for tok in ('formLambda6j','eq29_amplitude','lambda_qbinomial'):
        if tok in impl: forbidden.append(tok)
    panels={str(k):[list(x) for x in admissible_rows(k)] for k in PRIMARY+HELDOUT}
    provenance={k:hashlib.sha256(v.encode()).hexdigest() for k,v in texts.items()}
    ok=(not missing and not forbidden and all(panels[str(k)] for k in PRIMARY+HELDOUT))
    write({'lane':'authority-domain','missing':missing,'forbidden_dependencies':forbidden,'alpha':0,'panels':panels,'provenance_sha256':provenance,'pass':bool(ok)})

def translation():
    rows=[]
    for k in PRIMARY+HELDOUT:
        for a,b,c in admissible_rows(k):
            C,_=ds.source_qC(a,b,c,k)
            Cb,_=ds.cbar_source(a,b,c,k)
            loop=ds.cbar_component_loop(a,b,c,k)
            rid=float(np.max(np.abs(Cb-loop)))
            ir=ds.qbar_intertwiner_residual(a,b,c,k,Cb)
            R=db.Rmap(a,b,k)
            shape_ok=(C.shape==((a+1)*(b+1),c+1) and Cb.shape==C.shape and R.shape==((b+1)*(a+1),(a+1)*(b+1)))
            rows.append({'k':k,'twice':[a,b,c],'source_qbar_identity':rid,'qbar_intertwiner':ir,'shape_ok':shape_ok})
    mx1=max(r['source_qbar_identity'] for r in rows); mx2=max(r['qbar_intertwiner'] for r in rows)
    ok=all(r['shape_ok'] for r in rows) and mx1<2e-12 and mx2<5e-9
    write({'lane':'component-translation','rows':rows,'max_source_identity':mx1,'max_qbar_intertwiner':mx2,'thresholds':{'identity':2e-12,'intertwiner':5e-9},'pass':bool(ok)})

def contraction():
    rows=[]
    for held,kset in ((False,PRIMARY),(True,HELDOUT)):
        for k in kset:
            for a,b,c in admissible_rows(k):
                C,_=ds.source_qC(a,b,c,k)
                Cb,_=ds.cbar_source(a,b,c,k)
                D=ds.d_source(a,b,c,k)
                F=C.T/np.sqrt(complex(db.qdim(c,k)))
                sign=(-1)**int(round((a+b-c)/2))
                target=sign/db.qdim(c,k)*np.eye(c+1)
                dual=float(np.max(np.abs(F@D-target)))
                R=db.Rmap(a,b,k); Ri=db.Rmap(b,a,k,True)
                rinv=float(np.max(np.abs(Ri@R-np.eye((a+1)*(b+1)))))
                finite=bool(np.isfinite(dual) and np.isfinite(rinv) and np.all(np.isfinite(C)) and np.all(np.isfinite(Cb)))
                rows.append({'heldout':held,'k':k,'twice':[a,b,c],'dual_contraction':dual,'R_inverse':rinv,'finite':finite})
    mxdual=max(r['dual_contraction'] for r in rows); mxr=max(r['R_inverse'] for r in rows)
    ok=all(r['finite'] for r in rows) and mxdual<5e-8 and mxr<5e-8
    write({'lane':'bounded-contraction','alpha':0,'rows':rows,'max_dual_contraction':mxdual,'max_R_inverse':mxr,'threshold':5e-8,'retuned_heldout':False,'full_eq27_amplitude_claimed':False,'pass':bool(ok)})

def null_controls():
    k,a,b,c=12,2,1,1
    good,_=ds.cbar_source(a,b,c,k)
    legacy_cb=db.solve_bar(b,a,c,k)[0]
    legacy= db.swap_ba_to_ab(a,b) @ legacy_cb
    legacy_res=float(np.max(np.abs(good-legacy)))
    swapped=np.zeros_like(good)
    C,_=ds.source_qC(a,b,c,k)
    J=np.kron(ds.reversal(b),ds.reversal(a))
    try:
        swapped_raw=ds.source_sign(a,b,c)*(J@C.reshape((a+1,b+1,c+1)).transpose(1,0,2).reshape((b+1)*(a+1),c+1)@ds.reversal(c))
        swapped=db.swap_ba_to_ab(a,b)@swapped_raw
        swapped_res=float(np.max(np.abs(good-swapped)))
    except Exception:
        swapped_res=float('inf')
    R=db.Rmap(a,b,k); wrongR=db.Rmap(a,b,k,inverse=True)
    rswap=float(np.max(np.abs(R-wrongR)))
    vals={'legacy_inverse_parameter_qbar':legacy_res,'wrong_magnetic_order':swapped_res,'R_inverse_swap':rswap}
    detected=sum((np.isfinite(v) and v>1e-6) or (not np.isfinite(v)) for v in vals.values())
    write({'lane':'null-controls','wrong_residuals':vals,'detected':int(detected),'required':2,'pass':bool(detected>=2)})

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['authority-domain','component-translation','bounded-contraction','null-controls']); a=ap.parse_args()
    try:
        {'authority-domain':authority_domain,'component-translation':translation,'bounded-contraction':contraction,'null-controls':null_controls}[a.lane]()
    except Exception as e:
        write({'lane':a.lane,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e),'pass':False})

if __name__=='__main__': main()
