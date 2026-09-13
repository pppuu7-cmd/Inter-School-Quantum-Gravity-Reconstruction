import argparse, json, math
from fractions import Fraction

K=12
G=Fraction(1,3)
ALLOWED=[Fraction(0),Fraction(3,2),Fraction(3),Fraction(9,2),Fraction(6)]
SOURCE_ALPHAS=[-1.0,0.35,2.0]
HELDOUT=[-0.5,0.0,0.5,1.5]

def qdim(j):
    return math.sin(math.pi*(2*float(j)+1)/(K+2))/math.sin(math.pi/(K+2))

def c_abs(ext, lint, alpha):
    prod=math.prod(qdim(x) for x in ext)
    return (prod**alpha)*(qdim(lint)**2)

def phase_exp(ext, lint):
    # j_i^+ + j_i^- = l_i under the frozen EPRL map.
    return sum(ext)-2*lint

def lane_a():
    tests=[((Fraction(3),)*4,Fraction(0)),((Fraction(3),)*4,Fraction(3)),((Fraction(3),)*4,Fraction(6)),((Fraction(3,2),Fraction(3),Fraction(9,2),Fraction(6)),Fraction(3))]
    integral=all(phase_exp(e,l).denominator==1 for e,l in tests)
    dims_positive=all(qdim(x)>0 for x in ALLOWED)
    alpha1_ok=True
    omission_rejected=False
    for ext,lint in tests:
        source=math.prod(qdim(x) for x in ext)*(qdim(lint)**2)
        got=c_abs(ext,lint,1.0)
        alpha1_ok &= abs(source-got)<=1e-12*max(1.0,abs(source))
        wrong=math.prod(qdim(x) for x in ext)
        if abs(wrong-source)>1e-10: omission_rejected=True
    ok=integral and dims_positive and alpha1_ok and omission_rejected
    return {'lane':'A','pass':bool(ok),'phase_integral':integral,'qdims_positive':dims_positive,'alpha1_eq68_match':alpha1_ok,'omit_internal_dim_control_rejected':omission_rejected}

def ratios(exts,alpha):
    base=c_abs(exts[0],Fraction(3),alpha)
    return [c_abs(e,Fraction(3),alpha)/base for e in exts]

def lane_b():
    exts=[(Fraction(0),Fraction(0),Fraction(0),Fraction(0)),(Fraction(3),)*4,(Fraction(3,2),Fraction(3),Fraction(9,2),Fraction(6))]
    rs={str(a):ratios(exts,a) for a in SOURCE_ALPHAS}
    support_identical=all(all(v>0 for v in vals) for vals in rs.values())
    changed=any(abs(rs[str(SOURCE_ALPHAS[0])][i]-rs[str(SOURCE_ALPHAS[-1])][i])>1e-9 for i in range(len(exts)))
    return {'lane':'B','pass':bool(support_identical and changed),'support_identical':support_identical,'nontrivial_ratio_changes':changed,'ratios':rs}

def lane_c():
    endpoint=(Fraction(0),Fraction(6),Fraction(0),Fraction(6))
    mixed=(Fraction(0),Fraction(3),Fraction(6),Fraction(3))
    vals_end=[c_abs(endpoint,Fraction(0),a) for a in SOURCE_ALPHAS]
    vals_mix=[c_abs(mixed,Fraction(0),a) for a in SOURCE_ALPHAS]
    endpoint_insensitive=max(vals_end)-min(vals_end)<1e-12
    mixed_sensitive=max(vals_mix)-min(vals_mix)>1e-8
    # false-source classical dimensions 2j+1 must disagree on nontrivial q-group labels
    qprod=math.prod(qdim(x) for x in mixed)
    classical=math.prod(2*float(x)+1 for x in mixed)
    false_control=abs(qprod-classical)>1e-6
    return {'lane':'C','pass':bool(endpoint_insensitive and mixed_sensitive and false_control),'endpoint_alpha_insensitive':endpoint_insensitive,'mixed_alpha_sensitive':mixed_sensitive,'classical_dimension_control_rejected':false_control,'qprod':qprod,'classical_prod':classical}

def lane_d():
    ext=(Fraction(3,2),Fraction(3),Fraction(9,2),Fraction(6))
    prod=math.prod(qdim(x) for x in ext)
    target=math.log(prod)
    perms=[ext,(ext[1],ext[0],ext[3],ext[2]),tuple(reversed(ext))]
    perm_ok=all(abs(math.prod(qdim(x) for x in p)-prod)<1e-12 for p in perms)
    slopes=[]
    slope_ok=True
    wrong_rejected=False
    h=1e-6
    for a in HELDOUT:
        fp=math.log(c_abs(ext,Fraction(3),a+h)); fm=math.log(c_abs(ext,Fraction(3),a-h))
        slope=(fp-fm)/(2*h); slopes.append(slope)
        slope_ok &= abs(slope-target)<1e-9
        wrong_rejected |= abs(slope+target)>1e-6
    return {'lane':'D','pass':bool(perm_ok and slope_ok and wrong_rejected),'permutation_invariant':perm_ok,'analytic_log_slope':target,'numeric_slopes':slopes,'slope_match':slope_ok,'wrong_sign_control_rejected':wrong_rejected}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--lane',choices=list('ABCD'),required=True); a=p.parse_args()
    r={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}[a.lane]()
    print(json.dumps(r,indent=2,sort_keys=True))
    if not r['pass']: raise SystemExit(2)
if __name__=='__main__': main()
