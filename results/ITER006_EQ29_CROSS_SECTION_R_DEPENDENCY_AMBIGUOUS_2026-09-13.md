# ITER006 — Eq.(29) cross-section R-dependency localization terminal result

Date: 2026-09-13

## Authority
- Prereg commit: `2669d1d4a7a096e7e6475bc29b7e6443b1867a0b`
- Implementation/head: `728d0493fd5669de0d8d13667aec2ae82eaaff44`
- Run: `34722014367`
- `r_global` job: `103629526240`, artifact `10306202978`, digest `sha256:4b752070a5f9e0e048e5002a4b7cb04187d6691bd7104486ba05c519277b9cac`
- `appendix_f_refs` job: `103629526284`, artifact `10306034594`, digest `sha256:5fa23393db7ab3be00010eadaac9200cb57d14c9f08cf9ecb106005501e403b6`
- `exact_ref_graph` job: `103629526295`, artifact `10306820893`, digest `sha256:d89dd08e015bded5e1e8f5a4c1decb30fba1b82edcb69631cb8f7c77f7ec50b0`
- aggregate job: `103629543164`, artifact `10306119189`, digest `sha256:8d405e40922de55cf8886ddd824fbc8bac5fb81f5cc592978842d4f467122234`

## Frozen result
Aggregate classification: **`EQ29_R_DEPENDENCY_AMBIGUOUS_MULTIPLE_PATHS`**.

All lanes are valid and green, but this gate was preregistered as diagnostic-only (`scientific_credit=0`). The exact Appendix-F refs are `eq:EPRL-formula` and `eq:identity1`; source-global R neighborhoods are localized. The exact-ref graph nevertheless yields multiple reachable Appendix-F→R-neighborhood label paths rather than a unique dependency path. Examples include direct/component paths through `eq:EPRL-formula`, `app:EPRL-diagram`, and longer graph chains through `app:graph` / recoupling labels.

Therefore no path may be selected post hoc as “the” R derivation route. The terminal `EQ29_APPENDIX_F_CHAIN_INCOMPLETE` result from run `34721872311` remains unchanged.

## Locks
- `scientific_credit=0`
- `eq29_amplitude_authorized=false`
- `bridge_credit=false`
- no fitted path selector, contraction order, or final-block R placement
- relation-aware serialization scientific FAIL remains preserved
- no bridge/new-physics/new-theory/candidate-theory claim

## Consequence
The Eq.(29) branch is source-localized but presently BLOCKED at unique cross-section derivation composition. Compute is therefore shifted to the independent, already-authorized multivertex Lorentzian refinement stream rather than repeating lexical/reference scans.
