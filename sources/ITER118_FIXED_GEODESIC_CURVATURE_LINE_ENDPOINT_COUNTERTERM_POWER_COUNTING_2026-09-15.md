# ITER118 source authority — fixed-geodesic curvature line/endpoint counterterm power counting

Date: 2026-09-15
Gate: `ITER118_FIXED_GEODESIC_CURVATURE_LINE_ENDPOINT_COUNTERTERM_POWER_COUNTING`
Preregistration: `29eadfb45f0d2966262d9a34e648db55353e708b`

## 1. Only the linear-curvature part of a one-loop counterterm can enter RR at O(kappa^4)

The target correlator has leading curvature insertions `R~kappa R_1+...`. A one-loop observable counterterm starts at `O(kappa^2)` relative to its classical operator.

A counterterm nonlinear in curvature, e.g. `kappa^2 R^2`, begins as `kappa^4 h^2`. Correlating it with the other leading `kappa R_1` insertion gives an odd Gaussian moment at `O(kappa^5)`; an additional interaction pushes it beyond the frozen `O(kappa^4)` calculation.

Therefore the counterterm sector relevant to `RR` through `O(G^2)` need only retain operators **linear in curvature/metric fluctuations**.

Predicate A: **PASS**.
`NONLINEAR_CURVATURE_ORDER_CONTROL`: **PASS_CONTROL**.

## 2. One-loop derivative order is finite

Ordinary one-loop gravitational EFT divergences add at most the curvature-squared / four-derivative local structures at this order. In the fixed-geodesic scalar precedent, the new geodesic divergences require embedding-coordinate renormalization and the standard finite set of one-loop matter/gravity counterterms; no infinite derivative tower is generated at the one-loop order.

For a curvature insertion already carrying two derivatives, the linear local defect structures relevant at the same derivative accuracy therefore require at most **two additional derivatives**, i.e. geometric mass dimension `<=4`.

This is an order-scoped EFT statement, not an all-loop theorem.

Predicate B: **PASS_SCOPED**.

## 3. Complete dimension-2 endpoint scalar sector

Let `n^mu` be the physical unit tangent of the background geodesic and define

`S := R_nn = R_mn n^m n^n`.

At linear order in curvature, any scalar made from one Riemann tensor and the available tensors `g_mn,n^m` reduces to the two structures

- `R`;
- `S`.

A Riemann contraction with two tangents and one metric is equivalent to a Ricci-tangent contraction; a contraction with four identical tangents vanishes by Riemann antisymmetry. No independent Weyl scalar exists with only `g` and a single tangent.

These operators can appear at an endpoint with the dimensionless one-loop prefactor `kappa^2/l^2`.

## 4. Dimension-3 endpoint sector

At one extra derivative, the independent linear scalar descendants reduce to

- `D R := n^a nabla_a R`;
- `D S := n^a nabla_a S`.

Terms involving the divergence of Ricci reduce by the linearized contracted Bianchi identity to the same `D R` sector.

Their natural one-loop prefactor is `kappa^2/l`.

## 5. Dimension-4 endpoint sector

At two additional derivatives, a convenient flat-background linear basis is

- `Box R`;
- `D^2 R`;
- `Box S`;
- `D^2 S`.

Other contractions of two derivatives with `R_mn` reduce to these by the linearized contracted Bianchi identity and index symmetries. Curvature-commutator differences are nonlinear in curvature and therefore beyond the linear sector retained in Predicate A.

These operators carry the natural one-loop prefactor `kappa^2`.

Endpoint identity mixing proportional to `kappa^2/l^4` may shift one-point/contact conventions but does not provide a new curvature channel in a connected two-point function about flat space.

Predicates C,E: **PASS_SCOPED_ENDPOINT_BASIS**.
`TANGENT_SCALAR_COVARIANCE_CONTROL`: **PASS_CONTROL**.

## 6. Interior line-defect basis and total-derivative reduction

A reparameterization-invariant interior counterterm has the form

`int_0^l ds O(s)`

with local scalar density `O` constructed from the metric, curvature and tangent along the geodesic. UV locality permits local densities along the smooth interior; endpoint singularities are represented separately by endpoint operators rather than by arbitrary affine-parameter functions.

At linear curvature order:

### Dimension 2 line densities

- `R`;
- `S`.

To correct an endpoint operator of dimension two at one loop they appear with prefactor

`kappa^2/l^3 int ds (...)`.

### Dimension 3 line densities

- `D R`;
- `D S`.

Because `n` is parallel transported on the background geodesic,

`int ds D R = R|_endpoints`,

and similarly for `S`. Thus these are not independent interior sectors; they reduce to endpoint mixing.

### Dimension 4 line densities

The longitudinal second derivatives also reduce to endpoint derivatives after integration. A convenient independent interior basis is therefore the transverse combinations

- `Box_perp R := Box R-D^2 R`;
- `Box_perp S := Box S-D^2 S`,

