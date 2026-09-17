#!/usr/bin/env python3
import json, pathlib, re
ROOT=pathlib.Path(__file__).resolve().parents[1]
BASIS=['R','S','DR','DS','BoxR','D2R','BoxS','D2S']
# Lane B: require genuinely microscopic ingredients, not result/analysis prose.
patterns={
 'graviton_propagator':[r'graviton propagator',r'P_?\{?mu',r'D_{mu'],
 'geodesic_perturbation':[r'chi.?1',r'chi.?2',r'geodesic perturb'],
 'first_mg_vertex':[r'first[-_ ]?M/?G',r'mixed geodesic',r'M/G'],
 'general_d_regulator':[r'general[- ]d',r'dimensional regular',r'1/epsilon'],
 'endpoint_support_rule':[r'endpoint support',r'tau.?=.?0',r'tau.?=.?1'],
 'r_operation':[r'R-operation',r'subdiverg',r'counterterm']}
exclude=('analysis/ITER15','recovery/','.git/','.github/','scripts/iter158')
hits={k:[] for k in patterns}
for p in ROOT.rglob('*'):
 if not p.is_file() or any(str(p.relative_to(ROOT)).startswith(x) for x in exclude): continue
 try: txt=p.read_text(errors='ignore')
 except: continue
 for k,ps in patterns.items():
  if any(re.search(q,txt,re.I) for q in ps): hits[k].append(str(p.relative_to(ROOT)))
missing=[k for k,v in hits.items() if not v]
# Lane A is deliberately conservative: external source seed is frozen in preregistration,
# but CI cannot claim a convention map unless a checked-in primary-source convention manifest exists.
manifest=ROOT/'inputs'/'iter158_primary_source_convention_manifest.json'
lane_a='AVAILABLE_FOR_AUDIT' if manifest.exists() else 'BLOCKED_NO_CHECKED_IN_EXACT_CONVENTION_MANIFEST'
if missing:
 classification='BLOCKED_SCOPED_ITER158_EARLIEST_MICROSCOPIC_PRIMITIVE_MISSING'
 earliest=missing[0]
else:
 classification='BLOCKED_SCOPED_ITER158_PRIMARY_SOURCE_CONVENTION_MAP_INCOMPLETE'
 earliest=None
out={'gate':'ITER158','basis':BASIS,'lane_a':lane_a,'lane_b_hits':hits,'missing_primitives':missing,'earliest_missing_primitive':earliest,'classification':classification,'automatic_scientific_pass':False,'bridge_credit':False,'candidate_theory_authorized':False}
path=ROOT/'artifacts'/'iter158_endpoint_tensor_acquisition.json'; path.parent.mkdir(exist_ok=True); path.write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True))
