# ITER006 — Lorentzian graph/foam refinement source gate

Date: 2026-09-12

Authoritative workflow: `34710443728`.
Preregistered protocol: `protocol/ITER006_LORENTZIAN_GRAPH_REFINEMENT_SOURCE_GATE.json`.

## Terminal classification

`LORENTZIAN_FOAM_REFINEMENT_AUTHORITY_FOUND_IMPLEMENTATION_COMPATIBILITY_OPEN`

## Source roles

### arXiv:0909.0939 — KKL arbitrary-graph EPRL

This source authorizes EPRL amplitudes on arbitrary boundary spin networks / 2-complexes, but the frozen audit found no explicit refinement, subdivision, or cylindrical-consistency operation. It is therefore model-domain authority, not by itself a refinement rule.

### arXiv:1010.5227 — local spin foams and cylindrical moves

This source formulates locality, composition, and cylindrical consistency for spin foams and lifts LQG cylindrical moves such as link reversal, link splitting, and link erasing to spin-foam amplitudes. In particular, link-splitting consistency is expressed by dependence on the product of the split holonomies. This supplies an explicit class of graph-refinement/cylindrical moves.

The source discusses both Spin(4) and SL(2,C) formulations, but its explicit normalization statement emphasized in the abstract is Euclidean. Therefore this source is retained as structural/cylindrical authority and is not by itself sufficient for a Lorentzian numerical equality claim.

### arXiv:1010.5437 — fixed-boundary foam refinement and Lorentzian trivial extension

This source gives the strongest direct refinement authority for the present ISQGR front.

For proper foams with a fixed boundary it defines a directed partial order

`C1 <= C2`

when there is an embedding `iota: C1 -> C2`, consisting of injective maps on vertices, edges, and faces that preserve their incidence relations. Thus **fixed boundary does not preclude foam refinement**.

For a colored foam it defines a trivial extension by keeping the coloring unchanged on the embedded subfoam and assigning the trivial SU(2) representation `j=0` to the additional faces. The raw Lorentzian amplitude written in the source is invariant under such a trivial-face extension because the new face contributes unit dimension/characters at `j=0`.

For the stronger cylindrical-consistency identity relevant to the equivalence between refinement and the foam sum, the source introduces the coloring multiplicity `|sigma|_C` and the amplitude

`A_C(sigma) = |sigma|_C Z_C(sigma)`.

It then requires equality of `A_C` under trivial extension. Equivalently, a modified foam weight with the inverse multiplicity factor removes the residual automorphism overcounting.

The source explicitly states that the relevant trivial-extension property holds for the Lorentzian amplitude considered there (while excluding a distinct variant).

## Consequence for the DVD programme

The previous statement “same boundary means DVD2/DVD3 cannot be a refinement pair” was too strong. The corrected statement is:

- the DVD source studies several different foams with the same two-4-link-dipole boundary;
- fixed boundary is compatible with the refinement order of arXiv:1010.5437;
- however DVD2 and DVD3 may be called a direct refinement pair **only if an incidence-preserving embedding of their concrete 2-complexes is demonstrated** and any additional faces in the refined foam can be interpreted as the source-authorized trivial extension.

The pinned DVD paper itself does not state such an embedding. Its Appendix C instead describes DVD1–DVD4 as topologically distinct one-vertex vertex graphs with eight faces and different face routings / rigidity properties.

## Next gate

Freeze and execute a structural incidence-embedding audit for DVD2 versus DVD3 before any amplitude comparison is promoted to refinement credit. If no direct embedding exists, construct a new explicit trivial extension of one DVD foam rather than relabelling another topologically distinct DVD foam as its refinement.

## Claim locks

- Booster-shell cutoff `D` is not refinement.
- DVD2/DV D3 numerical differences are not refinement evidence unless the structural embedding gate passes.
- Raw `Z_C` trivial-extension invariance and multiplicity-corrected cylindrical consistency are distinct statements and must not be conflated.
- No bridge credit yet: `BRIDGE_DERIVED = false`.
- Candidate theory remains `UNFORMED / 0%`.
