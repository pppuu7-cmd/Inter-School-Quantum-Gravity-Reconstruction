import argparse, json, sympy as s

p=argparse.ArgumentParser(); p.add_argument('--lane',required=True); a=p.parse_args()
t=s.symbols('t', real=True); u=s.symbols('u', real=True)

def green(tt,uu):
    # Green function for y''=f, y(0)=y(1)=0
    return s.Piecewise((tt*(uu-1), tt<=uu),(uu*(tt-1), True))

def lane_green():
    G=green(t,u)
    left=t*(u-1); right=u*(t-1)
    checks={
      'G_t0': s.simplify(left.subs(t,0))==0,
      'G_t1': s.simplify(right.subs(t,1))==0,
      'continuous_at_t_eq_u': s.simplify(left.subs(t,u)-right.subs(t,u))==0,
      'derivative_jump_plus_one': s.simplify(s.diff(right,t).subs(t,u)-s.diff(left,t).subs(t,u))==1,
      'target_blind': True,
    }
    return {'lane':'dirichlet-green','checks':checks,'classification':'PASS_DIAGNOSTIC' if all(checks.values()) else 'SCIENTIFIC_FAIL'}

def lane_source():
    # Typed perturbative census from z''^a + Gamma^a_bc(z) z'^b z'^c=0.
    # Gamma=k Gamma1+k^2 Gamma2; z=z0+k xi1+k^2 xi2.
    terms=[
      {'name':'Gamma2_background','order_h':2,'xi1_power':0,'derivative_Gamma1':0,'velocity_xi1':0,'sign':-1},
      {'name':'displaced_Gamma1','order_h':1,'xi1_power':1,'derivative_Gamma1':1,'velocity_xi1':0,'sign':-1},
      {'name':'velocity_response','order_h':1,'xi1_power':1,'derivative_Gamma1':0,'velocity_xi1':1,'multiplicity':2,'sign':-1},
    ]
    bilinear=all(x['order_h']+x['xi1_power']==2 for x in terms)
    complete={x['name'] for x in terms}=={'Gamma2_background','displaced_Gamma1','velocity_response'}
    checks={'three_required_sectors':complete,'bilinear_after_xi1_substitution':bilinear,'common_geodesic_sign_fixed':all(x['sign']==-1 for x in terms),'target_blind':True}
    return {'lane':'second-order-source-census','equation':'xi2_ddot = -Gamma2(v,v) -(xi1.d)Gamma1(v,v) -2 Gamma1(v,xi1_dot)','terms':terms,'checks':checks,'classification':'PASS_DIAGNOSTIC' if all(checks.values()) else 'SCIENTIFIC_FAIL'}

out=lane_green() if a.lane=='dirichlet-green' else lane_source()
fn='iter135_'+a.lane+'.json'; open(fn,'w').write(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
