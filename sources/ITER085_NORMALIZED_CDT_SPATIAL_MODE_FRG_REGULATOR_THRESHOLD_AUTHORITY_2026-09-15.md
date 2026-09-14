# ITER085 source authority — normalized CDT spatial mode ↔ foliated-FRG regulator threshold

Date: 2026-09-15
Gate: `ITER085_NORMALIZED_CDT_SPATIAL_MODE_FRG_REGULATOR_THRESHOLD_CROSSWALK`
Preregistration: `c5abaa46cdc5a32801b469fb195e4aa2e8d455f1`
Workflow launch: `3327a99444cf0951c9580910031cef22c0aab4b9`

## Independently qualified CDT input

ITER084 fixed the finite-regulator cell-centred normalization

`z_CDT = 9 lambda_graph/a^2`,

with `z_CDT` having the sign/dimension of an eigenvalue of the positive operator `-Delta` on a spatial slice. No FRG quantity entered that derivation.

## FRG source authority

### 1. Operational meaning of `k`

arXiv `2306.10408`, Sec. 3.1, states that the Wetterich equation integrates quantum fluctuations with momenta close to the coarse-graining scale `k`. The regulator gives a `k`-dependent mass to modes with momentum squared much smaller than `k^2` and vanishes for modes much larger than `k^2`.

Thus `k` is source-defined as an FRG coarse-graining/probe scale. This does not identify it with the inverse CDT lattice spacing.

### 2. A genuinely spatial background-regulator route exists

The regulator discussion in Sec. 3.2 of `2306.10408` distinguishes the covariant background Laplacian from the additional options supplied by a foliation. It explicitly gives the spatial choice

`Box_sp = -bar_sigma^{ij} bar_D_i bar_D_j`,

with no derivatives in the time direction, and states that this route was taken in the background computations cited there, including arXiv `1212.5114` and `1609.04813`.

arXiv `1609.04813` independently states that its background ADM calculation uses a Type-I cutoff dressing the Laplacian by `Delta -> Delta + R_k`, chooses the Litim regulator, and presents the resulting beta functions for a `d`-dimensional spatial slice.

Therefore a source-qualified background-spatial route exists in which a spatial Laplacian eigenvalue `z` is the correct broad operator type for the regulator argument.

### 3. Litim support gives a target-independent threshold

The 2023 source writes the Type-I substitution

`Box -> P_k(Box) = Box + R_k(Box)`

and the Litim profile

`R_k(Box) = (k^2-Box) Theta(k^2-Box)`.

For an eigenmode with eigenvalue `z`, regulator support is therefore source-defined by

`z < k^2`, equivalently `x = z/k^2 < 1`.

In the qualified background-spatial route, inserting the independently normalized CDT eigenvalue gives the **probe variable**

`x_CDT = z_CDT/k^2 = 9 lambda_graph/(a^2 k^2)`.

The statement `x_CDT<1` means only that the corresponding spatial mode lies inside the support of this Litim coarse-graining profile. It is not an equality of physical observables and does not set `k=1/a`.

### 4. The 2023 production fluctuation calculation does not use that spatial regulator

The same `2306.10408` regulator discussion states explicitly that, because the present work is Euclidean, the authors adopt a **covariant** choice for `Box`, which is also technically preferred for their fluctuation computation.

In Sec. 4.1 the actual implementation is unambiguous. Candidate kinetic operators take the form

`Box_alpha = alpha p0^2 + vec(p)^2`.

To avoid different cutoff domains for the different dispersions, the source uses the replacement

`Box_alpha -> Box_alpha + R_k(Box_{alpha=1})`

and states that this choice is adopted in the sequel. Hence the regulator profile is a function of

`p^2 = p0^2 + vec(p)^2`.

The Litim support is thus the four-momentum domain

`p0^2 + vec(p)^2 < k^2`.

The appendix makes this operationally explicit for loop momenta: the selected regulator is `R_k(q^2)=(k^2-q^2)Theta(k^2-q^2)` and integrations are restricted by `q0^2+vec(q)^2 <= k^2`.

### 5. A spatial external projection does not convert the production regulator into a spatial regulator

The 2023 computation separately projects the graviton two-point flow onto `p0^2` and `vec(p)^2` tensor structures. This permits a **spatial-momentum projection of an external vertex**, but the internal coarse-graining operator remains `q^2=q0^2+vec(q)^2`.

Therefore setting an external `p0=0`, or studying the coefficient of `vec(p)^2`, does not remove the temporal loop momentum from the regulator support. The frozen source does not authorize replacing the production regulator by `R_k(vec(q)^2)` in this calculation.

A purely spatial CDT eigenvalue `z_CDT` therefore lacks the temporal-mode datum required to identify an eigenvalue of the full production coarse-graining operator.

## Predicate adjudication

- A — operational meaning of `k`: **PASS**.
- B — explicit regulator support/threshold: **PASS**, Litim `z/k^2<1` for the eigenvalue of the implemented regulator operator.
- C — source-defined background spatial Laplacian route: **PASS_SCOPED**.
- D — actual 2023 production regulator identified: **PASS**, covariant `p^2=p0^2+vec(p)^2` profile.
- E — source-authorized `p0=0` reduction of the production regulator: **NO**. External spatial projection is not a spatial loop regulator.
- F — support threshold kept distinct from physical-scale identity: **PASS_CONTROL**.
- G — ITER084 normalization imported without fitting: **PASS_CONTROL**.
- H — background/fluctuation and spatial/covariant scheme dependence retained: **PASS_CONTROL**.
- I — no trajectory/coupling inference: **PASS_CONTROL**.

## Exact scoped crosswalk that is authorized

For the **background-spatial** regulator route only:

`x_CDT(k) = 9 lambda_graph/(a^2 k^2)`.

With the Litim profile, `x_CDT<1` classifies the normalized spatial mode as lying inside regulator support, `x_CDT>1` as outside it, and `x_CDT=1` as the scheme-defined threshold.

This is a typed regulator-mode probe crosswalk. The threshold value `1` belongs to the chosen profile; it is not a universal observable.

## Exact production-flow obstruction

For the **2023 production fluctuation** route the regulator eigenvalue is of the form

`z_prod = q0^2 + z_spatial`

in the relativistic regulator argument. A CDT spatial eigenvalue supplies `z_spatial` but not `q0^2`. The source does not derive a production-flow rule assigning a temporal mode to a spatial CDT eigenmode.

Thus no exact full-production substitution `z_prod = z_CDT` is authorized.

## Source classification

**`PASS_SCOPED_BACKGROUND_SPATIAL_THRESHOLD_ROUTE_PRODUCTION_COVARIANT_OPEN`**

The spatial background route is stronger than a dimensional analogy: it contains the correct operator type and an explicit regulator-support threshold. The production fluctuation flow remains type-incomplete for a CDT spatial-only mode because its implemented regulator is covariant.

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.
