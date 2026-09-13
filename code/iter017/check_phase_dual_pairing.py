from fractions import Fraction
import json


def sign_from_integer(n):
    if n.denominator != 1:
        raise ValueError(f'expected integer exponent, got {n}')
    return -1 if int(n) % 2 else 1


def cap(j, m, mp):
    # Dittrich et al. Appendix B, B2:
    # (-1)^(j-m) q^(m/2) delta_{m,-m'}
    if mp != -m:
        return None
    return sign_from_integer(j-m), Fraction(m, 2)


def cup(j, mp, mpp):
    # Dittrich et al. Appendix B, B4:
    # (-1)^(j+m') q^(m'/2) delta_{m',-m''}
    if mpp != -mp:
        return None
    return sign_from_integer(j+mp), Fraction(mp, 2)


def magnetic_values(j):
    n = int(2*j)
    return [Fraction(-n + 2*i, 2) for i in range(n+1)]


def check_cap_cup(max_twice_j=12):
    failures=[]
    cases=0
    for twj in range(max_twice_j+1):
        j=Fraction(twj,2)
        vals=magnetic_values(j)
        for m in vals:
            for mpp in vals:
                total=[]
                for mp in vals:
                    c=cap(j,m,mp)
                    u=cup(j,mp,mpp)
                    if c is not None and u is not None:
                        total.append((c[0]*u[0], c[1]+u[1]))
                expected = 1 if mpp==m else 0
                if total:
                    s,e=total[0]
                    ok=(expected==1 and s==1 and e==0)
                else:
                    ok=(expected==0)
                cases += 1
                if not ok:
                    failures.append({'j':str(j),'m':str(m),'mpp':str(mpp),'terms':[(s,str(e)) for s,e in total],'expected':expected})
    return {'pass':not failures,'cases':cases,'failures':failures[:10]}


def allowed_target(k,j1,j2,j3):
    return (
        abs(j1-j2) <= j3 <= j1+j2
        and (j1+j2+j3).denominator == 1
        and j1+j2+j3 <= k
        and all(Fraction(0) <= x <= Fraction(k,2) for x in (j1,j2,j3))
    )


def allowed_fm(r,I,J,K):
    return (
        abs(I-J) <= K <= min(I+J, Fraction(r-2)-I-J)
        and (I+J+K).denominator == 1
        and all(Fraction(0) <= x <= Fraction(r-2,2) for x in (I,J,K))
    )


def check_fusion(max_k=16):
    failures=[]
    cases=0
    for k in range(1,max_k+1):
        r=k+2
        vals=[Fraction(n,2) for n in range(k+1)]
        for a in vals:
            for b in vals:
                for c in vals:
                    t=allowed_target(k,a,b,c)
                    f=allowed_fm(r,a,b,c)
                    cases += 1
                    if t!=f:
                        failures.append({'k':k,'r':r,'j1':str(a),'j2':str(b),'j3':str(c),'target':t,'fm':f})
                        if len(failures)>=10:
                            return {'pass':False,'cases':cases,'failures':failures}
    return {'pass':not failures,'cases':cases,'failures':failures}


def main():
    capcup=check_cap_cup()
    fusion=check_fusion()
    out={
        'cap_cup_identity': capcup,
        'fusion_cutoff_equivalence_r_eq_k_plus_2': fusion,
        'A9_phase_constraint': {
            'statement': 'For a normalized bilinear q-CG channel C -> lambda C, target A9 scales by lambda^2; preserving A9 requires lambda^2=1, hence lambda=+/-1 over C.',
            'residual_freedom': 'sign',
            'paired_dual_consequence': 'B5/B6 build the dual map from the same normalized channel; under the surviving lambda=+/-1 rephasing, a paired composition scales by lambda^2=1.'
        },
        'FM_root_domain': {
            'source_assumption': 'r>2 odd primitive root',
            'dictionary': 'r_FM = k_target + 2 for the fusion cutoff comparison',
            'consequence': 'FM root-of-unity section maps directly only to odd target k; it does not directly qualify even target k such as k=12.'
        },
        'physics_amplitude_runs': 0,
        'fitted_phases': 0
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    if not (capcup['pass'] and fusion['pass']):
        raise SystemExit(1)

if __name__=='__main__':
    main()
