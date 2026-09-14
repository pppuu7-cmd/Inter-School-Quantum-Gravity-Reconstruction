# ITER082 source authority — CDT spatial Laplacian ↔ FRG mode-scale crosswalk

Date: 2026-09-15
Gate: `ITER082_CDT_SPATIAL_LAPLACIAN_FRG_MODE_SCALE_CROSSWALK_AUTHORITY`
Preregistration commit: `457ec94f4afab5c28c01851a8dbfd06ff6be91ad`
Production head: `251f3ef0bf6ded8ef10dfdbde285320603fe1ee5`
Authoritative run: `34901587377`

## Validated artifact provenance

- `1903.00430`: artifact `10371211441`, digest `sha256:31510fcb67db5b14aa2774e7bed0ebcb6b2544b2a41366311af9e14061a29b0f`.
- `1912.11311`: artifact `10370408325`, digest `sha256:3c7eda37c0ded2ddc0ebc4124cba4965fd83f7a57b0747d4286f6e60a17b1c9c`.
- `2203.08003`: artifact `10370813371`, digest `sha256:e626f695236387d19898e30ae075adbce3344f84e2d8332b74506627f45c8fda`.
- `2306.10408`: artifact `10370907646`, digest `sha256:2af1ba3944d25dfde9a38368cb2dbb55257a8637c5eb2832f5af9d23a2d5a3e5`.
- `2402.01260`: artifact `10371236406`, digest `sha256:d40ce82b5a297b7688d0802ed58f749de55e7d5ce6a299537aadbf1089528491`.
- aggregate: artifact `10370828341`, digest `sha256:f3d48bbb6417c505877835cdf37b493d838f2a12eaad00548631c873c8bfe672`.

All source jobs and aggregate completed technically successfully. Green CI is not scientific PASS; the classification below comes from the frozen manual typed audit.

## Key source facts

### CDT spatial operator

The CDT sources explicitly define the graph/Laplace-Beltrami operator on spatial slices. Spatial tetrahedra are represented by the dual graph, and the low eigenvalues are interpreted as diffusion rates / squared wavenumbers. The spectral gap and low modes carry inverse-length-squared meaning and exhibit finite-size and critical scaling.

Predicate A: **PASS**.

### Covariant FRG spectral object

The covariant spectral-geometry source defines the background-spacetime Laplacian/d'Alembertian eigenproblem and regulator threshold modes with eigenvalues of modulus `k^2`. This is a four-dimensional effective-spacetime object and therefore does not by itself close the CDT slice mismatch.

### Foliated FRG spatial regulator — substantive positive result

The frozen foliated FRG source `2306.10408` explicitly states that, in the foliated setting, one may choose a regulator differential operator containing no time derivatives and discriminate modes using the Laplacian constructed on the spatial hypersurfaces,

`Box_spatial = - sigma_bar^{ij} Dbar_i Dbar_j`.

The source explains that this spatial operator can supply the `k`-dependent mass term and render the functional trace finite. It also retains the caveat that this introduces a non-covariant regulator choice and can source diffeomorphism-violating effects.

This means ITER081's strongest type obstruction is partially reduced: an FRG spatial-slice coarse-graining operator genuinely exists in the frozen source stack.

Predicate B: **PASS_SCOPED**.

### Missing cross-framework map

None of the frozen sources derives an embedding or identification from a CDT triangulated spatial slice / dual graph to the continuum ADM spatial hypersurface used in FRG. The sources do not provide a source-defined conversion from dimensionless graph eigenvalues to the continuum spatial-Laplacian eigenvalues entering the FRG regulator.

Predicate C: **NO**.
Predicate D: **NO**.

### Mode-to-k rule

On the FRG side, the regulator construction genuinely distinguishes spatial modes relative to the coarse-graining scale `k`; thus the mode-scale semantics are explicit within FRG. However, the source stack does not establish that a particular CDT eigenvalue is numerically equal to the FRG cutoff threshold `k^2`, nor does it fix the cross-framework proportionality/normalization.

Predicate E: **PASS_FRG_INTERNAL / CROSS_FRAMEWORK_OPEN**.

### Controls

- `SPATIAL_SLICE_FULL_SPACETIME_CONTROL`: no longer the sole obstruction because foliated FRG supplies a spatial operator, but covariant and foliated operators remain distinct.
- `FOLIATION_IS_NOT_OPERATOR_MAP_CONTROL`: **passes**; the positive result is based on an explicit spatial Laplacian regulator, not foliation language alone.
- `EIGENVALUE_K_CONTROL`: **triggered cross-framework**; `lambda_CDT = k^2` remains unauthorized.
- `NORMALIZATION_FREE_PARAMETER_CONTROL`: **triggered**.
- `MODE_NUMBER_RETUNING_CONTROL`: **passes as lock**; no mode was selected by target fitting.
- `ANISOTROPY_LAPSE_CONTROL`: **retained**; ADM temporal/spatial structure is not erased.
- `PHASE_ORDER_PARAMETER_CONTROL`: **retained**.

## Scientific classification

**`PASS_SCOPED_FOLIATED_OPERATOR_CANDIDATE_MAP_NORMALIZATION_OPEN`**

This is a real scoped positive result: an FRG spatial coarse-graining operator of the right broad mathematical type exists. It is not yet a CDT↔FRG crosswalk because the discrete-to-continuum domain/normalization map and cross-framework eigenvalue-to-`k` calibration are missing.

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Next admissible work

Two independent high-information successors are allowed:

1. a source-authority gate for a discrete CDT graph-Laplacian ↔ continuum spatial-Laplacian normalization/domain map, including whether lattice spacing and finite-volume scaling fix the conversion prospectively;
2. the independent ITER081 secondary route comparing CDT quantum Ricci curvature to FRG relational scalar curvature with a strict finite-radius/local-composite typed-map gate.

Neither may use target fitting or post-hoc normalization.