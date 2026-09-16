#!/usr/bin/env python3
"""ITER150: first M/G separated two-propagator master-pole continuation.

Scope: consume the frozen ITER140 v6 general-d numerator and evaluate only the
connected cross TWO_PROPAGATOR sector after the ITER143 denominator/contact
partition.  Q/K-cancelled contact sectors, counterterms, full B1 and bridge
claims remain outside this gate.
"""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
import sympy as s

EXPECTED_UPSTREAM = "PASS_SCOPED_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION_CLOSED_POLE_INTEGRATION_OPEN"
FAMILIES = ["M_R2_chi1_dR1","M_R1_chi1_dR2","G_R1_chi2_Gamma2_dR1"]

d, eps, L = s.symbols("d eps L", positive=True)
tau = s.symbols("tau", real=True)

# Frozen from ITER141: phase edge coordinates in units of L and source weight 1-tau.
ROUTES = {
    "M_R2_chi1_dR1": {"rx":"tau", "ry":"1", "sx":-1, "sy":-1},
    "M_R1_chi1_dR2": {"rx":"1", "ry":"1-tau", "sx":1, "sy":1},
    "G_R1_chi2_Gamma2_dR1": {"rx":"tau", "ry":"1-tau", "sx":1, "sy":-1},
}

# Fourier convention fixed by the ITER138/140 momentum-space denominators:
# int d^d p/(2pi)^d exp(i p.x)/p^2 = C_d |x|^(2-d).
C = s.gamma(d/s.Integer(2)-1)/(4*s.pi**(d/s.Integer(2)))
m = 2-d

# Independent radial-derivative construction of the four possible Q^0 K^0 basis masters.
f1 = m
f2 = m*(m-1)
f3 = m*(m-1)*(m-2)
f4 = m*(m-1)*(m-2)*(m-3)
ht = m
kt = m*(m-2)
lt = m*(m-2)*(m-3)
closed_struct = {
    "S^3": s.factor(m**2*(m-2)**2*((m-1)**2 + 3*(d-1))),
    "a^2*S^2": s.factor(m**2*(m-2)*(m-3)*((m-1)**2 + (d-1))),
    "a*b*S^2": s.factor(m**2*(m-2)**2*((m-1)**2 + (d-1))),
    "b^2*S^2": s.factor(m**2*(m-2)*(m-3)*((m-1)**2 + (d-1))),
}
radial_struct = {
    "S^3": s.factor(f3**2 + 3*(d-1)*kt**2),
    "a^2*S^2": s.factor(f4*f2 + (d-1)*lt*ht),
    "a*b*S^2": s.factor(f3**2 + (d-1)*kt**2),
    "b^2*S^2": s.factor(f2*f4 + (d-1)*ht*lt),
}
# derivative order on x and y after replacing each momentum by -i partial.
ORDERS = {"S^3":(3,3),"a^2*S^2":(4,2),"a*b*S^2":(3,3),"b^2*S^2":(2,4)}

def power(label,var):
    for tok in label.split('*'):
        if tok == var: return 1
        mm = re.fullmatch(re.escape(var)+r"\^(\d+)", tok)
        if mm: return int(mm.group(1))
    return 0

def beta_for(family,label):
    ox,oy=ORDERS[label]
    # n-th derivative of |x|^(2-d) scales as r^(2-d-n).
    ex = d + ox - 2
    ey = d + oy - 2
    rt=ROUTES[family]
    a = 1-ex if rt['rx']=='tau' else s.Integer(1)
    # source weight contributes one extra power of (1-tau).
    b = 2-ey if rt['ry']=='1-tau' else s.Integer(2)
    return s.factor(s.gamma(a)*s.gamma(b)/s.gamma(a+b)), a, b

