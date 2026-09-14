# Preregistration — ITER051 pinned Lorentzian backend runtime executability

Date frozen: 2026-09-14

## Inherited terminal state

ITER049 remains terminal SCIENTIFIC PASS — `LORENTZIAN_AUTHOR_CODE_ROUTING_RECONCILIATION_PASS`.

ITER050 is terminal `INVALID_IMPLEMENTATION — LORENTZIAN_BOUNDED_FIXED_CONFIGURATION_CONTRACTION_NOT_EXECUTED`. Its green Actions run did not evaluate any Lorentzian vertex and therefore created no fixed-configuration summand value.

The scientific five-vertex contraction remains unopened until the exact pinned backend can be built, initialized with source-required tables and used through its own executable interface.

## Frozen question

Can the exact pinned `sl2cfoam-next` backend be realized in a clean hosted Ubuntu runtime and execute its own standalone Lorentzian EPRL single-vertex tool at a pre-frozen low-spin point without any surrogate amplitude implementation?

This is an executable-runtime prerequisite gate. It is not a five-vertex refinement test and earns no bridge credit.

## Frozen source/runtime authority

Backend repository and commit:

`qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`.

Pinned source files already inspected before implementation:

- `README.md` git blob `ff8f05051f8584c7b2962a33eb9304ca872f7021`;
- `QUICKSTART_Ubuntu.md` git blob `159a00710c6b2cdb53f7c78dc78778af0a536efd`;
- `Makefile` git blob `d5c5c987632ab69ec12800e08e2b5d88c31a4a3f`;
- `tools/vertex-amplitude.c` git blob `12fb7fa321cd7668b2c0d8161e8e2c064e5c455e`.

The pinned backend documentation requires GMP/MPFR/MPC, quadmath, wigxjpf, fastwigxj, OpenMP/optional disabling, and BLAS. The pinned Makefile explicitly supports `BLAS=system`; this gate freezes `BLAS=system` and `OMP=0` to avoid introducing MKL as an extra runtime dependency. This does not change the backend Y-map definition; no `ADD_CFLAGS=-DRHO_GJ` override is allowed.

The pinned Ubuntu quickstart names:

- `wigxjpf-1.13`;
- `fastwigxj-1.4.1`;
- `.3j` table generated with `hash_js --max-E-3j=50`;
- `.6j` table generated with `hash_js --max-E-6j=40`.

The quickstart explicitly permits disabling the known unused fastwigxj 9j compilation block on recent GCC if required. That exact infrastructure-only repair is prospectively allowed and must be reported. No 3j/6j implementation may be changed.

## Frozen smoke configuration

Use the backend's own `bin/vertex-amplitude` tool with its documented doubled-spin/doubled-intertwiner CLI semantics:

- table folder: runtime-generated source-authorized `.3j` and `.6j` tables;
- Immirzi `gamma=1.2`;
- ten doubled boundary spins `two_js = (1,1,1,1,1,1,1,1,1,1)` corresponding to ten `j=1/2` spins;
- five doubled intertwiners `two_is = (0,0,0,0,0)`;
- `Dl=0`.

This smoke point is frozen before execution. No alternative spin/intertwiner point may be substituted after seeing output.

## Staged gate and independent lanes

### Stage A — exact backend build/runtime bundle

- verify exact backend checkout SHA;
- install only generic system dependencies plus source-named wigxjpf/fastwigxj versions;
- if and only if required by recent-GCC fastwigxj 9j compilation, apply the prospectively allowed quickstart 9j-only build repair and record it;
- generate the documented `.3j` and `.6j` tables;
- build backend tools with `make BLAS=system OMP=0`;
- record hashes of `bin/vertex-amplitude`, `lib/libsl2cfoam.so`, table files, exact compiler version and dependency source archive hashes;
- upload the runtime bundle/evidence for dependent lanes.

Stage A build/transport failure is `INFRASTRUCTURE_FAIL`, never scientific FAIL.

### Stage B — parallel independent checks after Stage A

1. `vertex-smoke-A`: run the frozen tool call once and require a parseable finite double.
2. `vertex-smoke-B`: independently run the exact same frozen tool call from a fresh process using the same frozen bundle and require a parseable finite double.
3. `runtime-identity`: verify binary/library/table hashes match the Stage-A manifest, exact backend SHA is preserved and no `RHO_GJ` override or surrogate executable is present.
4. `negative-control`: prove that output was produced by the backend's own `vertex-amplitude` binary; reject a deliberately wrong binary/hash identity and reject any changed gamma, `Dl`, spins or intertwiners. This lane need not deliberately corrupt the scientific output.

The final aggregate waits for all Stage-B lanes.

## Frozen predicates

`BACKEND_BUILD_PASS`: exact pinned backend and source-named 3j/6j dependencies build successfully using the frozen supported build choice; required tables exist; backend executable and shared library are present and hashed.

`VERTEX_SMOKE_A_PASS`: frozen tool invocation exits successfully and emits exactly one parseable finite numeric amplitude after backend diagnostic text is separated/recorded.

`VERTEX_SMOKE_B_PASS`: independent repeat satisfies the same predicate.

`REPRODUCIBILITY_PASS`: A and B agree within absolute tolerance `1e-12 + 1e-10*max(|A|,|B|)`. The tolerance is frozen before output.

`RUNTIME_IDENTITY_PASS`: backend checkout, executable/library/table identities and frozen CLI inputs match the Stage-A manifest; no alternative Y-map compile flag, no source-code amplitude surrogate and no post-output parameter change.

`NEGATIVE_CONTROL_PASS`: deliberately wrong runtime identity and changed-input sentinels are rejected by the manifest/control logic.

## Terminal classifications

- `LORENTZIAN_PINNED_BACKEND_RUNTIME_PASS` iff Stage A and every Stage-B predicate PASS.
- `LORENTZIAN_PINNED_BACKEND_RUNTIME_BLOCKED_DEPENDENCY` if the source-authorized backend cannot be built or initialized because an exact required dependency/table object cannot be transported or realized.
- `LORENTZIAN_PINNED_BACKEND_RUNTIME_NUMERICAL_FAIL` only if the exact backend is successfully instantiated but the frozen source-defined tool call reproducibly returns non-finite/unparseable output or inconsistent repeated values.
- `INVALID_IMPLEMENTATION` if the workflow does not actually use the pinned backend/tool/tables or changes the frozen inputs/identity/criteria.
- infrastructure transport/setup failures before backend execution are non-physical.

## Consequence of PASS

PASS authorizes only a new separately preregistered repair/retry of the bounded five-vertex fixed-configuration summand. That successor must restore the ITER048 exact SU(2) intertwiner label semantics (`a,b ∈ {0,1}` directly, not halved), call the actual pinned Lorentzian vertex executable for each source-defined local vertex, preserve `COMMENT_REPAIR`, and retain the frozen primary/held-out sectors.

PASS does not authorize an unbounded ten-face sum, shell convergence, coarse↔fine equality, zero-face deletion, refinement-map derivation, bridge credit or candidate formation.

## Claim locks

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory remains `UNFORMED / 0%`.

Still unauthorized: `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`, full Eq.(27), Eq.(29)/Lambda, one-step TNR, unbounded Lorentzian refinement.