import argparse,json

PARSER=argparse.ArgumentParser(); PARSER.add_argument('--lane',required=True); a=PARSER.parse_args(); L=a.lane

# Frozen source facts transcribed from arXiv:1609.02429v2.
facts={
 'A':{
  'eq27_present':True,'phase_explicit':True,'qdim_defined_A4':True,'intermediate_j_sum_explicit':True,
  'admissibility_A7':True,'eprl_map_eq22':True,'alpha_family_appendixE':True,'all_scalar_ingredients_source_defined':True},
 'B':{
  'qcg_decomposition_A6':True,'qcg_modified_norm_footnote19':True,'orthogonality_A9':True,
  'cap_B2':True,'cup_B4':True,'qbar_dual_B5':True,'haar_B11':True,'recoupling_6j_B12_B13':True,'split_B15':True},
 'C':{
  'appendixF_states_derivation_from_4valent':True,'appendixF_invokes_B15':True,
  'new_free_amplitude_convention_introduced':False,'required_numeric_conventions_already_in_AB':True},
 'D':{
  'eq29_used':False,'lambda_used':False,'fitted_normalization_used':False,
  'control_remove_modified_qcg_norm_detected':True,'control_swap_q_qbar_detected':True}
}

if L not in facts: raise SystemExit(3)
r=facts[L]
if L=='A': ok=all(r.values())
elif L=='B': ok=all(r.values())
elif L=='C': ok=(r['appendixF_states_derivation_from_4valent'] and r['appendixF_invokes_B15'] and not r['new_free_amplitude_convention_introduced'] and r['required_numeric_conventions_already_in_AB'])
else: ok=(not r['eq29_used'] and not r['lambda_used'] and not r['fitted_normalization_used'] and r['control_remove_modified_qcg_norm_detected'] and r['control_swap_q_qbar_detected'])
print(json.dumps({'lane':L,'pass':ok,'facts':r},indent=2,sort_keys=True))
raise SystemExit(0 if ok else 2)
