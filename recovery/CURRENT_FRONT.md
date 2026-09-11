# ISQGR Current Research Front

Updated: 2026-09-12  
Active iteration: `ITERATION_004` (**20%**)  
Last completed iteration: `ITERATION_003` (**100%**)  
Project phase: `PHASE_1 / BRIDGE_FALSIFICATION_ACTIVE`

## Canonical status

- Overall ISQGR scientific programme readiness: **21%**
- Repository/recovery bootstrap: **90%**
- Source-grounded interface atlas: **35%**
- Recurrent-motif search: **15%**, accepted motifs: **0**
- Bridge-principle validation: **30%**
- Executable obstruction/identifiability programme: **45%**
- Candidate-theory construction: **0%**
- Candidate theory: `UNFORMED`
- New physics: **NOT ESTABLISHED**
- RQIR/KMQGB promotion: **NOT AUTHORIZED**

Readiness numbers are roadmap-completion metrics, not probabilities of correctness.

## Active bridge hierarchy

### BH-001 — Scale-Compatible Physical Composition

The generic statement has been sharpened by the exact sequential coherence defect

`Delta_seq = D o Phi2 o (I-E o D) o Phi1 o E`.

Scale/composition coherence is therefore not automatic under coarse graining. It requires closure of the retained physical sector, irreversible loss of discarded information, or explicit memory/boundary variables carrying the defect.

### BH-001B — Boundary-aware compositional coherence

Parallel/subsystem composition cannot be assumed to factorize naively in gauge/gravity systems. Interface/edge data may be required for physical gluing and scale transport.

### BH-002 — Causal–Entanglement Metric Reconstruction

BH-002 is retained only in an identifiability-conditioned form. Entanglement-only reconstruction already has nontrivial internal consistency in controlled holographic settings, so causal input must demonstrate independent information gain, scale completion or a genuinely joint obstruction.

Established gate:

`CEMR-I1 — IDENTIFIABILITY_GATE`.

A good chi-square is insufficient if geometry and generalized-entropy nuisance share a near-null response direction.

### BH-003 — Causal–Spectral Entanglement Closure

Current lead hypothesis.

Causal-set spacetime entanglement supplies a same-realization laboratory containing causal order/discreteness and a covariant entanglement observable. The central question is whether the additional spectral scale required for continuum-like entanglement behavior can be derived from native causal/dynamical data rather than selected to reproduce a target area law.

## Campaign 001 — finite-surface CEMR + composition coherence

Status: `REPRODUCED_EXECUTABLE`.

Finite-surface CEMR:

- clean: mean reduced chi2 about `1.244`, phi RMSE `0.00384`;
- noise: mean reduced chi2 about `1.244`, phi RMSE `0.00765`;
- QES-like nuisance: mean reduced chi2 about `1.117`, phi RMSE `0.01239`, all fits apparently compatible;
- anisotropic contamination: mean reduced chi2 about `361.16`, 4/4 incompatible;
- wrong conformal class: mean reduced chi2 about `22.09`, 4/4 incompatible.

Key lesson: structured quantum-information nuisance can bias geometry without spoiling apparent fit quality.

Composition Monte Carlo:

- generic mixing mean coherence defect about `0.59737`;
- retained-subspace-preserving dynamics mean defect about `1.7e-16`;
- leakage/defect correlation about `0.473`.

## Campaign 002 — independent causal information gain

Workflow run `34652677145`: **SUCCESS**.

No synthetic rank gain was observed because area-only systems were already full rank. Strong conditioning gain appears only when the area inverse problem is nearly degenerate and the causal channel is sufficiently precise.

At degeneracy `0.999`, sigma_causal `0.02`:

- condition number: about `1999 -> 6.84`;
- conformal variance reduction: about `250.6x`;
- conformal RMSE improvement: about `13.9x`.

At degeneracy `0.9`, sigma_causal `0.10`, RMSE improvement is about `0.95x`, i.e. slightly worse in the finite-seed average.

