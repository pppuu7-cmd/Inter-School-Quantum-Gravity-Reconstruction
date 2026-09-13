# ITER024 prereg — RC006 cited authority chain

Frozen before implementation/result inspection.

Goal: resolve cited-source authority behind `q-spinnet`, `biedenharn`, and `wojtek` for the two remaining Iter023 blockers: explicit qbar graph-to-index ordering and executable R/R^-1 convention.

Independent lanes:
1. `bib-resolve`: recover exact bibliographic targets for the three citation keys from the primary EPRL/TNR source package.
2. `qbar-authority`: inspect resolved open source(s) for explicit index-level qbar duality/cup-cap ordering compatible with the already frozen q-CG normalization.
3. `r-authority`: inspect resolved open source(s) for explicit executable R/R^-1 formula/convention, not lexical mention alone.
4. `provenance-null`: verify source hashes/citation targets and reject deliberately incomplete lexical-only evidence.

Frozen PASS rule: `RC006_CITED_AUTHORITY_CHAIN_COMPLETE` only if all four lanes produce source-locatable evidence sufficient to determine both qbar index ordering and R convention without fitted phases/orientations. If bibliography resolves but either formula remains absent/ambiguous: `RC006_CITED_AUTHORITY_CHAIN_BLOCKED`. Transport/source-download failures are `INFRASTRUCTURE_FAIL`, not scientific BLOCKED.

Locks: no Eq.(27) numerical contraction, no Iter012 retry, no Eq.(29)/Lambda, no preferred alpha, no bridge credit, no candidate theory construction. Do not infer new physics from authority closure or failure.
