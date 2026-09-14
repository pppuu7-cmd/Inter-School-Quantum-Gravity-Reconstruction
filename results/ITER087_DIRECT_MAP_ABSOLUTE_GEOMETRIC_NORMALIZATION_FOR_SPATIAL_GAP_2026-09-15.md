# ITER087 terminal result — absolute geometric normalization of the direct reduced map for a held-out spatial-gap test

Date: 2026-09-15
Gate: `ITER087_DIRECT_MAP_ABSOLUTE_GEOMETRIC_NORMALIZATION_FOR_SPATIAL_GAP`
Preregistration: `6f24c0c3004c2b423815695ce42b636147003960`
Source authority: `80f070bfeb953f2ba0e7ce8a4a2719c723f7b616`
Adversarial review: `9b81e979f5f5d89bb9b21ac189c534f1e60ff6fe`

## Terminal classification

**`PASS_SCOPED_RELATIVE_SCALING_ONLY_ABSOLUTE_COEFFICIENT_OPEN`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Main result

The simplified direct CDT↔FRG reduced map is adequate for scaling and dimensionless reduced-coupling relations, but the frozen sources do not retain enough geometric/counting information to combine it with ITER084's physically normalized graph Laplacian into a unique **absolute** spatial-gap coefficient.

The missing factors are source-explicit rather than hypothetical:

- exact physical volumes of `(4,1)` and `(3,2)` four-simplices differ and depend on the time/space anisotropy;
- total `N_4`, controlled `N_41`, `sum_t N_3(t)` and fitted blob `N_4` are distinct variables;
- the source writes `2 sum_t N_3(t)=N_41 -> c N_4`, with bare-coupling-dependent `c`, and then sets that factor to one for notational/scaling simplicity;
- near the `A-C_dS` transition the stalk contribution can be non-negligible, so the fitted blob volume is not automatically the total controlled volume;
- the required matched `N_32/N_41` ratio is not supplied in the frozen stack with the precision needed for an absolute coefficient.

Thus the provisional coefficient obtained by blindly combining `V_4=(omega_0/omega)^(4/3)N_4 a^4` with `z_CDT=9 ell/a^2` is **not authorized as an absolute prediction**.

## What remains valid

At fixed bare couplings in the large-volume de-Sitter scaling regime the omitted geometric/counting factors are volume-independent to the source-qualified accuracy. They therefore cancel in relative finite-size ratios.

This leaves two testable scaling predictions:

1. in a consistent four-volume convention,
   `ell_1 propto N_4^(-1/2)`;
2. more cleanly, using the measured spatial-slice volume directly,
   **`ell_1 propto V_s^(-2/3)`**
   for an infrared round three-dimensional geometry.

The second relation avoids the `N_4/N_41/blob` normalization ambiguity and is the preferred successor.

## Why this is still progress

ITER087 prevents a false positive that would have arisen from mixing two normalization conventions at different precision levels. At the same time it identifies a ratio test in which the nuisance constants cancel prospectively.

No target spectral value was used to reach this result.

## Claim ceiling

No absolute gap prediction, no FRG trajectory, no shared fixed point, no bridge derivation and no candidate theory follow.

## Highest-information successor

Preregister and test, at fixed bare couplings within the `C_dS` phase, whether the **lowest nonzero** CDT spatial Laplacian eigenvalue obeys

`ell_1(V_b)/ell_1(V_a) = (V_b/V_a)^(-2/3)`

for independently selected large central-slice volume windows.

The volume windows, mode index and fit rule must be frozen before reading the numerical gap values. Failure must not be rescued by changing eigenmode or effective dimension after the fact.
