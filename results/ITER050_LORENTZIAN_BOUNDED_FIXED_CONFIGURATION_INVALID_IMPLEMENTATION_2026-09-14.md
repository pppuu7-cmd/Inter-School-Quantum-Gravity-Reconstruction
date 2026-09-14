# ITER050 — Lorentzian bounded fixed-configuration contraction

Date: 2026-09-14

## Terminal classification

**INVALID_IMPLEMENTATION — `LORENTZIAN_BOUNDED_FIXED_CONFIGURATION_CONTRACTION_NOT_EXECUTED`**.

This is not a scientific failure of the Lorentzian EPRL realization, not evidence against the 5→1 assembly, and not bridge evidence. It does not retrofit ITER048 or alter ITER049.

## Frozen contract reviewed

Preregistration: `prereg/ITER050_LORENTZIAN_BOUNDED_FIXED_CONFIGURATION_CONTRACTION_2026-09-14.md`, commit `61908806492f5053c83cf45a50ea54bc5905797b`.

The frozen object required, independently on the primary and held-out sectors:

1. evaluation of all five source-defined Lorentzian EPRL vertex amplitudes with pinned `sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`, `gamma=1.2`, `Dl=0`;
2. the five source-defined SU(2) recoupling factors under the ITER049 `COMMENT_REPAIR` routing;
3. source-prescribed phase and finite face/intertwiner weights;
4. multiplication/contraction into one bounded five-vertex fixed-configuration summand.

`PRIMARY_SUMMAND_PASS` and `HELDOUT_SUMMAND_PASS` explicitly required all five Lorentzian vertex values to be finite.

## Actions provenance

Initial implementation commit: `f9758afda5291661b1edf8115247a3d155e8e9ff`.

Initial run `34815874165` failed before substantive evaluation because `sympy` was absent. This was pre-science infrastructure only.

Dependency-only repair commit: `0158a25ef6f96236d3dc783e922bfebe4e88a360`.

Corrected run: `34815939847`, completed success at the Actions infrastructure level.

Jobs:
- backend-preflight `103886506015`;
- null-controls `103886506147`;
- primary-algebra `103886506165`;
- heldout-algebra `103886506189`;
- authority-freeze `103886506281`;
- aggregate `103886601301`.

Artifacts:
- `iter050-primary-algebra` id `10336795332`, digest `sha256:0f75cf5ff06f7b58f9d64c4ecf6c93b6f8e3d05e5d45cee3a6f7d02772bfe21c`;
- `iter050-aggregate` id `10336575855`, digest `sha256:ad0b15c318ae88f70ef4a9d5fdc89c79cea4b0d5c1273ccef22b3767e4bff2ba`;
- `iter050-backend-preflight` id `10336520282`, digest `sha256:158a4236515eaf97a02d36aff9cea42dbd43ba37aefb4bd503b8e1572e984be8`;
- `iter050-heldout-algebra` id `10336376608`, digest `sha256:2719f3d7ffef49a0eb41116e6835bc589d5d8660c450e9595e0ba78fc89eee7e`;
- `iter050-null-controls` id `10336249411`, digest `sha256:c68fcb34b37a9272b25d363c9772cb72b63c7d5a4e76404074b6a110a5e51d8c`;
- `iter050-authority-freeze` id `10336184435`, digest `sha256:d60a5de8e56044bfccdf278c3ca2dce2ddedbe43b6ec6dbef8078ba6fafcc69a`.

## Decisive implementation audit

### 1. Frozen scientific object was never executed

The aggregate explicitly records `lorentzian_vertex_evaluated=false`. The backend lane cloned the pinned backend and inspected `tools/vertex-amplitude.c`, but deliberately stopped before build/runtime/table setup and before any vertex evaluation.

The workflow implemented `primary-algebra` and `heldout-algebra` lanes rather than the preregistered `primary-summand` and `heldout-summand` lanes. Neither lane evaluated five Lorentzian vertices, phase/weights, or the fixed five-vertex summand. Therefore the workflow could not satisfy either frozen summand predicate even in principle.

This is stronger than a mere backend transport/build failure: the frozen contraction was omitted from the implementation. Classification is therefore `INVALID_IMPLEMENTATION`, not scientific FAIL and not scientific PASS.

### 2. Held-out recoupling implementation changed the frozen label meaning

ITER048 had already established the exact finite SU(2) basis for the frozen 0/1 intertwiner labels using

`wigner_6j(1/2, 1/2, a, 1/2, 1/2, b)` with `a,b ∈ {0,1}`,

yielding finite values for `(0,0)`, `(0,1)`, `(1,0)`, `(1,1)`.

ITER050 instead converted the frozen intertwiner entries with `S(ii[n])/2`. Thus the held-out label `1` was changed to `1/2`, producing triangle-relation errors in two of the five diagnostic tuples. Those errors are implementation artifacts, not scientific failures of the source recoupling object.

### 3. `authority-freeze` contained a false-positive SHA check

The lane used `git ls-remote <repository> <raw-commit-SHA>` and classified authority PASS from return code alone. The artifact records return code 0 with empty stdout for both repositories. That command therefore did not itself prove the requested SHA existed. The backend SHA was separately established by the clone/checkout lane, and the author-code SHA remains independently qualified by ITER049, but the ITER050 authority predicate was not mechanically implemented as frozen.

### 4. Null controls remain valid but are non-dispositive

The workflow correctly preserved the no-retuning/no-amplitude-selection/TEX_LITERAL-rejection locks. These controls do not rescue the absent production contraction.

## Scientific consequence

No Lorentzian fixed-configuration summand value exists from ITER050. No primary/held-out comparison is scientifically available. No finite/non-finite inference may be drawn from this run.

The exact new upstream blocker is executable runtime realization of the pinned `sl2cfoam-next` backend with source-required `wigxjpf/fastwigxj` tables and an actual finite single-vertex call. The backend documentation provides an Ubuntu build path, supports `BLAS=system`, and exposes `bin/vertex-amplitude` taking ten doubled spins, five doubled intertwiners, Immirzi parameter and `Dl`.

## Authorized next gate

A separate prospectively frozen **minimal pinned-backend runtime executability gate** is authorized. It must:

- preserve backend SHA `052e4346028870bd76f69a3034e6cae8defb8f7f`;
- use the backend's own documented dependency/table setup rather than a surrogate implementation;
- build with a source-supported BLAS choice (system BLAS is allowed by the pinned Makefile);
- initialize actual `.3j` and `.6j` fastwigxj tables;
- run the backend's own `vertex-amplitude` executable on a pre-frozen low-spin `gamma=1.2`, `Dl=0` smoke configuration;
- independently verify executable identity, table/runtime identity, and output finiteness;
- treat build/table/runtime failure as infrastructure BLOCKED/FAIL, not physical failure;
- make no five-vertex or refinement claim.

Only after such a runtime gate PASS may the fixed-sector five-vertex summand be re-preregistered with the corrected source-level SU(2) label semantics.

## Claim ceiling

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory remains `UNFORMED / 0%`.

Still unauthorized: unbounded ten-face summation, shell convergence, coarse↔fine amplitude equality, zero-face deletion, Eq.(29)/Lambda, one-step TNR, full Eq.(27), bridge derivation, candidate formation, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`.