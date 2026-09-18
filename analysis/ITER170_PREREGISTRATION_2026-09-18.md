# ITER170 preregistration — corrected call graph / term-to-geometry provenance

Frozen prospectively on 2026-09-18 after terminal adjudication of ITER169 and before ITER170 execution.

## Question
Can the frozen ITER163 upper-endpoint source object be mechanically traced through the *actual* asymmetric ITER161/ITER140 executable call graph and attached to independently executable ITER141/ITER143 endpoint denominator/contact geometry, without prose inference or retuning the failed ITER169 hypothesis?

## Frozen requirements
Producer lane must establish from AST/source segments: ITER163 imports ITER161 and calls `upper_open_vertex`; `upper_open_vertex` calls `dr1_real` and `g2_real` but does **not** call `r1_tensor`; the ITER161 reconstruction supplies q-side `r1_tensor` outside `upper_open_vertex`; `lower_open_vertices` calls `r1_tensor` and `g2_real` but does **not** call `dr1_real`; lower reconstruction supplies k-side `dr1_real` outside the helper. It must also establish that ITER140 `G1_value` contains all three primitives and that ITER163 coefficients are sourced only from the upper open vertex.

Geometry lane must independently establish executable G-family occurrence coordinates, both Wick edges, affine phase, endpoint-zero computation, denominator `Q*K`, q/k shrinking-edge geometry and lower/upper singular labels from ITER141/ITER143.

Critic lane must falsify any accidental symmetric-call assumption, require distinct upper/lower primitive placement, require contacts to remain explicit, require no ITER118 solve/contact-zero convention, and require the ITER163 source path to remain upper-endpoint-only.

## Classification
All frozen lane requirements must pass for `PASS_SCOPED_ITER170_CORRECTED_CALL_GRAPH_AND_GEOMETRY_PROVENANCE`. Any contradicted required executable relation is `SCIENTIFIC_FAIL_ITER170_PROVENANCE_CONTRADICTED`; missing executable source is `BLOCKED_SCOPED_ITER170_SOURCE_INCOMPLETE`; infrastructure errors are separate.

A scoped PASS authorizes only rebuilding the source-qualified singular-sector manifest. It does **not** establish a distributional extension, scaling degree, Laurent pole tensor, ITER118 matching, `B1_total`, bridge credit, new physics, or candidate theory.

Thresholds/relations are frozen here and must not be changed after results are observed.