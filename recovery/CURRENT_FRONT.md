# ISQGR CURRENT FRONT

Date: 2026-09-12  
Active iteration: `ITERATION_006`  
Iteration completion: **40%**  
Last completed iteration: **ITERATION_005 — 100%**  
Overall scientific programme readiness: **44%**  
Candidate-theory construction: **0% — UNFORMED / constitutionally locked**

## Current lead

`BH-004B_TRANSPORT_ENVELOPE_LOCAL_SELECTOR`

The lead remains structurally and stress-test supported, but a second independent **true QG amplitude/refinement** realization has not yet passed. Generic projector/orientation/overcomplete-envelope structure is already absorbed by standard amplitude-level TNR and is not ISQGR novelty. The remaining possible novelty domain is a **source-native physical selector plus non-retuned QG refinement transport**.

## RC-006 q-deformed EPRL/FK front — source/implementation prerequisites advanced

Authoritative combined note:

`results/ITER006_RC006_EQ29_PREAMPLITUDE_PREREQUISITES.md`

### Appendix-B13 source-to-kernel mapping — PASS

Run `34694997395`, aggregate job `103556894034`, artifact `10298094519`, SHA256 `ecb16a4dac552d6427aacda7f66048da4bb674e47628e5dd0cf42005e03629b1`.

The frozen source-side B13 comparison passed for all `8009/8009` admissible integer-sector cases at k=6,10,12. The pinned normalized `sixjr()` object may therefore be reused only where the source graph is explicitly reduced through B13/B16.

### Eq.(29) source-explicit channel topology — PASS, AMPLITUDE STILL BLOCKED

Commit `82dcf7ae62929e004ee2af348c1e97632746f337`; run `34695720379`, job `103558741023`, artifact `10299100320`, SHA256 `af7a1424bbe4aa3bf41f5914696e7873a5ecda6a88ce3eee3780d316b33a7a28`.

For k=12, gamma=1/3:

- 11 admissible source boundary triples;
- 46 admissible coarse `(J+,J-)` pairs;
- 35/46 (`0.7608695652`) lie outside the original simplicity image;
- every original simplicity target remains represented;
- all required explicit crossing-channel sets are nonempty.

This strengthens the finite-support `envelope + source target` architecture but is still not an amplitude calculation.

### Appendix-C first-step feasibility — PASS

Run `34695720384`, job `103558741014`, artifact `10298825789`, SHA256 `dca0e3d52d386b920c7fa3f19518ad5a08008dba8785190c9ff6fbb3589bed51`.

Minimal k=12 EPRL sector:

- 31 coarse blocks;
- 26 non-simple blocks;
- max fine-pair dimension per block = 6;
- naive first-step dense complex128 upper bound = 3760 bytes.

The frozen `<512 MiB` feasibility gate passes easily. Appendix-C implementation is therefore computationally feasible once Eq.(29) amplitudes exist.

### Explicit Eq.(26) R-factor — PARTIAL AMPLITUDE-FACTOR PASS

Workflow commit `d63da2a44ec9f955a0517e506f5b5fba87769d14`; run `34695809537`, aggregate job `103558996929`, artifact `10298790946`, SHA256 `2c34bf5f9f4d2e03fa1d0af0224f227d11f39899c5d413c4e8baad3a46861d80`.

All 11 boundary lanes and 27 internal R-channels are present; all explicit R coefficients are nonzero; minimum modulus `0.9999999999999987`.

This rules out immediate deletion of admissible channels by the explicit R factor alone. The rest of the q-spin-network graph can still cancel or vanish.

## Active computation

### Official arXiv source graph discovery

Run `34695891870` was launched from commit `c7e2c33816a87ffe4238c568d960643b51b7d26f` and is queued/running according to current GitHub-hosted runner availability.

Purpose: fetch the official arXiv source archive for `1609.02429` and produce a metadata-only manifest identifying the exact TeX region, macro/graphic representation, referenced source assets and hashes for the Eq.(29)/Appendix-F EPRL graph. This is intended to prevent guessing the oriented/braided contraction from a rendered figure.

## Saturated / blocked fronts

- `RC009_REDUCED_ISOTEMPORAL_POSITIVE_BRANCH`: **SCOPED BLOCKED** after endpoint/source-phase audits; no denser quadrature without a new justified measure/contour/regularization object.
- Lorentzian `Delta4` finite-cutoff scaling/classification diagnostics: **SATURATED NEGATIVE/SCOPED**; useful structure exists but preregistered universality/transfer gates failed. No further fit-only campaign without a true refinement object.
- Generic TNR orientation/envelope novelty: **ABSORBED**; do not spend compute rediscovering it.

## Active scientific gates

1. `RC006_EQ29_ORIENTED_BRAIDED_GRAPH_MAPPING_GATE` — ACTIVE.
2. `RC006_EQ29_MINIMAL_K12_AMPLITUDE_GATE` — BLOCKED on gate 1.
3. `RC006_APPENDIX_C_C1_C2_SVD_GATE` — BLOCKED on gate 2.
4. `RC006_HELDOUT_NONRETUNED_SELECTOR_TRANSPORT_GATE` — BLOCKED on gate 3.
5. `BH004B_INDEPENDENT_QG_AMPLITUDE_REFINEMENT_GATE` — OPEN.
6. `RC008_QUANTUM_CUBOID_AMPLITUDE_REPRODUCTION_GATE` — OPEN.
7. `MULTIVERTEX_LORENTZIAN_EPRL_REFINEMENT_GATE` — OPEN; Delta4 finite-cutoff data are not a refinement map.

## Claim locks

Still forbidden:

- `ALL_KNOWN_SCHOOLS_FAIL`;
- `NEW_QG_THEORY_REQUIRED`;
- `NEW_PHYSICS_FOUND`;
- `BRIDGE_DERIVED`;
- candidate action/Hamiltonian/field equation;
- RQIR/KMQGB candidate promotion from ISQGR structural evidence alone.

Current correct status:

`RM-001 ACCEPTED + BH-004B STRUCTURALLY/STRESS-TEST SUPPORTED + GENERIC TNR ENVELOPE ABSORBED + RC009 SCOPED BLOCKED + DELTA4 SCALING FRONT SATURATED + RC006 SOURCE-FAITHFUL PREAMPLITUDE PREREQUISITES PASS + FULL Eq29 AMPLITUDE OPEN`.

## Exact next allowed route

`official-source graph discovery -> exact Eq.(29) oriented/braided graph mapping -> minimal k=12 amplitude -> Appendix-C C1 contraction/C2 SVD -> held-out no-retune selector transport`.

No candidate-theory construction is authorized before the independent QG amplitude/refinement gate passes.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `results/ITER006_RC006_EQ29_PREAMPLITUDE_PREREQUISITES.md`
4. `results/ITER006_RC006_APPENDIX_B13_MAPPING.md`
5. `results/ITER006_RC006_QGROUP_KERNEL_QUALIFICATION.md`
6. `results/ITER006_FUSION_BASIS_EMBEDDING_ORIENTATION_NULL.md`
7. `results/ITER006_FUSION_BASIS_AMPLITUDE_REPRODUCTION.md`
8. `results/ITER006_RC009_SOURCE_PHASE_ENDPOINT_AUDIT.md`
9. `results/ITER006_RC009_ENDPOINT_POWER_AUDIT.md`
10. `docs/CONSTITUTION.md`
