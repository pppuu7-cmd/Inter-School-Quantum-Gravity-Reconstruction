# ISQGR recovery frontier addendum — terminal ITER127–ITER129, active ITER130

Date: 2026-09-15
Repository: `pppuu7-cmd/Inter-School-Quantum-Gravity-Reconstruction`

Candidate theory: **UNFORMED / 0%**.
Bridge credit: **0**.
Overall programme roadmap readiness: **50% (no authorized increment)**.

This addendum continues `recovery/FRONTIER_ADDENDUM_ITER112_ITER127_2026-09-15.md`.

## ITER127 — terminal

Classification:

`PASS_SCOPED_EXACT_CHI1_CHI2_WEIGHTS_SOURCE_QUALIFIED_SINGULAR_TABLE_CLOSED`.

Exact arXiv source authority for `1706.01891` is preserved through four GitHub Actions artifacts, including a strict same-equation check for:

- first-order initial-tangent coefficient `-1/2`;
- second-order quadratic initial-tangent coefficient `+3/8`;
- affine Green-difference kernel;
- `chi2` dependence on `chi1` and Christoffel structure.

Source-qualified affine weights include:

- outer `(1-tau)`;
- nested position `(1-tau)(tau-sigma)`;
- initial-position nested `tau(1-tau)`;
- bulk-bulk chi1 product `(1-tau)(1-sigma)`.

`d chi1` removes the inner `(tau-sigma)` polynomial suppression; chi1 itself retains it.

Machine table:
`analysis/iter127_projected_singular_strata_table.json`.

## ITER128 — terminal

Classification:

`PASS_SCOPED_CANONICAL_JET_BOUNDS_CLOSED_INTERACTION_SPECIFIC_ROWS_OPEN`.

Local one-propagator rule after bulk subtraction:

`m_raw=2+N`,
`m_eff=m_raw-s`,
`jet=m_eff-1`.

Two-propagator local products use `m_raw=4+N`.

Canonical bounds:

- R1–Gamma1: jet 4 lower endpoint, 3 upper endpoint with `(1-tau)`;
- R1–dGamma1: 5 unsuppressed, 4 with one Green suppression;
- Gamma1–Gamma1 diagonal: 3;
- dGamma1–Gamma1: 4 unsuppressed, 3 with `(tau-sigma)`;
- R1–BoxPerpR / BoxPerpRnn genuine defect endpoint: jet ceiling 7.

The single-variable residual-defect ceiling `k<=7` is post-subdivision/counterterm projection, not a raw integrand ceiling.

## ITER129 — terminal

Classification:

`PASS_SCOPED_GRAPH_DERIVATIVE_CEILINGS_CLOSED_EXACT_TENSOR_ALLOCATION_OPEN`.

Finite `O(kappa^4)` family census: 12 rows = 5 F + 3 M + 4 G.

Total derivative ceilings:

- F: `4,4,6,6,8`;
- M: `6,6,8`;
- G: `6,7,8,8`.

Thus `D_total<=8`. Affine one-propagator `N1_max<=5` in interaction/localization families. Conservative simultaneous raw two-propagator ceiling `m_raw<=12` before tensor reduction/source suppression.

Machine table:
`analysis/iter129_graph_derivative_ceiling_table.json`.

No ceiling is a pole residue and no physical `l^-12` behavior follows; corrected physical one-loop radial basis remains `G^2 l^-8[B0+B1 log]`.

## Active gate — ITER130

`ITER130_FIXED_GEODESIC_CURVATURE_R2_GAMMA2_VERTEX_AUTHORITY`.

Preregistration:
`prereg/ITER130_FIXED_GEODESIC_CURVATURE_R2_GAMMA2_VERTEX_AUTHORITY_2026-09-15.md`.

Reason for this prerequisite: the planned pole-relevant numerator-jet generator needs exact second-order nonlinear geometric vertices, not only derivative ceilings.

ITER130 must symbolically close:

- inverse metric through O(kappa^2);
- Gamma1/Gamma2 in the Fröb convention;
- R1/R2 in a canonical unreduced representation;
- bilinear momentum-space R2 and Gamma2 vertices;
- Bose/lower-index symmetries;
- consistency of R1 with ITER122;
- derivative-budget checks `D(R2)=2`, `D(Gamma2)=1`.

## Exact next action

Implement symbolic nonlinear-geometry expansion for ITER130 and use its tested R2/Gamma2 vertices as inputs to the first Gaussian M/G pole-relevant numerator jets. Do not start loop residues from derivative-count approximations alone.
