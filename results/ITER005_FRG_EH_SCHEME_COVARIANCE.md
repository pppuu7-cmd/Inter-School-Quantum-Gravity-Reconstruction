# ITERATION 005 — Einstein–Hilbert FRG Scheme-Covariance Stress

Date: 2026-09-12  
GitHub Actions run: `34665907393`  
Status: `SUCCESS / COVARIANCE STRESS PASSED / NO RM-001 IDENTIFICATION`

## Scope

Two standard d=4 Einstein–Hilbert truncation beta-function realizations were implemented in the same dimensionless `(g,lambda)` coordinates:

1. optimized/Litim threshold functions;
2. a sharp-cutoff analytic flow.

This is a truncation/regulator comparison, not a test of a full asymptotic-safety theory.

## Results

### Optimized/Litim

- `g_* = 0.70732088`;
- `lambda_* = 0.19320051`;
- `g_* lambda_* = 0.13665475`;
- critical exponents: `theta = 1.47530 ± 3.04321 i`.

### Sharp cutoff

- `g_* = 0.40266099`;
- `lambda_* = 0.32968121`;
- `g_* lambda_* = 0.13274976`;
- critical exponents: `theta = 1.94091 ± 3.31065 i`.

### Cross-scheme comparison

- both flows possess a positive non-Gaussian fixed point below the `lambda=1/2` singular wall;
- both have positive real parts of the two critical exponents in this truncation;
- relative spread of `g_* lambda_*`: `0.02899` (~`2.9%`);
- angle between the dominant right-singular directions of the local Jacobian in the shared `(g,lambda)` coordinates: `1.8384 degrees`.

## Interpretation

Raw fixed-point coordinates are visibly scheme dependent, while some composite/local-flow structure is substantially more stable in this two-scheme stress test.

For ISQGR this is primarily a warning about representation/covariance:

- one must not identify a coordinate direction in coupling space with a fundamental transported physical subspace merely because it is numerically stable in one truncation;
- robust bridge statements should be formulated in terms of quantities whose transformation under reparameterization/regulator changes is explicitly controlled.

The small angle observed here is therefore a useful stability datum, not evidence that the FRG critical direction is the same object as RM-001 retained-sector orientation.

## Claim lock

This calculation does not prove asymptotic safety, does not establish truncation convergence, and does not identify an FRG eigendirection with the ISQGR projector/transport object.
