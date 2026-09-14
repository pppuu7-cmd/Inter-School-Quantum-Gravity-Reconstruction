# ITER103 adversarial critic — CDT directional QRC constraint

Date: 2026-09-15
Gate: `ITER103_RETROSPECTIVE_CDT_DIRECTIONAL_QRC_TRACELESS_RICCI_CONSTRAINT`
Protocol: `bbb8df519d8d60cbf2e1e05818f03092b524a9cd`
Source authority: `98814cce68a667e191db6c1fec3ea4ec7278a761`
Retrospective validation credit: **0**

## Attack 1 — the fitted vertical shift can manufacture isotropy

Partially valid as a systematic warning, but it does not erase the source result. A single constant shift `-0.476` is fixed at `delta=6`; it cannot in general force two scale-dependent curves to coincide over all larger radii if their curvature profiles have different shapes. The reported near-perfect agreement for `delta>6` therefore carries nontrivial two-class shape information.

However, because the offset is selected diagnostically from the same directional dataset, ITER103 does not treat the match as prospective validation or as an independently normalized equality of QRC values.

## Attack 2 — two directional classes imply vanishing traceless Ricci tensor

Rejected. A four-dimensional traceless symmetric tensor has more independent information than two coarse projections. Maximally spacelike and maximally timelike classes can test a prominent anisotropy channel, but equality between them does not reconstruct all angular components or prove `S_ij=0`.

## Attack 3 — the selected sample may bias the directional result

Retained as a scope limitation. The construction keeps centre configurations for which a maximally timelike partner exists through the largest radius, succeeding for roughly half of attempted cases. The source argues the sample is plausibly representative, but no independent reweighting proof is supplied. This lowers the strength of the conclusion from a full isotropy theorem to source-reported two-class consistency.

## Attack 4 — use the `delta>6` equality as a numerical test of the ITER102 local coefficient

Rejected. ITER102 is a `delta -> 0` smooth-manifold expansion. The published CDT comparison operates deliberately outside the strongest lattice-artifact region and at finite radii. No controlled continuum overlap window maps those data to the local coefficient `-0.0469 delta^2 S_ij v^i v^j`.

## Attack 5 — author language “isotropic” should be promoted literally to local geometric isotropy

Rejected as too strong. The source's conclusion is properly retained as isotropy of the measured QRC curvature behaviour within accuracy and within the two directional classes. The project must not silently strengthen that into a statement about every local tensor component.

## Attack 6 — the result is too weak to matter

Rejected. The measurement is an independent quasi-local geometric observable and demonstrates that the leading visible directional difference is compatible with a nonuniversal lattice offset rather than a different scale-dependent curvature profile. This is useful source authority, even though it is not a full tensor reconstruction and receives retrospective credit 0.

## Critic verdict

**CONFIRMS `SOURCE_SUPPORTS_TWO_CLASS_DIRECTIONAL_CURVATURE_ISOTROPY_NOT_FULL_TENSOR_RECONSTRUCTION`.**

The correct next question is not to reinterpret these two directions more aggressively, but to determine whether FRG has an explicitly renormalized relational traceless-Ricci / Einstein-tensor / spin-2 curvature composite against which this independent QRC channel could eventually be typed.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.