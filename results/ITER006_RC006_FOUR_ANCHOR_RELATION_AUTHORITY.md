# ITER006 — RC006 four-anchor explicit source-relation authority

Date: 2026-09-12

## Prerequisite blocker

The previous contraction-serialization stability gate `34700639086` was a scientific FAIL: full-source ordering was unique, but only 6/8 leave-one-anchor holdouts remained unique and the minimum pairwise-order agreement fell to `0.8698752228163993`. Eq.(29) numerical amplitude therefore remained blocked.

A later diagnostic localized the source-authority sensitivity to four anchors: `app:EPRL-diagram`, `app:EPRL-norm`, `app:graph`, and `eq:recoupling-basis`.

## New prospective source-authority audit

Preregistered before production in `protocol/ITER006_RC006_FOUR_ANCHOR_RELATION_PREREG.json`.

Authoritative run: `34712998699`, launch commit `078fd4846a587156836b293c323fee83d0f943d1`, job `103605052196`, artifact `10304191011`, digest `sha256:d4c4cbbe7fe84fcbb0844ea02ccc4ebf794e2965288bafa66a52b7d322781c8a`.

All four frozen anchors occurred once. The source-explicit reference graph contains exactly three directed inter-anchor edges:

- `app:EPRL-diagram -> app:graph`
- `app:EPRL-norm -> app:graph`
- `eq:recoupling-basis -> app:graph`

All four anchors therefore belong to one connected component and the preregistered threshold of at least three explicit inter-anchor edges is met.

Classification: `RC006_FOUR_ANCHOR_EXPLICIT_RELATION_SOURCE_PASS`.

## Consequence

This is genuinely new source authority relative to the failed serialization gate and authorizes exactly one prospectively frozen relation-aware serialization retry. It does **not** itself reverse run `34700639086`, does not establish Eq.(29), and does not authorize deletion or down-weighting of any troublesome anchor.

The retry is preregistered at commit `c03b50a33d9937f542668b90751ec295bc235c24` and launched at commit `7a034f0766277656eb5fc09d3c492299e364281e`. It preserves the original 10-lane gate: full unique, all eight holdouts unique, minimum pairwise-order agreement exactly `1.0`, and unordered null ambiguous.

If that exact retry fails, Eq.(29) remains blocked absent genuinely new independent source authority.

## Claim lock

No Eq.(29) amplitude, q-deformed EPRL/FK amplitude, TNR refinement bridge, `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, or candidate-theory claim follows from the present source-authority PASS.
