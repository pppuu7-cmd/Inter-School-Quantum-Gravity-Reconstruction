#!/usr/bin/env python3
"""RC-009 source-data fixed-point survival audit.

This is deliberately a source-level numerical audit, not a reproduction of
hyperfrustum path integrals. It quantifies how much the reported alpha fixed
point moves as progressively stronger truncations are relaxed and records the
published EPRL-vs-Regge free-point discriminator.
"""
import argparse,json,math,statistics
from pathlib import Path

# Source-reported approximate locations.
POINTS=[
  {'stage':'flat_hypercuboid_1d','alpha':0.63,'source':'prior hypercuboid coarse-graining'},
  {'stage':'curved_hyperfrustum_isochoric_1d','alpha':0.69,'source':'arXiv:1804.00023 Eq.44 / summary Eq.63'},
  {'stage':'curved_hyperfrustum_3parameter','alpha':0.677,'G':0.037,'Lambda':0.008,'source':'arXiv:1804.00023 Eq.64'},
]

def rel(a,b): return abs(a-b)/(0.5*(abs(a)+abs(b)))

def main():
  ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
  pair=[]
  for a,b in zip(POINTS[:-1],POINTS[1:]):
    pair.append({'from':a['stage'],'to':b['stage'],'abs_shift':abs(a['alpha']-b['alpha']),'symmetric_relative_shift':rel(a['alpha'],b['alpha'])})
  alphas=[p['alpha'] for p in POINTS]
  mean=statistics.fmean(alphas)
  cv=statistics.stdev(alphas)/mean
  curved_extension_shift=pair[-1]['symmetric_relative_shift']
  # Frozen descriptive gates chosen before workflow launch.
  curved_parameter_extension_stable=curved_extension_shift <= 0.05
  family_level_location_moderately_stable=max(alphas)-min(alphas) <= 0.08
  out={
    'test':'RC009_FIXED_POINT_SURVIVAL_SOURCE_AUDIT','status':'PASS_EXECUTION',
    'points':POINTS,'pairwise_alpha_shifts':pair,
    'alpha_mean':mean,'alpha_range':max(alphas)-min(alphas),'alpha_coefficient_of_variation':cv,
    'curved_1d_to_3parameter_relative_shift':curved_extension_shift,
    'curved_parameter_extension_stable_le_5pct':curved_parameter_extension_stable,
    'all_three_alpha_locations_within_range_0p08':family_level_location_moderately_stable,
    'published_free_point_control':{
      'riemannian_EPRL_free_G0_Lambda0_fixed_point':False,
      'Regge_exponential_with_measure_free_G0_Lambda0_fixed_point':True,
      'interpretation':'source-reported discriminator; no new calculation of the path integral'
    },
    'interpretation_lock':'Quantifies survival of an approximate alpha fixed-point location under increasingly rich symmetry-restricted truncations. It does not establish a continuum fixed point of full EPRL-FK and does not compare energy-scale critical exponents.',
  }
  Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
  print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
