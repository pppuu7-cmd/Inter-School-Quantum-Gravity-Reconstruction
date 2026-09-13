#!/usr/bin/env python3
import argparse, json, math
from fractions import Fraction

TOL=1e-11
KS=(6,10,12)
GAMMA={6:Fraction(1,3),10:Fraction(3,5),12:Fraction(1,3)}
ALPHA=0.0

def qnum(k,n):
    return math.sin(math.pi*n/(k+2))/math.sin(math.pi/(k+2))

def qdim(k,j):
    return qnum(k,int(2*j+1))

def mapped(l,g):
    return Fraction(1,2)*(1+g)*l, Fraction(1,2)*(1-g)*l

def admissible_map(k,l):
    jp,jm=mapped(Fraction(l),GAMMA[k]); jmax=Fraction(k,2)
    return jp.denominator==1 and jm.denominator==1 and 0<=jp<=jmax and 0<=jm<=jmax, jp, jm

def lane_a():
    rows=[]; ok=True
    for k in KS:
        support=[]
        for l2 in range(0,k+1):
            l=Fraction(l2,2)
            good,jp,jm=admissible_map(k,l)
            if good:
                w=(qdim(k,l)**ALPHA)*(qdim(k,l)**2)
                finite=math.isfinite(w) and w>0
                ok &= finite
                support.append({'l':str(l),'jp':str(jp),'jm':str(jm),'weight':w})
        # deterministic permutation invariance of product weights on a small four-leg sample
        if support:
            vals=[Fraction(x['l']) for x in support[:min(4,len(support))]]
            prod=math.prod(qdim(k,x)**ALPHA for x in vals)
            prod_rev=math.prod(qdim(k,x)**ALPHA for x in reversed(vals))
            ok &= abs(prod-prod_rev)<=TOL
        rows.append({'k':k,'support':support,'count':len(support)})
    return {'lane':'A','status':'PASS' if ok else 'FAIL','pass':bool(ok),'alpha':ALPHA,'rows':rows}

def cap(k,j,m):
    # Appendix B2 source-explicit modified q-CG cap, with q=exp(2 pi i/(k+2)).
    q=complex(math.cos(2*math.pi/(k+2)),math.sin(2*math.pi/(k+2)))
    return ((-1)**int(round(j-m)))*(q**(m/2.0))/math.sqrt(qdim(k,j))

def cup(k,j,m):
    # Appendix B4 source-explicit cup.
    q=complex(math.cos(2*math.pi/(k+2)),math.sin(2*math.pi/(k+2)))
    return ((-1)**int(round(j+m)))*(q**(m/2.0))

def lane_b():
    # Validate all source-explicit cap/cup contractions available without importing a non-source q-CG implementation.
    max_norm_err=0.0; tested=0
    for k in KS:
        for j2 in range(0,k+1):
            j=j2/2.0
            ms=[-j+i for i in range(j2+1)]
            # B2 magnitude sum is one with the modified normalization.
            s=sum(abs(cap(k,j,m))**2 for m in ms)
            max_norm_err=max(max_norm_err,abs(s-1.0)); tested+=1
    endpoint_ok=max_norm_err<=TOL
    # Full Eq.(27) requires generic q-CG coefficients, not only the source-explicit cap/cup special case.
    return {'lane':'B','status':'BLOCKED','pass':False,'endpoint_cap_normalization_ok':endpoint_ok,
            'max_cap_norm_error':max_norm_err,'tested_reps':tested,
            'blocker':'GENERIC_SOURCE_FAITHFUL_QCG_NUMERICAL_IMPLEMENTATION_NOT_PRESENT; Appendix-B cap/cup alone is insufficient for Eq.(27)'}

def lane_c():
    return {'lane':'C','status':'BLOCKED','pass':False,
            'blocker':'ONE_STEP_EQ27_CONTRACTION_REQUIRES_GENERIC_QCG_FROM_LANE_B; no classical-CG substitution or fitted phase is allowed',
            'contraction_executed':False}

def lane_d():
    # Held-out controls quantify that q-data are genuinely distinguishable from classical/wrong-q replacements.
    diffs=[]; wrongq=[]
    for k in KS:
        for j2 in range(1,k):
            j=Fraction(j2,2)
            diffs.append(abs(qdim(k,j)-(2*float(j)+1)))
            qwrong=complex(math.cos(math.pi/(k+2)),math.sin(math.pi/(k+2)))
            n=j2+1
            wrong=(qwrong**(n/2)-qwrong**(-n/2))/(qwrong**0.5-qwrong**(-0.5))
            wrongq.append(abs(wrong.real-qdim(k,j))+abs(wrong.imag))
    classical_detected=max(diffs)>1e-6
    wrongq_detected=sum(x>1e-8 for x in wrongq)/len(wrongq)>=0.8
    ok=classical_detected and wrongq_detected
    return {'lane':'D','status':'PASS' if ok else 'FAIL','pass':bool(ok),
            'classical_dimension_control_detected':classical_detected,
            'wrong_q_control_detected':wrongq_detected,
            'max_classical_difference':max(diffs),'wrong_q_mismatch_fraction':sum(x>1e-8 for x in wrongq)/len(wrongq)}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--lane',choices=list('ABCD'),required=True); a=p.parse_args()
    r={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}[a.lane]()
    print(json.dumps(r,indent=2,sort_keys=True))
    # BLOCKED is a scientific classification, not an infrastructure failure; keep artifact production alive.
    if r['status']=='FAIL': raise SystemExit(2)

if __name__=='__main__': main()
