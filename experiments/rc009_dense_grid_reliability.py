#!/usr/bin/env python3
"""Independent numerical-reliability audit for the RC-009 isotemporal integral.

This intentionally does NOT use Cuba/Cuhre. It evaluates the same scan-center
log weight on deterministic midpoint grids with two resolutions and uses
log-sum-exp normalization. The goal is to diagnose narrow/boundary peaks and
whether a low-evaluation cubature result can be trusted.

It is a numerical control, not a replacement for source-defined cubature.
"""
from __future__ import annotations
import argparse, cmath, json, math
from pathlib import Path

ALPHA=0.677
G=0.0037
LAMBDA=0.008
GAMMA=0.5
HTOTAL=6.0
JMIN=0.01
JMAXS=[8.0,10.0,12.0]
COARSE_NS=[4001,16001]
FINE_NS=[161,321]


def geom(j0,j1,H):
    s=math.sqrt(j0)+math.sqrt(j1); d=j1-j0
    k=0.5*math.sqrt(H*H*s*s+0.5*d*d)
    c=d/(4*k)
    if abs(c)>=1/math.sqrt(2): return None
    phi=math.acos(max(-1,min(1,c)))
    K2=-math.cos(2*phi)
    if K2<=0: return None
    K=math.sqrt(K2)
    Q=2+(j0+j1)/(2*k)
    it=1/math.tan(phi)
    if abs(it)>1+1e-12: return None
    theta=math.acos(max(-1,min(1,it)))
    st=math.acos(max(-1,min(1,math.cos(theta)**2)))
    SR=6*j0*(math.pi/2-theta)+6*j1*(math.pi/2-(math.pi-theta))+12*k*(math.pi/2-st)
    V4=k*k*K*(Q-2)
    return k,K,Q,SR,V4,phi


def jac(j0,j1,H):
    s=math.sqrt(j0)+math.sqrt(j1); d=j1-j0
    return H*s*s/math.sqrt(4*H*H*s*s+2*d*d)


def logamp(j0,j1,H):
    g=geom(j0,j1,H)
    if g is None: return -math.inf
    k,K,Q,SR,V4,phi=g
    x=1+K*K-2*Q
    D=(j0**3*j1**3*k**15/16)*K*(K-1j*K*K+1j*Q)**3*x**3*(K+1j)**6*(K-3j)**2*(1+3*K*K-2*Q-2j*K*(Q-1))**3
    ad=abs(D)
    if not ad>0: return -math.inf
    B=ad/((1+K*K)**3*abs(1+K*K-2*Q)**6)
    if not B>0: return -math.inf
    varphi=cmath.phase(D)
    branch=math.cos(SR/G+varphi)+math.cos(GAMMA*SR/G-LAMBDA*V4/G)
    ab=abs(branch)
    if ab<=1e-300: return -math.inf
    return (3*ALPHA-1.5)*(math.log(j0)+math.log(j1))+6*(ALPHA-1)*math.log(k)-math.log(B)+math.log(ab)


def coarse_lw(j):
    a=1/9; H=HTOTAL/2
    l1=logamp(a,j,H); l2=logamp(j,a,H)
    J1=jac(a,j,H); J2=jac(j,a,H)
    if not math.isfinite(l1+l2): return -math.inf
    return math.log(J1)+math.log(J2)+27*l1+27*l2


def fine_lw(j1,j2):
    a=1/16; H=HTOTAL/3
    ls=(logamp(a,j1,H),logamp(j1,j2,H),logamp(j2,a,H))
    if not all(math.isfinite(x) for x in ls): return -math.inf
    Js=(jac(a,j1,H),jac(j1,j2,H),jac(j2,a,H))
    return sum(math.log(x) for x in Js)+64*sum(ls)


def coarse_obs(j):
    a=1/9; H=HTOTAL/2
    V3=27*j**1.5
    V4=27*(geom(a,j,H)[4]+geom(j,a,H)[4])
    return V3,V3*V3,V4


