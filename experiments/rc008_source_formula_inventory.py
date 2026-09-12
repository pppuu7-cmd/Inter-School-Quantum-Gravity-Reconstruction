#!/usr/bin/env python3
"""Source-provenance inventory for the RC008 quantum-cuboid amplitude/refinement gate.

The program inventories equation-bearing source regions using hashes and compact
metadata only.  It deliberately does not fit published numbers or infer a bridge.
"""
from pathlib import Path
import argparse, hashlib, json, re

def h(x): return hashlib.sha256(x.encode()).hexdigest()
def compact(x): return ' '.join(x.split())

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source-dir',required=True)
    ap.add_argument('--arxiv-id',required=True)
    ap.add_argument('--role',required=True,choices=['amplitude','phase','renormalization'])
    ap.add_argument('--output',required=True)
    a=ap.parse_args(); root=Path(a.source_dir)
    required={
      'amplitude':['vertex','amplitude','cuboid'],
      'phase':['alpha','cuboid','vertex'],
      'renormalization':['alpha','volume','refin']
    }[a.role]
    files=[]; combined=[]
    eq_re=re.compile(r'\\begin\{(equation\*?|align\*?|multline\*?|gather\*?)\}(.*?)\\end\{\1\}',re.S)
    for p in sorted(root.rglob('*.tex')):
        text=p.read_text(errors='ignore'); low=text.lower(); combined.append(low)
        eqs=[]
        for m in eq_re.finditer(text):
            body=m.group(2)
            b_low=body.lower()
            score=sum(tok in b_low for tok in required)
            if score or any(tok in low[max(0,m.start()-500):min(len(low),m.end()+500)] for tok in required):
                labels=re.findall(r'\\label\{([^{}]{1,100})\}',body)
                eqs.append({'environment':m.group(1),'sha256':h(body),'labels':labels[:10],
                            'char_count':len(body)})
        if eqs:
            files.append({'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                          'candidate_equations':eqs})
    alltext='\n'.join(combined)
    keyword_presence={tok:(tok in alltext) for tok in required}
    eq_count=sum(len(x['candidate_equations']) for x in files)
    out={
      'test':'RC008_SOURCE_FORMULA_INVENTORY', 'arxiv_id':a.arxiv_id, 'role':a.role,
      'required_keywords':required, 'keyword_presence':keyword_presence,
      'tex_files_with_candidate_equations':len(files), 'candidate_equation_count':eq_count,
      'files':files,
      'source_qualification_pass':all(keyword_presence.values()) and eq_count>0,
      'claim_lock':'Official-source formula inventory only; no RC008 amplitude reproduction or RG fixed-point recomputation is implied.'
    }
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='files'},indent=2,sort_keys=True))
    if not out['source_qualification_pass']: raise SystemExit(2)

if __name__=='__main__': main()
