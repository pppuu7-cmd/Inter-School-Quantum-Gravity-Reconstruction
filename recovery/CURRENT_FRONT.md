# ISQGR CURRENT FRONT

Date: 2026-09-12  
Active iteration: `ITERATION_006`  
Iteration completion: **40%**  
Last completed iteration: **ITERATION_005 — 100%**  
Overall scientific programme readiness: **44%**  
Candidate-theory construction: **0% — UNFORMED / constitutionally locked**

## Current lead

`BH-004B_TRANSPORT_ENVELOPE_LOCAL_SELECTOR`

The lead remains structurally and stress-test supported, but a second independent **true QG amplitude/refinement** realization has not yet passed. Generic projector/orientation/overcomplete-envelope structure is absorbed by standard amplitude-level TNR and is not counted as ISQGR novelty. The remaining possible novelty domain is a **source-native physical selector plus non-retuned QG refinement transport**.

## RC-006 q-deformed EPRL/FK front

The earlier source/implementation prerequisites remain valid: B13 source-to-kernel mapping passed `8009/8009`; Eq.(29) channel topology, Appendix-C feasibility and explicit Eq.(26) R-factor checks passed only in their scoped prerequisite senses. None is a full Eq.(29) amplitude.

Authoritative newest durable note:

`results/ITER006_RC006_SOURCE_GRAPH_AND_SVD_PLUMBING.md`

### Appendix-C response-blind synthetic regression — IMPLEMENTATION PASS ONLY

Initial run `34696095267` failed in the synthetic rank-1 Eckart–Young checker while reconstruction/order/phase controls passed. The first causal issue was a zero-tail numerical branch; classification: `NUMERICAL/IMPLEMENTATION FAIL`, not scientific failure. Frozen science was not changed.

Minimal fix commit: `c5076c360a9c8f70b223da76c582563a564111be`.

Authoritative rerun `34696313147`: all six seeds passed; aggregate job `103560627060`; artifact `10299121187`; digest `sha256:4447351ee441964e50afa9c49ef714f8fccc5c454c23dfaa046add1625637663`.

Classification: `PASS_IMPLEMENTATION_REGRESSION_ONLY`. It contains no Eq.(29) physical amplitude and does not raise bridge readiness.

### Official-source Eq.(29) graph extraction — SOURCE PREREQUISITES PASS

Graph-AST run `34696214389`, commit `a58f79332bdbf116115574ac225cbbe917261660`, job `103560037655`, artifact `10297799415`, digest `sha256:4d914893f24d4cc9c2d9eb14331e32e24e0327c6471fbb4f8b5eacd40c541dd3`.

Exact token-stream run `34696413575`, commit `3f984706536a24d4c8a948f4ced8724889f6a6e6`, job `103560557294`, artifact `10299235394`, digest `sha256:4554cd9168a9f99b0d8ea6672bbd47d8cf506074a9b503bbeb5a7f17ded5cfe9`.

The official arXiv `1609.02429` source identifies `bc-spin-nets.tex`; the exact nearest TikZ environment is lines `1094–1116`, environment SHA256 `47f99ddbbef16bdadaa6951933b0203bc4d671efebec67685441af67f03e6604`. The derived token stream has 68 structural tokens, 37 coordinate tokens and the required `J+`, `J-`, `j`, `l_1`, `l_2` labels.

Classification: `PASS_SOURCE_PROVENANCE/TOKENIZATION_PREREQUISITE_ONLY`. The oriented/braided incidence mapping gate is not yet closed and no contraction/amplitude is implied.

## Active parallel computation

### RC006 exact path/incidence reconstruction

Run `34697961643`, head `d914090ce98100d01aeaa9fe92ed6b94932f6701`.

Four independent TeX-preserving parser lanes (`fail-fast:false`) reconstruct the exact source environment under comment removal / line trimming / whitespace collapse / linebreak compaction. Frozen aggregate gate requires all lanes valid and one identical source hash, environment hash and canonical structural signature. This tests deterministic source mapping only.

### RC008 official-source formula qualification

