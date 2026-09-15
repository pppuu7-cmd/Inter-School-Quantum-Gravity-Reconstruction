# ITER119 preregistration — fixed-geodesic curvature line-defect observable projection rank

Date: 2026-09-15
Gate: `ITER119_FIXED_GEODESIC_CURVATURE_LINE_DEFECT_OBSERVABLE_PROJECTION_RANK`

## Motivation

ITER118 leaves four independent line-interior counterterm sectors at the frozen order:

`I = (int R, int R_nn, int Box_perp R, int Box_perp R_nn)`.

Corrected ITER114, however, proves that the complete separated one-loop scalar correlator has only two radial structures,

`G^2 l^-8` and `G^2 l^-8 L`, `L=log(mu^2 l^2)`.

ITER119 asks for the rank of the map from the finite defect-counterterm/mixing space to these two observable coefficients before computing the full internal mixing matrix.

## Required predicates

A. Preserve the four line operators as distinct renormalization directions; do not identify them merely because the final observable is scalar.

B. Show that any contribution to the separated scalar correlator at the frozen order must project into the two-dimensional radial function space `(B_0,B_1)`.

C. Separate finite renormalized line couplings from their RG running/pole residues: finite values can shift the constant radial coefficient, while running can generate/cancel explicit logarithmic dependence.

D. Determine whether the projection rank is provably `<=2` independent of the unknown 4x4 internal mixing matrix.

E. Test whether symmetry/power counting further reduces the rank to one; a claim of rank one requires source/analytic proof that either the log or constant line-counterterm projection is absent.

F. Identify the minimum combinations of line-sector data needed to predict the physical separated correlator even if the full four-coupling mixing matrix remains useful for renormalization.

G. No EDT data may be used to select the rank or combinations.

## Frozen classifications

- `PASS_SCOPED_LINE_DEFECT_OBSERVABLE_PROJECTION_RANK_TWO_MAXIMAL` if A-G establish rank `<=2` with no proof of a further reduction.
- `PASS_SCOPED_LINE_DEFECT_OBSERVABLE_PROJECTION_RANK_ONE` if one radial direction is provably absent from line-counterterm effects.
- `BLOCKED_SOURCE_AUTHORITY` if the radial-basis result cannot be consistently combined with defect renormalization.

## Controls

- `INTERNAL_MIXING_OBSERVABLE_RANK_SWAP_CONTROL`
- `SCALAR_OUTPUT_OPERATOR_IDENTITY_CONTROL`
- `FINITE_RUNNING_COEFFICIENT_SWAP_CONTROL`
- `EDT_RANK_SELECTION_CONTROL`

## Claim ceiling

A rank reduction does not compute the projected combinations or `B_0,B_1`. No noncancellation theorem, EDT fit, direct EDT/EFT conflict, `BRIDGE_DERIVED`, new physics or candidate theory follows.