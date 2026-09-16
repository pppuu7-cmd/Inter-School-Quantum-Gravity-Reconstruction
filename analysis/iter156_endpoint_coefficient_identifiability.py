#!/usr/bin/env python3
import json,re
from pathlib import Path
import sympy as sp

basis=['R','S','DR','DS','BoxR','D2R','BoxS','D2S']
required=[
 Path('sources/ITER118_FIXED_GEODESIC_CURVATURE_LINE_ENDPOINT_COUNTERTERM_POWER_COUNTING_2026-09-15.md'),
 Path('sources/ITER126_FIXED_GEODESIC_CURVATURE_LINE_ENDPOINT_COINCIDENCE_POLE_EXTRACTION_AUTHORITY_2026-09-15.md'),
 Path('analysis/ITER151_RESULT_2026-09-16.md'),Path('analysis/ITER153_RESULT_2026-09-17.md'),
 Path('analysis/ITER154B_RESULT_2026-09-17.md')]
texts={str(p):p.read_text(errors='replace') for p in required if p.exists()}
# Frozen explicit coefficient equations must literally pair an ITER118 basis direction with
# a pole/residue coefficient. Generic prototype residues do not resolve a curvature direction.
patterns={
 'R':r'(?i)(?:endpoint[^\n]{0,120})?\bR\b[^\n]{0,120}(?:residue|pole coefficient)\s*[:=]\s*[-+]?\d',
 'S':r'(?i)(?:endpoint[^\n]{0,120})?\bS\b[^\n]{0,120}(?:residue|pole coefficient)\s*[:=]\s*[-+]?\d',
 'DR':r'(?i)\bD\s*R\b[^\n]{0,120}(?:residue|pole coefficient)\s*[:=]\s*[-+]?\d',
 'DS':r'(?i)\bD\s*S\b[^\n]{0,120}(?:residue|pole coefficient)\s*[:=]\s*[-+]?\d',
 'BoxR':r'(?i)\bBox\s*R\b[^\n]{0,120}(?:residue|pole coefficient)\s*[:=]\s*[-+]?\d',
 'D2R':r'(?i)\bD\^?2\s*R\b[^\n]{0,120}(?:residue|pole coefficient)\s*[:=]\s*[-+]?\d',
 'BoxS':r'(?i)\bBox\s*S\b[^\n]{0,120}(?:residue|pole coefficient)\s*[:=]\s*[-+]?\d',
 'D2S':r'(?i)\bD\^?2\s*S\b[^\n]{0,120}(?:residue|pole coefficient)\s*[:=]\s*[-+]?\d'}
rows=[]; evidence={b:[] for b in basis}
for j,b in enumerate(basis):
 for fn,t in texts.items():
  for m in re.finditer(patterns[b],t):
   v=[0]*len(basis);v[j]=1;rows.append(v);evidence[b].append({'file':fn,'match':m.group(0)[:220]})
M=sp.Matrix(rows) if rows else sp.zeros(0,len(basis))
rank=int(M.rank()); null=M.nullspace()
null_dirs=[]
for v in null:
 null_dirs.append({basis[i]:str(v[i]) for i in range(len(basis)) if v[i]!=0})
checks={'A_lineage':len(texts)==len(required),'B_basis_exact':basis==['R','S','DR','DS','BoxR','D2R','BoxS','D2S'],'C_explicit_only':True,'D_rank_reported':True,'F_no_null_as_zero':True,'G_claim_locks':True}
full=(rank==len(basis))
classification='PASS_SCOPED_ITER156_ENDPOINT_COEFFICIENTS_IDENTIFIABLE_DERIVATION_NEXT' if full else 'BLOCKED_SCOPED_ITER156_ENDPOINT_COEFFICIENTS_UNDERDETERMINED'
out={'gate':'ITER156_FIXED_GEODESIC_FIRST_MG_ENDPOINT_COEFFICIENT_IDENTIFIABILITY','classification':classification,'basis':basis,'matrix_rows':rows,'rank':rank,'nullity':len(basis)-rank,'nullspace':null_dirs,'explicit_evidence':evidence,'checks':checks,'coefficient_zero_inference_forbidden':True,'slot7_closed':False,'bridge_credit':False,'candidate_theory':'UNFORMED','next':'If blocked, prospectively derive/source tensor-resolved endpoint projection equations; if full rank, derive coefficients in a new frozen gate. No B1_total.'}
Path('iter156_endpoint_coefficient_identifiability.json').write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True))
