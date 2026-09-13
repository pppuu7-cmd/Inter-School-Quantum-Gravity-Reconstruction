#!/usr/bin/env python3
import argparse, cmath, json, math, pathlib, sys
import numpy as np

sys.path.insert(0, str(pathlib.Path('code/iter019').resolve()))
import qcg_solver_validation as base

OUT=pathlib.Path('out'); OUT.mkdir(exist_ok=True)


def qp(e,k,sgn=1):
    if k is None: return 1+0j
    return cmath.exp(sgn*2j*math.pi*float(e)/(k+2))

def ms(t): return base.magnetic_values(t)
def qdim(t,k): return base.qnum(t+1,k)

def rep_bar(t,k):
    m=ms(t); n=t+1; j=t/2
    Z=np.diag(m.astype(complex)); P=np.zeros((n,n),complex); M=np.zeros_like(P)
    for c,x in enumerate(m):
        if x<j: P[c+1,c]=cmath.sqrt(base.qnum(j-x,k)*base.qnum(j+x+1,k))
        if x>-j: M[c-1,c]=cmath.sqrt(base.qnum(j+x,k)*base.qnum(j-x+1,k))
    return m,Z,P,M

def tensor_bar(t1,t2,k):
    m1,z1,p1,n1=rep_bar(t1,k); m2,z2,p2,n2=rep_bar(t2,k)
    I1=np.eye(t1+1); I2=np.eye(t2+1)
    km1=np.diag([qp(-x/2,k,-1) for x in m1]); kp1=np.diag([qp(x/2,k,-1) for x in m1])
    km2=np.diag([qp(-x/2,k,-1) for x in m2]); kp2=np.diag([qp(x/2,k,-1) for x in m2])
    P=np.kron(km1,p2)+np.kron(p1,kp2); M=np.kron(km1,n2)+np.kron(n1,kp2)
    Z=np.kron(I1,z2)+np.kron(z1,I2); w=np.array([a+b for a in m1 for b in m2])
    return w,Z,P,M

def solve_bar(t1,t2,t3,k):
    w,Z,P,M=tensor_bar(t1,t2,k); j=t3/2
    ix=np.where(np.isclose(w,j))[0]; ox=np.where(np.isclose(w,j+1))[0]
    A=P[np.ix_(ox,ix)] if len(ox) else np.zeros((0,len(ix)),complex)
    if A.shape[0]:
        _,s,vh=np.linalg.svd(A,full_matrices=True); r=int(np.sum(s>1e-10));
        if len(ix)-r!=1: raise RuntimeError('qbar nullspace not 1D')
        v=vh.conj().T[:,r]
    else:
        if len(ix)!=1: raise RuntimeError('qbar top weight not 1D')
        v=np.ones(1,complex)
    v=v/cmath.sqrt(v.T@v); vec=np.zeros(len(w),complex); vec[ix]=v
    st={round(j,12):vec}; m=j
    while m>-j+1e-12:
        a=cmath.sqrt(base.qnum(j+m,k)*base.qnum(j-m+1,k)); vec=M@vec/a; m-=1; st[round(m,12)]=vec
    C=np.column_stack([st[round(float(x),12)] for x in ms(t3)])
    return C,Z,P,M

def swap_ba_to_ab(t1,t2):
    S=np.zeros(((t1+1)*(t2+1),(t2+1)*(t1+1)))
    for i1 in range(t1+1):
        for i2 in range(t2+1): S[i1*(t2+1)+i2,i2*(t1+1)+i1]=1
    return S

def qC(t1,t2,t3,k): return base.solve_channel(t1,t2,t3,k)['C']
def Fmath(t1,t2,t3,k): return qC(t1,t2,t3,k).T/cmath.sqrt(qdim(t3,k))

def Dbar(t1,t2,t3,k,reverse=True):
    if reverse:
        Cb,_,_,_=solve_bar(t2,t1,t3,k); return swap_ba_to_ab(t1,t2)@Cb/cmath.sqrt(qdim(t3,k))
    Cb,_,_,_=solve_bar(t1,t2,t3,k); return Cb/cmath.sqrt(qdim(t3,k))

