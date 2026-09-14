# Preregistration — ITER044 genuine multi-vertex Lorentzian EPRL refinement source-map audit

Date frozen: 2026-09-14

## Inherited authoritative frontier

RC006 remains source-BLOCKED after ITER039 SCIENTIFIC FAIL and the authoritative ITER042 `DELEGATED_AUTHORITY_SOURCE_EXPANSION_BLOCKED`. ITER043 was an infrastructure-failed, scientifically void excursion created from a superseded interpretation and is not an RC006 successor.

The independent PHASE_1 front `MULTIVERTEX_LORENTZIAN_EPRL_REFINEMENT` is currently `BLOCKED_SOURCE_ALGEBRAIC_ZERO_FACE_COLLAPSE_AMBIGUOUS`; `refinement_map_derived=false`.

This iteration therefore switches to the independent genuine multi-vertex Lorentzian EPRL/spinfoam priority. It is a **source-map audit**, not a bridge derivation and not a numerical fit.

## Frozen source panel

Only the following openly inspectable Lorentzian EPRL multi-vertex/amplitude sources may determine the gate:

1. Sarno, Speziale, Stagno, *2-vertex Lorentzian Spin Foam Amplitudes for Dipole Transitions*, arXiv:`1801.03771`.
2. Donà, Frisoni, Wilson-Ewing, *Radiative corrections to the Lorentzian EPRL spin foam propagator*, arXiv:`2206.14755`.
3. Donà, Frisoni, *Summing bulk quantum numbers with Monte Carlo in spin foam theories*, arXiv:`2302.00072`.
4. Donà, *Infrared divergences in the EPRL-FK Spin Foam model*, arXiv:`1803.00835`.

No later paper may be substituted after results are seen. Newly encountered citations may be retained as future candidates only.

## Frozen scientific questions

A. Does the source panel give an explicit **genuine multi-vertex Lorentzian EPRL amplitude object**, with boundary data and internal-face/internal-edge sums identified well enough to distinguish it from a product of disconnected single-vertex amplitudes?

B. Does any frozen source give an explicit **refinement/coarse-fine map** between two 2-complexes or boundary discretizations, rather than merely evaluating a fixed multi-vertex diagram or studying cutoff scaling/divergence?

C. For the existing zero-face-collapse blocker: does any frozen source state an amplitude-preserving rule for deleting/collapsing zero-spin internal faces/strands, including its domain and normalization? Absence or ambiguity remains BLOCKED; zero-spin deletion may not be inferred from numerical convenience.

D. Is there an executable numerical representation of the frozen multi-vertex amplitude (e.g. finite-cutoff bulk sums / sl2cfoam-next decomposition) whose source definition is explicit enough to support a later preregistered validation gate without inventing a refinement map?

## Independent lanes

Use `fail-fast:false`:

- `dipole-1801`: source extraction and formula/topology inventory for arXiv:1801.03771.
- `radiative-2206`: source extraction and formula/topology inventory for arXiv:2206.14755.
- `montecarlo-2302`: source extraction and internal-sum/numerical inventory for arXiv:2302.00072, with arXiv:1803.00835 as a fixed auxiliary comparison in the same lane.
- `semantic-null`: frozen controls enforcing that (i) two vertices alone != refinement map, (ii) cutoff/profile/scaling != refinement map, (iii) numerical finiteness/divergence != refinement, and (iv) zero-face deletion without a sourced identity cannot count as an amplitude-preserving collapse.

## Frozen evidence predicates

For each source preserve exact pages/excerpts around: `two-vertex`, `2-complex`, `boundary`, `internal face`, `bulk`, `sum`, `cutoff`, `refinement`, `coarse`, `fine`, `Pachner`, `zero spin`, `j=0`, `sl2cfoam`, `vertex renormalization`, `self-energy`, and amplitude equations.

`MULTIVERTEX_AMPLITUDE_OBJECT_SOURCE_PASS` requires source evidence for a connected >1-vertex Lorentzian EPRL object plus explicit internal/boundary summation structure.

`REFINEMENT_MAP_SOURCE_PASS` is stricter: a source must explicitly map a coarse complex/boundary object to a refined one or compare amplitudes under a stated refinement/coarse-graining transformation. A fixed two-vertex graph, radiative diagram, or cutoff family is insufficient.

`ZERO_FACE_COLLAPSE_SOURCE_PASS` requires an explicit equality/identity or stated amplitude-preserving rule for zero-spin face/strand removal. Mere representation-theory intuition is insufficient.

`EXECUTABLE_MULTIVERTEX_OBJECT_PASS` requires enough source-defined ingredients for a later bounded computation, but gives no bridge credit by itself.

## Terminal classifications

- `LORENTZIAN_MULTIVERTEX_REFINEMENT_MAP_SOURCE_QUALIFIED_SCOPED` only if the strict refinement-map predicate passes.
- `LORENTZIAN_MULTIVERTEX_AMPLITUDE_SOURCE_PASS_REFINEMENT_MAP_BLOCKED` if a genuine multi-vertex amplitude/executable object is source-qualified but no true refinement map is.
- `LORENTZIAN_MULTIVERTEX_SOURCE_BLOCKED` if even the connected multi-vertex amplitude object cannot be source-qualified from the frozen panel.
- `INFRASTRUCTURE_FAIL` only for incomplete transport/extraction.

A refinement-map source PASS would authorize only a separate prospectively preregistered implementation/validation gate. No source-only result earns bridge credit.

## Claim locks

No `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, or `ALL_KNOWN_SCHOOLS_FAIL`. Candidate theory remains `0 / UNFORMED`. Eq.(29)/Lambda/TNR remain unauthorized. Finite-cutoff/profile/scaling diagnostics cannot raise bridge status without a true refinement map.