#!/usr/bin/env python3
"""Audit the explicit Eq.(26) R-matrix factor entering RC-006 Eq.(29).

For k=12,gamma=1/3 enumerate the 11 source-admissible (l1,l2,l) triples and
all internal j channels of the explicit crossing between j1+ and j2- indicated
by the Eq.(29) phase.  Compute quantum dimensions and exact unit-circle q phase.
This tests whether the explicit R factor itself suppresses any allowed channel.
It does NOT evaluate the remaining q-spin-network graph or authorize Eq.(29).
"""
from fractions import Fraction
from pathlib import Path
import argparse, cmath, json, math
K=12; JMAX=6; GAMMA=Fraction(1,3)
q=cmath.exp(2j*math.pi/(K+2))

def fuse(a,b):
    lo=abs(a-b); hi=min(a+b,K-a-b)
    return list(range(lo,hi+1)) if hi>=lo else []

def emap(l):
    jp=Fraction(1+GAMMA,2)*l; jm=Fraction(1-GAMMA,2)*l
    return None if jp.denominator!=1 or jm.denominator!=1 else (int(jp),int(jm))

def qnum(n):
    return math.sin(math.pi*n/(K+2))/math.sin(math.pi/(K+2))

def qdim(j): return qnum(2*j+1)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',type=int,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    simple={l:emap(l) for l in range(JMAX+1) if emap(l) is not None}
    triples=[]
    for l1,m1 in simple.items():
      for l2,m2 in simple.items():
        for l,mt in simple.items():
          if l in fuse(l1,l2): triples.append((l1,l2,l,m1,m2,mt))
    if not (0<=a.lane<len(triples)): raise SystemExit('lane out of range')
    l1,l2,l,m1,m2,mt=triples[a.lane]
    j1p,j1m=m1; j2p,j2m=m2
    rows=[]
    for j in fuse(j1p,j2m):
      expn=-Fraction(1,2)*(j1p*(j1p+1)+j2m*(j2m+1)-j*(j+1))
      coeff=qdim(j)*cmath.exp(2j*math.pi/(K+2)*float(expn))
      rows.append({'j':j,'q_exponent':[expn.numerator,expn.denominator],
                   'qdim':qdim(j),'coeff_real':coeff.real,'coeff_imag':coeff.imag,
                   'coeff_abs':abs(coeff),'nonzero':abs(coeff)>1e-12})
    out={'test':'RC006_EQ29_RMATRIX_FACTOR','lane':a.lane,'k':K,'gamma':'1/3',
         'boundary':{'l1':l1,'l2':l2,'l':l,'map_l1':list(m1),'map_l2':list(m2),'map_l':list(mt)},
         'channel_count':len(rows),'all_explicit_R_channels_nonzero':bool(rows) and all(x['nonzero'] for x in rows),
         'minimum_R_coefficient_abs':min((x['coeff_abs'] for x in rows),default=0.0),
         'channels':rows,
         'claim_lock':'Eq.(26) explicit R-factor only. Nonzero R weights do not prove the full Eq.(29) graph is nonzero; cancellations or other graph factors remain possible.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not out['all_explicit_R_channels_nonzero']: raise SystemExit(2)
if __name__=='__main__': main()
