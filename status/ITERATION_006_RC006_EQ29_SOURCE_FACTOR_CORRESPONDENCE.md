# ITERATION_006 RC006 Eq.(29) source-factor correspondence — preregistration

Date: 2026-09-12  
Status: PREREGISTERED BEFORE IMPLEMENTATION

## Frozen prerequisites

- Eq.(29) immutable source dependencies: run `34719456729`, terminal `EQ29_IMMUTABLE_SOURCE_DEPENDENCIES_COMPLETE_R_NOT_APPLICABLE`.
- Eq.(29) exact block SHA256: `4f505657a580216d176c1c63ec92f5614dc73e8113294722a854d5a350b67083`.
- Referenced `eq:eprl-3-valent` source environment recovered terminal `EQ29_LITERAL_SOURCE_RELATION_EXTRACTED` in run `34719782628`, exact environment SHA256 `88d2f7be9489980a763dd66b5c4900473c79900ccf72790095ae1675e9733b2d`.

## Scientific question

The referenced source environment contains a source-defined EPRL three-valent object and Eq.(29) directly points to it. Determine mechanically, without relabelling or graph isomorphism fitting, whether the complete Eq.(29) bracket is literally one and only one of the bracket factors appearing in `eq:eprl-3-valent`, and whether the non-bracket prefactor differs only by the source normalization factor `d_l` versus `\\sqrt{d_l}`.

## Frozen parser

For each immutable TeX environment:

1. strip TeX whitespace only (`space`, tab, CR, LF) for lexical comparison; do not reorder, rename or algebraically simplify tokens;
2. identify top-level bracket factors by exact source delimiters `\\left[` ... `\\right]`; nested bracket delimiters, if encountered, must be balanced and retained;
3. require exactly two top-level bracket factors in `eq:eprl-3-valent` and exactly one in Eq.(29); otherwise fail closed;
4. compute SHA256 of each whitespace-canonical bracket factor;
5. compare Eq.(29)'s canonical bracket hash against **both** referenced factor hashes, with no preferred factor index;
6. extract from each equation the RHS prefix beginning immediately after the first `=` and ending immediately before the first top-level `\\times` introducing a bracket factor;
7. canonicalize whitespace only. For the reference prefix replace exactly one literal normalization token `d_l` by sentinel `<DLNORM>`; for Eq.(29) replace exactly one literal `\\sqrt{d_l}` by the same sentinel. No other replacements are allowed. The resulting prefixes must then match byte-for-byte;
8. require the LHS through the first `=` to match byte-for-byte after whitespace canonicalization.

## Independent lanes

### TOKEN_FACTOR

Character/token parser implementing the rules above directly on the two immutable source environments.

### GRAPH_LABEL_VERIFY

Independently extract TikZ `node {...}` labels and the q-exponent substring from Eq.(29)'s sole bracket and from each referenced bracket. It must determine which, if any, referenced factor has an identical **ordered node-label sequence** and identical whitespace-canonical q-exponent substring. It does not use TOKEN_FACTOR hashes.

## Frozen classifications

- `EQ29_UNIQUE_SOURCE_FACTOR_CORRESPONDENCE`: TOKEN_FACTOR finds exactly one bracket-hash match, the LHS matches, normalized prefixes match under only the frozen `d_l ↔ sqrt(d_l)` sentinel substitution, and GRAPH_LABEL_VERIFY independently identifies the same unique factor by ordered labels + q-exponent.
- `EQ29_SOURCE_FACTOR_CORRESPONDENCE_AMBIGUOUS`: both factors match, lanes select different factors, or one structural discriminator is non-unique.
- `EQ29_SOURCE_FACTOR_CORRESPONDENCE_FAIL`: no factor matches or the prefactor/LHS relation fails under the frozen lexical rule.
- `INVALID_SOURCE_OR_IMPLEMENTATION`: pinned block/hash acquisition or parsing fails.

## Authorization

A UNIQUE PASS establishes a literal source factor relation only. It authorizes preregistration of a graph→q-symbol reduction/evaluator for that uniquely selected source factor. It does not itself authorize numerical Eq.(29) amplitude claims.

## Claim locks

Bridge credit remains zero. Candidate theory remains `UNFORMED`; no `BRIDGE_DERIVED`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND` claim is authorized.
