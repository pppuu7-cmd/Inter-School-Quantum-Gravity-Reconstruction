#!/usr/bin/env python3
import json
from pathlib import Path

# Frozen ITER165 hypothesis-gate manifest. This program deliberately does not
# infer pole coefficients: it tests whether the source data are sufficient to
# define the prerequisites frozen in ITER165_PREREGISTRATION_2026-09-18.md.
REQ = [
 "ambient_variables_and_affine_endpoint_coordinate",
 "test_function_domain_space",
 "d_equals_4_minus_2epsilon",
 "transverse_scaling_degree_per_singular_sector",
 "ambient_to_affine_pullback_conditions",
 "free_symmetric_metric_leg",
 "lower_upper_orientation_separate",
 "K_divisible_contacts_retained",
 "full_local_delta_normal_derivative_ambiguity_span",
 "laurent_coefficient_manifest_before_ITER118",
]
# Source-of-truth status entering ITER165. Items not established by ITER163/164
# remain false rather than being supplied by a convenient extension.
established = {
 "ambient_variables_and_affine_endpoint_coordinate": True,
 "test_function_domain_space": False,
 "d_equals_4_minus_2epsilon": True,
 "transverse_scaling_degree_per_singular_sector": False,
 "ambient_to_affine_pullback_conditions": False,
 "free_symmetric_metric_leg": True,
 "lower_upper_orientation_separate": True,
 "K_divisible_contacts_retained": True,
 "full_local_delta_normal_derivative_ambiguity_span": False,
 "laurent_coefficient_manifest_before_ITER118": False,
}
missing=[k for k in REQ if not established[k]]
A={"lane":"A_constructive_hypothesis","requirements":established,"missing":missing,
   "classification":"BLOCKED_SCOPED_ITER165_NONUNIQUE_OR_INCOMPLETE_HYPOTHESES" if missing else "PASS_SCOPED_ITER165_MEROMORPHIC_FAMILY_HYPOTHESES_COMPLETE"}
# Independent falsifier: a missing domain/pullback/scaling datum is itself a
# preregistered blocking witness; do not invent it from general extension theory.
B={"lane":"B_completeness_falsifier","blocking_witnesses":[x for x in missing if x in {
 "test_function_domain_space","transverse_scaling_degree_per_singular_sector","ambient_to_affine_pullback_conditions","full_local_delta_normal_derivative_ambiguity_span"}],
 "verdict":"BLOCKED"}
C={"lane":"C_contact_orientation_critic","contacts_retained":established["K_divisible_contacts_retained"],
   "orientations_separate":established["lower_upper_orientation_separate"],"verdict":"PASS_SCOPED_SUBCHECK"}
out={"iteration":"ITER165","frozen_required_count":len(REQ),"lane_A":A,"lane_B":B,"lane_C":C,
 "scientific_classification":A["classification"],"bridge_credit":False,"candidate_theory":"UNFORMED"}
Path("artifacts").mkdir(exist_ok=True)
Path("artifacts/iter165_hypothesis_gate.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
