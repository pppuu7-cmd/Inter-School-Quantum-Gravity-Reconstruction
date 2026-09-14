# ITER049 result — Lorentzian author-code routing reconciliation

Date: 2026-09-14

## Terminal classification

**SCIENTIFIC PASS — `LORENTZIAN_AUTHOR_CODE_ROUTING_RECONCILIATION_PASS`**.

This PASS is structural/source-authority only. It does not alter ITER048, derive a refinement map, earn bridge credit, or authorize any unbounded sum.

## Frozen question and answer

The preregistered question was whether the authors' cited implementation at `PietropaoloFrisoni/Monte_Carlo_spinfoams@84b375f2a2e0d29b44dd8820953553624bb007a3` uniquely distinguishes the disputed fifth SU(2) 6j routing in Eq.(11) without amplitude fitting.

It does. In executable EPRL vertex-renormalization code, the fourth recoupling uses `rbl/rbr`, while the fifth uses `rCDl/rCDr`. Under the exact arXiv comment crosswalk `rbl=i7`, `rbr=i8`, `rCDl=i9`, `rCDr=i10`, the implementation therefore selects the preregistered `COMMENT_REPAIR` interpretation: the fifth 6j carries `i9` on its left recoupling slot, while the fourth remains on `i8`.

No amplitude magnitude, sign, normalization fit, or numerical agreement was used to choose this route.

## Predicate classification

- `AUTHOR_CODE_ROUTING_PASS`: PASS. `src/vertex_renormalization_EPRL_MC.jl` constructs the bottom-right Wigner-6j matrix from `rbl/rbr`, then constructs the right-vertex Wigner-6j matrix from `rCDl/rCDr`.
- `CALLGRAPH_PROVENANCE_PASS`: PASS. The routing occurs in the executable EPRL data-generation/contraction path, not merely a plotting notebook label. The 5→1 EPRL analysis notebook is downstream of the vertex-renormalization code.
- `TEX_CODE_CROSSWALK_PASS`: PASS. The exact arXiv comment mapping for `i7...i15` is mechanically represented by the author-code names `rbl,rbr,rCDl,rCDr,rIul,rIur,rIu,rIbl,rIbr` and their tuple/index ordering.
- `ROUTING_NULL_PASS`: PASS. Frozen controls reject route selection by amplitude agreement, sign, fitted normalization, or silent replacement without code authority.

## Authoritative Actions provenance

Run: `34811866640` at production head `946d427f2821971c3342f2ff5831b2cdeae79dc9`.

Jobs:
- code-routing `103874660015`;
- routing-null `103874660170`;
- tex-code-crosswalk `103874660187`;
- notebook-callgraph `103874660292`;
- aggregate `103874707943`.

Artifacts:
- `iter049-code-routing` id `10335077657`, digest `sha256:ad2973efd6b40b738e12cdcec3d2ba5b043fdb5836464acfec973da13ad432eb`;
- `iter049-routing-null` id `10334149958`, digest `sha256:e511588ca17d290fc8a86edd22b3fda6696a77c97f328573db3d4eb74571cf11`;
- `iter049-tex-code-crosswalk` id `10334903275`, digest `sha256:b7935b36704dd3a6cdefc5767f773867b76fab57b0592957166cdbc8eee9a885`;
- `iter049-notebook-callgraph` id `10334279521`, digest `sha256:a3f9115c3d5f4134e4fc5f8d927be200c62e2d42a8f1773d936829169540fb61`;
- aggregate id `10334579193`, digest `sha256:565d9bcf277bb1514caab9d27ce90d3cb19b980571343ab2aeb3469a56a6fc20`.

## Consequence

A separately preregistered bounded fixed-configuration five-vertex summand contraction is now authorized using only the sectors frozen in ITER048 and this reconciled route. The following remain unauthorized: unbounded ten-face summation, shell-convergence claims, zero-face deletion, coarse↔fine amplitude equality, refinement-map derivation, bridge credit, and candidate-theory construction.

ITER048 remains terminal SCOPED BLOCKED historically and is not retrofitted.