#!/usr/bin/env python3
from __future__ import annotations
import ast,json,sys
from pathlib import Path

lane=sys.argv[1] if len(sys.argv)>1 else 'trace'
root=Path(__file__).resolve().parents[1]
def text(p): return (root/p).read_text(encoding='utf-8')
def funcs(p):
 t=ast.parse(text(p)); return {n.name:ast.get_source_segment(text(p),n) or '' for n in ast.walk(t) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}

p163='analysis/iter163_complete_covariant_reconstruction.py'; p161='analysis/iter161_endpoint_open_leg_factorization.py'; p140='analysis/iter140_first_mg_general_d_invariant_continuation.py'; p141='analysis/iter141_first_mg_wick_geometry_phase_strata.py'; p143='analysis/iter143_first_mg_denominator_contact_partition.py'
a,b,c,d,e=map(text,[p163,p161,p140,p141,p143]); f161=funcs(p161); f140=funcs(p140)
checks={}
if lane=='trace':
 checks={
  'A_163_imports_161':'import iter161_endpoint_open_leg_factorization as i161' in a,
  'B_163_calls_upper':'i161.upper_open_vertex' in a,
  'C_161_imports_140':'import iter140_first_mg_general_d_invariant_continuation as i140' in b,
  'D_upper_calls_g2':'i140.g2_real' in f161.get('upper_open_vertex',''),
  'E_upper_calls_dr1':'i140.dr1_real' in f161.get('upper_open_vertex',''),
  'F_upper_calls_r1':'i140.r1_tensor' in f161.get('upper_open_vertex',''),
  'G_140_G_family':'"G_R1_chi2_Gamma2_dR1": G1_value' in c,
  'H_G1_calls_g2':'g2_real' in f140.get('G1_value','') and 'dr1_real' in f140.get('G1_value','') and 'r1_tensor' in f140.get('G1_value','')}
elif lane=='geometry':
 checks={
  'A_G_occurrences':"'G_R1_chi2_Gamma2_dR1'" in d and "('R1_minus_q', s.Integer(0), -1, 0)" in d and "('Gamma2_q', tau, 1, 0)" in d and "('Gamma2_k', tau, 0, 1)" in d and "('dR1_minus_k', s.Integer(1), 0, -1)" in d,
  'B_wick_edges':"('R1_minus_q','Gamma2_q')" in d and "('Gamma2_k','dR1_minus_k')" in d,
  'C_phase':"'expected_phase': tau*qN-(1-tau)*kN" in d,
  'D_endpoint_zero_mechanical':'def endpoint_zeros' in d and "coeff.subs(tau,0)" in d and "coeff.subs(tau,1)" in d,
  'E_denominator_QK':'"denominator": "Q*K"' in e,
  'F_G_edges': '"q_edge": "tau*L", "k_edge": "(1-tau)*L"' in e,
  'G_G_singular':'"singular": {"lower": "q", "upper": "k"}' in e}
else:
 checks={
  'A_161_upper_orientation':'Upper endpoint: k edge shrinks' in b and 'retain the q-side metric leg' in b,
  'B_161_lower_orientation':'Lower endpoint: q edge shrinks' in b and 'retain the k-side' in b,
  'C_141_G_both_endpoints':"'expected_singular': ['lower','upper']" in d,
  'D_143_G_both_edges':'"q_edge": "tau*L", "k_edge": "(1-tau)*L"' in e,
  'E_contacts_retained_161':'cancelled-propagator contact distributions' in b,
  'F_contact_classes_exist':'Q_CANCELLED' in e and 'K_CANCELLED' in e and 'ENDPOINT_LOCAL_CONTACT_WITH_OTHER_PROPAGATOR_NONLOCAL' in e,
  'G_no_iter118':'no ITER118 coefficient equation' in b or 'no ITER118 counterterm coefficient' in b}
ok=all(checks.values())
cls=('PASS_SCOPED_SUBCHECK_ITER169_'+lane.upper()) if ok else ('SCIENTIFIC_FAIL_ITER169_SOURCE_CHAIN_CONTRADICTED' if any(v is False for v in checks.values()) else 'BLOCKED_SCOPED_ITER169_TRACE_INCOMPLETE')
out={'iteration':169,'lane':lane,'checks':checks,'classification':cls,'claim_ceiling':'source trace only; no Laurent/R-operation/ITER118/B1/bridge/candidate theory'}
Path(f'iter169_{lane}.json').write_text(json.dumps(out,indent=2)+"\n",encoding='utf-8'); print(json.dumps(out,indent=2)); raise SystemExit(0 if ok else 2)
