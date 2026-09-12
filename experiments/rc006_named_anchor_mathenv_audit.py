#!/usr/bin/env python3
"""Prospective RC006 named-anchor math-environment and symbol-incidence audit.

The scientific gate is unchanged from the first run. This implementation excludes
the document environment from anchor extraction and tokenizes only TeX math/
diagram source, fixing the first causal measurement defect observed in raw logs.
No frozen threshold or interpretation rule is changed.
"""
from pathlib import Path
import argparse, json, re

ANCHORS=(
 'app:EPRL-diagram','app:EPRL-norm','app:graph',
 'eq:BC-3-int','eq:BC-3-valent','eq:eprl-3-valent',
 'eq:eprl-map','eq:recoupling-basis','symbol_incidence')
EQ29_GROUP=('app:EPRL-diagram','app:EPRL-norm','app:graph','eq:BC-3-int','eq:BC-3-valent','eq:eprl-3-valent')
DOWNSTREAM=('eq:eprl-map','eq:recoupling-basis')
MATH_ENVS=('equation','equation*','align','align*','gather','gather*','multline','multline*','split','array','pmatrix','bmatrix','tikzpicture','figure','figure*')
STOP_CMDS={'begin','end','label','ref','eqref','autoref','frac','left','right','text','mathrm','mathcal','mathbf','operatorname','nonumber','quad','qquad'}

def line(t,p): return t.count('\n',0,p)+1

def normalize(s): return ' '.join(re.sub(r'%[^\n]*',' ',s).split())

def math_fragments(s):
    fr=[]
    # Explicit environments relevant to equations/diagrams.
    for env in MATH_ENVS:
        pat=r'\\begin\{'+re.escape(env)+r'\}(.*?)\\end\{'+re.escape(env)+r'\}'
        fr.extend(m.group(0) for m in re.finditer(pat,s,re.S))
    # Inline/display math not already dependent on prose tokenization.
    fr.extend(m.group(1) for m in re.finditer(r'(?<!\\)\$\$(.+?)(?<!\\)\$\$',s,re.S))
    fr.extend(m.group(1) for m in re.finditer(r'(?<!\\)\$(?!\$)(.+?)(?<!\\)\$(?!\$)',s,re.S))
    fr.extend(m.group(1) for m in re.finditer(r'\\\[(.*?)\\\]',s,re.S))
    return fr

def tokens(s):
    out=[]
    for frag in math_fragments(s):
        # TeX command names are meaningful source operators; variables are taken
        # only inside math/diagram fragments, never from prose.
        for m in re.finditer(r'\\([A-Za-z]+)|(?<![A-Za-z])([A-Za-z])(?:_\{?[^\s{}]+\}?|\^\{?[^\s{}]+\}?)?',frag):
            tok=(m.group(1) or m.group(2) or '').strip()
            if tok and tok not in STOP_CMDS:
                out.append(tok)
    return out

def enclosing_environment(t,p):
    candidates=[]
    for env in MATH_ENVS:
        for b in re.finditer(r'\\begin\{'+re.escape(env)+r'\}',t[:p]):
            e=re.search(r'\\end\{'+re.escape(env)+r'\}',t[p:])
            if not e: continue
            if re.search(r'\\end\{'+re.escape(env)+r'\}',t[b.end():p]): continue
            hi=p+e.end(); candidates.append((hi-b.start(),env,b.start(),hi))
    return min(candidates) if candidates else None

def block_for_label(t,name):
    ms=list(re.finditer(r'\\label\s*\{'+re.escape(name)+r'\}',t))
    if len(ms)!=1: return ms,None,None
    p=ms[0].start()
    chosen=enclosing_environment(t,p)
    if chosen:
        _,env,lo,hi=chosen; return ms,env,t[lo:hi]
    # Source-local fallback is deliberately bounded; unlike the invalid first
    # implementation it can never expand to the whole document.
    return ms,'LOCAL_BLOCK',t[max(0,p-1200):min(len(t),p+2200)]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--anchor',choices=ANCHORS,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    fs=list(Path(a.source_dir).rglob('*.tex'))
    if len(fs)!=1: raise SystemExit('monolithic source prerequisite violated')
    t=fs[0].read_text(errors='ignore')
    if a.anchor!='symbol_incidence':
        ms,env,blk=block_for_label(t,a.anchor)
        nt=normalize(blk or ''); toks=tokens(blk or '')
        explicit_math=bool(math_fragments(blk or ''))
        metrics={'definition_count':len(ms),'environment':env,'context_char_count':len(blk or ''),'normalized_char_count':len(nt),'ordered_symbol_token_count':len(toks),'ordered_symbol_tokens':toks[:160],'explicit_math_or_diagram_marker':explicit_math,'definition_line':line(t,ms[0].start()) if len(ms)==1 else None,'context_excerpt':nt[:2200]}
        # Frozen gate unchanged.
        ok=len(ms)==1 and len(nt)>=80 and explicit_math and len(toks)>=3
    else:
        rows={}
        for name in EQ29_GROUP+DOWNSTREAM:
            ms,env,blk=block_for_label(t,name); rows[name]={'unique':len(ms)==1,'environment':env,'tokens':tokens(blk or '')}
        sets={k:set(v['tokens']) for k,v in rows.items()}
        eq_union=set().union(*(sets[k] for k in EQ29_GROUP)); ds_union=set().union(*(sets[k] for k in DOWNSTREAM))
        shared=sorted(eq_union & ds_union)
        signatures={k:tuple(v['tokens'][:80]) for k,v in rows.items()}; unique_sigs=len(set(signatures.values()))
        metrics={'anchor_unique':{k:v['unique'] for k,v in rows.items()},'anchor_environments':{k:v['environment'] for k,v in rows.items()},'shared_symbol_tokens':shared,'shared_symbol_count':len(shared),'distinct_ordered_token_signatures':unique_sigs,'ordered_token_signatures':{k:list(v[:80]) for k,v in signatures.items()},'ambiguity_preserved':unique_sigs>1}
        # Frozen gate unchanged: source incidence plus explicit preservation of
        # multiple order signatures; it cannot authorize a unique contraction.
        ok=all(v['unique'] for v in rows.values()) and len(shared)>=2 and unique_sigs>1
    out={'test':'RC006_NAMED_ANCHOR_MATHENV_AUDIT','anchor':a.anchor,'source':'official arXiv 1609.02429 monolithic TeX source','metrics':metrics,'frozen_gate_pass':bool(ok),'classification_if_pass':'PASS_EXACT_SOURCE_MATHENV_SYMBOL_INCIDENCE_PREREQUISITE_ONLY','claim_lock':'No figure-geometry inference; no automatic unique tensor ordering; ambiguity is preserved; no Eq29 amplitude, bridge, or candidate-theory claim.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
    if not ok: raise SystemExit(2)
if __name__=='__main__': main()
