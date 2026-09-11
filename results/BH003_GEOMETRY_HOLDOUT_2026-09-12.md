# BH-003 Geometry Holdout — Frozen-Regulator Transfer

Date: 2026-09-12  
Source matrix run: `34654332996`  
Recovered aggregate run: `34654522616`  
Status: `POSITIVE TRANSFER / CLAIM LOCKED`

## Test

Keep the causal-set SSEE double spectral prescription fixed:

`lambda_min_tilde = sqrt(N)/(4*pi)`

with no per-region retuning, while changing the target causal interval in null coordinates.

Holdout families:

- central square;
- central boosted interval;
- offset square;
- offset boosted interval.

Each family was evaluated at `N = 384, 768, 1152` with three independent sprinklings per size, for **36 jobs total**.

## Result

Raw SSEE remains strongly volume-like in every family (`R^2 >= 0.9984`).

After the frozen double spectral cutoff, fitted logarithmic slopes are:

| geometry | truncated log slope | R^2 |
|---|---:|---:|
| central square | 0.35995 | 0.9891 |
| central boosted | 0.38659 | 0.9259 |
| offset square | 0.36911 | 0.9678 |
| offset boosted | 0.35600 | 0.8238 |

Across shapes:

- mean slope: **0.36791**;
- standard deviation across shapes: **0.01179**;
- max-minus-min spread: **0.03059**;
- continuum/source comparison target: `1/3 = 0.33333`.

Thus the slope is substantially more stable under position/boost/shape changes than under the earlier finite-size side-ratio campaign.

## Interpretation

Within this 1+1D causal-set free-field realization, the frozen spectral rule exhibits nontrivial geometry transfer:

1. it does not require entropy retuning for translated causal intervals;
2. it does not require retuning under null-coordinate boosts/aspect changes;
3. it converts a robust raw volume law into an approximately continuum-like logarithmic law;
4. the fitted logarithmic coefficient remains narrowly clustered near the expected continuum value.

The lower `R^2` for the offset-boosted family is a warning that only three density points were used and finite-size/statistical structure remains visible.  The slope itself, however, stays inside the narrow cross-shape band.

## Claim lock

This supports **transferability of the source-defined cutoff rule**, not endogenous determination of that rule.  BH-003's strongest requirement — deriving the regulator from native causal/dynamical data without importing the source scale relation — remains open.
