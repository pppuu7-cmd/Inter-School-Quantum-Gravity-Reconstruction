# ITER087 adversarial review — absolute geometric normalization for the held-out spatial-gap route

Date: 2026-09-15
Preregistration: `6f24c0c3004c2b423815695ce42b636147003960`
Source authority: `80f070bfeb953f2ba0e7ce8a4a2719c723f7b616`

## Attack 1 — restore the missing factor from `N_41=2 sum N_3`

This relation is exact for the total number of spatial tetrahedra, but it does not restore the total physical four-volume. The direct source distinguishes `N_41` from `N_32`, with

`N_4(total)=N_41+N_32`,

and explicitly writes `N_41 -> c N_4` with a bare-coupling-dependent `c` before setting `c=1` for scaling notation.

**Verdict:** exact spatial counting alone does not fix the absolute reduced four-volume coefficient.

## Attack 2 — use the exact `(4,1)` and `(3,2)` simplex volumes from Regge geometry

The exact per-simplex volumes are source-available, but total volume still requires the matched `N_32/N_41` ratio and the same anisotropy convention. The frozen stack does not provide the needed ensemble-by-ensemble ratio with uncertainty for the spectral comparison.

**Verdict:** per-simplex geometry does not close the ensemble-count factor.

## Attack 3 — the ratio is approximately constant, so choose any representative value

Rejected by `SIMPLEX_RATIO_ERASURE_CONTROL`. “Approximately constant in volume at fixed bare couplings” is enough to justify cancellation in relative finite-size ratios; it is not enough to authorize an absolute numerical coefficient across bare-coupling points.

## Attack 4 — ignore the stalk because the large-volume limit is dominated by the blob

This is not source-safe near the very transition region of interest. The direct numerical paper explicitly fits the blob `N_4` independently because the stalk contribution can become large. Substituting controlled `N_41` for fitted blob volume would change the absolute coefficient.

For ratios based directly on the measured central spatial-slice volume, this issue can be avoided.

## Attack 5 — use the simplified map exactly as printed, because ITER078 already accepted it

ITER078 accepted the map at its stated scope: reduced-action parameter and scaling crosswalk. It did not certify every suppressed Regge volume factor for a new absolute spectral observable. ITER084, in contrast, explicitly restored actual tetrahedral geometry to normalize the Laplacian.

Combining a physical edge-length spectral normalization with a convention where simplex volumes were explicitly set to one would overstate the source precision.

## Attack 6 — therefore no spectral prediction is possible at all

Too strong. At fixed bare couplings in the large-volume `C_dS` scaling regime, the omitted counting/volume factors are volume-independent to the stated source accuracy. They cancel in ratios.

Moreover, using the **measured spatial slice volume** directly avoids the four-dimensional `N_4` convention entirely. For a round three-dimensional infrared geometry,

`ell_1(V_s) propto V_s^(-2/3)`.

This is an absolute-normalization-free held-out prediction and is scientifically sharper than forcing a global coefficient from simplified volume conventions.

## Attack 7 — round-sphere scaling is already guaranteed by the de-Sitter volume profile

Rejected. The de-Sitter `N_3(t)` profile is a global one-point observable. The spatial Laplacian spectrum is an independent observable and the spectral papers explicitly stress that individual spatial triangulations are not simply round embedded spheres. Thus the `V_s^(-2/3)` spectral law remains a legitimate held-out test.

## Verdict

The source-authority classification survives:

**`PASS_SCOPED_RELATIVE_SCALING_ONLY_ABSOLUTE_COEFFICIENT_OPEN`**.

The important scientific consequence is methodological: the next test should use **same-bare-coupling volume ratios**, preferably in directly measured spatial slice volume, rather than attempt to reconstruct an absolute `N_4` coefficient from deliberately suppressed geometric factors.

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.
