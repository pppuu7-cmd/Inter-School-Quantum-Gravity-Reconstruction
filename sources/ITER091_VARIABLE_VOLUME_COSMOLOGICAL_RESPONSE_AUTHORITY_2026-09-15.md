# ITER091 source authority — variable-volume CDT cosmological response ↔ renormalized FRG cosmological direction

Date: 2026-09-15
Gate: `ITER091_VARIABLE_VOLUME_COSMOLOGICAL_RESPONSE_AUTHORITY`
Preregistration: `47cb72c9c1c47d6f135847cc69ca2fe61c5282b7`

## 1. Bare grand-canonical volume conjugacy is exact

The four-dimensional CDT Euclidean Regge action contains

`S_R = -(kappa_0+6 Delta) N_0 + kappa_4 (N_41+N_32) + Delta N_41`,

so the bare coupling `kappa_4` is conjugate to the total four-simplex count

`N_4 = N_41 + N_32`.

The standard grand-canonical decomposition is

`Z(kappa_0,Delta,kappa_4) = sum_{N_4} exp(-kappa_4 N_4) Z_{N_4}(kappa_0,Delta)`.

Therefore, at fixed `kappa_0,Delta` and in the unfixed-volume ensemble,

`- partial_{kappa_4} ln Z = <N_4>`,

and

`partial_{kappa_4}^2 ln Z = <N_4^2>-<N_4>^2 = Var(N_4)`.

This is an exact bare source/response pair. It lies outside the fixed-volume identifiability no-go of ITER090 because the total volume itself is allowed to fluctuate.

## 2. The relevant bare source is distance from the critical surface, not raw `kappa_4`

The fixed-volume partition function grows approximately as

`Z_{N_4} ~ exp(kappa_4^c N_4)`

at large volume. Thus the grand-canonical weight is controlled at leading order by

`exp[-(kappa_4-kappa_4^c) N_4]`.

For `kappa_4 < kappa_4^c` the sum is not well defined, while approaching `kappa_4^c` from above sends the average volume large.

Hence any continuum/infinite-volume susceptibility must retain the critical subtraction

`delta kappa_4 = kappa_4-kappa_4^c(kappa_0,Delta)`.

A raw value of `kappa_4` is not a universal cosmological observable.

## 3. Finite simulations use pseudocritical tuning and usually trade `kappa_4` for volume

At finite target volume simulations tune

`kappa_4 -> kappa_4^c(N,kappa_0,Delta)`

and introduce a volume-fixing potential, commonly

`S_VF = epsilon (N_41-Nbar_41)^2`.

The phase-structure literature explicitly says this trades the `kappa_4` direction for the chosen average volume and leaves an effective two-dimensional bare parameter plane in `kappa_0,Delta` at fixed target volume.

The finite-volume pseudocritical value approaches the true critical value only in the large-volume limit.

Thus measured fluctuations under `S_VF` are not automatically the grand-canonical physical susceptibility. The external quadratic restraint contributes a known artificial restoring curvature in the `N_41` direction and must be removed/undone before interpreting the variance as `partial^2 ln Z/partial kappa_4^2`.

A further type distinction remains: the simulation restraint is often imposed on `N_41`, while the bare cosmological term is conjugate to total `N_4=N_41+N_32`. At fixed `kappa_0,Delta` the ratio can be approximately stable, but an absolute response conversion requires its source-defined treatment rather than silent substitution.

## 4. CDT criticality does not by itself supply the renormalized FRG cosmological coupling

The direct CDT↔FRG paper arXiv `2408.07808` explicitly classifies `kappa_0, Delta, kappa_4` as **bare lattice couplings**. It states that `kappa_4` is related at bare Regge-action level to the dimensionless combination `a^4 Lambda/G`, controls `N_4`, and is traded for volume in the Monte Carlo setup.

The same paper then opens a separate section on **renormalized versus bare coupling constants** and states that renormalized couplings depend on both bare couplings and the cutoff and require fine-tuning toward a critical surface. Most decisively, its renormalization discussion says that for CDT the renormalized coupling constants corresponding to the lattice theory are not known how to be calculated; the paper instead assumes that they can be identified with those in a simple FRG model and constructs a map for the combination `lambda_k g_k` from the reduced volume sector.

The frozen source stack does not provide an equation of the form

`lambda_k = F(delta kappa_4, a, kappa_0,Delta)`

or a renormalized Legendre-response relation mapping

`Var(N_4)` / `partial<N_4>/partial kappa_4`

to an FRG cosmological susceptibility at scale `k`.

Therefore bare grand-canonical conjugacy does not close the renormalized cross-framework map.

## 5. Two-dimensional exact analogy is not four-dimensional authority

The direct paper reviews two-dimensional quantum gravity, where a lattice cosmological source `mu-mu_c`, average area, geodesic correlation length and canonical/grand-canonical Laplace transform are analytically related. It uses this as conceptual support for treating `N_4^(1/4)` as a four-dimensional correlation length.

Those exact 2d formulae do not establish the four-dimensional scaling exponent or normalization of `delta kappa_4` into a renormalized cosmological coupling. They cannot fill predicates G/H for four-dimensional CDT.

## Predicate adjudication

- A — exact bare `kappa_4` conjugacy to total `N_4`: **PASS**.
- B — grand-canonical/canonical discrete Laplace relation: **PASS**.
- C — bare response identities: **PASS** by exact differentiation of the source-defined partition function.
- D — critical subtraction retained: **PASS**.
- E — pseudocritical finite-volume distinction: **PASS**.
- F — Gaussian volume-fixing artifact distinguished from physical susceptibility: **PASS_CONTROL**.
- G — source-defined four-dimensional renormalization from `delta kappa_4`/susceptibility to a continuum cosmological response: **OPEN / NOT ESTABLISHED**.
- H — typed independent map to FRG `lambda_k`: **OPEN / NOT ESTABLISHED**.
- I — bare/pseudocritical/lattice-effective/FRG cosmological parameters kept distinct: **PASS_CONTROL**.
- J — no target normalization/trajectory fit: **PASS_CONTROL**.

## Source classification

**`PASS_SCOPED_BARE_VOLUME_RESPONSE_RENORMALIZED_MAP_OPEN`**

ITER091 confirms that changing ensemble genuinely escapes the algebraic fixed-volume no-go: total-volume response is an independent bare source direction. But the frozen four-dimensional source stack does not renormalize that response into `lambda_k` independently of the already-qualified fixed-volume product `g_k lambda_k`.

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.

## Highest-information successor

The next useful gate should not re-measure `Var(N_4)` under a Gaussian restraint. It should ask whether the **finite-size approach of the pseudocritical source**

`kappa_4^c(N_4;kappa_0,Delta) -> kappa_4^c(infinity;kappa_0,Delta)`

has a source-qualified scaling exponent/amplitude that can define a renormalized volume-source scaling field independently of the external fixing stiffness.

The first task is CDT-internal: establish whether a critical exponent for this cosmological-source direction is actually measured/derivable in four dimensions. Only afterward should any relation to an FRG critical exponent or cosmological eigendirection be considered.
