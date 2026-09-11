# BH-003 Retained-Rank Flow Sweep

Date: 2026-09-12  
GitHub Actions run: `34657326695`  
Status: `SOURCE SQRT FLOW REPRODUCED / TRANSFER-OPTIMAL SQRT MECHANISM FAILS`

## Question

The source-defined BH-003 sector remains strongly aligned under Bernoulli thinning, and initial two-point diagnostics suggested that its retained rank might scale approximately as `sqrt(p)` under a thinning fraction `p`. This campaign tests whether that square-root mode-count flow is independently selected by subspace-transfer stability.

The sweep contains 48 jobs:

- `N = 384, 512, 768, 1024`;
- `p = 0.35, 0.45, 0.55, 0.65, 0.75, 0.85`;
- two independent seeds per `(N,p)`.

Two exponents are fitted separately.

1. **Source-rule rank flow**: use the known source spectral prescription on the thinned causal set.
2. **Transfer-optimal rank flow**: after fixing the parent source sector, choose the thinned spectral rank only by minimizing projector mismatch with the restricted parent subspace. No entropy and no thinned source cutoff enters this rank choice.

## Result

### Source-rule rank flow

Global fit:

`rank_thin / rank_parent ~ p^beta`

with

- `beta = 0.53710 ± 0.01072` (free intercept);
- unit-intercept exponent `beta = 0.54163`;
- `R^2 = 0.98199`;
- mean `(rank ratio)/sqrt(p) = 0.97725 ± 0.02306`.

The square-root-like source-rule mode-count flow is therefore reproduced very cleanly.

By parent size, free-intercept beta:

- `N=384`: `0.5733 ± 0.0190`;
- `N=512`: `0.5507 ± 0.0116`;
- `N=768`: `0.5209 ± 0.0164`;
- `N=1024`: `0.5173 ± 0.0144`.

### Transfer-optimal rank flow

The independent projector-matching criterion gives a qualitatively different result:

- `beta = 0.04443 ± 0.01236` (free intercept);
- unit-intercept exponent `beta = 0.04958`;
- `R^2 = 0.21918`;
- mean `(best transfer rank ratio)/sqrt(p) = 1.28761 ± 0.17783`.

By parent size, free-intercept beta remains close to zero:

- `N=384`: `0.0355 ± 0.0239`;
- `N=512`: `0.0702 ± 0.0351`;
- `N=768`: `0.0438 ± 0.0185`;
- `N=1024`: `0.0331 ± 0.0208`.

The transfer-optimal rank is therefore nearly parent-rank preserving across the tested thinning range, not square-root scaling.

## Subspace geometry

Despite the rank-flow disagreement, the source sector remains geometrically stable:

- mean source-sector overlap: **0.97822**;
- mean principal cosine: **0.98888**.

Thus the data support a separation between

1. a robustly transported **subspace direction**, and
2. the **source-defined number/measure of retained modes**.

## Scientific conclusion

The tempting explanation

> `sqrt(N)` mode count emerges because transfer stability itself chooses a `sqrt(p)` thinned rank

is **falsified** by this campaign.

The observed source-rule square-root rank flow is real but is not independently derived here, because the source cutoff already contains the relevant square-root scale. Projector-transfer stability alone selects almost no rank flow.

Therefore an endogenous derivation of the BH-003 regulator requires an additional physical condition beyond subspace covariance/overlap under Bernoulli thinning.

## Claim lock

This campaign does not falsify the source SSEE regulator or the observed stability of its retained subspace. It falsifies only the proposed independent mechanism that projector-transfer optimization by itself would recover the `sqrt(N)` retained-mode scaling.
