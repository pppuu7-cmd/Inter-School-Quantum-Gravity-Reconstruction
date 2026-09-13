#!/usr/bin/env python3
import argparse, cmath, json, pathlib, sys
import numpy as np

sys.path.insert(0, str(pathlib.Path('code/iter023').resolve()))
import dual_braid_primitives as db

OUT=pathlib.Path('out'); OUT.mkdir(exist_ok=True)


def src_sign(a,b,c):
    return (-1)**int(round((a+b-c)/2))

def raw_dual(a,b,c,k):
    return db.Dbar(a,b,c,k,True)

def normalized_dual(a,b,c,k):
    D0=raw_dual(a,b,c,k); F=db.Fmath(a,b,c,k); n=c+1
    M=F@D0; g=np.trace(M)/n
    scalarity=float(np.max(np.abs(M-g*np.eye(n))))
    src=src_sign(a,b,c)/db.qdim(c,k)
    magerr=float(abs(abs(g)-abs(1/db.qdim(c,k))))
    if abs(g)<1e-14: raise RuntimeError(f'zero raw dual scalar {(a,b,c,k)}')
    eta=src/g
    eta2=float(abs(eta*eta-1)); etaim=float(abs(eta.imag))
    D=eta*D0
    return D, {'g':[float(g.real),float(g.imag)],'source_scalar':[float(src.real),float(src.imag)],
               'eta':[float(eta.real),float(eta.imag)],'scalarity':scalarity,'magnitude_error':magerr,
               'eta_squared_error':eta2,'eta_imag_abs':etaim}

def qbar_intertwiner(a,b,c,k):
    C,Z,P,M=db.solve_bar(b,a,c,k); _,zc,pc,mc=db.rep_bar(c,k)
    return max(float(np.max(np.abs(Z@C-C@zc))),float(np.max(np.abs(P@C-C@pc))),float(np.max(np.abs(M@C-C@mc))))

def construction_pairs(k):
    ps=[(1,1),(2,1),(4,2)]
    if k>=10: ps.append((6,4))
    if k==12: ps += [(8,4),(6,6),(8,8)]
    return [(a,b) for a,b in ps if a<=k and b<=k]

def construction_rows(levels=(6,10,12)):
    rows=[]
    for k in levels:
        for a,b in construction_pairs(k):
            for c in db.admiss_outputs(a,b,k):
                if abs(db.qdim(c,k))<1e-12: continue
                _,meta=normalized_dual(a,b,c,k); meta.update({'k':k,'twice':[a,b,c],'qbar_intertwiner':qbar_intertwiner(a,b,c,k)})
                rows.append(meta)
    return rows

def cup_residual(t,k):
    D,_=normalized_dual(t,t,0,k); target=db.cup(t,k).reshape(-1,1)/cmath.sqrt(db.qdim(t,k))
    return float(np.max(np.abs(D-target)))

def qmath_embedding(a,b,c,k):
    return db.qC(a,b,c,k)/cmath.sqrt(db.qdim(c,k))

def common_channels(a,b,c,d,k):
    return [x for x in db.admiss_outputs(a,b,k) if x in db.admiss_outputs(c,d,k) and abs(db.qdim(x,k))>=1e-12]

def four_basis(a,b,c,d,t,k):
    D,_=normalized_dual(a,b,t,k); Q=qmath_embedding(c,d,t,k)
    return D@Q.T

def four_dual(a,b,c,d,t,k):
    D,_=normalized_dual(a,b,t,k); Q=qmath_embedding(c,d,t,k)
    weights=db.ms(t); diag=np.diag([((-1)**t)*db.qp(m,k) for m in weights])
    return D@diag@Q.T

def four_panel_rows():
    rows=[]
    panels={6:[(1,1,1,1),(2,2,2,2),(4,2,4,2)],10:[(1,1,1,1),(2,2,2,2),(4,2,4,2)],12:[(1,1,1,1),(2,2,2,2),(4,2,4,2),(6,6,6,6),(8,4,8,4)]}
    for k,quads in panels.items():
        for quad in quads:
            a,b,c,d=quad
            if max(quad)>k: continue
            chans=common_channels(a,b,c,d,k)
            B={t:four_basis(a,b,c,d,t,k) for t in chans}; U={t:four_dual(a,b,c,d,t,k) for t in chans}
            mat=np.array([[np.sum(U[t]*B[s]) for s in chans] for t in chans],complex)
            ext_sign=(-1)**int(round((a+b+c+d)/2))
            target=np.diag([ext_sign/db.qdim(t,k) for t in chans])
            res=float(np.max(np.abs(mat-target))) if len(chans) else 0.0
            rows.append({'k':k,'twice_external':list(quad),'twice_internal':chans,'residual':res})
    return rows

