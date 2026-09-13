#!/usr/bin/env python3
import argparse, importlib.util, json, math
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('iter019_qcg', ROOT/'code/iter019/qcg_solver_validation.py')
q=importlib.util.module_from_spec(spec); spec.loader.exec_module(q)
OUT=Path('out'); OUT.mkdir(exist_ok=True)

def emit(ev):
    (OUT/'evidence.json').write_text(json.dumps(ev,indent=2,sort_keys=True)+'\n')
    print(json.dumps(ev,indent=2,sort_keys=True))

def solve_rows(k, channels):
    rows=[]; mx=0.0
    for ch in channels:
        if not q.admissible(*ch,k): continue
        r=q.solve_channel(*ch,k)
        mx=max(mx,r['max_intertwiner_residual'])
        rows.append({'twice_spins':list(ch),'null_dim':r['null_dim'],'max_intertwiner_residual':r['max_intertwiner_residual'],'a9_self_residual':r['a9_self_residual']})
    return rows,mx

def lane_level():
    panels={6:[(1,3,2),(1,3,4),(2,3,1),(2,3,3),(2,3,5),(3,3,0),(3,3,2),(3,3,4),(3,3,6)],10:[(1,3,2),(1,3,4),(2,4,2),(2,4,4),(2,4,6),(5,5,0),(5,5,2),(5,5,4),(5,5,6),(5,5,8),(5,5,10)]}
    allrows=[]; mx=0.0; ok=True
    for k,chs in panels.items():
        rows,m=solve_rows(k,chs); mx=max(mx,m); ok &= bool(rows) and all(x['null_dim']==1 for x in rows)
        allrows.append({'k':k,'channels':rows})
    ok &= mx<1e-9
    return {'lane':'level-transport','panels':allrows,'max_intertwiner_residual':mx,'threshold':1e-9,'pass':bool(ok)}

def lane_cutoff():
    rows=[]; mx=0.0; failures=[]
    for k in (6,10,12):
        for t1,t2 in ((k-2,k-2),(k-1,k-1),(k,k)):
            for t3 in range(k+1):
                if not q.admissible(t1,t2,t3,k): continue
                try:
                    r=q.solve_channel(t1,t2,t3,k)
                    mx=max(mx,r['max_intertwiner_residual'])
                    rows.append({'k':k,'twice_spins':[t1,t2,t3],'null_dim':r['null_dim'],'max_intertwiner_residual':r['max_intertwiner_residual']})
                except Exception as e:
                    failures.append({'k':k,'twice_spins':[t1,t2,t3],'error':repr(e)})
    ok=bool(rows) and not failures and all(x['null_dim']==1 for x in rows) and mx<2e-8
    return {'lane':'near-cutoff','channel_count':len(rows),'channels':rows,'failures':failures,'max_intertwiner_residual':mx,'threshold':2e-8,'pass':bool(ok)}

def lane_recoupling():
    panels=[(1,1,2,2),(2,1,2,1),(2,2,1,1)]
    rows=[]; gm=go=gi=0.0; ok=True
    for k in (6,10):
        for p in panels:
            if not q.admissible(p[0],p[1],abs(p[0]-p[1]),k): pass
            left,right,Fs=q.recoupling_panel(*p,k)
            if not left or not right:
                continue
            square=len(left)==len(right)
            F0=Fs[0]
            mr=max(float(np.max(np.abs(F-F0))) for F in Fs)
            ort=max(float(np.max(np.abs(F.T@F-np.eye(F.shape[0])))) for F in Fs)
            im=max(float(np.max(np.abs(F.imag))) for F in Fs)
            gm=max(gm,mr); go=max(go,ort); gi=max(gi,im)
            rp=square and mr<5e-8 and ort<5e-8 and im<5e-8
            ok &= rp
            rows.append({'k':k,'twice_spins_j1_j2_j3_J':list(p),'left':left,'right':right,'M_independence_residual':mr,'transpose_orthogonality_residual':ort,'max_imaginary_part':im,'pass':rp})
    ok &= bool(rows)
    return {'lane':'heldout-recoupling','panels':rows,'max_M_independence_residual':gm,'max_transpose_orthogonality_residual':go,'max_imaginary_part':gi,'threshold':5e-8,'phase_or_sign_fit':False,'pass':bool(ok)}

def wrong_tensor_ops(t1,t2,k,mode):
    ms1,z1,p1,m1=q.rep(t1,k); ms2,z2,p2,m2=q.rep(t2,k)
    I1=np.eye(t1+1,dtype=complex); I2=np.eye(t2+1,dtype=complex)
    if mode=='undeformed-coproduct':
        Jp=np.kron(I1,p2)+np.kron(p1,I2); Jm=np.kron(I1,m2)+np.kron(m1,I2)
    elif mode=='flip-exponent':
        km1=np.diag([q.qpow(x/2,k) for x in ms1]); kp1=np.diag([q.qpow(-x/2,k) for x in ms1]); km2=np.diag([q.qpow(x/2,k) for x in ms2]); kp2=np.diag([q.qpow(-x/2,k) for x in ms2])
        Jp=np.kron(km1,p2)+np.kron(p1,kp2); Jm=np.kron(km1,m2)+np.kron(m1,kp2)
    else:
        def rep_class(t):
            j=t/2; ms=q.magnetic_values(t); P=np.zeros((t+1,t+1),complex); M=P.copy()
            for c,m in enumerate(ms):
                if m<j:P[c+1,c]=math.sqrt((j-m)*(j+m+1))
                if m>-j:M[c-1,c]=math.sqrt((j+m)*(j-m+1))
            return ms,P,M
        ms1,p1,m1=rep_class(t1); ms2,p2,m2=rep_class(t2)
        km1=np.diag([q.qpow(-x/2,k) for x in ms1]); kp1=np.diag([q.qpow(x/2,k) for x in ms1]); km2=np.diag([q.qpow(-x/2,k) for x in ms2]); kp2=np.diag([q.qpow(x/2,k) for x in ms2])
        Jp=np.kron(km1,p2)+np.kron(p1,kp2); Jm=np.kron(km1,m2)+np.kron(m1,kp2)
    return Jp,Jm

def control_residual(mode,k=10,ch=(2,2,2)):
    r=q.solve_channel(*ch,k); C=r['C']; _,_,p3,m3=q.rep(ch[2],k); Jp,Jm=wrong_tensor_ops(ch[0],ch[1],k,mode)
    return max(float(np.max(np.abs(Jp@C-C@p3))),float(np.max(np.abs(Jm@C-C@m3))))

def lane_null():
    ch=(2,2,2); k=10; correct=q.solve_channel(*ch,k)['max_intertwiner_residual']
    modes=['undeformed-coproduct','classical-qnumbers','flip-exponent']; vals={m:control_residual(m,k,ch) for m in modes}
    detected=sum(v>1e-6 for v in vals.values())
    ok=correct<1e-9 and detected>=2
    return {'lane':'null-calibration','correct_residual':correct,'wrong_residuals':vals,'detected_wrong_constructions':detected,'required_detected':2,'pass':bool(ok)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['level-transport','near-cutoff','heldout-recoupling','null-calibration']); a=ap.parse_args()
    try: ev={'level-transport':lane_level,'near-cutoff':lane_cutoff,'heldout-recoupling':lane_recoupling,'null-calibration':lane_null}[a.lane]()
    except Exception as e: ev={'lane':a.lane,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e)}
    emit(ev)
if __name__=='__main__': main()
