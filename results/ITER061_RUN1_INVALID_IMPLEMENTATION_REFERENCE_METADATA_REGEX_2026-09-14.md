# ITER061 run 1 — parser false-negative

Date: 2026-09-14

## Classification

`INVALID_IMPLEMENTATION — SOURCE_REFERENCE_METADATA_REGEX_FALSE_NEGATIVE`

This is not a source-authority BLOCKED result.

## Frozen gate

Preregistration: `prereg/ITER061_RC008_COMPANION_REFINEMENT_COMPLEX_GLUING_AUTHORITY_2026-09-14.md`.

Source under test: Sebastian Steinhaus, *Coarse Graining Spin Foam Quantum Gravity—A Review*, Frontiers in Physics 8:295 (2020), DOI `10.3389/fphy.2020.00295`, as a source-faithful companion for RC008.

## Authoritative execution

- run: `34868725240`
- production head: `f32f10c44ad7b5e2abdd7ae02ac18f5db0a0c106`
- workflow terminal status: `completed / success`
- normalized source SHA256, identical in all six lanes: `2a0ffc7259c3167783dc11c63e78cfe100066ad9e515c4204f705d63d5df9673`
- raw HTML SHA256: `d390f1882ee4d2510eb63a685b7ccd35e7fe84e25bccba2de935c476d92a2f80`

Aggregate artifact:

- id `10358101978`
- digest `sha256:0faa49a30f5a24536b75fc52d8140a1df1075d67e72f08d1f14dd5bc0e7dcefb`

## Lane evidence

Five lanes passed their frozen predicates:

- `cuboid-complex`: PASS
- `embedding-relation`: PASS
- `amplitude-blocking`: PASS
- `observable-comparator`: PASS
- `null-controls`: PASS, 5/5 mutations applied and detected

`source-identity` alone emitted `BLOCKED_SOURCE_AUTHORITY` because `target_reference_metadata=false`.

Manual audit of that lane's own emitted source context shows that the reference is actually present exactly enough to satisfy the preregistered identity condition:

`Bahr B Steinhaus S . Hypercuboidal renormalization in spin foam quantum gravity . Phys Rev D . ( 2017 ) 95 : 126006 . 10.1103/PhysRevD.95.126006`

The parser pattern expected tighter punctuation/spacing around `D`, `(2017)` and `95:126006`; the normalized Frontiers text inserts spaces around punctuation. This is therefore a formatting parser false-negative, not missing source authority.

## Manual audit of the five non-failing lanes

The emitted contexts support the preregistered source statements:

- two hypercuboids glued along a common 3D cuboid;
- coarse boundary geometry fixed and coarse-face total areas fixed;
- each hypercuboid subdivided into 16 in the fine calculation;
- prescribed geometric embedding with fine areas summing to the coarse area;
- fine-to-coarse `alpha' -> alpha` flow;
- blocking of 16 vertex amplitudes for hypercubic combinatorics;
- boundary/bulk split, with bulk labels summed into the fine amplitude;
- embedding/coarse-graining maps deriving an effective coarse amplitude;
- 4-volume variance compared in coarse and fine calculations at fixed coarse boundary state;
- the comparison defines the reported one-parameter fixed point;
- all five adversarial mutations were detected.

## Minimal repair rule

Allowed repair: relax only whitespace/punctuation matching for the exact bibliography metadata predicate. No source, scientific predicate, attribution requirement, lane structure, null control, classification threshold, or claim ceiling may change.

## Locks

Until the corrected execution is terminal and manually audited:

- `RC008_COMPANION_REFINEMENT_COMPLEX_GLUING_AUTHORITY_COMPLETE=false`
- restricted coarse/refined amplitude reconstruction remains unauthorized
- `bridge_credit=false`
- candidate theory remains `UNFORMED / 0%`
