# ITER105 preregistration — CDT global volume covariance ↔ low-energy EFT relational volume correlator same-observable authority

Date: 2026-09-15
Gate: `ITER105_LATTICE_RELATIONAL_VOLUME_CORRELATOR_EFT_SAME_OBSERVABLE_AUTHORITY`

## Motivation frozen before EFT correlator extraction

ITER104 saturated the currently located AS-FRG tensor-composite route. A new 2026 low-energy quantum-gravity calculation provides diffeomorphism-invariant relational curvature and volume two-point functions explicitly proposed as comparators for nonperturbative lattice gravity.

CDT independently publishes a connected covariance matrix of spatial three-volume fluctuations. ITER105 asks whether these can be typed as the same observable after a source-defined spatial integration/projection, rather than matched merely because both concern volume fluctuations.

## Frozen sources

- arXiv:2510.11888 / Phys. Rev. D 113, 106032 (2026) — Laiho & Ratliff, *Euclidean correlation functions in quantum gravity*.
- arXiv:1510.08719 — 4D CDT spatial-volume covariance/effective-action reconstruction.
- arXiv:2408.07808 — direct reduced CDT↔continuum minisuperspace conventions and global-volume mode typing.
- ITER089 only as prior authority that the CDT covariance is the inverse Hessian of the global reduced action; it may not be used to assume observable identity with EFT.

## Frozen question

Does the EFT relational volume operator/correlator admit a source-defined projection onto constant-spatial-mode hypersurface volumes such that its connected two-point function can be identified with the CDT object

`C_tt' = <delta N_3(t) delta N_3(t')>`

up to explicit lattice/continuum normalization and fixed-total-volume conditioning?

## Required predicates

A. The EFT paper must define the relational volume observable and its connected two-point function with explicit coordinate/separation semantics.

B. The local EFT volume observable must admit a source-defined or mathematically unambiguous integration over a physical spatial hypersurface to a three-volume observable.

C. The EFT physical/master time labeling those hypersurfaces must be typed against CDT discrete proper time; equality cannot be assumed from both being one-dimensional labels.

D. CDT `N_3(t)` must be identified as the appropriate integrated spatial-volume variable with its alignment/centering and ensemble conventions retained.

E. Fixed-total-four-volume conditioning and the corresponding zero/constant-mode constraint must be accounted for before comparing connected covariance kernels.

F. Lattice spacing, simplex-volume and continuum density normalization must remain explicit; a shape-only comparison may be separately classified if absolute normalization is open.

G. The EFT perturbative/IR domain and CDT finite-regulator/semiclassical domain must admit an overlap interpretation; no UV/continuum claim follows from a formal projection alone.

H. No FRG coupling map or QRC result may be imported to force the volume correlators to agree.

## Frozen classifications

- `PASS_SCOPED_SAME_INTEGRATED_VOLUME_CORRELATOR_COMPARATOR_AUTHORIZED` if A-G pass with explicit normalizations/conditioning.
- `PASS_SCOPED_COMMON_CONSTANT_MODE_VOLUME_OBJECT_TIME_AND_CONDITIONING_MAP_OPEN` if the spatial integration gives the same abstract volume object but C/E/F remain unresolved.
- `FAIL_SCOPED_LOCAL_EFT_VOLUME_AND_CDT_SLICE_VOLUME_OBSERVABLE_IDENTITY_REJECTED` if even the integrated observable types are incompatible.
- `BLOCKED_SOURCE_AUTHORITY` if the frozen sources do not expose enough correlator/hypersurface information.

## Controls

- `LOCAL_DENSITY_GLOBAL_VOLUME_SWAP_CONTROL`
- `HARMONIC_TIME_PROPER_TIME_SWAP_CONTROL`
- `FIXED_VOLUME_UNCONSTRAINED_COVARIANCE_CONTROL`
- `ZERO_MODE_ERASURE_CONTROL`
- `NORMALIZATION_ERASURE_CONTROL`
- `IR_UV_PROMOTION_CONTROL`

## Claim ceiling

A PASS can authorize only an infrared relational-volume correlator comparator. It cannot establish continuum CDT, UV completion, FRG equivalence, a shared fixed point, `BRIDGE_DERIVED`, new physics or a candidate theory.