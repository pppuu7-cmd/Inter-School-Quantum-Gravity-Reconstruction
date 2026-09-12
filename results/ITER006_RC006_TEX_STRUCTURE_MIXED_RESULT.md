# ITERATION 006 — RC006 independent TeX source-structure audit

Date: 2026-09-12

## Provenance

Prospective script commit: `24bffc8b2649b84c26677fb18db9cb61b4d5c3a7`  
Workflow/head: `2675d390fac61b305478eee79815daa1f02293a1`  
Authoritative run: `34699578046`  
Aggregate job: `103568866019`  
Aggregate artifact: `10299662547`  
Aggregate digest: `sha256:a8c43568aa8e1fc33f1a09ef6c70e70a8221894e3de54c59ad5f4697e9e34047`

This was prospectively defined as a structurally distinct object from the earlier failed lexical Appendix-F/crossing gate. It parses TeX include topology, headings, labels/references, graphics, the Eq.(29) source component and the recoupling source component. It does not relax or rerun the lexical thresholds.

## Raw result

Aggregate: `5/6 PASS`, `1/6 FAIL`, `all_pass=false`.

PASS roles:

- `heading_graph`;
- `label_ref_graph`;
- `graphic_graph`;
- `eq29_component`;
- `recoupling_component`.

FAIL role:

- `include_graph` — job `103568837768`, artifact `10299926442`, digest `sha256:1d16c7e5d9840aee06d127a95ba27446bf649092df32c8677c1bf4a47e14308d`.

The failure is not infrastructure/numerical. The official source downloaded and parsed normally. The archive contains a single TeX file (`tex_file_count=1`) and therefore has `edge_count=0`, `source_count=0`, `target_count=0` for `\input/\include` topology. The frozen include-graph gate required a nonempty include graph and therefore correctly fails.

## Scientific classification

`MIXED_MACHINE_READABLE_SOURCE_STRUCTURE_5_OF_6 / MONOLITHIC_SOURCE_NO_INCLUDE_GRAPH / EQ29_MAPPING_STILL_OPEN`.

This establishes that the useful structural authority is internal to one source file rather than distributed over an include graph. In particular the Eq.(29) component, recoupling component, label/reference graph, heading structure and graphic references are all machine-readable under the frozen independent tests. The failed include result is preserved; it is not repaired by changing the criterion after the fact.

The result still does **not** establish a unique oriented/braided contraction. The next source-faithful object must therefore use the now-qualified internal label/reference graph to test an exact reference chain between Eq.(29), its figure/equation labels and the recoupling identities, rather than picture proximity or relaxed lexical matching.

## Claim locks

- no Eq.(29) numerical amplitude is authorized;
- no geometry-only graph inference is authorized;
- no Appendix-C SVD/refinement result follows;
- no `BRIDGE_DERIVED`, continuum-limit, new-physics or candidate-theory claim follows.
