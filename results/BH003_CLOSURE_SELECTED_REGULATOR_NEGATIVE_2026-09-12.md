# BH-003 Closure-Selected Regulator — Negative Result

Date: 2026-09-12  
Successful GitHub Actions run: `34654886088`  
Status: `NEGATIVE / INFORMATIVE FALSIFICATION`

## Pre-registered idea

Choose the spectral regulator without entropy by balancing compression against native causal-propagator closure.

For nested `iDelta` spectral sectors, scan a fixed retained-fraction grid and measure

`leakage = ||(I-P) G_R P||_F / ||G_R P||_F`,

with `G_R=C/2`.

Select the maximum-curvature corner of the `log(retained fraction)` versus `log(leakage)` L-curve.  Only after the corner is frozen, compute SSEE and compare the selected cutoff with the source-defined `sqrt(N)/(4*pi)` scale.

No entropy value and no source cutoff enters the selection rule.

## Campaign

- `N = 512, 768, 1024, 1280`;
- four independent sprinklings per size;
- 16 successful matrix jobs;
- the first run failed before science because NumPy 2.5 removed 2D `np.cross`; the mathematically identical scalar determinant was substituted, with no change to the selection criterion;
- rerun `34654886088`: 16/16 jobs + aggregate successful.

## Result

The closure L-curve identifies sectors with low causal leakage and return defect, but it does **not** identify the physical SSEE regulator.

Across all 16 realizations:

- mean parent selected/source cutoff ratio: **0.1422 ± 0.0502**;
- mean subregion selected/source cutoff ratio: **0.6554 ± 0.9467**;
- parent selected retained fraction is typically about **0.62–0.67**;
- parent one-step leakage is about **0.19–0.20**;
- parent two-step sequential return defect is only about **0.047–0.054**.

Despite this strong closure, the post-selection entropy does not show stable continuum-like logarithmic scaling:

`S_selected = 15.376 * log(sqrt(N_sub)/(4*pi)) + 10.675`,

with only `R^2 = 0.4545`.

The group means are also non-monotonic:

- `N=512`: `S_selected ≈ 9.04`;
- `N=768`: `≈ 13.43`;
- `N=1024`: `≈ 9.57` with very large realization spread;
- `N=1280`: `≈ 18.61`.

Raw entropy continues to be almost perfectly volume-like:

`S_raw ≈ 0.31861 N_sub - 2.632`, `R^2 = 0.99867`.

## Scientific consequence

The proposition

> "the physically relevant SSEE regulator is the compression/closure L-curve corner"

is rejected for this pre-registered rule.

This separates two facts that had previously been easy to conflate:

1. the source-defined BH-003 spectral sector is unusually closed under `G_R` compared with random rank-matched subspaces;
2. closure quality alone is insufficient to determine **where** the physical spectral cutoff must lie.

Thus closure is a useful structural property but not, by itself, a regulator-selection principle.

## Next non-circular test

The next endogenous criterion must add genuinely new operator information rather than another shape statistic of one spectrum.  The highest-priority test is **causal-set thinning transfer**:

- randomly thin one sprinkling;
- compare the restricted full-set spectral projector with projectors of the induced thinned causal set;
- infer the cutoff flow solely from projector-transfer stability;
- only after fitting the scale flow compare its exponent with the source `N^(1/2)` behavior and evaluate entropy.

No target entropy coefficient is permitted in this inference.
