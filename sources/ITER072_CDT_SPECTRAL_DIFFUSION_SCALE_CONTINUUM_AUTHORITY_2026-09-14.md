# ITER072 source authority — CDT spectral-diffusion scale / continuum

Date: 2026-09-14
Gate: `ITER072_CDT_SPECTRAL_DIFFUSION_SCALE_CONTINUUM_AUTHORITY`
Preregistration commit: `3cc0751629f6c3cf3eb2ba5bb89c1fcccbef439e`
Metadata-correction commit: `bfb8f7fab32f5bdf021c61e6ffc6b6adc397ad99`

## Frozen sources

- arXiv:1603.02076 — J. Ambjorn, D. Coumbe, J. Gizbert-Studnicki, J. Jurkiewicz, *Searching for a continuum limit in causal dynamical triangulation quantum gravity*.
- arXiv:1411.7712 — D. N. Coumbe, J. Jurkiewicz, *Evidence for Asymptotic Safety from Dimensional Reduction in Causal Dynamical Triangulations*.
- arXiv:2604.05641 — J. Ambjørn, R. Loll, *Causal Dynamical Triangulations: New Lattice Theory of Quantum Gravity*.

The correction after preregistration changed bibliographic labels only. The arXiv identifiers, scientific question, predicates, classifications and controls were unchanged.

## Authority result in one sentence

4D CDT has a source-defined internal calibration of spectral-diffusion scale changes, including an explicit `sigma/a_rel^2` rescaling and an independent semiclassical estimate of absolute lattice spacing in Planck units, but the frozen stack does not establish a terminal continuum-limit theorem or ultraviolet fixed point.

## Predicate A — diffusion duration and lattice-spacing scaling

**PASS_SCOPED.**

The 2016 source starts from the heat equation and its covariant Laplacian, then discretizes fictitious diffusion time as integer diffusion steps `sigma` on the dual lattice. To compare spectral-dimension curves between bare-coupling points it explicitly states that `sigma` must be rescaled by `a_rel^2`, because the diffusion operator contains a squared covariant derivative.

The fitted form is

`D_S(sigma) = a - b / (c + sigma/a_rel^2)`.

This is stronger than the qualitative statement that `sqrt(sigma)` probes a distance. It supplies the source-defined relative scaling law required by ITER072.

It does not by itself make `sqrt(sigma)` an absolute physical length; that stronger promotion remains controlled separately.

## Predicate B — relative spectral lattice-spacing estimator

**PASS.**

`a_rel` is chosen to maximize the overlap of spectral-dimension curves after the `sigma/a_rel^2` rescaling, relative to a canonical point assigned `a_rel = 1`. The source uses a standard-deviation comparison over selected central `D_S(sigma)` values to locate the best overlap.

## Predicate C — application and uncertainties

**PASS_SCOPED.**

The estimator is applied at eight points in the phase-C bare parameter space. The source reports `a_rel` values and an uncertainty procedure based on the displacement of the overlap minimum under allowed spectral-dimension error envelopes.

Important retained qualifier: close to the C-A transition the source warns that the quoted `a_rel` uncertainty is likely significantly underestimated because of the constrained large-distance fit and asymmetric comparison procedure.

Representative normalized values reported by the source include:

- canonical point P1: `a_rel = 1`;
- P2: `a_rel = 0.791 +/- 0.008`;
- P3: `a_rel = 0.336 +/- 0.006`;
- P4: `a_rel = 0.116 +/- 0.001`.

These numbers are authority for the estimator in the sampled regulated ensembles, not a continuum extrapolation.

## Predicate D — independent absolute calibration

**PASS_SCOPED_WITH_MODEL_ASSUMPTIONS.**

The independent method uses the semiclassical phase-C volume profile and fluctuations around an effective Euclidean de Sitter/minisuperspace description. Matching the discrete effective action to the continuum minisuperspace action yields

`G = [sqrt(C4) s0^2 / (3 sqrt(6))] Gamma a_abs^2`

and hence an absolute lattice-spacing estimate of the form

`a_abs = sqrt[3 sqrt(6)/(sqrt(C4) s0^2 Gamma)] l_Pl`.

The source reports `a_abs` in Planck-length units at the sampled phase-C points.

This is an actual physical-scale estimate, but it is not representation-free: it depends on the phase-C semiclassical de Sitter/minisuperspace identification and on assumptions entering `C4` / spacelike-timelike simplex geometry. The source itself studies several variants of those assumptions.

