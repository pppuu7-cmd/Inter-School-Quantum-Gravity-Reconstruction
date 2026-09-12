#!/usr/bin/env python3
"""Machine-readable structural AST for selected RC008 source equations.

Extracts operator/symbol/dependency structure around a labelled equation from the
official source without copying the equation text. This is the final provenance
layer before an executable restricted hypercuboid implementation.
"""
from pathlib import Path
import argparse,hashlib,json,re

def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def find_region(text,pos):
    starts=[]
    for pat in [r'\\begin\{equation\*?\}',r'\\begin\{align\*?\}',r'\\begin\{eqnarray\*?\}',r'\\\[',r'\$\$']:
        for m in re.finditer(pat,text[:pos],re.S): starts.append((m.start(),pat))
    if not starts: return max(0,pos-800),min(len(text),pos+800)
    s=max(starts)[0]
    ends=[m.end() for m in re.finditer(r'\\end\{(?:equation\*?|align\*?|eqnarray\*?)\}|\\\]|\$\$',text[pos:],re.S)]
    e=pos+(min(ends) if ends else min(1600,len(text)-pos))
    return s,e

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source-dir',required=True);ap.add_argument('--label',required=True);ap.add_argument('--output',required=True);a=ap.parse_args();root=Path(a.source_dir)
    rec=None
    for p in root.rglob('*.tex'):
        t=p.read_text(errors='ignore');needle='\\label{'+a.label+'}';pos=t.find(needle)
        if pos<0:continue
        s,e=find_region(t,pos);body=t[s:e]
        macros=sorted(set(re.findall(r'\\([A-Za-z@]+)',body)))
        refs=sorted(set(re.findall(r'\\(?:eqref|ref)\{([^{}]+)\}',body)))
        symbols=sorted(set(re.findall(r'(?<![A-Za-z])([A-Za-z](?:_[A-Za-z0-9{}+\-]+|\^[A-Za-z0-9{}+\-]+)?)',re.sub(r'\\[A-Za-z@]+',' ',body))))
        ops={x:bool(re.search(pat,body)) for x,pat in {'integral':r'\\int','sum':r'\\sum','product':r'\\prod','determinant':r'\\det','exponential':r'\\exp','logarithm':r'\\ln','limit':r'\\lim','derivative':r'\\partial'}.items()}
        rec={'label':a.label,'path':str(p.relative_to(root)),'file_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'region_sha256':sha(' '.join(body.split())),'region_char_count':len(body),'macros':macros,'references':refs,'symbol_tokens':symbols[:200],'operators':ops};break
    ok=rec is not None and len(rec['macros'])>0
    out={'test':'RC008_EQUATION_STRUCTURE_AST','label':a.label,'record':rec,'frozen_gate_pass':ok,'claim_lock':'Structural source AST only; no numerical amplitude/refinement result.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='record'},indent=2,sort_keys=True));
    if not ok:raise SystemExit(2)
if __name__=='__main__':main()
