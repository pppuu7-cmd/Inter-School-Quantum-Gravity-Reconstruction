# Iteration 006 / RC006 — Eq.(29) ↔ Appendix-B B14/B16 source-reduction topology

## Preregistration

This gate is frozen before implementation/production. It follows only after terminal run `34721521848` established `EQ29_ARC_AWARE_NO_PROPER_CROSSING` on the immutable Eq.(29) source block at both 80 and 120 decimal digits. The R/R^-1 convention is therefore not geometrically applicable to this immutable block; this does **not** itself reconstruct the Eq.(29) amplitude.

Pinned source: arXiv `1609.02429v2`, source-bundle SHA256 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

Immutable Eq.(29) EPRL block SHA256: `4f505657a580216d176c1c63ec92f5614dc73e8113294722a854d5a350b67083`.

## Scientific question

Does the literal planar spin-network graph appearing in Eq.(29) have the same source-level **unlabeled trivalent graph topology** as the Appendix-B nine-edge graph reduced in Eqs. (B14)–(B16), and is the B14/B16 reduction source text uniquely extractable? This is a prerequisite for using the already validated B13 q-6j convention to reconstruct the Eq.(29) bracket without arbitrary contraction ordering.

## Frozen lanes

Three independent lanes, `fail-fast:false`:

1. `eq29_graph`: extract only the immutable Eq.(29) `\\draw` geometry; reconstruct every straight/arc primitive under TikZ endpoint semantics; ignore geometric crossings as vertices; merge source-identical endpoints; suppress degree-2 bend vertices to obtain the logical graph. Record vertex/edge counts, degree multiset, cycle rank, adjacency and the nine distinct normalized spin labels. No image/OCR input.
2. `b14_graph`: in active TeX, require exactly one occurrence of the exact semantic anchor `A diagram worth mentioning is the following`; extract the first subsequent TikZ picture before the B15 discussion; reconstruct and degree-2-suppress its logical graph by the identical algorithm. Require the source diagram to expose generic labels `j_1,...,j_9` (TeX-normalized) without inventing synonyms.
3. `b16_source`: within the same Appendix-B neighborhood, require a unique active source segment containing the B16 reduction and exactly two source q-6j bracket objects produced by the B15 reduction chain. Record a SHA256 of the extracted source segment and the literal generic label set used by its two 6j factors. No numerical evaluation is performed here.

## Frozen comparison

The aggregate may return source-reduction topology PASS only if:

- all three lanes are valid;
- Eq.(29) and B14 logical graphs are isomorphic as simple multigraphs after degree-2 suppression;
- both have six trivalent logical vertices, nine logical edges and cycle rank four;
- Eq.(29) has exactly nine distinct normalized spin variables `{J^-,J^+,l,j,l_1,l_2,j^+_1,j^-_1,j^+_2,j^-_2}` after duplicate occurrences are collapsed to nine distinct names (i.e. exactly nine distinct variables; the explicit set is checked from source, not inferred from geometry);
- B14/B16 exposes exactly the nine generic variables `j_1,...,j_9`;
- the B16 source lane confirms two q-6j bracket factors in the extracted reduction segment.

No mapping from generic `j_i` to Eq.(29) labels is fitted in this gate.

## Frozen classifications

- `EQ29_B14_B16_SOURCE_REDUCTION_TOPOLOGY_QUALIFIED`: all criteria above pass. This authorizes only a separately preregistered **label-edge mapping / B16 expression transport** gate. It does not authorize numerical Eq.(29) amplitude evaluation.
- `EQ29_B14_TOPOLOGY_MISMATCH`: valid source objects but logical graphs are not isomorphic or the frozen 6V/9E trivalent signature fails. Scientific scoped negative result for this reduction route only.
- `EQ29_B16_SOURCE_REDUCTION_NOT_MACHINE_QUALIFIED`: graph topology is compatible but the frozen B16 source extraction/two-6j criterion fails. BLOCKED; no guessed formula.
- `INVALID_SOURCE_OR_IMPLEMENTATION`: source hash/anchor/parser validity fails. Infrastructure/implementation failure, not scientific evidence.

## Claim locks

`eq29_amplitude_authorized=false`, `bridge_credit=false`. No arbitrary graph-label selector, contraction order, counterterm, R-placement, post-hoc threshold change, `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, `ALL_KNOWN_SCHOOLS_FAIL`, or candidate-theory construction.
