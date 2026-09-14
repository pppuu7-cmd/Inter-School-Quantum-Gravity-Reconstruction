# Preregistration — ITER045 Lorentzian EPRL 1→5 implementation readiness

Date frozen: 2026-09-14

## Inherited result

ITER044 is source-scoped SCIENTIFIC PASS: `LORENTZIAN_MULTIVERTEX_REFINEMENT_MAP_SOURCE_QUALIFIED_SCOPED`. The source-qualified route is the 4D 1→5 Pachner refinement / 5→1 vertex-renormalization amplitude. The unrelated zero-spin face-collapse shortcut remains BLOCKED. No bridge credit exists yet.

This gate is an implementation-readiness validation, not an amplitude-equality or renormalization claim.

## Frozen implementation authority

Official backend: `qg-cpt-marseille/sl2cfoam-next`, exact commit
`052e4346028870bd76f69a3034e6cae8defb8f7f`.

The frozen repository README states that SL2Cfoam-next computes Lorentzian EPRL vertex amplitudes as tensors, and `QUICKSTART_Ubuntu.md` gives the reference first calculation with `gamma=1.2`, ten unit spins and a shell cutoff. No backend update after this preregistration may be substituted in ITER045.

Frozen source topology remains arXiv `1803.00835` + `2302.00072`, as qualified in ITER044.

## Frozen scientific questions

A. Does the combinatorial 1→5 subdivision reproduce the source-stated five Lorentzian EPRL vertices, ten internal tetrahedra/dual edges, ten internal triangles/dual faces and ten boundary triangles without hand-entering those counts?

B. Is the official pinned backend API/source tree sufficient to define each individual Lorentzian EPRL 4-simplex vertex tensor needed by that five-vertex object, with ten face spins per vertex and explicit Immirzi/shell controls?

C. What is the exact raw internal-spin state-space growth for the ten bulk faces under a homogeneous half-integer cutoff? This is a prospective feasibility diagnostic only; it must not be used to prune sectors after numerical amplitudes are seen.

D. Do topology null controls reject disconnected or malformed 1→5 constructions?

## Independent lanes

`fail-fast:false`:

1. `topology-incidence` — construct the 1→5 subdivision algorithmically from the original 4-simplex plus an interior vertex; enumerate refined 4-simplices, internal tetrahedra, internal triangles, boundary triangles and simplex adjacency. PASS iff counts are exactly 5 / 10 / 10 / 10 and every pair of refined 4-simplices shares exactly one internal tetrahedron.
2. `backend-provenance` — clone the official backend at the frozen SHA; hash README, quickstart, `inc/sl2cfoam.h`, `src/vertex.c`; mechanically verify the API/source contains Lorentzian vertex computation with ten spins plus shell/Immirzi configuration. This is backend provenance, not a numerical amplitude PASS.
3. `state-space` — prospectively compute raw Cartesian bulk-spin tuple counts for ten internal faces at frozen homogeneous half-integer cutoffs `Jmax={1,3/2,2,5/2,3}`. No amplitude values are consulted. Report only feasibility/scaling.
4. `topology-null` — frozen malformed controls: remove one refined simplex, duplicate one simplex, replace the interior vertex by an original vertex, and disconnect one simplex. Each must fail at least one exact topology predicate.

## Terminal outcomes

- `LORENTZIAN_1TO5_IMPLEMENTATION_READINESS_PASS` iff topology-incidence, backend-provenance and all null controls PASS and state-space lane completes.
- `LORENTZIAN_1TO5_IMPLEMENTATION_READINESS_BLOCKED` if the source topology cannot be represented uniquely or the pinned backend lacks the required single-vertex object/API.
- `INFRASTRUCTURE_FAIL` only for transport/tool failure before the frozen predicates can be evaluated.

A PASS authorizes only a new prospectively preregistered bounded numerical vertex/contraction validation. It does not authorize full 10-face summation, amplitude invariance, coarse↔fine equality, bridge credit, or candidate theory construction.

## Frozen locks

No retuning; no sector pruning from observed amplitudes; no zero-face deletion; no `BRIDGE_DERIVED`; no `NEW_PHYSICS_FOUND`; no `NEW_QG_THEORY_REQUIRED`; no `ALL_KNOWN_SCHOOLS_FAIL`. Candidate theory = 0 / UNFORMED; overall readiness remains 49% until a substantive numerical/refinement gate closes.