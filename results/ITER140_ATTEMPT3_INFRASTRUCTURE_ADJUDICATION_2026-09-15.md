# ITER140 attempt-3 adjudication — infrastructure/runtime failure only

Date: 2026-09-15
Gate: `ITER140_FIXED_GEODESIC_CURVATURE_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION`
Authoritative frozen preregistration remains unchanged.
Run: `34991523078`
Job: `104457100505`
Workflow head: `71139326311827f08c70126d71a093f439be9f47`

## Attempt classification

`NUMERICAL_OR_INFRASTRUCTURE_FAIL`

This is **not** a scientific FAIL of the ITER140 invariant basis or continuation predicates.

## Evidence

The optimized exact contraction stage completed all required direct tensor reconstructions for dimensions D=3 through D=10. Progress lines for every D=3,4,5,6,7,8,9,10 were emitted successfully for all three frozen families:

- `M_R2_chi1_dR1`;
- `M_R1_chi1_dR2`;
- `G_R1_chi2_Gamma2_dR1`.

The run was then cancelled exactly at the 180-minute job timeout while executing post-reconstruction symbolic continuation/validation work. No frozen predicate result or final JSON classification had been emitted, and artifact upload was skipped.

The earlier 60-minute cancellation and this 180-minute cancellation establish a reproducible performance bottleneck. Increasing timeout again is not the preferred next action.

## Authorized repair

A further implementation-only retry may replace expensive general-purpose symbolic `factor/simplify/interpolate` operations by exact rational / finite-difference polynomial arithmetic and staged exact equality checks, while preserving exactly:

- the 28-monomial frozen basis;
- training D=3..7;
- no-refit validation D=8..10;
- `(D-2)^2` trace-polynomial degree <=4 bound;
- D=4 ITER138/139 cross-authority;
- exact integer-D held-outs;
- O(epsilon) coefficientwise output;
- all original PASS/FAIL/BLOCKED classifications.

No scientific object or threshold may change.

## Claim ceiling

ITER140 remains scientifically open. No general-d PASS, loop pole, B1, noncancellation, B0, EDT comparison, bridge, new physics or candidate theory is established.
