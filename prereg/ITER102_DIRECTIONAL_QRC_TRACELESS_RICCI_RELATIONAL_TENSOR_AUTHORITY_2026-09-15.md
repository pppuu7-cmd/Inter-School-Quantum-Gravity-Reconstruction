# ITER102 preregistration — directional QRC traceless-Ricci ↔ relational tensor authority

Date: 2026-09-15
Gate: `ITER102_DIRECTIONAL_QRC_TRACELESS_RICCI_RELATIONAL_TENSOR_AUTHORITY`

## Motivation

ITER101 established that the directionally averaged leading small-`delta` QRC term closes onto scalar curvature. Before averaging, the same source formula carries additional directional information through `Ric(v,v)`. Subtracting the scalar average may isolate a traceless-Ricci channel independent of the scalar one.

## Frozen sources

- arXiv:1802.10524 — D=4 directional QRC smooth expansion.
- arXiv:2112.02118 — physical-coordinate relational observables and FRG composite flow.
- arXiv:1611.06522 — generic FRG composite-operator formalism.
- ITER101 only as prior coefficient/type authority.

## Frozen question

Does the leading direction-dependent part of the smooth 4D QRC expansion isolate `S_ij v^i v^j`, where `S_ij = Ric_ij - (R/4) g_ij`, and does the frozen FRG relational-observable framework source-define a physical-frame tensor route strong enough to type this object without collapsing it to scalar curvature?

## Required predicates

A. The scalar-average subtraction must algebraically cancel the explicit `R` term and leave a fixed coefficient multiplying `Ric(v,v)-R/4`.

B. The result must be independent of CDT target data and finite-radius fits.

C. The FRG relational formalism must explicitly allow physical components/contractions of tensor fields in a dynamical physical coordinate frame.

D. An explicit relational Ricci-tensor/traceless-Ricci composite flow counts as full PASS; generic statements that other tensors can be handled count only as a formal route.

E. The QRC direction `v` must be mapped conceptually to a physical tangent direction in the relational frame; coordinate-axis substitution without a physical frame is forbidden.

F. Small-`delta`, smooth-manifold and renormalized-normalization ceilings from ITER101 remain active.

G. No finite-radius CDT anisotropy/isotropy data may be used to select the tensor structure.

## Frozen classifications

- `PASS_SCOPED_EXPLICIT_TRACELESS_RICCI_RELATIONAL_COMPOSITE_MAP` if A-E pass with an explicit flowed relational tensor composite.
- `PASS_SCOPED_TRACELESS_RICCI_QRC_CHANNEL_FORMAL_RELATIONAL_TENSOR_ROUTE_FLOW_OPEN` if A-C/E pass but D is only formal/generic.
- `PASS_SCOPED_DIRECTIONAL_QRC_CHANNEL_ONLY_FRG_TENSOR_ROUTE_BLOCKED` if A-B pass but the FRG tensor route is not source-qualified.
- `FAIL_SCOPED_TRACELESS_DECOMPOSITION_INVALID` if A fails.

## Controls

- `SCALAR_COLLAPSE_CONTROL`
- `COORDINATE_DIRECTION_SWAP_CONTROL`
- `GENERIC_TENSOR_EXPLICIT_FLOW_CONTROL`
- `FINITE_RADIUS_PROMOTION_CONTROL`
- `TARGET_ANISOTROPY_FIT_CONTROL`

## Claim ceiling

A PASS can establish only an asymptotic directional operator-type route. It cannot establish measured CDT isotropy, an Einstein space, a finite-radius QRC tensor equality, a unique FRG trajectory/fixed point, `BRIDGE_DERIVED`, new physics, or a candidate theory.