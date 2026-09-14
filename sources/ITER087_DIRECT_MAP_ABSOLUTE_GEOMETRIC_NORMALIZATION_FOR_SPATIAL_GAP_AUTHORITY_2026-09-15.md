# ITER087 source authority — absolute geometric normalization of the direct reduced map for a held-out spatial-gap test

Date: 2026-09-15
Gate: `ITER087_DIRECT_MAP_ABSOLUTE_GEOMETRIC_NORMALIZATION_FOR_SPATIAL_GAP`
Preregistration: `6f24c0c3004c2b423815695ce42b636147003960`

## Executive result

The frozen source stack supports the **scaling structure** needed for a gap test but does not restore a unique absolute coefficient compatible with ITER084's physical graph-Laplacian normalization.

The direct CDT↔FRG papers explicitly simplify geometric volume factors because they are studying scaling. The omitted factors are harmless for critical exponents and proportionality statements, but they are exactly the factors required for an absolute spectral prediction.

Classification:

**`PASS_SCOPED_RELATIVE_SCALING_ONLY_ABSOLUTE_COEFFICIENT_OPEN`**.

## A — volume-variable identity

**FAIL_FOR_ABSOLUTE_COEFFICIENT / PASS_FOR_SCALING.**

arXiv `2411.02330` defines the microscopic total number of four-simplices as

`N_4 = N_41 + N_32`.

Its finite-size discussion uses this total `N_4` as the gravity correlation-volume variable.

arXiv `2408.07808`, however, makes the reduced volume-profile identification

`sum_i N_3(i) = N_4`

inside its simplified minisuperspace translation, while its Appendix immediately states the exact combinatorial relation

`2 sum_i N_3(i) = N_4^(4,1) -> c N_4`,

where `c` depends on the bare couplings through the ratio of `(3,2)` and `(4,1)` simplices. The authors then say that they put this factor to one for notational simplicity.

The numerical analysis adds another distinction: simulations control `N_4^(4,1)` while the fitted `N_4` in the de-Sitter profile is the volume contained in the blob; the fitted blob value is checked against `sum_t <N_3(t)>` inside the blob and differs from the total controlled volume when the stalk is sizable.

Thus no unique absolute replacement among total `N_4`, controlled `N_41`, `sum N_3`, and fitted blob `N_4` is source-authorized with all coefficients retained.

## B — geometric simplex volumes

**PASS_PARTIAL.**

The direct source gives the unit-edge spatial tetrahedron volume `sqrt(2)/12` and records exact anisotropic four-simplex-volume formulas for `(4,1)` and `(3,2)` simplices before simplifying them.

This is sufficient to show that an absolute geometric restoration is in principle meaningful. It is not sufficient to complete it because the total four-volume requires the ensemble-dependent counts of the two four-simplex types in the same convention used by the reduced map.

## C — anisotropy/deformation relation

**PASS_SCOPED.**

The direct source derives

`a_t = (omega_0/omega)^(4/3) a`,

so the time/space rescaling required to round the deformed average geometry is source-defined within the reduced comparison.

This supplies the anisotropy scaling needed by an exact restoration, but does not fix the missing simplex-count ratio.

## D — `N_32/N_41` authority

**OPEN / DECISIVE ABSOLUTE BLOCKER.**

The source states that for fixed bare couplings the ratio of `(3,2)` to `(4,1)` simplices is approximately constant and independent of volume, but the reduced equations suppress the corresponding coupling-dependent factor `c`.

The frozen stack does not provide a matched numerical value and uncertainty for this ratio for every spectral/reduced ensemble required by an absolute gap prediction. Because this factor enters total physical four-volume, it cannot be set to one under `SIMPLEX_RATIO_ERASURE_CONTROL`.

## E — stalk/blob distinction

**PASS_AS_CONTROL / FAIL_FOR_NAIVE_TOTAL_VOLUME SUBSTITUTION.**

The 2024 direct paper explicitly reports that near the `A-C_dS` transition a significant fraction of the controlled volume can sit in the stalk. It therefore fits a blob volume `N_4` independently and uses that fitted quantity in the critical-scaling analysis.

