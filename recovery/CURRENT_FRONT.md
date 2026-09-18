# Current front — ISQGR

Date: 2026-09-18.

Overall scientific programme: **50%**. Candidate theory: **0% / UNFORMED**. Bridge credit: **0**.

## ITER169 — terminal SCIENTIFIC FAIL
Authoritative execution: commit `b6cf6e9e1c81ce1d36bdc4adfae1dbbf4b2e3ab7`, run `35332355807`.

Trace job `105559335881`, artifact `10541257141`, ZIP SHA256 `795e62df3dce808833b3a5f46d1490dbc8c99d95359115642fb1f0c01dab96c1`; geometry job `105559335718`, artifact `10541761549`, SHA256 `1908f85cf62c5c8c39cb06984dd15586487253514243298b610cf78ac459b4c4`; critic job `105559335960`, artifact `10541641399`, SHA256 `9d97c4b2c83ca9f68b5766b1d36b3de94038b53ea5f0b89944898e0ae6bfbe95`.

Classification: **`SCIENTIFIC_FAIL_ITER169_SOURCE_CHAIN_CONTRADICTED`**. CI was technically green. The frozen trace hypothesis failed because `upper_open_vertex` does not itself call `r1_tensor`. The executable code instead has asymmetric endpoint primitive placement: upper directly uses `dr1_real + g2_real` and receives the q-side `r1_tensor` in reconstruction; lower directly uses `r1_tensor + g2_real` and receives k-side `dr1_real` in reconstruction. Geometry and orientation/contact lanes passed only as scoped subchecks.

ITER163 21-term source-complete tensor bookkeeping/K-divisibility remains intact; ITER164-168 negative/blocking results remain intact. No singular-sector manifest, Laurent/R-operation, ITER118 matching, `B1_total`, bridge credit or candidate theory follows.

## ITER170 — exact next admissible gate
Prospectively freeze a corrected-call-graph / term-to-geometry provenance gate. Mechanically recover the actual AST/call path for each frozen ITER163 term/class into ITER161/ITER140 primitives, and independently attach executable ITER141/ITER143 affine Wick denominator/contact geometry. Do not require a false symmetric primitive placement between upper and lower endpoints.

Run independent lanes for (A) term-to-primitive producer, (B) endpoint-asymmetry/orientation/contact critic, and (C) completeness/null critic. Every credited mapping must have executable file/function provenance and preserve exact term identity; prose labels are not evidence. A scoped PASS only authorizes rebuilding the source-qualified singular-sector manifest. It does not authorize scaling-degree/R-operation, Laurent extraction, ITER118 matching, `B1_total`, bridge credit or candidate theory.

## Persistent locks
`B1_total = UNAUTHORIZED`; `ALL_KNOWN_SCHOOLS_FAIL=false`; `NEW_QG_THEORY_REQUIRED=false`; `NEW_PHYSICS_FOUND=false`; `BRIDGE_DERIVED=false`; `ITER118_MATCHING_AUTHORIZED=false`. Candidate theory remains **UNFORMED / 0%**.

RC-009 remains scoped blocked; Lorentzian Delta4 negative results remain preserved without bridge credit absent genuine refinement.
