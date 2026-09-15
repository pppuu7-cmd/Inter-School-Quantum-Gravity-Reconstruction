#!/usr/bin/env python3
"""ITER144: pinned FeynGrav three-graviton source and independent EH cubic comparison.

The source vertex is used only for tensor-structure authority. Absolute Euclidean
phase/sign normalization remains explicitly open.
"""
from __future__ import annotations
from fractions import Fraction as F
import hashlib
import itertools
import json
import re
import urllib.request
import sympy as s

PINNED_COMMIT = "91f697a1ca62fd051cbb297827cb1a491b393538"
PINNED_BLOB = "98297aac3b640a93ac80c2cc72a8275280819954"
RAW_URL = f"https://raw.githubusercontent.com/BorisNLatosh/FeynGrav/{PINNED_COMMIT}/Libs/GravitonVertex_1"
D = 4
I = s.I

PAIR_RE = re.compile(r"^Pair\[(.+),(.+)\]$")
LI_RE = re.compile(r"^LorentzIndex\[([mn][123]),D\]$")
MOM_RE = re.compile(r"^Momentum\[(p[123]),D\]$")


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def split_top_level_terms(expr: str):
    # The pinned library is a flat sum of products; Pair arguments contain no +/-.
    terms=[]; start=0
    for i,ch in enumerate(expr):
        if i>0 and ch in '+-':
            terms.append(expr[start:i]); start=i
    terms.append(expr[start:])
    return [t for t in terms if t]


def split_product(term: str):
    # '*' occurs only between factors in the pinned grammar.
    return term.split('*')


def parse_source(text: str):
    expr=''.join(text.split())
    terms=[]
    unknown=[]
    common_phase_ok=True
    seen_index=set(); seen_mom=set()
    for raw in split_top_level_terms(expr):
        sign=1
        if raw[0]=='+': raw=raw[1:]
        elif raw[0]=='-': sign=-1; raw=raw[1:]
        coeff=F(sign,1); factors=[]; has_i=False; has_k=False
        for fac in split_product(raw):
            if fac=='I': has_i=True; continue
            if fac=='\\[Kappa]': has_k=True; continue
            if re.fullmatch(r"\d+/\d+",fac):
                a,b=fac.split('/'); coeff*=F(int(a),int(b)); continue
            if re.fullmatch(r"\d+",fac):
                coeff*=F(int(fac),1); continue
            m=PAIR_RE.match(fac)
            if not m:
                unknown.append(fac); continue
            a,b=m.group(1),m.group(2)
            la,lb=LI_RE.match(a),LI_RE.match(b)
            ma,mb=MOM_RE.match(a),MOM_RE.match(b)
            if la and lb:
                ia,ib=la.group(1),lb.group(1); factors.append(('metric',ia,ib)); seen_index|={ia,ib}
            elif la and mb:
                ia,pb=la.group(1),mb.group(1); factors.append(('ip',ia,pb)); seen_index.add(ia); seen_mom.add(pb)
            elif ma and lb:
                pa,ib=ma.group(1),lb.group(1); factors.append(('ip',ib,pa)); seen_index.add(ib); seen_mom.add(pa)
            elif ma and mb:
                pa,pb=ma.group(1),mb.group(1); factors.append(('pp',pa,pb)); seen_mom|={pa,pb}
            else:
                unknown.append(fac)
        common_phase_ok &= has_i and has_k
        terms.append((coeff,factors))
    return {
        'terms':terms,
        'unknown':sorted(set(unknown)),
        'common_phase_ok':common_phase_ok,
        'seen_index':sorted(seen_index),
        'seen_mom':sorted(seen_mom),
    }


def source_value(parsed, legs):
    idx={}
    mom={}
    for i,(a,b,p) in enumerate(legs,1):
        idx[f'm{i}']=a; idx[f'n{i}']=b; mom[f'p{i}']=tuple(s.Integer(x) for x in p)
    out=s.Rational(0)
    for coeff,factors in parsed['terms']:
        val=s.Rational(coeff.numerator,coeff.denominator)
        for typ,a,b in factors:
            if typ=='metric': val *= int(idx[a]==idx[b])
            elif typ=='ip': val *= mom[b][idx[a]]
            else: val *= sum(mom[a][j]*mom[b][j] for j in range(D))
            if val==0: break
        out += val
    return s.factor(out)


