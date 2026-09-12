# ISQGR CURRENT FRONT

Date: 2026-09-12  
Active iteration: `ITERATION_006`  
Iteration completion: **30%**  
Last completed iteration: **ITERATION_005 — 100%**  
Overall scientific programme readiness: **42%**  
Candidate-theory construction: **0% — UNFORMED / constitutionally locked**

## Current lead

`BH-004B_TRANSPORT_ENVELOPE_LOCAL_SELECTOR`

The programme has passed repeated held-out scale tests and cross-realization structural tests.  The active blocker remains a **second true amplitude/refinement QG realization** that tests envelope + source-native selector factorization beyond support combinatorics or a one-vertex shell extension.

## Iteration 005 retained result

All three preregistered confirmation lines were positive:

1. causal-set long-jump transport — STRONG PASS (`34665815765`);
2. reduced EPRL/FK support closure — PASS (`34665801653`, `34665997309`);
3. Lorentzian EPRL farther-shell orientation — STRONG PASS (`34665851619`).

Decision remains:

`BH-004/BH-004B = STRENGTHENED`  
`BRIDGE_DERIVED = NO`

The independent spin-foam coarse-graining evidence remains support-level and the direct Lorentzian EPRL evidence remains one-vertex rather than a true refinement map.

## Iteration 006 completed sub-results

### A. Pinned fusion-basis amplitude control — PASS_EXECUTION

GitHub Actions run `34666262016` successfully reproduced the pinned public `Fusion-basis-coarse-graining` implementation at commit `bb4d1adb1aa81e5090f3ef25a3b9fb8845f19ff4` for three RG iterations at `g=0,0.5,1.0`.

The logs contain genuine block SVD spectra and ribbon-operator observables.  This is an amplitude-level q-deformed lattice-gauge/TNR nearest-framework control, **not** an EPRL gravity realization.

### B. RC-009 endpoint power audit — BLOCKED SCOPED

Run `34669113055`, 9 parallel lanes.

The reduced isotemporal algebraic envelope behaves approximately as a severe negative endpoint power in every tested direction:

- coarse: `p ~ -141.77`;
- fine edges: roughly `p ~ -330 ... -344`;
- simultaneous fine diagonal: `p ~ -1200.15`.

All fits had very high log-log quality and all failed the corresponding simple absolute-integrability threshold.  Therefore denser quadrature alone cannot repair this reduced positive-measure branch.

### C. RC-009 source-phase endpoint audit — STRONGER BLOCKED SCOPED

Run `34671649669`, 9/9 lanes + aggregate SUCCESS.

The remaining source-internal conditional-convergence escape route was tested directly using the frozen branch

`cos(S_R/G + arg D) + cos(gamma S_R/G - Lambda V4/G)`.

Result: **all 9 lanes exclude this source branch as an endpoint regularizer in the reduced isotemporal realization**.  Toward the endpoint the phase variations shrink, the branch remains bounded away from zero, and the combined sign is stable.

Representative coarse terminal variations:

- phase 1: `2.568476e-4 rad`;
- phase 2: `1.222066e-4 rad`;
- minimum branch magnitude: `1.373953`.

Classification:

`RC009_REDUCED_ISOTEMPORAL_SOURCE_BRANCH_ENDPOINT_DIVERGENCE_NOT_RESCUED_BY_ITS_FROZEN_OSCILLATORY_FACTOR`.

Claim lock: no no-go for Lorentzian EPRL, other contours/measures, degrees of freedom removed by the reduction, or full multi-vertex refinement.

## Active parallel computation

### Fusion-basis SVD invariant audit

GitHub Actions run `34671694256`.

Six coupling lanes are running at

`g = 0, 0.25, 0.5, 0.75, 1.0, 1.15`

for five RG iterations each.  The preregistered outputs are normalized SVD-flow distances, effective retained-sector ranks, normalized spectral entropy and off-diagonal envelope mass.

Purpose: determine how much of `envelope + selector` language is already generic to standard SVD/TNR embedding-map coarse graining.  A generic persistent envelope in this control would weaken any uniqueness claim for the envelope part of BH-004B; only a **source-native local selector with extra closure/transport content** could remain discriminative.

## Current decisions

1. Stop spending compute on denser quadrature of the blocked RC-009 reduced isotemporal positive branch.
2. Consume the five-step fusion-basis SVD-control artifacts and quantify which BH-004B ingredients are generic TNR structure.
3. Continue searching for a genuine multi-vertex Lorentzian EPRL/spinfoam amplitude/refinement realization or another independent QG amplitude/refinement realization.
4. Keep amplitude-level orientation/closure metrics frozen before inspecting target QG outputs.
5. Keep candidate-theory construction locked until an independent amplitude/refinement gate passes.

## Claim locks

Still forbidden:

- `ALL_KNOWN_SCHOOLS_FAIL`;
- `NEW_QG_THEORY_REQUIRED`;
- `NEW_PHYSICS_FOUND`;
- `BRIDGE_DERIVED`;
- candidate action/Hamiltonian/field equation;
- RQIR/KMQGB candidate promotion from ISQGR structural evidence alone.

Current correct status:

`RM-001 ACCEPTED + BH-004B STRONGLY SUPPORTED IN CAUSAL SCALE TESTS + CROSS-REALIZATION SUPPORT/ONE-VERTEX GRAVITY SUPPORT + RC009 REDUCED BRIDGE BLOCKED + AMPLITUDE/TNR DISCRIMINATION GATE RUNNING`.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `results/ITER006_RC009_SOURCE_PHASE_ENDPOINT_AUDIT.md`
4. `results/ITER006_RC009_ENDPOINT_POWER_AUDIT.md`
5. `results/ITER005_BH004B_LONGJUMP_HELDOUT.md`
6. `results/ITER005_RC006_EPRL_FUSION_SUPPORT_CLOSURE.md`
7. `results/ITER005_RC006_MULTI_STEP_SUPPORT_ENVELOPE_GROWTH.md`
8. `results/ITER005_EPRL_SHELL_DISTANCE_ORIENTATION.md`
9. `results/ITER005_FRG_EH_SCHEME_COVARIANCE.md`
10. `hypotheses/BH-004B_TRANSPORT_ENVELOPE_LOCAL_SELECTOR.md`
11. `results/RM-001_RETAINED_SECTOR_ORIENTATION_CLOSURE_DATA_2026-09-12.md`
12. `docs/CONSTITUTION.md`
