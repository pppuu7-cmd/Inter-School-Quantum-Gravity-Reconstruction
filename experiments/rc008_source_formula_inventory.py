#!/usr/bin/env python3
"""Source-provenance inventory for the RC008 quantum-cuboid amplitude/refinement gate.

The program inventories equation-bearing source regions using hashes and compact
metadata only. It deliberately does not fit published numbers or infer a bridge.
"""
from pathlib import Path
import argparse, hashlib, json, re

def h(x): return hashlib.sha256(x.encode()).hexdigest()

def display_regions(text: str):
    """Yield common source-native TeX display-math regions without interpreting them."""
    env_re=re.compile(
        r'\\begin\{(equation\*?|align\*?|alignat\*?|multline\*?|gather\*?|eqnarray\*?|split|IEEEeqnarray)\}'
        r'(.*?)\\end\{\1\}', re.S)
    for m in env_re.finditer(text):
        yield m.start(),m.end(),m.group(1),m.group(2)
    for name,pat in [
        ('display_brackets', re.compile(r'\\\[(.*?)\\\]',re.S)),
        ('double_dollar', re.compile(r'\$\$(.*?)\$\$',re.S)),
    ]:
        for m in pat.finditer(text):
            yield m.start(),m.end(),name,m.group(1)

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
    for p in sorted(root.rglob('*.tex')):
        text=p.read_text(errors='ignore'); low=text.lower(); combined.append(low)
        eqs=[]
        for start,end,env,body in display_regions(text):
            vicinity=low[max(0,start-800):min(len(low),end+800)]
            body_low=body.lower()
            if any(tok in body_low or tok in vicinity for tok in required):
                labels=re.findall(r'\\label\{([^{}]{1,100})\}',body)
                eqs.append({'environment':env,'sha256':h(body),'labels':labels[:10],
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
