# ITER105 terminal result — CDT global volume covariance versus EFT relational volume correlator

Date: 2026-09-15
Gate: `ITER105_LATTICE_RELATIONAL_VOLUME_CORRELATOR_EFT_SAME_OBSERVABLE_AUTHORITY`
Preregistration: `5f974a058cce39805b7d25b82eb472f81cbefcbf`
Source authority: `02e3e045d93cce7f1ae4aa2df55db9b5884d2e46`
Adversarial review: `7f8425bde02cf20ed4e443d9613bafe2faad004f`

## Terminal classification

**`FAIL_SCOPED_LOCAL_EFT_VOLUME_AND_CDT_SLICE_VOLUME_OBSERVABLE_IDENTITY_REJECTED`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Main result

The 2026 low-energy EFT volume correlator and the standard CDT spatial-volume covariance are not the same observable.

The EFT calculation uses the invariantized **local four-dimensional volume factor** `sqrt(det G)(X)` evaluated at relational/harmonic master-coordinate points and computes its point-to-point two-point function.

The CDT covariance uses the **integrated intrinsic three-volume of a preferred spatial slice**, `N_3(t)`, and measures

`C_tt' = <delta N_3(t) delta N_3(t')>`

in a compact, volume-fixed causal ensemble.

## Independent mismatches

1. Local four-volume density is not intrinsic slice three-volume.
2. Spatial integration of `sqrt(g_4)` is lapse-weighted and requires a source-defined foliation/lapse map before it can become `V_3`.
3. Harmonic relational time is not source-mapped to CDT discrete proper time.
4. The CDT fixed-total-volume constraint modifies the zero/global mode, while the EFT correlator is calculated as an unconstrained local low-energy observable around flat space.
5. Absolute lattice/continuum normalization is not enough to repair these object differences.

## Positive retained result

The new EFT paper supplies a valuable family of gauge-invariant relational observables for lattice comparison, but the correct lattice partner must be selected by observable semantics rather than by name. The already-published CDT minisuperspace covariance cannot simply be recycled for this purpose.

## Exact successor

`ITER106_RETROSPECTIVE_EDT_EFT_RELATIONAL_CURVATURE_CORRELATOR_IDENTITY_AUTHORITY`

The curvature route is better typed: four-dimensional Euclidean dynamical-triangulation literature explicitly measures scalar-curvature two-point functions conditioned on dynamical geodesic distance, while the 2026 EFT gives a universal gauge-invariant curvature-curvature correlator with noncontact long-distance falloff

`<R(X) R(Y)>_EFT = 768 G^2/(pi^2 r^8)`

in four Euclidean dimensions at the calculated order.

Because the older EDT qualitative correlator results were inspected before the next protocol, that successor must be retrospective with validation credit 0 and must first adjudicate separation and connectedness conventions before comparing exponents.

## Claim ceiling

No failure of CDT, no validation of EFT, no continuum/UV conclusion, no `BRIDGE_DERIVED`, no new physics and no candidate theory follows.