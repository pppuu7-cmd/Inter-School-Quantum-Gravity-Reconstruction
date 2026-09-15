# ITER121 preregistration — fixed-geodesic curvature genuine-defect B1 projection authority

Date: 2026-09-15
Gate: `ITER121_FIXED_GEODESIC_CURVATURE_GENUINE_DEFECT_B1_PROJECTION_AUTHORITY`

## Motivation

ITER120 quotients the four allowed line curvature sectors by two local metric-field-redefinition directions. The genuine defect space is represented by

`J_R = int ds Box_perp R`,
`J_S = int ds Box_perp R_nn`.

Corrected ITER114/116 show that the separated logarithmic output at `O(G^2)` is a single number `B_1` multiplying `G^2 l^-8 log(mu^2 l^2)`.

## Frozen question

Can symmetry/Bianchi/field-redefinition structure determine the projection of the two genuine defect pole directions onto `B_1` up to one known combination before explicit loop integration? Or is one scalar output guaranteed but its two input weights remain dynamical quantities?

## Required predicates

A. Preserve `J_R,J_S` as two independent genuine defect operators from ITER120.

B. Prove that their complete contribution to the separated logarithmic radial sector is one-dimensional because only one `l^-8 L` function exists.

C. Test whether trace/traceless Ricci decomposition, Bianchi identities, line reversal, or residual rotations about the geodesic force a relation between the two pole projections.

D. Do not use full rotational averaging that erases the physical geodesic tangent `n^mu`.

E. If no symmetry relation exists, identify the minimum explicit UV data required: two pole matrix elements or an equivalent directly projected combined residue.

F. Retain field-redefinition redundant sectors as consistency checks but not independent physical inputs.

G. No EDT target may select the linear combination.

## Frozen classifications

- `PASS_SCOPED_GENUINE_DEFECT_B1_PROJECTION_ONE_DIMENSION_WEIGHT_FIXED` if symmetry fixes the input combination.
- `PASS_SCOPED_GENUINE_DEFECT_B1_OUTPUT_ONE_DIMENSION_TWO_INPUT_WEIGHTS_OPEN` if the output is one-dimensional but both genuine defect pole projections must be calculated.
- `BLOCKED_SOURCE_AUTHORITY` if the projection cannot be typed.

## Controls

- `GEODESIC_TANGENT_ISOTROPIC_AVERAGE_CONTROL`
- `TRACE_TRACELESS_RELATION_CONTROL`
- `FIELD_REDEFINITION_REDUNDANT_INPUT_CONTROL`
- `EDT_LINEAR_COMBINATION_FIT_CONTROL`

## Claim ceiling

No pole value, `B_1`, noncancellation theorem, EDT fit, direct EDT/EFT conflict, bridge, new physics or candidate theory follows from projection rank alone.