# ITER108 source authority — modern four-dimensional EDT curvature-correlator data

Date: 2026-09-15
Gate: `ITER108_RETROSPECTIVE_MODERN_4D_EDT_CURVATURE_CORRELATOR_DATA_AUTHORITY`
Protocol: `c2cd31a6abdfae7f40e65a369cafe8507528aba9`
Retrospective validation credit: **0**

## 1. Modern EDT curvature observables are explicitly defined in two discretizations

Bassler's 2019 four-dimensional degenerate-EDT analysis studies curvature correlations using two related but distinct local discretizations:

1. **triangle curvature**, based on the Regge deficit angle/order of a triangle and its associated dual volume;
2. **simplex curvature**, obtained by averaging the curvatures of the ten triangles in a four-simplex.

The triangle scalar curvature is explicitly affine in inverse triangle order for fixed equilateral simplices, so both discretizations target the same continuum scalar-curvature field while having different cutoff smearing.

Predicate A: **PASS**.

## 2. Distance and pair normalization are configuration-dependent and explicit

For triangle curvature, neighboring triangles are defined by a local combinatorial relation and distance is the minimal number of neighbor hops. The simplex discretization uses the analogous simplex graph distance.

For each configuration the unsubtracted correlator is a normalized average over sources and all targets at fixed dynamical distance. The distance shell and its multiplicity are therefore geometric observables themselves.

Predicate B: **PASS**.

## 3. Connected estimator improves on the 1995 subtraction

The thesis explicitly demonstrates the spurious disconnected correlation by replacing one curvature insertion with the identity. It first discusses the older de Bakker-Smit subtraction and then adopts the Ambjorn-Bialas-Jurkiewicz refinement.

The unnormalized shell correlators are

`G_AB(r) = sum_{x,y} A(x) B(y) delta_{r,d(x,y)}`.

The distance-conditioned one-point sector is fit by

`G_1R(r) = A G_11(r+delta)`

with constants `A` and distance shift `delta`; a cubic spline is used for noninteger shifted arguments. The connected curvature correlator is then

**`<RR>_c(r) = [G_RR(r) - A^2 G_11(r+2 delta)] / G_11(r)`**.

This explicitly accounts for the fact that the distance-shell volume itself is correlated with curvature and is materially stronger than subtracting a global `<R>^2`.

Predicate C: **PASS_SCOPED**.

## 4. Universal-window selection and fit systematics are source-visible

The source identifies three regimes:

- short distance: lattice/discretization artifacts;
- intermediate falloff: the candidate universal regime;
- long distance: asymptote and eventually baby-universe/finite-volume contamination.

The power-law fits use

`f(r) = a r^P + b`.

For each ensemble `r_min` and `r_max` are selected to retain the visible falloff while avoiding the asymptote and short-distance artifacts. Multiple fit ranges were tested. The source explicitly notes that the 8k `beta=-0.8` simplex fit is anomalous/poorly localized despite an acceptable nominal chi-square, and the coarsest 4k `beta=1.5` simplex ensemble is excluded because of a discretization-specific bump.

Therefore the final power is not a blind all-data fit; it is a source-reported universal-window analysis with non-negligible window/exclusion systematics.

Predicate D: **PASS_WITH_SYSTEMATICS**.
`FIT_WINDOW_RETUNING_CONTROL`: **ACTIVE / SOURCE CHOICES RECORDED**.
`ENSEMBLE_EXCLUSION_CONTROL`: **ACTIVE / EXCLUSIONS RECORDED**.

## 5. Relative lattice spacing is source-defined; absolute spacing is not

The same thesis determines relative lattice spacings by rescaling diffusion time in the return-probability curves so that different bare-coupling ensembles collapse onto a common curve. Since diffusion time has dimensions of length squared, the rescaling gives `a_rel^2`.

The representative table sets the `beta=0` ensembles to `a_rel=1`, with approximately

- `beta=1.5`: `a_rel=1.47(10)`;
- `beta=-0.8`: `a_rel=0.72(5)`.

The source explicitly leaves the **absolute** lattice spacing for future work; semiclassical estimates are discussed but are not a precision calibration.

Predicate E: **PASS_RELATIVE_ONLY**.
Predicate G: **ABSOLUTE NORMALIZATION OPEN**.
`RELATIVE_ABSOLUTE_LATTICE_SCALE_CONTROL`: **TRIGGERS**.

## 6. Source-reported modern curvature power

Individual fits in the candidate universal regime produce exponents clustered roughly around `-9` to `-12` for most triangle ensembles and around `-8` to `-9` for most simplex ensembles, with identified outliers/systematics.

