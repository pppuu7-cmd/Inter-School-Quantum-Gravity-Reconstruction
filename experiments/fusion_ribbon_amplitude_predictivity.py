#!/usr/bin/env python3
"""Continuous-amplitude audit for source-native ribbon observables versus SVD sectors.

This is a nearest-framework control for BH-004B.  It deliberately avoids the
binary support threshold used in the previous audit and asks whether the full
sector weights of a pre-RG ribbon observable predict the sector weights/ranks
of the two singular-value spectra produced by the next coarse-graining step.
The null is a sector-label permutation preserving both marginal spectra.
"""
from __future__ import annotations
import argparse, json, math, random, re, statistics
from pathlib import Path

NUM = re.compile(r'[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?')

def nums(section):
    return [float(x) for x in NUM.findall(section)]

def prob(v):
    a=[abs(float(x)) for x in v]
    s=sum(a)
    return [x/s for x in a] if s else [0.0 for _ in a]

def cosine(a,b):
    aa=sum(x*x for x in a); bb=sum(x*x for x in b)
    if aa==0 or bb==0: return 0.0
    return sum(x*y for x,y in zip(a,b))/math.sqrt(aa*bb)

def ranks(v):
    # average ranks for ties
    order=sorted(range(len(v)), key=lambda i:v[i])
    r=[0.0]*len(v); i=0
    while i<len(order):
        j=i+1
        while j<len(order) and v[order[j]]==v[order[i]]: j+=1
        rr=(i+j-1)/2+1
        for k in range(i,j): r[order[k]]=rr
        i=j
    return r

def pearson(a,b):
    ma=sum(a)/len(a); mb=sum(b)/len(b)
    da=[x-ma for x in a]; db=[y-mb for y in b]
    va=sum(x*x for x in da); vb=sum(y*y for y in db)
    if va==0 or vb==0: return 0.0
    return sum(x*y for x,y in zip(da,db))/math.sqrt(va*vb)

def spearman(a,b):
    return pearson(ranks(a),ranks(b))

def permutation_null(src,tgt,reps,seed):
    rng=random.Random(seed); vals=[]; idx=list(range(len(src)))
    for _ in range(reps):
        p=idx[:]; rng.shuffle(p); s=[src[i] for i in p]
        vals.append((cosine(s,tgt),spearman(s,tgt)))
    cs=sorted(x[0] for x in vals); ss=sorted(x[1] for x in vals)
    return {
      'cos_mean':sum(cs)/len(cs), 'cos_p95':cs[int(.95*(len(cs)-1))],
      'rho_mean':sum(ss)/len(ss), 'rho_p95':ss[int(.95*(len(ss)-1))]
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--log',required=True)
    ap.add_argument('--g',type=float,required=True); ap.add_argument('--iterations',type=int,default=5)
    ap.add_argument('--reps',type=int,default=2048); ap.add_argument('--output',required=True)
    args=ap.parse_args(); text=Path(args.log).read_text(errors='replace')
    if 'Singular values:' not in text or 'Expectation values of Ribbon operators' not in text:
        raise SystemExit('required output sections absent')
    svsec=text.split('Singular values:',1)[1].split('Expectation values of Ribbon operators',1)[0]
    exsec=text.split('Expectation values of Ribbon operators',1)[1]
    sv=nums(svsec); ex=nums(exsec)
    need_sv=18*args.iterations; need_ex=9*(args.iterations+1)
    if len(sv)<need_sv or len(ex)<need_ex: raise SystemExit(f'not enough values sv={len(sv)}/{need_sv} ex={len(ex)}/{need_ex}')
    sv=sv[-need_sv:]; ex=ex[-need_ex:]
    sm=[sv[i:i+9] for i in range(0,len(sv),9)]; first=sm[0::2]; second=sm[1::2]
    exp=[ex[i:i+9] for i in range(0,len(ex),9)]
    rows=[]
    for t in range(args.iterations):
        src=prob(exp[t])
        row={'step':t+1}
        for label,target0,off in [('svd1',first[t],10000),('svd2',second[t],20000)]:
            target=prob(target0); c=cosine(src,target); r=spearman(src,target)
            null=permutation_null(src,target,args.reps,off+100*t+int(round(args.g*100)))
            row[label]={'cosine':c,'spearman':r,'null':null,
                        'cos_above_p95':c>null['cos_p95'],'rho_above_p95':r>null['rho_p95']}
        rows.append(row)
    cos1=[r['svd1']['cosine'] for r in rows]; cos2=[r['svd2']['cosine'] for r in rows]
    rho1=[r['svd1']['spearman'] for r in rows]; rho2=[r['svd2']['spearman'] for r in rows]
    both=[r['svd1']['cos_above_p95'] and r['svd2']['cos_above_p95'] and r['svd1']['rho_above_p95'] and r['svd2']['rho_above_p95'] for r in rows]
    out={'test':'FUSION_RIBBON_CONTINUOUS_AMPLITUDE_PREDICTIVITY','g':args.g,'iterations':args.iterations,'permutations':args.reps,'rows':rows,
         'summary':{'mean_cos_svd1':statistics.mean(cos1),'mean_cos_svd2':statistics.mean(cos2),
                    'mean_rho_svd1':statistics.mean(rho1),'mean_rho_svd2':statistics.mean(rho2),
                    'fraction_steps_all_metrics_above_permutation_p95':sum(both)/len(both)},
         'claim_lock':'Nearest-framework q-deformed lattice-gauge/TNR control. Positive continuous predictivity means source-native ribbon sector amplitudes carry label-specific information about later SVD spectra beyond permutation nulls; it does not establish a gravity selector, continuum QG, or new physics.'}
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
