# ITER081 terminal result — second independent CDT/FRG observable discovery

Date: 2026-09-15
Gate: `ITER081_CDT_FRG_SECOND_INDEPENDENT_REDUCED_OBSERVABLE_DISCOVERY`
Preregistration commit: `57511d4110e33bbfbd978aef9a41840eda2b2895`
Source-authority commit: `c9111e106d747d353db68f72d852d998dd691893`

## Terminal classification

**`PASS_SCOPED_SPATIAL_LAPLACIAN_SCALE_CANDIDATE_ONLY`**

Secondary retained candidate:

**`RELATIONAL_CURVATURE_SECONDARY_CANDIDATE_REQUIRES_TYPED_MAP`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## What was established

The low-lying Laplace-Beltrami spectrum measured on CDT spatial slices is operationally independent of the reduced volume-profile/effective-action data used by ITER078. Its spectral gap and low eigenvalues carry inverse-length-squared scale information and show critical behavior near the `C_b-C_dS` transition.

FRG spectral geometry contains a genuinely scale-sensitive spectral family, and the cutoff construction singles out modes of order `k^2`. This makes the CDT slice spectrum a high-information comparator candidate rather than another repackaging of the reduced action sector.

## Mandatory obstruction retained

The CDT operator acts on three-dimensional spatial slices. The frozen FRG spectral-geometry source acts on the running four-dimensional self-consistent effective spacetime. No source-qualified slicing/embedding/operator-normalization map identifies a CDT slice eigenvalue with the FRG mode-resolution scale.

Therefore:

- `lambda_1 = k^2` is **not authorized**;
- no numerical second theory-space constraint is established;
- no operational `k` normalization is established;
- no out-of-sample validation of ITER078 is established.

## Controls

- `SAME_REDUCED_ACTION_DATA_CONTROL`: triggered for residual transfer/effective-action coefficients; they receive no independent-observable credit.
- `SPATIAL_SLICE_FULL_SPACETIME_CONTROL`: triggered and retained.
- `EIGENVALUE_K_CONTROL`: triggered and retained.
- `QRC_RELATIONAL_SCALAR_CONTROL`: triggered; relational scalar curvature remains only a secondary candidate requiring its own typed-map gate.

## Exact successor

`ITER082_CDT_SPATIAL_LAPLACIAN_FRG_MODE_SCALE_CROSSWALK_AUTHORITY`

The successor must test source authority for a 3D spatial-operator / FRG mode-scale map, including foliated/ADM FRG sources, without target fitting or post-hoc normalization.

## Claim locks

No `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`, full theory equivalence or shared UV fixed point claim is authorized.