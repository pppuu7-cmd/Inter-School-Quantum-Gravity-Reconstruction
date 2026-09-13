# ITER024 terminal — RC006 cited authority chain

Date: 2026-09-14

## Terminal classification

`INVALID_IMPLEMENTATION`

This is **not** a scientific negative and **not** source-authority closure.

## Authoritative execution

- prereg: `prereg/ITER024_RC006_CITED_AUTHORITY_CHAIN_2026-09-14.md`
- prereg commit: `6d007bf342997425d5eee88d0f354062e9f8bb95`
- implementation: `code/iter024/cited_authority_chain.py`
- implementation commit: `c223a73f0c66c950da98f478cfe4b7d2d3be8ca0`
- production/workflow head: `2511ad18bf53d7159b935df306419dad709a210c`
- run: `34788335930` — GitHub conclusion `success`
- artifacts:
  - aggregate `10327143320`, digest `sha256:aa84c692363d6d627686be23f67580e028208822de2f320ce836f26c2a69784a`
  - bib-resolve `10327238202`, digest `sha256:d78ad4c30700f7eec122a4124e7c657ddbd833499b71534f11435cae4710d24b`
  - qbar-authority `10326889371`, digest `sha256:37b396dcd0af3fce3f8202712c20a125c328cd7e2addbf0633a07cc467984693`
  - r-authority `10326743834`, digest `sha256:92cbfc7fc60f43de2ef3e37d867f1b16c57e5629ec3d996084be55bc5822c7b3`
  - provenance-null `10327263162`, digest `sha256:9c968fb31af4c60412636b2d11398af7cf1fc977d21ed3c58bea53e45c65bd35`

The frozen aggregate emitted `RC006_CITED_AUTHORITY_CHAIN_COMPLETE`, with all four machine lanes marked pass. Green CI and that aggregate label are retained as raw execution facts only.

## Why the scientific PASS is invalid

The preregistered qbar lane required inspection of the **resolved open cited source(s)** for an explicit index-level qbar duality/cup-cap ordering compatible with the frozen q-CG normalization. The implementation does not do that: `qbar()` calls `source_text()`, and `source_text()` downloads only `https://export.arxiv.org/e-print/1609.02429v2`. The resolved `q-spinnet` target (`arXiv:1312.0905`) is extracted from the bibliography but is never downloaded or inspected.

The qbar verdict is therefore based on a regex over the 1609.02429v2 source package and stores only a boolean `explicit_index_equality_in_primary_package`; it does not preserve the matched formula, source file, line/equation/page/appendix locator, index order, or convention translation. This is insufficient for the frozen PASS rule.

The preregistered R lane required an explicit executable R/R^-1 formula/convention from the resolved authority chain. The implementation again inspects only the 1609.02429v2 package. It checks that bibliography entries `biedenharn` and `wojtek` exist and that a regex resembling `\mathcal{R}=...q^` occurs somewhere in the target source. It does **not** open Biedenharn-Lohe or `arXiv:1311.1798`, and it stores no exact R formula, representation ordering, crossing/orientation convention, R versus R^-1 choice, or source locator.

The aggregate then promotes the four booleans directly to `RC006_CITED_AUTHORITY_CHAIN_COMPLETE`. Thus the implementation is weaker than the prospectively frozen acceptance criterion.

## Scientific consequence

ITER024 cannot authorize bounded Eq.(27) component contraction. It also cannot be reinterpreted as evidence that the needed authority is absent. The previous ITER023 blockers remain scientifically unresolved:

1. exact qbar graph-to-index ordering;
2. exact executable R/R^-1 convention.

No fitted phase, sign, index permutation, orientation, or crossing choice is authorized.

## Exact next admissible gate

Prospectively preregister a corrected source-authority audit that actually downloads and hashes the exact cited primary-source versions, preserves source-file/line context for every candidate formula, and asks whether the cited chain uniquely determines both missing conventions. If either remains ambiguous, terminalize `BLOCKED_SOURCE_AUTHORITY`. Only an unambiguous source-locatable closure may authorize a separately preregistered bounded Eq.(27) contraction.

## Claim locks

Unchanged: candidate theory remains `UNFORMED`; no bridge credit; no Iter012 retry; no Eq.(29)/Lambda; no preferred alpha; no new physics; no all-schools or universal-bridge claim.
