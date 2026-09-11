# ISQGR Iteration 003 — Multi-stream bridge falsification

Date: 2026-09-12  
Status: `COMPLETE`

## Goal

Turn the first inter-school bridge hypotheses into executable falsification/identifiability tests, while expanding source-grounded realization coverage without prematurely constructing a quantum-gravity model.

## Parallel workstreams completed

### A — Finite-surface CEMR inversion

Built and executed nonlinear synthetic inversions for clean, noisy, QES-like nuisance, anisotropic contamination and wrong-conformal-class cases.

Key result:

- clean/noisy scalar-conformal data are recoverable in the controlled basis;
- anisotropic and wrong-class contamination produce strong residual incompatibility;
- structured QES-like nuisance can preserve an apparently good fit while biasing the inferred geometry.

### B — Scale/composition coherence

Derived the exact abstract identity

`Delta_seq = D o Phi2 o (I-E o D) o Phi1 o E`.

Monte Carlo controls show nonzero coherence defect for generic fine-space mixing and floating-point-zero defect when the retained sector is invariant.

This converts BH-001 from generic coarse-graining language into a closure/no-return condition.

### C — EPRL/FK coarse-graining source audit

Added RC-006 based on reduced EPRL/FK-like tensor-network coarse graining. The studied model provides source-grounded evidence that simplicity/constraint data need not remain in the original sector under scale flow.

Recorded `MC-001 — PHYSICAL/CONSTRAINT SECTOR NOT AUTOMATICALLY CLOSED UNDER SCALE FLOW`.

Promotion to a recurrent motif remains locked because FRG truncation closure is not yet established as the same semantic object.

### D — CEMR novelty/domain audit

Compared BH-002 against existing covariant holographic entanglement inversion. Entanglement data can already contain internal cross-leaf integrability information and, in controlled settings, projected light-cone information.

Therefore CEMR novelty cannot rest on the statement that several entanglement-derived areas must fit one geometry.

Revised CEMR value criteria require independent causal information gain, scale completion or genuinely joint obstruction.

### E — Causal information-gain campaign

Added a Fisher/inverse-problem benchmark separating conformal modes from nonconformal/light-cone modes.

Result:

- no rank gain in the constructed cases because area-only systems were already full rank;
- large conditioning/variance gains occur when the area inversion is nearly degenerate and the causal channel is sufficiently precise;
- a weak/noisy causal channel can provide negligible benefit or slightly worsen finite-sample RMSE.

Thus `C1` was split into `C1a rank gain` and `C1b conditioning gain`; only C1b is supported by the current synthetic proxy.

### F — QES-like nuisance identifiability

Campaign 003 tested joint geometry+nuisance fits as the geometric and nuisance response spaces become collinear.

Result:

- low overlap: nuisance can be separated cheaply;
- medium overlap: bias is reduced at a finite variance cost;
- overlap `0.99`: joint fit retains excellent chi-square while geometry variance inflates about `50.25x` and geometric RMSE worsens.

Established gate:

`CEMR-I1 — IDENTIFIABILITY_GATE`.

Good fit quality is insufficient when geometry and quantum-information nuisance share a near-null direction.

### G — Parallel composition / edge data

Separated sequential composition from subsystem composition. Continuum gauge/gravity subsystem literature motivates an explicit boundary/interface-data obstruction to naive tensor factorization.

Recorded BH-001B: boundary-aware compositional coherence.

### H — Same-realization causal × entanglement laboratory

Added RC-007 causal-set spacetime entanglement. Causal-set SSEE provides causal order/discreteness and a covariant entanglement observable in one realization. Source literature exhibits a tension between raw volume-law entropy and area-law behavior after additional spectral truncation.

Introduced BH-003:

`Causal–Spectral Entanglement Closure (CSEC)`.

The central question is whether the required spectral scale can be derived from native causal/dynamical data rather than chosen to reproduce the target area law.

## GitHub compute record

### Campaign 001

- 20 finite-surface CEMR jobs;
- 6 x 1000 scale/composition Monte Carlo jobs;
- reproducibility rerun successful.

### Campaign 002

- 24 causal-information-gain jobs;
- workflow run `34652677145`: success.

### Campaign 003

- 24 nuisance-identifiability jobs;
- workflow run `34652964675`: success.

### Campaign 004

Three-channel causal rescue matrix launched as Iteration 004 front:

- 4 causal alignments;
- 3 causal precision levels;
- 4 seeds;
- 48 matrix jobs + aggregate.

## Scientific conclusions of Iteration 003

1. Cross-school synthesis is producing useful **obstructions and identifiability gates**, not yet a candidate action.
2. The most robust common theme so far is **closure under scale/composition with explicit accounting of discarded/interface information**.
3. CEMR remains viable only as a conditional information-complementarity programme, not as a claim that causality+entanglement automatically reconstruct spacetime.
4. Quantum-information nuisance can be statistically invisible yet physically bias geometry; near-collinearity can make geometry non-identifiable even under a good joint fit.
5. A same-realization causal-set entanglement laboratory may be a cleaner next bridge than direct causal-set ↔ AdS/CFT splicing.

## What remains locked

- accepted recurrent motifs: **0**;
- candidate QG model: **UNFORMED**;
- new physics claim: **NOT ESTABLISHED**;
- RQIR/KMQGB candidate promotion: **NOT AUTHORIZED**.

## Internal readiness metrics

Roadmap completion only; not truth probabilities.

- repository/recovery bootstrap: **90%**;
- source-grounded interface atlas: **35%**;
- recurrent-motif search: **15%** with **0 accepted motifs**;
- bridge-principle validation: **30%**;
- executable cross-school obstruction/identifiability programme: **45%**;
- candidate-theory construction: **0%**;
- overall ISQGR scientific programme readiness: **21%**;
- Iteration 003 completion: **100%**.

## Iteration 004 front

1. Complete Campaign 004: determine the causal precision/alignment threshold needed to rescue geometry from QES-like near-degeneracy.
2. Turn BH-003 into an executable holdout protocol for causal-set SSEE spectral truncation without area-law tuning.
3. Seek a realization-native version of the BH-001 leakage/coherence operator in RC-006.
4. Search for a second genuinely independent source-defined closure obstruction before promoting any recurrent motif.
5. Keep candidate equations locked unless a bridge theorem or recurrent motif crosses the constitution threshold.