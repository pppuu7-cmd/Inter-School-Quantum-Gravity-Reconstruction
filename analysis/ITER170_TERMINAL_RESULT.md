# ITER170 terminal result — corrected call graph / term-to-geometry provenance

Date: 2026-09-18.

## Authoritative execution
- workflow head: `670909926098b0c2954b9a543c13c9b25cd7223c`
- run: `35341999003`
- producer job `105589775982`, artifact `10544789062`, ZIP SHA256 `f3358fd402ea37d712826fe9379183eea48a2cadec35f1a511a5e7af91f5202a`
- geometry job `105589776208`, artifact `10544854538`, ZIP SHA256 `6bd2627cb696b6d427b0f587ecd1c0574f7b2f4c172c64e70fe6b239f6740951`
- critic job `105589776261`, artifact `10545193455`, ZIP SHA256 `98c458c94a6119ad960d1c1c85a29ab8bb6b44279266c5d953bcbae359f6fd35`

## Scientific adjudication
Classification: **`PASS_SCOPED_ITER170_CORRECTED_CALL_GRAPH_AND_GEOMETRY_PROVENANCE`**.

This is a scientific scoped PASS under the prospectively frozen ITER170 preregistration, not merely green CI. Producer established all frozen asymmetric executable relations: ITER163 imports ITER161 and sources `upper_open_vertex`; upper directly uses `dr1_real + g2_real`, not `r1_tensor`, while reconstruction supplies q-side `r1_tensor`; lower directly uses `r1_tensor + g2_real`, not `dr1_real`, while reconstruction supplies k-side `dr1_real`; ITER140 `G1_value` contains all required primitives. Geometry independently established G occurrences, two Wick edges, affine phase, executable endpoint zeros, denominator `Q*K`, edge geometry and singular labels. Critic preserved endpoint asymmetry/orientation and explicit contacts, with no contact-zero convention or ITER118 solve.

## Claim ceiling
ITER170 authorizes only rebuilding a source-qualified singular-sector manifest from the now-correct executable provenance. It does not establish scaling degree, a distributional extension/R-operation, Laurent pole tensor, ITER118 matching, `B1_total`, bridge credit, new physics, or candidate theory.

ITER163 structural closure remains scoped. ITER164-169 negative/blocking results remain preserved; in particular ITER169 remains a genuine scientific failure of its frozen false symmetric source-chain hypothesis.

## Next admissible gate
ITER171: prospectively freeze and construct a source-qualified singular-sector manifest by mapping the frozen ITER163 term/classes through the corrected ITER170 primitive provenance onto executable ITER141/ITER143 denominator/endpoint geometry. Independently test completeness for endpoint zeros, intersections and contact sectors. No scaling-degree/R-operation/Laurent/ITER118/B1 work until ITER171 terminal adjudication.
