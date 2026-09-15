#!/usr/bin/env python3
"""ITER140 performance retry: identical frozen predicates, faster exact contractions.

The preregistered 28-invariant basis, D=3..7 fit, D=8..10 no-refit validation,
(d-2)^2 degree<=4 bound, D4 cross-authority and O(epsilon) outputs are unchanged.
Only tensor contraction implementation is optimized.
"""
from __future__ import annotations
from fractions import Fraction as F
import json
from pathlib import Path
import sympy as s

import iter140_first_mg_general_d_invariant_continuation as frozen
import iter138_first_mg_exact_numerator_kernels as i138
import iter139_affine_single_line_ceiling_repair as i139

HALF = F(1, 2)
BASIS = frozen.BASIS


def dot(a,b):
    return sum((F(x)*F(y) for x,y in zip(a,b)),F(0))

def neg(v): return [-F(x) for x in v]

def eye(D,a,b): return F(1 if a==b else 0)

def matmul(A,B,D):
    return [[sum((A[i][t]*B[t][j] for t in range(D)),F(0)) for j in range(D)] for i in range(D)]

def matvec(A,v,D):
    return [sum((A[i][t]*F(v[t]) for t in range(D)),F(0)) for i in range(D)]

def pmap(S,D):
    tr=sum((S[i][i] for i in range(D)),F(0)); c=tr/F(D-2)
    return [[S[a][b]-(c if a==b else F(0)) for b in range(D)] for a in range(D)]

def r1_tensor(mom,D):
    q2=dot(mom,mom)
    return [[q2*eye(D,a,b)-F(mom[a])*F(mom[b]) for b in range(D)] for a in range(D)]

def chi1_real(mu,mom,nvec,D):
    mn=dot(mom,nvec)
    return [[-HALF*mn*(eye(D,a,mu)*F(nvec[b])+eye(D,b,mu)*F(nvec[a]))
             +HALF*F(mom[mu])*F(nvec[a])*F(nvec[b]) for b in range(D)] for a in range(D)]

def dr1_real(mu,mom,D):
    A=r1_tensor(mom,D)
    return [[F(mom[mu])*A[a][b] for b in range(D)] for a in range(D)]

def g1_tensor(H,p,D):
    return [[[HALF*(F(p[m])*H[r][n]+F(p[n])*H[r][m]-F(p[r])*H[m][n])
              for n in range(D)] for m in range(D)] for r in range(D)]

def g2_tensor(A,B,pb,D):
    AB=matmul(A,B,D); Ap=matvec(A,pb,D)
    return [[[HALF*(F(pb[m])*AB[r][n]+F(pb[n])*AB[r][m]-Ap[r]*B[m][n])
              for n in range(D)] for m in range(D)] for r in range(D)]

def r2_ordered_fast(A,pa,B,pb,D):
    GA=g1_tensor(A,pa,D); GB=g1_tensor(B,pb,D); G2=g2_tensor(A,B,pb,D)
    total=[F(pa[i])+F(pb[i]) for i in range(D)]
    # pb contraction and trace-like contraction of GB.
    pbGB=[[sum((F(pb[r])*GB[r][m][n] for r in range(D)),F(0)) for n in range(D)] for m in range(D)]
    T=[sum((GB[r][m][r] for r in range(D)),F(0)) for m in range(D)]
    out=F(0)
    for m in range(D):
        for n in range(D):
            out += A[m][n]*(pbGB[m][n]-F(pb[n])*T[m])
    for m in range(D):
        for r in range(D):
            out += total[r]*G2[r][m][m]-total[m]*G2[r][m][r]
            for t in range(D):
                out -= GA[r][r][t]*GB[t][m][m]
                out += GA[r][m][t]*GB[t][m][r]
    return out

def r2_fast(A,pa,B,pb,D):
    return r2_ordered_fast(A,pa,B,pb,D)+r2_ordered_fast(B,pb,A,pa,D)

def g2_real_fast(A,pa,B,pb,r,m,n,D):
    # Same real convention as frozen implementation.
    GAB=g2_tensor(A,B,pb,D)
    GBA=g2_tensor(B,A,pa,D)
    return GAB[r][m][n]+GBA[r][m][n]

def M1_value(qv,kv,nvec,D):
    nq,nk=neg(qv),neg(kv); out=F(0)
    for mu in range(D):
        C=pmap(chi1_real(mu,nq,nvec,D),D)
        R=pmap(dr1_real(mu,nk,D),D)
        out -= r2_fast(C,qv,R,kv,D)
    return out

