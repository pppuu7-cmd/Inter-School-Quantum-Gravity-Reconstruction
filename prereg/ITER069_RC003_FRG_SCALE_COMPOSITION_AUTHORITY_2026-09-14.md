# ITER069 preregistration — RC003 FRG scale/composition authority

Date: 2026-09-14
Gate: `ITER069_RC003_FRG_SCALE_COMPOSITION_AUTHORITY`

## Frozen question
Does the source-qualified EAA/FRG realization provide an explicit physical coarse-graining/composition map whose domain, codomain, regulator/measure dependence, gauge/background structure and composition law are sufficiently defined to compare with typed ISQGR composition objects, without identifying RG scale evolution with temporal gluing or tensor contraction by analogy?

## Frozen sources
- arXiv:2302.14152 — FRG in Quantum Gravity review
- arXiv:2606.21522 — Asymptotically safe quantum gravity review
- arXiv:2110.09566 — scalar-tensor asymptotic-safety realization

## Required authority predicates
A. Exact EAA/Wetterich flow object is explicitly defined.
B. Domain/codomain of the scale evolution is identifiable as effective actions/functionals/couplings at scales k, not physical spacetime states unless source explicitly states otherwise.
C. Regulator insertion and regulator dependence are explicit.
D. Gauge fixing/background-field or equivalent gravitational structure is explicit enough to prevent representation erasure.
E. Source specifies whether finite k1->k2 evolution has an exact source-defined composition/semigroup/coarse-graining law; absence must be recorded, not filled by analogy.
F. Fixed-point/trajectory information is separated from a physical refinement map on states/geometries.
G. No identification with CDT proper-time composition, HaPPY tensor contraction, or EPRL refinement is allowed without an explicit typed map.

## Frozen classification
- `PASS_SCOPED_FRG_SCALE_OPERATION_QUALIFIED` only if A-D and F are source-qualified; E may establish either an explicit finite composition law or a scoped absence, but must be adjudicated exactly.
- `BLOCKED_SOURCE_AUTHORITY` if the exact mathematical objects needed for A-D cannot be established from the frozen stack.
- `INFRASTRUCTURE_FAIL` only for extraction/transport failure.
- Any green CI is only `SOURCE_CANDIDATES_REQUIRE_MANUAL_EQUATION_AUDIT` until manual audit.

## Claim ceiling
No bridge credit. No universal common parent. No candidate theory. No claim that FRG scale flow is physical refinement, temporal composition, or tensor-network composition unless an explicit source-defined typed equivalence is found.

## Controls
- `RG_TIME_SWAP_CONTROL`: replacing k-flow with physical proper time must fail unless source-defined.
- `REGULATOR_ERASURE_CONTROL`: dropping R_k dependence cannot count as equivalence.
- `TRUNCATION_FULL_THEORY_CONTROL`: EH/scalar-tensor truncation cannot be promoted to full theory.
- `FIXED_POINT_REFINEMENT_CONTROL`: a fixed point alone is not a refinement map.

Thresholds and predicates are frozen prospectively before source extraction.