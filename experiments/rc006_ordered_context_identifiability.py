#!/usr/bin/env python3
"""RC006 ordered decorated-index context identifiability audit.

Follow-up to the valid incidence-count non-identifiability result. Uses the same
qualified exact source blocks but enriches each decorated symbol fingerprint with
ordered local neighbors and normalized occurrence positions. No rendered geometry
or post-result convention choice is used.
"""
from pathlib import Path
import argparse, collections, json, math, re

ROLES=('app:EPRL-diagram','app:EPRL-norm','app:graph','eq:BC-3-int','eq:BC-3-valent','eq:eprl-3-valent','global_ordered_context')
ALL=('app:EPRL-diagram','app:EPRL-norm','app:graph','eq:BC-3-int','eq:BC-3-valent','eq:eprl-3-valent','eq:eprl-map','eq:recoupling-basis')
MATH_ENVS=('equation','equation*','align','align*','gather','gather*','multline','multline*','split','array','pmatrix','bmatrix','tikzpicture','figure','figure*')
BASES={'j','J','l','m','n'}
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
    ap=argparse.ArgumentParser();ap.add_argument('--source-dir',required=True);ap.add_argument('--role',choices=ROLES,required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
    fs=list(Path(a.source_dir).rglob('*.tex'))
    if len(fs)!=1: raise SystemExit('monolithic source prerequisite violated')
    t=fs[0].read_text(errors='ignore'); S={n:seq(block(t,n)) for n in ALL}
    if a.role!='global_ordered_context':
        q=S[a.role]; transitions=collections.Counter(zip(q,q[1:])); valid=len(q)>=2
        metrics={'decorated_count':len(q),'unique_decorated_count':len(set(q)),'ordered_transition_count':len(transitions),'top_transitions':[[list(k),v] for k,v in transitions.most_common(30)]}
        cls='SOURCE_ORDERED_CONTEXT_OBSERVABLE' if valid else 'BLOCKED_INSUFFICIENT_ORDERED_CONTEXT'
    else:
        universe=sorted(set(x for q in S.values() for x in q))
        fps={}
        for x in universe:
            anchor_parts=[]
            for n in ALL:
                q=S[n]; occ=[]
                for i,v in enumerate(q):
                    if v==x:
                        prev=q[i-1] if i else '<BOS>'; nxt=q[i+1] if i+1<len(q) else '<EOS>'
                        # Frozen positional binning into quartiles adds ordering info
                        # without using picture coordinates.
                        posbin=min(3,int(4*i/max(1,len(q))))
                        occ.append((prev,nxt,posbin))
                anchor_parts.append(tuple(sorted(occ)))
            fps[x]=tuple(anchor_parts)
        groups=collections.defaultdict(list)
        for x,p in fps.items(): groups[(x[0],p)].append(x)
        interchangeable=[sorted(v) for v in groups.values() if len(v)>1]
        logp=sum(math.log10(math.factorial(len(g))) for g in interchangeable)
        unique=len(interchangeable)==0
        valid=len(universe)>=3 and sum(bool(S[n]) for n in ALL)>=6
        metrics={'decorated_symbol_count':len(universe),'interchangeable_groups':interchangeable,'interchangeable_group_count':len(interchangeable),'log10_surviving_relabelings_lower_bound':logp,'ordered_context_unique':unique}
        cls='SCIENTIFIC_PASS_ORDERED_CONTEXT_UNIQUE' if valid and unique else ('SCIENTIFIC_FAIL_ORDERED_CONTEXT_NONIDENTIFIABLE' if valid else 'BLOCKED_INSUFFICIENT_ORDERED_CONTEXT')
    out={'test':'RC006_ORDERED_CONTEXT_IDENTIFIABILITY','role':a.role,'valid_computation':bool(valid),'scientific_classification':cls,'metrics':metrics,'interpretation_rule':'Only valid global ordered-context uniqueness may support a later contraction-ready mapping; surviving interchangeable groups keep Eq29 amplitude blocked.','claim_lock':'No rendered geometry, no post-result convention choice, no Eq29 amplitude/bridge/candidate-theory claim.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
    if not valid: raise SystemExit(2)
if __name__=='__main__':main()