with prefactor

`kappa^2/l int ds (...)`.

This leaves a finite line basis modulo endpoint terms.

Predicates C-E: **PASS_SCOPED_LINE_BASIS**.
`TOTAL_DERIVATIVE_ENDPOINT_CONTROL`: **PASS_CONTROL**.

## 7. No arbitrary tau-dependent counterterm function is required by UV locality

The affine parameter is dimensionless after scaling `s=l tau`. Interior UV divergences on a smooth straight segment are local along the defect; their coefficients are constant defect couplings in the homogeneous flat background. Singularities at `tau=0,1` are endpoint divergences and belong to the endpoint basis.

An arbitrary function `f(tau)` would encode nonlocal information along the segment rather than an ultraviolet-local counterterm and is not generated merely by local one-loop divergence power counting.

Predicate D: **PASS_SCOPED**.
`ARBITRARY_TAU_WEIGHT_CONTROL`: **PASS_CONTROL**.

## 8. Explicit powers of l do not introduce a second scale

The factors `kappa^2/l^2`, `kappa^2/l`, `kappa^2/l^3`, etc. are fixed by engineering dimension using the measured geodesic length itself. This is analogous to the known `Z_chi~kappa^2/l^2` fixed-geodesic counterterm.

They do not introduce a new independent physical length. A separate renormalization scale enters only through ordinary logarithmic running.

Predicate F: **PASS_CONTROL**.
`L_LENGTH_NEW_SCALE_CONTROL`: **PASS_CONTROL**.

## 9. Which sectors are automatically separated-contact and which remain potentially relevant

### Endpoint-local linear sectors

Correlating `R` with any local linear endpoint descendant above at tree level gives a polynomial in external momentum because both operators are local derivatives of the graviton and the massless propagator supplies only one `1/q^2`. Hence their ordinary position-space correlators are contact distributions. Multiplying by the explicit powers of `1/l` does not turn their endpoint support into the universal bulk `l^-8` tail without additional defect renormalization.

Thus these endpoint sectors primarily renormalize endpoint/contact conventions at the frozen order.

### Interior line sectors

The line operators are different. Their correlation with the anchor curvature contains a contact singularity where the integration point approaches the anchor endpoint and can require defect renormalization. After the one-dimensional integration and renormalization, explicit `l` factors mean such counterterms can in principle modify the separated radial coefficients of the **nonlocal observable**, even though the underlying local curvature-curvature kernel is contact away from the coincidence point on the line.

Therefore the line sectors `int R`, `int S`, `int Box_perp R`, `int Box_perp S` cannot be declared irrelevant to `B_0/B_1` without computing their mixing/pole residues.

Predicate G: **PASS_CLASSIFICATION / LINE SECTOR POTENTIALLY RELEVANT**.

## 10. Finite basis summary

At the frozen order, modulo Bianchi identities and total derivatives, the counterterm categories reduce to:

### Endpoint basis

- identity/contact convention;
- `R`, `S`;
- `D R`, `D S`;
- `Box R`, `D^2 R`, `Box S`, `D^2 S`.

### Independent line-interior basis

- `int ds R`;
- `int ds S`;
- `int ds Box_perp R`;
- `int ds Box_perp S`.

with the powers of `l` fixed by engineering dimension as above, plus the known geodesic embedding renormalization `Z_chi` and ordinary bulk/action counterterms.

No infinite functional basis is required at `O(G^2)` within the frozen derivative accuracy.

Predicate H: **PASS**.

## 11. Target independence

No EDT datum is used to select, drop or normalize any operator.

Predicate I: **PASS_CONTROL**.
`EDT_OPERATOR_SELECTION_CONTROL`: **PASS_CONTROL**.

## Source classification

**`PASS_SCOPED_FINITE_LINE_ENDPOINT_COUNTERTERM_BASIS_POWER_COUNTING_CLOSED`**

The curvature-specific fixed-geodesic observable remains perturbatively renormalizable in the practical EFT sense of having a finite allowed defect-operator basis at this order. However, the four independent interior line sectors have not had their pole/mixing coefficients computed and can in principle feed the separated `B_0/B_1` coefficients.

## Consequence for ITER116

The highest-pole/log diagnostic remains cheaper than the full finite calculation, but it must be enlarged to include the pole/mixing matrix of the line operators above. The scalar-style `Z_chi` residue alone is not sufficient.

## Highest-information successor

Construct the **line-defect mixing matrix** for the four independent interior operators and determine, by tree-level contraction and symmetry, which linear combinations can actually project onto the scalar `RR` radial tail. This may reduce the four line couplings to one or two combinations before any one-loop integral is evaluated.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No counterterm is asserted to have a nonzero divergence, no `B_1` value/noncancellation theorem, no EDT fit, no direct EDT/EFT conflict, no continuum EDT, `BRIDGE_DERIVED`, or new physics follows.