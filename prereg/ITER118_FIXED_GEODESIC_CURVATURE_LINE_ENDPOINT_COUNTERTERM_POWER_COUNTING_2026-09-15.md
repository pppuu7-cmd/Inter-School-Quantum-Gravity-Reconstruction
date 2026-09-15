# ITER118 preregistration — fixed-geodesic curvature line/endpoint counterterm power counting

Date: 2026-09-15
Gate: `ITER118_FIXED_GEODESIC_CURVATURE_LINE_ENDPOINT_COUNTERTERM_POWER_COUNTING`

## Motivation frozen before basis construction

ITER117 showed that the matter-scalar geodesic embedding counterterm `Z_chi` is separated-point inactive for `RR`, because the lower-order curvature correlator is contact-only. The remaining renormalization question is whether the curvature-decorated fixed geodesic admits a finite endpoint/line composite counterterm basis at `O(G^2)`.

ITER118 classifies **allowed operator sectors by symmetry and power counting**. It does not assume that every allowed counterterm is actually generated.

## Frozen setup

- flat four-dimensional Euclidean background;
- a single geodesic segment of physical length `l` with unit tangent `n^mu`;
- scalar-curvature insertion at an endpoint and scalar-curvature insertion at the anchor;
- one-loop / `O(kappa^4)=O(G^2)` correlator;
- diffeomorphism-covariant local geometric ingredients, with reparameterization-invariant line integration;
- no additional physical mass scale.

## Required predicates

A. At one loop, counterterm corrections to a curvature insertion which can contribute through `O(kappa^4)` need only be linear in the fluctuating curvature/metric for their tree contraction with the other leading curvature insertion; nonlinear curvature counterterms start beyond the relevant Gaussian order unless accompanied by additional interactions.

B. The one-loop gravitational/composite superficial derivative order bounds the required local linear-curvature defect operators to mass dimension `<=4` (curvature plus at most two additional derivatives) at the frozen order.

C. Endpoint-local scalar operators may use the physical tangent `n^mu`; enumerate independent sectors modulo Bianchi identities, total derivatives and contact-only redundancies.

D. Interior line counterterms must be reparameterization-invariant integrals of local scalar defect densities. UV locality along a smooth geodesic should restrict interior coefficients to local densities; endpoint singularities are represented separately by endpoint operators rather than arbitrary functions of the affine parameter.

E. The basis must include the lowest curvature/tangent scalars `R` and `R_nn := R_mn n^m n^n`, plus all derivative descendants permitted by B.

F. Explicit powers of `l` required by engineering dimension are allowed, as in the known `Z_chi ~ kappa^2/l^2` counterterm, but they must not introduce a second independent physical scale.

G. Classify which sectors can in principle affect the separated `B_0/B_1` radial coefficients and which are guaranteed to remain pure contact in the anchored `RR` correlator.

H. A full PASS requires a finite basis/category decomposition; it does not require computing pole residues.

I. No EDT data may be used to select operators or finite renormalization conditions.

## Frozen classifications

- `PASS_SCOPED_FINITE_LINE_ENDPOINT_COUNTERTERM_BASIS_POWER_COUNTING_CLOSED` if A-I give a finite complete category basis at the frozen order.
- `PASS_SCOPED_FINITE_CATEGORY_BASIS_EXACT_TENSOR_REDUCTION_OPEN` if finiteness is established but some dimension-4 tensor descendants require an explicit algebraic reduction.
- `FAIL_SCOPED_COUNTERTERM_BASIS_NONCLOSED` if arbitrary functional/infinitely many defect operators are required already at `O(G^2)`.
- `BLOCKED_SOURCE_AUTHORITY` if superficial derivative order cannot be bounded.

## Controls

- `NONLINEAR_CURVATURE_ORDER_CONTROL`
- `ARBITRARY_TAU_WEIGHT_CONTROL`
- `TANGENT_SCALAR_COVARIANCE_CONTROL`
- `TOTAL_DERIVATIVE_ENDPOINT_CONTROL`
- `L_LENGTH_NEW_SCALE_CONTROL`
- `EDT_OPERATOR_SELECTION_CONTROL`

## Claim ceiling

A PASS establishes counterterm-basis finiteness only. It does not prove which operators diverge, determine `B_1`, establish noncancellation, authorize an EDT fit, or imply `BRIDGE_DERIVED`, new physics or a candidate theory.