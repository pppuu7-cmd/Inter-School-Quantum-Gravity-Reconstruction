#!/usr/bin/env python3
"""RC-009 endpoint absolute-convergence audit.

Separates the bounded oscillatory branch factor from the algebraic magnitude
of the isotemporal scan-center weight.  Fits the lower-endpoint power on a
logarithmic sequence.  This is a diagnostic of absolute local integrability,
not a statement about conditional oscillatory convergence or a source-defined
continuum measure.
"""
from __future__ import annotations
import argparse, cmath, json, math
from pathlib import Path
import rc009_dense_grid_reliability as r


def logamp_envelope(j0,j1,H):
    g=r.geom(j0,j1,H)
    if g is None: return -math.inf
    k,K,Q,SR,V4,phi=g
    x=1+K*K-2*Q
    D=(j0**3*j1**3*k**15/16)*K*(K-1j*K*K+1j*Q)**3*x**3*(K+1j)**6*(K-3j)**2*(1+3*K*K-2*Q-2j*K*(Q-1))**3
    ad=abs(D)
    if not ad>0: return -math.inf
    B=ad/((1+K*K)**3*abs(1+K*K-2*Q)**6)
    if not B>0: return -math.inf
    return (3*r.ALPHA-1.5)*(math.log(j0)+math.log(j1))+6*(r.ALPHA-1)*math.log(k)-math.log(B)


def coarse_env(j):
    a=1/9; H=r.HTOTAL/2
    l1=logamp_envelope(a,j,H); l2=logamp_envelope(j,a,H)
    return math.log(r.jac(a,j,H))+math.log(r.jac(j,a,H))+27*l1+27*l2


def fine_env(j1,j2):
    a=1/16; H=r.HTOTAL/3
    ls=(logamp_envelope(a,j1,H),logamp_envelope(j1,j2,H),logamp_envelope(j2,a,H))
    js=(r.jac(a,j1,H),r.jac(j1,j2,H),r.jac(j2,a,H))
    return sum(math.log(x) for x in js)+64*sum(ls)


def linfit(xs,ys):
    xm=sum(xs)/len(xs); ym=sum(ys)/len(ys)
    den=sum((x-xm)**2 for x in xs)
    slope=sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/den
    intercept=ym-slope*xm
    rss=sum((y-(intercept+slope*x))**2 for x,y in zip(xs,ys))
    tss=sum((y-ym)**2 for y in ys)
    r2=1-rss/tss if tss>0 else 1.0
    return slope,intercept,r2


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--mode',choices=['coarse','fine_diag','fine_edge'],required=True)
    ap.add_argument('--anchor',type=float,default=0.2)
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    ts=[10.0**(-x/4) for x in range(4,25)]  # 1e-1 ... 1e-6
    vals=[]
    for t in ts:
        if args.mode=='coarse': y=coarse_env(t)
        elif args.mode=='fine_diag': y=fine_env(t,t)
        else: y=fine_env(t,args.anchor)
        if math.isfinite(y): vals.append((t,y))
    tail=vals[-12:]
    xs=[math.log(t) for t,_ in tail]; ys=[y for _,y in tail]
    p,b,r2=linfit(xs,ys)
    # If w~t^p: 1D endpoint is absolutely integrable iff p>-1.
    # Along the simultaneous 2D radial diagonal, area measure adds one power,
    # hence the conservative radial criterion is p>-2.  The edge is 1D.
    crit=-2.0 if args.mode=='fine_diag' else -1.0
    out={
      'test':'RC009_ENDPOINT_POWER_AUDIT', 'mode':args.mode,
      'anchor':args.anchor if args.mode=='fine_edge' else None,
      'fit_points':len(tail),'t_min':tail[-1][0],'t_max':tail[0][0],
      'envelope_power_p':p,'fit_r2':r2,'absolute_integrability_threshold':crit,
      'passes_absolute_power_criterion':p>crit,
      'samples':[{'t':t,'log_weight_envelope':y} for t,y in vals],
      'interpretation_lock':'Algebraic magnitude/envelope test only. Failure rules out simple absolute endpoint integrability in this reduced coordinate diagnostic; it does not rule out conditional oscillatory convergence, cancellations, a different source-defined measure, or full QG refinement.'
    }
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
