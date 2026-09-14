# ITER091 adversarial review — variable-volume cosmological response

Date: 2026-09-15
Preregistration: `47cb72c9c1c47d6f135847cc69ca2fe61c5282b7`
Source authority: `894a8bf253a596da6507d2388bcfb7849bc213ec`

## Attack 1 — `kappa_4` is already the cosmological constant, so identify it with `lambda_k`

Rejected. At bare Regge-action level `kappa_4` is related to the dimensionless combination `a^4 Lambda/G` and is conjugate to lattice four-volume. FRG `lambda_k=Lambda_k/k^2` is a renormalized running coupling defined in a continuum effective average action.

The direct CDT↔FRG source explicitly distinguishes bare and renormalized couplings and states that the renormalized CDT couplings are not known directly from the lattice bare couplings. A bare semantic relation to the classical cosmological term is not a renormalization map.

## Attack 2 — use `kappa_4-kappa_4^c` directly as the renormalized cosmological coupling

Critical subtraction is necessary but not sufficient. A scaling field generally also needs a normalization and scaling dimension/eigenvector relative to the critical surface. The frozen four-dimensional stack does not derive

`lambda_R = Z_lambda(a,...) [kappa_4-kappa_4^c]`

or an equivalent relation, nor does it show that the bare `kappa_4` direction is already an RG eigendirection when `kappa_0,Delta` are allowed to mix.

Thus subtraction removes the leading entropy counterterm but does not by itself define FRG `lambda_k`.

## Attack 3 — the exact susceptibility `Var(N_4)` is physical and therefore renormalized

The exact grand-canonical variance is a legitimate bare lattice response. Its continuum physical interpretation requires scaling with the cutoff/critical distance. Without that renormalization, its magnitude is lattice-unit and source-normalization dependent.

Moreover the practical simulations usually add a quadratic restraint, which changes the measured curvature of the volume distribution. Removing this external contribution recovers the underlying bare susceptibility; it does not automatically perform continuum renormalization.

## Attack 4 — Gaussian volume fixing can be used as a known probe, so its variance supplies the missing second equation

The fixing stiffness `epsilon` is chosen by the simulation. In the strongly restrained regime it can dominate the observed volume variance. Varying a numerical restraint is therefore a useful deconvolution method but is not a gravitational coupling direction.

Any equation in which the inferred FRG coupling changes when the arbitrary fixing stiffness changes would fail the frozen control.

## Attack 5 — `N_41` can replace total `N_4` because their ratio is approximately constant

This is adequate for some fixed-bare-coupling finite-size scaling, but an absolute cosmological susceptibility is the response of the source actually present in the action, namely total `N_4=N_41+N_32`. A restraint on `N_41` must be converted with the correlated `N_32` response if an exact grand-canonical susceptibility is claimed.

The approximation cannot create the missing renormalized FRG map.

## Attack 6 — the canonical/grand-canonical Laplace transform means no genuinely new information exists

Ensemble equivalence does not make the response redundant with the **conditioned fixed-volume minisuperspace distribution** used in ITER090. ITER090 fixes the zero mode/total volume. Restoring its conjugate source probes the density of states as volume changes, which is precisely the direction projected out by conditioning on fixed `V_4`.

Thus ITER091 genuinely crosses the boundary of the no-go in principle.

## Attack 7 — the exact 2d cosmological scaling formulas supply the missing renormalization

Rejected by dimensional/source scope. The direct paper uses two-dimensional quantum gravity as an analytically controlled analogy for volume/correlation-length scaling. The critical exponent and normalization of the four-dimensional cosmological source are not inherited automatically.

## Attack 8 — use the existing direct map for `g_k lambda_k` plus bare `kappa_4` to solve for both couplings

This mixes one renormalized equation with one unrenormalized bare source. Without a source-qualified relation between `kappa_4` (or its critical deviation) and `lambda_k`, the system is not closed. Solving it by an arbitrary proportionality constant would simply hide the missing renormalization in that constant.

## Verdict

The source classification survives:

**`PASS_SCOPED_BARE_VOLUME_RESPONSE_RENORMALIZED_MAP_OPEN`**.

Positive result: variable-volume response is a genuine independent **bare** direction and escapes the algebraic fixed-volume no-go.

Remaining blocker: no source-qualified four-dimensional renormalization/eigendirection map from the CDT cosmological source or susceptibility to FRG `lambda_k`.

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.
