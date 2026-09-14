# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**. Bridge credit remains zero.

## RC006 unchanged

RC006 numerical retry remains unauthorized. No Eq.(27), Eq.(29), Lambda, one-step TNR, bridge or candidate-theory claim is opened by the current Lorentzian work.

## Lorentzian multi-vertex lineage

ITER047 remains SCIENTIFIC PASS — `LORENTZIAN_5TO1_ASSEMBLY_AUTHORITY_PASS`, run `34808646324`.

ITER048 remains terminal **SCOPED BLOCKED — `LORENTZIAN_EQ11_ROUTING_REFERENCE_AUTHORITY_BLOCKED_SOURCE_INDEX_INCONSISTENCY`**. It is not retrofitted.

ITER049 remains terminal **SCIENTIFIC PASS — `LORENTZIAN_AUTHOR_CODE_ROUTING_RECONCILIATION_PASS`**, run `34811866640`. The pinned authors' executable path uniquely selects `COMMENT_REPAIR`: fourth Wigner-6j uses `rbl/rbr`; fifth uses `rCDl/rCDr`, hence `i9` rather than the duplicated Eq.(11) `i8`, without amplitude fitting.

## ITER050 terminal INVALID_IMPLEMENTATION

Preregistration commit: `61908806492f5053c83cf45a50ea54bc5905797b`.

The corrected Actions run `34815939847` was infrastructure-green, but raw artifacts and implementation audit show the preregistered scientific object was never executed. The workflow implemented `primary-algebra`/`heldout-algebra` diagnostics instead of the frozen `primary-summand`/`heldout-summand`; `lorentzian_vertex_evaluated=false`; no five Lorentzian vertices, phase/weights or bounded five-vertex summand were evaluated.

The held-out algebra lane also incorrectly divided frozen integer intertwiner labels `0/1` by two, whereas ITER048 had already qualified the exact basis `wigner_6j(1/2,1/2,a,1/2,1/2,b)` with `a,b in {0,1}`. Its triangle errors are therefore implementation artifacts, not negative physics.

Terminal classification:

**`INVALID_IMPLEMENTATION — LORENTZIAN_BOUNDED_FIXED_CONFIGURATION_CONTRACTION_NOT_EXECUTED`**.

Durable report commit: `51cd9302f25f642fdb0ed85539fb7421bdbba213`.

No fixed-configuration Lorentzian summand value exists from ITER050.

## Active ITER051 — exact pinned backend runtime executability

Preregistration: `prereg/ITER051_LORENTZIAN_PINNED_BACKEND_RUNTIME_EXECUTABILITY_2026-09-14.md`, commit `f013d4800a306ce4c1d9838d2a63c781c16f864d`.

Frozen backend: `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f` using the backend's own documented Ubuntu dependency/table path, `BLAS=system`, `OMP=0`, unchanged default Y-map, source-named `wigxjpf-1.13` and `fastwigxj-1.4.1`, and the backend's own `bin/vertex-amplitude` executable.

Frozen smoke point before execution:
- `gamma=1.2`;
- ten doubled spins `1,1,1,1,1,1,1,1,1,1`;
- five doubled intertwiners `0,0,0,0,0`;
- `Dl=0`.

Stage A builds exact backend + source-required `.3j/.6j` tables. Only if Stage A passes do four independent Stage-B lanes run in parallel: `vertex-smoke-A`, `vertex-smoke-B`, `runtime-identity`, `negative-control`. The two smoke processes must agree within the prospectively frozen reproducibility tolerance.

### Run 1 pre-science infrastructure failure

Run `34817480937` stopped immediately after transporting `wigxjpf-1.13.tar.gz`: after changing directory to `work/backend/ext`, the workflow addressed the repository evidence folder with one too few `..` components. No dependency compilation, table generation, backend build or vertex evaluation occurred.

Classification: `INFRASTRUCTURE_FAIL_PRE_SCIENCE — OUTPUT_PATH_ORCHESTRATION_ONLY`. Durable note commit: `9736be6cffd08ec5f06591917f0022ebf210eda7`.

The control-only repair changes only evidence/output relative paths. Scientific contract, backend/dependency versions, build flags, tables, smoke point, tolerance and verdict criteria are unchanged. Repair commit: `426c053fe826d4d2cace74622785d63543804948`.

Authoritative recovery run: **`34817642670`**. At the last recovery sync its `build-runtime` job `103891696203` was queued.

## Exact next action

Consume run `34817642670` only after terminal evidence exists. Do not use partial vertex values.

- If build reaches the source-documented recent-GCC fastwigxj 9j-only failure, the ITER051 prereg prospectively permits only that exact 9j-only infrastructure repair, because the pinned backend does not use 9j.
- If some other exact dependency/table/runtime object cannot be realized, terminalize the exact infrastructure/dependency blocker; do not substitute a surrogate amplitude.
- If Stage A and all Stage-B lanes pass, manually audit raw artifacts before scientific PASS. Only then may a new separately preregistered bounded five-vertex retry be opened, restoring the correct ITER048 `0/1` SU(2) label semantics and actually calling the pinned Lorentzian backend.

## Persistent locks

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory `0 / UNFORMED`.

Full unbounded ten-face summation, shell convergence, coarse↔fine amplitude equality, zero-face deletion, Eq.(29)/Lambda, one-step TNR, full Eq.(27), bridge derivation and candidate-theory construction remain unauthorized. Still false: `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`.