def master(family,label,coeff):
    rt=ROUTES[family]
    ox,oy=ORDERS[label]
    orientation = rt['sx']**(ox % 2) * rt['sy']**(oy % 2)
    # Total numerator degree is six, hence (-i)^6 = -1.
    fourier_sign = s.Integer(-1)
    beta,a,b = beta_for(family,label)
    expr = s.factor(coeff * fourier_sign * orientation * C**2 * closed_struct[label] * beta * L**(-2*d-2))
    de = 4-2*eps
    expr_eps = expr.subs(d,de)
    residue = s.factor(s.limit(eps*expr_eps,eps,0))
    finite_pole = bool(residue != 0)
    return {
        'beta_a':str(a),'beta_b':str(b),'orientation_sign':orientation,
        'coefficient_d':str(coeff),'structure_d':str(closed_struct[label]),
        'master_d':str(expr),'residue_1_over_epsilon':str(residue),
        'has_simple_pole':finite_pole,
    }, residue

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('input'); args=ap.parse_args()
    src=json.loads(Path(args.input).read_text())
    upstream_ok=src.get('classification')==EXPECTED_UPSTREAM
    labels=src.get('basis_labels',[]); formulas=src.get('coefficient_formulas',{})
    basis_ok=len(labels)==28 and len(set(labels))==28
    radial_ok=all(s.simplify(radial_struct[k]-closed_struct[k])==0 for k in closed_struct)
    rows={}; total_res=s.Integer(0); unsupported=[]; nonzero_two=[]
    for fam in FAMILIES:
        famrows=[]
        for entry in formulas.get(fam,[]):
            label=entry['basis']; i=power(label,'Q'); j=power(label,'K')
            if i!=0 or j!=0: continue
            coeff=s.sympify(entry['coefficient_d'])
            if coeff==0: continue
            nonzero_two.append([fam,label])
            if label not in ORDERS:
                unsupported.append([fam,label]); continue
            row,res=master(fam,label,coeff)
            row['basis']=label
            famrows.append(row); total_res += res
        rows[fam]=famrows
    total_res=s.factor(total_res)
    # Independent exact check of the only pole-producing beta residue actually encountered.
    beta_g=s.gamma(1-d)*s.gamma(-d)/s.gamma(1-2*d)
    beta_g_res=s.factor(s.limit(eps*beta_g.subs(d,4-2*eps),eps,0))
    # Independent residue from Gamma(-n+a*eps) ~ (-1)^n/(n!*a*eps).
    r1=s.Rational((-1)**3, s.factorial(3)*2)
    r2=s.Rational((-1)**4, s.factorial(4)*2)
    rd=s.Rational((-1)**7, s.factorial(7)*4)
    beta_g_res_by_gamma=s.factor(r1*r2/rd)
    beta_residue_ok=s.simplify(beta_g_res-beta_g_res_by_gamma)==0
    # Brute-force D=4 Cartesian derivative check at x=2 n, y=3 n (C_d omitted).
    D4=4
    xx=s.symbols('x0:4'); yy=s.symbols('y0:4')
    fx=sum(z*z for z in xx)**s.Rational(2-D4,2); fy=sum(z*z for z in yy)**s.Rational(2-D4,2)
    sub={xx[0]:s.Integer(2),yy[0]:s.Integer(3),**{xx[i]:0 for i in range(1,D4)},**{yy[i]:0 for i in range(1,D4)}}
    direct_cart={
      'S^3':sum(s.diff(fx,xx[i],xx[j],xx[k])*s.diff(fy,yy[i],yy[j],yy[k]) for i in range(D4) for j in range(D4) for k in range(D4)),
      'a^2*S^2':sum(s.diff(fx,xx[0],xx[0],xx[i],xx[j])*s.diff(fy,yy[i],yy[j]) for i in range(D4) for j in range(D4)),
      'a*b*S^2':sum(s.diff(fx,xx[0],xx[i],xx[j])*s.diff(fy,yy[0],yy[i],yy[j]) for i in range(D4) for j in range(D4)),
      'b^2*S^2':sum(s.diff(fx,xx[i],xx[j])*s.diff(fy,yy[0],yy[0],yy[i],yy[j]) for i in range(D4) for j in range(D4)),
    }
    cart_ok=True
    for lab,(ox,oy) in ORDERS.items():
        direct=s.simplify(direct_cart[lab].subs(sub))
        closed=s.simplify(closed_struct[lab].subs(d,4)*s.Integer(2)**(2-4-ox)*s.Integer(3)**(2-4-oy))
        cart_ok &= bool(s.simplify(direct-closed)==0)
    checks={
      'A_frozen_ITER140_PASS':bool(upstream_ok),
      'B_exact_28_unique_basis':bool(basis_ok),
      'C_only_Q0K0_two_propagator_sector_evaluated':True,
      'D_all_nonzero_two_propagator_basis_labels_supported':not unsupported,
      'E_radial_tensor_contractions_independently_match_closed_forms':bool(radial_ok),
      'F_D4_cartesian_derivative_spotcheck':bool(cart_ok),
      'G_beta_meromorphic_residue_independent_gamma_crosscheck':bool(beta_residue_ok),
      'H_contact_and_counterterm_sectors_not_evaluated':True,
      'I_no_fitted_threshold_or_expected_residue':True,
    }
    if not upstream_ok: cls='BLOCKED_BY_ITER140_GENERAL_D_AUTHORITY'
    elif unsupported: cls='BLOCKED_UNSUPPORTED_TWO_PROPAGATOR_MASTER_BASIS'
    elif all(checks.values()) and total_res!=0:
        cls='PASS_SCOPED_FIRST_MG_NONLOCAL_TWO_PROPAGATOR_MASTER_POLE_NONZERO_CONTACT_SUBTRACTION_OPEN'
    elif all(checks.values()):
        cls='PASS_SCOPED_FIRST_MG_NONLOCAL_TWO_PROPAGATOR_MASTER_POLE_ZERO_CONTACT_SUBTRACTION_OPEN'
    else: cls='SCIENTIFIC_FAIL_FIRST_MG_NONLOCAL_MASTER_POLE'
    out={
      'gate':'ITER150_FIXED_GEODESIC_CURVATURE_FIRST_MG_NONLOCAL_TWO_PROPAGATOR_MASTER_POLE',
      'classification':cls,
      'regularization':'d=4-2 epsilon; meromorphic continuation from convergent Beta-function domain',
      'fourier_convention':'int d^d p/(2pi)^d exp(i p.x)/p^2 = Gamma(d/2-1)/(4*pi^(d/2))*|x|^(2-d)',
      'source_weight':'1-tau','L_condition':'L>0','n2':1,
      'nonzero_two_propagator_inputs':nonzero_two,
      'families':rows,
      'summed_nonlocal_two_propagator_residue_1_over_epsilon':str(total_res),
      'beta_G_b2S2_residue_crosscheck':str(beta_g_res),
      'beta_G_b2S2_residue_by_independent_gamma_residues':str(beta_g_res_by_gamma),
      'checks':checks,
      'claim_ceiling':'raw separated connected-cross TWO_PROPAGATOR master pole only; Q/K-cancelled contact terms, endpoint/bulk counterterms, subdivergence subtraction, full B1, gauge/BRST consistency, EDT, bridge, new physics and candidate theory remain open',
    }
    Path('iter150_first_mg_nonlocal_two_propagator_master_pole.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'classification':cls,'nonzero_two_propagator_inputs':nonzero_two,
      'family_residues':{f:{r['basis']:r['residue_1_over_epsilon'] for r in rr} for f,rr in rows.items()},
      'summed_residue':str(total_res),'checks':checks},indent=2))
    if cls.startswith('BLOCKED') or cls.startswith('SCIENTIFIC_FAIL'): raise SystemExit(1)

if __name__=='__main__': main()
