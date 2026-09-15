# ITER114 adversarial critic — corrected radial master-distribution basis

Date: 2026-09-15
Gate: `ITER114_FIXED_GEODESIC_CURVATURE_G2_RADIAL_MASTER_DISTRIBUTION_BASIS`
Preregistration: `22f0ee94fb43aba82b52c9a8ba29c0d22c26ce52`
Corrected source authority: `001b5bd81212e1b85698bafa0739d5810ac17336`
Correction record: `7e8d7e9c0ade3d0483de2448a8011bd09d6a699a`

## Correction accepted

The earlier critic incorrectly endorsed a separated `log^2` basis by reading the `log^2` inside the distributional definition of `H^(2)` as if it survived the outer Laplacian unchanged.

At `r>0`,

`partial^2[L/r^2] = -4/r^4`,

`partial^2[L^2/r^2] = 8(1-L)/r^4`,

so the correct separated one-loop template contains only constant and single-log terms.

This mathematical correction supersedes the earlier verdict while leaving the original commits in Git history.

## Attack 1 — line integrals may generate extra special functions

Under the frozen one-scale massless setup, there is no independent dimensionless cross-ratio after the geodesic parameter integrations and scalar rotational projection. Such integrals may change numerical coefficients but do not require a second functional argument beyond `mu r`.

## Attack 2 — curvature derivatives can regenerate log^2

Rejected. Differentiation of `r^-4(c_0+c_1L)` yields `r^-8(d_0+d_1L)` plus contact terms. Derivatives can lower but do not raise logarithmic degree.

## Attack 3 — hidden triple-pole structures could restore log^2 at separated points

No source-required triple-pole mechanism is present at the frozen one-loop order. The fixed-geodesic precedent's strongest singularity is the double pole whose renormalized distribution is `H^(2)`; after the defining Laplacian acts, its separated form is single-log. This is not an all-loop theorem.

## Attack 4 — geodesic finite renormalization introduces a new physical ratio

It introduces scheme/reference-scale dependence and finite dimensionless data, not automatically an independent propagating mass scale. A genuinely new physical scale would require a separate extension of the gate assumptions.

## Attack 5 — field-sector integrals need not literally equal H^(1),H^(2)

Correct but not fatal. The corrected claim is about the final one-scale radial function space, not equality of individual diagram coefficients to the matter template. One-loop massless distributions with the frozen pole structure reduce at separated points to `r^-8` times constant/single-log after curvature derivatives.

## Attack 6 — contact terms may contaminate the separated basis

They are essential during renormalization, but vanish at strictly nonzero separation once the distribution is properly defined. They form a separate local sector.

## Attack 7 — the finite-window slope can be tuned to EDT

Forbidden. For

`C=G^2 r^-8(B_0+B_1L)`,

`p_eff=-8+2B_1/(B_0+B_1L)`

is an algebraic identity. Without calculated `B_0,B_1` and matched distance semantics it is not an EDT prediction or fit.

## Corrected critic verdict

**CONFIRMS `PASS_SCOPED_G2_NONCONTACT_RADIAL_BASIS_L8_CONSTANT_PLUS_SINGLE_LOG`.**

The corrected basis is smaller than the initially reported one. The next valid RG gate must use `B_0+B_1L`, not the superseded `A_0+A_1L+A_2L^2` ansatz.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.