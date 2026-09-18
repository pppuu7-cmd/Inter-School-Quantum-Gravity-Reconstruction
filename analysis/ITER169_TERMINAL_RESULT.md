# ITER169 terminal result — upstream source trace

Date: 2026-09-18.

## Frozen-gate adjudication
Authoritative execution: commit `b6cf6e9e1c81ce1d36bdc4adfae1dbbf4b2e3ab7`, run `35332355807`.

The workflow was technically green, but the frozen source-chain hypothesis did not pass. The trace lane mechanically found `A_163_imports_161=true`, `B_163_calls_upper=true`, `C_161_imports_140=true`, `D_upper_calls_g2=true`, `E_upper_calls_dr1=true`, `G_140_G_family=true`, `H_G1_calls_g2=true`, while the preregistered `F_upper_calls_r1` was `false`. Therefore the scientific classification is **`SCIENTIFIC_FAIL_ITER169_SOURCE_CHAIN_CONTRADICTED`**. The criterion is not changed after seeing the result.

The failure is informative rather than infrastructural. Inspection of the executable ITER161 implementation shows the actual endpoint asymmetry: `upper_open_vertex` directly uses `dr1_real` and `g2_real`, with the q-side `r1_tensor` supplied later when reconstructing the full G1 value; `lower_open_vertices` directly uses `r1_tensor` and `g2_real`, with the k-side `dr1_real` supplied later in reconstruction. Thus a source-faithful term-to-geometry map must follow the actual AST/call graph rather than require the same primitive calls inside both endpoint helper functions.

## Provenance
- trace job `105559335881`; artifact `10541257141`; ZIP SHA256 `795e62df3dce808833b3a5f46d1490dbc8c99d95359115642fb1f0c01dab96c1`; classification `SCIENTIFIC_FAIL_ITER169_SOURCE_CHAIN_CONTRADICTED`.
- geometry job `105559335718`; artifact `10541761549`; ZIP SHA256 `1908f85cf62c5c8c39cb06984dd15586487253514243298b610cf78ac459b4c4`; scoped subcheck passed for executable affine Wick/endpoint geometry.
- critic job `105559335960`; artifact `10541641399`; ZIP SHA256 `9d97c4b2c83ca9f68b5766b1d36b3de94038b53ea5f0b89944898e0ae6bfbe95`; scoped subcheck passed for orientation/contact preservation.

## Scientific status
ITER163 source-complete 21-term tensor bookkeeping/K-divisibility remains intact. ITER164-168 negative/blocking results remain intact. ITER169 does not establish a source-qualified singular-sector manifest and gives no Laurent/R-operation, ITER118 matching, `B1_total`, bridge credit, or candidate-theory authorization.

Overall programme remains **50%**. Candidate theory remains **0% / UNFORMED**. Bridge credit remains **0**.

## Exact next admissible gate
Prospectively freeze **ITER170 corrected-call-graph / term-to-geometry provenance gate**. For every one of the frozen ITER163 terms/classes, mechanically recover the actual AST/call path into ITER161/ITER140 primitives and separately attach the executable ITER141/ITER143 affine Wick denominator/contact geometry. The gate must preserve upper/lower endpoint asymmetry, cancelled-propagator contacts, and exact term identity. Run independent producer, endpoint-asymmetry critic, and completeness/null critic lanes. Only a scoped PASS may authorize rebuilding the singular-sector manifest; no scaling-degree/R-operation/Laurent/ITER118/B1/bridge/candidate-theory credit follows directly.