#!/usr/bin/env python3
"""RC006 contraction-serialization stability gate.

Prospective follow-up to ordered-context uniqueness + 8/8 anchor holdout PASS.
Builds a canonical decorated-symbol order solely from exact source ordered-context
fingerprints.  Each lane removes one qualified anchor (or none) without retuning;
the null lane deliberately erases neighbor/position information.

Scientific gate is applied only by the workflow aggregate: every leave-one-anchor
canonical pairwise ordering must agree exactly with the full-source ordering,
while the unordered null must contain ambiguity.  This is a source-serialization
prerequisite only, not an Eq.(29) amplitude or bridge result.
"""
from pathlib import Path
import argparse, collections, json, re

ALL=('app:EPRL-diagram','app:EPRL-norm','app:graph','eq:BC-3-int','eq:BC-3-valent','eq:eprl-3-valent','eq:eprl-map','eq:recoupling-basis')
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
                if v==x:
                    if unordered: occ.append(('COUNT',))
                    else:
                        prev=q[i-1] if i else '<BOS>'; nxt=q[i+1] if i+1<len(q) else '<EOS>'
                        posbin=min(3,int(4*i/max(1,len(q))))
                        occ.append((prev,nxt,posbin))
            parts.append((n,tuple(sorted(occ))))
        fps[x]=(x[0],tuple(parts))
    groups=collections.defaultdict(list)
    for x,p in fps.items(): groups[p].append(x)
    ambiguous=[sorted(v) for v in groups.values() if len(v)>1]
    ordered=sorted(universe,key=lambda x:(fps[x],x))
    rank={x:i for i,x in enumerate(ordered)}
    pair_sign={}
    for i,x in enumerate(universe):
        for y in universe[i+1:]: pair_sign[x+'||'+y] = -1 if rank[x]<rank[y] else 1
    valid=len(universe)>=30 and sum(bool(S[n]) for n in ALL)>=6
    out={'test':'RC006_CONTRACTION_SERIALIZATION_STABILITY','role':a.role,'valid_computation':valid,
         'decorated_symbol_count':len(universe),'ambiguous_groups':ambiguous,'ambiguous_group_count':len(ambiguous),
         'canonical_order':ordered,'pair_sign':pair_sign,
         'lane_classification':('NULL_AMBIGUITY_PRESENT' if unordered and ambiguous else ('ORDER_UNIQUE' if not ambiguous else 'ORDER_AMBIGUOUS')),
         'frozen_aggregate_rule':'Authorize source contraction serialization only if full is unique, all 8 leave-one-anchor orders are unique AND 100% pairwise-order identical to full, and unordered null is ambiguous.',
         'claim_lock':'Source serialization prerequisite only; no Eq29 numerical amplitude, TNR bridge, or candidate-theory claim.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='pair_sign'},indent=2,sort_keys=True))
    if not valid: raise SystemExit(2)
if __name__=='__main__': main()
