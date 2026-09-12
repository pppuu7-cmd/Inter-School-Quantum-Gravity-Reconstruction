# Iter006 — DED/DLD6 source-algebraic zero-face collapse prerequisite

Status: PROSPECTIVELY FROZEN BEFORE AUTHORITATIVE PRODUCTION
Date: 2026-09-13

## Scientific purpose

Test a genuinely new representation-independent source object for the blocked Lorentzian multi-vertex refinement route: the published TeX amplitude formulas for the DED and DLD6 two-vertex foams in arXiv:1801.03771v2. This gate does **not** use rasterized figures, EPS/SVG coordinates, fitted geometric tolerances, or a post-result selector.

The question is deliberately prerequisite-level: does the immutable source define a unique algebraic candidate for collapsing the DLD6 internal-face sector at `j_f=0` onto the DED contraction structure, with every extra DLD6 summation/factor either disappearing by an explicit source identity or reducing to an explicitly source-defined normalization? A PASS only qualifies a later numerical held-out amplitude identity test. It is not itself a refinement map, cylindrical consistency, convergence, or `BRIDGE_DERIVED`.

## Frozen source

- arXiv `1801.03771` current immutable source authority used by recovery, corresponding to v2 (19 Mar 2018);
- authoritative recovery-pinned source-tar SHA256: `9fc0b3396573b4f5ec457cafbc487aa5a1681fcb48561916d1398ed5bcc35303`;
- every production lane must independently verify this SHA256 exactly; no alternate version or mirror-normalized archive may be substituted.

A pre-production source-authority audit briefly proposed runtime cross-lane hash agreement because code search missed the existing recovery pin. Re-reading `recovery/CURRENT_FRONT.md` recovered the authoritative hash above before authoritative production. The earlier unpinned launch is therefore diagnostic/non-authoritative regardless of its eventual result. No scientific object, reduction rule, threshold, PASS/BLOCKED/FAIL criterion, or interpretation has changed.

## Frozen lanes

Four independent lanes, all source-only:

1. `ded_formula_ast`: locate the DED amplitude definition from TeX structure/context and emit a normalized symbolic-token/dependency AST.
2. `dld6_formula_ast`: locate the DLD6 amplitude definition and emit the analogous AST, including the internal-face variable and all sums/factors that depend on it.
3. `jf0_reduction`: apply **only** exact source/symbolic `j_f=0` substitutions and identities evident in the pinned source; no numerical fitting, coordinate matching, inferred routing, or manually chosen permutation.
4. `independent_context_control`: independently verify that the DED and DLD6 formula blocks, internal-face label, and source hash are stable under a second extraction strategy based on surrounding section/equation context rather than the first lane's token parser.

The aggregate runs only after all four lanes are terminal.

## Frozen PASS / BLOCKED / FAIL rules

`PASS_SOURCE_ALGEBRAIC_ZERO_FACE_COLLAPSE_OBJECT_QUALIFIED` iff all of the following hold:

- all lanes report the pinned SHA256 exactly;
- exactly one DED formula block and exactly one DLD6 formula block are identified by both extraction strategies;
- the DLD6 block contains one uniquely identifiable internal-face spin variable `j_f` (allowing TeX-equivalent spelling only when resolved mechanically from its local definition);
- after exact `j_f=0` reduction, there is a unique deterministic boundary-label-preserving algebraic correspondence to the DED contraction structure;
- every extra DLD6 sum/factor is either eliminated by an explicit exact source identity or retained as an explicitly source-defined normalization independent of any fitted/post-hoc selector;
- both extraction strategies agree on the reduced dependency graph and normalization inventory.

`BLOCKED_SOURCE_ALGEBRAIC_ZERO_FACE_COLLAPSE_AMBIGUOUS` if the source/formula blocks are valid but any required mapping, permutation, normalization, or internal-face dependency is non-unique or unresolved.

`SCIENTIFIC_FAIL_SOURCE_ALGEBRAIC_ZERO_FACE_COLLAPSE_MISMATCH` if a unique source-defined reduction/correspondence exists but the reduced DLD6 algebraic structure is not DED-isomorphic under the frozen boundary-label-preserving rules.

`INFRASTRUCTURE_OR_PARSE_FAIL` only for source retrieval/hash failure, invalid archive, parser crash, source-hash disagreement, or inability to form the preregistered source objects for technical reasons. Such failure has no scientific interpretation.

## Claim locks

Even a full PASS gives zero bridge credit by itself. It does not establish DED→DLD refinement, physical amplitude equality, cylindrical consistency, continuum convergence, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, or `BRIDGE_DERIVED`. Candidate theory remains 0/UNFORMED.

## Next step lock

Only a PASS may authorize a separately preregistered, non-retuned, held-out numerical DED-vs-DLD6 `j_f=0` amplitude comparison using the already pinned SL2C kernel. BLOCKED or SCIENTIFIC_FAIL forbids post-hoc permutation/normalization fitting and requires a genuinely new independent source/mathematical object before another collapse attempt.
