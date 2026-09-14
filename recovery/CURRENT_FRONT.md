# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**. Bridge credit remains zero.

## RC006 unchanged

RC006 numerical retry remains unauthorized. No Eq.(27), Eq.(29), Lambda, one-step TNR, bridge or candidate-theory claim is opened by the current Lorentzian work.

## Lorentzian multi-vertex lineage

ITER047 remains SCIENTIFIC PASS — `LORENTZIAN_5TO1_ASSEMBLY_AUTHORITY_PASS`, run `34808646324`.

ITER048 remains terminal **SCOPED BLOCKED — `LORENTZIAN_EQ11_ROUTING_REFERENCE_AUTHORITY_BLOCKED_SOURCE_INDEX_INCONSISTENCY`**. It is not retrofitted.

ITER049 remains terminal **SCIENTIFIC PASS — `LORENTZIAN_AUTHOR_CODE_ROUTING_RECONCILIATION_PASS`**, run `34811866640`. The pinned authors' executable path selects `COMMENT_REPAIR` for the disputed recoupling route: fourth Wigner-6j uses `rbl/rbr`; fifth uses `rCDl/rCDr`, hence `i9` rather than the duplicated displayed Eq.(11) `i8`, without amplitude fitting.

ITER050 remains terminal **INVALID_IMPLEMENTATION — `LORENTZIAN_BOUNDED_FIXED_CONFIGURATION_CONTRACTION_NOT_EXECUTED`**. Its green Actions run never evaluated a Lorentzian vertex and did not instantiate the frozen five-vertex summand. Durable report commit `51cd9302f25f642fdb0ed85539fb7421bdbba213`.

## ITER051 terminal PASS — pinned Lorentzian backend runtime

Preregistration: `prereg/ITER051_LORENTZIAN_PINNED_BACKEND_RUNTIME_EXECUTABILITY_2026-09-14.md`, commit `f013d4800a306ce4c1d9838d2a63c781c16f864d`.

Authoritative run: **`34818301950`** at production head **`52150ba71882c04091edbfac16e6f55ca0d244fe`**.

Terminal classification:

**`PASS — LORENTZIAN_PINNED_BACKEND_RUNTIME_PASS`**.

The exact pinned backend `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f` was successfully built in the hosted Ubuntu environment using:

- source-named `wigxjpf-1.13`, archive SHA256 `90ab9bfd495978ad1fdcbb436e274d6f4586184ae290b99920e5c978d64b3e6a`;
- source-named `fastwigxj-1.4.1`, archive SHA256 `0a4171c18dfd0ad5689c9456c873a9edd7a2a2af8e15805e880b800e8f766550`;
- `.3j` table with `max-E-3j=50`;
- `.6j` table with `max-E-6j=40`;
- `BLAS=system`, `OMP=0`, no Y-map override.

No fastwigxj 9j repair was required or applied.

Frozen smoke point:
- `gamma=1.2`;
- ten `two_j=1` = physical `j=1/2`;
- five `two_i=0` = physical `i=0`;
- `Dl=0`.

Two independent processes launched the backend's own `bin/vertex-amplitude` executable and both returned exactly

**`1.34499311005e-09`**

with return code zero, finite output and exact runtime identity. Absolute A/B difference = `0.0`, well below the prospectively frozen reproducibility tolerance.

Runtime identity and negative-control lanes PASS. Changed gamma, changed Dl, changed spin tuple and deliberately wrong binary identity were rejected.

Key frozen runtime hashes:
- `bin/vertex-amplitude`: `b4f8f536645b3fe6bc55830040f624140eefca02a3b960b9940b2564a7876e26`;
- `lib/libsl2cfoam.so`: `a539c968afde2a7ec397b2fa7184f9dd036042b82ff2ec5d8026c2b6881b71fc`;
- `.3j` table: `73d9170de4f04b776923106c5c6ea1bbb70cf2e62a14d24b83cda31194567e6e`;
- `.6j` table: `de1a29d0252c3c1ebf51b96d7fdebe7f21587ee65dcbc3864070774c14704b72`.

Build artifact `10336669907`, digest `sha256:f357f01e2aa370db20701bbced8cf7f6d03d6c43751ba5399584dd343820454b`; aggregate artifact `10337373597`, digest `sha256:842a9868229de381de47ede61556bb2efe274b986ec3eed75e3e070ed9a63016`.

Durable terminal report: `results/ITER051_LORENTZIAN_PINNED_BACKEND_RUNTIME_PASS_2026-09-14.md`, commit `16c8934ae7074f5c29aa20af3ded0a73dbfb0bdf`.

### Interpretation ceiling

This proves executable runtime availability and reproducibility for one prospectively frozen local Lorentzian vertex smoke configuration only. It is not a five-vertex result and earns no bridge credit.

## New local-vertex argument source blocker

During ITER051, an outcome-independent source audit found a mapping issue that is invisible in the all-zero smoke sector but material in the old alternating `0/1` held-out sector.

Durable record: `sources/ITER051_LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK.md`, commit `b918058a35cbaf66456aa57b19576104c4d8c2f3`.

Exact arXiv Eq.(11) local vertex intertwiner argument lists and the pinned authors' executable `vertex_compute` local range comments/code-name mapping differ in several slots, not only the already-known displayed fifth-6j `i8/i9` inconsistency. Examples include the up local fifth slot (`i2` literal Eq.(11) versus executable `rBCl=i1`) and analogous left/right recoupling-basis differences.

These discrepancies may reflect a basis/orientation recoupling between the displayed formula and executable implementation. They must not be guessed or selected from amplitude agreement.

The exact backend doubled-label semantics are separately source-qualified in `sources/ITER051_LORENTZIAN_BACKEND_LABEL_SEMANTICS.md`: physical `j=1/2 -> two_j=1`, physical `i=0 -> two_i=0`, physical `i=1 -> two_i=2`.

## Exact next admissible gate

The next primary scientific/source gate is **not yet another numerical five-vertex contraction**.

Prospectively freeze and execute a **`LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK` authority gate** that reconciles without amplitude fitting:

1. the five literal Eq.(11) local `A_v` intertwiner lists;
2. the exact source comment mapping `rBCl=i1 ... rIbr=i15`;
3. the pinned authors' executable `vertex_compute` local range comments and tensor-axis order;
4. each Wigner-6j pre-contraction from left to right recoupling basis;
5. the pinned `sl2cfoam-next` `(i1,...,i5)` / doubled-label API.

Only after that crosswalk closes may a repaired bounded primary/held-out five-vertex summand gate be preregistered and run with the now-validated runtime backend.

## Persistent locks

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory `0 / UNFORMED`.

Still unauthorized: unbounded ten-face summation, shell convergence, coarse↔fine amplitude equality, zero-face deletion, full Eq.(27), Eq.(29)/Lambda, one-step TNR, bridge derivation, candidate-theory construction, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`.
