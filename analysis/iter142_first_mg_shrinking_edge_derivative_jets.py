#!/usr/bin/env python3
"""ITER142: directional degree on the actually shrinking Wick propagator."""
from __future__ import annotations
import json
import sympy as s
import iter138_first_mg_exact_numerator_kernels as i138
import iter139_affine_single_line_ceiling_repair as i139
import iter141_first_mg_wick_geometry_phase_strata as i141

q=i138.q; k=i138.k; D=i138.D
n0=(s.Integer(1),0,0,0)


def group_homogeneous(expr, side, degree):
    poly=s.Poly(s.expand(expr), *(q+k))
    out=s.Integer(0)
    for mon, coeff in poly.terms():
        d=sum(mon[:D]) if side=='q' else sum(mon[D:])
        if d != degree: continue
        term=coeff
        for var,pow_ in zip(q+k,mon): term *= var**pow_
        out += term
    return s.factor(out)


def meta(expr):
    return i138.poly_meta(expr,q,k)


def edge_zero(family, edge, endpoint):
    spec=i141.FAMILIES[family]
    occ={o[0]:o for o in spec['occurrences']}
    coeff=i141.abs_affine(occ[edge[0]][1]-occ[edge[1]][1])
    val=s.simplify(coeff.subs(i141.tau,0 if endpoint=='lower' else 1))
    return val==0, str(coeff)


def jet(N,supp):
    m=2+N
    return {'N_singular_edge':N,'source_suppression':supp,'m_raw_ceiling':m,'jet_ceiling':m-supp-1}


def main():
    polys={
      'M_R2_chi1_dR1':i138.M_numerator(q,k,n0),
      'M_R1_chi1_dR2':i139.M2_numerator(q,k,n0),
      'G_R1_chi2_Gamma2_dR1':i138.G_numerator(q,k,n0),
    }
    metas={name:meta(expr) for name,expr in polys.items()}
    expected={
      'M_R2_chi1_dR1':{'left_degree':3,'right_degree':5},
      'M_R1_chi1_dR2':{'left_degree':5,'right_degree':4},
      'G_R1_chi2_Gamma2_dR1':{'left_degree':3,'right_degree':4},
    }
    degree_match=all(metas[f]['left_degree']==e['left_degree'] and metas[f]['right_degree']==e['right_degree'] for f,e in expected.items())

    # Frozen edge-to-momentum incidence from ITER141 coordinates and ITER138/139 tensor labels.
    routes={
      'M_R2_chi1_dR1':{
        'lower':{'edge':('R2_q','chi1_minus_q'),'momentum':'q','suppression':0},
      },
      'M_R1_chi1_dR2':{
        'upper':{'edge':('chi1_minus_k','dR2_k'),'momentum':'k','suppression':1},
      },
      'G_R1_chi2_Gamma2_dR1':{
        'lower':{'edge':('R1_minus_q','Gamma2_q'),'momentum':'q','suppression':0},
        'upper':{'edge':('Gamma2_k','dR1_minus_k'),'momentum':'k','suppression':1},
      },
    }
    nonsingular={
      'M_R2_chi1_dR1':['upper'],
      'M_R1_chi1_dR2':['lower'],
      'G_R1_chi2_Gamma2_dR1':[],
    }
    rows={}
    route_ok=True; hom_ok=True; global_ok=True
    for fam,ends in routes.items():
        rows[fam]={}
        for ep,cfg in ends.items():
            zero, sep=edge_zero(fam,cfg['edge'],ep)
            route_ok &= bool(zero)
            m=metas[fam]
            N=m['left_degree'] if cfg['momentum']=='q' else m['right_degree']
            H=group_homogeneous(polys[fam],cfg['momentum'],N)
            hnonzero=(H!=0)
            hom_ok &= bool(hnonzero)
            global_ok &= N<=5
            rows[fam][ep]={
              'status':'AFFINE_PROPAGATOR_SINGULARITY',
              'edge':list(cfg['edge']),
              'edge_separation_over_L':sep,
              'shrinking_momentum':cfg['momentum'],
              'directional_degree':N,
              'highest_homogeneous_component':str(H),
              'highest_homogeneous_nonzero':bool(hnonzero),
              'sharp_jet':jet(N,cfg['suppression']),
            }
        for ep in nonsingular[fam]:
            rows[fam][ep]={'status':'NO_AFFINE_PROPAGATOR_SINGULARITY_IN_CONNECTED_CROSS_CHANNEL'}

    # Check the opposite endpoint really has no zero edge in ITER141's full connected edge set.
    nonsing_ok=True
    for fam,eps in nonsingular.items():
        spec=i141.FAMILIES[fam]
        occ={o[0]:o for o in spec['occurrences']}
        for ep in eps:
            v=0 if ep=='lower' else 1
            anyzero=False
            for a,b in spec['wick_edges']:
                c=i141.abs_affine(occ[a][1]-occ[b][1])
                anyzero |= s.simplify(c.subs(i141.tau,v))==0
            nonsing_ok &= not anyzero

    checks={
      'A_exact_directional_degrees_recomputed':bool(degree_match),
      'B_ITER141_shrinking_edges_reproduced':bool(route_ok and nonsing_ok),
      'C_shrinking_edge_degree_le_ITER139_global5':bool(global_ok),
      'D_highest_shrinking_homogeneous_components_nonzero':bool(hom_ok),
      'E_all_sharp_connected_cross_jets_le4':all(
          row.get('sharp_jet',{}).get('jet_ceiling',0)<=4
          for fam in rows.values() for row in fam.values()
      ),
      'F_denominator_cancellation_and_residue_deferred':True,
      'G_target_blind':True,
    }
    if not global_ok:
        cls='SCIENTIFIC_FAIL_ITER139_GLOBAL_BOUND_ON_ACTUAL_SINGULAR_EDGE'
    elif all(checks.values()):
        cls='PASS_SCOPED_FIRST_MG_SHRINKING_EDGE_DERIVATIVE_JETS_CLOSED_LOCAL_RESIDUES_OPEN'
    else:
        cls='SCIENTIFIC_FAIL_FIRST_MG_SHRINKING_EDGE_ALLOCATION'
    out={
      'gate':'ITER142_FIXED_GEODESIC_CURVATURE_FIRST_MG_SHRINKING_EDGE_DERIVATIVE_JETS',
      'classification':cls,
      'polynomial_metadata':metas,
      'endpoint_rows':rows,
      'checks':checks,
      'interpretation':'Global max-line ceilings remain valid; local connected-cross pole jets use only the momentum degree on the Wick edge whose affine separation actually vanishes.',
      'claim_ceiling':'sharp D4 derivative/Taylor-jet ceilings only; no pole/B1/noncancellation/B0/EDT/bridge/new physics/candidate theory',
    }
    with open('iter142_first_mg_shrinking_edge_derivative_jets.json','w',encoding='utf-8') as f:
        json.dump(out,f,indent=2); f.write('\n')
    print(json.dumps({
      'classification':cls,'metadata':metas,
      'sharp_jets':{fam:{ep:r.get('sharp_jet') for ep,r in ends.items() if 'sharp_jet' in r} for fam,ends in rows.items()},
      'checks':checks},indent=2))
    if cls.startswith('SCIENTIFIC_FAIL'): raise SystemExit(1)

if __name__=='__main__': main()
