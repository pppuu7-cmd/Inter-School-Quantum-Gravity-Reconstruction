# ITER084 terminal result — CDT cell-centred TPFA ↔ dual-graph Laplacian normalization

Date: 2026-09-15
Gate: `ITER084_CDT_CELL_CENTERED_TPFA_GRAPH_LAPLACIAN_NORMALIZATION`
Preregistration: `68138f796c29d2bd7035d12083b8a8d53b593519`
Workflow launch: `74d08a37425cd5b982699ad3c3b3e07039cd8dab`
Source authority: `6155de3f2aeeea12472fd2f560df64fe3d6ec760`
Adversarial review: `cba0535984bb00a1745a5c10ab42aaed3bd671d5`

## Terminal classification

**`PASS_SCOPED_EXACT_LOCAL_TPFA_COEFFICIENT_CONTINUUM_CONVERGENCE_OPEN`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Main result

ITER083A's missing local geometric coefficient is resolved under a prospectively frozen, target-independent cell-centred finite-volume interpretation of the actual CDT dual-graph field.

For a spatial regular tetrahedron of edge length `a`,

- face area `A_f = (sqrt(3)/4)a^2`,
- cell volume `V_t = a^3/(6 sqrt(2))`,
- adjacent tetrahedron-centre distance `d = a/sqrt(6)`.

The source-defined TPFA transmissibility is `tau=A_f/d`, and all four faces/neighbours have identical transmissibility. Dividing the cell flux balance by `V_t` gives

**`-Delta_FV = (9/a^2)(4I-A)`**,

so that

**`lambda_FV = (9/a^2) lambda_graph`**

at finite regulator within the frozen discretization.

No FRG scale, target spectrum, de-Sitter matching, spectral-dimension curve, critical exponent or fitted constant appears in the derivation.

## Independent consistency check

The same coefficient follows directly from the second moment of the four tetrahedral neighbour directions. With neighbour separation `d=a/sqrt(6)`, tetrahedral symmetry gives `sum_i n_i n_i^T=(4/3)I`, so Taylor expansion yields

`(4I-A)f = -(a^2/9) Delta f + ...`.

Thus the factor `9/a^2` is not an isolated finite-volume convention; it is the isotropic normalization of the actual four-neighbour tetrahedral stencil.

## What this closes

The narrow ITER083A blocker `EXACT_GRAPH_CONTINUUM_LOCAL_NORMALIZATION_COEFFICIENT_OPEN` is closed at finite regulator under the cell-centred TPFA interpretation.

It is therefore no longer accurate to treat the spatial graph eigenvalues as normalized only up to an arbitrary multiplicative geometric constant. The finite-regulator conversion to a unit-diffusivity local Laplace operator is fixed by the equilateral tetrahedron geometry.

## What remains open

1. The Eymard-Gallouët-Herbin convergence theorem is for admissible meshes of Euclidean polygonal/polyhedral domains. It does not by itself prove spectral convergence of fluctuating curved CDT piecewise-flat manifolds to a smooth continuum Laplace-Beltrami operator as `a -> 0`.
2. ITER084 does not determine the CDT continuum trajectory or prove a second-order critical point.
3. It does not identify the FRG cutoff `k` with any CDT eigenvalue or with `1/a`.
4. It does not resolve the underdetermined FRG trajectory identified by ITER080.
5. It does not authorize an absolute Planck-scale prediction without importing separately qualified scale authority and its assumptions.

## Claim ceiling

No CDT continuum theorem, no `lambda_CDT=k^2`, no FRG trajectory, no shared fixed point, no theory equivalence, no bridge derivation and no candidate theory follow.

## Highest-information successor

The next useful gate is no longer another graph-normalization search. It should ask whether the **source-selected foliated-FRG regulator profile itself** supplies a target-independent mode-threshold rule `z/k^2 = const` for the already normalized CDT spatial eigenvalue

`z_CDT = 9 lambda_graph/a^2`,

and whether this can be used as a typed probe-scale crosswalk without identifying the lattice cutoff `1/a` with the FRG cutoff `k` or using CDT spectral targets to choose an FRG trajectory.

A PASS there would authorize at most a regulator-mode probe crosswalk, not physical theory equivalence or bridge credit.
