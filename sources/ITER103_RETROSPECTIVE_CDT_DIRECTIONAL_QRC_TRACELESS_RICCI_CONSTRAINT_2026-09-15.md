# ITER103 source authority — retrospective CDT directional QRC constraint

Date: 2026-09-15
Gate: `ITER103_RETROSPECTIVE_CDT_DIRECTIONAL_QRC_TRACELESS_RICCI_CONSTRAINT`
Protocol: `bbb8df519d8d60cbf2e1e05818f03092b524a9cd`
Retrospective validation credit: **0**

## 1. Exact measurement scope

The 4D CDT QRC source performs an exploratory directional study at fixed volume `N_41=150k`, within the de-Sitter phase at the stated bare point `(kappa_0, Delta)=(2.2,0.6)`.

On the dual lattice it introduces fractional dual-time labels and defines two extreme classes for sphere centres at dual-link distance `delta`:

- **maximally spacelike**: equal fractional time labels;
- **maximally timelike**: fractional time labels differ by `delta/4`.

The measurement considers radii up to `delta=15`. To make the paired comparison homogeneous, the procedure retains centre choices for which the required maximally timelike partner exists out to the largest shell; the source notes this succeeds in about half the cases and argues the retained sample is plausibly representative.

Predicate A: **PASS**.

## 2. Raw directional difference is dominated by a vertical offset

Before correction, the timelike normalized average sphere distance is systematically larger than the spacelike one and follows a visibly offset trajectory.

The source emphasizes that `c_q` is nonuniversal on piecewise-flat/discrete metric spaces and can itself depend on lattice direction because link-distance anisotropy changes the constant part of `dbar/delta` even in otherwise flat lattice examples.

Therefore a vertical separation in `dbar/delta` cannot be interpreted directly as a Ricci-curvature difference.

Predicate B: **PASS**.
`CQ_OFFSET_CURVATURE_SWAP_CONTROL`: **PASS_CONTROL**.

## 3. Offset-controlled comparison

The authors shift the maximally timelike data vertically by `-0.476`, chosen so that timelike and spacelike values coincide at `delta=6`.

After this one constant offset subtraction:

- remaining discrepancies are confined to the short-distance region;
- for the reported range **`delta > 6` the match is almost perfect**;
- the source interprets the effect as evidence that the original directional difference is due to a `Delta c_q` lattice-discretization offset while the QRC curvature behaviour itself is isotropic within measuring accuracy.

Predicate C: **PASS_SOURCE_REPORTED**.

## 4. What this constrains in ITER102 language

ITER102 showed that in a smooth small-radius expansion the directional residual is proportional to

`S_ij v^i v^j`,

with `S_ij` the traceless Ricci tensor.

The CDT directional study supports equality of the **scale-dependent curvature-profile shape** for two selected extreme directional classes after an allowed nonuniversal constant-offset correction.

This is evidence that the corresponding spacelike and timelike QRC curvature projections are equal within the resolution/systematics of that finite-regulator study.

It is **not** a reconstruction of the full four-dimensional traceless Ricci tensor because:

1. only two coarse directional classes are compared;
2. no complete basis of independent tangent directions/components is measured;
3. the comparison is finite-radius (`delta > 6`), not the `delta -> 0` regime of the local tensor expansion;
4. a fitted/diagnostic constant offset is needed to remove lattice anisotropy;
5. the study is exploratory and does not provide a tensor-component covariance/inversion.

Predicate D: **PASS_CONTROL; FULL TENSOR NOT IDENTIFIED**.
`TWO_DIRECTIONS_FULL_TENSOR_CONTROL`: **TRIGGERS**.

## 5. No local-coefficient fit

The source does not fit the directional difference to the ITER102 coefficient `0.0469 delta^2 S_ij v^i v^j`. Its physical conclusion is based on finite-radius profile shape after offset control.

ITER103 therefore records the published directional constraint without reinterpreting it as a local traceless-Ricci numerical estimate.

Predicate E: **PASS_CONTROL**.
`FINITE_RADIUS_LOCAL_EXPANSION_CONTROL`: **TRIGGERS**.

## 6. Retrospective lock

The qualitative spacelike/timelike outcome was inspected before protocol registration. It receives **zero prospective validation credit** regardless of agreement with any FRG/de-Sitter expectation.

Predicate F: **PASS_CONTROL; CREDIT=0**.

## Source classification

**`SOURCE_SUPPORTS_TWO_CLASS_DIRECTIONAL_CURVATURE_ISOTROPY_NOT_FULL_TENSOR_RECONSTRUCTION`**

The published 4D CDT QRC measurement provides nontrivial finite-radius evidence that, after accounting for a direction-dependent lattice `c_q` offset, maximally spacelike and maximally timelike curvature profiles behave the same over the reliable reported scale range. This is stronger than scalar averaging alone but weaker than `S_ij=0` as a tensor statement.

## Consequence for the cross-school route

The result is structurally compatible with the round-S4 / Einstein-background sector, where traceless Ricci vanishes, but it cannot validate a quantum FRG traceless-Ricci expectation or determine its renormalized flow. That requires the explicit relational tensor composite missing in ITER102.

## Highest-information successor

Search the FRG/asymptotic-safety observable literature specifically for an explicit relational Ricci-tensor, Einstein-tensor, traceless-curvature or spin-2 local composite flow. A generic statement that arbitrary tensors can be made relational is no longer sufficient. If no explicit source exists, record the operator-flow gap rather than inferring it from scalar-curvature calculations.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No full isotropy theorem, Einstein-space theorem, quantum tensor equality, shared fixed point, full theory equivalence, `BRIDGE_DERIVED`, or new physics follows.