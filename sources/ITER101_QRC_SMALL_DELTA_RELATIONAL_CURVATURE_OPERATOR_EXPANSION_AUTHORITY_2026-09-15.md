# ITER101 source authority — QRC small-delta ↔ relational scalar-curvature operator map

Date: 2026-09-15
Gate: `ITER101_QRC_SMALL_DELTA_RELATIONAL_CURVATURE_OPERATOR_EXPANSION_AUTHORITY`
Preregistration: `a8131c9435c935d655012fddde89f4c048421083`
Bibliographic correction: `c1c8166a3c0ac4ae537bc1c8c7c78d0bf10d6d66`

## 1. Source-explicit D=4 QRC expansion

The smooth-manifold expansion quoted in *Implementing quantum Ricci curvature* is, in four dimensions,

`dbar/delta = 1.6524 + delta^2[-0.0469 Ric(v,v) - 0.0067 R + O(delta)]`,

where `v` is the unit vector from the centre `p` toward `p'`, and `R` is the Ricci scalar at `p`.

Equivalently, with the outer `delta^2` displayed,

`dbar/delta = 1.6524 - delta^2[0.0469 Ric(v,v)+0.0067 R] + O(delta^3)`.

The source states that these numerical coefficients arise from exact dimension-dependent integral expressions and depend on dimension, not on the particular geometry.

Predicate A: **PASS**.

## 2. Directional and scalar contributions remain distinct before averaging

The source formula contains both `Ric(v,v)` and `R`. Therefore the finite-direction object must not be replaced by a scalar before the directional averaging used to construct the scalar QRC profile.

Predicate B: **PASS**.
`DIRECTIONAL_SCALAR_SWAP_CONTROL`: **PASS_CONTROL**.

## 3. Directional average in D=4

For an isotropic average over unit tangent directions at a smooth point,

`<v^i v^j>_Omega = g^{ij}/D`.

Hence

`<Ric(v,v)>_Omega = R/D = R/4`.

Substituting into the source expansion gives

`<dbar/delta>_Omega`
`= 1.6524 - [0.0469/4 + 0.0067] R delta^2 + O(delta^3)`
`= 1.6524 - 0.018425 R delta^2 + O(delta^3)`.

Thus the first nonconstant term of the directionally averaged smooth 4D QRC observable is uniquely proportional to the local scalar curvature.

Predicate C: **PASS**.

## 4. Equivalent QRC normalization

The QRC definition is

`dbar/delta = c_q [1-K_q]`.

For a smooth four-dimensional manifold the constant term of the small-radius expansion fixes the corresponding local smooth normalization to the quoted `c_4 = 1.6524` convention. Therefore

`<K_q(delta)>_Omega = alpha_4 R delta^2 + O(delta^3)`

with

`alpha_4 = 0.018425 / 1.6524 ≈ 0.01115045`.

No CDT measured curvature profile, fitted sphere radius or FRG target value enters this coefficient.

Predicate D: **PASS**.
`TARGET_FIT_CONTROL`: **PASS_CONTROL**.

## 5. FRG relational scalar-curvature operator

The frozen FRG source arXiv:2112.02118 constructs relational observables in a physical coordinate frame supplied by dynamical scalar fields and uses composite-operator FRG machinery to evolve them toward quantum expectation values. At leading derivative order its explicit observables include the relational inverse metric and the **relational scalar curvature**.

Therefore the local operator appearing in the leading directionally averaged QRC expansion has a source-defined FRG quantum-composite counterpart of the same scalar-curvature type.

The reference-field dressing and FRG truncation are part of the operator definition and are not erased here.

Predicate E: **PASS_SCOPED**.

## 6. Resulting asymptotic operator map

Within the common smooth Euclidean local regime, the source-qualified type map is

`QRC_scalar(delta)`
`= alpha_4 delta^2 R_rel + O(delta^3 * local curvature/derivative structures)`

in the normalization above, or equivalently

`<dbar/delta>_Omega`
`= c_4 - 0.018425 delta^2 R_rel + O(delta^3)`.

This is an **asymptotic local operator expansion**. It is not an identity at finite `delta`.

Predicate F: **PASS_SCOPED**.
`HIGHER_ORDER_REMAINDER_ERASURE_CONTROL`: **PASS_CONTROL**.

## 7. Why this does not immediately predict the measured 4D CDT QRC profile

The QRC lattice literature emphasizes a short-distance lattice-artifact regime; reliable nontrivial CDT measurements are taken at separations above that regime. The smooth expansion, by contrast, is controlled when `delta` is small compared with curvature/variation scales.

At finite regulator there is no source-established overlap window

`a << delta << L_curv`

with the required continuum normalization and negligible artefacts that would justify inserting measured CDT finite-`delta` values into the leading expansion.

Thus the local map is source-qualified while the direct finite-radius numerical comparator remains open.

Predicate G: **PASS_CONTROL / FINITE-RADIUS PROMOTION BLOCKED**.
`FINITE_RADIUS_PROMOTION_CONTROL`: **TRIGGERS**.
`LATTICE_SMALL_DELTA_CONTROL`: **TRIGGERS**.

## 8. No delta-k identification

The expansion contains a physical/geometric resolution `delta`; FRG flow uses a coarse-graining scale `k`. Dimensional compatibility alone does not source-define `delta=1/k` or any fixed proportionality.

Predicate H: **PASS_CONTROL**.
`DELTA_K_SWAP_CONTROL`: **TRIGGERS**.

## Source classification

**`PASS_SCOPED_SMALL_DELTA_QRC_TO_RELATIONAL_SCALAR_OPERATOR_MAP`**

This closes a precise part of ITER100's operator-closure gap: the first curvature-sensitive term of the directionally averaged 4D QRC has a universal source-derived local scalar-curvature form and therefore a typed FRG relational-composite counterpart.

It does **not** close the full finite-radius QRC operator. Higher-order nonlocal information and the scale/expectation map remain open.

## Highest-information successor

The next gate should ask whether the source-defined next terms in the smooth QRC expansion can be organized into a finite local operator basis (curvature-squared and derivative composites) already covered by asymptotic-safety composite-operator calculations. If they cannot, that precisely locates where the local derivative expansion stops approximating finite-radius QRC.

No CDT QRC target values should be consumed to choose that operator basis.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No finite-radius QRC equality, `delta=1/k`, numerical CDT/FRG agreement, shared RG trajectory/fixed point, full theory equivalence, `BRIDGE_DERIVED`, or new physics follows.