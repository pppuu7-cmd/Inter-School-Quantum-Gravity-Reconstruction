# ITER126 preregistration — fixed-geodesic curvature line endpoint/coincidence pole extraction authority

Date: 2026-09-15
Gate: `ITER126_FIXED_GEODESIC_CURVATURE_LINE_ENDPOINT_COINCIDENCE_POLE_EXTRACTION_AUTHORITY`

## Motivation frozen before prototype evaluation

ITER125 reduces the future `B_1` calculation to ordinary bubbles plus one-/two-line parameter master families. The expensive finite oscillatory dependence is not required if ultraviolet poles are determined entirely by local affine-parameter endpoint/coincidence regions after ordinary bulk subdivergences have been subtracted.

ITER126 tests that locality and evaluates two universal scalar prototypes. It does not claim that their residues are the curvature `B_1` coefficients.

## Frozen setup

Use `d=4-2 epsilon` and the massless Euclidean propagator scaling

`G_d(r) ~ r^(2-d)`

up to its standard dimension-dependent normalization.

Line parameters are dimensionless after `s=l tau`.

## Required predicates

A. After bulk UV subdivergence subtraction, show that line-parameter regions bounded away from endpoint/coincidence configurations are UV finite; residual defect poles are local in the affine parameters.

B. Evaluate the endpoint-product prototype

`E(epsilon)=int_0^1 d tau [tau(1-tau)]^(-2+2 epsilon)`

by analytic continuation and determine `Res_{epsilon=0} E`.

C. Evaluate the line-line coincidence prototype

`D(epsilon)=int_0^1 d tau int_0^1 d sigma |tau-sigma|^(-2+2 epsilon)`

and determine its pole residue.

D. Interpret B/C only as local prototype residues. Tensor derivatives and source-specific line weights can shift exponents/numerators and must be expanded separately.

E. For M2/two-parameter bubble families with overlapping endpoint+coincidence regions, require sector/forest subtraction to avoid double counting and to expose higher-pole consistency.

F. Show that a smooth finite line-form-factor dependence away from singular regions cannot alter the pole residue except through its local Taylor coefficients at those regions.

G. Establish an asymptotic-subtraction algorithm: expand smooth weights around each singular region to the finite order needed by power counting, integrate the singular monomials analytically, and send the subtracted remainder to finite numerical/symbolic integration only after poles are removed.

H. Produce a symbolic check of the two prototype residues.

I. No prototype residue may be identified with `B_1` or fitted to EDT data.

## Frozen classifications

- `PASS_SCOPED_DEFECT_POLES_LOCAL_ENDPOINT_COINCIDENCE_ASYMPTOTIC_SUBTRACTION_AUTHORIZED` if A-I pass.
- `PASS_SCOPED_PROTOTYPE_POLES_LOCAL_FULL_M2_OVERLAP_REDUCTION_OPEN` if B-D/F-H pass but E/G cannot be closed generally.
- `FAIL_SCOPED_NONLOCAL_INTERIOR_CONTRIBUTES_TO_UV_POLE` if a pole requires finite interior line data after bulk subtraction.
- `INFRASTRUCTURE_FAIL` only for symbolic-check failure.

## Controls

- `PROTOTYPE_B1_SWAP_CONTROL`
- `POWER_DIVERGENCE_DR_ZERO_CONTROL`
- `OVERLAP_DOUBLE_COUNT_CONTROL`
- `FINITE_INTERIOR_POLE_CONTROL`
- `TARGET_RESIDUE_FIT_CONTROL`

## Claim ceiling

A PASS authorizes local pole extraction, not the actual curvature residue. No `B_1`, noncancellation theorem, EDT fit, bridge, new physics or candidate theory follows.