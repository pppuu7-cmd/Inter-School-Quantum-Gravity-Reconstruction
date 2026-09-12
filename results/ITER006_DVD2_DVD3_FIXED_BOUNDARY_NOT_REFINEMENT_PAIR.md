# ITER006 — DVD2/DVD3 direct refinement relation is unestablished

Date: 2026-09-12

Pinned DVD source: arXiv:1801.03771.
Refinement authority added later: arXiv:1010.5437.

## Correction to the earlier fixed-boundary argument

The DVD source chooses the same external boundary — two 4-link dipoles — and studies several different internal foams at that fixed boundary graph. This fact **does not by itself rule out foam refinement**.

arXiv:1010.5437 defines a refinement order precisely among proper foams with the same boundary: `C1 <= C2` when there is an incidence-preserving embedding of vertices, edges and faces of `C1` into `C2`. A colored refinement can be a trivial extension when any added faces carry `j=0`.

Therefore the earlier inference “same boundary => not a refinement pair” is withdrawn.

## What remains locked

The pinned DVD paper itself does not state an incidence embedding `DVD2 -> DVD3` or `DVD3 -> DVD2`. Appendix C instead presents DVD1–DVD4 as four **topologically distinct** integrable one-vertex vertex graphs for the DVD foam, each with eight faces. DVD2 and DVD3 have different face-rigidity/routing structure and different explicit amplitudes.

Hence the currently valid statement is:

`DVD2_DVD3_DIRECT_REFINEMENT_RELATION_UNESTABLISHED_PENDING_INCIDENCE_AUDIT`

Consequences:

- `DVD2 = coarse` and `DVD3 = fine` remains forbidden unless the structural incidence-embedding audit passes.
- Same boundary is compatible with refinement, but same boundary plus a different foam is not sufficient evidence of refinement.
- Numerical stabilization across DVD2/DVD3, internal-face structure, diagram complexity, or booster-shell depth `D` cannot independently receive refinement/cylindrical-consistency credit.
- If the direct DVD2/DVD3 embedding fails, the correct next object is a **new explicit trivial extension of one DVD foam**, not a semantic relabelling of another topologically distinct DVD graph.
- Raw Lorentzian `Z_C` invariance under a `j=0` face extension and multiplicity-corrected cylindrical consistency `A_C=|sigma|_C Z_C` must be kept distinct.
- `BRIDGE_DERIVED = false`; candidate theory remains `UNFORMED / 0%`.
