# ITER133 preregistration — first exact M/G pole-relevant numerator jets

Date: 2026-09-15
Gate: `ITER133_FIXED_GEODESIC_CURVATURE_FIRST_MG_NUMERATOR_JETS`
Execution dependency: ITER132 must first classify `PASS_SCOPED_D4_R2_GAMMA2_VERTEX_TRANSFER_CLOSED`.

## Frozen motivation
ITER129 closed only derivative ceilings. ITER130/131 supplied canonical nonlinear geometry and an explicit component generator, while ITER132 transfers that authority to D=4. The next admissible step is exact tensor allocation for the simplest Gaussian localization families before any pole residue is evaluated.

## Frozen families
1. `M_R2_chi1_dR1` with source-qualified bulk chi1 weight `(1-tau)`.
2. `G_R1_chi2_Gamma2_dR1` with source-qualified bulk chi2-Gamma2 weight `(1-tau)`.

These are chosen because they use the newly authorized R2/Gamma2 vertices without cubic/quartic action vertices and therefore isolate the first exact M/G numerator construction.

## Frozen predicates
A. Work in flat Euclidean background and de Donder propagator convention of ITER124, retaining symbolic affine parameter and external momentum direction.
B. Construct every graviton contraction explicitly from R1/dR1 plus the D=4 R2 or Gamma2 vertex; no derivative-count proxy may substitute for a tensor numerator.
C. Preserve the source-qualified affine factor `(1-tau)` and distinguish lower-endpoint unsuppressed from upper-endpoint +1 suppression.
D. Emit the exact numerator polynomial before denominator integration, together with total loop-momentum degree and actual endpoint jet degree after tensor cancellations.
E. Verify the realized loop-momentum degree does not exceed the ITER129 family ceiling (`D_total<=6`, `N1_max<=4`).
F. Verify graviton-leg exchange consistency and de Donder projector index symmetries on deterministic exact panels.
G. Keep all numerator construction target-independent: no B1 value, EDT exponent, desired cancellation or fitted coefficient may enter.

## Frozen classifications
- `PASS_SCOPED_FIRST_MG_EXACT_NUMERATOR_JETS_CLOSED_POLE_INTEGRATION_OPEN` iff A-G pass for both families.
- `FAIL_SCOPED_MG_NUMERATOR_TENSOR_OR_AFFINE_MISMATCH` if an exact identity or source weight fails.
- `BLOCKED_ITER132_D4_TRANSFER_NOT_CLOSED` if ITER132 has not passed.

## Claim ceiling
A PASS authorizes these two exact numerator jets as inputs to subsequent endpoint-pole extraction. It is not a pole residue, B1 determination, noncancellation result, EDT match, bridge, new physics or candidate theory.
