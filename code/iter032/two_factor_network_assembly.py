#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, pathlib, re, sys
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT/'out'/'iter032'
OUT.mkdir(parents=True, exist_ok=True)

# Reuse the validated numerical and exact-source machinery; do not re-fit conventions.
spec27 = importlib.util.spec_from_file_location('iter027_kernel', ROOT/'code/iter027/eq27_bounded_component_contraction.py')
k27 = importlib.util.module_from_spec(spec27); spec27.loader.exec_module(k27)
spec30 = importlib.util.spec_from_file_location('iter030_stage_s', ROOT/'code/iter030/corrected_stage_s.py')
k30 = importlib.util.module_from_spec(spec30); spec30.loader.exec_module(k30)

PRIMARY=(6,10,12)
HELDOUT=(7,9,11)
THRESH=5e-8
NULL_THRESH=1e-6
REQ=[
    ROOT/'prereg/ITER032_RC006_EQ27_TWO_FACTOR_NETWORK_ASSEMBLY_2026-09-14.md',
    ROOT/'results/ITER031_RC006_EQ27_BOUNDED_CONTRACTION_CORRECTED_STAGE_S_PASS_2026-09-14.md',
    ROOT/'results/ITER030_RC006_EQ27_CORRECTED_STAGE_S_PASS_2026-09-14.md',
]

def write(obj):
    p=OUT/'evidence.json'; p.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
    print(json.dumps(obj,indent=2,sort_keys=True))

def rows(level):
    return sorted(k27.admissible_rows(level))

def pairs(level):
    rs=rows(level)
    return [(rs[i],rs[(i+1)%len(rs)]) for i in range(len(rs))]

def single(row, level):
    a,b,c=row
    C,_=k27.ds.source_qC(a,b,c,level)
    D=k27.ds.d_source(a,b,c,level)
    F=C.T/np.sqrt(complex(k27.db.qdim(c,level)))
    sign=(-1)**int(round((a+b-c)/2))
    T=sign/k27.db.qdim(c,level)*np.eye(c+1,dtype=complex)
    M=F@D
    return M,T

def lane_authority():
    missing=[str(p.relative_to(ROOT)) for p in REQ if not p.exists()]
    src,err=k30.load_source()
    if err:
        return {**err,'lane':'source-factorization-authority','pass':False,'infrastructure_failure':True,'missing_prerequisites':missing}
    d=src['display']
    # Use the same bracket definition as ITER030, but retain spans to test distinct/non-nested source factors.
    pat=re.compile(r'\\left\[\s*\\sum.*?\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\s*\\right\]',re.S)
    ms=list(pat.finditer(d))
    sums=len(re.findall(r'\\sum\b|\\sum_',d))
    distinct=(len(ms)==2 and ms[0].end()<=ms[1].start())
    # Source-level multiplicative separation: after the first closing bracket and before the second opening bracket,
    # there is no equality/comma/plus operator that would turn them into alternatives/terms. Whitespace or TeX spacing is allowed.
    separator=d[ms[0].end():ms[1].start()] if len(ms)==2 else ''
    sep_clean=re.sub(r'\\(?:,|;|!|quad|qquad)','',separator)
    multiplicative=bool(len(ms)==2 and not re.search(r'[=,+]',sep_clean))
    forbidden_exec=[]  # this implementation imports no Eq.(29)/Lambda numerical object.
    ok=(not missing and len(ms)==2 and sums==2 and distinct and multiplicative and not forbidden_exec)
    cls='PASS' if ok else 'BLOCKED_TWO_FACTOR_SOURCE_FACTORIZATION'
    return {'lane':'source-factorization-authority','pass':bool(ok),'classification':cls,
            'archive_sha':src['archive_sha'],'eq_sha':src['eq_sha'],'missing_prerequisites':missing,
            'bracketed_factors':len(ms),'sum_structures':sums,'distinct_non_nested':distinct,
            'separator_repr':repr(separator),'multiplicative_syntax':multiplicative,
            'forbidden_executable_dependencies':forbidden_exec}