def fine_obs(j1,j2):
    a=1/16; H=HTOTAL/3
    amid=0.5*(math.sqrt(j1)+math.sqrt(j2))
    V3=64*amid**3
    V4=64*(geom(a,j1,H)[4]+geom(j1,j2,H)[4]+geom(j2,a,H)[4])
    return V3,V3*V3,V4


def weighted_summary(records,dim,jmin,jmax):
    # records: tuples (coords, logw, obs)
    m=max(r[1] for r in records)
    sw=sw2=0.0; s=[0.0,0.0,0.0]
    low=high=0.0
    for coords,lw,obs in records:
        w=math.exp(max(-745,lw-m)); sw+=w; sw2+=w*w
        for k in range(3): s[k]+=w*obs[k]
        if any((x-jmin)/(jmax-jmin)<=0.01 for x in coords): low+=w
        if any((jmax-x)/(jmax-jmin)<=0.01 for x in coords): high+=w
    mean=[x/sw for x in s]
    return {'V3':mean[0],'VarV3':mean[1]-mean[0]**2,'V4':mean[2],
            'logweight_max':m,'effective_grid_points':sw*sw/sw2,
            'low_boundary_weight_fraction':low/sw,'high_boundary_weight_fraction':high/sw}


def coarse_grid(jmax,n):
    h=(jmax-JMIN)/n; rec=[]; peak=(-math.inf,None)
    for i in range(n):
        j=JMIN+(i+0.5)*h; lw=coarse_lw(j)
        if lw>peak[0]: peak=(lw,j)
        rec.append(((j,),lw,coarse_obs(j)))
    out=weighted_summary(rec,1,JMIN,jmax)
    out.update({'n':n,'peak_j':peak[1],'peak_fraction_of_domain':(peak[1]-JMIN)/(jmax-JMIN)})
    return out


def fine_grid(jmax,n):
    h=(jmax-JMIN)/n; rec=[]; peak=(-math.inf,None,None)
    vals=[JMIN+(i+0.5)*h for i in range(n)]
    for j1 in vals:
        for j2 in vals:
            lw=fine_lw(j1,j2)
            if lw>peak[0]: peak=(lw,j1,j2)
            rec.append(((j1,j2),lw,fine_obs(j1,j2)))
    out=weighted_summary(rec,2,JMIN,jmax)
    out.update({'n':n,'peak_j1':peak[1],'peak_j2':peak[2],
                'peak_fraction_j1':(peak[1]-JMIN)/(jmax-JMIN),'peak_fraction_j2':(peak[2]-JMIN)/(jmax-JMIN)})
    return out


def rel(a,b): return abs(a-b)/max(0.5*(abs(a)+abs(b)),1e-300)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    lanes=[]
    for jm in JMAXS:
        c=[coarse_grid(jm,n) for n in COARSE_NS]
        f=[fine_grid(jm,n) for n in FINE_NS]
        shifts={}
        for lat,arr in [('coarse',c),('fine',f)]:
            shifts[lat]={k:rel(arr[0][k],arr[1][k]) for k in ('V3','VarV3','V4')}
            shifts[lat]['max_observable_resolution_shift']=max(shifts[lat].values())
        reliable=(shifts['coarse']['max_observable_resolution_shift']<=0.05 and shifts['fine']['max_observable_resolution_shift']<=0.05)
        lanes.append({'jmax':jm,'coarse_resolutions':c,'fine_resolutions':f,'resolution_shifts':shifts,
                      'dense_grid_resolution_stable_le_5pct':reliable})
    out={'test':'RC009_DENSE_GRID_RELIABILITY_AUDIT','status':'PASS_EXECUTION',
         'parameters':{'alpha':ALPHA,'G':G,'Lambda':LAMBDA,'jmin':JMIN,'jmaxs':JMAXS},
         'coarse_ns':COARSE_NS,'fine_ns':FINE_NS,'lanes':lanes,
         'all_cutoffs_resolution_stable_le_5pct':all(x['dense_grid_resolution_stable_le_5pct'] for x in lanes),
         'interpretation_lock':'Independent deterministic midpoint-grid/log-sum-exp diagnostic. It checks peak localization, cutoff domination and resolution sensitivity; it is not a substitute for source-defined Cuba integration and does not by itself establish cylindrical consistency.'}
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
