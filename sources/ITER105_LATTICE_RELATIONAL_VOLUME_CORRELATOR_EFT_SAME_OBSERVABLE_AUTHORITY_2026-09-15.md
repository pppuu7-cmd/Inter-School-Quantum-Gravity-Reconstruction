# ITER105 source authority — CDT global slice-volume covariance versus EFT relational volume correlator

Date: 2026-09-15
Gate: `ITER105_LATTICE_RELATIONAL_VOLUME_CORRELATOR_EFT_SAME_OBSERVABLE_AUTHORITY`
Preregistration: `5f974a058cce39805b7d25b82eb472f81cbefcbf`

## 1. EFT target object

arXiv:2510.11888 / Phys. Rev. D 113, 106032 (2026) constructs diffeomorphism-invariant observables using harmonic coordinate scalars `X^mu` built from the fluctuating metric. Its volume observable is the invariantized local four-dimensional volume factor

`sqrt(det G)(X)`

(up to Euclidean/Lorentzian determinant-sign conventions), and the paper computes the point-to-point two-point function of this object through one loop. The correlator is a function of the four-dimensional source-sink separation in the relational/master-coordinate frame. Coordinate-correction terms are essential for gauge invariance.

Predicate A: **PASS**.

## 2. CDT target object

arXiv:1510.08719 measures the covariance of global spatial-volume fluctuations,

`C_tt' = <delta n_t delta n_t'>`,

where `n_t` is the discrete spatial three-volume on the preferred CDT slice labelled by discrete proper time `t`. The covariance is related to the inverse Hessian of the reduced effective action for the slice-volume profile.

This is an integrated hypersurface observable / constant spatial mode, not a point-local four-volume density.

Predicate D: **PASS**.

## 3. Spatial integration of the EFT operator does not automatically produce CDT `N_3(t)`

The local EFT operator is the four-volume factor `sqrt(g_4)`. At fixed relational time `X^0`, integrating

`int d^3 X sqrt(g_4)`

over the remaining master coordinates yields a lapse-weighted hypersurface density in a generic 3+1 decomposition. The intrinsic spatial three-volume instead uses `sqrt(h_3)`.

A source-defined lapse/shift or unit-lapse physical-frame reduction would be required to identify these objects. The frozen EFT paper does not derive such a projection for the volume correlator, and it works perturbatively around flat spacetime rather than a compact CDT foliation.

Thus the proposed projection is not source-equivalent to `N_3(t)`.

Predicate B: **FAIL_FOR_SAME_OBJECT**.
`LOCAL_DENSITY_GLOBAL_VOLUME_SWAP_CONTROL`: **TRIGGERS**.

## 4. Time/separation semantics are also different

The EFT master coordinates are harmonic scalar functionals of the full metric. The CDT label `t` is the preferred discrete proper-time foliation built into causal triangulations.

No frozen source defines `X^0 <-> t` or shows that constant-harmonic-time hypersurfaces coincide with the CDT slices.

Predicate C: **OPEN / TYPE MISMATCH**.
`HARMONIC_TIME_PROPER_TIME_SWAP_CONTROL`: **TRIGGERS**.

## 5. Fixed-total-volume conditioning is a second independent obstruction

The CDT covariance measurements are performed in ensembles with total four-volume constrained/fixed (or tightly volume-fixed), producing a constrained global mode and associated covariance/Hessian treatment.

The low-energy EFT correlator is an unconstrained local correlator about flat space. Its universal noncontact result does not include the CDT global fixed-volume conditioning projector.

A valid global comparison would require projecting/removing the constant four-volume mode in the continuum observable with the same ensemble semantics.

Predicate E: **OPEN / NOT SOURCE-DERIVED**.
`FIXED_VOLUME_UNCONSTRAINED_COVARIANCE_CONTROL`: **TRIGGERS**.
`ZERO_MODE_ERASURE_CONTROL`: **TRIGGERS**.

## 6. Normalization and regime

CDT `n_t` is a simplex count converted to physical three-volume through lattice-spacing and simplex-volume conventions. The EFT operator has continuum density normalization in the perturbative relational frame.

Because the underlying operator and hypersurface map already fail, normalization alone cannot rescue the comparison. The EFT result is an IR/low-energy prediction, while the CDT covariance is usually interpreted through a compact de-Sitter minisuperspace sector at finite regulator.

Predicates F-G: **OPEN / NOT REACHED FOR SAME-OBJECT PASS**.

## 7. Predicate adjudication

- A EFT relational local volume correlator: **PASS**.
- B source-defined projection to the CDT spatial three-volume: **NO**.
- C harmonic master time versus CDT proper time: **NO MAP**.
- D CDT global slice-volume covariance typed: **PASS**.
- E fixed-volume conditioning crosswalk: **NO**.
- F absolute normalization: **OPEN**.
- G common IR regime for this object: **OPEN**.
- H no FRG/QRC forcing: **PASS_CONTROL**.

## Source classification

**`FAIL_SCOPED_LOCAL_EFT_VOLUME_AND_CDT_SLICE_VOLUME_OBSERVABLE_IDENTITY_REJECTED`**

The failure is a useful type result. The 2026 EFT volume correlator is not the continuum version of the already-published CDT `N_3(t)` covariance merely by spatial integration. They are different observables with different dimensionality, hypersurface/time semantics and ensemble conditioning.

## Highest-information successor

The EFT paper's curvature-curvature correlator is a better candidate because both continuum and dynamical-triangulation literature define scalar-curvature two-point functions at a separation. Audit observable identity there, paying special attention to:

- relational master-coordinate separation versus dynamical geodesic distance;
- distance-conditioned one-point subtraction in triangulations;
- local Regge curvature normalization;
- source/shell averaging and measure factors;
- the EFT long-distance prediction `~ G^2/r^8` away from contact terms.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No statement about the correctness of either theory follows from this type mismatch.