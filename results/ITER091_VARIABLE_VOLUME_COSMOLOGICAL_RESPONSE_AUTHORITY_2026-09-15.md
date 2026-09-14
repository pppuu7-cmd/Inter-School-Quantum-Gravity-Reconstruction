# ITER091 terminal result — variable-volume CDT cosmological response ↔ renormalized FRG cosmological direction

Date: 2026-09-15
Gate: `ITER091_VARIABLE_VOLUME_COSMOLOGICAL_RESPONSE_AUTHORITY`
Preregistration: `47cb72c9c1c47d6f135847cc69ca2fe61c5282b7`
Source authority: `894a8bf253a596da6507d2388bcfb7849bc213ec`
Adversarial review: `e555d70f57f4f5919a41a8bc4c8dd89fe5b6b965`

## Terminal classification

**`PASS_SCOPED_BARE_VOLUME_RESPONSE_RENORMALIZED_MAP_OPEN`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Exact positive result

The four-dimensional CDT grand-canonical ensemble contains a genuine source direction projected out by the fixed-volume construction used in ITER090.

The bare Regge action contains `kappa_4 N_4`, with `N_4=N_41+N_32`, and

`Z(kappa_4)=sum_N4 exp(-kappa_4 N_4) Z_N4`.

Therefore

`-partial_{kappa_4} ln Z = <N_4>`,

`partial_{kappa_4}^2 ln Z = Var(N_4)`.

This bare source/response pair is not algebraically redundant with the fixed-volume distribution: restoring the total-volume zero mode genuinely crosses the ITER090 no-go boundary.

## Critical-source refinement

The density of triangulations grows approximately as `exp(kappa_4^c N_4)`, so the large-volume source is the critical deviation

`delta kappa_4 = kappa_4-kappa_4^c(kappa_0,Delta)`,

not raw `kappa_4`.

Finite simulations use pseudocritical `kappa_4^c(N,kappa_0,Delta)` and often a quadratic volume restraint. The external fixing stiffness must be removed/accounted for before the measured variance can be called the underlying grand-canonical susceptibility.

## Renormalized blocker

The frozen CDT↔FRG source explicitly distinguishes bare lattice couplings from renormalized continuum couplings. It states that the renormalized CDT couplings are not known how to be calculated directly from the lattice bare couplings; its successful direct map concerns the reduced combination `g_k lambda_k`, not an independent renormalization of `kappa_4`.

No frozen source provides a source-defined four-dimensional relation

`lambda_k = F(delta kappa_4, a, kappa_0,Delta)`

or a typed map from the grand-canonical volume susceptibility to an FRG cosmological susceptibility.

Thus the new source direction is real, but it is currently **bare**, not yet a second renormalized FRG coordinate.

## What changed relative to ITER090

ITER090 should not be interpreted as saying no global second observable can exist. ITER091 establishes that changing ensemble restores a genuinely independent bare direction. The obstruction has moved from **identifiability** to **renormalization/source typing**.

## Claim ceiling

No separate `g_k` and `lambda_k`, no unique FRG trajectory, no shared fixed point, no bridge derivation and no candidate theory follow.

## Highest-information successor

Audit whether the finite-size approach

`kappa_4^c(N;kappa_0,Delta) -> kappa_4^c(infinity;kappa_0,Delta)`

has a source-qualified scaling exponent or scaling field in four-dimensional CDT. If a nontrivial critical exponent exists independently of the Gaussian fixing stiffness, it may define a renormalized cosmological-source direction on the CDT side before any FRG comparison is attempted.
