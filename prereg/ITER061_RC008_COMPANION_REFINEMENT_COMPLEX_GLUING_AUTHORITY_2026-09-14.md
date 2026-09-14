# ITER061 — RC008 companion refinement-complex + gluing authority

Date: 2026-09-14

## Scientific question

Can the exact source-authority blocker that currently prevents source-only RC008 coarse/refined reconstruction be closed by a source-faithful companion reference that explicitly supplies the missing coarse/fine complex, gluing, subdivision, embedding-map, internal-sum/blocking and fixed-boundary observable structure?

This gate is source-authority only. It does not reproduce the restricted EPRL-FK hypercuboid amplitude or its RG flow.

## Prior frozen blocker

Two terminal RC008 gates are preserved unchanged:

1. `SOURCE_CLOSURE_BLOCKED_MISSING_EXPLICIT_OBJECT`: core amplitude objects and refinement language were present, but the frozen search did not locate an explicit multi-vertex gluing object.
2. `SOURCE_STRUCTURAL_GLUING_AUTHORITY_BLOCKED`: face/edge/vertex products, internal sums, shared boundary data and amplitude composition were located, but coarse/refined-complex context failed the frozen exact-TeX predicate.

The second report explicitly leaves open a `source-faithful companion reference`; this gate tests only that route and cannot retroactively convert either historical result into PASS.

## Frozen source set

Target realization/source:

- RC008: `realizations/RC-008_QUANTUM_CUBOID_HYPERCUBOID_RENORMALIZATION.md`
- Bahr & Steinhaus, *Hypercuboidal renormalization in spin foam quantum gravity*, Phys. Rev. D 95, 126006 (2017), arXiv:1701.02311.

Source-faithful companion under test:

- Sebastian Steinhaus, *Coarse Graining Spin Foam Quantum Gravity—A Review*, Frontiers in Physics 8:295 (2020), DOI `10.3389/fphy.2020.00295`, arXiv:2007.01315.
- Exact public authority endpoint for machine audit: `https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2020.00295/full`.

The companion must itself explicitly identify/reference the Bahr-Steinhaus quantum-cuboid results, including the 2017 hypercuboidal-renormalization paper. Generic spin-foam statements not tied to the cuboid discussion cannot close the RC008 blocker.

## Frozen authority predicates

### A — source identity / attribution

Require all:

- exact companion title and author identity;
- DOI `10.3389/fphy.2020.00295`;
- bibliography entry for Bahr & Steinhaus, *Hypercuboidal renormalization in spin foam quantum gravity*, Phys. Rev. D 95, 126006;
- the quantum-cuboid coarse-graining discussion explicitly attributes the setup to Bahr/Steinhaus source work.

### B — explicit RC008 coarse/fine complex

Require all in the source-faithful cuboid discussion:

- two hypercuboids glued along a common 3D cuboid;
- fixed coarse boundary geometry/state;
- a coarse and a fine calculation of the same transition/observable;
- each hypercuboid subdivided into 16 in the fine description.

### C — explicit refinement/embedding relation

Require all:

- geometric embedding map is prescribed;
- fine areas sum to the corresponding coarse area;
- the flow is explicitly fine-to-coarse (`alpha' -> alpha`) or an equivalent unambiguous fine/coarse parameter relation.

### D — amplitude blocking / internal-degree composition authority

Require all from the same companion review's coarse-graining construction:

- blocking of amplitudes, explicitly including the hypercubic example of 16 vertex amplitudes or an exact equivalent;
- split between boundary and block-bulk degrees of freedom;
- block-bulk/internal labels are summed/integrated over to define a fine/block amplitude;
- embedding/coarse-graining maps define an effective coarse amplitude.

This lane is required because mere geometric subdivision is insufficient to authorize an amplitude-level coarse/refined implementation.

### E — fixed-boundary observable comparator

Require all:

- the coarse boundary state is kept fixed;
- the 4-volume variance is compared in coarse and fine calculations;
- the observable comparison is what defines the one-parameter flow/fixed point in this restricted setup.

### F — adversarial/null controls

At least four frozen wrong-source variants must fail one or more authority predicates:

1. remove the `subdivided into 16` relation;
2. replace `fine areas sum to the coarse area` with an unrelated equality;
3. remove the common-3D-cuboid gluing statement;
4. remove bulk/internal summation from the blocking construction;
5. replace the cited 2017 Bahr-Steinhaus target with an unrelated reference.

At least 4/5 must be detected. These controls calibrate parser sensitivity only; they are not physics tests.

## Frozen execution architecture

Run independent lanes with `fail-fast:false` after preregistration:

- `source-identity`
- `cuboid-complex`
- `embedding-relation`
- `amplitude-blocking`
- `observable-comparator`
- `null-controls`

Each lane must independently fetch/normalize the frozen companion endpoint and emit:

- HTTP/source provenance;
- normalized source-content SHA256;
- exact predicate booleans;
- bounded context excerpts/offsets for every positive predicate;
- no scientific verdict beyond its own lane.

A dependent aggregate may combine lane booleans only after all six lanes terminate.

Manual audit of the emitted source contexts against this preregistration remains mandatory; green CI is not sufficient.

## Frozen classification

### PASS

`PASS — RC008_COMPANION_REFINEMENT_COMPLEX_GLUING_AUTHORITY_COMPLETE`

only if A-E all pass, F detects at least 4/5 wrong variants, source attribution is exact, and manual audit confirms that the cuboid-specific statements plus general blocking construction jointly instantiate the previously missing RC008 source-authority object without importing an invented rule.

A PASS authorizes only a new separately preregistered source-faithful restricted hypercuboid coarse/refined amplitude reconstruction.

### BLOCKED

`BLOCKED_SOURCE_AUTHORITY — RC008_COMPANION_AUTHORITY_INCOMPLETE_<reason>`

if the companion source lacks any required A-E relation or the cuboid-specific setup cannot be connected to the blocking construction without an extra convention.

### INVALID / INFRASTRUCTURE

- `INVALID_IMPLEMENTATION` if the parser/source object does not implement the frozen predicates;
- `INFRASTRUCTURE_FAIL` if the endpoint cannot be retrieved or parsed before authority predicates are evaluated.

No absence claim is allowed from an infrastructure failure.

## Atlas / bridge scope

Realization: RC008, F04 symmetry-restricted Riemannian EPRL-FK quantum-cuboid sector.

Primary atlas coordinates tested: `D, C, R, M/O` with emphasis on `C -> R`. This gate does not establish `X` or `E` recovery and provides zero bridge credit by itself.

## Claim ceiling

Even PASS does **not** establish:

- a reproduced hypercuboid vertex amplitude;
- a reproduced coarse/refined 4-volume variance curve;
- a new alpha fixed point;
- cylindrical consistency beyond the source's restricted setup;
- full EPRL-FK or Lorentzian EPRL refinement;
- continuum/GR recovery;
- BH004/BH004B universality;
- `BRIDGE_DERIVED`;
- `NEW_PHYSICS_FOUND`;
- `NEW_QG_THEORY_REQUIRED`;
- `ALL_KNOWN_SCHOOLS_FAIL`;
- candidate-theory construction.

Candidate theory remains `UNFORMED / 0%`.
