# ISQGR CURRENT FRONT

Date: 2026-09-12  
Active iteration: `ITERATION_004`  
Iteration completion: **90%**  
Overall scientific programme readiness: **34%**  
Candidate-theory construction: **0% — UNFORMED / constitutionally locked**

## Current lead

`BH-004_PROJECTOR_MEASURE_COVARIANT_SCALE_TRANSPORT`

The programme has crossed from motif discovery into falsifiable bridge transport, but it has **not** crossed into candidate-theory construction.

## What is now established inside ISQGR

### RM-001 accepted

`RM-001_RETAINED_SECTOR_ORIENTATION_CLOSURE_DATA` is the first accepted recurrent motif.

Structural statement:

> projected composition is not determined in general by retained rank and operator spectra alone; relative orientation of the retained/source-defined subspace to the composition operators is independent closure data.

Evidence stack:

1. exact `2x2` spectral-insufficiency theorem for `Delta = P C2 (I-P) C1 P`;
2. causal-set SSEE/source-sector chain with held-out orientation-to-closure prediction;
3. pinned SU(2) BF shared-unitary orientation null;
4. direct pinned Lorentzian EPRL shared-unitary orientation null across `gamma=0.5,1.2,2.0`.

The Lorentzian EPRL campaign passes its preregistered strong-support orientation gate for all three gamma lanes. This is gravity-side support for RM-001, not full spin-foam refinement or GR recovery.

### BH-004 admitted and first scale gate passed

BH-004 encodes effective scale data minimally as

`E_s = (P_s, mu_s)`

where `P_s` carries retained-sector orientation and `mu_s` denotes independent scale/measure/normalization data. The notation is a bridge requirement, not a fundamental ontology.

The first true three-level nested-thinning holdout used only `p0=1` and `p1=0.75` to predict the unseen `p2=0.50` projector/rank.

Aggregate over `N=512,768,1024` and seeds `301..304`:

- median held-out rank error: `0.02427`;
- median trained rank-flow exponent: `0.50349`;
- median mean principal cosine: `0.9000466`;
- median minimum principal cosine: `0.08089`;
- median random/predicted leakage gain: `2.1255x`;
- median random/predicted sequential-defect gain: `5.3339x`;
- all `12/12` jobs beat rank-matched random controls on both closure metrics.

Decision: `NATURAL SUPPORT = YES`; `STRONG SUPPORT = NO`.

Interpretation: a closure-relevant bulk/core of the source sector transports to an unseen nested scale, but a directional tail remains unstable.

### Novelty lock tightened

Projector/isometry-aware coarse graining has close precedents in tensor-network RG, projected effective dynamics, and spin-foam coarse graining. Therefore generic projector-awareness is **not** an ISQGR new-physics claim.

Potentially distinctive content is restricted to a source-native, constraint-preserving, non-retuned QG transport law that predicts unseen refinements and survives comparison with the nearest standard framework.

## Active computation

GitHub Actions run `34664913496` — `ISQGR BH-004 Stable-Core Heldout`.

Design:

1. training seeds `401..404` and sizes `512,768,1024` determine one global stable-core singular-value threshold from source-subspace geometry only, using transitions `p0->p1` and `p1->p2`;
2. no closure target is allowed in threshold fitting;
3. the threshold is frozen globally;
4. distinct test seeds `501..504` evaluate the fourth nested level `p3=0.421875`;
5. success requires stronger principal-angle stability while retaining substantial source rank and preserving closure advantage over rank-matched random controls.

This is the current decisive computation.

## Active blockers

1. Determine whether the low minimum principal cosines are an identifiable unstable edge/tail or evidence of genuine nontransportability.
2. Reproduce a true scale/refinement transport result in a second sufficiently independent QG realization. The present EPRL result is one-vertex shell change, not a refinement map.
3. Keep projector orientation flow distinct from scalar measure/normalization flow.
4. Complete the nearest-framework absorption test before any novelty promotion.
5. Replace the remaining synthetic causal-rescue component in the CEMR branch with a source-defined observable if a defensible realization is available.

## Claim locks

Still forbidden:

- `ALL_KNOWN_SCHOOLS_FAIL`;
- `NEW_QG_THEORY_REQUIRED`;
- `NEW_PHYSICS_FOUND`;
- candidate action/Hamiltonian/field equation;
- RQIR/KMQGB promotion based only on ISQGR motif evidence.

Current correct status:

`FIRST_RECURRENT_MOTIF_ACCEPTED + FIRST_SCALE_HOLDOUT_NATURAL_PASS + CANDIDATE_THEORY_UNFORMED`.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `results/ITER004_BH004_NESTED_THINNING_HELDOUT_TRANSPORT.md`
4. `results/ITER004_BH004_NEAREST_FRAMEWORK_AUDIT.md`
5. `hypotheses/BH-004_PROJECTOR_MEASURE_COVARIANT_SCALE_TRANSPORT.md`
6. `results/RM-001_RETAINED_SECTOR_ORIENTATION_CLOSURE_DATA_2026-09-12.md`
7. `results/ITER004_RM001_SPECTRAL_INSUFFICIENCY_THEOREM.md`
8. `results/ITER004_EPRL_SHARED_UNITARY_ORIENTATION_NULL.md`
9. `results/ITER004_EPRL_CROSSSHELL_GAMMA_ROBUSTNESS.md`
10. `docs/CONSTITUTION.md`
