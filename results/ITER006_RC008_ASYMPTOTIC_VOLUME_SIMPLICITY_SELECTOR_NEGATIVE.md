# ITERATION 006 — RC008 asymptotic volume-simplicity selector

Date: 2026-09-12

## Authoritative provenance

- Workflow run: `34700870181`
- Head commit: `f93326b4f5f45e36f2f955b367103c9f580caed1`
- Aggregate job: `103572312400`
- Summary artifact: `10300317494`
- Summary digest: `sha256:6a7e7bce9add0a0074abdaf433e7a24edd7868f47edbd0157b4afa07304b2e8a`

## Frozen test

Five independent lanes used the already frozen alpha values `0.45, 0.55, 0.63, 0.67, 0.75`. Each lane evaluated the source-asymptotic dressed quantum-hypercuboid amplitude under equal-scale perturbations away from exact volume simplicity. No published `alpha_*` was fitted.

The frozen aggregate required at least `3/5` lane PASS for natural selector support and `4/5` for strong support.

## Terminal result

All five computations were valid, but `0/5` lanes passed the preregistered selector criterion.

- `valid = true`
- `lanes_passed = 0`
- `natural_dynamic_selector_support = false`
- `strong_dynamic_selector_support = false`
- scientific classification: `SCIENTIFIC_NEGATIVE_SELECTOR_NOT_SUPPORTED`

## Interpretation

Within this local source-asymptotic dressed-amplitude diagnostic, the amplitude does not supply the preregistered dynamic preference for the volume-simple submanifold. Volume simplicity therefore remains an independent source-native condition/selector at this level rather than an emergent result of this local amplitude test.

This negative does **not** imply failure of the full quantum-hypercuboid renormalization calculation. It strengthens the need for an actual coarse/refined amplitude computation with the full gluing/state-sum structure.

## Claim lock

No full RC008 amplitude reproduction, RG flow, refinement bridge, `BRIDGE_DERIVED`, new physics, or candidate theory is established.
