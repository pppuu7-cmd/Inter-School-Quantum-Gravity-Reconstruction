# ITERATION 006 — RC006 source-graph mapping and Appendix-C plumbing

Date: 2026-09-12

## Classification

`SOURCE_MAPPING_PREREQUISITES_PARTIAL_PASS + GRAPHIC_GEOMETRY_AUTHORITY_FAIL + RESPONSE_BLIND_NUMERICAL_PLUMBING_PASS / FULL_EQ29_AMPLITUDE_STILL_OPEN`

These results qualify implementation and source provenance only. They do not constitute an Eq.(29) amplitude, a physical TNR result, `BRIDGE_DERIVED`, or candidate-theory authorization.

## Appendix-C response-blind synthetic regression

Initial run `34696095267` at commit `41db3d1fe1ddf6f44b5ab9d14deb5d0d70f5b4b5` failed in all six seeds at the frozen rank-1 Eckart–Young plumbing check while the full reconstruction, singular-order and projector-phase controls passed. Raw logs identified a zero-tail numerical branch in the synthetic checker. This was classified as `NUMERICAL/IMPLEMENTATION FAIL`, not a scientific failure.

Only that numerical branch was repaired; no physical model, threshold or scientific interpretation rule was changed. Fix commit: `c5076c360a9c8f70b223da76c582563a564111be`.

Authoritative rerun: `34696313147`; aggregate job `103560627060`; aggregate artifact `10299121187`, digest `sha256:4447351ee441964e50afa9c49ef714f8fccc5c454c23dfaa046add1625637663`; all six seeds passed.

Scientific classification: `PASS_IMPLEMENTATION_REGRESSION_ONLY`.

## Official-source TikZ graph AST and token stream

AST run `34696214389`, commit `a58f79332bdbf116115574ac225cbbe917261660`, job `103560037655`, artifact `10297799415`, digest `sha256:4d914893f24d4cc9c2d9eb14331e32e24e0327c6471fbb4f8b5eacd40c541dd3`.

Token-stream run `34696413575`, commit `3f984706536a24d4c8a948f4ced8724889f6a6e6`, job `103560557294`, artifact `10299235394`, digest `sha256:4554cd9168a9f99b0d8ea6672bbd47d8cf506074a9b503bbeb5a7f17ded5cfe9`.

The official arXiv `1609.02429` source identifies `bc-spin-nets.tex`; exact nearest TikZ environment lines `1094–1116`, environment SHA256 `47f99ddbbef16bdadaa6951933b0203bc4d671efebec67685441af67f03e6604`. The derived stream contains 68 structural tokens, 37 coordinate tokens, the required source labels and 18 path operators including two arcs.

Classification: `PASS_SOURCE_PROVENANCE_AND_TOKENIZATION_PREREQUISITE_ONLY`.

## Eq.(29) path/incidence parser-invariance subgate — PASS

Computation commit `82f8e5869d77327dca00ddb958d4ff36bc44921f`; workflow/head `d914090ce98100d01aeaa9fe92ed6b94932f6701`; run `34697961643`.

Four lanes succeeded: `103564616715`, `103564616779`, `103564616696`, `103564616649`; aggregate `103564711935`; artifact `10298684340`, digest `sha256:ca8afc4093abb580b704666084ee1209851fdadf661a280affa09adee4a056ae`.

Frozen aggregate: `lane_count=4`, `all_lane_pass=true`, `source_hash_invariant=true`, `environment_hash_invariant=true`, `structural_signature_invariant=true`, `frozen_gate_pass=true`.

Classification: `PASS_DETERMINISTIC_SOURCE_PATH_RECONSTRUCTION_SUBGATE`.

## Eq.(29) source-graphic label authority — SCIENTIFIC/DIAGNOSTIC FAIL

Prospective computation commit `86ca9806e3934fade69817518091325849f8359e`; workflow/head `d37a4f2abdacfaa9de6d5b38f239f57e44188a4a`; run `34698228895`.

Frozen gate: every source label had to have a uniquely dominant nearest graph primitive with both absolute nearest/second-nearest distance gap `>=0.05` and distance ratio `>=1.20`, invariant over coordinate rounding at 12, 9, 6 and 4 digits.

All four lanes reached the scientific comparison and failed: jobs `103565301058` (12), `103565301029` (9), `103565301033` (6), `103565301142` (4); aggregate `103565420131` failed. Aggregate artifact `10299149029`, digest `sha256:907e1781389a719bc75985a012895e85b80e9d340aa81ac1c3a2f4204a1e618f`, records `lane_count=4`, `all_lane_pass=false`, `assignment_precision_invariant=true`, `frozen_gate_pass=false`.

The 12-digit raw artifact `10299068962`, digest `sha256:93adec18a829976f21f4ea6c0e9688244b590055ee576080066a2f661b7e9e87`, shows why the gate fails rather than an infrastructure problem:

- `J^-`: absolute gap `0.0500776` passes but ratio `1.11803 < 1.20`;
- `J^+`: same ratio `1.11803 < 1.20`;
- `j^-_1`: exact nearest/second-nearest tie, gap `0`, ratio `1`;
- `l_1`: gap `0.00440229`, ratio `1.00778`;
- `l_2`: gap `0.00440229`, ratio `1.00778`.

The assignments are precision-invariant, so this is not coordinate-roundoff instability. Scientific classification: `FAIL_GRAPHIC_GEOMETRY_ALONE_DOES_NOT_AUTHORIZE_CONTRACTION_LABEL_ASSIGNMENT`.

No threshold is relaxed and no nearest-line heuristic may be promoted after this result. The full `RC006_EQ29_ORIENTED_BRAIDED_GRAPH_MAPPING_GATE` therefore remains open and must be closed from explicit source equations/text/macros and orientation/braiding conventions, not geometric proximity in the rendered/source TikZ diagram.

## Independent RC008 source-formula qualification

Initial run `34697983144` failed because the first extractor recognized only a narrow subset of TeX display environments; role keywords were present. Classification: `INFRASTRUCTURE/IMPLEMENTATION FAIL`.

Minimal source-syntax-only repair commit `8ce783247216f600195b0a4cfd6c179ac7506e55` preserved the frozen gate. Authoritative rerun `34698110637` passed all three official-source roles and aggregate `103565184050`; aggregate artifact `10298993915`, digest `sha256:8a74186a001f7b5730af162033043704975ad0b3d6deed842992127741594c0f`.

Classification: `PASS_SOURCE_FORMULA_QUALIFICATION_ONLY`; amplitude/refinement reproduction remains open. Detailed note: `results/ITER006_RC008_SOURCE_FORMULA_QUALIFICATION.md`.

## Current implication

RC006 source discovery, exact tokenization and deterministic path reconstruction are qualified, but geometry-only label authority is rejected. The next RC006 route must derive a contraction-ready graph from source semantics/conventions before any minimal `k=12, gamma=1/3` Eq.(29) amplitude run.

RC008 now has an independent, source-authorized formula inventory and can proceed to formula dependency closure followed by executable restricted hypercuboid amplitude/variance reconstruction.

## Claim locks

- `ALL_KNOWN_SCHOOLS_FAIL`: forbidden;
- `NEW_QG_THEORY_REQUIRED`: forbidden;
- `NEW_PHYSICS_FOUND`: forbidden;
- `BRIDGE_DERIVED`: forbidden;
- candidate theory: `0% / UNFORMED`;
- synthetic SVD plumbing is not physical TNR evidence;
- source graph extraction/path reconstruction is not an Eq.(29) amplitude;
- failed graphic proximity authority cannot be repaired by weakening its frozen thresholds.
