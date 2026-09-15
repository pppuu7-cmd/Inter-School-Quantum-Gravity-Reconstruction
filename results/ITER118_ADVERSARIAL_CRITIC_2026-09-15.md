# ITER118 adversarial critic — line/endpoint counterterm power counting

Date: 2026-09-15
Gate: `ITER118_FIXED_GEODESIC_CURVATURE_LINE_ENDPOINT_COUNTERTERM_POWER_COUNTING`
Preregistration: `29eadfb45f0d2966262d9a34e648db55353e708b`
Source authority: `e3fd7bec52807bed587d91e8c43a9cc60534b550`

## Attack 1 — extrinsic-curvature / acceleration defect operators are missing

For the frozen observable the reference path is a smooth geodesic. Its covariant acceleration vanishes in the background construction, so line scalars built from geodesic acceleration are zero/redundant at the operator order used to define the counterterm basis. Endpoint variations of the path are already represented by the geodesic embedding sector and endpoint/tangent operators.

A cusped or piecewise-geodesic observable would require additional cusp data and is outside this gate.

## Attack 2 — Riemann/Weyl tensors add independent dimension-2 line scalars

With only the metric and one unit tangent available, a scalar linear in one Riemann tensor reduces to `R` and `R_nn`; four-tangent Riemann contractions vanish by antisymmetry and Weyl traces vanish. No third independent dimension-2 scalar is exposed.

## Attack 3 — the dimension-4 endpoint basis may be overcomplete or incomplete

The listed basis is deliberately a convenient linearized flat-background spanning set. Contracted Bianchi identities reduce mixed divergences of Ricci to derivatives of `R`; commutators of covariant derivatives are nonlinear in curvature and are beyond the retained linear sector. Some combinations may still be algebraically redundant, but this can only reduce the basis; it does not generate an infinite new sector.

## Attack 4 — higher derivatives multiplied by powers of l create an infinite allowed tower

Engineering dimension alone would permit this, but one-loop superficial divergence order does not. The gravitational/matter source template generates at most the standard one-loop increase to four-derivative local structures at the frozen order. Operators with arbitrarily many derivatives would correspond to higher EFT order rather than counterterms required by the `O(G^2)` divergence structure.

This is the most important scope assumption: the finite basis is valid at the chosen one-loop/derivative order, not as an exact nonperturbative statement.

## Attack 5 — arbitrary tau-dependent weights are allowed on a finite segment

Finite nonlocal definitions can certainly contain such weights, but ultraviolet **counterterms** are constrained by locality on the defect. Interior divergences are local densities; endpoint-sensitive singularities are distributions supported at endpoints and map to the endpoint basis. Arbitrary smooth `f(tau)` finite deformations would define a different observable, not be forced by local UV subtraction.

## Attack 6 — identity/perimeter line counterterms were omitted

They may renormalize overall defect normalization/perimeter conventions. At this order their action on the curvature correlator is equivalent to multiplicative/identity sectors whose lower-order separated `RR` piece is contact-only. They do not introduce a new independent curvature/tangent channel for `B_0/B_1`, but should be retained in full normalization bookkeeping.

## Attack 7 — line integrals of D R and D S may not be pure endpoints once the metric fluctuates

At the **counterterm classification level** the line density is evaluated covariantly along the geodesic and `D=n.nabla`; for a scalar `R`, integrating `D R` is exactly a boundary difference. For `S=R_mn n^m n^n`, parallel transport of `n` along the geodesic makes the same statement hold up to curvature-nonlinear corrections, which are beyond the linear sector. Thus the reduction is consistent at frozen order.

## Attack 8 — endpoint-local operators with explicit 1/l factors might generate separated tails

Their correlation with the anchor at the linearized tree level remains a distribution supported at endpoint coincidence; multiplying by a smooth function of nonzero `l` does not turn that support into a bulk radial tail. By contrast, line operators have an integration over the defect and can generate endpoint-divergence renormalization whose finite coefficient carries explicit `l` dependence; retaining them is the conservative choice.

## Critic verdict

**CONFIRMS `PASS_SCOPED_FINITE_LINE_ENDPOINT_COUNTERTERM_BASIS_POWER_COUNTING_CLOSED`** within the frozen one-loop/linear-curvature/derivative-order scope.

The next best reduction is to project the four line operators onto the scalar RR channel and compute their tree-level/UV mixing rank before evaluating loop residues.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.