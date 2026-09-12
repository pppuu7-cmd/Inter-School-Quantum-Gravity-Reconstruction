# ITER006 — RC-009 source-phase endpoint audit

Date: 2026-09-12

GitHub Actions run: `34671649669`

## Question

The preceding endpoint-power audit found severe algebraic divergence in the reduced isotemporal RC-009 positive-measure realization.  The principal remaining source-internal escape route was conditional convergence from the frozen oscillatory branch

`cos(S_R/G + arg D) + cos(gamma S_R/G - Lambda V4/G)`.

This audit asks whether those source phases become increasingly oscillatory toward the singular endpoint or instead freeze to finite limits while the branch remains nonzero.

## Parallel campaign

Nine preregistered lanes were executed:

- coarse endpoint;
- simultaneous fine diagonal;
- seven fine-edge anchors: `0.05, 0.10, 0.20, 0.50, 1.00, 2.00, 4.00`.

All 9 lanes and aggregate completed successfully.

## Result

Aggregate classification:

`ALL_NINE_SOURCE_BRANCH_OSCILLATORY_ESCAPES_EXCLUDED_SCOPED = TRUE`.

Across every lane:

1. both source phase arguments show shrinking total variation toward the endpoint;
2. the combined branch is bounded away from zero on the terminal samples;
3. the combined branch sign is stable;
4. therefore the frozen RC-009 source oscillation does not become fast enough to conditionally regularize the previously measured algebraic endpoint singularity.

Representative coarse terminal variations:

- phase 1 total variation: `2.568476e-4 rad`;
- phase 2 total variation: `1.222066e-4 rad`;
- minimum terminal branch magnitude: `1.373953`.

For the simultaneous fine diagonal, the middle `(t,t)` block is even more strongly frozen:

- phase 1 terminal variation: `1.258692e-5 rad`;
- phase 2 terminal variation: approximately `2.44e-14 rad`;
- minimum branch magnitude: `0.0100506`.

## Scientific consequence

The reduced isotemporal RC-009 branch is now blocked more strongly than after the absolute-value audit alone:

`RC009_REDUCED_ISOTEMPORAL_SOURCE_BRANCH_ENDPOINT_DIVERGENCE_NOT_RESCUED_BY_ITS_FROZEN_OSCILLATORY_FACTOR`.

This removes the specific conditional-convergence escape route supplied by the branch already present in the frozen RC-009 realization.

## Claim lock

This is **not** a no-go theorem for Lorentzian EPRL/spinfoams.  It does not exclude:

- a different source-defined contour or measure;
- cancellations involving degrees of freedom removed by the isotemporal reduction;
- a genuinely complex full amplitude with additional phase structure;
- full multi-vertex spin-foam refinement/cylindrical consistency.

The correct programme response is therefore to stop investing in denser quadrature of this particular reduced positive/isotemporal bridge and redirect effort toward a genuine source-defined amplitude/refinement realization.
