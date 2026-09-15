# ITER121 adversarial critic — genuine-defect projection onto B1

Date: 2026-09-15
Gate: `ITER121_FIXED_GEODESIC_CURVATURE_GENUINE_DEFECT_B1_PROJECTION_AUTHORITY`
Preregistration: `6695ff2cd161e6252d45937c5939350a5a77dd46`
Source authority: `ba56594977d44f60cb0c28d736a9bb4d2ae8e210`

## Attack 1 — scalar output forces J_R and J_S to be proportional

Rejected. A scalar observable can receive independent scalar contributions from trace and tangent-traceless curvature channels. The fixed geodesic supplies `n^mu`, so `R_nn` is not reduced to `R/4` before the path integral.

## Attack 2 — contracted Bianchi identity fixes R_nn in terms of R

Rejected. Bianchi constrains divergences of Ricci, not the full off-shell tangent projection `R_mn n^m n^n`. It reduced derivative redundancies in ITER118 but does not impose an Einstein condition.

## Attack 3 — residual rotations around the line kill the traceless channel

Rejected. `S_nn` is invariant under rotations that leave the line tangent fixed. Only a full average over all tangent directions would remove its traceless expectation at linear isotropic level, and the fixed-geodesic observable does not perform that average.

## Attack 4 — one-dimensional B1 output means only one loop integral is needed

Not necessarily. Two independent tensor/defect kernels can project into the same radial log function with different coefficients. One may compute them separately or construct a directly projected integrand that combines them before integration. The latter is preferable but still contains both tensor structures.

## Attack 5 — field-redefinition redundant sectors can be ignored entirely

Rejected. They are not independent physical inputs, but retaining them in intermediate algebra provides a stringent check that the final projected residue is invariant under local metric field-coordinate changes.

## Critic verdict

**CONFIRMS `PASS_SCOPED_GENUINE_DEFECT_B1_OUTPUT_ONE_DIMENSION_TWO_INPUT_WEIGHTS_OPEN`.**

A reproducible tensor-kernel reduction is the next safe step before actual pole integration.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.