The follow-up likewise states that the critical-scaling plots use the `N_4` volume contained in the `S^4` blob, not all four-simplices.

Consequently `N_4^(4,1)` from the simulation input cannot be inserted blindly as the reduced-map `N_4` in an absolute spectral formula.

## F — central slice ↔ equatorial round `S^3`

**PASS_SCOPED_AT_MEAN_PROFILE LEVEL, NOT EXACT SPECTRAL ISOMETRY.**

The direct map rescales the average de-Sitter volume profile to a continuum round `S^4` minisuperspace geometry. This identifies the maximum of the mean profile with the equatorial slice at the reduced/mean-field level.

The spectral papers stress, however, that individual CDT spatial `S^3` triangulations are not round embedded spheres; the spectrum is an independent observable of their fluctuating geometry. Therefore the map is sufficient to formulate a held-out spectral test, but not to assume the test must pass or to import the continuum gap as an identity.

## G — round spectral identity

**AUTHORIZED ONLY AFTER NORMALIZATION; ABSOLUTE TEST NOT YET AUTHORIZED.**

For a round `S^3` of radius `R`, `z_1=3/R^2`. ITER084 gives `z_CDT=9 ell_1/a^2`.

Combining these is mathematically straightforward. The obstruction is not the spectral identity but the missing exact conversion from the reduced lattice volume variable to the physical round-sphere radius with all source-suppressed factors restored.

## H/I — no fit and scaling/absolute distinction

**PASS_CONTROLS.**

No gap value was used to infer a missing coefficient. The provisional coefficient obtained by setting all suppressed volume factors to one is explicitly rejected as an absolute prediction.

## What remains source-qualified

Although the absolute coefficient is open, the direct stack does fix the **relative scaling**:

- at fixed bare couplings in the de-Sitter phase, `omega` approaches a volume-independent constant for sufficiently large volume;
- the reduced geometry has linear scale proportional to `N_4^(1/4)`;
- an equatorial round-sphere Laplace gap therefore scales as inverse radius squared, hence as `N_4^(-1/2)`;
- equivalently, using central spatial-slice volume `N_3 ~ N_4^(3/4)`, the gap scales as `N_3^(-2/3)`.

Any coupling-dependent constant from `N_32/N_41`, simplex volumes or the precise blob/total convention is volume-independent at fixed bare couplings in the scaling regime and cancels in **ratios between matched volumes**.

Thus a prospectively frozen relative finite-size test can be performed without the missing absolute normalization.

## Controls

- `UNIT_SIMPLEX_VOLUME_ERASURE_CONTROL`: triggered against absolute prediction; preserved.
- `N4_N41_SWAP_CONTROL`: triggered; distinctions retained.
- `BLOB_TOTAL_VOLUME_SWAP_CONTROL`: triggered near transition; distinctions retained.
- `SIMPLEX_RATIO_ERASURE_CONTROL`: triggered; missing factor not set to one.
- `ANISOTROPY_ERASURE_CONTROL`: passed; `a_t/a` relation retained.
- `SCALING_ABSOLUTE_CONTROL`: passed; final classification is scaling-only.
- `TARGET_GAP_FIT_CONTROL`: passed.
- `ROUND_SLICE_CONTROL`: passed as a held-out-test ceiling.

## Source classification

**`PASS_SCOPED_RELATIVE_SCALING_ONLY_ABSOLUTE_COEFFICIENT_OPEN`**

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.

## Highest-information successor

Freeze a same-bare-coupling, multi-volume test before reading the spectral target values:

`ell_1(N_b)/ell_1(N_a) = [N_b/N_a]^(-1/2)`

when the comparison uses the same qualified four-volume convention and lies in the large-volume de-Sitter scaling regime.

Or, using matched central spatial-slice volumes directly,

`ell_1(V_b)/ell_1(V_a) = [V_b/V_a]^(-2/3)`

for a round three-dimensional infrared geometry.

The second form avoids the `N_4`/`N_41` conversion and is therefore the cleaner next gate. Any observed deviation must be interpreted as a failure of the round-`S^3` infrared spectral hypothesis at that scale, not repaired by an absolute normalization factor.
