# ITERATION 004 — BH-004 Nested-Thinning Held-Out Transport

Date: 2026-09-12  
GitHub Actions run: `34664755715`  
Status: `SUCCESS / NATURAL SUPPORT / STRONG SUPPORT NOT REACHED`

## Question

Can a projector-aware scale-transport rule be frozen from two causal-set levels and predict a third, unseen nested-thinning level without using the held-out source projector or closure target to choose its orientation or rank?

## Construction

For each parent causal set, fixed uniform thinning marks define nested induced sets

`p0 = 1.0 > p1 = 0.75 > p2 = 0.50`.

At `p0` and `p1` only, construct the source-defined Pauli–Jordan retained sector using the frozen BH-003 prescription

`|lambda(iDelta)| >= sqrt(N)/(4*pi)`.

From `(N0,r0)` and `(N1,r1)`, infer a two-point rank flow

`r ~ N^alpha`.

For the held-out `p2` level:

1. predict `r2` from the frozen rank-flow exponent;
2. canonically restrict the `p1` retained basis to the nested `p2` subset;
3. take the leading left-singular directions of that restricted basis, truncated to the predicted rank;
4. only after the prediction is frozen, construct the actual `p2` source sector for evaluation.

No held-out closure metric or source projector is used to construct the predicted projector.

Campaign:

- parent sizes `N = 512, 768, 1024`;
- seeds `301,302,303,304`;
- `12` independent numerical jobs;
- `16` rank-matched Haar orientation controls per job.

## Preregistered gate

Natural support was frozen before the results as:

- median mean principal cosine `> 0.90`;
- median held-out rank relative error `<= 0.20`;
- median random/predicted leakage improvement `> 1`;
- median random/predicted sequential-defect improvement `> 1`;
- at least `2/3` of jobs improve both closure metrics.

Strong support required:

- median mean principal cosine `> 0.95`;
- median rank relative error `<= 0.15`;
- both median closure improvements `> 1.5`;
- at least `0.80` of jobs improve both metrics.

## Aggregate result

| quantity | result |
|---|---:|
| jobs | 12 |
| median held-out rank relative error | `0.02427` |
| median trained rank-flow exponent | `0.50349` |
| median mean principal cosine | `0.9000466` |
| median minimum principal cosine | `0.08089` |
| median random/predicted leakage improvement | `2.1255x` |
| median random/predicted sequential-defect improvement | `5.3339x` |
| fraction jobs improving both closure metrics | `1.000` |
| fraction jobs where majority random controls are worse in both | `1.000` |
| natural support | **YES** |
| strong support | **NO** |

Every one of the twelve held-out predictions beats the rank-matched random controls on both closure metrics.

The trained rank-flow exponent is centered very near `1/2`. This exponent describes retained-rank flow and must **not** be conflated with the previously measured native eigenvalue-scale transport exponent near `1.03`; they are different observables.

## Interpretation

The first BH-004 scale/refinement gate is positive but deliberately limited.

What transfers well:

- held-out retained rank is predicted accurately;
- the predicted subspace has substantial mean alignment with the unseen source sector;
- the predicted projector retains a large and completely reproducible closure advantage over orientation-free rank-matched controls.

What does not yet transfer strongly:

- the minimum principal cosine is often small;
- median mean cosine clears the natural threshold only narrowly (`0.9000466` versus `0.90`);
- therefore some directions in the retained sector are unstable under the second thinning step even while the bulk subspace and closure behaviour remain useful.

The correct current reading is therefore:

> **a closure-relevant core of the source sector is transportable under nested thinning, but the full retained subspace has an unstable directional tail.**

This is more informative than either “projector transport works” or “projector transport fails.”

## Relation to RM-001

RM-001 established that orientation is independent closure data. This campaign now shows that, in one source-defined causal-set scale map, useful orientation data can be transported to an unseen level without target-closure retuning.

Thus BH-004 advances from an admitted structural bridge to a **numerically supported bridge hypothesis**, but not yet `BRIDGE_DERIVED`.

## Nearest-framework lock

The generic fact that retained isometries/projectors matter in coarse graining has close precedents in tensor-network RG and projected effective dynamics. Therefore this result is not new physics by itself.

Potential ISQGR-specific novelty still requires a non-arbitrary, constraint-preserving transport law that survives stronger holdouts and another sufficiently independent realization.

## Next decisive test

Resolve the unstable directional tail without post-selection.

The next campaign should preregister a **stable-core transport rule** using only training levels, freeze its singular-direction criterion, and test it on a fourth nested level. The key question is whether the low minimum principal cosines represent harmless edge directions that can be source-independently identified at training scales, or whether they signal genuine nontransportability that will eventually destroy closure.

A second, later gate must reproduce the transport phenomenon in a distinct QG realization; the Lorentzian EPRL one-vertex result is not yet a true refinement map.

## Claim lock

This result does not establish:

- a universal QG renormalization law;
- full causal-set interacting dynamics;
- continuum recovery;
- GR recovery;
- a candidate QG theory;
- new physics.
