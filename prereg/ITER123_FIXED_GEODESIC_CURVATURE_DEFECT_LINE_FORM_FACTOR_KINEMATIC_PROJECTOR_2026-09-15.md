# ITER123 preregistration — fixed-geodesic curvature defect line form factor / kinematic projector

Date: 2026-09-15
Gate: `ITER123_FIXED_GEODESIC_CURVATURE_DEFECT_LINE_FORM_FACTOR_KINEMATIC_PROJECTOR`

## Motivation

ITER122 reduces the two genuine curvature-defect channels to the angular shapes

`f_0(u)=1-u`,
`f_1(u)=(1-u)(u-1/d)`,

with `u=(q.n)^2/q^2`.

ITER123 asks whether the straight-geodesic line integration introduces a common exactly known Fourier form factor and, if so, whether the two unknown UV defect residues can be recovered from two generic scalar kinematic evaluations rather than from a full tensor-valued function.

## Frozen geometry / conventions

By translation invariance, center the flat-background geodesic segment at the origin:

`x(s)=s n`, `s in [-l/2,l/2]`, `n^2=1`.

For a local line density `O(x(s))`, define

`J_O = int_{-l/2}^{l/2} ds O(s n)`.

Set

`z=(q.n)l`, `Q=q^2`, `u=(q.n)^2/Q`.

## Required predicates

A. Derive the exact centered line Fourier factor

`F(z)=int_{-l/2}^{l/2} ds exp(i s q.n)`.

B. Show that the same `F(z)` multiplies both genuine linear line operators `J_R` and `J_TF` at tree/projector level; operator-specific information remains in `f_0,f_1`.

C. Establish that centering changes only a translation phase relative to an endpoint-anchored parameterization and does not change the line-operator content.

D. Define a normalized pole amplitude with the known common factors `Q^2 F(z)` divided out, away from zeros of `F`.

E. In `d=4`, choose two nonexceptional values of `u` for which the 2x2 matrix built from `f_0,f_1` is invertible, and derive exact reconstruction formulas for the two defect residues.

F. The chosen kinematics must avoid `u=1`, where `Box_perp` vanishes, and avoid line-form-factor zeros.

G. The procedure must be classified as a projector/extraction method only: it is valid once the UV divergent amplitude has been reduced to the genuine defect subspace; it does not prove that no other bulk/redundant structures exist before that reduction.

H. Produce a reproducible symbolic script/workflow verifying the determinant and inversion formulas.

I. No EDT target may select the kinematic points or residues.

## Frozen classifications

- `PASS_SCOPED_TWO_POINT_KINEMATIC_PROJECTOR_FOR_GENUINE_DEFECT_RESIDUES` if A-I pass.
- `PASS_SCOPED_LINE_FORM_FACTOR_COMMON_PROJECTOR_MORE_THAN_TWO_POINTS_REQUIRED` if A-D pass but the two-shape inversion fails.
- `FAIL_SCOPED_LINE_FORM_FACTOR_BREAKS_TWO_SHAPE_REDUCTION` if B fails.
- `INFRASTRUCTURE_FAIL` only for symbolic workflow failure.

## Controls

- `ENDPOINT_CENTERED_PARAMETERIZATION_CONTROL`
- `FORM_FACTOR_ZERO_CONTROL`
- `U_EQUAL_ONE_CONTROL`
- `PRE_BASIS_REDUCTION_PROJECTOR_CONTROL`
- `EDT_KINEMATIC_SELECTION_CONTROL`

## Claim ceiling

A PASS supplies a cheap residue-extraction strategy only. It does not compute the UV amplitude, `B_1`, noncancellation, an EDT fit, a direct EDT/EFT comparison, bridge, new physics or candidate theory.