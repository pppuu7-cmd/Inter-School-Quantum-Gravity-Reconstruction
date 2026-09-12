# ITERATION 006 — RC006 serialization failure localization

Date: 2026-09-12

## Authoritative provenance

- Workflow run: `34700891523`
- Head commit: `8cb26ab0fb631ff36c2d2b52773019e021b4b665`
- Aggregate job: `103572467066`
- Summary artifact: `10300127995`
- Summary digest: `sha256:a9f94f2148035b1f0223c7a2168308224fea2f0ad1a50bd380e15c0d1fd2439b`

## Diagnostic result

All eight single-anchor localization lanes were valid. Four source anchors carry nontrivial ordering authority under the frozen fingerprint construction:

- `app:EPRL-diagram`
- `app:EPRL-norm`
- `app:graph`
- `eq:recoupling-basis`

Across the eight holdouts the maximum number of pairwise order flips was `73`, and the minimum agreement with the full-source canonical ordering was `0.8698752228163993`.

Classification: `DIAGNOSTIC_SOURCE_AUTHORITY_LOCALIZED`.

## Interpretation

This localizes the previously observed serialization instability to a small source-authority subset. It does **not** reverse the terminal scientific FAIL of run `34700639086` and does not authorize the minimal Eq.(29) amplitude. The next RC006 route is to determine whether the pinned source contains an explicit contraction/leg-order relation tying these four anchors together. Such authority must be frozen and tested independently before the blocked amplitude gate can reopen.

No threshold is weakened and no favorable anchor subset is selected post hoc.
