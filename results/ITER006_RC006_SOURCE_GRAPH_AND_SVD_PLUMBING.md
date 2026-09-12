# ITERATION 006 — RC006 source-graph mapping and Appendix-C plumbing

Date: 2026-09-12

## Classification

`SOURCE_MAPPING_PREREQUISITES_PASS + RESPONSE_BLIND_NUMERICAL_PLUMBING_PASS / FULL_EQ29_AMPLITUDE_STILL_OPEN`

These results qualify implementation and source provenance only. They do not constitute an Eq.(29) amplitude, a physical TNR result, `BRIDGE_DERIVED`, or candidate-theory authorization.

## Appendix-C response-blind synthetic regression

Initial run `34696095267` at commit `41db3d1fe1ddf6f44b5ab9d14deb5d0d70f5b4b5` failed in all six seeds at the frozen rank-1 Eckart–Young plumbing check while the full reconstruction, singular-order and projector-phase controls passed. Raw logs identified a zero-tail numerical branch in the synthetic checker. This was classified as `NUMERICAL/IMPLEMENTATION FAIL`, not a scientific failure.

Only that numerical branch was repaired; no physical model, threshold or scientific interpretation rule was changed. Fix commit: `c5076c360a9c8f70b223da76c582563a564111be`.

Authoritative rerun: `34696313147`.

- six seed jobs: `103560293437` (101), `103560293409` (202), `103560293339` (303), `103560293471` (404), `103560293448` (505), `103560293454` (606);
- aggregate job: `103560627060`;
- aggregate artifact: `10299121187` (`rc006-c-reg-summary`);
- artifact digest: `sha256:4447351ee441964e50afa9c49ef714f8fccc5c454c23dfaa046add1625637663`;
- aggregate result: `all_pass=true`, `all_six_present=true`.

Scientific classification: `PASS_IMPLEMENTATION_REGRESSION_ONLY`. The regression is deliberately response-blind and contains no Eq.(29) physical amplitudes.

## Official-source TikZ graph AST

Authoritative run: `34696214389` at commit `a58f79332bdbf116115574ac225cbbe917261660`.

- job: `103560037655`;
- artifact: `10297799415` (`rc006-eq29-tikz-graph-ast`);
- digest: `sha256:4d914893f24d4cc9c2d9eb14331e32e24e0327c6471fbb4f8b5eacd40c541dd3`.

The source-faithful extractor found the Eq.(29) region in official arXiv `1609.02429` source file `bc-spin-nets.tex`, records the exact source SHA256, candidate TikZ environments and compact labels, and passed its frozen provenance/mapping-prerequisite gate.

Scientific classification: `PASS_SOURCE_PROVENANCE_MAPPING_PREREQUISITE_ONLY`. No graph contraction or amplitude follows from AST extraction alone.

## Exact Eq.(29)-region token stream

Authoritative run: `34696413575` at commit `3f984706536a24d4c8a948f4ced8724889f6a6e6`.

- job: `103560557294`;
- artifact: `10299235394` (`rc006-eq29-tikz-token-stream`);
- digest: `sha256:4554cd9168a9f99b0d8ea6672bbd47d8cf506074a9b503bbeb5a7f17ded5cfe9`.

The exact nearest TikZ environment is source lines `1094–1116` in `bc-spin-nets.tex`; environment SHA256 `47f99ddbbef16bdadaa6951933b0203bc4d671efebec67685441af67f03e6604`. The derived stream contains 68 structural tokens, 37 coordinate tokens, the required labels `J+`, `J-`, `j`, `l_1`, `l_2` (including source superscripts/subscripts), and an ordered path-operator stream. `has_required_labels=true`.

Scientific classification: `PASS_EXACT_SOURCE_TOKENIZATION_PREREQUISITE_ONLY`. This materially reduces the risk of hand-transcribing the braided/oriented graph but still does not close `RC006_EQ29_ORIENTED_BRAIDED_GRAPH_MAPPING_GATE`.

## Current implication

The next RC006 step is no longer source discovery. It is deterministic incidence/path reconstruction from the exact source environment, with a prospectively frozen parser-invariance gate. Only after that mapping passes may the minimal `k=12, gamma=1/3` Eq.(29) amplitude gate be implemented.

In parallel, RC008 remains an independent permitted route toward a second true QG amplitude/refinement realization; its amplitude-level reproduction is still open.

## Claim locks

- `ALL_KNOWN_SCHOOLS_FAIL`: forbidden;
- `NEW_QG_THEORY_REQUIRED`: forbidden;
- `NEW_PHYSICS_FOUND`: forbidden;
- `BRIDGE_DERIVED`: forbidden;
- candidate theory: `0% / UNFORMED`;
- synthetic SVD plumbing is not physical TNR evidence;
- source graph extraction is not an Eq.(29) amplitude.
