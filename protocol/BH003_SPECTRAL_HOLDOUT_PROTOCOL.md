# BH-003 Spectral Holdout Protocol v0.1

Status: `ACTIVE / ITERATION_004`  
Date: 2026-09-12

## Objective

Test whether the spectral coarse graining used in causal-set spacetime entanglement can be fixed independently of the target entropy law and transferred across unseen causal-set regions/backgrounds.

The protocol is designed to separate three statements:

1. a cutoff can be tuned to reproduce a continuum area/log law;
2. a cutoff can be predicted from independent causal/spectral data;
3. the predicted cutoff transfers to new geometries without retuning.

Only (2)+(3) are admissible evidence for BH-003.

## Source anchor

For the 1+1D nested-diamond construction, the source relates the causal-set Pauli–Jordan spectrum to the continuum spectrum by a density factor and identifies a retained-eigenvalue threshold

`lambda_min^cs ~ sqrt(N)/(4 pi)`.

The argument uses the causal-set discreteness length together with the continuum wavelength/eigenvalue relation. The source also reports a visible break in the causal-set spectrum near the same region and suggests that this spectral feature could guide truncation.

This is stronger than arbitrary entropy fitting, but the density rule still imports continuum spectral information. ISQGR therefore distinguishes a continuum-calibrated rule from a purely spectrum-internal rule.

## Competing rules

### R0 — no extra spectral truncation

Use the full non-null Pauli–Jordan spectrum.

Purpose: preserve the raw causal-set prediction as a negative/alternative control.

### RG — density/geometric rule

Use

`lambda_min = sqrt(N)/(4 pi)`

in the declared 1+1D normalization.

This rule is frozen before examining holdout-region entropy. It is source-grounded but partially continuum-calibrated.

### RK — spectrum-internal break rule

Infer a spectral break/knee from the **global Pauli–Jordan spectrum only**, without using target-region entropy values or target scaling.

Candidate estimator:

1. sort the positive `iDelta` eigenvalues by magnitude;
2. work in log-rank/log-eigenvalue space;
3. fit a two-regime spectral model over a predeclared admissible interior range;
4. choose the break minimizing the declared information criterion or cross-validated spectral residual;
5. freeze all fitting choices using training spectra only.

RK remains `METHOD_CANDIDATE` until its estimator is validated against synthetic controls and source spectra.

## Training / validation separation

### Training may use

- global causal-set spectra;
- element count / sprinkling density;
- parent-region causal relations;
- known matrix normalization;
- synthetic spectra for algorithm calibration.

### Training must not use

- target subregion SSEE values;
- area/log-law fit residuals on the evaluation regions;
- per-region retuning after seeing entropy scaling;
- desired continuum coefficient as an optimization target.

## Holdout hierarchy

H1 — new random sprinklings at the same parent geometry.  
H2 — new parent densities/sizes.  
H3 — different nested-region size ratios.  
H4 — displaced/shape-varied subregions where a controlled comparator exists.  
H5 — a different background such as the source-defined de Sitter setup, with all normalization changes declared before evaluation.

A rule failing at an earlier level is not promoted to later levels by retuning.

## Required outputs

For each rule R0/RG/RK and holdout level:

- retained spectral rank;
- entropy and uncertainty across sprinklings;
- scaling model evidence rather than only a preferred fit;
- stability of the inferred threshold under random realization changes;
- covariance between threshold uncertainty and entropy uncertainty;
- deviation from independently known continuum behavior where such a comparator exists;
- explicit record of whether continuum matching entered the rule construction.

## Primary anti-overfitting statistic

Define a threshold-transfer ratio

`T_lambda = lambda_holdout_pred / lambda_holdout_ref`,

where `lambda_holdout_ref` is a reference determined without using the holdout entropy target. Depending on the test this can be a source-grounded density rule or independently estimated spectral break.

Entropy scaling is evaluated **after** `T_lambda` is frozen.

## Bridge success criterion

BH-003 is strengthened only if a regulator rule derived independently from causal/spectral data:

1. transfers across at least H1–H3 without region-specific retuning;
2. gives stable retained rank scaling;
3. reproduces controlled continuum entanglement behavior in the regime where that behavior is independently expected;
4. preserves or explains deviations outside that regime rather than forcing the target law;
5. supplies a scale/composition interpretation compatible with BH-001.

## Strong falsification outcomes

The strong form of BH-003 fails if:

- only entropy-target tuning selects the successful threshold;
- threshold rules vary arbitrarily with region shape/position;
- spectrum-internal breaks are unstable under sprinkling noise;
- RG transfers but only because continuum information has already fixed the answer and no causal-set-native information remains;
- raw volume-law behavior survives every independently motivated spectral/coarse-graining prescription.

The last outcome would be scientifically significant and would shift the programme toward genuine nonlocal UV entanglement rather than continuum restoration.

## Current executable

`experiments/causal_set_ssee_2d_reproduction.py`

implements the first H1/H2 reproduction front for R0 and RG. RK is deliberately not enabled until the spectral-break estimator itself passes a separate validation test.

## Claim lock

This protocol tests regulator provenance and transfer. It does not assume that continuum area-law entropy is fundamentally correct at the causal-set discreteness scale.