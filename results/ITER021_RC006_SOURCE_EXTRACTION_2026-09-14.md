# ITER021 — RC006 Eq.(27) source extraction checkpoint

Date: 2026-09-14
Preregistration commit: `1e6574aa6fcf5aaf2f245abf9ad9cdc0c43b6574`
Source-extraction run: `34785463210`
Job: `103800021974`
Artifact: `10326272007`
Artifact ZIP SHA256: `2bdab37917744ae8ce231c7299d702ffc1b98e1cffdd04e0bf8f848ee11f40a3`

## Terminal classification

**`RC006_EQ27_SOURCE_EXTRACTION_BLOCKED`**, specifically because the preregistered source-number benchmark provenance predicate was false.

This is not a scientific failure of Eq.(27), Appendix E, the q-CG solver, or the EPRL construction. The exact primary source bytes and all required graph/formula environments were recovered successfully. The blocker is that the four numerical sentinels introduced in the ITER021 preregistration are not literal values in the byte-pinned primary source and are not present in the historical ITER012 preregistration or current repository history. They therefore cannot be used as a source-faithful benchmark.

## What passed

Fresh arXiv:1609.02429v2 e-print SHA256 exactly reproduced the frozen value:

`3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

The extraction found exactly one Eq.(27) source display, `\label{eq:eprl-3-valent}`, in `bc-spin-nets.tex`.

The exact target source sections were recovered for:
- Appendix-A quantum-group basics / admissibility / completeness / orthogonality;
- Appendix-B `Diagrammatic Calculus`, including cap/cup, qbar duality, 4-valent basis/dual, and graphical identities;
- Appendix-E `Normalisation of EPRL model` (`app:EPRL-norm`);
- Appendix-F / EPRL construction and derivation contexts.

Appendix E explicitly gives the final closed-graph reduction

`(-1)^(sum_i(j_i^+ + j_i^-) - 2 l) * (d_l1 d_l2 d_l3 d_l4)^(-1) * d_l^(-2) * delta_(l l')`

and the corresponding normalization constant

`c_{l} = (-1)^(sum_i(j_i^+ + j_i^-) - 2 l) * d_l1 d_l2 d_l3 d_l4 * d_l^2`,

followed by the source normalization-family choice

`c_{l} = (-1)^(...) * (d_l1 d_l2 d_l3 d_l4)^alpha * d_l^2`.

The k=12 source context is also explicit: for gamma=1/3, the nontrivial simplicity maps include `l=3 -> (j^+,j^-)=(2,1)` and `l=6 -> (4,2)`; the source identifies k=12 as the smallest level where the normalization exponent alpha matters nontrivially in this model.

## What failed and why it is not repaired here

The preregistration demanded exact source occurrences of four numerical values:
`7.41492`, `1.399277`, `-1.931582`, `-3.861564`, plus a claimed k=12 l=3 cancellation benchmark.

None of those four numbers occurs in the exact arXiv TeX or parsed PDF text. They also do not occur in the historical ITER012 preregistration, whose frozen inputs are k={6,10,12}, alpha=0 and source-faithful q-CG/contraction predicates. Repository code search finds no independent provenance record for those numbers.

The exact primary source instead states that at k=12, gamma=1/3 the l=3 map is a nontrivial allowed map `3 -> (2,1)`; no source claim of a general vanishing l=3 EPRL contribution was located in this checkpoint.

Therefore those numerical predicates are withdrawn from future authority, but **not silently removed from ITER021**. ITER021 remains BLOCKED under its own frozen preregistration.

## Handoff

A new prospectively registered checkpoint may use only the recovered source-grounded identities: Appendix-B q/qbar duality and 4-valent basis/dual contraction, Appendix-E closed-graph E3 reduction, and the k=12 gamma=1/3 simplicity map. It must not inherit the unsupported numerical sentinels.

No TNR, Eq.(29)/Lambda, alpha selection, bridge credit, candidate theory, or new-physics claim was executed or authorized in ITER021.