# ITER085 adversarial review — normalized CDT spatial mode ↔ FRG regulator threshold

Date: 2026-09-15
Preregistration: `c5abaa46cdc5a32801b469fb195e4aa2e8d455f1`
Source authority: `ff5c24e32e9757fd533edd0878b11e73e4d8f67b`

## Attack 1 — the background-spatial route is only a candidate mentioned by the 2023 paper

The 2023 fluctuation paper indeed does **not** implement the spatial regulator in its production flow. However, its regulator discussion explicitly states that the purely spatial Laplacian route is the one taken in the earlier background computations it cites. The 2016 background paper independently uses a Type-I Litim cutoff in the foliated background flow and reports the resulting flow for a `d`-dimensional spatial slice.

**Verdict:** the spatial route is source-qualified at background level, but it must not be attributed to the 2023 production calculation.

## Attack 2 — `z_CDT/k^2=1` secretly sets `k=1/a`

No. With ITER084,

`z_CDT = 9 lambda_graph/a^2`,

so the Litim threshold occurs at

`k_thr = sqrt(z_CDT) = 3 sqrt(lambda_graph)/a`.

The dimensionless graph eigenvalue remains mode-dependent. This is not `k=1/a`, and no universal proportionality between the lattice cutoff and FRG cutoff follows.

**Verdict:** threshold scale is a regulator-mode probe scale only.

## Attack 3 — the Litim threshold `1` is universal physics

Rejected. The value `z/k^2=1` is fixed by the chosen Litim profile. A different admissible regulator changes the detailed profile and potentially the operational threshold convention. Scheme dependence must be retained.

## Attack 4 — set `p0=0` in the production flow and obtain the same spatial crosswalk

Rejected as a full-production identification. The 2023 source separately projects external vertices onto `p0^2` and `vec(p)^2`, but its **loop regulator** remains a function of `q^2=q0^2+vec(q)^2`, with integration domain `q0^2+vec(q)^2<=k^2`. Setting an external frequency to zero does not remove the temporal loop momentum.

The source does not define a production flow in which the regulator is replaced by `R_k(vec(q)^2)`.

## Attack 5 — nevertheless the production regulator contains no information usable from a spatial eigenvalue

Too strong. If one conditionally inserts a spatial eigenvalue `z_sp` into the spatial part of the covariant regulator argument, then

`q0^2 + z_sp < k^2`.

This implies a source-defined **support envelope**:

- if `z_sp >= k^2`, no real temporal mode is inside the Litim support;
- if `z_sp < k^2`, supported temporal modes satisfy
  `|q0| < sqrt(k^2-z_sp)`.

Thus the spatial eigenvalue determines whether the corresponding spatial sector can have any regulated temporal modes and, if so, the allowed temporal bandwidth. It still does not specify a unique full production eigenmode.

For the normalized CDT candidate this becomes

`|q0| < sqrt(k^2 - 9 lambda_graph/a^2)`

when the radicand is positive.

## Attack 6 — same eigenvalue dimension means same spectral geometry

Rejected. ITER084 fixed a local finite-regulator normalization under a cell-centred discretization; it did not prove global spectral convergence of CDT slices to the FRG background geometry. Consequently `z_CDT` may be used as a normalized **probe argument** under the scoped crosswalk, but equality of eigenvalues does not establish equality of eigenfunctions, multiplicities, background geometry, spectral measure or continuum domain.

This is an important residual ceiling.

## Attack 7 — the threshold can now determine the FRG trajectory

Rejected. A regulator mode threshold contains no information fixing `(g_k,lambda_k,...)`. ITER080's trajectory underdetermination remains intact. Choosing a trajectory from CDT spectral values would violate the frozen target-fit control.

## Attack 8 — background and fluctuation fixed points are close, so the spatial regulator may be transferred to production

Rejected. Qualitative or numerical robustness of fixed points under scheme/truncation changes is not an operator identity. The source explicitly records different regulator choices. The gate is about typed regulator support, not universality evidence.

## Adversarial verdict

The strongest defensible classification is

**`PASS_SCOPED_BACKGROUND_SPATIAL_THRESHOLD_ROUTE_PRODUCTION_COVARIANT_OPEN`**.

Retained positive sub-result for the production flow:

**`PRODUCTION_COVARIANT_SUPPORT_ENVELOPE_FROM_SPATIAL_EIGENVALUE`**.

This envelope is weaker than a full mode crosswalk and cannot be promoted to `PASS_SCOPED_PRODUCTION_SPATIAL_REGULATOR_MODE_THRESHOLD_CROSSWALK`.

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.
