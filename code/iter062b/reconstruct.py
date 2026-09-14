#!/usr/bin/env python3
"""ITER062B source-faithful restricted quantum-cuboid numerical reconstruction.

Frozen by prereg/ITER062B_RC008_RESTRICTED_HYPERCUBOID_COARSE_FINE_NUMERICAL_RECONSTRUCTION_2026-09-14.md
before scientific execution.
"""
import argparse, json, math
from pathlib import Path
import numpy as np
from scipy.stats import qmc

ALPHAS=np.array([0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80],dtype=float)
SEEDS=[104729,130363,154858]
POWERS=[12,14,16]
CENTRAL={0.55,0.60,0.65,0.70}
BOUNDARIES={
    'B0':(1.0,1.0,1.0,1.0),
    'B1':(1.0,1.0,1.0,3.0),
    'B2':(3.0,1.0,1.0,1.0),
    'B3':(3.0,5.0,1.0,1.0),
}

def p3(a,b,c):
    return (a+b)*(b+c)*(a+c)

def det_h(j):
    j1,j2,j3,j4,j5,j6=[np.asarray(x,dtype=float) for x in j]
    I=1j
    f1=j1*j1*(j2+j4)+j2*j4*(j2+j4)+j1*(j2*j2+(1+I)*j2*j4+j4*j4)
    f2=j1*j1*(j3+j5)+j3*j5*(j3+j5)+j1*(j3*j3+(1+I)*j3*j5+j5*j5)
    f3=j3*j4*j5+j2*(j4*j5+j3*(j4+j5))
    f4=j2*j2*(j3+j6)+j3*j6*(j3+j6)+j2*(j3*j3+(1+I)*j3*j6+j6*j6)
    f5=j4*j4*(j5+j6)+j5*j6*(j5+j6)+j4*(j5*j5+(1+I)*j5*j6+j6*j6)
    f6=j3*j4*j6+j1*(j4*j6+j3*(j4+j6))
    f7=j2*j5*j6+j1*(j5*j6+j2*(j5+j6))
    return 2.0*f1*f2*f3*f4*f5*f6*f7

def area_map(x,y,z,t, malformed=False):
    j1=y*z; j2=x*y; j3=x*z; j4=y*t; j5=z*t; j6=x*t
    if malformed:
        j6=x*y
    return (j1,j2,j3,j4,j5,j6)

def log_amp_parts_from_spins(j):
    """Return base and alpha coefficient for source large-j dressed amplitude.

    Variable-independent gamma/numeric constants are omitted because every reported
    quantity is a normalized expectation at fixed boundary and alpha.
    """
    j1,j2,j3,j4,j5,j6=j
    tiny=np.finfo(float).tiny
    dh=det_h(j)
    bv=2.0*np.real(1.0/np.sqrt(dh))
    edge=p3(j1,j4,j5)*p3(j3,j6,j5)*p3(j2,j6,j4)*p3(j2,j3,j1)
    base=np.log(np.maximum(edge,tiny))+2.0*np.log(np.maximum(np.abs(bv),tiny))
    coeff=2.0*(np.log(j1)+np.log(j2)+np.log(j3)+np.log(j4)+np.log(j5)+np.log(j6))
    return base,coeff

def log_fp(x,y,z,t):
    j1,j2,j3,j4,_,_=area_map(x,y,z,t)
    term=(j1**4*(j2*j2+j3*j3)*(j2*j2+j4*j4)
          +j3*j3*(j2*j2+j3*j3)*j4*j4*(j2*j2+j4*j4)
          +j1*j1*(j3*j3+j4*j4)*(j2**4+j3*j3*j4*j4))
    costh=(j1*j1*j2*j2)/np.sqrt(term)
    jac=x*y*y*z
    return np.log(jac)-np.log(costh)

def local_parts(x,y,z,t, malformed=False):
    b,c=log_amp_parts_from_spins(area_map(x,y,z,t,malformed=malformed))
    return b+log_fp(x,y,z,t),c

def weighted_stats(base,coeff,obs):
    out=[]
    finite_base=np.isfinite(base)&np.isfinite(coeff)&np.isfinite(obs)
    for a in ALPHAS:
        lw=base+a*coeff
        finite=finite_base&np.isfinite(lw)
        frac=float(np.mean(finite))
        if not np.any(finite):
            out.append({'alpha':float(a),'value':None,'ess':0.0,'ess_fraction':0.0,'finite_fraction':frac})
            continue
        z=lw[finite]; o=obs[finite]; m=float(np.max(z)); w=np.exp(z-m)
        sw=float(np.sum(w)); sw2=float(np.sum(w*w))
        val=float(np.sum(w*o)/sw)
        ess=sw*sw/sw2
        out.append({'alpha':float(a),'value':val,'ess':ess,'ess_fraction':float(ess/len(base)),'finite_fraction':frac})
    return out

