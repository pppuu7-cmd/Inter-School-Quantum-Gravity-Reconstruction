# ITER006 RC006 — q-binomial primary-source authority-chain audit

Date: 2026-09-13

Gate: `ITER006_RC006_LAMBDA_QBINOMIAL_PRIMARY_SOURCE_AUTHORITY_CHAIN`

## Prospective authority
- preregistration commit: `8f2bc5fa90899d7abf609a9961449e33ff4ee545`
- implementation / production head: `f18f3165f73d5505d11e1d4446f0901103a14587`
- production run: `34753224660`

The frozen gate required all three independent conditions: an explicit import/provenance statement in the current Buffenoir–Roche source, an explicit q-binomial convention definition in the prior same-author primary source, and explicit compatible q-number normalization. Numerical agreement was prohibited from supplying any missing convention.

## Raw terminal provenance
- `prior-explicit-definition` job `103713163081`; artifact `10316900185`; digest `sha256:9feee3392706618876a899ffbfa5981f98298403c981333e8f96f4d742073fea`
- `symbol-compatibility` job `103713163155`; artifact `10316687508`; digest `sha256:4f9d685726004724be4e9b872d44c6eb2fe247150c2f6b47bd643cc7ca17a864`
- `import-chain` job `103713163196`; artifact `10316143934`; digest `sha256:d6c090ce2a84342495f8a9a6cd53c6b03ba5816746173ad9634f7e3099ee5185`
- aggregate job `103713183243`; summary artifact `10315693822`; digest `sha256:2f66acf7a989dc70aad3d646ed3dbd1b0d6a59ccfb89f0cd80d457439a9a9ac8`

Current source: arXiv `math/9910147v1`, SHA256 `316ab7737a6e201c9c5d988326077358b562e6f5d47cfffbf1d2935cdd9389bc`.
Prior same-author source: arXiv `q-alg/9710022`, SHA256 `7acfbb6e3ae77d8fab56f00f4c0ae78287b706f4d99d5db77afa1b3310fecd98`.

## Terminal findings
- `import-chain`: lane PASS. Five import/provenance hits were found, including two strong import hits.
- `prior-explicit-definition`: lane FAIL. Two q-binomial occurrences were found but zero explicit definition candidates.
- `symbol-compatibility`: lane FAIL. Six bracket candidates and ten factorial hits were found, but zero explicit symmetric-bracket normalization candidates satisfying the frozen compatibility rule.

## Frozen scientific classification
`BLOCKED_SOURCE_AUTHORITY_CHAIN_NOT_ESTABLISHED`

This is a substantive source-authority BLOCKED result, not infrastructure/numerical failure. It is not eligible for a control repair or broader post-hoc convention search under this gate.

## Consequences
The previously completed 8/8 low-spin numerical panel retains its frozen scoped numerical qualification, but source-faithful promotion remains unauthorized. In particular:
- no source-faithful q-binomial convention is authorized by this chain;
- general `formlamb6j` reconstruction remains blocked;
- Eq.(29) amplitude authorization remains false;
- amplitude/refinement bridge credit remains zero for this RC006 branch;
- candidate-theory construction remains 0/UNFORMED.

The successful numerical panel must not be used to infer, fit, or choose the missing convention.

## Claim locks
No `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, `ALL_KNOWN_SCHOOLS_FAIL`, or candidate-theory promotion follows from this result.