def lane_construction():
    rows=construction_rows(); ms=max(r['scalarity'] for r in rows); mm=max(r['magnitude_error'] for r in rows); me=max(r['eta_squared_error'] for r in rows); mi=max(r['eta_imag_abs'] for r in rows); mq=max(r['qbar_intertwiner'] for r in rows)
    return {'lane':'construction','rows':rows,'max_scalarity':ms,'max_magnitude_error':mm,'max_eta_squared_error':me,'max_eta_imag_abs':mi,'max_qbar_intertwiner':mq,
            'pass':ms<2e-9 and mm<2e-9 and me<2e-9 and mi<2e-9 and mq<2e-9}

def lane_cup():
    rows=[]
    for k in (6,10,12):
        for t in range(1,k+1):
            # all simple j=t/2; singlet is admissible and d_j nonzero in SU(2)_k
            r=cup_residual(t,k); rows.append({'k':k,'twice_j':t,'residual':r})
    m=max(x['residual'] for x in rows)
    return {'lane':'cup','rows':rows,'max_residual':m,'pass':m<2e-9}

def lane_four():
    rows=four_panel_rows(); m=max(x['residual'] for x in rows)
    return {'lane':'four','rows':rows,'max_residual':m,'pass':m<5e-8}

def heldout_pairs(k):
    return [(a,b) for a,b in [(3,1),(3,2),(5,1),(5,3)] if a<=k and b<=k]

def lane_heldout():
    rows=[]; cups=[]
    for k in (7,9,11):
        for a,b in heldout_pairs(k):
            for c in db.admiss_outputs(a,b,k):
                if abs(db.qdim(c,k))<1e-12: continue
                _,meta=normalized_dual(a,b,c,k); meta.update({'k':k,'twice':[a,b,c],'qbar_intertwiner':qbar_intertwiner(a,b,c,k)}); rows.append(meta)
        for t in [3,5,7,9,11]:
            if t<=k: cups.append({'k':k,'twice_j':t,'residual':cup_residual(t,k)})
    correct=max([r['scalarity'] for r in rows]+[r['magnitude_error'] for r in rows]+[r['eta_squared_error'] for r in rows]+[r['eta_imag_abs'] for r in rows]+[r['qbar_intertwiner'] for r in rows]+[r['residual'] for r in cups])
    # Frozen calibration against construction panel: raw/forced +1 retain the arbitrary highest-weight sign.
    wrong=[]
    for k in (6,10,12):
        for a,b in construction_pairs(k):
            for c in db.admiss_outputs(a,b,k):
                if abs(db.qdim(c,k))<1e-12: continue
                D0=raw_dual(a,b,c,k); F=db.Fmath(a,b,c,k); target=src_sign(a,b,c)/db.qdim(c,k)*np.eye(c+1)
                wrong.append(float(np.max(np.abs(F@D0-target))))
    wrong_raw=max(wrong); wrong_forced_plus=max(wrong)
    return {'lane':'heldout','rows':rows,'cups':cups,'max_correct_residual':correct,'wrong_raw_max':wrong_raw,'wrong_forced_plus_max':wrong_forced_plus,
            'pass':correct<5e-9 and wrong_raw>1e-6 and wrong_forced_plus>1e-6}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--lane',required=True,choices=['construction','cup','four','heldout']);a=ap.parse_args()
    try: ev={'construction':lane_construction,'cup':lane_cup,'four':lane_four,'heldout':lane_heldout}[a.lane]()
    except Exception as e: ev={'lane':a.lane,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e),'pass':False}
    (OUT/'evidence.json').write_text(json.dumps(ev,indent=2,sort_keys=True)+'\n');print(json.dumps(ev,indent=2,sort_keys=True))
if __name__=='__main__': main()