def coarse_samples(boundary,seed,m):
    X,Y,Z,T=boundary; n=2**m
    u=qmc.Sobol(d=1,scramble=True,seed=seed).random_base2(m=m)[:,0]
    total_t=2.0*T; t1=total_t*u; t2=total_t-t1
    b1,c1=local_parts(X,Y,Z,t1); b2,c2=local_parts(X,Y,Z,t2)
    base=b1+b2; coeff=c1+c2
    v1=X*Y*Z*t1; vtot=X*Y*Z*total_t
    obs=(v1-0.5*vtot)**2
    return weighted_stats(base,coeff,obs)

def fine_samples(boundary,seed,m):
    X,Y,Z,T=boundary; n=2**m
    u=qmc.Sobol(d=6,scramble=True,seed=seed).random_base2(m=m)
    xcut=X*u[:,0]; ycut=Y*u[:,1]; zcut=Z*u[:,2]
    xs=[xcut,X-xcut]; ys=[ycut,Y-ycut]; zs=[zcut,Z-zcut]
    tc=np.sort((2.0*T)*u[:,3:6],axis=1)
    ts=[tc[:,0],tc[:,1]-tc[:,0],tc[:,2]-tc[:,1],2.0*T-tc[:,2]]
    base=np.zeros(n); coeff=np.zeros(n)
    for xx in xs:
        for yy in ys:
            for zz in zs:
                for tt in ts:
                    b,c=local_parts(xx,yy,zz,tt); base+=b; coeff+=c
    v1=X*Y*Z*(ts[0]+ts[1]); vtot=X*Y*Z*(2.0*T)
    obs=(v1-0.5*vtot)**2
    return weighted_stats(base,coeff,obs)

def calibration():
    rng=np.random.default_rng(8675309)
    hom=[]
    for k in range(32):
        j=tuple(rng.uniform(0.6,3.2,size=6)); lam=float(rng.uniform(0.45,2.7))
        b,c=log_amp_parts_from_spins(j); bs,cs=log_amp_parts_from_spins(tuple(lam*x for x in j))
        for a in [0.50,0.65,0.80]:
            logratio=(bs+a*cs)-(b+a*c); expected=(12*a-9)*math.log(lam)
            rel=abs(math.exp(logratio-expected)-1.0)
            hom.append(rel)
    perm_errors=[]; malformed_shifts=[]; fp_ok=[]
    for k in range(24):
        dims=rng.uniform(0.7,2.9,size=4); x,y,z,t=map(float,dims)
        a=0.63
        b,c=local_parts(x,y,z,t); ref=b+a*c
        # Coordinate relabelling should preserve a geometric hypercuboid amplitude.
        vals=[]
        for perm in [(1,0,2,3),(0,2,1,3),(3,1,2,0)]:
            q=dims[list(perm)]; bp,cp=local_parts(*map(float,q)); vals.append(bp+a*cp)
        perm_errors.append(max(abs(math.exp(v-ref)-1.0) for v in vals))
        bm,cm=local_parts(x,y,z,t,malformed=True); malformed_shifts.append(abs(math.exp((bm+a*cm)-ref)-1.0))
        fp=float(log_fp(x,y,z,t)); fp_ok.append(math.isfinite(fp))
    result={
        'homogeneity_worst_relative_error':float(max(hom)),
        'homogeneity_pass':bool(max(hom)<=1e-10),
        'permutation_worst_relative_error':float(max(perm_errors)),
        'permutation_pass':bool(max(perm_errors)<=1e-10),
        'fp_positive_finite_count':int(sum(fp_ok)),
        'fp_pass':bool(all(fp_ok)),
        'malformed_detected_count':int(sum(s>=1e-3 for s in malformed_shifts)),
        'malformed_min_relative_shift':float(min(malformed_shifts)),
        'malformed_pass':bool(sum(s>=1e-3 for s in malformed_shifts)>=23),
    }
    result['pass']=all(result[x] for x in ['homogeneity_pass','permutation_pass','fp_pass','malformed_pass'])
    result['classification']='PASS_ANALYTIC_CALIBRATION' if result['pass'] else 'INVALID_IMPLEMENTATION_CALIBRATION'
    return result

def boundary_run(name):
    bd=BOUNDARIES[name]; rows=[]
    for seed in SEEDS:
        for m in POWERS:
            rows.append({'boundary':name,'coords':bd,'seed':seed,'power':m,'coarse':coarse_samples(bd,seed,m),'fine':fine_samples(bd,seed,m)})
    return {'boundary':name,'coords':bd,'alphas':ALPHAS.tolist(),'seeds':SEEDS,'powers':POWERS,'rows':rows,'claim_lock':'restricted Riemannian quantum-cuboid geometric-sector reconstruction only; zero bridge credit'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mode',choices=['calibration','boundary'],required=True); ap.add_argument('--boundary',choices=sorted(BOUNDARIES)); ap.add_argument('--out',required=True); a=ap.parse_args()
    if a.mode=='calibration': res=calibration()
    else:
        if not a.boundary: raise SystemExit('--boundary required')
        res=boundary_run(a.boundary)
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
    print(json.dumps(res if a.mode=='calibration' else {'boundary':a.boundary,'rows':len(res['rows'])},indent=2))
if __name__=='__main__': main()
