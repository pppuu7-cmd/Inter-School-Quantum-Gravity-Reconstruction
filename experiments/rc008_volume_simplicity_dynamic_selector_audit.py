#!/usr/bin/env python3
"""RC-008 asymptotic hypercuboid amplitude: volume-simplicity selector audit.

Purpose
-------
Test a narrow BH-004B question without fitting to the answer: does the
published large-j quantum-hypercuboid *dressed vertex amplitude itself*
prefer the volume-simple/geometric submanifold, or must volume simplicity
remain an independent physical selector?

This is NOT a coarse/refined 16-hypercuboid reproduction. It is a local
amplitude-level diagnostic using the published asymptotic determinant and
hypercuboid boundary incidence.

Source equations used:
- det H polynomial for the hypercuboid stationary point (degree 21),
- B_v proportional to 1/sqrt(-det H) + complex conjugate,
- face weight j_f^(2 alpha),
- cuboid edge-norm factor (ja+jb)(ja+jc)(jb+jc),
- volume simplicity j1*j6 = j2*j5 = j3*j4.

The overall normalization is irrelevant because only log-amplitude ratios
between equal-scale configurations are compared.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
import random
import statistics
from pathlib import Path

ALPHAS = [0.45, 0.55, 0.63, 0.67, 0.75]
EPSILONS = [0.15, 0.30, 0.45, 0.60]
N_BASE = 256
PERTURBATIONS_PER_EPS = 4
PERMUTATIONS = 200
SEED = 260912008


def det_h(j):
    j1, j2, j3, j4, j5, j6 = j
    z = 1.0 + 1.0j
    f1 = j1*j1*(j2+j4) + j2*j4*(j2+j4) + j1*(j2*j2 + z*j2*j4 + j4*j4)
    f2 = j1*j1*(j3+j5) + j3*j5*(j3+j5) + j1*(j3*j3 + z*j3*j5 + j5*j5)
    f3 = j3*j4*j5 + j2*(j4*j5 + j3*(j4+j5))
    f4 = j2*j2*(j3+j6) + j3*j6*(j3+j6) + j2*(j3*j3 + z*j3*j6 + j6*j6)
    f5 = j4*j4*(j5+j6) + j5*j6*(j5+j6) + j4*(j5*j5 + z*j5*j6 + j6*j6)
    f6 = j3*j4*j6 + j1*(j4*j6 + j3*(j4+j6))
    f7 = j2*j5*j6 + j1*(j5*j6 + j2*(j5+j6))
    return 2.0 * f1*f2*f3*f4*f5*f6*f7


def edge_norm_factor(a, b, c):
    return (a+b)*(a+c)*(b+c)


def log_dressed_amplitude(j, alpha):
    if min(j) <= 0:
        return float('-inf')
    d = det_h(j)
    root = cmath.sqrt(-d)
    if abs(root) == 0:
        return float('-inf')
    b = 1.0/root + (1.0/root).conjugate()
    b2 = abs(b)**2
    if not math.isfinite(b2) or b2 <= 0:
        return float('-inf')

    # Four distinct cuboid boundary-edge types of a 4D hypercuboid.
    j1,j2,j3,j4,j5,j6 = j
    e = (
        edge_norm_factor(j1,j2,j3) *
        edge_norm_factor(j1,j4,j5) *
        edge_norm_factor(j2,j4,j6) *
        edge_norm_factor(j3,j5,j6)
    )
    return 2.0*alpha*sum(math.log(x) for x in j) + math.log(e) + math.log(b2)


def geometric_spins(rng):
    # Coordinate-plane areas A12,A13,A14,A23,A24,A34 from four edge lengths.
    ls = [math.exp(rng.uniform(-0.8, 0.8)) for _ in range(4)]
    l1,l2,l3,l4 = ls
    return [l1*l2, l1*l3, l1*l4, l2*l3, l2*l4, l3*l4]


def volume_simplicity_residual(j):
    p = [j[0]*j[5], j[1]*j[4], j[2]*j[3]]
    lp = [math.log(x) for x in p]
    m = sum(lp)/3.0
    return math.sqrt(sum((x-m)**2 for x in lp)/3.0)


def perturb_equal_scale(j, epsilon, rng):
    q = [rng.gauss(0.0, 1.0) for _ in range(6)]
    qm = sum(q)/6.0
    q = [x-qm for x in q]  # preserve geometric mean of six spins exactly.
    n = math.sqrt(sum(x*x for x in q))
    if n == 0:
        q[0], q[1] = 1.0, -1.0
        n = math.sqrt(2.0)
    q = [x/n for x in q]
    return [x*math.exp(epsilon*d) for x,d in zip(j,q)]


def ranks(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0]*len(xs)
    i = 0
    while i < len(order):
        k = i+1
        while k < len(order) and xs[order[k]] == xs[order[i]]:
            k += 1
        avg = 0.5*((i+1)+k)
        for t in range(i,k):
            r[order[t]] = avg
        i = k
    return r


def pearson(x,y):
    mx,my = statistics.fmean(x),statistics.fmean(y)
    dx=[a-mx for a in x]; dy=[b-my for b in y]
    den=math.sqrt(sum(a*a for a in dx)*sum(b*b for b in dy))
    return 0.0 if den == 0 else sum(a*b for a,b in zip(dx,dy))/den


def spearman(x,y):
    return pearson(ranks(x),ranks(y))


def qtile(xs,q):
    ys=sorted(xs)
    p=(len(ys)-1)*q
    lo=int(math.floor(p)); hi=int(math.ceil(p))
    if lo==hi: return ys[lo]
    f=p-lo
    return ys[lo]*(1-f)+ys[hi]*f


def homogeneity_audit():
    rng=random.Random(SEED+1)
    rows=[]
    for alpha in ALPHAS:
        errs=[]
        target=12.0*alpha-9.0
        for _ in range(64):
            j=geometric_spins(rng)
            lam=math.exp(rng.uniform(-1.0,1.0))
            a=log_dressed_amplitude(j,alpha)
            b=log_dressed_amplitude([lam*x for x in j],alpha)
            observed=(b-a)/math.log(lam) if abs(math.log(lam))>1e-10 else target
            errs.append(abs(observed-target))
        rows.append({'alpha':alpha,'target_degree':target,'max_abs_degree_error':max(errs)})
    return rows


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    rng=random.Random(SEED)

    hom=homogeneity_audit()
    hom_pass=all(r['max_abs_degree_error'] <= 2e-9 for r in hom)

    by_alpha=[]
    all_rows={a:[] for a in ALPHAS}
    invalid=0
    base_residuals=[]
    for _ in range(N_BASE):
        base=geometric_spins(rng)
        base_residuals.append(volume_simplicity_residual(base))
        base_logs={a:log_dressed_amplitude(base,a) for a in ALPHAS}
        for eps in EPSILONS:
            for _ in range(PERTURBATIONS_PER_EPS):
                jp=perturb_equal_scale(base,eps,rng)
                res=volume_simplicity_residual(jp)
                for a in ALPHAS:
                    lp=log_dressed_amplitude(jp,a)
                    if not (math.isfinite(lp) and math.isfinite(base_logs[a])):
                        invalid += 1
                        continue
                    all_rows[a].append((res, lp-base_logs[a], eps))

    for a in ALPHAS:
        rows=all_rows[a]
        residual=[r[0] for r in rows]
        delta=[r[1] for r in rows]
        rho=spearman(residual,delta)
        frac=sum(x<0 for x in delta)/len(delta)
        med=statistics.median(delta)
        # deterministic permutation null for correlation only
        null=[]
        prng=random.Random(SEED + int(round(a*10000)))
        for _ in range(PERMUTATIONS):
            rr=residual[:]
            prng.shuffle(rr)
            null.append(spearman(rr,delta))
        p_lower=(1+sum(x<=rho for x in null))/(1+len(null))
        by_eps=[]
        for eps in EPSILONS:
            ds=[d for r,d,e in rows if e==eps]
            by_eps.append({'epsilon':eps,'n':len(ds),'fraction_perturbed_lower_amplitude':sum(x<0 for x in ds)/len(ds),'median_log_amplitude_delta':statistics.median(ds)})
        dynamic=bool(frac>=0.75 and rho<=-0.20 and p_lower<=0.05)
        by_alpha.append({
            'alpha':a,'n':len(rows),
            'fraction_perturbed_lower_amplitude':frac,
            'median_log_amplitude_delta':med,
            'spearman_residual_vs_logamp_delta':rho,
            'permutation_lower_tail_p':p_lower,
            'dynamic_selector_lane_pass':dynamic,
            'by_epsilon':by_eps,
        })

    lanes=sum(r['dynamic_selector_lane_pass'] for r in by_alpha)
    natural=bool(hom_pass and lanes>=3)
    strong=bool(hom_pass and lanes>=4)
    out={
      'test':'RC008_VOLUME_SIMPLICITY_DYNAMIC_SELECTOR_AUDIT',
      'status':'PASS_EXECUTION',
      'seed':SEED,
      'n_base':N_BASE,
      'perturbations_per_epsilon':PERTURBATIONS_PER_EPS,
      'epsilons':EPSILONS,
      'alphas':ALPHAS,
      'base_volume_simplicity_residual_max':max(base_residuals),
      'invalid_amplitude_evaluations':invalid,
      'homogeneity_audit':hom,
      'homogeneity_pass':hom_pass,
      'preregistered_gate':{
        'lane_pass':'fraction perturbed lower amplitude >=0.75 AND Spearman(residual, delta log amplitude)<=-0.20 AND permutation lower-tail p<=0.05',
        'natural_dynamic_selector_support':'homogeneity sanity passes and >=3/5 alpha lanes pass',
        'strong_dynamic_selector_support':'homogeneity sanity passes and >=4/5 alpha lanes pass',
      },
      'dynamic_selector_lanes_passed':lanes,
      'natural_dynamic_selector_support':natural,
      'strong_dynamic_selector_support':strong,
      'by_alpha':by_alpha,
      'interpretation_lock':'Positive result means the local asymptotic dressed hypercuboid amplitude statistically favors the volume-simple submanifold under equal-scale perturbations. Negative result means volume simplicity remains an independent source-native selector in this diagnostic. Neither outcome is a full coarse/refined RC-008 reproduction.',
    }
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
