#!/usr/bin/env python3
"""RC006 decorated-index leg-order identifiability audit.

Prospectively tests whether exact source math/diagram blocks distinguish the
numbered/decorated legs needed for an Eq.(29) contraction.  It never uses
rendered-picture geometry.  A valid computation can scientifically FAIL
identifiability: if two or more decorated symbols of the same base have the same
source-incidence fingerprint, a nontrivial relabeling survives and the numerical
Eq.(29) amplitude remains blocked.
"""
from pathlib import Path
import argparse, collections, json, math, re

ANCHORS=('app:EPRL-diagram','app:EPRL-norm','app:graph','eq:BC-3-int','eq:BC-3-valent','eq:eprl-3-valent','global_identifiability')
SOURCE_ANCHORS=ANCHORS[:-1]+('eq:eprl-map','eq:recoupling-basis')
MATH_ENVS=('equation','equation*','align','align*','gather','gather*','multline','multline*','split','array','pmatrix','bmatrix','tikzpicture','figure','figure*')
BASES={'j','J','l','m','n'}

def enclosing_environment(t,p):
    cand=[]
    for env in MATH_ENVS:
        for b in re.finditer(r'\\begin\{'+re.escape(env)+r'\}',t[:p]):
            e=re.search(r'\\end\{'+re.escape(env)+r'\}',t[p:])
            if not e or re.search(r'\\end\{'+re.escape(env)+r'\}',t[b.end():p]): continue
            hi=p+e.end(); cand.append((hi-b.start(),b.start(),hi))
    return min(cand) if cand else None

def block(t,name):
    ms=list(re.finditer(r'\\label\s*\{'+re.escape(name)+r'\}',t))
    if len(ms)!=1: return None
    p=ms[0].start(); env=enclosing_environment(t,p)
    if env:
        _,lo,hi=env; return t[lo:hi]
    return t[max(0,p-1200):min(len(t),p+2200)]

def math_fragments(s):
    fr=[]
    for env in MATH_ENVS:
        fr.extend(m.group(0) for m in re.finditer(r'\\begin\{'+re.escape(env)+r'\}(.*?)\\end\{'+re.escape(env)+r'\}',s,re.S))
    fr.extend(m.group(1) for m in re.finditer(r'(?<!\\)\$(?!\$)(.+?)(?<!\\)\$(?!\$)',s,re.S))
    fr.extend(m.group(1) for m in re.finditer(r'\\\[(.*?)\\\]',s,re.S))
    return fr

def decorated_tokens(s):
    out=[]
    # Capture bases j,J,l,m,n only when carrying explicit sub/superscript source
    # decoration; normalize whitespace but preserve the decoration string.
    pat=re.compile(r'(?<![A-Za-z])([jJlmn])\s*((?:_\s*(?:\{[^{}]*\}|[A-Za-z0-9+\-]+)|\^\s*(?:\{[^{}]*\}|[A-Za-z0-9+\-]+)){1,2})')
    for frag in math_fragments(s):
        for m in pat.finditer(frag):
            base=m.group(1); dec=re.sub(r'\s+','',m.group(2)); out.append(base+dec)
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--role',choices=ANCHORS,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    fs=list(Path(a.source_dir).rglob('*.tex'))
    if len(fs)!=1: raise SystemExit('monolithic source prerequisite violated')
    t=fs[0].read_text(errors='ignore')
    blocks={name:block(t,name) for name in SOURCE_ANCHORS}
    toks={name:decorated_tokens(blocks[name] or '') for name in SOURCE_ANCHORS}
    if a.role!='global_identifiability':
        seq=toks[a.role]; unique=sorted(set(seq))
        metrics={'decorated_token_count':len(seq),'unique_decorated_token_count':len(unique),'ordered_decorated_tokens':seq[:200],'unique_decorated_tokens':unique}
        # Frozen qualification criterion: at least two explicit decorated source
        # tokens. This is an observability prerequisite, not uniqueness.
        valid=len(seq)>=2 and len(unique)>=1
        scientific='SOURCE_LEG_DECORATION_OBSERVABLE' if valid else 'SOURCE_LEG_DECORATION_INSUFFICIENT'
    else:
        # Exact incidence fingerprint = count in each qualified source anchor.
        universe=sorted(set(x for seq in toks.values() for x in seq))
        profiles={x:tuple(toks[name].count(x) for name in SOURCE_ANCHORS) for x in universe}
        groups=collections.defaultdict(list)
        for x,p in profiles.items():
            base=x[0]
            if base in BASES: groups[(base,p)].append(x)
        interchangeable=[sorted(v) for v in groups.values() if len(v)>1]
        log10_perm=0.0
        for g in interchangeable: log10_perm += math.log10(math.factorial(len(g)))
        unique_identifiable=(len(interchangeable)==0)
        metrics={'anchor_order':list(SOURCE_ANCHORS),'decorated_symbol_count':len(universe),'incidence_profiles':{k:list(v) for k,v in profiles.items()},'interchangeable_leg_groups':interchangeable,'interchangeable_group_count':len(interchangeable),'log10_surviving_relabelings_lower_bound':log10_perm,'source_incidence_unique':unique_identifiable}
        # Computation validity is independent of scientific uniqueness. Require a
        # nontrivial decorated-symbol universe and at least six populated anchors.
        valid=len(universe)>=3 and sum(bool(toks[n]) for n in SOURCE_ANCHORS)>=6
        scientific='SCIENTIFIC_PASS_SOURCE_INCIDENCE_UNIQUE' if (valid and unique_identifiable) else ('SCIENTIFIC_FAIL_SOURCE_INCIDENCE_NONIDENTIFIABLE' if valid else 'BLOCKED_INSUFFICIENT_DECORATED_SOURCE_DATA')
    out={'test':'RC006_LEG_ORDER_IDENTIFIABILITY','role':a.role,'valid_computation':bool(valid),'scientific_classification':scientific,'metrics':metrics,'interpretation_rule':'Only global valid+source_incidence_unique may support a later contraction-ready mapping; nonidentifiable or insufficient results keep Eq29 amplitude blocked.','claim_lock':'No picture geometry; no post-result convention choice; no Eq29 amplitude, bridge, or candidate theory.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
    if not valid: raise SystemExit(2)
if __name__=='__main__': main()
