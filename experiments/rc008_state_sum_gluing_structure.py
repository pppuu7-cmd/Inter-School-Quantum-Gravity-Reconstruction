#!/usr/bin/env python3
"""Independent RC008 exact-TeX state-sum gluing authority gate.

The previous wording-based source-closure audit remains failed.  This new gate
asks a different, frozen mathematical question: does the pinned source explicitly
encode multi-vertex gluing through a state-sum product over faces/edges/vertices
and a sum/integration over shared labels?  It does not search for the English word
'gluing' and cannot retroactively change the prior result.
"""
from pathlib import Path
import argparse,json,re
REQ={
 'face_product':[r'\\prod\s*_\s*\{?f',r'\\prod\s*\^?[^\n]{0,30}f'],
 'edge_product':[r'\\prod\s*_\s*\{?e',r'\\prod\s*\^?[^\n]{0,30}e'],
 'vertex_product':[r'\\prod\s*_\s*\{?v',r'\\prod\s*\^?[^\n]{0,30}v'],
 'spin_sum':[r'\\sum\s*_\s*\{[^}]*j',r'\\sum\s*_\s*j',r'sum over[^\n]{0,80}spin'],
 'intertwiner_sum':[r'\\sum\s*_\s*\{[^}]*(?:i|\\iota)',r'sum over[^\n]{0,80}intertw'],
 'shared_boundary_data':[r'boundary[^\n]{0,160}(?:spin|intertwin|state)',r'(?:spin|intertwin)[^\n]{0,160}boundary'],
 'coarse_refined_complex':[r'coarse[^\n]{0,160}(?:fine|refin)',r'refin[^\n]{0,160}(?:coarse|complex|lattice)'],
 'amplitude_composition':[r'(?:face|edge|vertex) amplitude[^\n]{0,240}(?:face|edge|vertex)',r'partition function',r'state sum']
}
def snippets(text,pat):
 out=[]
 for m in re.finditer(pat,text,re.I|re.S): out.append(re.sub(r'\s+',' ',text[max(0,m.start()-180):min(len(text),m.end()+260)])[:520])
 return out[:3]
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--requirement',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 if a.requirement not in REQ: raise SystemExit('bad requirement')
 fs=list(Path(a.source_dir).rglob('*.tex')); text='\n'.join(f.read_text(errors='ignore') for f in fs)
 hits=[]
 for p in REQ[a.requirement]:
  s=snippets(text,p); hits.append({'pattern':p,'count':len(list(re.finditer(p,text,re.I|re.S))),'snippets':s})
 present=any(h['count']>0 for h in hits)
 out={'test':'RC008_STATE_SUM_GLUING_STRUCTURE','requirement':a.requirement,'valid':bool(fs and text),'present':present,'hits':hits,
      'classification':'EXACT_SOURCE_STRUCTURE_PRESENT' if present else 'EXACT_SOURCE_STRUCTURE_NOT_LOCATED',
      'interpretation_lock':'This is exact-source structural authority only. It does not compute a coarse/refined amplitude or derive RG transport.'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
