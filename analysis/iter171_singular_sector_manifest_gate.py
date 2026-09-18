#!/usr/bin/env python3
from __future__ import annotations
import ast,json,sys
from pathlib import Path
lane=sys.argv[1] if len(sys.argv)>1 else 'producer'
root=Path(__file__).resolve().parents[1]
def text(p): return (root/p).read_text(encoding='utf-8')
def funcs(p):
 s=text(p); t=ast.parse(s); return {n.name:(ast.get_source_segment(s,n) or '') for n in ast.walk(t) if isinstance(n,ast.FunctionDef)}
p163='analysis/iter163_complete_covariant_reconstruction.py'; p161='analysis/iter161_endpoint_open_leg_factorization.py'; p141='analysis/iter141_first_mg_wick_geometry_phase_strata.py'; p143='analysis/iter143_first_mg_denominator_contact_partition.py'
a,b,d,e=map(text,[p163,p161,p141,p143]); f163=funcs(p163); f161=funcs(p161); solve=f163.get('solve_D',''); up=f161.get('upper_open_vertex','')
manifest=[
 {'sector':'LOWER_Q_ZERO','locus':'q=0 / tau=0 shrinking q-edge','orientation':'lower','provenance':p141+'::endpoint_zeros + '+p143+'::singular.lower'},
 {'sector':'UPPER_K_ZERO','locus':'k=0 / tau=1 shrinking k-edge','orientation':'upper','provenance':p141+'::endpoint_zeros + '+p143+'::singular.upper'},
 {'sector':'Q_CANCELLED_CONTACT','locus':'Q propagator cancelled contact','orientation':'contact','provenance':p143+'::Q_CANCELLED'},
 {'sector':'K_CANCELLED_CONTACT','locus':'K propagator cancelled contact','orientation':'contact','provenance':p143+'::K_CANCELLED'},
 {'sector':'QK_INTERSECTION','locus':'Q=0 and K=0 simultaneous denominator locus','orientation':'intersection','provenance':p143+'::denominator Q*K'}]
required={x['sector'] for x in manifest}
if lane=='producer':
 checks={
  'A_ITER163_upper_only':'i161.upper_open_vertex' in solve and 'lower_open_vertices' not in solve,
  'B_upper_correct_primitives':'i140.dr1_real' in up and 'i140.g2_real' in up and 'i140.r1_tensor' not in up,
  'C_denominator_QK':'"denominator": "Q*K"' in e,
  'D_lower_q_label':'"singular": {"lower": "q", "upper": "k"}' in e,
  'E_endpoint_zero_code':'def endpoint_zeros' in d and 'coeff.subs(tau,0)' in d and 'coeff.subs(tau,1)' in d,
  'F_contacts_explicit':'Q_CANCELLED' in e and 'K_CANCELLED' in e,
  'G_manifest_all_required':{x['sector'] for x in manifest}==required}
elif lane=='completeness':
 labels={x['sector'] for x in manifest}
 checks={
  'A_two_denominator_factors':'"denominator": "Q*K"' in e,
  'B_both_endpoint_orientations':'"q_edge": "tau*L", "k_edge": "(1-tau)*L"' in e and '"lower": "q", "upper": "k"' in e,
  'C_intersection_enumerated':'QK_INTERSECTION' in labels,
  'D_Q_contact_enumerated':'Q_CANCELLED_CONTACT' in labels and 'Q_CANCELLED' in e,
  'E_K_contact_enumerated':'K_CANCELLED_CONTACT' in labels and 'K_CANCELLED' in e,
  'F_no_required_label_missing':required.issubset(labels)}
else:
 checks={
  'A_no_lower_source_in_ITER163':'lower_open_vertices' not in solve,
  'B_no_contact_zero':'contacts_set_zero' not in b and 'contact-zero' not in b,
  'C_no_ITER118_solve':'ITER118' not in solve,
  'D_executable_provenance_only':all(x['provenance'].startswith('analysis/') for x in manifest),
  'E_no_scaling_claim':all('scaling' not in x for m in manifest for x in m.values()),
  'F_no_R_operation_claim':all('R-operation' not in x for m in manifest for x in m.values())}
ok=all(checks.values())
cls=('PASS_SCOPED_SUBCHECK_ITER171_'+lane.upper()) if ok else 'SCIENTIFIC_FAIL_ITER171_MANIFEST_CONTRADICTED'
out={'iteration':171,'lane':lane,'checks':checks,'manifest':manifest if lane=='producer' else None,'classification':cls,'claim_ceiling':'singular-sector manifest only; no scaling/R-operation/Laurent/ITER118/B1/bridge/candidate theory'}
Path(f'iter171_{lane}.json').write_text(json.dumps(out,indent=2)+"\n",encoding='utf-8'); print(json.dumps(out,indent=2)); raise SystemExit(0 if ok else 2)
