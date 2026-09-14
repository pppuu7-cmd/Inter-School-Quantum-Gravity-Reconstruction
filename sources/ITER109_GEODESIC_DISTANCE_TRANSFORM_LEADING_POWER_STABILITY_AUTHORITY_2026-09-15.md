# ITER109 source authority — fixed-geodesic transform and leading inverse-power stability

Date: 2026-09-15
Gate: `ITER109_GEODESIC_DISTANCE_TRANSFORM_LEADING_POWER_STABILITY_AUTHORITY`
Preregistration: `b5662ed023e44ab52218ffe2e20a760adcdccf05`

## 1. Engineering dimensions fix the possible noncontact power at each order in G

In four dimensions,

- scalar curvature has mass dimension `[R]=2`;
- a curvature two-point function has dimension `[<RR>]=4`;
- Newton's constant has `[G]=-2` in mass units, equivalently `[G]=L^2`.

Therefore a separated-point contribution proportional to `G^n` and containing no additional physical mass scale must have the form

`G^n / l^(4+2n)`

up to dimensionless constants and logarithms.

In particular:

- `n=2` forces `G^2/l^8`;
- `n=3` forces `G^3/l^10`.

Predicate A: **PASS**.

## 2. The 2026 master-coordinate curvature correlator realizes the G^2/l^8 structure explicitly

The low-energy EFT calculation finds that the lower-order curvature-curvature contributions are contact/local at the relevant orders and that the first universal noncontact term occurs at next-to-leading order. In Euclidean position space, away from the origin,

`<R(X)R(Y)> = 768 G^2/(pi^2 r^8) + O(G^3)`.

The higher-curvature low-energy constants appearing at the same calculation order contribute only local/contact structures to this noncoincident observable. Thus the separated `G^2/r^8` term is a universal low-energy prediction in the master-coordinate relational scheme.

Predicate B: **PASS for the dimensional statement and explicit master-coordinate realization**.

## 3. Fixed-geodesic renormalization introduces logs and dimensionless scheme data, not an alternative G^2 inverse power

The Fröb fixed-geodesic calculation treats a different insertion (a massless matter scalar), so it cannot determine the curvature coefficient. It is nevertheless a clean structural test of what changing the separation observable does perturbatively.

At one graviton loop the fixed-geodesic scalar propagator acquires terms schematically of the form

`kappa^2 * partial^2[log^2(mu^2 x^2)/x^2]`

and analogous single-log/geodesic-counterterm terms. Away from coincidence this scales as

`kappa^2 / x^4 * polynomial(log(mu x))`

on top of the free `1/x^2` scalar propagator.

The geodesic wave-function renormalization is dimensionless once its explicit `kappa^2/l^2` factor is extracted. Its finite part and the renormalization scale generate coefficients and logarithms, not a new independent length dimension.

Predicate C: **PASS_CONTROL — structural precedent only**.
Predicate D: **PASS_SCOPED**.
`CURVATURE_MATTER_SCALAR_SWAP_CONTROL`: **PASS_CONTROL**.
`RENORMALIZATION_SCALE_POWER_SWAP_CONTROL`: **PASS_CONTROL**.

## 4. Conditional theorem for a fixed-geodesic curvature correlator

Suppose the fixed-geodesic scalar-curvature correlator has a nonzero noncontact term at order `G^2` in the massless low-energy EFT, and suppose no new physical mass scale is introduced by the observable definition.

Then dimensional analysis requires

**`<RR>_{d_g=l}^{(G^2)} = G^2/l^8 * F(log(mu l), dimensionless scheme data)`**,

where `F` is dimensionless.

Consequently a pure `G^2/l^10` leading term is impossible at that order. A change from master-coordinate to fixed-geodesic localization may alter coefficients, add logs, and add scheme dependence, but cannot change the engineering inverse power from `8` to `10` while remaining at `O(G^2)`.

This statement is independent of the EDT target exponent.

## 5. Noncancellation of the G^2 term is not source-established

The crucial missing calculation is curvature-specific. The master-coordinate `G^2/r^8` coefficient receives contributions from coordinate corrections needed for gauge invariance. A fixed-geodesic observable reorganizes the same perturbative metric fluctuations and adds nonlocal line-supported geodesic insertions with their own counterterms.

No frozen source computes the full fixed-geodesic curvature observable and no general Ward identity or positivity theorem in the source stack proves that the sum of all `O(G^2)` noncontact terms must remain nonzero.

Therefore the possibility

`C_fixed-geodesic^(G^2)(l) = 0`

through an observable-specific cancellation cannot currently be excluded by source authority.

If such a cancellation occurred, the first nonzero term could move to `O(G^3)`, where `G^3/l^10` is dimensionally allowed.

Predicate E: **NOT ESTABLISHED**.
Predicate F: **PASS_CONTROL / CANCELLATION OPEN**.
`G2_CANCELLATION_ASSUMPTION_CONTROL`: **TRIGGERS**.

## 6. Higher-derivative and contact terms do not rescue a different G^2 long-range power in the frozen EFT

The 2026 master-coordinate calculation explicitly separates local analytic momentum-space terms, whose Fourier transforms are contact distributions. Higher-curvature low-energy constants enter those local pieces at the order considered and do not alter the universal separated `G^2/r^8` tail.

A future fixed-geodesic curvature calculation may require new geodesic counterterms, as ITER107 shows. Unless these introduce a new physical mass scale rather than a renormalization scale/dimensionless finite parameter, they can modify logs/coefficient but not the engineering power at fixed `G^2` order.

Predicate G: **PASS_SCOPED**.
`CONTACT_NONCONTACT_SWAP_CONTROL`: **PASS_CONTROL**.

## 7. No target-driven cancellation inference

The modern EDT power near `-10` is not used to infer that the continuum `G^2` term cancels. Such an inference would reverse the predictive logic and fit an uncomputed continuum observable to a lattice target.

Predicate H: **PASS_CONTROL**.
`EDT_TARGET_CANCELLATION_FIT_CONTROL`: **PASS_CONTROL**.

## Source classification

**`PASS_SCOPED_CONDITIONAL_G2_POWER_IS_MINUS8_NONCANCELLATION_OPEN`**

The result is sharp:

> If the fixed-geodesic scalar-curvature correlator has a nonzero `O(G^2)` separated-point term, its leading engineering power in four dimensions is necessarily `l^-8` up to logarithms. A leading `l^-10` term is compatible with EFT power counting only if the `O(G^2)` tail cancels/vanishes so that an `O(G^3)` term becomes leading (or if an additional physical scale/operator changes the assumptions).

The frozen literature does not establish or exclude that cancellation for the curvature observable.

## Highest-information successor

The next gate should test whether the `O(G^2)` coefficient can be protected against cancellation using observable-independent information: spectral/positivity arguments, the graviton exchange/cut structure, unitarity of the low-energy nonlocal amplitude, or a source-defined relation between different relational completions at separated points. If no such protection exists, an explicit fixed-geodesic curvature computation is genuinely necessary.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No direct EDT/EFT exponent conflict, no proof of a nonzero fixed-geodesic `G^2` coefficient, no continuum EDT claim, no `BRIDGE_DERIVED`, no new physics follows.