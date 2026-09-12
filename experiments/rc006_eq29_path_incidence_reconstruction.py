#!/usr/bin/env python3
"""Prospective source-faithful path/incidence reconstruction for the Eq.(29) TikZ graph.

This audit does not evaluate the EPRL/FK amplitude.  It tests whether the exact
official-source diagram has a deterministic structural reconstruction under
TeX-preserving lexical normalizations before any contraction is implemented.
"""
from pathlib import Path
import argparse, hashlib, json, re

TARGET = 'Before we discuss the behaviour of the EPRL model under coarse graining'
REQUIRED = ('J^+','J^-','j','l_1','l_2')

def sha(x: str) -> str:
    return hashlib.sha256(x.encode()).hexdigest()

def line_of(text: str, pos: int) -> int:
    return text.count('\n', 0, pos) + 1

def compact(x: str) -> str:
    return ' '.join(x.replace('$','').split())

def find_environment(text: str, target_pos: int):
    b='\\begin{tikzpicture}'; e='\\end{tikzpicture}'
    target_line=line_of(text,target_pos); candidates=[]; p=0
    while True:
        i=text.find(b,p)
        if i < 0: break
        j=text.find(e,i)
        if j < 0: break
        j += len(e)
        d=abs(line_of(text,i)-target_line)
        if d <= 80: candidates.append((d,i,j,text[i:j]))
        p=j
    if not candidates: raise RuntimeError('no nearby tikz environment')
    _,i,j,env=min(candidates,key=lambda z:z[0])
    return i,j,env

def normalize(env: str, mode: str) -> str:
    # All modes are intended to preserve TeX path semantics.
    no_comments='\n'.join(re.sub(r'(?<!\\)%.*$','',x) for x in env.splitlines())
    if mode == 'raw_comments_removed': return no_comments
    if mode == 'trim_lines': return '\n'.join(x.strip() for x in no_comments.splitlines())
    if mode == 'collapse_spaces': return re.sub(r'[ \t]+',' ',no_comments)
    if mode == 'compact_linebreaks': return re.sub(r'\s*\n\s*',' ',no_comments)
    raise ValueError(mode)

def parse_draws(body: str):
    records=[]
    for chunk in body.split(';'):
        if not re.search(r'\\(draw|path)\b',chunk): continue
        typ=re.search(r'\\(draw|path)\b',chunk).group(1)
        opts=[]
        om=re.search(r'\\'+typ+r'\s*\[([^\]]*)\]',chunk,re.S)
        if om: opts=[compact(x) for x in om.group(1).split(',') if compact(x)]
        coords=[compact(x) for x in re.findall(r'\(([^()]{1,120})\)',chunk,re.S)]
        labels=[compact(x) for x in re.findall(r'node(?:\[[^\]]*\])?\s*\{([^{}]{0,160})\}',chunk,re.S)]
        ops=[]
        token_re=re.compile(r'(?P<arc>arc\s*(?:\[[^\]]*\])?\s*\([^()]*\))|(?P<line>--)|(?P<vh>\|-)|(?P<hv>-\|)|(?P<to>\bto\b(?:\s*\[[^\]]*\])?)|(?P<controls>\.\.\s*controls\s*[^.]{0,160}?\.\.)',re.S)
        arcs=[]
        for m in token_re.finditer(chunk):
            ops.append(m.lastgroup)
            if m.lastgroup=='arc':
                am=re.search(r'\(([^()]*)\)',m.group(0),re.S)
                arcs.append(compact(am.group(1) if am else ''))
        records.append({'type':typ,'options':opts,'coordinates':coords,'labels':labels,'operators':ops,'arcs':arcs})
    return records

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source-dir',required=True)
    ap.add_argument('--mode',required=True,choices=['raw_comments_removed','trim_lines','collapse_spaces','compact_linebreaks'])
    ap.add_argument('--output',required=True)
    a=ap.parse_args()
    root=Path(a.source_dir); found=None
    for p in root.rglob('*.tex'):
        text=p.read_text(errors='ignore'); q=text.lower().find(TARGET.lower())
        if q >= 0: found=(p,text,q); break
    if not found: raise SystemExit('target source region not found')
    p,text,q=found; i,j,env=find_environment(text,q)
    body=normalize(env,a.mode); records=parse_draws(body)
    labels=[x for r in records for x in r['labels']]
    required_ok=all(any(req in lab for lab in labels) for req in REQUIRED)
    path_valid=bool(records) and all(len(r['operators'])>0 for r in records)
    # Signature excludes lexical formatting and source positions by construction.
    signature=sha(json.dumps(records,sort_keys=True,separators=(',',':')))
    out={
      'test':'RC006_EQ29_PATH_INCIDENCE_RECONSTRUCTION',
      'mode':a.mode,
      'source':'official arXiv 1609.02429 source archive',
      'tex_path':str(p.relative_to(root)),
      'tex_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
      'target_line':line_of(text,q),
      'environment_line_start':line_of(text,i),
      'environment_line_end':line_of(text,j),
      'environment_sha256':sha(env),
      'draw_path_count':len(records),
      'labels':labels,
      'required_labels_pass':required_ok,
      'all_paths_have_operator_pass':path_valid,
      'structural_signature':signature,
      'records':records,
      'claim_lock':'Source-diagram structural reconstruction only; no Eq.(29) contraction or amplitude is implied.'
    }
    out['lane_pass']=required_ok and path_valid
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2,sort_keys=True))
    if not out['lane_pass']: raise SystemExit(2)

if __name__=='__main__': main()
