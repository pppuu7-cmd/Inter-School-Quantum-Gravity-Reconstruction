#!/usr/bin/env python3
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
required=['analysis/iter161_endpoint_open_leg_factorization.py','analysis/iter163_complete_covariant_reconstruction.py','analysis/ITER163_TERMINAL_RESULT.md']
rows=[]; all_present=True; explicit_operation=False
for rel in required:
 p=ROOT/rel
 present=p.exists(); all_present &= present
 txt=p.read_text(encoding='utf-8',errors='ignore') if present else ''
 has_open=bool(re.search(r'open[-_ ]leg|open_vertex|open symmetric metric leg',txt,re.I))
 has_dist=bool(re.search(r'plus[-_ ]distribution|Hadamard|finite part|R[-_ ]operation|forest subtraction|BPHZ',txt,re.I))
 has_contact=bool(re.search(r'cancelled[-_ ]propagator|contact',txt,re.I))
 has_orient=bool(re.search(r'lower|upper|orientation',txt,re.I))
 # Documentation saying an operation is missing is not executable evidence.
 defs=bool(re.search(r'^def\s+\w*(?:endpoint|laurent|distribution|r_operation)\w*\s*\(',txt,re.I|re.M))
 sufficient=has_open and has_dist and has_contact and has_orient and defs and p.suffix=='.py'
 explicit_operation |= sufficient
 rows.append({'file':rel,'present':present,'open_leg':has_open,'distributional_semantics':has_dist,'contact_semantics':has_contact,'orientation_semantics':has_orient,'executable_candidate':defs,'sufficient':sufficient})
classification='PASS_SOURCE_OPERATION_AVAILABLE_CRITIC' if all_present and explicit_operation else ('BLOCKED_MISSING_SOURCE_OPERATION_CRITIC' if all_present else 'INFRASTRUCTURE_FAIL_MISSING_DEPENDENCY')
out={'gate':'ITER164_INDEPENDENT_CLOSURE_CRITIC','classification':classification,'dependencies':rows,'all_dependencies_present':all_present,'explicit_complete_operation_found':explicit_operation,'complete_pole_tensor_authorized':bool(all_present and explicit_operation),'locks':{'contacts_set_zero':False,'ITER118_MATCHING_AUTHORIZED':False,'BRIDGE_DERIVED':False,'candidate_theory':'UNFORMED / 0%'}}
Path('iter164_closure_critic.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
raise SystemExit(0 if all_present else 2)
