# ITER051 — pinned Lorentzian backend runtime executability

Date: 2026-09-14

## Terminal classification

**PASS — `LORENTZIAN_PINNED_BACKEND_RUNTIME_PASS`**.

This is an executable-runtime prerequisite PASS only. It proves that the exact pinned Lorentzian EPRL backend can be built, initialized with its source-required SU(2) tables, and used through its own standalone single-vertex interface at the prospectively frozen smoke point.

It does **not** establish a five-vertex contraction, refinement-map derivation, unbounded spin sum, shell convergence, coarse↔fine equality, bridge credit, or candidate theory.

## Frozen contract

Preregistration:

`prereg/ITER051_LORENTZIAN_PINNED_BACKEND_RUNTIME_EXECUTABILITY_2026-09-14.md`

Prereg commit: `f013d4800a306ce4c1d9838d2a63c781c16f864d`.

Frozen backend:

`qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`.

Frozen runtime choice:

- `BLAS=system`;
- `OMP=0`;
- `ADD_CFLAGS=''`;
- no `RHO_GJ` / alternative Y-map override;
- `wigxjpf-1.13`;
- `fastwigxj-1.4.1`;
- source-documented `.3j` table `max-E-3j=50`;
- source-documented `.6j` table `max-E-6j=40`.

Frozen smoke configuration:

- `gamma=1.2`;
- ten doubled spins `two_js=(1,1,1,1,1,1,1,1,1,1)` = ten physical `j=1/2`;
- five doubled intertwiners `two_is=(0,0,0,0,0)` = five physical `i=0`;
- `Dl=0`.

The pinned backend Julia wrapper independently establishes that the physical all-`j=1/2` four-valent intertwiner range is `i=0..1`, so the frozen all-zero smoke tuple is inside the backend domain before its amplitude value is inspected.

## Pre-science repair history

No scientific criterion or runtime input was changed during repairs.

### Run 1

Run `34817480937`: `INFRASTRUCTURE_FAIL_PRE_SCIENCE — OUTPUT_PATH_ORCHESTRATION_ONLY`.

The workflow stopped at an incorrectly addressed evidence directory before dependency compilation. Durable note: `results/ITER051_RUN1_PRE_SCIENCE_INFRASTRUCTURE_FAIL_2026-09-14.md`, commit `9736be6cffd08ec5f06591917f0022ebf210eda7`.

### Run 4

Run `34817878894`: `INFRASTRUCTURE_FAIL_PRE_SCIENCE — PINNED_MAKEFILE_PARALLEL_TOOL_LINK_RACE`.

Exact wigxjpf/fastwigxj builds and table generation succeeded. The pinned Makefile declares `tools: lib $(TOOLS)` while individual tool targets depend on the common object set rather than explicitly on `lib/libsl2cfoam.so`; the parallel `make -j2 ... tools` invocation allowed a tool linker to race the shared-library linker. No vertex value was evaluated.

Durable note: `results/ITER051_RUN4_PRE_SCIENCE_TOOL_LINK_RACE_2026-09-14.md`, commit `15579da53f17f124a06ef620f7cea446110120ec`.

Control-only repair commit: `52150ba71882c04091edbfac16e6f55ca0d244fe`. It changed only build scheduling to serial `make ... lib` then serial `make ... tools`; backend source bytes, build science flags, versions, tables, frozen CLI, tolerances and verdict criteria were unchanged.

The source-documented recent-GCC fastwigxj 9j repair was never needed and never applied.

## Authoritative production run

Run: **`34818301950`**.

Production head: **`52150ba71882c04091edbfac16e6f55ca0d244fe`**.

Jobs:

- build-runtime `103893774566` — PASS;
- vertex-smoke-A `103894699020` — PASS;
- negative-control `103894699027` — PASS;
- vertex-smoke-B `103894699038` — PASS;
- runtime-identity `103894699162` — PASS;
- aggregate `103894836697` — PASS.

## Stage A — exact build/runtime identity

PASS.

Dependency archive identities:

- `wigxjpf-1.13.tar.gz` SHA256 `90ab9bfd495978ad1fdcbb436e274d6f4586184ae290b99920e5c978d64b3e6a`;
- `fastwigxj-1.4.1.tar.gz` SHA256 `0a4171c18dfd0ad5689c9456c873a9edd7a2a2af8e15805e880b800e8f766550`.

`fastwigxj_initial_rc=0`; no 9j repair was applied.

Runtime manifest:

- compiler `gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0`;
- `bin/vertex-amplitude` SHA256 `b4f8f536645b3fe6bc55830040f624140eefca02a3b960b9940b2564a7876e26`;
- `lib/libsl2cfoam.so` SHA256 `a539c968afde2a7ec397b2fa7184f9dd036042b82ff2ec5d8026c2b6881b71fc`;
- `data_sl2cfoam/table_50.3j` SHA256 `73d9170de4f04b776923106c5c6ea1bbb70cf2e62a14d24b83cda31194567e6e`;
- `data_sl2cfoam/table_40.6j` SHA256 `de1a29d0252c3c1ebf51b96d7fdebe7f21587ee65dcbc3864070774c14704b72`.

