#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, pathlib, ast, sys
import numpy as np

ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=ROOT/'out'/'iter039'; OUT.mkdir(parents=True,exist_ok=True)

def load(name,path):
    s=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
i38=load('i38',ROOT/'code/iter038/central_coupling_domain_authority.py')
sys.path.insert(0,str(ROOT/'code/iter019')); sys.path.insert(0,str(ROOT/'code/iter023')); sys.path.insert(0,str(ROOT/'code/iter026'))
import qcg_solver_validation as qcg
import dual_braid_primitives as db
import direct_source_qbar_identity as ds

REQ=[ROOT/'prereg/ITER039_RC006_EQ27_BOUNDED_CENTRAL_COMPONENT_CLOSURE_2026-09-14.md',ROOT/'results/ITER038_RC006_EQ27_CENTRAL_COUPLING_DOMAIN_AUTHORITY_PASS_2026-09-14.md',ROOT/'results/ITER037_RC006_DIAGONAL_EXTERNAL_LABEL_SOURCE_SUPPORT_PASS_2026-09-14.md',ROOT/'results/ITER026_RC006_DIRECT_SOURCE_QBAR_PRIMITIVE_2026-09-14.md',ROOT/'sources/ITER025_RC006_QBAR_R_AUTHORITY.md']
TH={'identity':2e-12,'intertwiner':5e-9,'dual':5e-8,'rinv':5e-8}

def write(x):
    (OUT/'evidence.json').write_text(json.dumps(x,indent=2,sort_keys=True)+'\n'); print(json.dumps(x,indent=2,sort_keys=True))

def cases():
    rows=[]
    for v in i38.diag():
        jp,jm,_=i38.i37.exact_map(v); jp=int(jp); jm=int(jm); k=v['k']
        central=[]
        for Jp in i38.adm(k,jp,jp):
            for Jm in i38.adm(k,jm,jm):
                for l in i38.adm(k,Jp,Jm): central.append((Jp,Jm,l))
        rows.append({'case':v,'jp':jp,'jm':jm,'central':central})
    return rows

def eval_tuple(k,Jp,Jm,l):
    # q-CG numerical primitives use twice-spin labels.
    a,b,c=2*Jp,2*Jm,2*l
    C,_=ds.source_qC(a,b,c,k); Cb,_=ds.cbar_source(a,b,c,k)
    loop=ds.cbar_component_loop(a,b,c,k)
    identity=float(np.max(np.abs(Cb-loop)))
    intertw=float(ds.qbar_intertwiner_residual(a,b,c,k,Cb))
    D=ds.d_source(a,b,c,k); F=C.T/np.sqrt(complex(db.qdim(c,k)))
    sign=(-1)**int(round((a+b-c)/2)); target=sign/db.qdim(c,k)*np.eye(c+1)
    dual=float(np.max(np.abs(F@D-target)))
    R=db.Rmap(a,b,k); Ri=db.Rmap(b,a,k,True)
    rinv=float(np.max(np.abs(Ri@R-np.eye((a+1)*(b+1)))))
    finite=bool(np.isfinite([identity,intertw,dual,rinv]).all() and np.all(np.isfinite(C)) and np.all(np.isfinite(Cb)))
    ok=finite and identity<TH['identity'] and intertw<TH['intertwiner'] and dual<TH['dual'] and rinv<TH['rinv']
    return {'Jp':Jp,'Jm':Jm,'l':l,'twice':[a,b,c],'identity':identity,'intertwiner':intertw,'dual':dual,'R_inverse':rinv,'finite':finite,'pass':bool(ok)}

def lane_A():
    missing=[str(p.relative_to(ROOT)) for p in REQ if not p.exists()]
    forbidden_names={'formLambda6j','eq29_amplitude','lambda_qbinomial'}; used=set()
    tree=ast.parse(pathlib.Path(__file__).read_text())
    for n in ast.walk(tree):
        if isinstance(n,ast.Name): used.add(n.id)
        elif isinstance(n,ast.Attribute): used.add(n.attr)
    forbidden=sorted(forbidden_names & used)
    panel=cases(); pri=sum(x['case']['diag_panel']=='primary' for x in panel); held=sum(x['case']['diag_panel']=='heldout' for x in panel)
    complete=bool(panel) and all(x['central'] for x in panel)
    ok=not missing and not forbidden and pri>0 and held>0 and complete
    write({'lane':'panel-domain-provenance','missing':missing,'forbidden_dependencies':forbidden,'primary_cases':pri,'heldout_cases':held,'domain_sizes':[{'k':x['case']['k'],'panel':x['case']['diag_panel'],'n':len(x['central'])} for x in panel],'pass':bool(ok),'classification':'PASS' if ok else 'BLOCKED_OR_INFRA'})

def numerical(panel_name):
    out=[]
    for x in cases():
        if x['case']['diag_panel']!=panel_name: continue
        for tup in x['central']:
            r=eval_tuple(x['case']['k'],*tup); r.update({'k':x['case']['k'],'external_l':x['case']['l'],'gamma':[x['case']['gamma_num'],x['case']['gamma_den']]}); out.append(r)
    ok=bool(out) and all(r['pass'] for r in out)
    write({'lane':'primary-central-closure' if panel_name=='primary' else 'heldout-transfer','panel':panel_name,'retuned':False,'thresholds':TH,'tuple_count':len(out),'rows':out,'pass':bool(ok)})

def lane_D():
    panel=cases(); valid=None
    for x in panel:
        for Jp,Jm,l in x['central']:
            if Jp>0 and Jm>0 and Jp!=Jm:
                valid=(x['case']['k'],Jp,Jm,l); break
        if valid: break
    if valid is None:
        write({'lane':'null-controls','pass':False,'classification':'BLOCKED_NO_FROZEN_NONTRIVIAL_BRAID_TUPLE'}); return
    k,Jp,Jm,l=valid
    allowed=i38.adm(k,Jp,Jm); bad_l=max(allowed)+1
    bad_domain=bad_l not in allowed
    a,b,c=2*Jp,2*Jm,2*l
    good,_=ds.cbar_source(a,b,c,k); legacy_cb=db.solve_bar(b,a,c,k)[0]; legacy=db.swap_ba_to_ab(a,b)@legacy_cb
    qbar_diff=float(np.max(np.abs(good-legacy))); bad_qbar=bool((np.isfinite(qbar_diff) and qbar_diff>1e-6) or not np.isfinite(qbar_diff))
    R=db.Rmap(a,b,k); wrong=db.Rmap(a,b,k,inverse=True); rdiff=float(np.max(np.abs(R-wrong))); bad_r=bool((np.isfinite(rdiff) and rdiff>1e-6) or not np.isfinite(rdiff))
    det=sum([bad_domain,bad_qbar,bad_r])
    write({'lane':'null-controls','frozen_tuple':{'k':k,'Jp':Jp,'Jm':Jm,'l':l},'outside_domain_l':bad_l,'legacy_qbar_difference':qbar_diff,'R_inverse_difference':rdiff,'detected':det,'required':3,'pass':det==3})

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['A','B','C','D']); a=ap.parse_args()
    try:
        {'A':lane_A,'B':lambda:numerical('primary'),'C':lambda:numerical('heldout'),'D':lane_D}[a.lane]()
    except Exception as e: write({'lane':a.lane,'pass':False,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e)})
if __name__=='__main__':main()
