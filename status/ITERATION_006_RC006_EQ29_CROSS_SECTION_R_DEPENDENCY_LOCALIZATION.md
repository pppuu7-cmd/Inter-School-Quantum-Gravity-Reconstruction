# Iteration 006 / RC006 — Eq.(29) cross-section R-dependency localization

## Status
Prospectively preregistered before implementation/production. This is a **diagnostic-only** follow-up to terminal run `34721872311 = EQ29_APPENDIX_F_CHAIN_INCOMPLETE`. It cannot revise that frozen result to PASS.

Pinned source: arXiv `1609.02429v2`; source bundle SHA256 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

## Scientific object
Determine where, in the active TeX source, the source-global R/R^{-1} convention connects to the exact objects referenced by Appendix F, using only literal TeX labels/refs and source offsets. No lexical synonym is allowed to create graph edges; semantic text is used only to locate R-definition neighborhoods, not to infer an edge.

## Frozen independent lanes (`fail-fast:false`)
1. `r_global`: enumerate every active literal `\\mathcal{R}` / `\\mathcal{R}^{-1}` defining formula and every `R-matrix` text occurrence. For each, record all labels and refs in a fixed ±5000-character source neighborhood.
2. `appendix_f_refs`: extract unique Appendix-F source segment, enumerate its exact refs, resolve each ref to its unique active label definition, and record source offsets/hashes. The known refs `eq:identity1` and `eq:EPRL-formula` are not hard-coded as a PASS requirement; the lane reports whatever exact active source contains.
3. `exact_ref_graph`: construct a directed graph whose only edges are literal `\\ref{X}`/`\\eqref{X}` occurrences from the smallest containing labeled structural block to label `X`. Add no synonym/nearby-text edges. Record whether any Appendix-F-referenced label and any label in an R-definition neighborhood lie in the same exact-ref connected component, and record shortest exact label paths if they exist.

## Frozen classifications
Aggregate is valid only if all lanes parse the pinned source deterministically.
- `EQ29_R_DEPENDENCY_EXACT_REF_PATH_LOCALIZED`: at least one exact label/ref path links an Appendix-F referenced object to an R-neighborhood labeled object.
- `EQ29_R_DEPENDENCY_SOURCE_NEIGHBORHOOD_ONLY`: R source neighborhoods and Appendix-F refs are both uniquely localized, but no exact label/ref path connects them.
- `EQ29_R_DEPENDENCY_AMBIGUOUS_MULTIPLE_PATHS`: multiple incompatible exact-ref paths/components prevent a unique dependency localization.
- `INVALID_SOURCE_OR_IMPLEMENTATION`: source/hash/parser validity failure only.

## Interpretation locks
This diagnostic has `scientific_credit=0`, `eq29_amplitude_authorized=false`, `bridge_credit=false`. Even `...EXACT_REF_PATH_LOCALIZED` does not override `34721872311`; it may only support a new prospectively frozen derivation-composition gate whose object is explicitly different from the failed Appendix-F-contained-R criterion. No fitted contraction order, no additional final-block R crossing, no threshold/source-block retuning, no bridge/new-physics/new-theory claims.
