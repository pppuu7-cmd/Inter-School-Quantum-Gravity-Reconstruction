# ITER018 preregistration - parallel Eq.(27), even-k, and provenance audit

Date: 2026-09-14
Parent checkpoint: ITER017, recovery head `91a6a210727ae931d0e326ccc14e98830ce0767a`.

## Status at registration
ITER017 established a scoped source/algebra PASS for target cap/cup and residual phase gauge, but exact Eq.(27) graph topology and an independent even-k convention check remained open. Before this registration, exploratory source discovery located Zache, Gonzalez-Cuadra and Zoller, arXiv:2304.02527v2, whose supplemental material visibly states SU(2)_k data for positive integer k. No Iter018 source archive has yet been downloaded in a production run, no Eq.(27) source graph has been translated to components, no q-CG coefficient implementation has been run, and no amplitude/Iter012 computation is authorized.

## Parallel execution design
The checkpoint is split into independent lanes that may run concurrently. Failure or transport blocking in one lane must not erase evidence from another.

### Lane A - exact Eq.(27) source-graph recovery
Frozen primary source: Dittrich, Schnetter, Seth, Steinhaus, arXiv:1609.02429v2.

Allowed operations: download the exact-version e-print and/or PDF; hash it; unpack source without executing untrusted source; locate the unique source environment corresponding to Eq.(27) by equation-number/adjacent-text evidence; extract the complete TikZ/source environment and immediately adjacent normalization text; optionally render the exact source or PDF page to an image. A source-derived graph AST/edge list is admissible only if every edge/node comes mechanically from the frozen source environment and the mapping to Eq.(27) is unambiguous.

PASS predicate for the lane: exact source provenance + unambiguous Eq.(27) environment + complete graph connectivity sufficient to state which q-CG/dual objects are contracted. BLOCKED if equation identity or connectivity remains ambiguous. No diagram may be reconstructed from memory or prose alone.

### Lane B - independent even-k category convention qualification
Frozen independent cross-check: T. V. Zache, D. Gonzalez-Cuadra, P. Zoller, arXiv:2304.02527v2, supplemental material "Facts about SU(2)_k".

Required predicates: source states `q = exp(2*pi*i/(k+2))` with k a positive integer; finite labels through k/2; fusion constraints including j1+j2+j3 <= k; q-number convention; F-matrix/q-6j convention; and an internal orthogonality/unitarity statement. The source must not impose an odd-k restriction on these displayed formulas. This lane may qualify the even-k fusion/category convention, including k=12, but does not by itself qualify a q-CG component phase convention unless the source explicitly supplies one.

### Lane C - byte/provenance reproducibility
Frozen archives: arXiv:1609.02429v2, 1312.0905v2, 1506.04749v3, and 2304.02527v2.

For the first three, freshly downloaded e-print SHA256 values must be compared with the historical ITER014 hashes:
- 1609.02429v2 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`
- 1312.0905v2 `69334656117892b255ebb9b0c3855b6387bafc630bb9345b084e5434e22294c0`
- 1506.04749v3 `758e05bf73390015fb02f374c69892ad155c8edacb40a97876c12aa7f64c1e14`
Record the fresh hash of 2304.02527v2. A hash mismatch is provenance-significant and must be reported, not normalized away.

## Cross-lane synthesis rule
Only after lanes A and B complete may the checkpoint ask whether target Eq.(27), together with Appendix-B source-defined duality and the independent even-k category check, is sufficiently convention-pinned to authorize a *separate* bounded q-CG implementation-validation preregistration.

Authorization requires all of:
1. Lane A PASS with exact graph connectivity;
2. target Appendix-B dual pairing remains compatible with that exact graph;
3. Lane B PASS for even k at category/fusion level;
4. no new source-level convention contradiction;
5. provenance lane does not invalidate the frozen target bytes.

A PASS may authorize only the next bounded implementation-validation preregistration. It does **not** authorize Iter012, Eq.(29)/Lambda amplitude work, phase fitting, alpha selection, bridge credit, candidate theory, RQIR/KMQGB promotion, or a new-physics claim.

## Fixed terminal classes
- `RC006_EQ27_GRAPH_AND_EVENK_CATEGORY_PINNED_IMPLEMENTATION_PREREG_ALLOWED`
- `RC006_EQ27_GRAPH_PINNED_EVENK_COMPONENT_CONVENTION_STILL_PARTIAL`
- `RC006_EQ27_GRAPH_SOURCE_BLOCKED`
- `RC006_EVENK_CATEGORY_SOURCE_BLOCKED`
- `RC006_PROVENANCE_MISMATCH_REQUIRES_REAUDIT`
- `RC006_CONVENTION_INCOMPATIBLE_SCOPED`

## Execution discipline
Use separate GitHub Actions matrix jobs where practical so lanes run in parallel. Each lane must emit a machine-readable evidence JSON and a plain-text/Markdown evidence file. The aggregate job may synthesize only after all lanes complete and must preserve lane-specific failures. Green CI is not scientific PASS unless predicates in the evidence files pass.

Administrative readiness values remain unchanged during this checkpoint. Historical ITER013-017 classifications are immutable.