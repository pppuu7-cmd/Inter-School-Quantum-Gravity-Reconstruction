# ITER114 terminal result — corrected fixed-geodesic curvature `O(G^2)` radial master-distribution basis

Date: 2026-09-15
Gate: `ITER114_FIXED_GEODESIC_CURVATURE_G2_RADIAL_MASTER_DISTRIBUTION_BASIS`
Preregistration: `22f0ee94fb43aba82b52c9a8ba29c0d22c26ce52`
Correction record: `7e8d7e9c0ade3d0483de2448a8011bd09d6a699a`
Corrected source authority: `001b5bd81212e1b85698bafa0739d5810ac17336`
Corrected adversarial review: `385a23cb26d9b0aaa2e9dc666bdd433196843ca3`

## Corrected terminal classification

**`PASS_SCOPED_G2_NONCONTACT_RADIAL_BASIS_L8_CONSTANT_PLUS_SINGLE_LOG`**

Scope: one-loop, massless, flat Euclidean background, one fixed geodesic separation, no additional physical scale.

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Correction to the earlier terminal record

The earlier version incorrectly promoted the `log^2` appearing inside the distributional definition of `H^(2)` to a separated-point `log^2` term. For nonzero separation,

`partial^2[L/r^2] = -4/r^4`,

`partial^2[L^2/r^2] = 8(1-L)/r^4`,

with `L=log(mu^2 r^2)`.

Therefore the outer Laplacian lowers the separated logarithmic degree. This correction was identified before coefficient adjudication or any target fit.

## Correct main functional-form result

The complete separated anchored fixed-geodesic scalar-curvature correlator through `O(G^2)` is restricted to

**`C_RR^geo(l;mu) = (G^2/l^8)[B_0(mu)+B_1(mu)L] + O(G^3)`**,

`L=log(mu^2 l^2)`,

plus contact distributions at `l=0`.

Only two separated coefficients remain: `B_0`, `B_1`.

## Why the basis closes

The source fixed-geodesic one-loop distributions are

`H^(k) ~ partial^2[log^k(mu^2 x^2)/x^2]`, `k=1,2`.

At separated points these reduce to `x^-4` times constant/single-log. Four further external derivatives associated with the two curvature insertions raise the inverse radial power to `l^-8` but do not raise the log degree. Rotational invariance leaves no second independent dimensionless argument.

## Finite-window consequence

For

`C(l)=G^2 l^-8[B_0+B_1L]`,

the local log-log slope is

`p_eff(l)=-8 + 2 B_1/(B_0+B_1L)`.

Thus finite-window slopes can differ from `-8` even when the true one-loop engineering power is `l^-8`. This is not an EDT fit and supplies no values for `B_0,B_1`.

## Invalidated successor

The preregistered ITER115 assumed the superseded three-coefficient basis `A_0+A_1L+A_2L^2`. It must be invalidated before adjudication.

The correct successor is a fresh RG-consistency gate on `B_0+B_1L`, asking whether `B_1` is fixed by the highest UV-pole/geodesic-renormalization residue and whether a nonzero `B_1` can prove noncancellation without the full finite calculation.

## Claim ceiling

No values of `B_0,B_1`, no noncancellation theorem, no EDT fit, no direct EDT/EFT conflict, no continuum EDT, no `BRIDGE_DERIVED`, no new physics and no candidate theory follow.