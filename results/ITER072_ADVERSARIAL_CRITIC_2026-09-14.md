# ITER072 adversarial critic — CDT spectral-diffusion scale / continuum authority

Date: 2026-09-14
Preregistration commit: `3cc0751629f6c3cf3eb2ba5bb89c1fcccbef439e`
Metadata-correction commit: `bfb8f7fab32f5bdf021c61e6ffc6b6adc397ad99`
Source-authority audit: `c341d4191c9db02af027b80d997ac622f9c7dcc1`

## Target

Attempt to falsify or strengthen:

`PASS_SCOPED_CDT_DIFFUSION_SCALE_CALIBRATED_CONTINUUM_OPEN`.

## Attack 1 — `sigma/a_rel^2` is dimensional analysis, not a measured scale

The `a_rel^2` dependence follows from the squared covariant derivative in the diffusion equation, but the value of `a_rel` is not inserted by hand: it is fitted by optimizing overlap of measured spectral-dimension curves at different bare-coupling points. The paper reports the estimator and an error procedure.

Therefore the scaling exponent alone is theoretical, but the relative scale factor is data-constrained.

**Verdict: relative-scale authority survives.**

## Attack 2 — curve collapse could be a shape-degeneracy rather than lattice-spacing change

This is a genuine vulnerability. A single observable can admit approximate reparameterizations, and near the C-A transition the authors constrain the large-distance fit and warn that some error estimates may be substantially underestimated.

However ITER072 does not rely on spectral collapse alone. The source compares it with a second estimator from volume fluctuations and obtains the same dominant direction of change with `kappa_0`. The magnitudes are not identical and are not promoted to exact equality.

**Verdict: scoped calibration survives; precision/universality claims do not.**

## Attack 3 — the Planck-scale `a_abs` estimate is circular

The absolute estimate identifies the coefficient of the semiclassical effective volume-fluctuation action with the continuum minisuperspace action and Newton constant. It therefore assumes that phase-C data can be interpreted through the Euclidean de Sitter/minisuperspace sector and that the matching coefficient is physically meaningful.

This is not a model-independent metrological determination of `a`. It is nevertheless an explicit source-defined physical-scale calibration conditional on stated semiclassical assumptions.

**Verdict: `ABSOLUTE_LATTICE_SCALE_AUTHORITY = true_scoped_semiclassical`; no stronger promotion.**

## Attack 4 — anisotropy invalidates a single lattice spacing

CDT distinguishes spacelike and timelike link lengths and uses an asymmetry parameter. The 2016 paper explicitly explores different assumptions for the effective simplex volume `C4`, including variants sensitive to the spacelike/timelike geometry, and notes breakdown/ambiguity of the most general method near part of the transition region.

Thus a single `a_abs` is an effective calibration within a specified geometric prescription, not an exact isotropic microscopic ruler.

**Verdict: calibration remains scoped; anisotropy lock is essential.**

## Attack 5 — agreement of two methods proves a continuum limit

Rejected. The two estimators diagnose how lattice spacing changes over sampled regulated points. They do not by themselves prove the existence of a second-order UV critical point, a divergent correlation length, or a trajectory along which all required observables remain fixed while `a -> 0`.

The 2016 paper uses deliberately provisional language: it proposes a route and says further study is needed.

**Verdict: no continuum promotion.**

## Attack 6 — the 2026 review closes the continuum question

The later review provides stronger evidence than the 2016 study: it presents finite-size-scaling behavior compatible with a UV path and states that the cutoff tends toward zero when the candidate critical line is approached. This is important positive evidence and must not be erased.

But the same review describes the UV result as numerical evidence, identifies an interpretational problem in the scaling variables/time extension, and calls for further Monte Carlo work. Under ITER072's frozen standard — a controlled source-established continuum construction rather than evidence for one — the stronger classification still does not pass.

**Verdict: `CONTINUUM_OPEN` remains the source-faithful ceiling.**

## Attack 7 — old phase-C language is obsolete after phase-diagram refinements

Later CDT work distinguishes the de Sitter phase and additional/bifurcation structure more carefully. This can change which path through bare-coupling space is considered physically promising. It does not erase the measured lattice-spacing estimators at the sampled ensembles, but it weakens any attempt to turn the 2016 proposed path into a universal RG trajectory.

**Verdict: scale estimator survives; old trajectory interpretation remains nonterminal.**

## Attack 8 — once `a_abs` is known, FRG/CDT pointwise matching is automatic

Rejected. A separate typed map is still required between:

- CDT dual-lattice random-walk duration / effective diffusion length;
- spacelike/timelike lattice scales and the chosen absolute calibration;
- QEG heat-kernel diffusion duration;
- QEG Laplacian eigenmode/RG resolution `k`.

Even if both sides can express scales in Planck units, matching units is not the same as proving equality of scale-setting procedures or averaging objects.

**Verdict: cross-school pointwise comparator remains separately gated.**

## Attack 9 — the classification should be only `RELATIVE_SCALE_ONLY`

Too weak. The frozen stack contains an independent, explicit formula for `a_abs` in Planck units and applies it at the same sampled parameter points. Its assumptions are substantial but recorded. The preregistration does not require assumption-free absolute metrology; it requires an explicit absolute calibration with assumptions visible.

**Verdict: `PASS_SCOPED_CDT_DIFFUSION_SCALE_CALIBRATED_CONTINUUM_OPEN` is preferred over `PASS_SCOPED_RELATIVE_SCALE_ONLY`.**

## Critic verdict

**CONFIRMS `PASS_SCOPED_CDT_DIFFUSION_SCALE_CALIBRATED_CONTINUUM_OPEN`.**

The strongest durable statement is:

- relative spectral diffusion scale calibration across sampled 4D CDT ensembles: **established in scope**;
- independent absolute lattice-spacing estimate in Planck units: **established conditionally on semiclassical/de-Sitter and simplex-geometry assumptions**;
- exact equality of the two estimators: **not established**;
- controlled UV continuum limit / fixed point: **evidence exists, not terminally established**;
- direct FRG/CDT physical-scale comparator: **not yet authorized**.

## Highest-information successor

The next gate can now move back across schools without pretending that CDT has no scale calibration:

`PREREGISTER_ITER073_FRG_CDT_SPECTRAL_PHYSICAL_SCALE_CROSSWALK`.

It should freeze an explicit map between CDT diffusion scale and QEG heat-kernel/RG resolution, carry the Planck-unit and regulator/anisotropy assumptions through the map, and test whether any overlap window exists in which both `D_s` curves can be compared at matched physical resolution. Similar values alone remain non-evidence for microscopic equivalence.