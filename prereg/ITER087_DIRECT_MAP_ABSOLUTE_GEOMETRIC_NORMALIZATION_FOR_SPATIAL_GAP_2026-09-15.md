# ITER087 preregistration — absolute geometric normalization of the direct CDT↔FRG reduced map for a held-out spatial-gap test

Date: 2026-09-15
Gate: `ITER087_DIRECT_MAP_ABSOLUTE_GEOMETRIC_NORMALIZATION_FOR_SPATIAL_GAP`

## Motivation frozen before further numerical extraction

ITER086 rejected the ad hoc equality `k^2=z_1`. Its failure suggested a better route: use the source-defined self-consistent de-Sitter geometry to predict the spatial gap without assigning the gap itself to the FRG cutoff.

A naive combination of the simplified ITER078 equations appears to yield a dimensionless prediction of the form

`ell_1 sqrt(N_4) = C_simplified (omega/omega_0)^(2/3)`.

However, arXiv `2408.07808` explicitly states that geometric simplex-volume factors are set to one for notational/scaling purposes, distinguishes `(4,1)` and `(3,2)` simplex volumes, and notes that the relation between `N_4^(4,1)`, `sum_t N_3(t)` and total four-volume contains a coupling-dependent ratio.

Because ITER084 restored the **physical** local graph-Laplacian normalization using the actual equilateral-tetrahedron geometry, an absolute held-out spectral prediction cannot mix that normalization with the reduced map's suppressed volume factors without auditing the conventions first.

## Frozen question

Can the frozen CDT/direct-map source stack restore all geometric and counting factors needed to convert the reduced-map round-`S^4` radius into an absolute prediction for the normalized CDT spatial gap `ell_1`, with no fitted multiplicative constant?

Specifically, can it determine a unique coefficient in

`ell_1 sqrt(N_volume) = C(omega/omega_0, bare couplings)`,

where `N_volume` is precisely the volume variable used in the reduced map and the spectral simulation, after retaining:

- tetrahedron physical volume;
- `(4,1)` and `(3,2)` four-simplex volumes;
- spacelike/timelike anisotropy;
- the ratio `N_4^(3,2)/N_4^(4,1)` where required;
- the distinction between total controlled `N_4^(4,1)`, fitted blob volume `N_4`, total four-simplex number, and `sum_t N_3(t)`;
- stalk/blob subtraction where relevant.

## Frozen sources

- arXiv `2408.07808` — direct CDT↔FRG reduced-map equations, exact/simplex-volume caveat, numerical volume conventions.
- arXiv `2411.02330` — follow-up IR/UV interpretation and lattice-spacing normalization discussion.
- arXiv `1804.02294` — spectral-slice volume conventions and `L=4I-A` definition.
- arXiv `1912.11311` — later spatial-spectrum scaling conventions.
- ITER084 source/terminal records — only for `z_CDT=9 ell/a^2`; no missing global volume normalization may be filled from ITER084.

## Required predicates

A. The direct source's `N_4` appearing in the reduced action/map is unambiguously related to the controlled Monte-Carlo volume `N_4^(4,1)` and to `sum_t N_3(t)` with all numerical factors required for an absolute calculation.

B. The physical tetrahedron volume and both four-simplex volumes are explicit in the same spacelike edge-length convention `a` used by ITER084.

C. The anisotropy parameter entering the exact four-simplex volumes is source-related to the measured deformation `omega/omega_0` at the scope used by the direct map.

D. Any required ratio `N_4^(3,2)/N_4^(4,1)` is source-determined for the matched ensemble or cancels algebraically. A statement that it is merely approximately constant is insufficient for an absolute coefficient unless its value and uncertainty are provided.

E. Stalk volume and fitted blob `N_4` are separated whenever the reduced-map `omega,Gamma` extraction uses the blob rather than total controlled volume.

F. The central/equatorial spatial slice whose gap is to be predicted has a source-defined mapping to the equatorial `S^3` of the round continuum `S^4` after the `a_t/a` rescaling.

G. The round `S^3` spectral identity `z_1=3/R^2` is applied only after A-F pass and with the physical normalized CDT eigenvalue `z_CDT=9 ell_1/a^2`.

H. No free multiplicative coefficient, target gap, spectral-dimension datum or FRG trajectory is used to repair missing normalization.

I. Scaling-only relations are not promoted to absolute-normalization relations.

## Frozen controls

- `UNIT_SIMPLEX_VOLUME_ERASURE_CONTROL`: setting tetrahedron/four-simplex volumes to one is forbidden in an absolute spectral prediction.
- `N4_N41_SWAP_CONTROL`: `N_4`, `N_4^(4,1)`, total four-simplex count and `sum N_3` cannot be interchanged without source authority.
- `BLOB_TOTAL_VOLUME_SWAP_CONTROL`: fitted blob volume cannot be replaced by total controlled volume when stalk contributions are non-negligible.
- `SIMPLEX_RATIO_ERASURE_CONTROL`: `N_32/N_41` may not be dropped merely because it is approximately constant.
- `ANISOTROPY_ERASURE_CONTROL`: exact simplex volumes must retain the measured/derived spacelike-timelike asymmetry.
- `SCALING_ABSOLUTE_CONTROL`: a relation sufficient for critical exponents may still be insufficient for an absolute coefficient.
- `TARGET_GAP_FIT_CONTROL`: no spectral value may set a missing constant.
- `ROUND_SLICE_CONTROL`: the central CDT slice is not assumed exactly round unless the direct map supplies the relevant scoped identification.

## Frozen classifications

- `PASS_SCOPED_ABSOLUTE_GAP_NORMALIZATION_COEFFICIENT_DERIVED` if A-H determine a unique target-independent coefficient (with stated source uncertainties) for the held-out gap prediction.
- `PASS_SCOPED_RELATIVE_SCALING_ONLY_ABSOLUTE_COEFFICIENT_OPEN` if the sources determine the scaling with `N` and `omega` but leave one or more absolute geometric/counting factors unresolved.
- `SCOPED_BLOCKED_VOLUME_CONVENTION_MISMATCH` if the reduced-map and spectral-volume variables cannot be source-qualified into the same absolute convention.
- `FAIL_SCOPED_DIRECT_MAP_NORMALIZATION_INCONSISTENT` if source-defined exact factors contradict the simplified map in a way that cannot be reconciled at its claimed scope.
- `INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION` only for source transport/extraction failure.

## Claim ceiling

A PASS only authorizes a parameter-free **held-out spatial-gap prediction formula** to be tested in a later preregistered gate. It does not itself validate the formula, determine an FRG trajectory, establish a shared fixed point, create bridge credit or authorize candidate-theory construction.

Predicates, controls and classifications are frozen before additional matched numerical extraction.
