# ISQGR CURRENT FRONT

Date: 2026-09-12  
Active iteration: `ITERATION_006`  
Iteration completion: **12%**  
Last completed iteration: **ITERATION_005 — 100%**  
Overall scientific programme readiness: **42%**  
Candidate-theory construction: **0% — UNFORMED / constitutionally locked**

## Current lead

`BH-004B_TRANSPORT_ENVELOPE_LOCAL_SELECTOR`

The programme has now passed repeated held-out scale tests and cross-realization structural tests. The active blocker is no longer discovery of an orientation/closure motif; it is obtaining a **second true amplitude/refinement realization** that tests the envelope + selector factorization without reducing the problem to support combinatorics or a one-vertex shell extension.

## Iteration 005 completed

Three preregistered confirmation lines were required to yield at least two positives. All three were positive.

### 1. Causal-set long-jump transport — STRONG PASS

GitHub Actions run `34665815765`.

New sizes/seeds were used at two substantially larger nested thinning jumps.

`p=0.75 -> 0.375`:

- median rank error `0.0500`;
- mean/min principal cosine `0.989998 / 0.937160`;
- predicted/envelope projector-distance ratio `0.487849`;
- closure gains over rank-matched random `3.171x / 6.518x`;
- `9/9` jobs improve both closure metrics;
- strong gate: **PASS**.

`p=0.75 -> 0.25`:

- median rank error `0.07895`;
- mean/min principal cosine `0.990514 / 0.946815`;
- projector-distance ratio `0.424011`;
- closure gains `3.218x / 7.287x`;
- `9/9` jobs improve both metrics;
- strong gate: **PASS**.

Conclusion: the causal-set BH-004B factorization survives much larger scale jumps and is not a local-thinning artifact in the tested realization.

### 2. RC-006 reduced EPRL/FK support closure — PASS

GitHub Actions runs `34665801653` and `34665997309`.

Exact finite `SU(2)_k` fusion-support audits show the same semantic architecture:

`source simplicity support -> overcomplete recoupling envelope -> source-native local selector`.

One-step raw support leakage:

- `k=6, gamma=1/3`: `2/6` events leaked;
- `k=10, gamma=3/5`: `2/6` leaked;
- `k=12, gamma=1/3`: `60/71` leaked.

All source targets remained inside the recoupling envelope and the frozen source simplicity selector recovered the source support.

Multi-step raw support growth:

- `k=6`: `2 -> 4 -> 8 -> 8`;
- `k=10`: `2 -> 4 -> 9 -> 12`;
- `k=12`: `3 -> 45 -> 119 -> 119`.

For `k=12`, the fraction of saturated support still obeying the source EPRL map falls to about `2.5%`.

Claim lock: this is support-level combinatorics, not q-deformed amplitude/TNR reproduction.

### 3. Lorentzian EPRL farther-shell orientation — STRONG PASS

GitHub Actions run `34665851619`.

The previous pinned one-vertex orientation-null diagnostic was extended from `Dl=1` to `Dl=2` across `gamma=0.5,1.2,2.0`.

Far-shell median orientation-null/source return improvements:

- `gamma=0.5`: `1.847x`, majority-null-worse `0.623`;
- `gamma=1.2`: `4.238x`, majority-null-worse `0.697`;
- `gamma=2.0`: `4.144x`, majority-null-worse `0.694`.

All three gamma lanes pass the preregistered strong gate. Median far/near orientation-gain ratio is about `1.041`, so the effect does not decay at the second shell in this diagnostic.

Claim lock: one-vertex shell distance is not multi-vertex spin-foam refinement.

## FRG covariance stress

GitHub Actions run `34665907393`.

Two Einstein–Hilbert truncation regulator schemes retain a positive NGFP but move its raw coordinates substantially:

- optimized/Litim: `(g*,lambda*)=(0.7073,0.1932)`;
- sharp cutoff: `(0.4027,0.3297)`.

More composite/local-flow quantities are substantially more stable:

- `g* lambda*` relative spread ~`2.9%`;
- dominant local-Jacobian right-singular direction angle in common `(g,lambda)` coordinates ~`1.84 degrees`.

This is treated as a covariance/representation warning, not an identification of FRG eigendirections with RM-001.

## Iteration 005 decision

Preregistered promotion condition: at least two positive lines among causal long-jump, RC-006 support factorization, and Lorentzian EPRL far shell.

Observed: **3/3 positive**.

Decision:

`BH-004/BH-004B = STRENGTHENED`  
`BRIDGE_DERIVED = NO`

Reason: the independent spin-foam coarse-graining realization is still support-level, while the direct Lorentzian EPRL realization remains one-vertex rather than a true refinement map.

## Iteration 006 active computation

GitHub workflow launched from commit `2917fce29f9dca8c4741be4f6aee2eaccca75dda`:

`ISQGR Fusion-Basis Amplitude Control`.

It pins Sebastian Steinhaus's public `Fusion-basis-coarse-graining` implementation at commit

`bb4d1adb1aa81e5090f3ef25a3b9fb8845f19ff4`,

and attempts a three-RG-step execution at couplings `g=0,0.5,1.0`.

Purpose: establish an executable **amplitude-level q-deformed nearest-framework control** with genuine SVD embedding maps and RG singular values before testing whether BH-004B merely redescribes standard tensor-network embedding-map structure.

This control is not an EPRL gravity realization and cannot promote the QG bridge by itself.

## Active blockers

1. Reproduce or reconstruct an amplitude-level version of RC-006 with at least one BC control and one EPRL/FK case.
2. Obtain a genuine multi-vertex Lorentzian EPRL/spinfoam refinement or another independent QG amplitude/refinement realization.
3. Test whether envelope + local selector remains informative after comparison with standard TNR embedding maps and singular-value truncation.
4. Define all amplitude-level orientation/closure metrics before inspecting target outputs.
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

`RM-001 ACCEPTED + BH-004B STRONGLY SUPPORTED IN CAUSAL SCALE TESTS + CROSS-REALIZATION SUPPORT/ONE-VERTEX GRAVITY SUPPORT + AMPLITUDE-REFINEMENT GATE OPEN`.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `results/ITER005_BH004B_LONGJUMP_HELDOUT.md`
4. `results/ITER005_RC006_EPRL_FUSION_SUPPORT_CLOSURE.md`
5. `results/ITER005_RC006_MULTI_STEP_SUPPORT_ENVELOPE_GROWTH.md`
6. `results/ITER005_EPRL_SHELL_DISTANCE_ORIENTATION.md`
7. `results/ITER005_FRG_EH_SCHEME_COVARIANCE.md`
8. `results/ITER004_BH004B_ENVELOPE_LOCAL_SELECTOR_HELDOUT.md`
9. `hypotheses/BH-004B_TRANSPORT_ENVELOPE_LOCAL_SELECTOR.md`
10. `results/RM-001_RETAINED_SECTOR_ORIENTATION_CLOSURE_DATA_2026-09-12.md`
11. `docs/CONSTITUTION.md`
