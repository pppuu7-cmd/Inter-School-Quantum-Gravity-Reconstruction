# ITER113 adversarial critic — nonlocal F/M/G cancellation diagnostic

Date: 2026-09-15
Gate: `ITER113_FIXED_GEODESIC_CURVATURE_G2_NONLOCAL_STRUCTURE_CANCELLATION_DIAGNOSTIC`
Preregistration: `53143c5a9d1faea102b97834bb329ff03ec1871f`
Source authority: `fa267ec33645614818c3dc12c2335709d22fc971`

## Attack 1 — every line-integral form factor is nonanalytic in the external momentum and therefore contributes to the `q^4 log q^2` coefficient

Too strong. A geodesic line factor such as `(e^{ip.l}-1)/(p.l)` is non-polynomial, so M/G cannot be declared contact-only. But specific tensor contractions or parameter integrations can still reduce to analytic/contact terms or cancel internally. ITER113 classifies **eligibility for nonlocal contribution**, not a guaranteed nonzero contribution from every term.

## Attack 2 — local counterterms can never affect a separated observable

Too strong as a blanket operator statement. Local bulk counterterms are needed to renormalize the calculation and can change local operator definitions. What ITER113 safely prunes is the part of their momentum-space contribution proven to be polynomial/analytic and therefore contact after Fourier transform. Observable-specific geodesic renormalization is not covered by that pruning.

## Attack 3 — the master-coordinate nonzero F result proves `C_F` is nonzero in the fixed-geodesic decomposition

Not as a separately gauge-invariant coefficient. The ordinary field diagrams share vertices with the master-coordinate calculation, but decomposition between `F` and localization corrections depends on the relational completion and gauge bookkeeping. Only the full fixed-geodesic sum has physical meaning. A source-identical sub-coefficient cannot be imported from the master-coordinate observable without recalculation.

## Attack 4 — BRST/gauge invariance forces the final nonanalytic coefficient to equal the master-coordinate one

Rejected. BRST constrains gauge dependence, not relational-observable uniqueness. Two different gauge-invariant nonlocal observables may have different finite separated coefficients.

## Attack 5 — if cancellation remains open, the pruning achieved nothing

Rejected. ITER113 removes pure polynomial/contact structures and scaleless tadpoles from the target coefficient, identifies the exact classes that must remain, and reduces the computation to bubble-type loop integrals dressed by zero/one/two geodesic parameter integrations. That is a real reduction in calculation complexity even without a sign theorem.

## Attack 6 — tensor reduction can be done before constructing the complete gauge-invariant operator and may accidentally discard longitudinal pieces needed for cancellation

Valid warning. Projection to scalar master structures must be performed after preserving enough tensor information to verify the gauge-parameter cancellation of the complete F/M/G observable. Longitudinal-looking pieces cannot be discarded simply because scalar curvature is a scalar; geodesic localization carries the physical direction vector and can couple to them before cancellation.

## Attack 7 — the fixed-length vector `l^mu` introduces a new scale and invalidates the power-counting result

Rejected. Its magnitude is the measured separation itself, not an independent physical mass parameter. Dimensionless dependence on `q.l`, angular structures and logarithms is allowed; it does not permit an arbitrary engineering power at fixed `G^2`.

## Critic verdict

**CONFIRMS `PASS_SCOPED_CONTACT_PRUNING_VALID_NONLOCAL_FMG_BASIS_REMAINS_CANCELLATION_OPEN`.**

The safe next step is a gauge-respecting tensor/form-factor reduction, not numerical fitting or class deletion.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.