# ITER131 preregistration — explicit R2/Gamma2 momentum tensor generator

Date: 2026-09-15
Gate: `ITER131_FIXED_GEODESIC_CURVATURE_EXPLICIT_MOMENTUM_VERTEX_GENERATOR`

## Frozen motivation
ITER130 closed canonical position-space nonlinear vertices but, under its preregistered decision rule, did not earn the stronger full-vertex PASS because R2 momentum space remained a Fourier/polarization prescription rather than an explicit indexed bilinear tensor generator.

## Frozen predicates
A. Generate coefficient tensors for two symmetric graviton legs `h_ab(p) h_cd(k)` by polarization of the canonical unreduced ITER130 R2 and Gamma2 formulas; `q=p+k`.
B. Preserve Euclidean `partial -> i momentum` convention and do not integrate by parts or use on-shell identities.
C. Verify R2 Bose symmetry `(p,ab)<->(k,cd)` componentwise for deterministic integer momentum/index test panels.
D. Verify Gamma2 lower Christoffel symmetry `m<->n` and graviton-leg Bose symmetry after bilinear polarization.
E. Independently evaluate direct two-plane-wave substitution and show equality to the generated bilinear vertex on held-out deterministic panels.
F. Verify derivative homogeneity: R2 degree 2 in momenta; Gamma2 degree 1.
G. No loop denominator, pole, B1, EDT target, desired cancellation, or fitted coefficient may enter generation or tests.

## Frozen classifications
- `PASS_SCOPED_EXPLICIT_R2_GAMMA2_MOMENTUM_TENSOR_GENERATOR_CLOSED` iff A-G pass.
- `FAIL_SCOPED_MOMENTUM_VERTEX_POLARIZATION_OR_SYMMETRY_MISMATCH` if any exact identity fails.
- `NUMERICAL_OR_INFRASTRUCTURE_FAIL` only for execution/tool failure before predicates are evaluated.

## Claim ceiling
A PASS supplies explicit nonlinear momentum vertices for later pole-relevant numerator jets only. It is not a loop-pole result, B1, noncancellation, EDT match, bridge, new physics, or candidate theory.