#!/usr/bin/env python3
"""RC008 source-closure audit for a genuine coarse/refined amplitude calculation.

This is a source-authority test, not a physics PASS.  It asks whether the pinned
arXiv source 1508.07961 explicitly contains each object needed to reconstruct a
coarse/refined hypercuboid amplitude without importing an unstated gluing rule.
"""
from pathlib import Path
import argparse,json,re
REQ={
 'vertex_amplitude':[r'VertexDefinition',r'vertex amplitude'],
 'face_weight':[r'face amplitude',r'face weight',r'j_f\^\{?2\\alpha'],
 'edge_norm':[r'edge amplitude',r'intertwiner norm',r'edge.*norm'],
 'state_sum':[r'AsymptoticStateSum',r'state sum',r'partition function'],
 'quantum_cuboid':[r'QuantumCuboid',r'quantum cuboid'],
 'volume_simplicity':[r'4Volume',r'volume simplicity',r'volume constraint'],
 'coarse_graining_map':[r'coarse.?grain',r'renormalization',r'refinement'],
 'explicit_multi_vertex_gluing':[r'gluing',r'internal face',r'multi.?vertex',r'16 hypercub',r'2\^4']
}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--requirement',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 if a.requirement not in REQ: raise SystemExit('bad requirement')
 fs=list(Path(a.source_dir).rglob('*.tex')); text='\n'.join(f.read_text(errors='ignore') for f in fs)
 hits=[]
 for p in REQ[a.requirement]:
  ms=list(re.finditer(p,text,re.I|re.S)); hits.append({'pattern':p,'count':len(ms),'examples':[re.sub(r'\s+',' ',text[max(0,m.start()-100):min(len(text),m.end()+160)])[:320] for m in ms[:2]]})
 present=any(x['count'] for x in hits)
 out={'test':'RC008_REFINEMENT_SOURCE_CLOSURE','requirement':a.requirement,'valid':bool(fs and text),'present':present,'patterns':hits,
      'classification':'SOURCE_OBJECT_PRESENT' if present else 'SOURCE_OBJECT_NOT_LOCATED',
      'interpretation_lock':'Presence is only source-authority evidence. Absence blocks source-only reconstruction but does not show the physical model lacks the object elsewhere.'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
