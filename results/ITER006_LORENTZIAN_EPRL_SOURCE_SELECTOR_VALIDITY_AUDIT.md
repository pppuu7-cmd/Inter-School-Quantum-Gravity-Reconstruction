# ITER006 — Lorentzian EPRL source-selector validity audit

Date: 2026-09-12

## Preserved failed gate

The frozen leave-one-anchor source-lock run `34701317882` remains `SOURCE_EQUATION_SELECTION_ROBUSTNESS_FAIL` with only 2/8 stable targets. Numerical two-vertex implementation remains unauthorized.

## Additional validity finding

Inspection of the two nominally stable artifacts shows that **selection stability is not sufficient for semantic correctness**:

- `full_amplitude` selected hash `963e6a9df1e6ee0468f212308dd65901e1851af5518eabfc18393500ccd9fd33`, labelled `B3InhomLim`. The selected object is an asymptotic large-spin scaling relation for booster functions, not a full-amplitude definition.
- `correlation_observable` selected hash `01bee2ae0c4b3455c9b9fd3a69af23a4c7c9fa1d7d6cf3557bdab86897ae5d2e`, labelled `giorgio`; structurally it is a correlation/cutoff sum and is semantically compatible with that target.

The old selector concatenated all `.tex` files before measuring proximity, so file identity was not part of the frozen nearest-object metric. Because the gate already failed, this does not rescue or reverse any result; it establishes an additional **method-validity reason not to implement from the old selector**.

## Source-authored label diagnostics

Run `34702507649` found broad lexical ambiguity for all six unstable targets (distinct selected math objects: 13, 13, 4, 8, 5, 10). Two targets, `two_vertex_amplitude` and `cutoff_or_truncation`, independently resolved the same source-authored mathematical label `decaffeinato`, exact hash `b6cfed3b44137175935857587f1b577fdd843aa720ec1d01edeb7aa385f84c46`.

Run `34702654029` confirmed that `decaffeinato` is owned by a standard `equation` environment in `2VertexDipoleV2.tex`, section `Boxes and Integrations`, around line 1799. The two-vertex amplitude context contains a source-authored `\\ref{decaffeinato}` around line 493. The other four unstable targets did not expose a standard math-owner through the current label-owner audit.

## Consequence

Do not construct a new 8/8 source lock from proximity or from the two nominally stable old selections. The permitted next step is a root-document equation/label registry and semantic source-object audit restricted to the actual paper root. A later source lock must be prospectively frozen from source-authored file/section/label identities before numerical results are inspected.

No amplitude reproduction, refinement map, bridge promotion, candidate theory or new-physics claim is authorized here.
