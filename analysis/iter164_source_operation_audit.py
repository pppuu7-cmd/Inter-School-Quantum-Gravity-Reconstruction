#!/usr/bin/env python3
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
KEYS={
 'distributional_extension':r'distribution|plus[-_ ]distribution|Hadamard|finite part',
 'r_operation':r'R[-_ ]operation|forest subtraction|BPHZ',
 'laurent_pole':r'Laurent|1/epsilon|1/\\epsilon|pole tensor|pole extraction',
 'contact':r'contact|cancelled[-_ ]propagator|counterterm',
 'orientation':r'orientation|lower endpoint|upper endpoint|endpoint-selected',
 'open_leg':r'open[-_ ]leg|open symmetric metric leg|upper_open_vertex|lower_open_vertex',
}
files=[]
for base in ('analysis','docs','recovery'):
 p=ROOT/base
 if p.exists(): files += [x for x in p.rglob('*') if x.is_file() and x.suffix in {'.py','.md','.json','.txt'}]
# Exclude this audit and prereg from evidence so the gate cannot self-satisfy.
files=[p for p in files if p.name not in {'iter164_source_operation_audit.py','ITER164_PREREG.md'}]
hits={k:[] for k in KEYS}
for p in files:
 try: lines=p.read_text(encoding='utf-8',errors='ignore').splitlines()
 except Exception: continue
 for i,line in enumerate(lines,1):
  for k,pat in KEYS.items():
   if re.search(pat,line,re.I): hits[k].append({'file':str(p.relative_to(ROOT)),'line':i,'text':line.strip()[:240]})
# Executable sufficiency is intentionally strict and frozen: a Python definition must itself
# identify an endpoint/open-leg operation and distributional/R-operation semantics, while the
# same source file must explicitly retain contact and orientation treatment.
candidates=[]
for p in files:
 if p.suffix!='.py': continue
 txt=p.read_text(encoding='utf-8',errors='ignore')
 for m in re.finditer(r'^def\s+([A-Za-z0-9_]+)\s*\(',txt,re.M):
  name=m.group(1); lo=max(0,m.start()-600); hi=min(len(txt),m.start()+5000); block=txt[lo:hi]
  semantic=bool(re.search(r'(distribution|R[-_ ]operation|Hadamard|finite part|plus[-_ ]distribution)',block,re.I))
  endpoint=bool(re.search(r'(endpoint|open[-_ ]leg|upper_open_vertex|lower_open_vertex)',block,re.I))
  contact=bool(re.search(r'(contact|cancelled[-_ ]propagator|counterterm)',block,re.I))
  orient=bool(re.search(r'(orientation|lower endpoint|upper endpoint)',block,re.I))
  if semantic and endpoint: candidates.append({'file':str(p.relative_to(ROOT)),'function':name,'contact_explicit':contact,'orientation_explicit':orient,'sufficient':semantic and endpoint and contact and orient})
sufficient=[c for c in candidates if c['sufficient']]
classification='PASS_SOURCE_OPERATION_AVAILABLE' if sufficient else 'BLOCKED_MISSING_SOURCE_OPERATION'
out={'gate':'ITER164_SOURCE_OPERATION_AVAILABILITY','classification':classification,'scientific_pass':bool(sufficient),'files_scanned':len(files),'hit_counts':{k:len(v) for k,v in hits.items()},'hits':hits,'candidate_executable_operations':candidates,'sufficient_operations':sufficient,'locks':{'contacts_set_zero':False,'ITER118_MATCHING_AUTHORIZED':False,'BRIDGE_DERIVED':False,'candidate_theory':'UNFORMED / 0%'}}
Path('iter164_source_operation_audit.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='hits'},indent=2,sort_keys=True))
