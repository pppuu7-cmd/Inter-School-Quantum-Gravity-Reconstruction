#!/usr/bin/env python3
"""ITER132 frozen prerequisite audit. Does not invent missing geodesic kernels."""
import json, pathlib, re
root=pathlib.Path('.')
required={'ITER131_R2_Gamma2':'analysis/iter131_explicit_momentum_vertices.py','ITER129_ceilings':'analysis/iter129_graph_derivative_ceiling_table.json'}
files={k:(root/v).exists() for k,v in required.items()}
patterns={'chi1_kernel':re.compile(r'def\s+chi1\b|chi1_kernel\s*='),'chi2_kernel':re.compile(r'def\s+chi2\b|chi2_kernel\s*='),'dR1_tensor':re.compile(r'def\s+dR1\b|dR1_tensor\s*='),'dR2_tensor':re.compile(r'def\s+dR2\b|dR2_tensor\s*=')}
hits={k:[] for k in patterns}
for p in (root/'analysis').glob('*.py'):
 if p.name==pathlib.Path(__file__).name: continue
 txt=p.read_text(errors='ignore')
 for k,pat in patterns.items():
  if pat.search(txt): hits[k].append(str(p))
mg_families=['M_R2_chi1_dR1','M_R1_chi1_dR2','M_R1_chi1_dR1_S3','G_R1_chi2_Gamma2_dR1','G_R1_chi2_Gamma1_dchi1_dR1','G_R1_chi2_dGamma1_chi1_dR1','G_R1_chi1chi1_d2R1']
missing=[k for k,v in hits.items() if not v]
classification='BLOCKED_MISSING_PREREQUISITE' if missing else 'READY_FOR_EXPLICIT_NUMERATOR_JETS'
out={'gate':'ITER132_GAUSSIAN_MG_NUMERATOR_JET','classification':classification,'locked_iter131_head':'da613bc5cc9bff6b68ff1423f7aec06f5a30a28c','required_files':files,'admitted_families':mg_families,'symbolic_kernel_hits':hits,'missing_symbolic_objects':missing,'scientific_note':'No scalar/derivative-counting surrogate is substituted for a missing fixed-geodesic localization tensor kernel.','claim_ceiling':'prerequisite audit only; no pole/B1/EDT match/bridge/new physics/candidate theory'}
open('iter132_prerequisite_audit.json','w').write(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
if not all(files.values()): raise SystemExit(2)
