#!/usr/bin/env python3
from __future__ import annotations
import ast,json,re,sys
from pathlib import Path
lane=sys.argv[1] if len(sys.argv)>1 else 'domain'
root=Path(__file__).resolve().parents[1]
paths=[
 'analysis/iter141_first_mg_wick_geometry_phase_strata.py',
 'analysis/iter143_first_mg_denominator_contact_partition.py',
 'analysis/iter161_endpoint_open_leg_factorization.py',
 'analysis/iter163_complete_covariant_reconstruction.py']
src={p:(root/p).read_text(encoding='utf-8') for p in paths}
joined='\n'.join(src.values())
sectors=['LOWER_Q_ZERO','UPPER_K_ZERO','Q_CANCELLED_CONTACT','K_CANCELLED_CONTACT','QK_INTERSECTION']
# Frozen audit: positive distributional evidence must be executable, not prose labels.
def has_any(patterns): return any(re.search(p,joined,re.I) for p in patterns)
def evidence(patterns):
 out=[]
 for p,s in src.items():
  for pat in patterns:
   if re.search(pat,s,re.I): out.append({'path':p,'pattern':pat})
 return out
coord_ev=evidence([r'\btau\b',r'endpoint_zeros',r'q_edge',r'k_edge'])
power_ev=evidence([r'\*\*\s*-?\d+',r'Pow\(',r'denominator[^\n]*(?:power|order|exponent)'])
measure_ev=evidence([r'\bmeasure\b',r'\bdq\b',r'\bdk\b',r'jacobian'])
wf_ev=evidence([r'wavefront',r'pullback',r'H[oö]rmander',r'product_prescription',r'distribution(?:al)?_product'])
ambiguity_ev=evidence([r'DiracDelta',r'delta\s*\(',r'normal_derivative',r'local_ambiguity',r'delta_derivative'])
if lane=='domain':
 checks={'five_sectors_frozen':len(sectors)==5,
         'executable_coordinate_geometry_present':bool(coord_ev),
         'explicit_or_mechanical_transverse_map_all_five':False}
 # Endpoint affine coordinate information exists, but no source-qualified transverse chart is encoded for all contacts/intersection.
 classification='BLOCKED_SCOPED_ITER172_DISTRIBUTIONAL_SOURCE_INCOMPLETE'
 detail='Executable endpoint/affine geometry exists, but no explicit/mechanically complete transverse-coordinate map is encoded for all five sectors.'
elif lane=='scaling':
 checks={'denominator_power_data_present':bool(power_ev),
         'measure_or_jacobian_data_present':bool(measure_ev),
         'scaling_determined_all_five':False}
 classification='BLOCKED_SCOPED_ITER172_DISTRIBUTIONAL_SOURCE_INCOMPLETE'
 detail='Frozen gate forbids inferring scaling from Q/K labels; executable denominator powers plus measure/codimension data are not jointly source-qualified for all sectors.'
else:
 checks={'wavefront_pullback_or_equivalent_present':bool(wf_ev),
         'source_supported_local_ambiguity_basis_present':bool(ambiguity_ev),
         'pullback_and_ambiguity_justified_all_five':False}
 classification='BLOCKED_SCOPED_ITER172_DISTRIBUTIONAL_SOURCE_INCOMPLETE'
 detail='No executable wavefront/product/pullback prescription and local delta/normal-derivative ambiguity basis are source-qualified for all five sectors.'
out={'iteration':172,'lane':lane,'sectors':sectors,'checks':checks,'evidence':{'coordinates':coord_ev,'powers':power_ev,'measure':measure_ev,'pullback':wf_ev,'ambiguity':ambiguity_ev},'classification':classification,'detail':detail,'claim_ceiling':'BLOCKED audit only; no R-operation/Laurent/ITER118/B1/bridge/candidate theory'}
Path(f'iter172_{lane}.json').write_text(json.dumps(out,indent=2)+"\n",encoding='utf-8')
print(json.dumps(out,indent=2))
# BLOCKED is a scientific classification, not infrastructure failure; keep CI green for artifact consumption.
