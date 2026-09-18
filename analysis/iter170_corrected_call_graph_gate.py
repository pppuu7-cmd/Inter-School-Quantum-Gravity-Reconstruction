#!/usr/bin/env python3
from __future__ import annotations
import ast,json,sys
from pathlib import Path
lane=sys.argv[1] if len(sys.argv)>1 else 'producer'
root=Path(__file__).resolve().parents[1]
def text(p): return (root/p).read_text(encoding='utf-8')
def funcs(p):
 s=text(p); t=ast.parse(s); return {n.name:(ast.get_source_segment(s,n) or '') for n in ast.walk(t) if isinstance(n,ast.FunctionDef)}
p163='analysis/iter163_complete_covariant_reconstruction.py'; p161='analysis/iter161_endpoint_open_leg_factorization.py'; p140='analysis/iter140_first_mg_general_d_invariant_continuation.py'; p141='analysis/iter141_first_mg_wick_geometry_phase_strata.py'; p143='analysis/iter143_first_mg_denominator_contact_partition.py'
a,b,c,d,e=map(text,[p163,p161,p140,p141,p143]); f161=funcs(p161); f140=funcs(p140); up=f161.get('upper_open_vertex',''); low=f161.get('lower_open_vertices',''); main161=f161.get('main',''); solve163=funcs(p163).get('solve_D',''); g1=f140.get('G1_value','')
if lane=='producer':
 checks={
 'A_163_imports_161':'import iter161_endpoint_open_leg_factorization as i161' in a,
 'B_163_source_calls_upper':'i161.upper_open_vertex' in solve163,
 'C_upper_direct_dr1':'i140.dr1_real' in up,
 'D_upper_direct_g2':'i140.g2_real' in up,
 'E_upper_not_direct_r1':'i140.r1_tensor' not in up,
 'F_upper_reconstruction_supplies_r1':'upper_open_vertex' in main161 and 'r1_tensor' in main161 and 'upper_reconstructed' in main161,
 'G_lower_direct_r1':'i140.r1_tensor' in low,
 'H_lower_direct_g2':'i140.g2_real' in low,
 'I_lower_not_direct_dr1':'i140.dr1_real' not in low,
 'J_lower_reconstruction_supplies_dr1':'lower_open_vertices' in main161 and 'dr1_real' in main161 and 'lower_reconstructed' in main161,
 'K_G1_has_all_primitives':all(x in g1 for x in ['r1_tensor','dr1_real','g2_real']),
 'L_ITER163_source_upper_only':'upper_open_vertex' in solve163 and 'lower_open_vertices' not in solve163}
elif lane=='geometry':
 checks={
 'A_G_occurrences':all(x in d for x in ["('R1_minus_q', s.Integer(0), -1, 0)","('Gamma2_q', tau, 1, 0)","('Gamma2_k', tau, 0, 1)","('dR1_minus_k', s.Integer(1), 0, -1)"]),
 'B_two_wick_edges':"('R1_minus_q','Gamma2_q')" in d and "('Gamma2_k','dR1_minus_k')" in d,
 'C_affine_phase':"'expected_phase': tau*qN-(1-tau)*kN" in d,
 'D_endpoint_zeros_executable':'def endpoint_zeros' in d and 'coeff.subs(tau,0)' in d and 'coeff.subs(tau,1)' in d,
 'E_denominator_QK':'"denominator": "Q*K"' in e,
 'F_edge_geometry':'"q_edge": "tau*L", "k_edge": "(1-tau)*L"' in e,
 'G_singular_labels':'"singular": {"lower": "q", "upper": "k"}' in e}
else:
 checks={
 'A_asymmetry_real':('dr1_real' in up and 'r1_tensor' not in up and 'r1_tensor' in low and 'dr1_real' not in low),
 'B_upper_orientation':'Upper endpoint: k edge shrinks' in b and 'q-side metric leg' in b,
 'C_lower_orientation':'Lower endpoint: q edge shrinks' in b and 'k-side' in b,
 'D_contacts_retained':'cancelled-propagator contact distributions' in b and 'Q_CANCELLED' in e and 'K_CANCELLED' in e,
 'E_no_contact_zero':'contacts_set_zero' not in b and 'contact-zero' not in b,
 'F_no_ITER118_solve':'no ITER118 counterterm coefficient' in b or 'no ITER118 coefficient equation' in b,
 'G_ITER163_upper_only':'upper_open_vertex' in solve163 and 'lower_open_vertices' not in solve163}
ok=all(checks.values())
if ok: cls='PASS_SCOPED_SUBCHECK_ITER170_'+lane.upper()
elif any(v is False for v in checks.values()): cls='SCIENTIFIC_FAIL_ITER170_PROVENANCE_CONTRADICTED'
else: cls='BLOCKED_SCOPED_ITER170_SOURCE_INCOMPLETE'
out={'iteration':170,'lane':lane,'checks':checks,'classification':cls,'claim_ceiling':'corrected executable provenance only; no scaling/R-operation/Laurent/ITER118/B1/bridge/candidate theory'}
Path(f'iter170_{lane}.json').write_text(json.dumps(out,indent=2)+"\n",encoding='utf-8'); print(json.dumps(out,indent=2)); raise SystemExit(0 if ok else 2)
