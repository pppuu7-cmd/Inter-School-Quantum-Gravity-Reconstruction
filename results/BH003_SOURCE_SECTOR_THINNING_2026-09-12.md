# BH-003 Source-Sector Thinning Diagnostic

Date: 2026-09-12  
GitHub Actions run: `34655808210`  
Status: `POSITIVE SUBSPACE TRANSFER / SCALE-FLOW MISMATCH`

## Question

The corrected thinning-transfer campaign found an entropy-blind exponent near one rather than the source SSEE regulator scaling near one-half. This diagnostic asks a narrower question: does Bernoulli thinning destroy the physically sourced BH-003 spectral sector itself, or does it mostly preserve the subspace while changing its effective scale/rank?

The source sector is fixed by the previously reproduced causal-set SSEE prescription. No entropy is used and no new cutoff is inferred.

## Result

Across 24 jobs:

- mean source-sector overlap fraction: **0.976132**;
- mean principal cosine: **0.987801**;
- mean source projector distance: **0.393425**;
- mean best achievable rank-matched projector distance: **0.298662**;
- source/best projector-distance ratio: **1.31559**;
- mean thinned/source retained-rank ratio: **0.760993**.

By thinning fraction:

| thinning `p` | source overlap | principal cosine | source projector distance | best distance | source/best | retained-rank ratio |
|---:|---:|---:|---:|---:|---:|---:|
| 0.5 | 0.974675 | 0.987067 | 0.449159 | 0.334331 | 1.34426 | 0.693493 |
| 0.7 | 0.977590 | 0.988536 | 0.337692 | 0.262993 | 1.28691 | 0.828494 |

## Interpretation

Bernoulli thinning does **not** erase the source-defined physical sector. The retained source subspace remains strongly aligned with the corresponding sector on the thinned causal set: the average principal cosine is about 0.988 and overlap is about 97.6%.

However, the rank/scale does not transfer trivially. The thinned sector contains only about 69% of the source retained rank for `p=0.5` and about 83% for `p=0.7`; its projector distance remains systematically larger than the best rank-matched transfer.

This resolves the apparent tension with the corrected thinning-projector exponent near one: thinning appears to preserve the **direction/geometry of the physical subspace** much better than it preserves the source regulator's **scale or measure**.

## Consequence for ISQGR

The next endogenous-regulator search should not treat coarse graining as a scalar eigenvalue-flow problem alone. A more promising object is a pair

`(retained subspace, induced measure/scale flow)`

with the subspace constrained by transfer stability and the scale fixed by an additional physical condition.

## Claim lock

This is a semantic diagnostic of a source-defined causal-set spectral sector under Bernoulli thinning. It is not a derivation of the SSEE regulator, not evidence that the exponent must be one-half, and not a quantum-gravity theory result by itself.
