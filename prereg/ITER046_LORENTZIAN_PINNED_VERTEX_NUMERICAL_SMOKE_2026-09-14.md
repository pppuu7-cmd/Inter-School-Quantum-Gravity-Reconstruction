# Preregistration — ITER046 pinned Lorentzian EPRL vertex numerical smoke

Date frozen: 2026-09-14

## Inherited status

ITER044 source-qualified the 1→5/5→1 Lorentzian EPRL Pachner route. ITER045 closed `LORENTZIAN_1TO5_IMPLEMENTATION_READINESS_PASS` after a duplicate-detection-only technical recovery. Full multi-vertex contraction, coarse↔fine equality and bridge credit remain unauthorized.

## Frozen backend

Official backend: `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`.

Frozen build mode: Ubuntu hosted runner, system OpenBLAS (`BLAS=system`), `OMP=0`, default Y-map of the pinned backend. No backend patch affecting science is permitted. Transport/build-only repairs may be made if they do not alter backend source, compiler science flags, input amplitudes or acceptance predicates.

## Frozen numerical inputs

Immirzi parameter: `gamma=1.2`.

Boundary face spins: all ten `j=1`, passed to the C CLI as doubled spins `two_j=(2,2,2,2,2,2,2,2,2,2)`.

Shell cutoff: `Dl=0`.

Primary intertwiner tuple: all five `i=0`, doubled `two_i=(0,0,0,0,0)`.

Held-out intertwiner tuple, frozen before primary result: all five `i=1`, doubled `two_i=(2,2,2,2,2)`.

Each tuple is evaluated twice in the same compiled environment. No expected amplitude magnitude/sign is preregistered; this gate tests executable source-faithful numerics, finiteness and deterministic repeatability only.

## Independent lanes

1. `numerical-primary-heldout`: build the exact pinned backend from upstream instructions/dependencies and compute primary + held-out amplitudes twice each.
2. `vertex-face-map`: algorithmically map the five refined 4-simplices of the 1→5 complex to their ten face-spin slots and verify every internal triangle belongs to exactly three refined 4-simplices while every boundary triangle belongs to exactly two.
3. `backend-source-control`: verify pinned SHA plus source hashes/API signatures for `vertex-amplitude.c`, `src/vertex.c`, `inc/sl2cfoam.h`, Makefile and quickstart; verify CLI expects exactly 10 doubled face spins, 5 doubled intertwiners and `Dl`.
4. `semantic-null`: reject the claims that (a) finite single-vertex amplitude implies 1→5 amplitude convergence, (b) deterministic repeatability implies refinement invariance, (c) `Dl=0` convergence implies shell convergence, or (d) a held-out finite amplitude authorizes parameter retuning.

Use `fail-fast:false`.

## Frozen numerical PASS predicates

N1. Both primary and held-out CLI evaluations terminate normally.
N2. All four returned values parse as finite real doubles.
N3. Primary repeat difference <= `1e-12 * max(1,abs(A_primary))`.
N4. Held-out repeat difference <= `1e-12 * max(1,abs(A_heldout))`.
N5. No source/backend/input retuning occurs between primary and held-out calls.

No condition on amplitude sign, nonzero magnitude, ratio, agreement between primary and held-out, or closeness to any post-hoc target is allowed.

## Terminal outcomes

- `LORENTZIAN_PINNED_VERTEX_NUMERICAL_SMOKE_PASS` iff all four lanes pass frozen predicates.
- `SCIENTIFIC_FAIL` only if the exact compiled pinned backend executes but N1–N5 fail for scientific/numerical reasons.
- `INFRASTRUCTURE_FAIL` if dependencies/build/transport prevent the pinned executable from being evaluated.
- `BLOCKED` if source/API inconsistency prevents a source-faithful implementation without modifying frozen science.

A PASS authorizes only a separately preregistered bounded multi-vertex assembly/contraction gate using the same pinned backend and 1→5 topology. It does not authorize full ten-face summation or bridge credit.

## Locks

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory `0 / UNFORMED`; no `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, `ALL_KNOWN_SCHOOLS_FAIL`; zero-face deletion remains BLOCKED.