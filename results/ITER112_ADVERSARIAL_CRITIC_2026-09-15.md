# ITER112 adversarial critic — fixed-geodesic curvature `O(G^2)` census

Date: 2026-09-15
Gate: `ITER112_FIXED_GEODESIC_CURVATURE_G2_OPERATOR_DIAGRAM_CENSUS`
Preregistration: `38e92177aec907b055be86c74239c2496dcd7937`
Source authority: `11c3466ae05c4fb64e1267e3f8e64e95c636078e`

## Attack 1 — the F/M/G split was derived for a matter scalar and need not close for curvature

The literal scalar vertices do not transfer, but the **localization-order split does**. It follows from the perturbative Taylor expansion of any scalar insertion evaluated at the fluctuating geodesic endpoint. Curvature changes `R_1,R_2,R_3` and their renormalization, not the need for endpoint orders beyond `chi_2` at overall `kappa^4`.

Thus F/M/G is a valid structural census, provided curvature-specific vertices are generated independently.

## Attack 2 — path-integral measure, gauge-fixing and ghosts create a fourth localization class

Rejected as a new localization class. Gauge-fixing, Faddeev-Popov ghosts and any source-required local measure contributions belong to the ordinary path-integral/field sector F and its interaction/counterterm expansion. They do not introduce an independent power of the geodesic endpoint functional unless they are coupled to `chi_1` or `chi_2`, in which case the term is already mixed/pure-geodesic M/G.

They must nevertheless be included in the actual F/M/G contractions; `calculation-ready` does not mean `graviton-only`.

## Attack 3 — curvature-composite mixing could require infinitely many operators

Rejected at fixed EFT order. At one loop / fixed derivative and `kappa` order, EFT renormalization requires a finite local operator basis. The 2026 curvature calculation explicitly works with the `O(R^2)` effective Lagrangian at the relevant order. Higher-derivative operators beyond the required order do not generate an infinite class at `O(G^2)`.

What remains open is the numerical/mixing coefficient in the fixed-geodesic observable, not closure of the perturbative census.

## Attack 4 — geodesic renormalization might generate arbitrary new nonlocal operators

The 2018 source shows severe new divergences but closes them at the studied order through renormalization of the geodesic embedding plus ordinary counterterms. This is source evidence for perturbative closure at one loop, not proof of all-order renormalizability. ITER112 is explicitly restricted to `O(G^2)`.

## Attack 5 — endpoint Taylor expansion misses shell-measure fluctuations relevant to EDT

**Valid scope correction.** ITER112 constructs the anchored fixed-geodesic two-point function, following the Fröb observable class. The modern EDT estimator additionally averages over all pairs in a fluctuating distance shell and divides by the shell-pair count, followed by its improved connected subtraction.

Those shell-measure/normalization fluctuations are **not** part of ITER112's F/M/G endpoint census. They belong to a later observable-transform step after the fixed-endpoint correlator is known. Therefore `CALCULATION_READY` applies to the anchored fixed-geodesic `RR` calculation, not yet to the full EDT shell estimator.

## Attack 6 — both endpoints should be geodesically corrected symmetrically

A symmetric midpoint parameterization is possible, but it is not a new physical class. The anchored construction fixes one endpoint and initial physical tangent/length and lets the second endpoint fluctuate. Translational invariance of the flat background supplies the anchor. A symmetric parameterization redistributes localization corrections between endpoints while retaining the same perturbative orders/classes; equality of the final gauge-invariant result is a nontrivial check, not a reason to double-count classes.

## Attack 7 — local counterterms can be discarded before the calculation because they are contact

Too strong. The 2026 master-coordinate result establishes that the relevant higher-curvature EFT coefficients contribute only contact structures **for that observable/order**. In the fixed-geodesic calculation, local insertion/counterterm pieces must first be included consistently before the contact/noncontact decomposition; only terms proven to remain pure contact may be removed from the separated-tail coefficient.

This tightens the wording of the census but does not open a new class.

## Attack 8 — gauge independence of the full observable guarantees each class can be computed in any inconsistent convention

Rejected. F/M/G must share the same gauge, graviton normalization, Euclidean continuation and geodesic boundary conventions. Gauge-parameter cancellation is a global diagnostic only after conventions are aligned.

## Critic verdict

**CONFIRMS `PASS_SCOPED_FINITE_G2_OPERATOR_DIAGRAM_CENSUS_CALCULATION_READY`**, with the explicit scope:

> calculation-ready for the anchored fixed-geodesic scalar-curvature two-point function through `O(G^2)`, not yet for the normalized EDT distance-shell estimator.

The next highest-information step is a nonlocal-structure/cancellation diagnostic across F/M/G before full tensor integral evaluation.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.