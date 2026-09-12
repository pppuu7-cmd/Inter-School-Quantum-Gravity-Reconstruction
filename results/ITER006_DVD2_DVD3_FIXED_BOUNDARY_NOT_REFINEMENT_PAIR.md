# ITER006 — DVD2/DVD3 are fixed-boundary foams, not a coarse/fine refinement pair

Date: 2026-09-12

Pinned DVD source: arXiv:1801.03771.

## Source evidence

The source states that it chooses a simple boundary consisting of **two 4-link dipoles** and studies a collection of different spin-foam amplitudes with up to two vertices and one internal face. It then formulates one of its guiding questions explicitly **at fixed boundary graph**: how do the different foams scale and which foams dominate.

Thus the DVD diagrams are different internal spin-foam histories/combinatorics associated with the same external boundary graph/data class. They are not introduced as a partially ordered pair of boundary discretizations `b < b'`, nor does the source provide an embedding `H_b -> H_b'` relating DVD2 and DVD3.

This agrees with the earlier semantic source-authority audit `34709790323`, which found no explicit refinement map in the pinned DVD source.

## Terminal compatibility statement

`DVD2_DVD3_FIXED_BOUNDARY_FOAMS_NOT_DIRECT_REFINEMENT_PAIR`

Consequences:

- `DVD2 = coarse` and `DVD3 = fine` is forbidden.
- Differences or stabilization across DVD2/DVD3, internal-face content, booster-shell depth `D`, or diagram complexity cannot by themselves receive refinement/cylindrical-consistency credit.
- A genuine Lorentzian DVD refinement test must introduce a source-authorized refinement of the **boundary graph/state space** or an explicitly equivalent foam-refinement operation with a proven amplitude-consistency relation.
- `BRIDGE_DERIVED = false`; candidate theory remains `UNFORMED / 0%`.