def momentum_degree(factors):
    return sum(0 if t=='metric' else 1 if t=='ip' else 2 for t,_,_ in factors)


def H(pair):
    a,b=pair; M=s.zeros(D); M[a,b]=1
    if a!=b: M[b,a]=1
    return M


def g1(A,p,r,m,n):
    return I*s.Rational(1,2)*(p[m]*A[r,n]+p[n]*A[r,m]-p[r]*A[m,n])


def g2_cross(A,B,pb,r,m,n):
    return -I*s.Rational(1,2)*sum(A[r,t]*(pb[m]*B[t,n]+pb[n]*B[t,m]-pb[t]*B[m,n]) for t in range(D))


def pref1(A,m,n):
    tr=sum(A[i,i] for i in range(D))
    return s.Rational(1,2)*tr*int(m==n)-A[m,n]


def eh_gamma_gamma_cubic(Hs,ps):
    """uvw coefficient of sqrt(g) g^mn (Gamma^r_ms Gamma^s_nr-Gamma^r_mn Gamma^s_rs)."""
    out=s.Integer(0)
    modes=list(zip(Hs,ps))
    # Linear prefactor times Gamma1 Gamma1: all assignments of three distinct modes.
    for ia,ib,ic in itertools.permutations(range(3),3):
        A,pa=modes[ia]; B,pb=modes[ib]; C,pc=modes[ic]
        for m in range(D):
            for n in range(D):
                P=pref1(A,m,n)
                if P==0: continue
                for r in range(D):
                    for t in range(D):
                        out += P*(g1(B,pb,r,m,t)*g1(C,pc,t,n,r)-g1(B,pb,r,m,n)*g1(C,pc,t,r,t))
    # Flat prefactor times Gamma1 Gamma2 + Gamma2 Gamma1.
    for ia,ib,ic in itertools.permutations(range(3),3):
        A,pa=modes[ia]; B,pb=modes[ib]; C,pc=modes[ic]
        for m in range(D):
            n=m
            for r in range(D):
                for t in range(D):
                    G2_tnr=g2_cross(B,C,pc,t,n,r)
                    G2_rmt=g2_cross(B,C,pc,r,m,t)
                    G2_trt=g2_cross(B,C,pc,t,r,t)
                    G2_rmn=g2_cross(B,C,pc,r,m,n)
                    out += g1(A,pa,r,m,t)*G2_tnr + G2_rmt*g1(A,pa,t,n,r)
                    out -= g1(A,pa,r,m,n)*G2_trt + G2_rmn*g1(A,pa,t,r,t)
    return s.factor(s.simplify(out))


def pol_source(parsed,pairs,ps):
    mult=s.Integer(1)
    legs=[]
    for pair,p in zip(pairs,ps):
        mult *= 1 if pair[0]==pair[1] else 2
        legs.append((pair[0],pair[1],p))
    return s.factor(mult*source_value(parsed,legs))