def lane_factors():
    out=[]
    mx=0.0
    for held,levels in ((False,PRIMARY),(True,HELDOUT)):
        for level in levels:
            for r1,r2 in pairs(level):
                for pos,r in ((1,r1),(2,r2)):
                    M,T=single(r,level)
                    res=float(np.max(np.abs(M-T)))
                    finite=bool(np.all(np.isfinite(M)) and np.all(np.isfinite(T)) and np.isfinite(res))
                    mx=max(mx,res)
                    out.append({'heldout':held,'k':level,'factor_position':pos,'row':list(r),'residual':res,'finite':finite})
    ok=all(x['finite'] for x in out) and mx<THRESH
    return {'lane':'independent-factor-reconstruction','pass':bool(ok),'max_single_factor_residual':mx,
            'threshold':THRESH,'retuned_heldout':False,'rows':out}

def lane_assembly():
    out=[]; mx=0.0
    for held,levels in ((False,PRIMARY),(True,HELDOUT)):
        for level in levels:
            for r1,r2 in pairs(level):
                M1,T1=single(r1,level); M2,T2=single(r2,level)
                N=np.kron(M1,M2); target=np.kron(T1,T2)
                res=float(np.max(np.abs(N-target)))
                finite=bool(np.all(np.isfinite(N)) and np.all(np.isfinite(target)) and np.isfinite(res))
                mx=max(mx,res)
                out.append({'heldout':held,'k':level,'row1':list(r1),'row2':list(r2),'shape':list(N.shape),'residual':res,'finite':finite})
    ok=all(x['finite'] for x in out) and mx<THRESH
    return {'lane':'two-factor-assembly','pass':bool(ok),'max_two_factor_residual':mx,'threshold':THRESH,
            'retuned_heldout':False,'full_eq27_amplitude_claimed':False,'rows':out}

def lane_nulls():
    level=12
    ps=pairs(level)
    r1,r2=ps[0]
    # For the qdim-null, preregistered deterministic advance to first unequal output channel if necessary.
    unequal_idx=0
    if r1[2]==r2[2]:
        for i,(a,b) in enumerate(ps):
            if a[2]!=b[2]: unequal_idx=i; r1,r2=a,b; break
    M1,T1=single(r1,level); M2,T2=single(r2,level)
    good=np.kron(M1,M2)
    target=np.kron(T1,T2)
    good_res=float(np.max(np.abs(good-target)))

    wrong_sign=np.kron(T1,-T2)
    sign_res=float(np.max(np.abs(good-wrong_sign)))

    a2,b2,c2=r2; c1=r1[2]
    sign2=(-1)**int(round((a2+b2-c2)/2))
    wrong_qdim_T2=sign2/k27.db.qdim(c1,level)*np.eye(c2+1,dtype=complex)
    qdim_res=float(np.max(np.abs(good-np.kron(T1,wrong_qdim_T2))))

    collapse_T2=np.eye(c2+1,dtype=complex)
    collapse_res=float(np.max(np.abs(good-np.kron(T1,collapse_T2))))
    vals={'flip_second_target_sign':sign_res,'second_uses_first_qdim':qdim_res,'collapse_second_to_identity':collapse_res}
    detected=sum((np.isfinite(v) and v>NULL_THRESH) or not np.isfinite(v) for v in vals.values())
    ok=(good_res<THRESH and detected>=2)
    return {'lane':'null-controls','pass':bool(ok),'k':level,'pair_index':unequal_idx,'row1':list(r1),'row2':list(r2),
            'good_residual':good_res,'wrong_residuals':vals,'detected':int(detected),'required':2,
            'null_threshold':NULL_THRESH,'assembly_threshold':THRESH}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['authority','factors','assembly','nulls']); a=ap.parse_args()
    try:
        obj={'authority':lane_authority,'factors':lane_factors,'assembly':lane_assembly,'nulls':lane_nulls}[a.lane]()
    except Exception as e:
        obj={'lane':a.lane,'pass':False,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e)}
    write(obj)

if __name__=='__main__': main()
