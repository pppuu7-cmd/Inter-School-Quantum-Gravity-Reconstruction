#!/usr/bin/env python3
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXCLUDE=('PREREG','TERMINAL','CURRENT_FRONT','NAVIGATOR','RESULT','recovery/')
TEXT_EXT={'.py','.json','.yaml','.yml','.toml','.csv','.tsv'}

def eligible(p):
 s=p.relative_to(ROOT).as_posix()
 return p.suffix.lower() in TEXT_EXT and not any(x.lower() in s.lower() for x in EXCLUDE) and '.github/workflows/' not in s

def scan():
 hits=[]
 pats=re.compile(r'(denom|propagator|phase|endpoint|affine|lorentz|delta4|contact|cancelled|K\b|Q\b)',re.I)
 for p in ROOT.rglob('*'):
  if not p.is_file() or not eligible(p): continue
  try: lines=p.read_text(errors='ignore').splitlines()
  except Exception: continue
  for i,l in enumerate(lines,1):
   if pats.search(l): hits.append({'path':p.relative_to(ROOT).as_posix(),'line':i,'text':l[:300]})
 return hits

def main(lane):
 hits=scan(); paths=sorted({h['path'] for h in hits})
 iter163=[h for h in hits if 'iter163' in h['path'].lower()]
 # Frozen semantic requirement: an eligible object must encode geometry, not merely ledger labels.
 geom=re.compile(r'(1\s*/|denom|propagator|phase|exp\s*\(|endpoint.*(?:=|\+|\-|\*)|affine.*(?:=|\+|\-|\*))',re.I)
 geom163=[h for h in iter163 if geom.search(h['text'])]
 hardcoded=[h for h in iter163 if re.search(r'(QQ|QK|KQ|TERM_ROWS|ledger)',h['text'],re.I)]
 out={'iteration':168,'lane':lane,'eligible_candidate_paths':paths,'iter163_hits':iter163,'iter163_geometry_hits':geom163,'iter163_bookkeeping_hits':hardcoded}
 if lane=='extractor':
  out['classification']='PASS_SCOPED_SUBCHECK_EXECUTABLE_PROVENANCE' if geom163 else 'BLOCKED_MISSING_SOURCE_EXPRESSION'
 elif lane=='leakage_critic':
  out['classification']='BLOCKED_PROVENANCE_LEAKAGE_OR_BOOKKEEPING_ONLY' if hardcoded and not geom163 else ('PASS_SCOPED_SUBCHECK_NO_LEAKAGE' if geom163 else 'BLOCKED_MISSING_SOURCE_EXPRESSION')
 else:
  out['classification']='PASS_SCOPED_SUBCHECK_COMPLETENESS_ELIGIBLE_SOURCE_PRESENT' if geom163 else 'BLOCKED_MISSING_SOURCE_EXPRESSION'
 print(json.dumps(out,indent=2))
 Path(f'iter168_{lane}.json').write_text(json.dumps(out,indent=2))

if __name__=='__main__':
 import sys
 main(sys.argv[1] if len(sys.argv)>1 else 'extractor')
