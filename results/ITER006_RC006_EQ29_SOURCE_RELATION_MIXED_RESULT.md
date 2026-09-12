# ITERATION 006 — RC006 Eq.(29) source-relation context audit

Date: 2026-09-12

## Frozen gate and provenance

Prospective extraction script commit: `7df0e50b7b3574e8bafe9ccf4ff5f182236059f2`  
Workflow/head: `bdcda53f683f9d684de90d29e2b956b57bfd75a2`  
Authoritative run: `34699432919`  
Aggregate job: `103568483952`  
Aggregate artifact: `10300395360`  
Aggregate digest: `sha256:7ddf84f729011d1f8b91bd13134c2884035fba85813526625e2b79f43f06df79`

The eight source roles were frozen before viewing the result: `eq29_context`, `rmatrix`, `crossing`, `representations`, `internal_l`, `recoupling`, `appendix_f`, `simplicity`. For a one-pattern role at least one exact source hit was required. For roles with multiple preregistered lexical forms at least two distinct forms were required. The object tested was source-text relation-context availability only; a PASS could not authorize a unique graph contraction or a numerical Eq.(29) amplitude.

## Raw terminal classification

The aggregate job was green by design because it preserves lane classifications. It is **not** a scientific PASS.

Raw aggregate:

- lanes: `8`;
- PASS: `6`;
- FAIL: `2`;
- `all_pass = false`.

Passing roles: `eq29_context`, `internal_l`, `recoupling`, `representations`, `rmatrix`, `simplicity`.

Failing roles:

1. `appendix_f` — job `103568457253`, artifact `10299921244`, digest `sha256:9754083e1ef69e7e6594bb2b88fef9c86e6d47cf2a8f4f0fc68ae9378b3d1822`. The official source archive downloaded and parsed normally. The frozen lexical forms produced `match_count=0`, `distinct_patterns_found=0`, versus required `2`. Classification: `SCIENTIFIC/SOURCE-QUALIFICATION FAIL`, not infrastructure/numerical failure.
2. `crossing` — job `103568457268`, artifact `10300305561`, digest `sha256:715daa593ce3dd4f2445d909ed0a3c467f5c3be25e1ce9f734010c9cc07bf8fe`. The source produced three matches, but only one of the three preregistered lexical forms (`distinct_patterns_found=1` versus required `2`). Classification: `SCIENTIFIC/SOURCE-QUALIFICATION FAIL`, not infrastructure/numerical failure.

## Scientific interpretation

Classification:

`MIXED_SOURCE_RELATION_QUALIFICATION_6_OF_8 / EQ29_CONTRACTION_MAPPING_REMAINS_BLOCKED`.

The result strengthens source authority for six semantic roles but fails the prospectively frozen textual qualification for the Appendix-F anchor and for robust multi-form crossing language. The failed thresholds are preserved. They will not be weakened and the same lexical audit will not be rerun merely with easier patterns.

The failures do **not** imply that the paper lacks a relevant recoupling derivation or crossing structure. They show only that the exact preregistered textual-anchor object is insufficient for a contraction-ready machine mapping. A distinct source-structure object — TeX include/section/label/reference topology — may be audited prospectively without changing this result.

## Consequences

- `RC006_EQ29_ORIENTED_BRAIDED_GRAPH_MAPPING_GATE`: **OPEN/BLOCKED**.
- `RC006_EQ29_MINIMAL_K12_AMPLITUDE_GATE`: remains **BLOCKED**.
- Appendix-C SVD and held-out non-retuned selector transport remain blocked downstream.
- No geometry-nearest fallback is authorized.
- No numerical Eq.(29) amplitude, refinement bridge, continuum result, `BRIDGE_DERIVED`, or candidate theory follows.
