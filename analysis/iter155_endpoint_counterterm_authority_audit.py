#!/usr/bin/env python3
import json, pathlib, re, subprocess
ROOT=pathlib.Path('.')

def grep(pattern):
    p=subprocess.run(['git','grep','-n','-i','-E',pattern,'--',':(exclude)analysis/iter155_endpoint_counterterm_authority_audit.py'],text=True,capture_output=True)
    return [x for x in p.stdout.splitlines() if x.strip()]
state=json.loads((ROOT/'recovery/state.json').read_text())
front=(ROOT/'recovery/CURRENT_FRONT.md').read_text()
queries={
 'iter118_endpoint_basis': r'ITER118.*(endpoint|geodesic)|(endpoint|geodesic).*ITER118',
 'three_strata': r'first[- ]M/G|three.*(endpoint|strata)|endpoint strata',
 'general_d_pole': r'general[- ]d|general d|1/epsilon|1/eps|pole convention',
 'tensor_projection': r'tensor projection|tensor-resolved|project.*tensor|local residue.*basis|residue.*endpoint',
 'divergent_finite': r'divergent.*finite|finite.*divergent|counterterm coefficient|renormalization',
}
hits={k:grep(v) for k,v in queries.items()}
# Exclude ITER155 prereg/current-front statements from evidence for a pre-existing tensor map.
def prior(lines):
    return [x for x in lines if 'ITER155_PREREGISTRATION' not in x and 'recovery/CURRENT_FRONT.md' not in x and 'recovery/state.json' not in x]
checks={
 'A_lineage': state.get('active_iteration')=='POST_ITER154B_ENDPOINT_COUNTERTERM_FRONT' and 'ITER155_FIXED_GEODESIC' in state.get('next_gate',''),
 'B_iter118_basis_authority_located': bool(prior(hits['iter118_endpoint_basis'])),
 'C_three_endpoint_strata_located': bool(prior(hits['three_strata'])),
 'D_general_d_and_divergent_finite_authority_located': bool(prior(hits['general_d_pole'])) and bool(prior(hits['divergent_finite'])),
 'E_preexisting_tensor_projection_authority_located': bool(prior(hits['tensor_projection'])),
 'F_claim_locks': not any(state.get('claim_locks',{}).values()),
}
if all(checks.values()):
    classification='PASS_SCOPED_ITER155_ENDPOINT_COUNTERTERM_AUTHORITY_IDENTIFIED_COEFFICIENT_DERIVATION_ALLOWED'
else:
    missing=[k for k,v in checks.items() if not v]
    classification='BLOCKED_ITER155_ENDPOINT_COUNTERTERM_AUTHORITY_INCOMPLETE_'+'_'.join(missing)
out={'gate':'ITER155_FIXED_GEODESIC_FIRST_MG_ENDPOINT_COUNTERTERM_COEFFICIENT_AUTHORITY','checks':checks,'classification':classification,'missing_predicates':[k for k,v in checks.items() if not v], 'evidence_counts':{k:len(prior(v)) for k,v in hits.items()},'evidence':{k:prior(v)[:40] for k,v in hits.items()},'bridge_credit':False,'candidate_theory':'UNFORMED'}
pathlib.Path('iter155_endpoint_counterterm_authority_audit.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))