The standalone binary dynamically resolves the built `libsl2cfoam.so`, system BLAS/OpenBLAS, MPC/MPFR/GMP/quadmath and the expected runtime libraries.

Build artifact:

- `iter051-runtime-build` id `10336669907`;
- digest `sha256:f357f01e2aa370db20701bbced8cf7f6d03d6c43751ba5399584dd343820454b`.

## Stage B — independent smoke processes

Both processes used the same frozen runtime manifest and independently launched the backend's own `bin/vertex-amplitude` executable.

### Smoke A

- return code `0`;
- finite `true`;
- runtime identity `true`;
- amplitude **`1.34499311005e-09`**;
- PASS.

Artifact `iter051-vertex-smoke-A` id `10337188950`, digest `sha256:57f43eed88bcf9be731454e621906a64319c61780a2c480d9cb7e7369c50bade`.

### Smoke B

- return code `0`;
- finite `true`;
- runtime identity `true`;
- amplitude **`1.34499311005e-09`**;
- PASS.

Artifact `iter051-vertex-smoke-B` id `10336917839`, digest `sha256:dea816efb712fb6a7a1f6563fd784cbbc1fdaa1905c59513e59de62da46be175`.

### Reproducibility

Absolute difference: **`0.0`**.

Frozen tolerance:

`1e-12 + 1e-10*max(|A|,|B|)` = approximately `1.000000134499311e-12`.

Therefore `REPRODUCIBILITY_PASS=true` by a wide margin.

## Identity and negative controls

`runtime-identity` PASS:

- exact backend SHA match;
- binary/library/table hashes match manifest;
- build flags match;
- frozen CLI matches.

Artifact id `10337610524`, digest `sha256:b27252ff5aff9050314fa347e756df13c8ee5823d447b8c6215f247c63f6aa03`.

`negative-control` PASS:

- changed gamma rejected;
- changed `Dl` rejected;
- changed spin tuple rejected;
- deliberately wrong binary hash rejected.

Artifact id `10337268822`, digest `sha256:350ed79d86f0245b9bf021ce475009ab4558133741e1c0c95b77cc4a5f4c5703`.

Aggregate artifact id `10337373597`, digest `sha256:842a9868229de381de47ede61556bb2efe274b986ec3eed75e3e070ed9a63016` records `LORENTZIAN_PINNED_BACKEND_RUNTIME_PASS`. Manual raw-artifact audit agrees with the frozen predicates; the verdict is not based on green CI alone.

## New structural fact

The exact pinned Lorentzian `sl2cfoam-next` realization is now demonstrably executable in the hosted environment, including its source-required SU(2) table runtime. The previous inability to evaluate a Lorentzian vertex in ITER050 was therefore an implementation/orchestration defect, not evidence that the backend or the frozen low-spin vertex object is unavailable.

The scoped numeric amplitude above is only a smoke witness at one pre-frozen local vertex configuration. It is not a five-vertex physical result.

## Separate source-mapping finding discovered during the runtime gate

Outcome-independent source audit produced `sources/ITER051_LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK.md`, commit `b918058a35cbaf66456aa57b19576104c4d8c2f3`.

Literal Eq.(11) and the pinned authors' executable code differ in several local vertex global-intertwiner slots beyond the already known fifth-6j `i8/i9` issue. Those discrepancies are invisible in the all-zero smoke point but material in the alternating `0/1` held-out sector.

Therefore ITER051 PASS does **not** directly authorize immediate execution of the old ITER050 held-out contraction.

## Authorized next gate

The highest-information next gate is a separately prospectively frozen **`LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK` authority gate**.

It must reconcile, without amplitude fitting:

1. the five literal Eq.(11) local `A_v` intertwiner lists;
2. the exact arXiv code-name crosswalk `rBCl=i1 ... rIbr=i15`;
3. the authors' executable `vertex_compute` local range comments and tensor-axis order;
4. the Wigner-6j pre-contraction mapping from left to right recoupling bases;
5. the pinned `sl2cfoam-next` `(i1,...,i5)` / doubled-label API.

Only after that mapping is source-qualified may a repaired bounded primary/held-out five-vertex summand gate be preregistered and executed.

## Claim ceiling

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory remains **UNFORMED / 0%**.

Still unauthorized: unbounded ten-face summation, shell convergence, coarse↔fine equality, zero-face deletion, full Eq.(27), Eq.(29)/Lambda, one-step TNR, bridge derivation, candidate formation, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`.