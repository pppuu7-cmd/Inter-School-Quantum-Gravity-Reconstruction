# Iter003 Result — Parallel Compute Campaign 001

Status: `NUMERICALLY_VERIFIED_SYNTHETIC`  
Date: 2026-09-12  
Workflow run: `34652279466`  
Aggregate artifact: `10283774657`

## 1. Campaign structure

The first GitHub Actions campaign executed in parallel:

- 20 finite-surface CEMR inversions = 5 scenarios x 4 random seeds;
- 6 scale/composition Monte Carlo jobs = 1000 trials each;
- local CEMR regression tests;
- aggregate result packaging.

All 26 numerical matrix jobs completed successfully. The workflow-level failure was isolated to a Python unittest invocation-path error; the numerical calculations themselves and aggregate artifact completed successfully. The workflow invocation has been corrected for the next campaign.

Canonical aggregate: `compute_results/CAMPAIGN_001_summary.json`.

## 2. Finite-surface CEMR results

### Clean control

- mean reduced `chi2 = 1.2440`;
- mean `phi` RMSE = `0.00384`;
- 3/4 seeds `FIT_COMPATIBLE`, 1/4 `FIT_TENSION` under the deliberately simple screening threshold;
- all 4 recover the synthetic scalar conformal field.

Interpretation: the finite-patch inverse problem is identifiable and numerically stable in this low-dimensional controlled basis.

### Increased random noise

- mean reduced `chi2 = 1.2442`;
- mean `phi` RMSE = `0.00765`;
- 3/4 compatible, 1/4 tension;
- all 4 recover the synthetic field.

Interpretation: doubling the fractional noise approximately doubles field error without destroying identifiability.

### QES-like structured nuisance

- mean reduced `chi2 = 1.1172`;
- mean `phi` RMSE = `0.01239`;
- 4/4 `FIT_COMPATIBLE`.

This is the most important cautionary result in the CEMR stream:

> a structured unmodeled correction can **bias the reconstructed conformal field while preserving apparently good fit quality**.

Therefore goodness-of-fit alone cannot validate a leading RT-area CEMR inversion. A nuisance/correction audit is mandatory before interpreting an inferred `Omega(x)` physically.

### Hidden anisotropic contamination

- mean reduced `chi2 = 361.16`;
- 4/4 `FIT_INCOMPATIBLE`;
- the scalar component itself remains close to the injected scalar field (`phi` RMSE about `0.00281`).

This is a strong synthetic obstruction result. The scalar conformal model cannot absorb orientation-dependent area information even though it still recovers the underlying scalar component.

Thus fit incompatibility and parameter-recovery error carry different information and must both be reported.

### Wrong conformal-class contamination

- mean reduced `chi2 = 22.09`;
- 4/4 `FIT_INCOMPATIBLE`;
- mean scalar-field RMSE remains small (`0.00426`).

Again the residual structure, rather than coefficient bias, detects the fact that the supplied area data cannot be represented by the assumed single scalar conformal completion.

## 3. Scale/composition Monte Carlo

Across six independent seeds with 1000 trials each:

- mean normalized coherence defect for generic random mixing: `0.59737`;
- mean defect for retained-subspace-preserving fine dynamics: `1.73e-16`;
- mean correlation between leakage probability and coherence defect: `0.4731`.

This numerically supports the exact algebraic identity

`Delta_seq = D o Phi2 o (I-E o D) o Phi1 o E`.

The experiment demonstrates that sequential scale/composition coherence is **not generic** under compression. Exact coherence returns at floating-point precision when the retained sector is invariant.

## 4. Scientific consequences

### CEMR

BH-002 survives the first finite-surface synthetic falsification attempt, but only in a narrower form:

- scalar-conformal incompatibility is detectable;
- wrong-class/anisotropic information produces a strong residual obstruction;
- structured QES-like nuisance can evade the obstruction by biasing the inferred scalar field.

Therefore the next decisive CEMR task is **nuisance identifiability**, not merely larger synthetic inversion.

### BH-001

BH-001 now has a sharper necessary condition:

> a physically valid scale map must close the retained physical sector under composition, explicitly retain the memory/boundary variables responsible for leakage, or carry a controlled coherence defect.

A claim that an effective theory composes after coarse graining cannot simply assume this closure.

## 5. Candidate motif status

`MC-001 — PHYSICAL/CONSTRAINT SECTOR NOT AUTOMATICALLY CLOSED UNDER SCALE FLOW`

is strengthened by:

- the exact scale/composition leakage identity;
- its Monte Carlo control;
- RC-006 source-grounded EPRL/FK-type coarse-graining behavior.

But `RM-001` remains **LOCKED** because a second independent source-grounded QG realization has not yet been mapped at the same semantic level.

## 6. Next parallel campaign

Priority streams:

1. **CEMR nuisance identifiability:** fit scalar geometry jointly with one or more generalized-entropy nuisance bases; quantify degeneracy and rank loss.
2. **CEMR information gain:** compare inverse-problem rank/conditioning with and without causal conformal-class restriction.
3. **FRG closure audit:** identify generated-operator / truncation-closure structure in an asymptotic-safety realization and test whether it is genuinely analogous to MC-001.
4. **EPRL native leakage map:** turn RC-006 from analogy into a native retained/discarded-sector calculation where possible.
5. **Parallel composition:** quantify `Delta_parallel` and determine whether strict monoidality must be replaced by boundary/edge-data coherence.

## Claim lock

Campaign 001 establishes properties of controlled synthetic and abstract proxy systems only. It does not validate CEMR in a physical holographic spacetime, establish a common QG mechanism, or authorize candidate-theory construction.