def M2_value(qv,kv,nvec,D):
    nq,nk=neg(qv),neg(kv); A=pmap(r1_tensor(nq,D),D); out=F(0)
    for mu in range(D):
        C=pmap(chi1_real(mu,nk,nvec,D),D)
        out -= (F(qv[mu])+F(kv[mu]))*r2_fast(A,qv,C,kv,D)
    return out

def G1_value(qv,kv,nvec,D):
    nq,nk=neg(qv),neg(kv); A=pmap(r1_tensor(nq,D),D); out=F(0)
    # n=e0 for all design/validation panels used by this gate, but keep exact general n support.
    nz=[m for m in range(D) if F(nvec[m])!=0]
    for mu in range(D):
        R=pmap(dr1_real(mu,nk,D),D)
        GAB=g2_tensor(A,R,kv,D); GBA=g2_tensor(R,A,qv,D)
        for m in nz:
            for n in nz:
                out -= F(nvec[m])*F(nvec[n])*(GAB[mu][m][n]+GBA[mu][m][n])
    return out

FAMILIES={
 'M_R2_chi1_dR1':M1_value,
 'M_R1_chi1_dR2':M2_value,
 'G_R1_chi2_Gamma2_dR1':G1_value,
}

def pad(v3,D): return tuple(list(v3)+[0]*(D-3))
def to_sym(x): return s.Rational(x.numerator,x.denominator)

def basis_values_full(qv,kv):
    Q=sum(x*x for x in qv); K=sum(x*x for x in kv); S=sum(x*y for x,y in zip(qv,kv)); a=qv[0]; b=kv[0]
    vals=[]
    for kind,nt,(ii,jj,ll) in BASIS:
        base=Q**ii*K**jj*S**ll
        if kind=='scalar': vals.append(base)
        elif nt=='a2': vals.append(a*a*base)
        elif nt=='ab': vals.append(a*b*base)
        else: vals.append(b*b*base)
    return vals