To infer the reported infinite-volume/continuum power, the source compares the two discretizations and excludes the 32k `beta=0` point from the final constant fit on the argument that it has the largest physical volume but a relatively coarse lattice spacing and is especially susceptible to long-distance regulator artifacts.

The reported constants are:

- **triangle curvature:** `P = -10.03(35)`;
- **simplex curvature:** `P = -9.09(54)`.

The source describes the two discretizations as mutually consistent within the quoted accuracy and concludes that the power is **consistent with `-10`**.

Predicate F: **PASS_SOURCE_REPORTED**, with the fit/exclusion systematics above retained.
`TWO_DISCRETIZATIONS_UNIVERSALITY_CONTROL`: **PASS_SCOPED / NOT EXACT EQUALITY**.

## 7. The source's continuum interpretation is a hypothesis with explicit assumptions

The 2019 analysis interprets the observed cross-ensemble/discretization behavior using a line-of-constant-physics picture, relative lattice-spacing estimates and tuning of the measure parameter to restore regulator-broken diffeomorphism invariance. The exponent itself is summarized by a constant fit after the stated exclusion rather than by a high-leverage multi-parameter continuum extrapolation with many independent lattice spacings.

The source also explicitly acknowledges unresolved systematics in fit-window choice, long-distance asymptotes, baby universes and some excluded ensembles.

Subsequent 2023 four-dimensional EDT simulations with combinatorial triangulations and a local measure term find results **consistent with a line of first-order phase transitions**, with latent heat decreasing as the gravitational coupling grows. That later work reports broad universality with earlier degenerate/different-measure formulations but does not establish the higher-order critical point assumed by the strongest 2019 continuum interpretation.

Because the formulations/triangulation classes are not identical, the later result is not a direct falsification of the Bassler ensemble analysis. It does mean that `established continuum EDT` is too strong a label for the 2019 curvature exponent.

Predicate H: **CONTINUUM INTERPRETATION OPEN / MODEL-DEPENDENT**.
`CONTINUUM_STATUS_PROMOTION_CONTROL`: **TRIGGERS**.

## 8. Relation to the 2026 low-energy EFT prediction

The 2026 relational EFT calculation gives the universal noncontact master-coordinate result

`<R(X)R(Y)> = 768 G^2/(pi^2 r^8) + O(G^3)`.

The modern EDT correlator remains conditioned on **fluctuating combinatorial/geodesic distance** and uses the improved shell-volume connected estimator described above. ITER106-107 established that this is not source-equivalent to the 2026 harmonic/master-coordinate separation and that fixed-geodesic observables acquire their own perturbative renormalization.

Therefore the numerical difference between the source-reported EDT power near `-10` and the EFT master-coordinate power `-8` is **not yet a direct theory discrepancy**.

Predicate I: **MAP OPEN / DIRECT EXPONENT TEST NOT AUTHORIZED**.
`GEODESIC_MASTER_COORDINATE_SWAP_CONTROL`: **TRIGGERS**.

## 9. Retrospective lock

The approximate `-10` outcome was inspected before protocol registration. It receives **zero prospective validation credit** and cannot be used to redefine the EFT observable, distance variable, counterterms or lattice fit window.

Predicate J: **PASS_CONTROL; CREDIT=0**.

## Source classification

**`PASS_SCOPED_MODERN_EDT_CURVATURE_POWER_LAW_DATA_AUTHORITY_MASTER_COORDINATE_MAP_OPEN`**

This is substantially stronger lattice authority than the historical 1995 curvature correlator: the estimator explicitly corrects distance-shell disconnected contamination, two curvature discretizations are compared, relative lattice-spacing information is available, and a source-reported universal power consistent with `-10` is extracted.

The result still does not authorize a direct comparison to the 2026 `r^-8` master-coordinate EFT prediction because relational distance/renormalization semantics remain different and the EDT continuum interpretation is not independently closed.

## Highest-information successor

The discrepancy in nominal powers makes the distance-map question quantitative. The next gate should determine whether perturbative conversion from master-coordinate separation to a fluctuating geodesic-distance observable can change the **leading noncontact power** of a curvature correlator, or whether it can only add logarithms/subleading terms at the same canonical power. The known fixed-geodesic scalar-field calculation provides an authority template but not the curvature answer.

If leading-power stability can be established generically, the `-10` versus `-8` difference becomes a sharper diagnostic. If not, exponent comparison remains scheme-dependent.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No direct EDT/EFT conflict, no established continuum EDT, no shared fixed point, no `BRIDGE_DERIVED`, no new physics follows.