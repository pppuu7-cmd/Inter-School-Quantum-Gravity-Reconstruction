#!/usr/bin/env python3
"""Extract a metadata-only AST for TikZ spin-network diagrams near RC-006 Eq.(29).

The official arXiv TeX source is parsed in-place during CI.  Output contains
command types, line numbers, coordinates, compact math labels, options and hashes,
not verbatim TeX environments.  This is a source-provenance/mapping prerequisite.
"""
from pathlib import Path
import argparse, hashlib, json, re

def h(s): return hashlib.sha256(s.encode()).hexdigest()

def line_of(text,pos): return text.count('\n',0,pos)+1

def balanced_envs(text,name='tikzpicture'):
    begin='\\begin{'+name+'}'; end='\\end{'+name+'}'
    out=[]; pos=0
    while True:
        a=text.find(begin,pos)
        if a<0: break
        b=text.find(end,a)
        if b<0: break
        b2=b+len(end); out.append((a,b2,text[a:b2])); pos=b2
    return out

def compact_label(s):
    s=' '.join(s.split())
    return s[:80]

def parse_env(env,base_line):
    commands=[]
    # Split only at TeX semicolons; retain derived fields, not raw command text.
    offset=0
    for chunk in env.split(';'):
        c=chunk.strip(); start=env.find(chunk,offset); offset=max(offset,start+len(chunk)+1)
        m=re.search(r'\\(draw|path|node|coordinate|filldraw|fill)\b',c)
        if not m: continue
        typ=m.group(1)
        opts=[]
        om=re.search(r'\\'+typ+r'\s*\[([^\]]*)\]',c,re.S)
        if om: opts=[x.strip() for x in om.group(1).split(',') if x.strip()][:20]
        coords=re.findall(r'\(([^()]{1,80})\)',c)
        math=re.findall(r'\$([^$]{1,120})\$',c)
        node_text=re.findall(r'node(?:\[[^\]]*\])?\s*\{([^{}]{0,120})\}',c,re.S)
        ops=[]
        for tok in ('--','|-','-|','to','arc','circle','controls'):
            if tok in c: ops.append(tok)
        commands.append({
            'type':typ,
            'line':base_line + env.count('\n',0,max(start,0)),
            'options':opts,
            'coordinates':[compact_label(x) for x in coords[:20]],
            'math_labels':[compact_label(x) for x in math[:20]],
            'node_text':[compact_label(x) for x in node_text[:20]],
            'edge_ops':ops,
            'command_sha256':h(c),
        })
    labels=[]
    for q in commands:
        labels += q['math_labels'] + q['node_text']
    return {'line_start':base_line,'line_end':base_line+env.count('\n'),
            'environment_sha256':h(env),'command_count':len(commands),
            'labels':sorted(set(labels)),'commands':commands}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    root=Path(a.source_dir)
    hits=[]
    phrase='Before we discuss the behaviour of the EPRL model under coarse graining'
    for p in root.rglob('*.tex'):
        text=p.read_text(errors='ignore')
        idx=text.lower().find(phrase.lower())
        if idx<0: continue
        target_line=line_of(text,idx)
        envs=[]
        for s,e,env in balanced_envs(text):
            ls=line_of(text,s)
            # Eq.(29) region and nearby derivational diagrams only.
            if abs(ls-target_line) <= 240:
                ast=parse_env(env,ls)
                ast['distance_to_target_line']=ls-target_line
                envs.append(ast)
        hits.append({'tex_path':str(p.relative_to(root)),'tex_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                     'target_line':target_line,'candidate_tikz_environment_count':len(envs),'tikz_environments':envs})
    if not hits: raise SystemExit('target EPRL source region not found')
    total=sum(x['candidate_tikz_environment_count'] for x in hits)
    labels=sorted(set(l for x in hits for e in x['tikz_environments'] for l in e['labels']))
    out={'test':'RC006_ARXIV_TIKZ_GRAPH_AST','source':'official arXiv 1609.02429 source archive',
         'target_region_count':len(hits),'candidate_tikz_environment_count':total,
         'unique_compact_labels':labels,
         'has_Jplus_like_label':any('J' in x and '+' in x for x in labels),
         'has_Jminus_like_label':any('J' in x and '-' in x for x in labels),
         'has_l_like_label':any('l' in x for x in labels),
         'mapping_prerequisite_pass':total>0,
         'regions':hits,
         'claim_lock':'Source graph AST/provenance only; no graph contraction or Eq.(29) amplitude is implied.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='regions'},indent=2,sort_keys=True))
    for r in hits:
        for i,e in enumerate(r['tikz_environments']):
            print(json.dumps({'env':i,'line_start':e['line_start'],'line_end':e['line_end'],'labels':e['labels'],'command_count':e['command_count']},sort_keys=True))
    if not out['mapping_prerequisite_pass']: raise SystemExit(2)
if __name__=='__main__': main()
