# ISQGR CURRENT FRONT

Date: 2026-09-12  
Active iteration: `ITERATION_006`  
Iteration completion: **40%**  
Last completed iteration: **ITERATION_005 — 100%**  
Overall scientific programme readiness: **44%**  
Candidate-theory construction: **0% — UNFORMED / constitutionally locked**

## Current lead

`BH-004B_TRANSPORT_ENVELOPE_LOCAL_SELECTOR`

The lead remains structurally/stress-test supported, but the independent true-QG amplitude/refinement gate has not passed. Generic projector/orientation/envelope structure remains absorbed by standard amplitude-level TNR; the possible ISQGR novelty domain stays restricted to a source-native physical selector plus non-retuned QG refinement transport.

## Newly closed prerequisites

### RC006 Eq.(29) deterministic source path reconstruction — PASS subgate

Authoritative run `34697961643`, head `d914090ce98100d01aeaa9fe92ed6b94932f6701`.

All four TeX-preserving parser lanes succeeded and aggregate job `103564711935` passed. Aggregate artifact `10298684340`, digest `sha256:ca8afc4093abb580b704666084ee1209851fdadf661a280affa09adee4a056ae`, records `frozen_gate_pass=true`, source/environment hash invariance and canonical structural-signature invariance.

Classification: `PASS_DETERMINISTIC_SOURCE_PATH_RECONSTRUCTION_SUBGATE`. It does **not** yet close the full oriented/braided contraction mapping: explicit source-authorized association of representation labels and braiding/orientation semantics is still required.

Durable note: `results/ITER006_RC006_SOURCE_GRAPH_AND_SVD_PLUMBING.md`.

### RC008 official-source formula qualification — PASS prerequisite

Initial run `34697983144` failed technically because the first parser recognized too narrow a set of TeX equation syntaxes. Required keywords were present; failure occurred before physics. Classification: `INFRASTRUCTURE/IMPLEMENTATION FAIL`.

Minimal syntax-only fix commit `8ce783247216f600195b0a4cfd6c179ac7506e55` preserved the frozen source gate. Authoritative rerun `34698110637` passed all three source lanes and aggregate job `103565184050`; aggregate artifact `10298993915`, digest `sha256:8a74186a001f7b5730af162033043704975ad0b3d6deed842992127741594c0f`.

The amplitude source `1508.07961` yields 30 candidate equation regions including `Eq:VertexDefinition`, `Eq:AmplitudeIntegral`, `Eq:ComplexAction`, `Eq:AsymptoticStateSum`, `Eq:4Volume`. The renormalization source `1701.02311` yields 27 candidate regions including `Eq:EmbeddingMaps`, `Eq:Observable`, `Eq:RenormalizedAmplitude`, `Eq:FixedPoint01/02`, and `Eq:ExpectationValueCoarseGraining`.

Classification: `PASS_SOURCE_FORMULA_QUALIFICATION_ONLY`. No amplitude, variance curve, RG flow or held-out transport has yet been reproduced.

Durable note: `results/ITER006_RC008_SOURCE_FORMULA_QUALIFICATION.md`.

## Active computation

### RC006 source-graphic label authority audit

Run `34698228895`, head `d37a4f2abdacfaa9de6d5b38f239f57e44188a4a`.

Four independent precision lanes are queued/running. Frozen gate asks whether source graphic label positions map uniquely to graph primitives with absolute nearest/second-nearest distance gap `>=0.05` and ratio `>=1.20`, invariant across numerical precision. Even a PASS only qualifies the graphic label-association layer; missing source orientation/contraction authority remains separately locked.

## Saturated / blocked fronts

- `RC009_REDUCED_ISOTEMPORAL_POSITIVE_BRANCH`: **SCOPED BLOCKED**; no denser quadrature without a justified measure/contour/regularization object.
- Lorentzian `Delta4` finite-cutoff/profile/scaling diagnostics: **SATURATED NEGATIVE/SCOPED**; no bridge promotion without a genuine refinement map.
- Generic TNR orientation/envelope novelty: **ABSORBED**.

## Active gates

1. `RC006_EQ29_ORIENTED_BRAIDED_GRAPH_MAPPING_GATE` — ACTIVE; path reconstruction passed, graphic label authority running, full contraction-ready mapping still open.
2. `RC006_EQ29_MINIMAL_K12_AMPLITUDE_GATE` — BLOCKED on gate 1.
3. `RC006_APPENDIX_C_C1_C2_SVD_GATE` — BLOCKED on gate 2.
4. `RC006_HELDOUT_NONRETUNED_SELECTOR_TRANSPORT_GATE` — BLOCKED on gate 3.
5. `BH004B_INDEPENDENT_QG_AMPLITUDE_REFINEMENT_GATE` — OPEN.
6. `RC008_QUANTUM_CUBOID_AMPLITUDE_REPRODUCTION_GATE` — OPEN; source formula inventory now qualified.
7. `MULTIVERTEX_LORENTZIAN_EPRL_REFINEMENT_GATE` — OPEN.

## Exact next allowed route

RC006: consume the source-graphic label-authority run. If it passes, combine it only with explicit source braiding/orientation conventions to freeze a contraction-ready Eq.(29) graph; then implement the minimal `k=12, gamma=1/3` amplitude. Do not run physical Appendix-C SVD before that amplitude gate passes.

RC008: use the qualified labelled formulas to build the dependency closure for the restricted hypercuboid amplitude, embedding, volume observable and expectation-value/coarse-graining formulas. Then reproduce at least two coarse/refined source boundary states, freeze the inferred `alpha' -> alpha` map, and test a held-out source boundary without retuning.

Candidate theory remains `0% / UNFORMED`. `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`, candidate equations and RQIR/KMQGB promotion remain forbidden.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `results/ITER006_RC006_SOURCE_GRAPH_AND_SVD_PLUMBING.md`
4. `results/ITER006_RC008_SOURCE_FORMULA_QUALIFICATION.md`
5. `results/ITER006_RC006_EQ29_PREAMPLITUDE_PREREQUISITES.md`
6. `results/ITER006_RC006_APPENDIX_B13_MAPPING.md`
7. `results/ITER006_RC006_QGROUP_KERNEL_QUALIFICATION.md`
8. `results/ITER006_FUSION_BASIS_EMBEDDING_ORIENTATION_NULL.md`
9. `results/ITER006_FUSION_BASIS_AMPLITUDE_REPRODUCTION.md`
10. `docs/CONSTITUTION.md`