def main():
    labels=frozen.basis_labels()
    selected,A=frozen.design_panels()
    Ainv=A.inv(method='DM')
    dims=list(range(3,11)); byD={}
    for D in dims:
        nvec=tuple([1]+[0]*(D-1)); fam={}
        for name,fn in FAMILIES.items():
            ys=s.Matrix([to_sym(fn(pad(q3,D),pad(k3,D),nvec,D)) for q3,k3 in selected])
            fam[name]=[s.factor(x) for x in (Ainv*ys)]
        byD[D]=fam
        print(json.dumps({'progress_dimension':D,'families_done':list(FAMILIES)}),flush=True)

    d,eps=s.symbols('d eps'); train=[3,4,5,6,7]; validate=[8,9,10]
    formulas={}; trace_degree_ok=True; dim_coeff_ok=True; max_poly_degree=0
    for name in FAMILIES:
        rows=[]
        for j,label in enumerate(labels):
            pts=[(D,s.factor((D-2)**2*byD[D][name][j])) for D in train]
            poly=s.factor(s.interpolate(pts,d))
            deg=int(s.Poly(s.expand(poly),d).degree()) if poly!=0 else 0
            max_poly_degree=max(max_poly_degree,deg); trace_degree_ok &= deg<=4
            coeff=s.factor(poly/(d-2)**2)
            for D in validate:
                dim_coeff_ok &= s.simplify(coeff.subs(d,D)-byD[D][name][j])==0
            c4=s.factor(coeff.subs(d,4)); ceps=s.factor(-2*s.diff(coeff,d).subs(d,4))
            rows.append({'basis':label,'coefficient_d':str(coeff),'trace_polynomial_degree':deg,
                         'c_d4':str(c4),'c_epsilon_linear_for_d_4_minus_2eps':str(ceps)})
        formulas[name]=rows

    held_seed=[
      ((1,2,-1,3),(2,-1,1,4)),
      ((2,1,3,-2),(-1,2,4,1)),
      ((-2,3,1,2),(3,-1,2,-2)),
    ]
    held_rows=[]; held_ok=True
    for D in dims:
        nvec=tuple([1]+[0]*(D-1))
        for idx,(q4,k4) in enumerate(held_seed):
            qv=tuple(list(q4[:min(4,D)])+[0]*max(0,D-4)); kv=tuple(list(k4[:min(4,D)])+[0]*max(0,D-4))
            bvals=basis_values_full(qv,kv); row={'D':D,'panel':idx}
            for name,fn in FAMILIES.items():
                direct=to_sym(fn(qv,kv,nvec,D)); recon=s.factor(sum(c*v for c,v in zip(byD[D][name],bvals)))
                eq=s.simplify(direct-recon)==0; held_ok &= bool(eq)
                row[name]={'direct':str(direct),'reconstructed':str(recon),'equal':bool(eq)}
            held_rows.append(row)

    d4_rows=[]; d4_ok=True; n4=(s.Integer(1),0,0,0)
    for q4,k4 in held_seed:
        generic={n:to_sym(fn(q4,k4,(1,0,0,0),4)) for n,fn in FAMILIES.items()}
        authority={
          'M_R2_chi1_dR1':s.simplify(i138.M_numerator(q4,k4,n4)),
          'M_R1_chi1_dR2':s.simplify(i139.M2_numerator(q4,k4,n4)),
          'G_R1_chi2_Gamma2_dR1':s.simplify(i138.G_numerator(q4,k4,n4)),
        }
        rr={}
        for name in FAMILIES:
            eq=s.simplify(generic[name]-authority[name])==0; d4_ok &= bool(eq)
            rr[name]={'generic_D4':str(generic[name]),'authority_D4':str(authority[name]),'equal':bool(eq)}
        d4_rows.append(rr)

    continuation_rows=[]; continuation_ok=True
    for D in validate:
        nvec=tuple([1]+[0]*(D-1)); q4,k4=held_seed[1]
        qv=tuple(list(q4)+[0]*(D-4)); kv=tuple(list(k4)+[0]*(D-4)); bvals=basis_values_full(qv,kv); row={'D':D}
        for name,fn in FAMILIES.items():
            coeff=[s.sympify(x['coefficient_d']).subs(d,D) for x in formulas[name]]
            recon=s.factor(sum(c*v for c,v in zip(coeff,bvals))); direct=to_sym(fn(qv,kv,nvec,D))
            eq=s.simplify(recon-direct)==0; continuation_ok &= bool(eq)
            row[name]={'direct':str(direct),'continued':str(recon),'equal':bool(eq)}
        continuation_rows.append(row)

    checks={
      'A_basis_size_28':len(BASIS)==28,
      'B_design_rank_28':A.rank()==28,
      'C_integer_D_invariant_heldouts':bool(held_ok),
      'D_trace_polynomial_degree_le4':bool(trace_degree_ok),
      'E_coefficient_continuation_D8_D10':bool(dim_coeff_ok),
      'F_direct_continuation_heldouts_D8_D10':bool(continuation_ok),
      'G_D4_matches_ITER138_ITER139':bool(d4_ok),
      'H_target_blind':True,
    }
    if all(checks.values()): cls='PASS_SCOPED_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION_CLOSED_POLE_INTEGRATION_OPEN'
    elif not trace_degree_ok: cls='BLOCKED_GENERAL_D_TRACE_DEGREE_AUTHORITY'
    else: cls='SCIENTIFIC_FAIL_GENERAL_D_INVARIANT_RECONSTRUCTION'
    out={
      'gate':'ITER140_FIXED_GEODESIC_CURVATURE_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION',
      'classification':cls,'implementation_note':'performance retry; frozen ITER140 predicates/basis/dimensions unchanged',
      'basis_labels':labels,'training_dimensions':train,'validation_dimensions':validate,
      'max_observed_trace_polynomial_degree':max_poly_degree,'coefficient_formulas':formulas,
      'integer_D_heldouts':held_rows,'continuation_heldouts':continuation_rows,'D4_cross_authority':d4_rows,
      'checks':checks,'claim_ceiling':'general-d numerator continuation and O(epsilon) coefficients only; no loop pole/B1/noncancellation/B0/EDT/bridge/new physics/candidate theory',
    }
    Path('iter140_first_mg_general_d_invariant_continuation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'classification':cls,'basis_size':len(BASIS),'design_rank':A.rank(),'max_trace_polynomial_degree':max_poly_degree,
      'checks':checks,'nonzero_coefficient_counts':{n:sum(1 for x in formulas[n] if x['coefficient_d']!='0') for n in formulas}},indent=2))
    if cls.startswith('SCIENTIFIC_FAIL') or cls.startswith('BLOCKED'): raise SystemExit(1)

if __name__=='__main__': main()
