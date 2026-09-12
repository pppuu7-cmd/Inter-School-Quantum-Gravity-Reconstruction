# ISQGR CURRENT FRONT

Date: 2026-09-12  
Active iteration: `ITERATION_006`  
Iteration completion: **34%**  
Last completed iteration: **ITERATION_005 — 100%**  
Overall scientific programme readiness: **44%**  
Candidate-theory construction: **0% — UNFORMED / constitutionally locked**

## Current lead

`BH-004B_TRANSPORT_ENVELOPE_LOCAL_SELECTOR`

The programme has repeated held-out scale support and cross-realization structural support, but the active blocker remains a **second true QG amplitude/refinement realization** with source-native non-retuned transport/refinement content. Generic projector/orientation/envelope structure is treated as absorbed by standard amplitude-level TNR and is not novelty.

## Newly consumed terminal result — RC006 q-group kernel qualification

Authoritative result note: `results/ITER006_RC006_QGROUP_KERNEL_QUALIFICATION.md`.

The initial raw tetrahedral-symmetry qualification was retained as a failure at k=12, rather than weakened after inspection. A convention-relevant follow-up was then frozen: orthogonality of every nontrivial square admissible recoupling matrix built from the pinned `sixjr` object.

Authoritative workflow run: `34694602675`  
Aggregate job: `103555842825`  
Aggregate artifact: `10298547764`  
Artifact SHA256: `a271a9de96dbf77dea0ec9b68b9480c0d0edd666c29ae7e3e89739eb93055f5e`

Frozen gate:

`max(||M M^T-I||_inf, ||M^T M-I||_inf) <= 1e-9`

for every nontrivial square admissible block.

Scientific classification: **PASS — convention/kernel qualification only**.

- k=6: 16 nontrivial blocks, 0 bad, max error about `1.50e-15`;
- k=10: 216 blocks, 0 bad, max error about `3.72e-15`;
- k=12: 505 blocks, 0 bad, max error about `2.47e-15`.

This permits reuse of the pinned kernel only for fusion/admissibility and recoupling identities directly validated by the qualification. It does **not** reproduce the EPRL tensor, Eq. (29), Appendix-C RG flow, a refinement map, or a bridge.

## Active computation — RC006 Appendix-B13 source-to-kernel mapping

Independent source-side implementation commit:

`442f3bb3304cc9b07947cf980db1499cd3880dc1`

Workflow-launch commit:

`3f036645fa0d66d16a7078f4d8c6a46a759ffbf9`

The gate exhaustively compares the source-side Appendix-B Eq. (B13) normalized graphical recoupling coefficient against the pinned `Fusion-basis-coarse-graining` `sixjr()` implementation at levels k=6,10,12.

Frozen per-case gate:

`absolute_error <= 1e-11 OR relative_error <= 1e-11`

for every admissible integer-sector sextuple.

A PASS authorizes using the pinned `sixjr` only where the RC006 source graph has explicitly been reduced via the paper's B13/B16 identities. Eq. (29) remains unimplemented until its whole graph is mapped without ambiguity.

## Other open / blocked fronts

- `BH004B_INDEPENDENT_QG_AMPLITUDE_REFINEMENT_GATE`: OPEN; no independent true QG amplitude/refinement bridge yet.
- `RC008_QUANTUM_CUBOID_AMPLITUDE_REPRODUCTION_GATE`: OPEN.
- `RC006_QDEFORMED_EPRL_FK_AMPLITUDE_TNR_RECONSTRUCTION_GATE`: OPEN; B13 convention bridge is the current prerequisite.
- `MULTIVERTEX_LORENTZIAN_EPRL_REFINEMENT_GATE`: OPEN; finite-cutoff Delta4 diagnostics are not sufficient without a genuine refinement map.
- `RC009_REDUCED_ISOTEMPORAL_POSITIVE_BRANCH`: **SCOPED BLOCKED** after endpoint-power and source-phase audits; do not spend compute on denser quadrature without a mathematically justified new measure/contour/regularization object.

## Claim locks

Still forbidden:

- `ALL_KNOWN_SCHOOLS_FAIL`;
- `NEW_QG_THEORY_REQUIRED`;
- `NEW_PHYSICS_FOUND`;
- `BRIDGE_DERIVED`;
- candidate action/Hamiltonian/field equation;
- RQIR/KMQGB candidate promotion from ISQGR structural evidence alone.

Current correct status:

`RM-001 ACCEPTED + BH-004B STRUCTURALLY/STRESS-TEST SUPPORTED + GENERIC TNR ENVELOPE ABSORBED + RC009 REDUCED BRIDGE SCOPED BLOCKED + RC006 SOURCE-FAITHFUL Q-DEFORMED AMPLITUDE RECONSTRUCTION IN PROGRESS`.

## Exact next allowed gate

If Appendix-B13 mapping passes: map the remaining Eq. (29) EPRL graphical factor source-faithfully into the validated B13/B16 recoupling objects, freeze a minimal k=12 amplitude check, and only after that attempt Appendix-C coarse graining/SVD with held-out non-retuned transport/selector tests.

If Appendix-B13 mapping fails: retain the failure and isolate the exact source/kernel convention mismatch without changing the frozen threshold.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `results/ITER006_RC006_QGROUP_KERNEL_QUALIFICATION.md`
4. `experiments/rc006_b13_sixjr_source_mapping.jl`
5. `results/ITER006_FUSION_BASIS_EMBEDDING_ORIENTATION_NULL.md`
6. `results/ITER006_FUSION_BASIS_AMPLITUDE_REPRODUCTION.md`
7. `results/ITER006_RC008_PUBLISHED_BOUNDARY_ROBUSTNESS.md`
8. `results/ITER006_RC009_SOURCE_PHASE_ENDPOINT_AUDIT.md`
9. `results/ITER006_RC009_ENDPOINT_POWER_AUDIT.md`
10. `docs/CONSTITUTION.md`
