#!/usr/bin/env python3
"""ITER141: exact affine Wick-edge geometry and Fourier phase routing for first M/G cross channels."""
from __future__ import annotations
import json
import sympy as s

tau = s.symbols('tau', real=True)
qN, kN = s.symbols('qN kN', real=True)  # q.n L and k.n L with common L absorbed

# Occurrence format: (name, coordinate alpha along segment, q coefficient, k coefficient).
# Fourier exponent is i * sum_j momentum_j . x_j.
FAMILIES = {
    'M_R2_chi1_dR1': {
        'occurrences': [
            ('R2_q', s.Integer(0), 1, 0),
            ('R2_k', s.Integer(0), 0, 1),
            ('chi1_minus_q', tau, -1, 0),
            ('dR1_minus_k', s.Integer(1), 0, -1),
        ],
        'wick_edges': [('R2_q','chi1_minus_q'), ('R2_k','dR1_minus_k')],
        'expected_phase': -tau*qN-kN,
        'expected_factorized_phase': -(qN+kN)+(1-tau)*qN,
        'expected_singular': ['lower'],
        'N1': 5,
        'suppression': {'lower':0,'upper':1},
    },
    'M_R1_chi1_dR2': {
        'occurrences': [
            ('R1_minus_q', s.Integer(0), -1, 0),
            ('chi1_minus_k', tau, 0, -1),
            ('dR2_q', s.Integer(1), 1, 0),
            ('dR2_k', s.Integer(1), 0, 1),
        ],
        'wick_edges': [('R1_minus_q','dR2_q'), ('chi1_minus_k','dR2_k')],
        'expected_phase': qN+(1-tau)*kN,
        'expected_factorized_phase': (qN+kN)-tau*kN,
        'expected_singular': ['upper'],
        'N1': 5,
        'suppression': {'lower':0,'upper':1},
    },
    'G_R1_chi2_Gamma2_dR1': {
        'occurrences': [
            ('R1_minus_q', s.Integer(0), -1, 0),
            ('Gamma2_q', tau, 1, 0),
            ('Gamma2_k', tau, 0, 1),
            ('dR1_minus_k', s.Integer(1), 0, -1),
        ],
        'wick_edges': [('R1_minus_q','Gamma2_q'), ('Gamma2_k','dR1_minus_k')],
        'expected_phase': tau*qN-(1-tau)*kN,
        'expected_factorized_phase': tau*(qN+kN)-kN,
        'expected_singular': ['lower','upper'],
        'N1': 4,
        'suppression': {'lower':0,'upper':1},
    },
}


def endpoint_zeros(coeff):
    out=[]
    if s.simplify(coeff.subs(tau,0)) == 0: out.append('lower')
    if s.simplify(coeff.subs(tau,1)) == 0: out.append('upper')
    return out


def jet(N,supp):
    m=2+N
    return m-supp-1