## Predicate E — cross-check of relative and absolute estimators

**PASS_SCOPED / TREND-LEVEL AGREEMENT, NOT IDENTITY.**

The paper was designed to compare the two independent estimators. Both indicate that lattice spacing decreases strongly as `kappa_0` increases and is much less sensitive to `Delta` over the sampled region. The abstract and conclusions characterize the methods as yielding similar results, and normalized tables/figures compare them point by point.

The numerical estimators are not identical. For example, at the finest sampled points the spectral-overlap `a_rel` can decrease more strongly than the normalized de-Sitter `a_abs` estimators. Thus ITER072 records agreement as an independent directional/scale diagnostic, not as an exact equality of calibration schemes.

## Predicate F — discretization, finite size and fit windows

**PASS_SCOPED.**

The source explicitly controls or records:

- finite-volume growth of systematics at finer lattice spacing;
- use of larger ensembles near the C-A line;
- short-distance odd/even oscillations;
- omission of affected `D_S(sigma)` values from fits, typically once oscillations become significant;
- thermalization checks;
- bounded diffusion window;
- the possibility that near-transition uncertainty estimates are too small.

These effects remain part of the authority result.

## Predicate G — continuum limit / UV fixed point

**OPEN / EVIDENCE-LEVEL ONLY.**

The 2016 source is explicit about the logical standard: a UV limit requires `a -> 0` while observables are held fixed in physical units. Its measurements suggest a path of decreasing lattice spacing and propose tuning toward the C-A boundary, but it states that further study is needed to confirm or refute the proposed RG picture.

The 2026 review strengthens the evidence. It gives a finite-size-scaling criterion for a UV path and reports numerical behavior compatible with the required scaling exponent, interpreting this as evidence that the A-C_dS transition may be a UV critical line and that the cutoff tends toward zero along such paths. However, the review also records a remaining interpretational problem and the need for additional Monte Carlo work.

Under the preregistered ITER072 threshold, this is not promoted to `CONTINUUM_ESTABLISHED`: the status is candidate/evidence for a continuum path rather than a closed theorem or fully controlled continuum construction.

## Predicate H — no FRG import

**PASS_CONTROL.**

No QEG/FRG scale relation is needed for A-G. The CDT calibration is internally defined. Mapping it to QEG `k`, `1/k`, or a QEG heat-kernel scale remains unauthorized until a separate cross-school gate.

## Control audit

- `SQRT_SIGMA_PHYSICAL_LENGTH_PROMOTION_CONTROL`: passes; no bare `sqrt(sigma)` is promoted to absolute length.
- `RELATIVE_ABSOLUTE_SCALE_SWAP_CONTROL`: passes; `a_rel` and `a_abs` remain distinct estimators.
- `PHASE_BOUNDARY_CONTINUUM_CONTROL`: passes; boundary approach is not called a completed continuum limit.
- `TWO_ESTIMATOR_AGREEMENT_CONTROL`: passes; agreement strengthens calibration but does not prove a UV fixed point.
- `FINITE_SIZE_ERASURE_CONTROL`: passes; artifacts/fit windows are retained.
- `DE_SITTER_ASSUMPTION_ERASURE_CONTROL`: passes; the absolute Planck-scale estimate retains its semiclassical assumptions.
- `ANISOTROPY_ERASURE_CONTROL`: passes; spacelike/timelike and `C4` assumptions remain visible.
- `FRG_IMPORT_CONTROL`: passes.

## Source-authority classification

**`PASS_SCOPED_CDT_DIFFUSION_SCALE_CALIBRATED_CONTINUUM_OPEN`**

Retained locks:

- `CONTINUUM_LIMIT_ESTABLISHED = false`
- `UV_FIXED_POINT_ESTABLISHED = false`
- `RELATIVE_SPECTRAL_SCALE_AUTHORITY = true`
- `ABSOLUTE_LATTICE_SCALE_AUTHORITY = true_scoped_semiclassical`
- `FRG_CDT_POINTWISE_PHYSICAL_SCALE_COMPARATOR = REQUIRES_SEPARATE_TYPED_CROSSWALK`

## Claim ceiling

This result does not establish a full continuum CDT theory, exact universality of spectral dimension, microscopic equivalence to QEG/FRG, `BRIDGE_DERIVED`, `UNIVERSAL_COMMON_PARENT_FOUND`, new physics, or a candidate theory.