Therefore a second channel is not automatically useful; independence and precision are quantitative gates.

## Campaign 003 — geometry/nuisance identifiability

Workflow run `34652964675`: **SUCCESS**.

At response-space overlap `0.2`, nuisance can be separated with geometry variance inflation only about `1.04x`.

At overlap `0.8`, joint fitting can strongly reduce bias but costs about `2.78x` geometry variance.

At overlap `0.99`:

- joint condition number about `199`;
- geometry variance inflation about `50.25x`;
- joint reduced chi2 still about `0.72`;
- joint geometry RMSE about `0.1346` and can be worse than the naive geometry-only fit.

Thus explicit nuisance modelling can itself create a practically non-identifiable geometry when response directions are nearly collinear.

## Source-grounded motif search

### MC-001

`PHYSICAL/CONSTRAINT SECTOR NOT AUTOMATICALLY CLOSED UNDER SCALE FLOW`.

RC-006 reduced EPRL/FK-type tensor coarse graining supports this as a scoped source-defined tension. FRG truncation closure is structurally related but not yet the same semantic object, so promotion to `RM-001` remains forbidden.

### MC-002

`SCALE EVOLUTION REQUIRES CLOSURE DATA BEYOND A CHOSEN REDUCED DESCRIPTION`.

This is broader but currently too generic to count as new quantum-gravity structure.

## Same-realization Corridor B upgrade

RC-007 causal-set spacetime entanglement replaces part of the difficult causal-set ↔ holography splice with a same-realization laboratory.

The strong next question is not whether an area law can be recovered by tuning a spectral threshold, but whether a **frozen spectral rule** can be derived independently from causal density/dynamics and transferred to unseen regions/backgrounds without retuning.

## Active Campaign 004

Workflow run `34653258086` launched.

Three-channel synthetic system:

`area/entanglement + quantum-information nuisance + causal observable`.

Matrix:

- geometry/nuisance overlap fixed at `0.99`;
- causal alignment with the dangerous near-null direction: `0.0, 0.5, 0.9, 1.0`;
- causal uncertainty: `0.02, 0.05, 0.20`;
- four seeds;
- `48` jobs plus aggregate.

Target: quantify the minimum independent causal precision/alignment required to restore stable geometric inference.

## Iteration 004 decisive fronts

1. Complete Campaign 004 and derive a quantitative `CAUSAL_RESCUE_GATE`.
2. Turn BH-003 into an executable non-circular spectral holdout protocol.
3. Build a realization-native retained/discarded-sector map for RC-006 if the source objects permit it.
4. Find a genuinely independent second closure obstruction before any recurrent-motif promotion.
5. Keep action/field-equation construction locked until a bridge theorem or recurrent motif survives the constitution threshold.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `research_log/ITERATION_003.md`
4. `results/ITER003_PARALLEL_CAMPAIGN_003_NUISANCE_IDENTIFIABILITY.md`
5. `results/ITER003_PARALLEL_CAMPAIGN_002_INFORMATION_GAIN.md`
6. `results/ITER003_PARALLEL_CAMPAIGN_001.md`
7. `hypotheses/BH-003_CAUSAL_SPECTRAL_ENTANGLEMENT_CLOSURE.md`
8. `realizations/RC-007_CAUSAL_SET_SPACETIME_ENTANGLEMENT.md`
9. `results/ITER003_BH001_SCALE_COMPOSITION_LEAKAGE_IDENTITY.md`
10. `realizations/RC-006_EPRL_FK_TENSOR_COARSE_GRAINING.md`
11. `hypotheses/BH-002_CAUSAL_ENTANGLEMENT_METRIC_RECONSTRUCTION.md`
12. `hypotheses/BH-001_SCALE_COMPATIBLE_PHYSICAL_COMPOSITION.md`
13. `docs/CONSTITUTION.md`
14. `protocol/INTERFACE_FAILURE_TAXONOMY.md`