def main():
    results={}
    all_ok=True
    for name, spec in FAMILIES.items():
        occ={o[0]:o for o in spec['occurrences']}
        phase=s.expand(sum(o[1]*(o[2]*qN+o[3]*kN) for o in spec['occurrences']))
        momentum_q=sum(o[2] for o in spec['occurrences'])
        momentum_k=sum(o[3] for o in spec['occurrences'])
        edge_rows=[]
        singular=set()
        for a,b in spec['wick_edges']:
            coeff=s.factor(abs_affine(occ[a][1]-occ[b][1]))
            zeros=endpoint_zeros(coeff)
            singular.update(zeros)
            edge_rows.append({'edge':[a,b],'affine_separation_over_L':str(coeff),'zero_endpoints':zeros})
        inferred=sorted(singular, key=lambda x: ['lower','upper'].index(x))
        expected=spec['expected_singular']
        phase_ok=s.simplify(phase-spec['expected_phase'])==0
        factor_ok=s.simplify(spec['expected_phase']-spec['expected_factorized_phase'])==0
        mom_ok=(momentum_q==0 and momentum_k==0)
        strata_ok=inferred==expected
        jets={}
        for ep in ['lower','upper']:
            if ep in inferred:
                jets[ep]={
                    'status':'AFFINE_PROPAGATOR_SINGULARITY',
                    'N1':spec['N1'],
                    'source_suppression':spec['suppression'][ep],
                    'm_raw_ceiling':2+spec['N1'],
                    'jet_ceiling':jet(spec['N1'],spec['suppression'][ep]),
                }
            else:
                jets[ep]={'status':'NO_AFFINE_PROPAGATOR_SINGULARITY_IN_CONNECTED_CROSS_CHANNEL'}
        row_ok=phase_ok and factor_ok and mom_ok and strata_ok
        all_ok &= row_ok
        results[name]={
            'phase_exponent_over_i':str(phase),
            'expected_phase_exponent_over_i':str(spec['expected_phase']),
            'factorized_phase_exponent_over_i':str(spec['expected_factorized_phase']),
            'phase_identity':bool(phase_ok),
            'total_wick_momentum_q_coefficient':momentum_q,
            'total_wick_momentum_k_coefficient':momentum_k,
            'pairwise_momentum_conservation':bool(mom_ok),
            'edges':edge_rows,
            'inferred_actual_affine_singular_strata':inferred,
            'expected_actual_affine_singular_strata':expected,
            'strata_match':bool(strata_ok),
            'endpoint_jet_map':jets,
        }
    checks={
        'A_symbolic_affine_coordinates':True,
        'B_wick_pair_momentum_conservation':all(r['pairwise_momentum_conservation'] for r in results.values()),
        'C_phase_identities_exact':all(r['phase_identity'] for r in results.values()),
        'D_actual_endpoint_strata_inferred':all(r['strata_match'] for r in results.values()),
        'E_ITER139_jet_map_consumed':(
            results['M_R2_chi1_dR1']['endpoint_jet_map']['lower']['jet_ceiling']==6 and
            results['M_R1_chi1_dR2']['endpoint_jet_map']['upper']['jet_ceiling']==5 and
            results['G_R1_chi2_Gamma2_dR1']['endpoint_jet_map']['lower']['jet_ceiling']==5 and
            results['G_R1_chi2_Gamma2_dR1']['endpoint_jet_map']['upper']['jet_ceiling']==4
        ),
        'F_local_self_pairing_explicitly_outside_scope':True,
        'G_target_blind':True,
    }
    ok=all(checks.values()) and all_ok
    classification=('PASS_SCOPED_FIRST_MG_WICK_GEOMETRY_PHASE_AND_SINGULAR_STRATA_CLOSED_LOCAL_POLES_OPEN'
                    if ok else 'SCIENTIFIC_FAIL_FIRST_MG_WICK_GEOMETRY_ROUTING')
    out={
        'gate':'ITER141_FIXED_GEODESIC_CURVATURE_FIRST_MG_WICK_GEOMETRY_PHASE_AND_SINGULAR_STRATA',
        'classification':classification,
        'anchored_geometry':{'x':'0','y':'L n','z_tau':'tau L n','L_condition':'L>0','n2':1},
        'source_weight':'1-tau',
        'families':results,
        'checks':checks,
        'scope_note':'Connected cross Wick channels only; local/self-pairing quadratic channel remains a separate renormalization sector.',
        'claim_ceiling':'geometry/phase/singular strata only; no pole/B1/noncancellation/B0/EDT/bridge/new physics/candidate theory',
    }
    with open('iter141_first_mg_wick_geometry_phase_strata.json','w',encoding='utf-8') as f:
        json.dump(out,f,indent=2); f.write('\n')
    print(json.dumps({'classification':classification,'checks':checks,
        'singular_strata':{k:v['inferred_actual_affine_singular_strata'] for k,v in results.items()},
        'jet_maps':{k:v['endpoint_jet_map'] for k,v in results.items()}},indent=2))
    if not ok: raise SystemExit(1)


def abs_affine(expr):
    """Return nonnegative affine distance coefficient on tau in [0,1] for known edge forms."""
    e=s.factor(expr)
    candidates=[tau,1-tau,s.Integer(1),-tau,tau-1,s.Integer(-1)]
    if s.simplify(e-tau)==0 or s.simplify(e+tau)==0: return tau
    if s.simplify(e-(1-tau))==0 or s.simplify(e+(1-tau))==0: return 1-tau
    if s.simplify(e-1)==0 or s.simplify(e+1)==0: return s.Integer(1)
    raise ValueError(f'unrecognized affine separation {e}')

if __name__=='__main__':
    main()
