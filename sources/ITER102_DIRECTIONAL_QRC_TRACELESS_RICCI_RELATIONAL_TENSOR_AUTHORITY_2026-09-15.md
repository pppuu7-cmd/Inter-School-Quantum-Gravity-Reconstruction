# ITER102 source authority — directional QRC traceless Ricci and FRG relational tensor route

Date: 2026-09-15
Gate: `ITER102_DIRECTIONAL_QRC_TRACELESS_RICCI_RELATIONAL_TENSOR_AUTHORITY`
Preregistration: `1800d5a4fbc2a0607f8f3af4c5ae79d3afe974ab`

## 1. Exact leading directional decomposition

The D=4 smooth QRC source gives

`Q(v,delta) := dbar/delta`
`= c_4 - delta^2[0.0469 Ric(v,v)+0.0067 R] + O(delta^3)`,

with `c_4=1.6524` in the stated convention.

ITER101 established the isotropic directional average

`<Q>_Omega = c_4 - 0.018425 R delta^2 + O(delta^3)`,

using `<Ric(v,v)>=R/4`.

Subtracting gives

`Q(v,delta)-<Q>_Omega`
`= -0.0469 delta^2 [Ric(v,v)-R/4] + O(delta^3)`.

Writing the traceless Ricci tensor

`S_ij := Ric_ij - (R/4) g_ij`,

one obtains the exact leading channel

**`Q(v)-<Q> = -0.0469 delta^2 S_ij v^i v^j + O(delta^3)`**.

Equivalently, in QRC normalization,

`K_q(v)-<K_q> = (0.0469/1.6524) delta^2 S_ij v^i v^j + O(delta^3)`

with coefficient approximately `0.02838296`.

Predicate A: **PASS**.

## 2. Target independence

The decomposition follows entirely from the source-explicit smooth D=4 coefficients and the tensor identity splitting Ricci into trace plus traceless parts. No CDT QRC anisotropy data, sphere fit, FRG fixed-point value or trajectory is used.

Predicate B: **PASS**.
`TARGET_ANISOTROPY_FIT_CONTROL`: **PASS_CONTROL**.

## 3. Relational physical-frame tensor semantics

The frozen FRG relational-observable source motivates physical coordinate frames precisely so that tensor components can acquire diffeomorphism-invariant physical meaning. It states that a physical local reference frame can give physical meaning to components of tensor fields evaluated in that frame, and develops a composite-operator FRG framework for relational observables.

Therefore a contraction of a relational tensor with a physical tangent direction is a source-qualified **formal observable type**, not an illicit coordinate-axis insertion.

Predicate C: **PASS_FORMAL**.
Predicate E: **PASS_FORMAL / PHYSICAL-FRAME REQUIRED**.
`COORDINATE_DIRECTION_SWAP_CONTROL`: **PASS_CONTROL**.

## 4. Explicit traceless-Ricci flow is not in the frozen calculation

The first explicit application of arXiv:2112.02118 computes the flow/scaling of the inverse relational metric and the relational scalar curvature. The source emphasizes that the formalism can be generalized to observables constructed from other tensors and develops a derivative expansion, including higher-order observables.

However, the frozen source does **not** present an explicit beta/anomalous-dimension calculation for a relational Ricci tensor `Ric_hat{mu hat{nu}}`, its traceless part, or the directional contraction `S_hat{mu hat{nu}} u^hat{mu} u^hat{nu}`.

Thus the required tensor route is formally source-qualified, but its specific composite mixing/flow is open.

Predicate D: **FORMAL ROUTE ONLY / EXPLICIT FLOW OPEN**.
`GENERIC_TENSOR_EXPLICIT_FLOW_CONTROL`: **TRIGGERS**.

## 5. Small-radius and renormalization ceilings

The relation above is a smooth local expansion. At the renormalized FRG level, tensor composite operators can mix and carry their own normalization. At finite CDT regulator, lattice directions and geodesic separations do not automatically realize the smooth tangent-sphere average.

Predicate F: **PASS_CONTROL**.
`FINITE_RADIUS_PROMOTION_CONTROL`: **TRIGGERS**.

## Source classification

**`PASS_SCOPED_TRACELESS_RICCI_QRC_CHANNEL_FORMAL_RELATIONAL_TENSOR_ROUTE_FLOW_OPEN`**

The QRC observable contains, at the same leading order as its scalar channel, an independent traceless-Ricci directional channel with a fixed geometric coefficient. FRG relational-observable machinery has the correct physical-frame tensor semantics to represent such a quantity formally, but the specific relational traceless-Ricci composite flow has not been computed in the frozen source stack.

## Scientific consequence

ITER101's scalar map is not the full information content of local QRC. The directional residual supplies a second operator channel that would vanish on an exact Einstein/constant-curvature geometry but respond to local Ricci anisotropy.

This channel could become a genuinely stronger cross-school comparator only after its FRG composite flow and its CDT finite-regulator directional estimator are separately source-qualified.

## Highest-information successor

Audit the 4D CDT QRC source for what directional information is actually published and whether the spacelike/timelike directional comparison is sufficient to constrain the traceless-Ricci channel without reconstructing unreported raw data. Because the qualitative directional result has already been inspected historically, any such gate must be explicitly retrospective with validation credit 0.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No measured isotropy, Einstein-space theorem, finite-radius tensor equality, unique FRG flow, shared fixed point, full theory equivalence, `BRIDGE_DERIVED`, or new physics follows.