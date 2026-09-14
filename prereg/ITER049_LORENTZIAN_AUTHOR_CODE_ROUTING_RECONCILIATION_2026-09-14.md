# Preregistration — ITER049 Lorentzian author-code routing reconciliation

Date frozen: 2026-09-14

## Inherited terminal state

ITER048 is terminal **SCOPED BLOCKED — `LORENTZIAN_EQ11_ROUTING_REFERENCE_AUTHORITY_BLOCKED_SOURCE_INDEX_INCONSISTENCY`**. Exact arXiv `main.tex` Eq.(11) uses `i_8` in both the fourth and fifth 6j factors and omits `i_9` from the displayed routing, while the immediately following source comment maps `rCDl=i9`, `rCDr=i10`. No amplitude-based convention choice is allowed.

The same frozen arXiv source directly cites `https://github.com/PietropaoloFrisoni/Monte_Carlo_spinfoams`; ITER048 recovery pinned that repository at `84b375f2a2e0d29b44dd8820953553624bb007a3` and found source-relevant EPRL vertex-renormalization notebooks/code. This author code is therefore admissible as an independent source-derived authority. No substitute repository may be introduced after results.

## Frozen scientific question

Does the authors' cited implementation at the already-pinned commit provide an explicit, mechanically recoverable routing that uniquely distinguishes `i8` from `i9` in the fifth SU(2) 6j / corresponding recoupling object, thereby resolving the Eq.(11) source inconsistency **without** consulting numerical amplitude agreement?

This gate reconciles routing authority only. It does not retroactively change ITER048, compute a five-vertex EPRL amplitude, establish a refinement map, or earn bridge credit.

## Frozen authority panel

1. exact arXiv `2302.00072` source with `main.tex` SHA256 `bff93f3a7857658264a04eb23521bb935a68eccb7760b284589ff5ec4073f063`;
2. literal cited repository `PietropaoloFrisoni/Monte_Carlo_spinfoams@84b375f2a2e0d29b44dd8820953553624bb007a3`;
3. exact backend `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f` only for API naming/arity context, not numerical fitting.

## Frozen candidate interpretations

- `TEX_LITERAL`: fifth 6j uses `i8`, leaving `i9` absent from the displayed Eq.(11) coupling structure.
- `COMMENT_REPAIR`: fifth 6j uses `i9`, consistent with the exact source comment `rCDl=i9`, `rCDr=i10` and keeping the fourth 6j on `i8`.
- `OTHER`: any different mapping mechanically stated by the pinned author implementation.

No candidate may be selected from amplitude size/sign/agreement.

## Independent lanes (`fail-fast:false`)

1. `code-routing`: clone the exact author-code commit; mechanically extract all vertex-renormalization scripts/notebooks and every occurrence of `rCDl`, `rCDr`, `i8`, `i9`, `i_8`, `i_9`, Wigner/6j calls, recoupling arrays and EPRL partial-amplitude routines. Preserve file hashes and exact excerpts.
2. `notebook-callgraph`: identify the EPRL 5→1 notebook(s), the code/data-generation routines they invoke, argument order, and the exact author-code commit. Determine whether routing is executable or only post-processing/data analysis.
3. `tex-code-crosswalk`: preserve the exact arXiv comment mapping `rbl=i7`, `rbr=i8`, `rCDl=i9`, `rCDr=i10`, `rIul=i11`, `rIur=i12`, `rIu=i13`, `rIbl=i14`, `rIbr=i15`; compare it mechanically to names/order used by the pinned implementation. No numerical amplitude values may enter this lane.
4. `routing-null`: prospectively test whether the implementation evidence distinguishes `TEX_LITERAL` from `COMMENT_REPAIR`; reject any procedure that chooses a route by maximizing agreement, matching a sign, minimizing an error, or fitting a normalization. If the implementation does not uniquely distinguish the candidates, this lane is BLOCKED.

## Frozen PASS predicates

`AUTHOR_CODE_ROUTING_PASS` requires source-preserved implementation evidence that directly and uniquely maps the fifth recoupling/6j object to either `i8`, `i9`, or an explicitly different source-defined label, with no amplitude-based inference.

`CALLGRAPH_PROVENANCE_PASS` requires that the relevant mapping belongs to code that generates/evaluates the vertex-renormalization object, not merely a plotting label or unrelated notebook annotation.

`TEX_CODE_CROSSWALK_PASS` requires a one-to-one mechanical crosswalk for at least `i7...i15` between exact source comment names and author-code names/order, sufficient to explain the disputed slot.

`ROUTING_NULL_PASS` requires that the selected mapping be fixed solely by source/code structure and that all amplitude-fitting selection rules remain rejected.

## Terminal outcomes

- `LORENTZIAN_AUTHOR_CODE_ROUTING_RECONCILIATION_PASS` iff all four predicates PASS and exactly one routing is structurally selected.
- `LORENTZIAN_AUTHOR_CODE_ROUTING_RECONCILIATION_BLOCKED` if the pinned author code is analysis-only, lacks the relevant mapping, or remains ambiguous between candidate routings.
- `SCIENTIFIC_FAIL` only if an executed frozen structural predicate contradicts a uniquely specified author-code mapping.
- `INFRASTRUCTURE_FAIL` only for clone/source/tool transport failure before the structural predicates are evaluable.

PASS authorizes only a separately preregistered bounded fixed-configuration five-vertex summand contraction using the reconciled route and the sectors already frozen in ITER048. ITER048 remains historically BLOCKED regardless of outcome.

## Locks

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory `0 / UNFORMED`. No `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, or `BRIDGE_DERIVED`. Unbounded ten-face sum, shell convergence, zero-face deletion and coarse↔fine amplitude equality remain unauthorized.
