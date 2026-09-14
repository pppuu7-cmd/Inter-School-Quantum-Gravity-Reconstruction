# ITER103 protocol — retrospective CDT directional-QRC traceless-Ricci constraint

Date: 2026-09-15
Gate: `ITER103_RETROSPECTIVE_CDT_DIRECTIONAL_QRC_TRACELESS_RICCI_CONSTRAINT`
Protocol status: **RETROSPECTIVE / validation credit permanently 0**

## Motivation

ITER102 isolated a leading small-radius directional QRC channel proportional to the traceless Ricci contraction `S_ij v^i v^j`. The published 4D CDT QRC paper contains a comparison of maximally spacelike and maximally timelike sphere-centre separations.

The qualitative directional result was inspected before this protocol. This gate therefore receives no prospective validation credit and is limited to source-accurate constraint typing.

## Frozen source

- arXiv:2006.06263 — Klitgaard & Loll, *How round is the quantum de Sitter universe?*
- ITER102 only for the local tensor decomposition and claim ceiling.

## Frozen question

What does the published spacelike-versus-timelike QRC comparison actually constrain: merely a directional lattice offset, equality of two curvature projections, or the full four-dimensional traceless Ricci tensor?

## Required predicates

A. Preserve the source's exact directional definitions and volume/coupling scope.

B. Separate vertical/nonuniversal `c_q` offset effects from scale-dependent curvature-profile shape.

C. Record the source's stated scale window over which the shifted curves agree.

D. Do not convert equality of two selected directional classes into full tensor isotropy without sufficient independent directions/symmetry authority.

E. Do not force the finite-radius data into ITER102's `delta -> 0` coefficient formula.

F. Retrospective validation credit remains zero.

## Frozen classifications

- `SOURCE_SUPPORTS_TWO_CLASS_DIRECTIONAL_CURVATURE_ISOTROPY_NOT_FULL_TENSOR_RECONSTRUCTION` if the source supports matching curvature behaviour in the two selected classes after offset control, but not all tensor components.
- `SOURCE_SUPPORTS_FULL_TRACELESS_RICCI_ZERO` only if enough independent directional information and normalization authority are actually present.
- `SOURCE_DIRECTIONAL_RESULT_INCONCLUSIVE` if offset/systematics prevent even the two-class curvature comparison.

## Controls

- `CQ_OFFSET_CURVATURE_SWAP_CONTROL`
- `TWO_DIRECTIONS_FULL_TENSOR_CONTROL`
- `FINITE_RADIUS_LOCAL_EXPANSION_CONTROL`
- `RETROSPECTIVE_CREDIT_CONTROL`

## Claim ceiling

No Einstein-space theorem, no full local isotropy theorem, no prospective validation credit, no FRG tensor-flow validation, no bridge derivation and no candidate theory.