# ITER156 preregistration — first-M/G endpoint coefficient identifiability

Date: 2026-09-17
Gate: `ITER156_FIXED_GEODESIC_FIRST_MG_ENDPOINT_COEFFICIENT_IDENTIFIABILITY`

## Frozen inputs

Use only repository authority already present before this preregistration: ITER118 endpoint basis, ITER126 pole-extraction prototype, ITER140/141/151 first-M/G general-d/contact strata, ITER153 distributional audit, ITER154B slot-6 closure, and terminal ITER155 authority-identification result. No basis, tensor projection, dimensional convention, subtraction prescription, threshold, or expected coefficient may be changed after seeing this gate.

## Question

Does the frozen authority contain enough independent, tensor-resolved endpoint pole equations to identify the divergent coefficients of the immutable ITER118 endpoint basis for the three first-M/G strata? This is an identifiability gate before any `B1_total` combination.

Endpoint basis is frozen as `R,S,DR,DS,BoxR,D2R,BoxS,D2S`. For each authoritative endpoint-pole relation, record which basis directions it resolves. Construct the exact rational incidence/projection matrix and compute its rank. A coefficient is derivable only if its basis direction is uniquely constrained by source-faithful equations; absence of an equation is not a zero coefficient.

## Frozen adjudication

A. lineage files present.
B. endpoint basis exactly the eight ITER118 curvature directions above.
C. only explicit pre-preregistered endpoint residue/projection equations may enter the matrix.
D. exact rank and nullspace are reported.
E. PASS only if all coefficient directions needed by the three first-M/G endpoint strata are uniquely identifiable; otherwise `BLOCKED_SCOPED_ITER156_ENDPOINT_COEFFICIENTS_UNDERDETERMINED` with exact missing/null directions.
F. no null direction may be assigned coefficient zero.
G. no `B1_total`, bridge, new-physics, or candidate-theory claim.

A BLOCKED result is scientifically valid and must not be repaired by adding equations after inspecting the nullspace. A successor may add new source-faithful equations only under a new prospective preregistration.
