# ITER114 adversarial critic — radial master-distribution basis

Date: 2026-09-15
Gate: `ITER114_FIXED_GEODESIC_CURVATURE_G2_RADIAL_MASTER_DISTRIBUTION_BASIS`
Preregistration: `22f0ee94fb43aba82b52c9a8ba29c0d22c26ce52`
Source authority: `1ab0a0855772a03b75a22632ca979746d7b560b7`

## Attack 1 — a line integral can generate arbitrary special functions of `mu l`

Not under the frozen massless one-scale setup. The geodesic parameter runs over a dimensionless fixed interval and all coordinate differences on the straight background geodesic are proportional to the same vector `l`. Factoring out `l` leaves dimensionless beta/Feynman/line-parameter integrals whose nontrivial dependence is numerical; dimensional regularization introduces powers `(mu^2 l^2)^epsilon`, whose expansion gives logarithms.

A genuine additional special-function argument would require a second independent ratio/cross-ratio, mass scale or angle. None survives in the final scalar two-point geometry.

## Attack 2 — curvature insertions may raise the logarithmic degree beyond two

Curvature derivatives can raise inverse powers of `l` and change coefficients, but differentiation of `log^k(mu^2 l^2)` does not increase `k`. The only route to a higher log degree would be a stronger pole structure than the one-loop fixed-geodesic template's double pole.

At the frozen one-loop order there is a single loop integration; the extra geodesic endpoint singularity already produces the known double pole. Curvature-composite counterterms at the same order are local and do not introduce an additional independent loop subdivergence in the separated noncontact sector. No source-required triple-pole mechanism is identified.

Therefore the `log^2` ceiling is justified **at this order and within this renormalization structure**, not as an all-loop theorem.

## Attack 3 — finite geodesic counterterms introduce a new physical scale

They introduce scheme/renormalization data and a reference scale, not automatically a new propagating physical mass. Their dependence enters dimensionless coefficients and logarithms. If one imposed a new physical renormalization length as extra observable data, the one-scale ansatz would need extension; ITER114 does not assume such an extra measured scale.

## Attack 4 — fixed geodesic direction leaves anisotropic functions

Intermediate diagrams depend on the unit tangent `n^mu`, but the endpoint separation is `l^mu=l n^mu`; after all scalar contractions there is no independent vector. Terms such as `(n.partial)^k f(l^2)` reduce to radial derivatives. A second preferred vector/background structure would invalidate this reduction, but none exists in the frozen flat Euclidean setup.

## Attack 5 — field-sector loop integrals need not reduce to the same `H^(1),H^(2)` distributions as the matter template

Correct at the coefficient/integrand level, but not fatal to the **radial function-space** claim. Different curvature vertices can yield different linear combinations of derivatives of renormalized one-scale massless distributions. Dimensionality and one-loop pole structure still restrict the separated scalar result to `l^-8` times constants/single/double logs.

Thus ITER114 does not assert that every curvature diagram literally equals the matter `H` coefficients.

## Attack 6 — contact-term derivatives can mix into the radial answer under renormalization

They can shift local distributional definitions and RG bookkeeping, but at strictly nonzero separation they vanish. The split is valid only after the renormalized distribution is defined; one must not drop contact pieces before pole cancellation.

## Attack 7 — the effective-slope formula can be used to explain the EDT `-10` target

Not as a validation claim. Algebraically,

`p_eff=-8+2P'(L)/P(L)`

shows that logarithms can change a finite-window slope. Without `A_0,A_1,A_2` and a matched distance observable, this does not predict the EDT fit and cannot be used to tune coefficients.

## Critic verdict

**CONFIRMS `PASS_SCOPED_G2_NONCONTACT_RADIAL_BASIS_L8_LOG0_LOG1_LOG2`** under the explicit one-loop, massless, single-separation, no-extra-physical-scale assumptions.

The next highest-information step is RG consistency: determine which log coefficients are fixed by the anomalous running of the geodesic embedding / curvature composite and how many independent finite constants remain.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.