def main():
    data=urllib.request.urlopen(RAW_URL,timeout=30).read()
    blob=git_blob_sha(data)
    text=data.decode('utf-8')
    parsed=parse_source(text)
    source_integrity=(blob==PINNED_BLOB)
    syntax_ok=(len(parsed['unknown'])==0 and parsed['common_phase_ok'])
    exact_labels=(parsed['seen_index']==['m1','m2','m3','n1','n2','n3'] and parsed['seen_mom']==['p1','p2','p3'])
    degrees=[momentum_degree(f) for _,f in parsed['terms']]
    degree_ok=bool(degrees and min(degrees)==2 and max(degrees)==2)

    # Deterministic spatial panels; p0=0 and p1+p2+p3=0.
    panels=[
      (((1,1),(1,2),(2,2)), ((0,1,2,-1),(0,2,-1,1))),
      (((1,2),(2,3),(1,3)), ((0,2,1,1),(0,-1,2,-2))),
      (((1,1),(2,3),(3,3)), ((0,1,-2,2),(0,2,1,-1))),
      (((1,3),(1,2),(2,2)), ((0,-2,1,3),(0,1,2,-1))),
      (((2,2),(1,3),(2,3)), ((0,3,-1,1),(0,-2,2,1))),
      (((1,2),(1,2),(3,3)), ((0,1,3,-2),(0,2,-1,2))),
    ]
    panel_rows=[]; perm_ok=True; idx_ok=True; ratios=[]
    for pairs,(p1,p2) in panels:
        p3=tuple(-(p1[i]+p2[i]) for i in range(D)); ps=(p1,p2,p3)
        base=source_value(parsed,[(pairs[i][0],pairs[i][1],ps[i]) for i in range(3)])
        # All six leg permutations, carrying pair and momentum together.
        vals=[]
        for perm in itertools.permutations(range(3)):
            vals.append(source_value(parsed,[(pairs[i][0],pairs[i][1],ps[i]) for i in perm]))
        this_perm=all(s.simplify(v-base)==0 for v in vals)
        perm_ok &= this_perm
        # Within-pair symmetry.
        this_idx=True
        for leg in range(3):
            pp=list(pairs); pp[leg]=(pairs[leg][1],pairs[leg][0])
            v=source_value(parsed,[(pp[i][0],pp[i][1],ps[i]) for i in range(3)])
            this_idx &= s.simplify(v-base)==0
        idx_ok &= this_idx
        sp=pol_source(parsed,pairs,ps)
        Hs=[H(x) for x in pairs]
        eh=eh_gamma_gamma_cubic(Hs,ps)
        ratio=None
        if sp!=0 and eh!=0:
            ratio=s.factor(sp/eh); ratios.append(ratio)
        panel_rows.append({
          'pairs':[list(x) for x in pairs], 'momenta':[list(x) for x in ps],
          'source_component':str(base), 'source_polarization':str(sp),
          'eh_gamma_gamma_cubic':str(eh), 'ratio_source_over_eh':None if ratio is None else str(ratio),
          'all_leg_permutations_equal':bool(this_perm),'within_pair_symmetry':bool(this_idx),
        })
    enough_ratios=len(ratios)>=3
    ratio_const=bool(enough_ratios and all(s.simplify(r-ratios[0])==0 for r in ratios[1:]))
    ratio_nonzero=bool(ratios and ratios[0]!=0)
    checks={
      'A_pinned_git_blob_sha':bool(source_integrity),
      'B_parser_frozen_grammar_only':bool(syntax_ok),
      'C_exact_three_leg_labels':bool(exact_labels),
      'D_every_source_term_momentum_degree2':bool(degree_ok),
      'E_all_six_leg_permutations':bool(perm_ok),
      'F_each_graviton_index_pair_symmetric':bool(idx_ok),
      'G_at_least_three_nonzero_independent_ratios':bool(enough_ratios),
      'H_constant_nonzero_source_over_EH_ratio':bool(ratio_const and ratio_nonzero),
      'I_target_blind':True,
    }
    if not source_integrity or not syntax_ok:
        cls='BLOCKED_CUBIC_GRAVITON_SOURCE_INTEGRITY_OR_SYNTAX'
    elif all(checks.values()):
        cls='PASS_SCOPED_CUBIC_GRAVITON_S3_TENSOR_STRUCTURE_SOURCE_AUTHORITY_GLOBAL_PHASE_OPEN'
    else:
        cls='SCIENTIFIC_FAIL_CUBIC_GRAVITON_S3_SOURCE_STRUCTURE_MISMATCH'
    out={
      'gate':'ITER144_CUBIC_GRAVITON_S3_SOURCE_STRUCTURE_AUTHORITY',
      'classification':cls,
      'source':{'url':RAW_URL,'pinned_commit':PINNED_COMMIT,'expected_blob_sha':PINNED_BLOB,'observed_blob_sha':blob,'bytes':len(data),'term_count':len(parsed['terms'])},
      'parser_unknown_factors':parsed['unknown'],
      'momentum_degree_minmax':[min(degrees) if degrees else None,max(degrees) if degrees else None],
      'panels':panel_rows,
      'constant_source_over_EH_ratio':str(ratios[0]) if ratio_const else None,
      'checks':checks,
      'claim_ceiling':'S3 tensor structure source authority only; absolute Euclidean phase/sign normalization and all loop poles remain open; no B1/EDT/bridge/new physics/candidate theory',
    }
    with open('iter144_cubic_graviton_s3_source_structure_authority.json','w',encoding='utf-8') as f:
        json.dump(out,f,indent=2); f.write('\n')
    print(json.dumps({'classification':cls,'source_blob':blob,'term_count':len(parsed['terms']),'ratio':out['constant_source_over_EH_ratio'],'checks':checks},indent=2))
    if cls.startswith('SCIENTIFIC_FAIL') or cls.startswith('BLOCKED'): raise SystemExit(1)

if __name__=='__main__': main()
