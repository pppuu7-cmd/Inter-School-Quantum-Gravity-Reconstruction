#!/usr/bin/env python3
"""Tokenize the exact official-source TikZ environment nearest RC-006 Eq.(29).

Output is a derived structural token stream (coordinates, path operators, compact
labels/options, hashes), not verbatim article TeX.  It is used to reconstruct the
oriented/braided graph without hand-transcribing the rendered PDF.
"""
from pathlib import Path
import argparse, hashlib, json, re

def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def ln(text,pos): return text.count('\n',0,pos)+1

def envs(text):
    b='\\begin{tikzpicture}'; e='\\end{tikzpicture}'; out=[]; p=0
    while True:
        i=text.find(b,p)
        if i<0: break
        j=text.find(e,i)
        if j<0: break
        j+=len(e); out.append((i,j,text[i:j])); p=j
    return out

def clean_label(x): return ' '.join(x.replace('$','').split())[:100]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    root=Path(a.source_dir); phrase='Before we discuss the behaviour of the EPRL model under coarse graining'
    target=None
    for p in root.rglob('*.tex'):
        text=p.read_text(errors='ignore'); q=text.lower().find(phrase.lower())
        if q>=0: target=(p,text,q); break
    if target is None: raise SystemExit('target phrase not found')
    p,text,q=target; tl=ln(text,q)
    choices=[(abs(ln(text,i)-tl),i,j,e) for i,j,e in envs(text) if abs(ln(text,i)-tl)<=80]
    if not choices: raise SystemExit('no nearby tikz environment')
    _,i,j,env=min(choices,key=lambda x:x[0])
    # Remove comments only; no semantic rewriting.
    body='\n'.join(re.sub(r'(?<!\\)%.*$','',x) for x in env.splitlines())
    token_re=re.compile(
      r'(?P<draw>\\draw\b(?:\s*\[[^\]]*\])?)|'
      r'(?P<node>node\s*(?:\[[^\]]*\])?\s*\{[^{}]*\})|'
      r'(?P<arc>arc\s*(?:\[[^\]]*\])?\s*\([^()]*\))|'
      r'(?P<coord>\([^()]{1,100}\))|'
      r'(?P<line>--)|(?P<vh>\|-)|(?P<hv>-\|)|'
      r'(?P<to>\bto\b(?:\s*\[[^\]]*\])?)|'
      r'(?P<controls>\.\.\s*controls\s*[^.]{0,160}?\.\.)', re.S)
    toks=[]
    for m in token_re.finditer(body):
        kind=m.lastgroup; raw=m.group(0); d={'kind':kind,'ordinal':len(toks),'token_sha256':sha(raw)}
        if kind=='coord': d['coordinate']=raw[1:-1].strip()
        elif kind=='node':
            om=re.search(r'node\s*(?:\[([^\]]*)\])?',raw,re.S); lm=re.search(r'\{([^{}]*)\}',raw,re.S)
            d['options']=[x.strip() for x in (om.group(1) if om and om.group(1) else '').split(',') if x.strip()]
            d['label']=clean_label(lm.group(1) if lm else '')
        elif kind=='draw':
            om=re.search(r'\[([^\]]*)\]',raw,re.S); d['options']=[x.strip() for x in (om.group(1) if om else '').split(',') if x.strip()]
        elif kind=='arc':
            om=re.search(r'\[([^\]]*)\]',raw,re.S); cm=re.search(r'\(([^()]*)\)',raw,re.S)
            d['options']=[x.strip() for x in (om.group(1) if om else '').split(',') if x.strip()]
            d['arc_spec']=cm.group(1).strip() if cm else ''
        elif kind=='to':
            om=re.search(r'\[([^\]]*)\]',raw,re.S); d['options']=[x.strip() for x in (om.group(1) if om else '').split(',') if x.strip()]
        toks.append(d)
    coords=[t['coordinate'] for t in toks if t['kind']=='coord']
    labels=[t.get('label','') for t in toks if t['kind']=='node' and t.get('label')]
    ops=[t['kind'] for t in toks if t['kind'] in {'line','vh','hv','to','arc','controls'}]
    out={'test':'RC006_EQ29_TIKZ_TOKEN_STREAM','source':'official arXiv 1609.02429 source archive',
         'tex_path':str(p.relative_to(root)),'tex_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
         'target_line':tl,'environment_line_start':ln(text,i),'environment_line_end':ln(text,j),
         'environment_sha256':sha(env),'token_count':len(toks),'coordinate_count':len(coords),
         'path_operator_sequence':ops,'labels':labels,'unique_labels':sorted(set(labels)),
         'has_required_labels':all(any(req in x for x in labels) for req in ('J^+','J^-','j','l_1','l_2')),
         'token_stream':toks,
         'claim_lock':'Derived TikZ structural token stream only; no graph contraction or Eq.(29) amplitude is implied.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='token_stream'},indent=2,sort_keys=True))
    if not (out['token_count']>0 and out['has_required_labels']): raise SystemExit(2)
if __name__=='__main__': main()
