#!/usr/bin/env python3
"""ITER162 frozen structural diagnostic.

This script does NOT derive endpoint counterterms or ITER118 coefficients.
It mechanically enumerates the prospectively frozen upper-endpoint symmetric
covariant tensor span from the ITER162 preregistration and reports exact
combinatorial/rank-ready metadata. No fitted coefficients or ITER160 residue
are consumed.
"""
from fractions import Fraction
import json

# seed: name, momentum degree, tangent count
SEEDS = [
    ("delta_ab",0,0),("q_aq_b",2,0),("q_(a k_b)",2,0),("k_ak_b",2,0),
    ("q_(a n_b)",1,1),("k_(a n_b)",1,1),("n_an_b",0,2),
]
# scalar variables: name, momentum degree, tangent count
VARS = [("Q",2,0),("K",2,0),("S",2,0),("a",1,1),("b",1,1)]

def exponent_solutions(target_deg,target_tan):
    out=[]
    # degree <=4 makes bounds 0..4 sufficient
    for eQ in range(3):
      for eK in range(3):
       for eS in range(3):
        for ea in range(5):
         for eb in range(5):
          es=(eQ,eK,eS,ea,eb)
          deg=sum(e*v[1] for e,v in zip(es,VARS))
          tan=sum(e*v[2] for e,v in zip(es,VARS))
          if deg==target_deg and tan==target_tan: out.append(es)
    return out

def monomial(es):
    parts=[]
    for e,(name,_,_) in zip(es,VARS):
        if e: parts.append(name if e==1 else f"{name}^{e}")
    return "*".join(parts) if parts else "1"

cols=[]
for seed,d,t in SEEDS:
    for es in exponent_solutions(4-d,2-t):
        cols.append({"seed":seed,"scalar":monomial(es),"exponents":es})

# Frozen tensor-level contact prefilter: explicit scalar K divisibility only.
# Full numerator divisibility for reconstructed source tensors remains a later
# symbolic source-derived operation and is intentionally not guessed here.
for c in cols:
    c["explicit_K_factor"] = c["exponents"][1] > 0

assert len({(c['seed'],tuple(c['exponents'])) for c in cols})==len(cols)
assert all(c['exponents'][0]*2+c['exponents'][1]*2+c['exponents'][2]*2+c['exponents'][3]+c['exponents'][4] + next(d for s,d,t in SEEDS if s==c['seed']) == 4 for c in cols)
assert all(c['exponents'][3]+c['exponents'][4] + next(t for s,d,t in SEEDS if s==c['seed']) == 2 for c in cols)

out={
 "gate":"ITER162_OPEN_G_ENDPOINT_DISTRIBUTIONAL_R_OPERATION_AND_POLE_TENSOR",
 "classification":"STRUCTURAL_ENUMERATION_ONLY_NOT_SCIENTIFIC_PASS",
 "upper_candidate_column_count":len(cols),
 "explicit_K_factor_column_count":sum(c['explicit_K_factor'] for c in cols),
 "columns":cols,
 "locks":{"iter160_residue_consumed":False,"iter118_rank_solve":False,"contacts_set_zero":False,"inverse_28_scalar_map":False},
 "next_required_operation":"SOURCE_DERIVED_COVARIANT_RECONSTRUCTION_PLUS_EXACT_TENSOR_NUMERATOR_K_DIVISIBILITY_AND_DISTRIBUTIONAL_LAURENT_EXTENSION"
}
with open('iter162_structural_span.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps({k:v for k,v in out.items() if k!='columns'},indent=2,sort_keys=True))