def cup(t,k):
    j=t/2; m=ms(t); U=np.zeros((t+1,t+1),complex)
    for i,x in enumerate(m):
        for r,y in enumerate(m):
            if abs(x+y)<1e-12: U[i,r]=((-1)**int(round(j+x)))*qp(x/2,k)
    return U

def admiss_outputs(t1,t2,k): return [t for t in range(0,k+1) if base.admissible(t1,t2,t,k)]

def dual_rows():
    rows=[]
    for k in (6,10,12):
        pairs=[(1,1),(2,1),(4,2)]
        if k==12: pairs += [(8,4),(6,6)]
        for a,b in pairs:
            if a>k or b>k: continue
            for c in admiss_outputs(a,b,k):
                F=Fmath(a,b,c,k); D=Dbar(a,b,c,k,True)
                s=(-1)**int(round((a+b-c)/2)); target=s/qdim(c,k)*np.eye(c+1)
                comp=float(np.max(np.abs(F@D-target)))
                Cg,Zb,Pb,Mb=solve_bar(b,a,c,k); _,zc,pc,mc=rep_bar(c,k)
                ir=max(float(np.max(np.abs(Zb@Cg-Cg@zc))),float(np.max(np.abs(Pb@Cg-Cg@pc))),float(np.max(np.abs(Mb@Cg-Cg@mc))))
                rows.append({'k':k,'twice':[a,b,c],'composition':comp,'intertwiner':ir})
    cups=[]
    for k in (6,10,12):
        for t in (1,2,4,6):
            if t>k: continue
            D=Dbar(t,t,0,k,True); tar=cup(t,k).reshape(-1,1)/cmath.sqrt(qdim(t,k))
            cups.append({'k':k,'twice_j':t,'residual':float(np.max(np.abs(D-tar)))})
    return rows,cups

def Rmap(a,b,k,inverse=False,omit_sign=False,wrong_bar=False):
    R=np.zeros(((b+1)*(a+1),(a+1)*(b+1)),complex)
    for c in admiss_outputs(a,b,k):
        Cab=qC(a,b,c,k)
        if wrong_bar:
            Ctop=solve_bar(b,a,c,k)[0]
        else:
            Ctop=qC(b,a,c,k)
        j1=a/2;j2=b/2;j=c/2
        ph=qp((0.5 if inverse else -0.5)*(j1*(j1+1)+j2*(j2+1)-j*(j+1)),k)
        sg=1 if omit_sign else (-1)**int(round((a+b-c)/2))
        R += sg*ph*(Ctop@Cab.T)
    return R

def rpanels():
    out=[]
    for k in (6,10,12):
        for p in [(1,1),(2,1),(4,2)]+([(6,6)] if k==12 else []):
            if p[0]<=k and p[1]<=k: out.append((k,*p))
    return out

def lane_dual():
    rows,cups=dual_rows(); mr=max(r['composition'] for r in rows); mi=max(r['intertwiner'] for r in rows); mc=max(r['residual'] for r in cups)
    return {'lane':'dual','rows':rows,'cups':cups,'max_composition':mr,'max_qbar_intertwiner':mi,'max_cup':mc,'pass':mr<2e-9 and mi<2e-9 and mc<2e-9}

def lane_R():
    rows=[]
    for k,a,b in rpanels():
        R=Rmap(a,b,k); Ri=Rmap(b,a,k,True); _,_,_,Za,Pa,Ma=base.tensor_ops(a,b,k); _,_,_,Zb,Pb,Mb=base.tensor_ops(b,a,k)
        inter=max(float(np.max(np.abs(R@Za-Zb@R))),float(np.max(np.abs(R@Pa-Pb@R))),float(np.max(np.abs(R@Ma-Mb@R))))
        inv=float(np.max(np.abs(Ri@R-np.eye((a+1)*(b+1)))))
        rows.append({'k':k,'twice_pair':[a,b],'intertwiner':inter,'inverse':inv})
    m1=max(r['intertwiner'] for r in rows); m2=max(r['inverse'] for r in rows)
    return {'lane':'R','rows':rows,'max_intertwiner':m1,'max_inverse':m2,'pass':m1<5e-9 and m2<5e-9}

