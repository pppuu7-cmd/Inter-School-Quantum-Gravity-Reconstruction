# ITER130 terminal result — R2 / Gamma2 nonlinear vertex authority

Date: 2026-09-15
Prereg commit: `85176033b9022d03859d8ba769207f0d96f02a5e`
Implementation commits: `5e934d85bc83dad77cec8a74e658333c7269681d`, workflow `faa6d9327662238199347a1775ce7f1abb344913`
Authoritative run: `34915342840`
Job: `104211639689` (`symbolic-vertex-audit`)
Artifact: `10375288985`
Artifact SHA256: `208da6d17e7ec796320143810275823d0467336f4d5c44e19f88ed946662efa4`

## Scientific classification

`PASS_SCOPED_POSITION_VERTICES_CLOSED_MOMENTUM_TENSOR_GENERATOR_OPEN`

This classification follows the preregistered gate rather than the script's internal green label. The raw log/artifact validates A-D/G and the structural symmetry controls, but the R2 momentum-space output is still a prescription (Fourier transform + polarization), not an explicit indexed bilinear tensor vertex. Therefore the stronger `PASS_SCOPED_R2_GAMMA2_VERTEX_AUTHORITY_SYMBOLICALLY_CLOSED` is not credited.

Validated content:

- inverse metric through O(kappa^2);
- Gamma1 and Gamma2, with Gamma2 entirely from the inverse-metric correction and no independent second-order metric field;
- canonical unreduced position-space R2;
- R1 agreement with the frozen convention;
- Gamma2 lower-index symmetry;
- derivative budgets D(R2)=2 and D(Gamma2)=1;
- target-independent construction.

Open item: explicit bilinear momentum-space tensor generator for R2 and Gamma2, with leg-index symmetrization and numerical/symbolic spot checks against direct plane-wave polarization.

No loop pole, B1, noncancellation, EDT fit, bridge, new physics or candidate theory is implied.