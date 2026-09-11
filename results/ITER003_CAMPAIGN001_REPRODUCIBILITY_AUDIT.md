# Iter003 Result — Campaign 001 Reproducibility Audit

Status: `REPRODUCED_EXECUTABLE`  
Date: 2026-09-12

## Runs compared

- Run `34652279466` — first campaign; numerical matrices/aggregate succeeded, workflow status failed only because of a unittest invocation-path error.
- Run `34652499160` — corrected workflow; full workflow concluded `success`.

Both runs used the same declared scenario/seed matrices.

## Reproduction result

All qualitative classifications reproduced exactly:

- clean: 3 `FIT_COMPATIBLE`, 1 `FIT_TENSION`;
- noise: 3 `FIT_COMPATIBLE`, 1 `FIT_TENSION`;
- QES-like nuisance: 4 `FIT_COMPATIBLE`;
- anisotropic contamination: 4 `FIT_INCOMPATIBLE`;
- wrong conformal class: 4 `FIT_INCOMPATIBLE`.

The scale/composition Monte Carlo reproduced the same aggregate random-mixing mean defect to displayed precision:

`0.597365154386256`.

Mean leakage/defect correlation differed only at floating rounding:

- first run: `0.4731249781201378`;
- corrected run: `0.4731249781201379`.

Subspace-preserving mean defects remained at floating-point zero scale:

- first run: `1.7322204827571536e-16`;
- corrected run: `1.7338658364044513e-16`.

Finite-surface mean values changed only at tiny solver floating-point levels (typically around 1e-10 or smaller in reported RMSE values); scenario verdicts were unchanged.

## Interpretation

Campaign 001 therefore passes the current deterministic-seed reproducibility requirement at the level relevant to its scientific conclusions.

The tiny differences are numerical-solver/floating-point effects and do not change any classification.

## Remaining reproducibility hardening

For publication-grade packaging later:

1. pin exact Python/numpy/scipy versions;
2. record runner image and dependency lock file;
3. store per-seed outputs in a deterministic release bundle;
4. define tolerance-based hash-equivalence for floating numerical results rather than requiring byte identity from solver outputs.

## Claim lock

Reproducibility of a synthetic benchmark establishes reproducibility of that benchmark only, not physical validity of CEMR or BH-001.