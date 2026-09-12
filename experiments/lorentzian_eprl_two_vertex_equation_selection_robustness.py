#!/usr/bin/env python3
"""Equation-selection robustness for arXiv:1801.03771.

After source/equation extraction PASS, verify that the nearest exact math object
selected for each numerical target is stable under leave-one-anchor-pattern-out.
This prevents implementing a neighboring formula chosen only by one lexical cue.
PASS is a source lock only, not an amplitude/refinement result.
"""
from pathlib import Path
import argparse,hashlib,json,re
TARGETS={
 'two_vertex_amplitude':[r'two[- ]vertex',r'transition amplitude',r'amplitude'],
 'internal_face_sum':[r'internal face',r'bulk face',r'\\sum'],
 'full_amplitude':[r'full EPRL',r'full amplitude'],
 'simplified_amplitude':[r'simplified EPRL',r'simplified amplitude'],
 'correlation_observable':[r'correlation',r'correlator'],
 'large_spin_scaling':[r'large spin',r'asymptotic',r'power[- ]law'],
 'immirzi':[r'Immirzi',r'gamma'],
 'cutoff_or_truncation':[r'cutoff',r'truncat',r'virtual spin',r'booster']
}
MATH=[r'\\begin\{equation\*?\}(.*?)\\end\{equation\*?\}',r'\\begin\{align\*?\}(.*?)\\end\{align\*?\}',r'\\\[(.*?)\\\]']
def envs(text):
 out=[]
 for pat in MATH:
  for m in re.finditer(pat,text,re.S): out.append((m.start(),m.end(),m.group(0)))
 return sorted(out)
def norm(s): return re.sub(r'\s+','',s)
def select(text,ee,patterns):
 cand=[]
 for p in patterns:
  for m in re.finditer(p,text,re.I|re.S):
   pos=m.start()
   if not ee: continue
   z=min(ee,key=lambda e:min(abs(e[0]-pos),abs(e[1]-pos)))
   dist=min(abs(z[0]-pos),abs(z[1]-pos))
   if dist<=2500: cand.append((dist,z[2],p))
 if not cand:return None
 cand.sort(key=lambda x:x[0]); raw=cand[0][1]
 return {'distance':cand[0][0],'hash':hashlib.sha256(norm(raw).encode()).hexdigest(),'math':raw[:5000],'anchor_pattern':cand[0][2]}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--target',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 pats=TARGETS[a.target]; fs=list(Path(a.source_dir).rglob('*.tex')); text='\n'.join(f.read_text(errors='ignore') for f in fs); ee=envs(text)
 full=select(text,ee,pats); hold=[]
 for i in range(len(pats)):
  q=pats[:i]+pats[i+1:]; s=select(text,ee,q) if q else None; hold.append({'drop_index':i,'drop_pattern':pats[i],'selection':s})
 valid=bool(fs and text and ee and full)
 usable=[h for h in hold if h['selection']]
 agreements=[h['selection']['hash']==full['hash'] for h in usable]
 stable=bool(valid and usable and all(agreements))
 out={'test':'LORENTZIAN_EPRL_TWO_VERTEX_EQUATION_SELECTION_ROBUSTNESS','target':a.target,'valid':valid,
      'full_selection_hash':full['hash'] if full else None,'full_distance':full['distance'] if full else None,
      'holdout_count':len(hold),'usable_holdout_count':len(usable),'stable_holdout_count':sum(agreements),'selection_stable':stable,
      'holdouts':hold,'classification':'SOURCE_EQUATION_SELECTION_STABLE' if stable else ('SOURCE_EQUATION_SELECTION_UNSTABLE' if valid else 'INVALID_COMPUTATION'),
      'interpretation_lock':'Source lock only. Failure blocks implementation of this target until source authority is disambiguated; thresholds are not relaxed.'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='holdouts'},indent=2,sort_keys=True))
if __name__=='__main__': main()
