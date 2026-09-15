# ITER114 source authority — fixed-geodesic curvature `O(G^2)` radial master-distribution basis

Date: 2026-09-15
Gate: `ITER114_FIXED_GEODESIC_CURVATURE_G2_RADIAL_MASTER_DISTRIBUTION_BASIS`
Preregistration: `22f0ee94fb43aba82b52c9a8ba29c0d22c26ce52`
Correction record: `7e8d7e9c0ade3d0483de2448a8011bd09d6a699a`

## Correction notice

An earlier version of this source record incorrectly promoted the `log^2` appearing **inside** the distributional definition of `H_0^(2)` to a separated-point `log^2` radial term. The exact outer Laplacian lowers the separated logarithmic degree. The corrected result below supersedes that claim; old commits remain in history.

## 1. Fixed-geodesic one-loop source reduces to two distributions plus contact

The explicit one-loop fixed-geodesic matter calculation reduces the mixed and pure geodesic terms to coefficients multiplying `G_0(x,y)^2`. Near four dimensions the singular distribution is renormalized into

`H_0^(k)(x;mu) = i/(64 pi^4) partial^2 [log^k(mu^2 x^2)/x^2]`, `k=1,2`,

plus a local contact contribution.

The `k=2` distribution is tied to the double UV pole/geodesic renormalization structure. This source fact does not by itself fix the separated logarithmic degree after `partial^2` acts.

Predicate A: **PASS**.

## 2. Exact separated form of H^(1), H^(2)

Let `L=log(mu^2 r^2)`. In four Euclidean dimensions, for `r>0`, radial differentiation gives

`partial^2[L/r^2] = -4/r^4`,

`partial^2[L^2/r^2] = 8(1-L)/r^4`.

Therefore the separated one-loop template contains at most a **single** logarithm:

- `H^(1) ~ r^-4`;
- `H^(2) ~ r^-4 [constant - L]`.

Contact terms required by the distributional extension are kept separate.

Predicate B: **PASS_CORRECTED / MAX_SEPARATED_LOG_DEGREE_1**.

## 3. Final anchored scalar correlator is radial

The background is flat Euclidean space and the observable is scalar at both endpoints. The fixed geodesic introduces only the separation vector `l^mu`; after all tensor indices and tangent factors are contracted, there is no independent external angle or ratio.

Hence the complete separated scalar correlator depends only on `l^2` and `mu`.

Predicate C: **PASS**.

## 4. Engineering dimension fixes the radial prefactor

In four dimensions,

`[R]=L^-2`, `[RR]=L^-4`, `[G^2]=L^4`.

Any separated `O(G^2)` term with no additional physical scale must therefore be `G^2/l^8` times a dimensionless function of `mu l` and finite dimensionless renormalization data.

Predicate D: **PASS**.

## 5. Curvature derivatives preserve the corrected log ceiling

Relative to the `r^-4` fixed-geodesic master distributions, the two scalar-curvature insertions supply four net derivatives. Acting with a rotationally contracted four-derivative operator on

`r^-4 [c_0+c_1 L]`

produces, away from `r=0`, another radial expression of the form

`r^-8 [d_0+d_1 L]`.

Differentiation can lower logarithmic degree but cannot create a new `L^2` term.

Predicate E: **PASS_CORRECTED**.

## 6. Correct complete noncontact ansatz

Under the frozen one-loop, massless, single-separation, no-extra-physical-scale assumptions,

**`C_RR^geo(l;mu) = (G^2/l^8) [B_0(mu)+B_1(mu)L] + O(G^3)`**,

`L=log(mu^2 l^2)`,

plus contact distributions at `l=0`.

The coefficients `B_0,B_1` are not computed here and are not imported from the matter calculation or inferred from EDT.

Predicate F: **PASS_CONTROL**.

## 7. Contact sector remains separate

Delta functions and their derivatives are needed for renormalization/distributional consistency but vanish at strictly nonzero separation. They are not additional separated radial basis functions.

Predicate G: **PASS_CONTROL**.

## 8. No additional dimensionless function is required

The geodesic parameter is integrated over a fixed dimensionless interval and all background coordinate differences are proportional to one separation vector. With no second separation, angle, mass ratio or physical scale, parameter integration can change numerical coefficients and the same logarithm but cannot generate an independent functional argument in the final rotational scalar.

Predicate H: **PASS**.

## Corrected source classification

**`PASS_SCOPED_G2_NONCONTACT_RADIAL_BASIS_L8_CONSTANT_PLUS_SINGLE_LOG`**

The complete separated one-loop coefficient problem is reduced to two radial coefficients:

`B_0`, `B_1`.

## Finite-window slope

For

`C(l)=G^2 l^-8 [B_0+B_1 L]`,

the local slope is

`p_eff(l) = -8 + 2 B_1/(B_0+B_1 L)`.

A finite-window slope can therefore differ from `-8` without changing the asymptotic engineering power. This is an algebraic statement only; no EDT fit is performed.

## Correct successor

The preregistered ITER115 assumed the superseded three-coefficient basis and must not be adjudicated. Its valid successor should use the corrected two-coefficient basis and RG consistency to test whether `B_1` is controlled by the highest UV-pole/geodesic residue and whether `B_1 != 0` would prove a nonzero `O(G^2)` separated tail.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No values of `B_0,B_1`, no noncancellation theorem, no EDT fit, no direct EDT/EFT conflict, no continuum EDT, `BRIDGE_DERIVED`, or new physics follows.