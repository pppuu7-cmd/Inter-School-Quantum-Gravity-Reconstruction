# ITER006 RC006 Lambda formula authority chain — terminal result

Date: 2026-09-13

## Frozen gate
Preregistration commit: `1deee2a885fddf5a2c92d7d4aee6ee0e2d27cc7d`.
Implementation/workflow head: `1fb60e63a48f13f3faab873dc63ff5335e5d2182`.
Run: `34746758765`.

Jobs:
- Buffenoir–Roche tensor-product lane: `103695987260`
- Buffenoir–Roche harmonic-analysis lane: `103695987359`
- EPRL proceedings lane: `103695987368`
- full EPRL paper lane: `103695987440`
- aggregate: `103696006904`

Artifacts:
- BR harmonic `10314770743`, digest `sha256:eb3dcaa9bb75573711c1cf2c5451b2a1cc1101a4061f4f9f548aa7edc22ae8c2`
- BR tensor `10313759064`, digest `sha256:ee196d2cb31ecdc9e5e690e0f21907042707961e2db1631bbde8ccaee39f9671`
- EPRL proceedings `10313808778`, digest `sha256:53c8dca3841a59cde02f8c4b0473212fa2ea04566f4899a9bf10aabe3c675195`
- EPRL full `10313714364`, digest `sha256:86729ef1340906e69c823054d529a479e287b1bef4822b01e39a4e3ce3fd81e1`
- aggregate `10314183009`, digest `sha256:41fbd115758784856ef19f121d157846e20c7cde1ab5e2051c1681c942bcce03`

Downloaded immutable-source SHA256 values recorded by the raw lanes:
- `1112.2511v1`: `d2dfda1a79b9978422b5a57387f9bbf1ebd4828327c656b59ed74c0acc98302c`
- `1012.4784v3`: `6baa297f99e42b4232c6aee395260f28d22d3dab81ed2b83cb641229da0ff43b`
- `math/9910147v1`: `316ab7737a6e201c9c5d988326077358b562e6f5d47cfffbf1d2935cdd9389bc`
- `q-alg/9710022v2`: `7acfbb6e3ae77d8fab56f00f4c0ae78287b706f4d99d5db77afa1b3310fecd98`

## Raw-source findings
Both EPRL lanes independently identify the same principal-series coefficient `Lambda^{JM}_{NL}(alpha)` in the representation action and explicitly state that it is defined by analytic continuations of `U_q(su(2))` 6j symbols while referring elsewhere for the lengthy explicit expression. Thus the EPRL papers themselves are not a sufficient numerical implementation authority.

The `math/9910147v1` Buffenoir–Roche lane contains explicit Lambda macros/notation, principal-unitary representation context, analytic-continuation/6j content, q-Racah/Askey–Wilson content, normalization signals and domain signals. Its source SHA is fixed above. The machine audit also raised an explicit-definition signal.

However, the current artifact does not yet expose a uniquely identified exact equation/normalization map that can be translated into `Lambda^{JM}_{NL}(alpha)` with no free convention choices. The `q-alg/9710022v2` lane was retrievable but its current text-extraction representation exposed no usable principal/Lambda anchors, so it provides no independent formula confirmation in this gate.

## Scientific classification
`QEPRL_LAMBDA_AUTHORITY_CHAIN_PARTIAL`

Reason: the source-authority chain is established, but the retrieved evidence in this gate does not yet satisfy the frozen requirement for an unambiguous executable coefficient definition plus normalization/domain map.

This is not a scientific failure of q-EPRL. It is a source/executability blocker for the planned low-spin numerical Lambda implementation.

## Scope
No Eq.(29) authorization, amplitude/refinement bridge credit, `BRIDGE_DERIVED`, candidate theory, `NEW_PHYSICS_FOUND`, or rewrite of the historical braid-projection FAIL follows.

## Next admissible gate
Prospectively freeze an exact-equation extraction/reconstruction audit on `math/9910147v1`, with independent parsers for Lambda macro definitions, equality/definition contexts, analytic-continuation/6j contexts and normalization/domain conventions. The gate must output exact source anchors sufficient to construct the coefficient or explicitly classify the low-spin implementation as source-blocked. Do not invent a surrogate formula.