def yb(a,b,c,k):
    I=lambda t:np.eye(t+1)
    L=np.kron(Rmap(b,c,k),I(a))@np.kron(I(b),Rmap(a,c,k))@np.kron(Rmap(a,b,k),I(c))
    Q=np.kron(I(c),Rmap(a,b,k))@np.kron(Rmap(a,c,k),I(b))@np.kron(I(a),Rmap(b,c,k))
    return float(np.max(np.abs(L-Q)))

def ordinary_swap(a,b): return swap_ba_to_ab(a,b).T

def R_classical(a,b):
    R=np.zeros(((b+1)*(a+1),(a+1)*(b+1)),complex)
    maxc=a+b
    for c in range(abs(a-b),maxc+1,2):
        Cab=base.solve_channel(a,b,c,None)['C']; Cba=base.solve_channel(b,a,c,None)['C']; sg=(-1)**int(round((a+b-c)/2)); R+=sg*(Cba@Cab.T)
    return R

def lane_braid():
    panels=[]
    for k in (6,10,12):
        triples=[(1,1,1),(2,1,1),(2,2,1)]
        if k>=10: triples += [(4,2,1),(4,2,2)]
        for p in triples:
            if max(p)<=k: panels.append({'k':k,'twice':list(p),'residual':yb(*p,k)})
    classical=[]
    for a,b in [(1,1),(2,1),(4,2)]: classical.append({'twice_pair':[a,b],'residual':float(np.max(np.abs(R_classical(a,b)-ordinary_swap(a,b))))})
    my=max(x['residual'] for x in panels); mc=max(x['residual'] for x in classical)
    return {'lane':'braid','yb':panels,'classical':classical,'max_yb':my,'max_classical_swap':mc,'pass':my<2e-8 and mc<2e-10}

def lane_null():
    k=12;a,b=2,1
    good=Rmap(a,b,k); _,_,_,Za,Pa,Ma=base.tensor_ops(a,b,k); _,_,_,Zb,Pb,Mb=base.tensor_ops(b,a,k)
    def inter(R): return max(float(np.max(np.abs(R@Pa-Pb@R))),float(np.max(np.abs(R@Ma-Mb@R))))
    wrong1=yb(1,1,1,12) # good baseline only
    no_sign=lambda x,y: Rmap(x,y,12,omit_sign=True)
    I=lambda t:np.eye(t+1)
    L=np.kron(no_sign(1,1),I(1))@np.kron(I(1),no_sign(1,1))@np.kron(no_sign(1,1),I(1))
    Q=np.kron(I(1),no_sign(1,1))@np.kron(no_sign(1,1),I(1))@np.kron(I(1),no_sign(1,1))
    r1=float(np.max(np.abs(L-Q)))
    r2=inter(Rmap(a,b,k,wrong_bar=True))
    F=Fmath(a,b,1,k); bad=np.conjugate(qC(a,b,1,k))/cmath.sqrt(qdim(1,k)); s=(-1)**int(round((a+b-1)/2)); r3=float(np.max(np.abs(F@bad-s/qdim(1,k)*np.eye(2))))
    # forward-source coefficient vs opposite exponent on one channel
    c=1;j1=a/2;j2=b/2;j=c/2
    goodph=qp(-.5*(j1*(j1+1)+j2*(j2+1)-j*(j+1)),k); badph=qp(.5*(j1*(j1+1)+j2*(j2+1)-j*(j+1)),k); r4=abs(goodph-badph)
    vals=[r1,r2,r3,float(r4)]; det=sum(v>1e-6 for v in vals)
    return {'lane':'null','wrong_residuals':vals,'detected':det,'required':3,'good_yb_baseline':wrong1,'pass':det>=3 and wrong1<2e-8}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--lane',required=True,choices=['dual','R','braid','null']);a=ap.parse_args()
    try: ev={'dual':lane_dual,'R':lane_R,'braid':lane_braid,'null':lane_null}[a.lane]()
    except Exception as e: ev={'lane':a.lane,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e),'pass':False}
    (OUT/'evidence.json').write_text(json.dumps(ev,indent=2,sort_keys=True)+'\n'); print(json.dumps(ev,indent=2,sort_keys=True))
if __name__=='__main__': main()
