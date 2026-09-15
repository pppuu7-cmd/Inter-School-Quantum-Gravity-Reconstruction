# ISQGR recovery frontier addendum — ITER130 through active ITER133

Date: 2026-09-15
Repository: `pppuu7-cmd/Inter-School-Quantum-Gravity-Reconstruction`

Candidate theory: **UNFORMED / 0%**.
Bridge credit: **0**.
Overall programme roadmap readiness: **50% (no authorized increment)**.

This addendum supersedes the active-gate portion of `recovery/FRONTIER_ADDENDUM_ITER127_ITER130_2026-09-15.md` while preserving all earlier terminal results.

## ITER130 — terminal

Classification:

`PASS_SCOPED_POSITION_VERTICES_CLOSED_MOMENTUM_TENSOR_GENERATOR_OPEN`.

Canonical unreduced position-space nonlinear geometry is closed: inverse metric through O(kappa^2), Gamma1/Gamma2, R1/R2, symmetry controls and derivative budgets. The stronger full momentum-tensor claim was withheld because the R2 momentum representation was still only a prescription.

## ITER131 — terminal

Classification:

`PASS_SCOPED_EXPLICIT_R2_GAMMA2_MOMENTUM_TENSOR_GENERATOR_CLOSED`.

Authoritative run `34915420210`, job `104211875981`, artifact `10375867797`, artifact SHA256 `30a58134151946466742172d709d95e0ec22477f8be327f4905177226557fa3d`.

The D=2 deterministic component generator produced 9 R2 and 72 Gamma2 components and passed Bose/lower-index symmetries, homogeneity and frozen polarization controls. Because the concrete machine table was D=2, downstream physical use required a separate D=4 transfer audit.

## ITER132 — terminal

Classification:

`PASS_SCOPED_D4_R2_GAMMA2_VERTEX_TRANSFER_CLOSED`.

Authoritative run `34951905279`, job `104324613596`, artifact `10389487686`, artifact SHA256 `4d6dc0baea302bd99735e4bf04407b85881f18657ecb0d8776ee2528396a1b0f`.

The full ten-element D=4 symmetric graviton-leg basis passed R2 Bose symmetry, Gamma2 lower-index symmetry, Gamma2 leg Bose symmetry and momentum homogeneity. Three independent direct two-plane-wave metric reconstructions, including off-diagonal polarizations and non-collinear momenta, exactly matched the explicit R2 generator. D=4 R2/Gamma2 vertices are therefore authorized for downstream M/G numerator construction.

## Active gate — ITER133

`ITER133_FIXED_GEODESIC_CURVATURE_FIRST_MG_NUMERATOR_JETS`.

Preregistration:
`prereg/ITER133_FIXED_GEODESIC_CURVATURE_FIRST_MG_NUMERATOR_JETS_2026-09-15.md`.

Frozen first families:

- `M_R2_chi1_dR1`, bulk affine weight `(1-tau)`;
- `G_R1_chi2_Gamma2_dR1`, bulk affine weight `(1-tau)`.

The task is to build exact tensor numerator polynomials using the now-authorized D=4 nonlinear vertices and the ITER124 de-Donder projector convention, preserve the ITER127 source-qualified affine weights, and measure realized loop/endpoint jet degrees after tensor cancellation. No derivative ceiling may substitute for an exact numerator.

## Exact next action

Implement ITER133 exact numerator construction for the two frozen Gaussian M/G families. Emit numerator polynomials before denominator integration, realized degrees, affine endpoint suppression, graviton-leg/projector symmetry checks, and comparison against ITER129 ceilings. Only after ITER133 closes may the corresponding endpoint pole residues be extracted.

No B1 value, noncancellation result, EDT comparison, bridge, new physics or candidate theory is authorized at this frontier.
