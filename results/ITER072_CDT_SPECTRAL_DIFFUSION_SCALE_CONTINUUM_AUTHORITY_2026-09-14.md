# ITER072 terminal result — CDT spectral-diffusion scale / continuum authority

Date: 2026-09-14
Gate: `ITER072_CDT_SPECTRAL_DIFFUSION_SCALE_CONTINUUM_AUTHORITY`
Preregistration commit: `3cc0751629f6c3cf3eb2ba5bb89c1fcccbef439e`
Metadata-correction commit: `bfb8f7fab32f5bdf021c61e6ffc6b6adc397ad99`
Source-authority commit: `c341d4191c9db02af027b80d997ac622f9c7dcc1`
Adversarial critic commit: `57de6150d6ffe0f681ed8daf8c0dfd58f766f310`

## Terminal scientific classification

**`PASS_SCOPED / CDT_DIFFUSION_SCALE_CALIBRATED_CONTINUUM_OPEN`**

Retained locks:

- `CONTINUUM_LIMIT_ESTABLISHED = false`
- `UV_FIXED_POINT_ESTABLISHED = false`
- `RELATIVE_SPECTRAL_SCALE_AUTHORITY = true`
- `ABSOLUTE_LATTICE_SCALE_AUTHORITY = true_scoped_semiclassical`
- `FRG_CDT_POINTWISE_PHYSICAL_SCALE_COMPARATOR = REQUIRES_SEPARATE_TYPED_CROSSWALK`

Bridge credit: **0**.

## Question adjudicated

Does 4D CDT itself provide a source-defined map from spectral-diffusion duration in lattice units to changes in lattice/physical scale, and does that evidence already establish the continuum limit required for a universal spectral comparator?

## Result

The scale-calibration question passes in scope. The continuum-limit question remains open.

### Relative spectral calibration

The 2016 CDT source explicitly derives and uses the rescaling

`D_S(sigma) = a - b / (c + sigma/a_rel^2)`

where the squared factor follows from the covariant Laplacian in the diffusion equation and `a_rel` is determined by best overlap of measured spectral-dimension curves at different bare-coupling points.

The method is applied at eight sampled points and includes an uncertainty procedure. Thus `sigma` is not merely an ordinal short/long-distance label: changes of its scale between ensembles are tied to a measured relative lattice-spacing parameter.

### Independent absolute calibration

A second method matches the measured phase-C volume fluctuations to an effective Euclidean de Sitter/minisuperspace action. It yields

`G = [sqrt(C4) s0^2/(3 sqrt(6))] Gamma a_abs^2`

and therefore an estimate of `a_abs` in Planck units.

This supplies a physical-scale anchor, but only within the source's explicit semiclassical and simplex-geometry assumptions. Several `C4` prescriptions are studied; spacelike/timelike anisotropy and breakdown of the most general prescription in part of the transition region are not erased.

### Cross-check

The relative spectral estimator and the de-Sitter fluctuation estimator are compared on the same sampled parameter points. They agree on the principal direction of scale change — strong decrease with increasing `kappa_0` and much weaker dependence on `Delta` in the sampled region — but they are not numerically identical.

The correct result is therefore a calibrated, multi-estimator scale diagnostic, not an exact universal ruler.

## Predicate results

- A — explicit `sigma`/lattice-spacing scaling law: **PASS_SCOPED**.
- B — explicit relative spectral estimator: **PASS**.
- C — estimator applied with reported errors/procedure: **PASS_SCOPED**.
- D — independent absolute Planck-scale calibration: **PASS_SCOPED_WITH_MODEL_ASSUMPTIONS**.
- E — relative/absolute estimator comparison: **PASS_SCOPED / TREND-LEVEL AGREEMENT**.
- F — finite-size/discretization/fit-window controls: **PASS_SCOPED**.
- G — controlled continuum limit / UV fixed point established: **OPEN / EVIDENCE-LEVEL ONLY**.
- H — no FRG import: **PASS_CONTROL**.

This predicate pattern maps exactly to the preregistered classification:

**`PASS_SCOPED_CDT_DIFFUSION_SCALE_CALIBRATED_CONTINUUM_OPEN`**.

## Why continuum remains open

The 2016 source defines the correct criterion: a UV limit requires `a -> 0` while physical observables remain fixed. It then reports decreasing lattice-spacing estimators and proposes a trajectory toward the C-A region, explicitly stating that further study is required to confirm the proposal.

The 2026 CDT review strengthens the status substantially. It reports finite-size-scaling behavior compatible with a UV critical path and an exponent consistent with the required growth of the relevant combination of observables, and interprets this as evidence that the cutoff can tend to zero near the candidate critical line. But it also retains an interpretational problem and the need for further Monte Carlo sharpening.

ITER072's frozen threshold does not convert `evidence suggests` plus unresolved interpretation into `CONTINUUM_ESTABLISHED`.

## Adversarial critic

The critic attempted to:

- demote the result to relative-scale-only because `a_abs` is model-dependent;
- reject the spectral estimator as a curve-collapse degeneracy;
- promote two-estimator agreement to a UV fixed-point proof;
- use the 2026 review to claim the continuum theory is complete;
- make direct FRG/CDT scale matching automatic once Planck units are available.

None succeeds.

The absolute estimate is source-defined but conditional; the spectral estimator is independently data-constrained but has systematics; the two methods support scale calibration rather than a fixed-point theorem; and a cross-school physical-scale identification still requires an explicit typed map.

Critic verdict: **CONFIRMS terminal classification**.

## Structural consequence

ITER071 and ITER072 together change the frontier materially:

1. the FRG/QEG and CDT spectral dimension is a source-qualified common observable definition;
2. 4D CDT is no longer blocked merely because diffusion steps lack any scale calibration;
3. CDT now has a scoped relative calibration and an independent semiclassical physical-scale anchor;
4. the remaining cross-school blocker is the exact typed crosswalk between the two scale-setting procedures, not the absence of a CDT ruler;
5. the continuum/UV status must remain separate from finite-regulator scale matching.

## Downstream authorization

A new, separately preregistered cross-school scale gate is authorized:

**`PREREGISTER_ITER073_FRG_CDT_SPECTRAL_PHYSICAL_SCALE_CROSSWALK`**.

ITER073 may ask whether there exists a controlled overlap window in which:

- CDT diffusion duration is converted through its source-defined lattice-scale calibration;
- QEG diffusion duration is related to Laplacian-mode / RG resolution without identifying diffusion time with RG time;
- both sides are expressed in compatible dimensionless or Planck-normalized physical resolution;
- finite-size, anisotropy, regulator and truncation assumptions remain explicit;
- the resulting `D_s` values are compared only after the scale map is frozen.

Even a successful comparator would not establish microscopic equivalence.

## Claim ceiling

ITER072 does **not** establish:

- a completed CDT continuum theory;
- a CDT UV fixed point as a terminal theorem;
- universal short-distance spectral dimension;
- FRG/CDT equivalence;
- `BRIDGE_DERIVED`;
- `UNIVERSAL_COMMON_PARENT_FOUND`;
- new physics;
- a candidate theory.

`CANDIDATE_THEORY = UNFORMED`

`THEORY_ESTABLISHED = 0%`

`BRIDGE_CREDIT = 0`