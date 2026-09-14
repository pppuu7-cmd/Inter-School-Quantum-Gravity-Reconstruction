# ITER114 terminal result — fixed-geodesic curvature `O(G^2)` radial master-distribution basis

Date: 2026-09-15
Gate: `ITER114_FIXED_GEODESIC_CURVATURE_G2_RADIAL_MASTER_DISTRIBUTION_BASIS`
Preregistration: `22f0ee94fb43aba82b52c9a8ba29c0d22c26ce52`
Source authority: `1ab0a0855772a03b75a22632ca979746d7b560b7`
Adversarial review: `7a9e2fbe491e334c2199da520451053a531d1351`

## Terminal classification

**`PASS_SCOPED_G2_NONCONTACT_RADIAL_BASIS_L8_LOG0_LOG1_LOG2`**

Scope: one-loop, massless, flat Euclidean background, one fixed geodesic separation, no additional physical scale.

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Main functional-form result

The complete separated anchored fixed-geodesic scalar-curvature correlator through `O(G^2)` is restricted to

**`C_RR^geo(l;mu) = (G^2/l^8)[A_0(mu)+A_1(mu)L+A_2 L^2] + O(G^3)`**,

with

`L = log(mu^2 l^2)`,

plus contact distributions at `l=0`.

The coefficients are not computed in ITER114.

## Why the basis closes

The explicit fixed-geodesic one-loop source reduces mixed/pure geodesic corrections to `G_0^2` and after renormalization to two nonlocal distributions

`H_0^(k) ~ partial^2[log^k(mu^2 x^2)/x^2]`, `k=1,2`,

plus contact terms. The double-log distribution comes from the strongest one-loop geodesic pole structure.

Scalar curvature supplies additional derivatives, changing `l^-4` to the required `l^-8` dimension but not creating a new independent scale or raising the logarithmic degree. Rotational invariance leaves only `l^2` after the fixed-geodesic tangent is fully contracted.

## Important finite-window consequence

For `P(L)=A_0+A_1 L+A_2 L^2`, the local log-log slope is

`p_eff(l) = -8 + 2 P'(L)/P(L)`.

Therefore an `O(G^2) l^-8` asymptotic structure with logarithms can display an effective slope steeper than `-8` over a finite window. This is an algebraic warning against comparing a finite-range lattice power fit directly to the bare engineering exponent.

It is not an EDT fit and gives no value for the observed lattice slope.

## Exact successor

`ITER115_FIXED_GEODESIC_CURVATURE_G2_RG_LOG_HIERARCHY_AUTHORITY`

Use `mu`-independence and the known fixed-geodesic renormalization template to determine the RG hierarchy among `A_0,A_1,A_2`. In particular, test whether `A_2` is fixed by the highest UV-pole/geodesic anomalous structure and whether showing `A_2 != 0` would settle the `O(G^2)` noncancellation question without evaluating all finite integrals.

## Claim ceiling

No values of `A_0,A_1,A_2`, no noncancellation theorem, no EDT fit, no direct EDT/EFT conflict, no continuum EDT, `BRIDGE_DERIVED`, new physics or candidate theory follows.