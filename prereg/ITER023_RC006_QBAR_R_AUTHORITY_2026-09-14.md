# ITER023 preregistration — RC006 qbar index-order + R authority split

Date: 2026-09-14

## Basis

ITER022 terminal: `RC006_QBAR_DUAL_TRANSLATION_BLOCKED`.

Two independent authority questions remain. They are frozen separately so neither can be repaired by tuning the other.

## Lane A — qbar source equation inventory

Recover every source equation/context in arXiv:1609.02429v2 containing qbar/q^{-1}, cup/cap and CG symbols. Emit exact snippets/hashes and enumerate all graph-to-index ordering obligations. PASS only if the source gives enough explicit information to identify a unique index ordering without fitting.

## Lane B — qbar orientation adversary

Using only source-declared cup/cap directions and the validated q-CG embeddings, enumerate the finite set of plausible leg-order/orientation maps for the frozen channels `(1,1)->0,2`, `(1,2)->1,3`, `(2,2)->0,2,4` at k=6,10,12. No data-fit selection. PASS only if exactly one map satisfies all source graphical identities and round-trip residual `<2e-9`; 0 or >1 surviving maps => BLOCKED.

## Lane C — R exact source authority

Recover every exact source context matching R-matrix/R matrix/braiding in Appendix F and neighboring derivation text. PASS only if an explicit target-convention component formula is present or the source explicitly proves cancellation before the intended Eq.(27) contraction. A bare mention/reference is BLOCKED.

## Lane D — provenance/null audit

Verify source digest equals `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`; verify cap/cup identity remains `<1e-12`; reject ordinary Hermitian qbar substitution and missing-orientation manifests. PASS requires all provenance controls and at least 2/2 wrong manifests rejected.

## Aggregate

- `RC006_QBAR_R_AUTHORITY_COMPLETE`
- `RC006_QBAR_INDEX_ORDER_BLOCKED`
- `RC006_R_AUTHORITY_BLOCKED`
- `RC006_QBAR_R_INFRASTRUCTURE_PARTIAL`

Only complete PASS may authorize a new bounded Eq.(27) numerical contraction preregistration.

Locks: no bridge credit, no candidate theory, no new physics, no Eq29, no alpha selection, no Iter012 retry.