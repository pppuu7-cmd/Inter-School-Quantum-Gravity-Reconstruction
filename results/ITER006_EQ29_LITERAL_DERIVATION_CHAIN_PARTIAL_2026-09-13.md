# ITER006 — Eq.(29) literal source-derivation chain terminal result

Date: 2026-09-13

## Authoritative production

- Gate: `ITER006_RC006_EQ29_LITERAL_DERIVATION_CHAIN`
- Prereg commit: `98197e8fa44224fc8af547edbc47a2e65f49ba56`
- Implementation/head commit: `a210a47edbc8f4510b6edd4e18e3f1dee377ed47`
- Run: `34721872311`
- `appendix_b_identities` job: `103629143761`
- `eq29_literal` job: `103629143876`
- `appendix_f_chain` job: `103629143895`
- aggregate job: `103629162115`
- `appendix_f_chain` artifact: `10306990275`, digest `sha256:44bf81b80361c067520aee533eee6338ad3ebc04357366a0143f8c7d2cdb44be`
- `appendix_b_identities` artifact: `10306532225`, digest `sha256:e5be8cc593ebff0b6118de0f01b97decd07b75fc4e75828dbc2d3d940d81db7e`
- `eq29_literal` artifact: `10306447226`, digest `sha256:8b4e8e78153a719a4e0c65b557f92a1b5aacf0200a08017f96592ceaebe85cb5`
- aggregate artifact: `10306412313`, digest `sha256:4aff93ac51382f5cfb9f010a3f6a111f0a75e2ad9f8151bde05bca8749ddd56e`

All jobs were green. Scientific classification follows the frozen aggregate and raw source artifacts, not CI color.

## Frozen lane classifications

- `eq29_literal`: **`EQ29_LITERAL_FACTOR_QUALIFIED`**.
- `appendix_b_identities`: **`EQ29_APPENDIX_B_IDENTITY_CHAIN_QUALIFIED`**.
- `appendix_f_chain`: **`EQ29_APPENDIX_F_CHAIN_INCOMPLETE`**.

Aggregate: **`EQ29_APPENDIX_F_CHAIN_INCOMPLETE`**.

This is a valid source-level BLOCKED result, not an infrastructure/numerical failure and not a scientific FAIL of the physical amplitude.

## Raw Appendix-F evidence

The frozen Appendix-F extractor found the unique appendix and the source sentence

`Essentially one applies the identities \eqref{eq:identity1}. We will demonstrate this only for one diagram in \eqref{eq:EPRL-formula}, as it follows for the other diagram analogously:`

with both exact references resolved in the source graph. A displayed derivation is present. The extracted segment SHA256 is `6770c20294ee2ff50e4ef3c4724fc9857e69aaff7667524bc4d637c9b03995df`.

However the preregistered predicate `r_matrix_statement` is **false** inside that Appendix-F segment. Therefore the frozen gate cannot return `EQ29_LITERAL_DERIVATION_CHAIN_SOURCE_QUALIFIED`.

No post-result weakening from “R statement inside Appendix F” to “R statement somewhere in the paper” is permitted within this gate.

## Scientific interpretation

Two important pieces are source-qualified without ambiguity:

1. the literal final Eq.(29) prefactor/sum/q-phase object;
2. the Appendix-B B13/B15/B16 graphical identity chain.

The missing item is narrower: a machine-qualified **cross-section dependency path** connecting the derivation chain to the source-global R convention. This is especially relevant because the independently terminal arc-aware gate `34721521848` found zero proper crossings in the final immutable Eq.(29) drawing, so any R contribution must not be invented as an additional final-block graphical crossing.

The current result does not authorize a numerical Eq.(29) amplitude reconstruction and does not overturn the earlier relation-aware serialization scientific FAIL.

## Locks

- `eq29_amplitude_authorized=false`.
- `bridge_credit=false`.
- `SCIENTIFIC_FAIL_RELATION_AWARE_CONTRACTION_SERIALIZATION_UNSTABLE` remains preserved.
- no fitted contraction order or R placement;
- no `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, `ALL_KNOWN_SCHOOLS_FAIL`, or candidate theory construction.

## Next admissible object

Only a separately preregistered **cross-section source dependency localization diagnostic** is admissible now. It may map exact labels/refs and source-global R/R^-1 definitions, but it may not change this terminal aggregate from BLOCKED to PASS and may not authorize amplitude reconstruction by itself.
