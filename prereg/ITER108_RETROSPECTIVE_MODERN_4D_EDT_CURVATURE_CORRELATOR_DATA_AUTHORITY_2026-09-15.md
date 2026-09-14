# ITER108 protocol — retrospective modern 4D EDT curvature-correlator data authority

Date: 2026-09-15
Gate: `ITER108_RETROSPECTIVE_MODERN_4D_EDT_CURVATURE_CORRELATOR_DATA_AUTHORITY`
Protocol status: **RETROSPECTIVE SOURCE/DATA AUDIT / validation credit permanently 0**

## Motivation

ITER106 showed that the historical 1995 EDT curvature correlator and the 2026 low-energy EFT relational curvature correlator share a scalar-curvature field but differ in relational separation and connectedness. ITER107 showed that fixed-geodesic-distance perturbation theory is a distinct renormalized observable and cannot be obtained by substituting `r -> d_g` in the master-coordinate result.

A more modern four-dimensional EDT curvature-correlator calculation exists in Scott Bassler's 2019 dissertation and 2018 Lattice conference work. Its qualitative power-law outcome was inspected before this protocol was registered. Therefore ITER108 is retrospective and cannot receive predictive-validation credit.

## Frozen sources

1. Scott D. Bassler, *Euclidean Dynamical Triangulations: Running Couplings and Curvature Correlation Functions* (PhD thesis, Syracuse University, 2019).
2. S. Bassler et al., *Curvature Correlators in Lattice Quantum Gravity*, Lattice 2018 conference contribution.
3. M. Asaduzzaman and S. Catterall, *Euclidean dynamical triangulations revisited*, Phys. Rev. D 107, 074505 (2023), used only as current phase/continuum-status authority.
4. arXiv:2510.11888 / Phys. Rev. D 113, 106032 (2026), used only to retain the master-coordinate EFT comparison ceiling.
5. ITER106–107 only as prior observable-typing authority.

## Frozen question

Does the modern EDT calculation provide a reproducible, multi-discretization curvature-correlator result with controlled disconnected subtraction, finite-size/lattice-spacing analysis and a source-reported universal power law? If yes, is that result strong enough for a direct exponent comparison to the 2026 EFT master-coordinate `r^-8` correlator, or does the geodesic-shell observable mismatch remain decisive?

## Required predicates

A. The local curvature variables and at least two discretizations must be explicit.

B. The dynamical distance and pair/shell normalization must be explicit.

C. The disconnected subtraction must be explicitly improved relative to the naive historical prescription and its fit parameters retained.

D. The fit ansatz, fit windows and ensemble exclusions/systematics must be source-recorded rather than summarized only by the final exponent.

E. A relative lattice-spacing procedure must be source-defined if continuum/lattice-spacing language is used.

F. The source-reported power in the claimed universal/infinite-volume/continuum regime must be recorded separately for both curvature discretizations, including uncertainties.

G. Lack of an absolute lattice spacing/Newton normalization must block a universal amplitude comparison where relevant.

H. Later phase-diagram evidence must be retained when assessing whether the 2019 extrapolation is an established continuum limit or a model-dependent continuum hypothesis.

I. EDT geodesic-shell separation and the 2026 EFT harmonic/master-coordinate separation must remain distinct; exponent equality/inequality cannot be interpreted as a direct theory test without a relational-distance map.

J. The already-inspected EDT power-law outcome receives validation credit 0.

## Frozen classifications

- `PASS_SCOPED_MODERN_EDT_CURVATURE_POWER_LAW_DATA_AUTHORITY_MASTER_COORDINATE_MAP_OPEN` if A-F pass but G-I retain the cross-framework ceiling.
- `PASS_SCOPED_MODERN_EDT_CORRELATOR_ESTIMATOR_AUTHORITY_CONTINUUM_POWER_OPEN` if the estimator is controlled but the continuum power is not source-stable.
- `SCOPED_BLOCKED_MODERN_EDT_CORRELATOR_SYSTEMATICS_DOMINATE` if fit/exclusion/discretization systematics prevent a source-qualified power-law statement.
- `INFRASTRUCTURE_FAIL` only if the frozen sources cannot be inspected.

## Controls

- `TWO_DISCRETIZATIONS_UNIVERSALITY_CONTROL`
- `FIT_WINDOW_RETUNING_CONTROL`
- `ENSEMBLE_EXCLUSION_CONTROL`
- `RELATIVE_ABSOLUTE_LATTICE_SCALE_CONTROL`
- `CONTINUUM_STATUS_PROMOTION_CONTROL`
- `GEODESIC_MASTER_COORDINATE_SWAP_CONTROL`
- `RETROSPECTIVE_POWER_CREDIT_CONTROL`

## Claim ceiling

A PASS can establish a modern lattice curvature-correlator datum only. It cannot by itself validate/falsify the 2026 EFT exponent, establish a continuum EDT quantum-gravity theory, derive a shared fixed point, `BRIDGE_DERIVED`, new physics or a candidate theory.