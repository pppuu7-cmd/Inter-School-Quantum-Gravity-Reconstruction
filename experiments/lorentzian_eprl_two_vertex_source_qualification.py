#!/usr/bin/env python3
"""Source qualification for genuine two-vertex Lorentzian EPRL dipole amplitudes.

Pinned source: arXiv:1801.03771 (Sarno, Speziale, Stagno).
This prerequisite asks whether the source explicitly contains the ingredients
needed for a nontrivial multi-vertex amplitude benchmark before any numerical
reimplementation is attempted.  It is not itself a refinement-map PASS.
"""
from pathlib import Path
import argparse,json,re
REQ={
 'two_vertex':[r'two[- ]vertex',r'2[- ]vertex',r'two vertices'],
 'lorentzian_eprl':[r'Lorentzian[^\n]{0,100}EPRL',r'EPRL[^\n]{0,100}Lorentzian'],
 'internal_face':[r'internal face',r'bulk face'],
 'bulk_sum':[r'bulk[^\n]{0,120}(?:sum|spin|intertw)',r'\\sum[^\n]{0,120}(?:l|k|j)'],
 'full_vs_simplified':[r'simplified EPRL',r'full[^\n]{0,100}simplified',r'simplified[^\n]{0,100}full'],
 'large_spin_scaling':[r'large spin',r'power[- ]law',r'asymptotic'],
 'boundary_correlation':[r'correlation',r'dipole'],
 'immirzi_dependence':[r'Immirzi',r'gamma']
}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--requirement',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 if a.requirement not in REQ: raise SystemExit('bad requirement')
 fs=list(Path(a.source_dir).rglob('*.tex')); text='\n'.join(f.read_text(errors='ignore') for f in fs)
 rows=[]
 for p in REQ[a.requirement]:
  ms=list(re.finditer(p,text,re.I|re.S)); rows.append({'pattern':p,'count':len(ms),'snippets':[re.sub(r'\s+',' ',text[max(0,m.start()-150):min(len(text),m.end()+250)])[:480] for m in ms[:2]]})
 present=any(x['count']>0 for x in rows)
 out={'test':'LORENTZIAN_EPRL_TWO_VERTEX_SOURCE_QUALIFICATION','source':'arXiv:1801.03771','requirement':a.requirement,'valid':bool(fs and text),'present':present,'matches':rows,
      'classification':'SOURCE_OBJECT_PRESENT' if present else 'SOURCE_OBJECT_NOT_LOCATED',
      'interpretation_lock':'Source qualification only; no refinement map, continuum limit, bridge, or candidate-theory claim.'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
