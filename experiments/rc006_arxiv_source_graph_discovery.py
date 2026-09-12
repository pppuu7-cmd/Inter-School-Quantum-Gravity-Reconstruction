#!/usr/bin/env python3
"""Locate the Eq.(29)/EPRL-intertwiner source region in the official arXiv source.

Outputs metadata only: target TeX file, line/region hashes, macro inventory and
referenced asset names/hashes. It deliberately does not copy the article source
text into this repository.
"""
from pathlib import Path
import argparse, collections, hashlib, json, re

def sha(b): return hashlib.sha256(b).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    root=Path(a.source_dir)
    candidates=[]
    phrases=['EPRL intertwiner model','Before we discuss the behaviour of the EPRL model under coarse graining','Before we discuss the behavior of the EPRL model under coarse graining']
    for p in root.rglob('*.tex'):
      try: text=p.read_text(errors='ignore')
      except Exception: continue
      for ph in phrases:
        idx=text.lower().find(ph.lower())
        if idx>=0: candidates.append((0 if ph.startswith('Before') else 1,p,text,idx,ph))
    if not candidates:
      raise SystemExit('EPRL target phrase not found in arXiv TeX source')
    _,p,text,idx,ph=sorted(candidates,key=lambda x:(x[0],len(str(x[1]))))[0]
    line=text.count('\n',0,idx)+1
    lo=max(0,idx-2500); hi=min(len(text),idx+12000); region=text[lo:hi]
    macros=collections.Counter(re.findall(r'\\([A-Za-z@]+)',region))
    graphics=re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',region)
    inputs=re.findall(r'\\(?:input|include)\{([^}]+)\}',region)
    asset_meta=[]
    for g in sorted(set(graphics)):
      matches=[]
      gp=Path(g)
      for ext in ('','.pdf','.eps','.png','.jpg','.tex'):
        q=(p.parent/(str(gp)+ext))
        if q.exists() and q.is_file(): matches.append(q)
      for q in matches:
        b=q.read_bytes(); asset_meta.append({'reference':g,'path':str(q.relative_to(root)),'size':len(b),'sha256':sha(b),'suffix':q.suffix})
    markers={
      'has_sum_macro':'\\sum' in region,
      'has_includegraphics':bool(graphics),
      'has_tikz':('tikz' in region.lower()),
      'has_pstricks':('pspicture' in region.lower() or 'psfrag' in region.lower()),
      'has_xymatrix':('xymatrix' in region.lower()),
      'has_equation_environment':('\\begin{equation' in region),
      'has_eprl_token':('EPRL' in region),
      'has_alpha_token':('alpha' in region.lower()),
    }
    out={
      'test':'RC006_ARXIV_SOURCE_GRAPH_DISCOVERY',
      'target_tex_path':str(p.relative_to(root)),
      'target_phrase_class':ph,
      'target_line':line,
      'target_tex_sha256':sha(p.read_bytes()),
      'target_region_sha256':sha(region.encode()),
      'region_char_count':len(region),
      'macro_inventory_top40':macros.most_common(40),
      'referenced_graphics':sorted(set(graphics)),
      'referenced_inputs':sorted(set(inputs)),
      'resolved_asset_metadata':asset_meta,
      'structural_markers':markers,
      'discovery_success':True,
      'claim_lock':'Provenance/structure discovery only; no source equation or graph value is reconstructed by this metadata audit.'
    }
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
