# ITER023 — RC006 qbar/R authority split

Date: 2026-09-14

## Frozen gate
Prospectively frozen split audit of (i) qbar graph-to-index ordering authority and (ii) exact R-matrix authority. No numerical fitting/orientation selection was permitted. Full PASS alone could authorize a separately preregistered bounded Eq.(27) contraction.

## Authoritative provenance
- prereg: `f236741ce6b76050b40ed9fc5ef52998048a8c35`
- implementation: `b3ac56b8dec57873d2e59c72c57c30b64f1f46b3`
- production head: `86366a7abd003c166ea5ef277b1a3d1048e92e0a`
- run: `34785936567`
- jobs: qbar-inventory `103801306450`; r-authority `103801306540`; qbar-orientation `103801306566`; provenance-null `103801306710`; aggregate `103801340359`
- artifacts: qbar-inventory `10326980301` digest `sha256:8227e7e19d3c3332e409a92b3965e461eec76bca46d676f2d2a182b7fc6b18db`; r-authority `10326551766` digest `sha256:ee26345e1157eaf7d8741ab3fe364d85da2561b2e0025644b90f6ed953a493e2`; qbar-orientation `10326239080` digest `sha256:5384deb8d57ab26dd9b7723da65a91ce12aa7e60f1857aab4855971115ad0d1a`; provenance-null `10326184126` digest `sha256:ebb162c687a4cf34da284c13754f5f3705ede9b10d9e797190f4c54d2afc83f7`; aggregate `10326268909` digest `sha256:626ed7f8fc035b845783828f8121d0da40698804d2cd44369a47af5c4f32d642`.

## Raw scientific classification
Aggregate classification: `RC006_QBAR_INDEX_ORDER_BLOCKED`.

- qbar-inventory: BLOCKED_GRAPHICAL_ONLY. Source contains qbar, q-CG, cap/cup and inverse-q signals, but no explicit index-level equality fixing graph-to-index ordering.
- qbar-orientation: BLOCKED. Six prospectively enumerated candidate maps were tested; zero were source-qualified survivors; no numerical fit was used.
- R-authority: BLOCKED_BARE_MENTION_OR_REFERENCE. The preserved source gives graphical R/R^-1 decompositions but the frozen authority detector did not establish an independently executable component formula/source cancellation chain.
- provenance/null: PASS. Historical source hash matched, missing orientation manifest was rejected, ordinary-Hermitian substitution was rejected, cap/cup residual remained `2.6360122491655997e-17` against `1e-12`.

Green CI is not the scientific classification. This is not a scientific failure of q-deformed EPRL; it is an authority/translation blocker.

## Locks
`bridge_credit=false`; `candidate_theory_authorized=false`; `iter012_retry_authorized=false`; `eq29_amplitude_authorized=false`; `new_physics_found=false`; `preferred_alpha_found=false`.

## Next allowed gate
Resolve the exact cited-source authority chain behind `q-spinnet`, `biedenharn`, and `wojtek` and determine whether those sources provide an explicit index-level qbar duality map and an executable R-matrix convention compatible with the already frozen q-CG/cap-cup conventions. Missing authority must remain BLOCKED; no post-hoc orientation or convention fitting is allowed.
