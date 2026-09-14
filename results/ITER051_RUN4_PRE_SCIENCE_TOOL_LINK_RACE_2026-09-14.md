# ITER051 run 4 — pre-science tool-link dependency race

Date: 2026-09-14

Workflow run: `34817878894`, production head `e3118247bc8d89dbb259b719f89ada0189ee6a7b`.

Classification: **INFRASTRUCTURE_FAIL_PRE_SCIENCE — PINNED_MAKEFILE_PARALLEL_TOOL_LINK_RACE**.

This is not a Lorentzian numerical/physical failure. No `vertex-amplitude` value was evaluated; Stage-B smoke/identity/control lanes were correctly skipped.

## What succeeded before the failure

The exact pinned backend `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f` was checked out successfully.

Source-named external dependencies were transported and compiled:

- `wigxjpf-1.13.tar.gz` SHA256 `90ab9bfd495978ad1fdcbb436e274d6f4586184ae290b99920e5c978d64b3e6a`; wigxjpf build PASS.
- `fastwigxj-1.4.1.tar.gz` SHA256 `0a4171c18dfd0ad5689c9456c873a9edd7a2a2af8e15805e880b800e8f766550`; fastwigxj build PASS.

The prospectively allowed recent-GCC fastwigxj 9j repair was **not needed and not applied**.

Source-documented tables were generated successfully:

- `.3j`, `max-E-3j=50`, 3,478,762 entries;
- `.6j`, `max-E-6j=40`, 9,366,820 entries.

The backend source objects compiled and `lib/libsl2cfoam.so` linking began successfully. The failure occurred when `bin/vertex-fulltensor` was linked in parallel, with unresolved references to `sl2cfoam_init_conf`, `sl2cfoam_vertex_fullrange`, and `sl2cfoam_free`.

Build artifact: `iter051-runtime-build`, artifact id `10336917125`, digest `sha256:b48c266a16d81994f87ca4617e8c1da7946bac36bfd81ada6d3b4e5042ee04b9`.

## Source-level diagnosis

The pinned backend Makefile defines:

```make
$(LIBDIR)/libsl2cfoam.so: $(OBJS)
    $(CC) -shared $(OBJS) -o $@ ...

$(BINDIR)/%: $(TOOLSDIR)/%.c $(OBJS)
    $(CC) ... $< -Llib/ ... -lsl2cfoam ...

tools: lib $(TOOLS)
```

Thus `tools` names `lib` as a sibling prerequisite, but each individual tool target depends only on source plus `$(OBJS)`, not explicitly on `lib/libsl2cfoam.so`. Under the run4 invocation `make -j2 BLAS=system OMP=0 tools`, GNU make may start a tool linker concurrently with the shared-library link once the common object prerequisites exist. The observed log does exactly that: `CC lib/libsl2cfoam.so` and then `CC bin/vertex-fulltensor`, followed by unresolved backend symbols.

This is build orchestration/dependency ordering, not a modification of the EPRL implementation.

## Exact allowed repair

Preserve all frozen scientific/runtime identities and all backend source bytes. Change only build scheduling:

1. `make -j1 BLAS=system OMP=0 lib`
2. `make -j1 BLAS=system OMP=0 tools`

This enforces completion of the pinned shared library before any standalone tool link. It changes no compiler scientific flags, backend SHA, dependency version, table content, Y-map, gamma, spins, intertwiners, `Dl`, reproducibility threshold or verdict criteria.

The ITER051 preregistration remains authoritative and unchanged.