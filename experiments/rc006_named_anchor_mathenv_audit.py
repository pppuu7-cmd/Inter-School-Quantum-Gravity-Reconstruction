#!/usr/bin/env python3
"""Prospective RC006 named-anchor math-environment and symbol-incidence audit.

This audit consumes only source labels qualified by the prior reference-chain and
named-anchor dependency gates. It extracts the exact enclosing TeX environment
(or a bounded local source block when the label is not inside an environment),
then records ordered symbol tokens without interpreting rendered figure geometry.

PASS means source math/context is machine-readable for the frozen anchor. It does
not mean that a unique tensor contraction has been established. The incidence
lane explicitly reports ambiguity and never selects one ordering.
"""
from pathlib import Path
import argparse, collections, json, re

ANCHORS=(
 'app:EPRL-diagram','app:EPRL-norm','app:graph',
 'eq:BC-3-int','eq:BC-3-valent','eq:eprl-3-valent',
 'eq:eprl-map','eq:recoupling-basis','symbol_incidence')
EQ29_GROUP=('app:EPRL-diagram','app:EPRL-norm','app:graph','eq:BC-3-int','eq:BC-3-valent','eq:eprl-3-valent')
DOWNSTREAM=('eq:eprl-map','eq:recoupling-basis')
TOKEN_RE=re.compile(r'\\(?:mathcal|mathrm|mathbf|operatorname)?\s*\{?([A-Za-z]+)\}?|([A-Za-z])(?:_[{A-Za-z0-9+\-]+|\^[{A-Za-z0-9+\-]+)?')

def line(t,p): return t.count('\n',0,p)+1

def normalize(s): return ' '.join(re.sub(r'%.*',' ',s).split())

def tokens(s):
    out=[]
    for m in TOKEN_RE.finditer(s):
        tok=(m.group(1) or m.group(2) or '').strip()
        if tok and tok not in {'begin','end','label','ref','eqref','frac','left','right','text','mathrm','mathcal'}:
            out.append(tok)
    return out

def block_for_label(t,name):
    ms=list(re.finditer(r'\\label\s*\{'+re.escape(name)+r'\}',t))
    if len(ms)!=1: return ms,None,None
    p=ms[0].start()
    # Find nearest enclosing explicit environment by scanning begins before label.
    begins=list(re.finditer(r'\\begin\{([^}]+)\}',t[:p]))
    chosen=None
    for b in reversed(begins):
        env=b.group(1)
        e=re.search(r'\\end\{'+re.escape(env)+r'\}',t[p:])
        if e:
            # Ensure there is no closing of same env between begin and label.
            middle=t[b.end():p]
            if not re.search(r'\\end\{'+re.escape(env)+r'\}',middle):
                end=p+e.end(); chosen=(env,b.start(),end); break
    if chosen:
        env,lo,hi=chosen; return ms,env,t[lo:hi]
    return ms,'LOCAL_BLOCK',t[max(0,p-900):min(len(t),p+1800)]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--anchor',choices=ANCHORS,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    fs=list(Path(a.source_dir).rglob('*.tex'))
    if len(fs)!=1: raise SystemExit('monolithic source prerequisite violated')
    t=fs[0].read_text(errors='ignore')
    if a.anchor!='symbol_incidence':
        ms,env,blk=block_for_label(t,a.anchor)
        nt=normalize(blk or '')
        toks=tokens(blk or '')
        explicit_math=bool(re.search(r'\\begin\{(?:equation|align|gather|multline|split|array|pmatrix|bmatrix|tikzpicture|figure)[^}]*\}|\$|\\\[',blk or ''))
        metrics={'definition_count':len(ms),'environment':env,'context_char_count':len(blk or ''),'normalized_char_count':len(nt),'ordered_symbol_token_count':len(toks),'ordered_symbol_tokens':toks[:160],'explicit_math_or_diagram_marker':explicit_math,'definition_line':line(t,ms[0].start()) if len(ms)==1 else None,'context_excerpt':nt[:2200]}
        # Frozen before result: exact unique label + nontrivial source block + at least
        # one explicit math/diagram marker and at least 3 ordered symbol tokens.
        ok=len(ms)==1 and len(nt)>=80 and explicit_math and len(toks)>=3
    else:
        rows={}
        for name in EQ29_GROUP+DOWNSTREAM:
            ms,env,blk=block_for_label(t,name); rows[name]={'unique':len(ms)==1,'environment':env,'tokens':tokens(blk or '')}
        sets={k:set(v['tokens']) for k,v in rows.items()}
        eq_union=set().union(*(sets[k] for k in EQ29_GROUP))
        ds_union=set().union(*(sets[k] for k in DOWNSTREAM))
        shared=sorted(eq_union & ds_union)
        # Count how many distinct source token orderings occur among anchor blocks.
        signatures={k:tuple(v['tokens'][:80]) for k,v in rows.items()}
        unique_sigs=len(set(signatures.values()))
        metrics={'anchor_unique':{k:v['unique'] for k,v in rows.items()},'shared_symbol_tokens':shared,'shared_symbol_count':len(shared),'distinct_ordered_token_signatures':unique_sigs,'ordered_token_signatures':{k:list(v[:80]) for k,v in signatures.items()},'ambiguity_preserved': unique_sigs>1}
        # Frozen criterion qualifies incidence only; it explicitly requires >1
        # signature so the audit cannot collapse structural co-occurrence into a
        # fake unique contraction ordering.
        ok=all(v['unique'] for v in rows.values()) and len(shared)>=2 and unique_sigs>1
    out={'test':'RC006_NAMED_ANCHOR_MATHENV_AUDIT','anchor':a.anchor,'source':'official arXiv 1609.02429 monolithic TeX source','metrics':metrics,'frozen_gate_pass':bool(ok),'classification_if_pass':'PASS_EXACT_SOURCE_MATHENV_SYMBOL_INCIDENCE_PREREQUISITE_ONLY','claim_lock':'No figure-geometry inference; no automatic unique tensor ordering; ambiguity is preserved; no Eq29 amplitude, bridge, or candidate-theory claim.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
    if not ok: raise SystemExit(2)
if __name__=='__main__': main()
