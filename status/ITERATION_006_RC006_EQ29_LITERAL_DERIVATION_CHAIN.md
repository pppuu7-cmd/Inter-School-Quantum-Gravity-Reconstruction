# Iteration 006 / RC006 — Eq.(29) literal source-derivation chain

## Preregistration

Frozen before implementation/production. Precondition: run `34721521848` is terminal `EQ29_ARC_AWARE_NO_PROPER_CROSSING` on the immutable Eq.(29) block at 80/120 dps. This removes the need to infer an R/R^-1 crossing placement from the final Eq.(29) drawing; it does not remove the explicit q-phase already present in the literal formula and does not reconstruct the amplitude.

Pinned source: arXiv `1609.02429v2`, source-bundle SHA256 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

Immutable Eq.(29) align block SHA256: `4f505657a580216d176c1c63ec92f5614dc73e8113294722a854d5a350b67083`.

## Question

Is there a machine-qualified source chain from the literal Eq.(29) tensor factor to the Appendix-F derivation rule and the Appendix-B graphical identities, sufficient to define a **new numerical reconstruction gate prospectively** without fitting contraction order or inventing an R placement?

## Independent frozen lanes (`fail-fast:false`)

### `eq29_literal`

Extract the immutable Eq.(29) block and require the literal source to contain, in the same active align environment:

- outer sign factor beginning with `(-1)`;
- normalization factors involving `d_{l_1}`, `d_{l_2}` and `d_l`;
- a literal sum over the internal spin `j`;
- a literal factor `d_j`;
- a literal q-power whose exponent contains all three Casimir-like terms `j^+_1(j^+_1+1)`, `j^-_2(j^-_2+1)`, and `j(j+1)` with the source signs/order preserved as raw text;
- exactly one active TikZ diagram in the bracket and the previously validated source label set.

No algebraic simplification is allowed in this lane. Record hashes of the block and of the q-power substring.

### `appendix_f_chain`

Within the unique active `Appendix F: Derivation of EPRL amplitude`, require the exact source-semantic statements that the 3-valent EPRL diagrams are obtained by applying identities `(B15)` and that the final expression also requires the R-matrix identity. Require exactly one displayed derivation associated with `(F1)` between that appendix heading and the references. Record the Appendix-F segment SHA256 and the exact refs encountered (`B15`, `F1`, R-matrix text). This is a source dependency qualification, not a claim that R is a crossing in the final Eq.(29) drawing.

### `appendix_b_identities`

In Appendix B, independently require active source objects for `(B13)`, `(B15)`, `(B16)` and verify from source text that B13 defines the q-6j graphical coefficient while B15 is explicitly described as the splitting used for the 3-valent algorithm and B16 is the resulting reduction of B14 into two `[6j]` factors. No numerical evaluation is performed; the already terminal `RC006_B13_SOURCE_MAPPING_PASS` remains a separate convention authority.

## Frozen aggregate

PASS only if all three lanes are valid and all required literal/source-dependency predicates are true.

Classifications:

- `EQ29_LITERAL_DERIVATION_CHAIN_SOURCE_QUALIFIED`: the complete source chain is machine-qualified. This authorizes only a separately preregistered numerical reconstruction gate that must keep the literal Eq.(29) prefactor/q-phase frozen and use only source-qualified B13/B15/B16 reductions or an independently validated direct contraction.
- `EQ29_LITERAL_SOURCE_FACTOR_INCOMPLETE`: Eq.(29) literal factor predicates fail. Scientific/source BLOCKED; do not guess missing factors.
- `EQ29_APPENDIX_F_CHAIN_INCOMPLETE`: Appendix-F B15/R dependency predicates fail. BLOCKED; do not infer the derivation.
- `EQ29_APPENDIX_B_IDENTITY_CHAIN_INCOMPLETE`: B13/B15/B16 source predicates fail. BLOCKED.
- `INVALID_SOURCE_OR_IMPLEMENTATION`: source hash/unique-anchor/parser validity fails; infrastructure/implementation only.

## Claim locks

This gate cannot authorize numerical Eq.(29) amplitudes: `eq29_amplitude_authorized=false`. `bridge_credit=false`. It cannot revise the earlier relation-aware serialization scientific FAIL, cannot fit a contraction order, cannot add an R matrix to the final planar graph, and cannot support `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, `ALL_KNOWN_SCHOOLS_FAIL`, or candidate theory construction.
