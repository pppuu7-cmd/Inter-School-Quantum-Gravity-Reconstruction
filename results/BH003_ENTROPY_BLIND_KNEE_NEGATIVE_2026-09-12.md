# BH-003 Entropy-Blind Spectral Knee — Negative Result

Date: 2026-09-12  
Source matrix run: `34654299290`  
Recovered aggregate run: `34654522616`  
Status: `NEGATIVE / INFORMATIVE FALSIFICATION`

## Pre-registered question

Can a simple entropy-blind spectral-knee detector infer the physically useful causal-set SSEE truncation scale directly from the spectrum of `iDelta`, without using:

- entropy values;
- the target continuum entropy coefficient;
- the source formula `sqrt(N)/(4*pi)` to select the break?

The tested rule fits two lines in `log(rank)`–`log(lambda)` space and selects the minimum-SSE break after fixed endpoint trimming.  The rule is applied independently to the parent and restricted spectra.

## Campaign

- `N = 512, 768, 1024, 1280`;
- four independent seeds per size;
- 16 jobs total;
- every matrix job completed successfully;
- the original workflow failure was only an aggregation-environment error and was recovered without recomputing the matrices.

## Result

The operator-only knee is very statistically visible but occurs at the wrong physical scale.

Across all runs:

- mean blind/source parent-cutoff ratio: **0.11999 ± 0.02237**;
- mean blind/source subregion-cutoff ratio: **0.19887 ± 0.02917**;
- parent two-line spectral SSE improvement: about **0.91**;
- subregion two-line spectral SSE improvement: about **0.89–0.91**.

So a strong mathematical break exists, but it is substantially deeper in the small-eigenvalue sector than the source-defined SSEE regulator.

Consequently, blind-truncated entropy still grows very rapidly:

- `N=512`: mean `S_blind = 13.71`;
- `N=768`: mean `S_blind = 19.57`;
- `N=1024`: mean `S_blind = 25.45`;
- `N=1280`: mean `S_blind = 31.74`.

A formal fit against the logarithmic size proxy has `R^2 = 0.9837` but slope **41.43**.  This high `R^2` must not be misread as continuum-like logarithmic scaling: over the tested range the entropy magnitude retains the wrong, near-volume-law growth.

For comparison, raw entropy continues to show the expected volume behavior:

`S_raw ~= 0.2970 N_sub - 0.844`, `R^2 = 0.99867`.

## Scientific consequence

The naive statement

> "the visible spectral knee of iDelta determines the physical entanglement cutoff"

is **rejected for this knee definition**.

This strengthens BH-003 methodologically because it prevents circular promotion of any visually prominent spectral crossover.  The physical regulator needs an additional native criterion beyond two-line spectral shape alone.

## Next admissible tests

Future entropy-blind regulator rules must be chosen from independent operator/dynamical criteria before looking at target entropy.  High-priority candidates are:

1. a closure/compression L-curve based on `P G_R (I-P) G_R P`;
2. stability of retained observables under causal-set thinning;
3. a scale-flow/fixed-point criterion for the spectral sector;
4. a source-derived causal-density-to-resolution map tested on unseen geometries.

No threshold may be tuned to improve the entropy coefficient on the same evaluation data.
