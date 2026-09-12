#!/usr/bin/env python3
"""RC008 source-derived stationary-phase Hessian kernel scaling audit.

Implements the pinned Eq:OffDiagonalHessian block formulas on the 8-node
hypercuboid boundary adjacency graph (each facet is adjacent to all except its
opposite). One SU(2) node is gauge-fixed, leaving 21 real Lie-algebra directions.
The prospective gate tests source-implied block transpose symmetry and exact
homogeneity det(H(lambda*j))/det(H(j)) = lambda^21. This is an amplitude-kernel
qualification, not the full quantum-cuboid vertex amplitude or RG flow.
"""
import argparse,json,math
from pathlib import Path
import numpy as np

N=8
OPP={0:1,1:0,2:3,3:2,4:5,5:4,6:7,7:6}
EDGES=[(a,b) for a in range(N) for b in range(a+1,N) if OPP[a]!=b]
I=np.eye(3,dtype=np.complex128)

def crossmat(n):
    x,y,z=n
    return np.array([[0,-z,y],[z,0,-x],[-y,x,0]],dtype=np.complex128)

def build(seed,scale):
    rng=np.random.default_rng(seed)
    H=np.zeros((3*N,3*N),dtype=np.complex128)
    spins={}
    normals={}
    for a,b in EDGES:
        j=scale*rng.uniform(0.5,3.0)
        n=rng.normal(size=3); n=n/np.linalg.norm(n)
        spins[(a,b)]=j; normals[(a,b)]=n; normals[(b,a)]=-n
        P=I-np.outer(n,n)
        Hab=0.5*j*(P-1j*crossmat(n))
        Hba=0.5*j*(P+1j*crossmat(n))
        H[3*a:3*a+3,3*b:3*b+3]=Hab
        H[3*b:3*b+3,3*a:3*a+3]=Hba
    for a in range(N):
        D=np.zeros((3,3),dtype=np.complex128)
        for b in range(N):
            if a==b or OPP[a]==b: continue
            key=(min(a,b),max(a,b)); j=spins[key]; n=normals[(a,b)]
            D += -0.5*j*(I-np.outer(n,n))
        H[3*a:3*a+3,3*a:3*a+3]=D
    # Fix node 0 SU(2) gauge: delete its 3 Lie-algebra directions.
    Hr=H[3:,3:]
    return H,Hr

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--seed',type=int,required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
    scales=[0.5,0.8,1.0,1.7,3.0,5.0]
    H1,R1=build(a.seed,1.0)
    # Whole Hessian must be symmetric under combined (aI)<->(bJ), not Hermitian.
    symerr=float(np.max(np.abs(H1-H1.T)))
    sign1,logdet1=np.linalg.slogdet(R1)
    nonsingular=bool(abs(sign1)>0 and np.isfinite(logdet1))
    errs=[]; rows=[]
    for s in scales:
        H,R=build(a.seed,s)
        sign,ld=np.linalg.slogdet(R)
        observed=float(ld-logdet1)
        expected=21.0*math.log(s)
        err=abs(observed-expected)
        errs.append(err); rows.append({'scale':s,'logdet_ratio':observed,'expected_21logscale':expected,'abs_error':err})
    # independent direct linear-homogeneity control
    _,R2=build(a.seed,2.0)
    linerr=float(np.max(np.abs(R2-2.0*R1))/max(1.0,float(np.max(np.abs(R1)))))
    ok=nonsingular and symerr<=1e-12 and linerr<=1e-12 and max(errs)<=1e-9
    out={'test':'RC008_SOURCE_HESSIAN_KERNEL_SCALING','seed':a.seed,'node_count':N,'edge_count':len(EDGES),'gauge_fixed_dimension':21,'source_equation':'Eq:OffDiagonalHessian','symmetry_error':symerr,'linear_homogeneity_error':linerr,'nonsingular_gauge_fixed_fixture':nonsingular,'scale_rows':rows,'max_logdet_scaling_error':max(errs),'frozen_thresholds':{'symmetry':1e-12,'linear_homogeneity':1e-12,'logdet_scaling':1e-9},'frozen_gate_pass':ok,'classification_if_pass':'PASS_SOURCE_DERIVED_STATIONARY_PHASE_HESSIAN_KERNEL_HOMOGENEITY_ONLY','claim_lock':'Not full vertex amplitude, not RG/refinement, not BRIDGE_DERIVED.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='scale_rows'},indent=2,sort_keys=True))
    if not ok: raise SystemExit(2)
if __name__=='__main__': main()
