# ITERATION_006 Eq.(29) source-factor correspondence — LHS parser implementation diagnosis

Date: 2026-09-12

Preregistered run `34719930174` completed validly but aggregate classified `EQ29_SOURCE_FACTOR_CORRESPONDENCE_FAIL`. The only failed predicate was `lhs_match=false`.

All substantive source-factor predicates agreed:

- lexical bracket hashing selected exactly reference factor index `1`;
- independent ordered TikZ-node-label + q-exponent verification independently selected factor index `1`;
- the frozen prefactor comparison passes after **only** the preregistered normalization sentinel replacement `d_l ↔ \\sqrt{d_l}`;
- no competing factor match exists.

The LHS mismatch is an implementation error in the token-factor lane. Its `lhs(x)` function hashes `x[:first '=']`, so for the referenced environment it includes source-environment metadata `\\begin{align} \\label{eq:eprl-3-valent}` before the mathematical left-hand side. Eq.(29)'s align block has no corresponding source label, making the metadata bytes unequal even though the actual mathematical LHS expression is the same object. The preregistration explicitly calls this field the **LHS**; environment delimiters and `\\label{...}` are source metadata, not part of the mathematical left-hand side.

The historical FAIL remains recorded and is not overwritten. An infrastructure-only recovery may re-extract the mathematical LHS by removing only the opening allowed environment token and any immediately following `\\label{...}` metadata before taking bytes through the first `=`. It may not rename/reorder/simplify mathematical tokens. Promotion is allowed only if:

1. corrected mathematical LHS values match byte-for-byte after whitespace canonicalization;
2. original frozen token-factor match remains uniquely `[1]`;
3. independent graph-label/q-exponent match remains uniquely `[1]`;
4. the original frozen normalized-prefix predicate remains true.

No numerical Eq.(29) amplitude is authorized by this diagnosis.