Run `34697983144`, head `efb61448a401a9661f57798f5054d9fc7a2e919c`.

Three independent lanes inspect the official source archives of arXiv `1508.07961`, `1605.07649`, `1701.02311` for the amplitude, phase and renormalization formula regions respectively. This is a source-provenance prerequisite for the independent RC008 amplitude/refinement reproduction; it does not reuse the previously audited published fixed-point numbers as a fit target.

## Saturated / blocked fronts

- `RC009_REDUCED_ISOTEMPORAL_POSITIVE_BRANCH`: **SCOPED BLOCKED** after endpoint/source-phase audits; no denser quadrature without a new justified measure/contour/regularization object.
- Lorentzian `Delta4` finite-cutoff scaling/classification diagnostics: **SATURATED NEGATIVE/SCOPED**; no bridge promotion without a genuine multi-vertex refinement map.
- Generic TNR orientation/envelope novelty: **ABSORBED**; do not spend compute rediscovering it.

## Active scientific gates

1. `RC006_EQ29_ORIENTED_BRAIDED_GRAPH_MAPPING_GATE` — ACTIVE; path/incidence reconstruction running.
2. `RC006_EQ29_MINIMAL_K12_AMPLITUDE_GATE` — BLOCKED on gate 1.
3. `RC006_APPENDIX_C_C1_C2_SVD_GATE` — BLOCKED on gate 2.
4. `RC006_HELDOUT_NONRETUNED_SELECTOR_TRANSPORT_GATE` — BLOCKED on gate 3.
5. `BH004B_INDEPENDENT_QG_AMPLITUDE_REFINEMENT_GATE` — OPEN.
6. `RC008_QUANTUM_CUBOID_AMPLITUDE_REPRODUCTION_GATE` — OPEN; source-formula qualification running.
7. `MULTIVERTEX_LORENTZIAN_EPRL_REFINEMENT_GATE` — OPEN; Delta4 finite-cutoff data are not a refinement map.

## Claim locks

Still forbidden: `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`, candidate action/Hamiltonian/field equations, and RQIR/KMQGB candidate promotion from ISQGR structural evidence alone.

Current correct status:

`RM-001 ACCEPTED + BH-004B STRUCTURALLY/STRESS-TEST SUPPORTED + GENERIC TNR ENVELOPE ABSORBED + RC009 SCOPED BLOCKED + DELTA4 SCALING FRONT SATURATED + RC006 OFFICIAL-SOURCE GRAPH TOKENIZATION PASS + ORIENTED/BRAIDED INCIDENCE MAPPING RUNNING + FULL Eq29 AMPLITUDE OPEN + RC008 AMPLITUDE REPRODUCTION OPEN`.

## Exact next allowed route

If RC006 path/incidence parser-invariance passes: freeze the explicit oriented/braided graph object and implement the minimal `k=12, gamma=1/3` Eq.(29) amplitude. Only after physical amplitude PASS may Appendix-C C1/C2 SVD run on it, followed by held-out no-retune selector transport.

In parallel, if all three RC008 source-formula lanes qualify, extract/reconstruct the published restricted hypercuboid amplitude and coarse/refined volume-variance computation prospectively, reproduce at least two boundaries, then freeze the inferred flow and test a held-out boundary without retuning.

Candidate theory remains `0% / UNFORMED` until the constitution gate authorizes otherwise.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `results/ITER006_RC006_SOURCE_GRAPH_AND_SVD_PLUMBING.md`
4. `results/ITER006_RC006_EQ29_PREAMPLITUDE_PREREQUISITES.md`
5. `results/ITER006_RC006_APPENDIX_B13_MAPPING.md`
6. `results/ITER006_RC006_QGROUP_KERNEL_QUALIFICATION.md`
7. `results/ITER006_FUSION_BASIS_EMBEDDING_ORIENTATION_NULL.md`
8. `results/ITER006_FUSION_BASIS_AMPLITUDE_REPRODUCTION.md`
9. `results/ITER006_RC008_PUBLISHED_BOUNDARY_ROBUSTNESS.md`
10. `docs/CONSTITUTION.md`
