# Iteration 006 — DED/DLD source-semantic refinement-relation audit

## Preregistration
Frozen before implementation/production. This is an **independent** multivertex-refinement stream after the raster topology prerequisite failed. It does not retune any raster threshold and does not depend on the RC006 Eq.(29) result.

Pinned source: arXiv `1801.03771`, source tarball SHA256 `9fc0b3396573b4f5ec457cafbc487aa5a1681fcb48561916d1398ed5bcc35303`.
Pinned assets: `_images/DEDconplex_plus_vg.eps` and `_images/DLDandVertex.eps`.

## Scientific question
Does the paper's **active TeX source itself**, independently of rasterized figures, contain a machine-verifiable semantic relation between the DED and DLD objects strong enough to define a later combinatorial incidence-map gate?

## Frozen lanes (`fail-fast:false`)
1. `DED_context`: locate every active `\\includegraphics` whose path basename is exactly `DEDconplex_plus_vg`; record containing figure environment, caption, label, subsection/section heading and exact source SHA256.
2. `DLD_context`: same for basename exactly `DLDandVertex`.
3. `relation_prose`: using only the labels discovered by the first two exact filename anchors, scan active prose outside comments for sentences/paragraphs that literally reference **both** figure labels via `\\ref{...}`/`\\eqref{...}`. Record verbatim source hashes and whether the same source span contains one of the prospectively fixed relation stems: `refin`, `subdiv`, `split`, `gluing`, `glue`, `insert`, `embed`, `coarse`, `fine`, `obtained`, `replace`.
4. `explicit_map_tokens`: within ±6000 active-source characters of any both-figure reference span, search for explicit combinatorial-map evidence: an arrow/map token (`\\mapsto`, `\\to`, `->`, `→`) **and** at least one of literal vertex/edge/face tokens (`vertex`, `vertices`, `edge`, `edges`, `face`, `faces`, `V`, `E`, `F`). This lane records evidence only; it may not infer a map from geometry.

## Frozen classification
- `DED_DLD_SOURCE_SEMANTIC_INCIDENCE_GATE_READY`: both asset contexts are unique and valid, at least one both-figure exact-reference span contains a frozen relation stem, and explicit-map lane contains both an arrow/map token and V/E/F-type token. This authorizes only a separately preregistered exact combinatorial map extraction gate; no bridge credit.
- `DED_DLD_SOURCE_RELATION_PROSE_ONLY`: both figures are source-qualified and a both-figure relation span exists, but explicit map-token criterion is absent. Source-semantic relation is localized but incidence-map gate remains BLOCKED.
- `DED_DLD_SOURCE_CONTEXT_ONLY`: both figures are source-qualified but no both-figure relation span meets the frozen criterion. Refinement-map derivation remains BLOCKED.
- `INVALID_SOURCE_OR_IMPLEMENTATION`: pinned source/hash/unique-context parser failure; technical only.

## Locks
No image topology threshold changes, no OCR, no manual figure reading, no synthetic mapping, no amplitude identity, no cylindrical consistency, `bridge_credit=false`, candidate theory `0/UNFORMED`, and no `BRIDGE_DERIVED`/new-physics/new-theory claims.
