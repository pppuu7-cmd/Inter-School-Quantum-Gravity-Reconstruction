# ITERATION_006 Eq.(29) literal source relation — boundary implementation diagnosis

Date: 2026-09-12

Run `34719666891` returned aggregate `EQ29_LITERAL_SOURCE_RELATION_AMBIGUOUS` solely because the two independent lanes emitted different SHA256 values for the enclosing source environment. The scientific/source-identity predicates themselves agreed:

- both lanes found the source label `eq:eprl-3-valent` uniquely;
- both independently identified the enclosing environment as `align`;
- both returned their lane-level classification `EQ29_LITERAL_SOURCE_RELATION_EXTRACTED`;
- both independently found exactly one direct `\\eqref{eq:eprl-3-valent}` in the active Eq.(29) EPRL subsection.

The mismatch is traceable to implementation boundaries:

- `ENVIRONMENT_EXTRACTOR` hashes the exact character interval beginning at `\\begin{align}` and ending at the end of `\\end{align}`; it reports 2138 characters and SHA256 `88d2f7be9489980a763dd66b5c4900473c79900ccf72790095ae1675e9733b2d`;
- `LINE_STRUCTURAL_VERIFY` locates the enclosing environment by line nesting, but then hashes **entire source lines 1000–1053**, contrary to the preregistered requirement to compare the smallest complete enclosing environment. Its SHA256 is `894c83775801522eb9a55b578f5f11f382949c157d7b643c0af169727559e4cf`.

Therefore the aggregate ambiguity is an implementation/canonical-boundary mismatch, not evidence for two competing source environments. The original aggregate result remains historically recorded; it is not overwritten.

An infrastructure-only recovery is admissible: preserve the independent linewise discovery of start/end lines, but canonicalize the recovered block from the exact `\\begin{align}` token on the independently discovered start line through the exact `\\end{align}` token on the independently discovered end line. No label, environment type, source reference, threshold or scientific predicate may change. Recovery may promote only if this independently canonicalized SHA equals the already frozen exact-character SHA `88d2f7be9489980a763dd66b5c4900473c79900ccf72790095ae1675e9733b2d` and the direct Eq.(29) reference count remains one.

No numerical Eq.(29) amplitude is authorized by this diagnosis.
