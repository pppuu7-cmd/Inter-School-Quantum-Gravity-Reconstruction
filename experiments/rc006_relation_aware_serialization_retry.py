#!/usr/bin/env python3
"""Prospectively frozen relation-aware retry of RC006 contraction serialization.

Adds one source-authorized pooled fingerprint for the independently validated
explicit-reference component, while retaining the original exact lane set and
100% holdout/null aggregate gate. No anchor weighting or favorable selection.
"""
from pathlib import Path
import argparse, collections, json, re

ALL=('app:EPRL-diagram','app:EPRL-norm','app:graph','eq:BC-3-int','eq:BC-3-valent','eq:eprl-3-valent','eq:eprl-map','eq:recoupling-basis')
REL=('app:EPRL-diagram','app:EPRL-norm','app:graph','eq:recoupling-basis')
MATH_ENVS=('equation','equation*','align','align*','gather','gather*','multline','multline*','split','array','pmatrix','bmatrix','tikzpicture','figure','figure*')
PAT=re.compile(r'(?<![A-Za-z])([jJlmn])\s*((?:_\s*(?:\{[^{}]*\}|[A-Za-z0-9+\-]+)|\^\s*(?:\{[^{}]*\}|[A-Za-z0-9+\-]+)){1,2})')

def enclosing(t,p):
    c=[]
    for env in MATH_ENVS:
        for b in re.finditer(r'\\begin\{'+re.escape(env)+r'\}',t[:p]):
            e=re.search(r'\\end\{'+re.escape(env)+r'\}',t[p:])
            if e and not re.search(r'\\end\{'+re.escape(env)+r'\}',t[b.end():p]):
                hi=p+e.end(); c.append((hi-b.start(),b.start(),hi))
    return min(c) if c else None

def block(t,name):
    ms=list(re.finditer(r'\\label\s*\{'+re.escape(name)+r'\}',t))
    if len(ms)!=1:return None
    p=ms[0].start(); e=enclosing(t,p)
    if e:
        _,lo,hi=e; return t[lo:hi]
    return t[max(0,p-1200):min(len(t),p+2200)]

def frags(s):
    out=[]
    for env in MATH_ENVS:
        out += [m.group(0) for m in re.finditer(r'\\begin\{'+re.escape(env)+r'\}(.*?)\\end\{'+re.escape(env)+r'\}',s,re.S)]
    out += [m.group(1) for m in re.finditer(r'(?<!\\)\$(?!\$)(.+?)(?<!\\)\$(?!\$)',s,re.S)]
    out += [m.group(1) for m in re.finditer(r'\\\[(.*?)\\\]',s,re.S)]
    return out

def seq(s):
    z=[]
    for f in frags(s or ''):
        for m in PAT.finditer(f): z.append(m.group(1)+re.sub(r'\s+','',m.group(2)))
    return z

def occurrence_tuple(q,i,unordered):
    if unordered:return ('COUNT',)
    prev=q[i-1] if i else '<BOS>'; nxt=q[i+1] if i+1<len(q) else '<EOS>'
    posbin=min(3,int(4*i/max(1,len(q))))
    return (prev,nxt,posbin)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--role',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    fs=list(Path(a.source_dir).rglob('*.tex'))
    if len(fs)!=1: raise SystemExit('monolithic source prerequisite violated')
    t=fs[0].read_text(errors='ignore'); S={n:seq(block(t,n)) for n in ALL}
    universe=sorted(set(x for q in S.values() for x in q))
    if a.role=='full': active=list(ALL); unordered=False
    elif a.role=='null_unordered': active=list(ALL); unordered=True
    elif a.role.startswith('drop:') and a.role[5:] in ALL: active=[n for n in ALL if n!=a.role[5:]]; unordered=False
    else: raise SystemExit('bad role')
    fps={}
    for x in universe:
        parts=[]
        for n in active:
            q=S[n]; occ=[]
            for i,v in enumerate(q):
                if v==x: occ.append(occurrence_tuple(q,i,unordered))
            parts.append((n,tuple(sorted(occ))))
        pooled=[]
        for n in REL:
            if n not in active: continue
            q=S[n]
            for i,v in enumerate(q):
                if v==x: pooled.append(occurrence_tuple(q,i,unordered))
        # Anchor identity is deliberately removed only in this appended pooled feature.
        fps[x]=(x[0],tuple(parts),('REL_COMPONENT',tuple(sorted(pooled))))
    groups=collections.defaultdict(list)
    for x,p in fps.items(): groups[p].append(x)
    ambiguous=[sorted(v) for v in groups.values() if len(v)>1]
    ordered=sorted(universe,key=lambda x:(fps[x],x)); rank={x:i for i,x in enumerate(ordered)}
    pair_sign={}
    for i,x in enumerate(universe):
        for y in universe[i+1:]: pair_sign[x+'||'+y]=-1 if rank[x]<rank[y] else 1
    valid=len(universe)>=30 and sum(bool(S[n]) for n in ALL)>=6
    out={'test':'RC006_RELATION_AWARE_SERIALIZATION_RETRY','role':a.role,'valid_computation':valid,
         'relation_component':list(REL),'decorated_symbol_count':len(universe),
         'ambiguous_groups':ambiguous,'ambiguous_group_count':len(ambiguous),
         'canonical_order':ordered,'pair_sign':pair_sign,
         'lane_classification':('NULL_AMBIGUITY_PRESENT' if unordered and ambiguous else ('ORDER_UNIQUE' if not ambiguous else 'ORDER_AMBIGUOUS')),
         'frozen_aggregate_rule':'Full unique; all 8 leave-one-anchor orders unique and 100% pairwise-order identical to full; unordered null ambiguous.',
         'claim_lock':'Stable serialization prerequisite only; no Eq29 amplitude, TNR/refinement bridge or candidate-theory claim.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='pair_sign'},indent=2,sort_keys=True))
    if not valid: raise SystemExit(2)
if __name__=='__main__': main()
