# Preregistration — ITER006 RC006 q-binomial explicit delegation-target audit

Frozen prospectively on 2026-09-13 before implementation/production evidence.

## Scientific purpose
The completed primary-source authority-chain gate found that `math/9910147v1` explicitly imports prior Buffenoir–Roche material, but the audited prior source `q-alg/9710022` contains no explicit q-binomial definition or explicit compatible symmetric q-number normalization satisfying the frozen rule. Source-faithful RC006 promotion is therefore BLOCKED.

This +0-credit audit asks one narrower provenance question: **does the prior primary source explicitly delegate the q-binomial / bracket / factorial convention to a specific cited source or named convention?** It is not a broader literature search and may not choose a convention based on numerical agreement.

## Frozen source inputs
- current source: arXiv `math/9910147v1`, immutable SHA256 `316ab7737a6e201c9c5d988326077358b562e6f5d47cfffbf1d2935cdd9389bc`;
- prior source: arXiv `q-alg/9710022`; production must record and require the same SHA256 already validated by the previous gate: `7acfbb6e3ae77d8fab56f00f4c0ae78287b706f4d99d5db77afa1b3310fecd98`.

## Frozen independent lanes
1. `qbinomial-context`: exhaustively enumerate every q-binomial/binomial notation occurrence in the prior source with ±12 source lines and extract citation keys/named references in the same local paragraph or displayed-definition block.
2. `notation-preamble`: exhaustively inspect notation/convention/definition preambles for explicit language such as `we use the conventions of`, `as defined in`, `following`, `notation of`, or equivalent, tied to bracket q-numbers, factorials or q-binomials; extract cited keys/names.
3. `bibliography-map`: map every candidate citation key from lanes 1–2 to its exact bibliography entry in the prior source; a key with no resolvable bibliography entry is invalid.

## Frozen classifier
- `EXPLICIT_DELEGATION_TARGET_IDENTIFIED`: at least one candidate has BOTH (a) explicit delegation language tied to the relevant notation/convention and (b) an exact resolvable bibliography entry. Mere citation proximity, general historical attribution, or bibliography presence is insufficient.
- `NO_EXPLICIT_DELEGATION_TARGET_IN_AUDITED_SOURCE`: source parsing succeeds but no candidate satisfies both conditions.
- `INFRASTRUCTURE_DELEGATION_AUDIT_FAIL`: immutable source fetch/hash/parser failure prevents exhaustive audit.

## Interpretation lock
This audit carries zero bridge credit. Even `EXPLICIT_DELEGATION_TARGET_IDENTIFIED` does not authorize a convention; it only authorizes a subsequent prospectively preregistered fetch-and-definition audit of the exact identified primary source(s). A null result leaves RC006 source-faithful promotion BLOCKED and closes this provenance path unless a different explicit source chain is independently discovered.

No numerical panel output may influence candidate extraction, convention choice, or classification.
