# ITER131 terminal result — explicit R2/Gamma2 momentum tensor generator

Date: 2026-09-15
Prereg commit: `85aa6efd9c83c34ee42207d25538acfa5a159f40`
Implementation commit: `e210dd680a113debde8fc16f65e958641929bc64`
Workflow commit: `630f9a3bea419d32ad9d38e1214daf7d9c0463db`
Authoritative run: `34915420210`
Job: `104211875981` (`momentum-vertex-generator`)
Artifact: `10375867797` (`iter131-explicit-momentum-vertices`)
Artifact SHA256: `30a58134151946466742172d709d95e0ec22477f8be327f4905177226557fa3d`

## Scientific classification

`PASS_SCOPED_EXPLICIT_R2_GAMMA2_MOMENTUM_TENSOR_GENERATOR_CLOSED`

All preregistered checks passed in the authoritative GitHub Actions run:

- explicit component tables were generated;
- R2 Bose symmetry passed;
- Gamma2 lower-index symmetry passed;
- Gamma2 graviton-leg Bose symmetry passed;
- held-out plane-wave polarization check passed;
- R2 degree-2 and Gamma2 degree-1 momentum homogeneity passed;
- construction remained target-independent.

The artifact contains 9 R2 components and 72 Gamma2 components for the deterministic D=2 symmetric-leg component generator used by this gate.

## Scope note for downstream 4D use

The canonical indexed ITER130 formulas are dimension-independent, but the concrete ITER131 machine table is D=2. Therefore ITER131 closes the explicit component-generator method and its frozen gate, while a separate direct D=4 transfer audit is required before these vertices are admitted into the physical four-dimensional M/G pole-numerator calculation. That transfer check is not a new loop result and does not alter the ITER131 preregistered classification.

No loop pole, B1, noncancellation, EDT match, bridge, new physics or candidate theory is implied.
