# ITER120 preregistration — fixed-geodesic curvature field-redefinition / defect quotient

Date: 2026-09-15
Gate: `ITER120_FIXED_GEODESIC_CURVATURE_FIELD_REDEFINITION_DEFECT_QUOTIENT`

## Motivation

ITER118 leaves four line-interior curvature sectors. ITER119 proves that only two radial output combinations can be measured. Before computing pole residues, ITER120 asks whether part of the four-dimensional line basis is redundant under standard local metric field redefinitions of low-energy gravity.

## Frozen setup

At one-loop order consider the local metric redefinition

`delta g_mn = kappa^2 [a R_mn + b g_mn R]`

with constant dimensionless `a,b`, and a smooth unit-speed geodesic of length `l` and tangent `n^m`.

## Required predicates

A. Derive the first variation of geodesic length under `delta g_mn`.

B. Show whether `int ds R` and `int ds R_nn` appear exactly as the induced line structures.

C. Retain the simultaneous transformation of endpoint curvature operators; a field redefinition is not permission to change the observable while leaving its insertions fixed.

D. Determine whether these dimension-2 line directions are redundant scheme/field-coordinate directions rather than independent physical defect couplings when the theory and observable are transformed consistently.

E. Test whether the dimension-4 transverse line operators `int Box_perp R` and `int Box_perp R_nn` can arise from an `O(kappa^2)` local metric redefinition without an additional scale.

F. If E fails, classify those sectors as genuine defect directions at the frozen order, while retaining the possibility of higher-order field redefinitions beyond the gate.

G. Determine the quotient dimension of the line-defect counterterm space relevant before pole evaluation.

H. No EDT data may be used to select a field-redefinition scheme.

## Frozen classifications

- `PASS_SCOPED_DIM2_LINE_SECTORS_FIELD_REDEFINITION_REDUNDANT_GENUINE_DEFECT_RANK_TWO` if A-H reduce the independent line sectors from four to two.
- `PASS_SCOPED_FIELD_REDEFINITION_RELATION_EXISTS_QUOTIENT_RANK_OPEN` if A-C pass but independence cannot be adjudicated.
- `FAIL_SCOPED_FIELD_REDEFINITION_DOES_NOT_GENERATE_LINE_BASIS` if B fails.

## Controls

- `FIELD_REDEFINITION_OBSERVABLE_CHANGE_CONTROL`
- `R_RNN_INDEPENDENT_COUPLING_CONTROL`
- `HIGHER_ORDER_REDEFINITION_ORDER_CONTROL`
- `EDT_FIELD_SCHEME_SELECTION_CONTROL`

## Claim ceiling

A quotient result reduces renormalization bookkeeping only. It does not compute a pole residue, `B_1`, an EDT prediction, a bridge, new physics or a candidate theory.