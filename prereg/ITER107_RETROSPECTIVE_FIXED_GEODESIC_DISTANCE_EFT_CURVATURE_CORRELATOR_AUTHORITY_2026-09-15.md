# ITER107 protocol — retrospective fixed-geodesic-distance EFT curvature-correlator authority

Date: 2026-09-15
Gate: `ITER107_RETROSPECTIVE_FIXED_GEODESIC_DISTANCE_EFT_CURVATURE_CORRELATOR_AUTHORITY`
Protocol status: **RETROSPECTIVE SOURCE-DISCOVERY AUDIT / predictive credit 0**

## Motivation

ITER106 established that the historical EDT curvature correlator and the 2026 low-energy EFT curvature correlator share a scalar-curvature field but differ in relational localization: fluctuating geodesic-distance conditioning versus harmonic/master-coordinate separation.

Before this protocol was registered, a perturbative continuum precedent at fixed fluctuating geodesic distance was located: arXiv:1706.01891 (Fröb), which computes a scalar-field two-point function with one-loop graviton corrections. Therefore ITER107 is retrospective and cannot receive prospective validation credit.

## Frozen sources

1. arXiv:1706.01891 / Class. Quantum Grav. 35, 055006 (2018) — M. B. Fröb, *One-loop quantum gravitational corrections to the scalar two-point function at fixed geodesic distance*.
2. arXiv:2510.11888 / Phys. Rev. D 113, 106032 (2026) — Laiho & Ratliff, master-coordinate relational curvature correlator.
3. arXiv:hep-lat/9503004 — EDT fixed dynamical-distance curvature correlator, used only to type the target scheme.
4. ITER106 only as prior type/claim authority.

## Frozen question

Does the perturbative quantum-gravity literature already provide a renormalized scalar-curvature two-point function at fixed **fluctuating geodesic distance** that can be compared to EDT? If not, does it at least source-qualify the fixed-geodesic-distance observable and reveal which additional renormalization structures make the calculation nontrivially different from the 2026 master-coordinate correlator?

## Required predicates

A. A continuum perturbative definition of a two-point function at fixed geodesic distance in the fluctuating metric must be explicit.

B. Gauge independence/diffeomorphism invariance and renormalization of the geodesic-distance construction must be source-qualified.

C. A full PASS requires the inserted local operators themselves to be scalar curvature `R` (or an explicitly equivalent curvature composite), not a matter scalar field.

D. Renormalization specific to the geodesic embedding/distance observable must be retained; it cannot be absorbed silently into ordinary local curvature counterterms.

E. The fixed-geodesic result must not be obtained by replacing the 2026 master-coordinate separation `r` with `d_g` after the calculation.

F. EDT's normalized shell conditioning and distance-dependent connected subtraction remain separate issues unless the continuum source reproduces them.

G. No historical EDT exponent may be used to choose finite counterterms or renormalization conditions.

## Frozen classifications

- `PASS_SCOPED_FIXED_GEODESIC_CURVATURE_CORRELATOR_EFT_AUTHORITY` if A-F pass with an explicit curvature calculation.
- `PASS_SCOPED_FIXED_GEODESIC_PERTURBATIVE_FORMALISM_EXISTS_CURVATURE_CALCULATION_OPEN` if A-B/D-E pass but the explicit calculation is only for another field/operator.
- `SCOPED_BLOCKED_FIXED_GEODESIC_OBSERVABLE_NOT_RENORMALIZABLE` only if the source establishes a genuine obstruction.
- `BLOCKED_SOURCE_AUTHORITY` if the fixed-geodesic formalism itself is insufficiently explicit.

## Controls

- `MATTER_SCALAR_CURVATURE_SWAP_CONTROL`
- `MASTER_DISTANCE_GEODESIC_SUBSTITUTION_CONTROL`
- `GEODESIC_EMBEDDING_RENORMALIZATION_ERASURE_CONTROL`
- `SHELL_CONDITIONING_CONTROL`
- `CONNECTEDNESS_CONTROL`
- `RETROSPECTIVE_CREDIT_CONTROL`

## Claim ceiling

A PASS of the formalism does not establish the EDT curvature exponent, does not convert `r^-8` into a geodesic-distance prediction, and cannot establish continuum EDT, a bridge derivation, new physics or a candidate theory.