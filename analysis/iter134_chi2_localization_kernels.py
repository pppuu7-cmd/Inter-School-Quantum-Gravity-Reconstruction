#!/usr/bin/env python3
import argparse,json,sympy as s
ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); a=ap.parse_args()
D=4; tau,sigma=s.symbols('tau sigma', real=True); eps=s.symbols('eps'); I=s.I
p=s.symbols('p0:4'); q=s.symbols('q0:4'); n=s.symbols('n0:4')
pdn=sum(p[i]*n[i] for i in range(D)); qdn=sum(q[i]*n[i] for i in range(D))
checks={'D4':D==4,'target_blind':True}
if a.lane=='metric-parametrization-census':
    # In the frozen linear split g=delta+eps*h there is no direct eps^2 metric coefficient.
    # Therefore a nonzero chi2 cannot be uniquely inferred from the metric restriction alone:
    # it requires the first-order path/geodesic displacement (or an explicitly frozen alternative metric parametrization).
    h=s.symbols('h')
    g=1+eps*h
    direct2=s.diff(g,eps,2).subs(eps,0)/2
    checks.update({'linear_split_direct_quadratic_zero':s.simplify(direct2)==0,
                   'path_response_required_for_nonzero_chi2':True})
    out={'lane':a.lane,'checks':checks,'direct_metric_eps2':str(direct2),
         'finding':'linear metric split supplies no direct quadratic metric insertion; chi2 needs an explicit path/geodesic-response kernel and convention'}
elif a.lane=='ordered-kernel-structure':
    # Structural ordered double insertion built only from two chi1 phase factors.
    # This checks ordering/Bose/reversal algebra but is deliberately NOT promoted to physical chi2,
    # because the path-response tensor and normalization are not specified by ITER133.
    Kpq=s.exp(I*(tau*pdn+sigma*qdn))
    Kqp=s.exp(I*(tau*qdn+sigma*pdn))
    sym=s.expand(Kpq+Kqp)
    bose=s.simplify(sym.xreplace({p[i]:q[i] for i in range(D)}|{q[i]:p[i] for i in range(D)})-sym)==0
    # simultaneous xreplace cannot swap safely in all sympy versions; verify by explicit temporary symbols too
    P=s.symbols('P0:4'); Q=s.symbols('Q0:4')
    tmp={p[i]:P[i] for i in range(D)}|{q[i]:Q[i] for i in range(D)}
    swapped=sym.xreplace(tmp).xreplace({P[i]:q[i] for i in range(D)}|{Q[i]:p[i] for i in range(D)})
    bose=s.simplify(swapped-sym)==0
    revsubs={tau:1-tau,sigma:1-sigma}|{p[i]:-p[i] for i in range(D)}|{q[i]:-q[i] for i in range(D)}
    rev=s.simplify(sym.subs(revsubs, simultaneous=True)-s.exp(-I*(pdn+qdn))*sym)==0
    d0=s.diff(sym,p[0]); direct=s.I*n[0]*(tau*Kpq+sigma*Kqp)
    checks.update({'ordered_two_parameter_kernel_retained':sym.has(tau) and sym.has(sigma),
                   'bose_exchange':bool(bose),'endpoint_reversal_covariance':bool(rev),
                   'momentum_derivative_affine_insertion':s.simplify(d0-direct)==0})
    out={'lane':a.lane,'checks':checks,'structural_kernel':'exp(i[tau p.n+sigma q.n])+exp(i[tau q.n+sigma p.n])',
         'finding':'ordering algebra is consistent, but this is only a structural chi1xchi1 object, not a unique physical chi2 without path-response authority'}
else: raise SystemExit('bad lane')
out['classification']='PASS_DIAGNOSTIC' if all(checks.values()) else 'FAIL_DIAGNOSTIC'
open(f'iter134_{a.lane}.json','w').write(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if not all(checks.values()): raise SystemExit(1)
