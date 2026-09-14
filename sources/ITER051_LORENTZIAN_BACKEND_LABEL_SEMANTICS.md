# ITER051 source record — Lorentzian backend label semantics

Date: 2026-09-14

Purpose: outcome-independent source/provenance audit for the active pinned-backend runtime front and any later separately preregistered bounded five-vertex retry. This record is not a scientific gate and does not authorize a five-vertex result.

## Frozen sources

### Authors' executable 5→1 implementation

`PietropaoloFrisoni/Monte_Carlo_spinfoams@84b375f2a2e0d29b44dd8820953553624bb007a3`

`src/vertex_renormalization_EPRL_MC.jl` uses `HalfInt` physical spin/intertwiner variables. The source-defined recoupling path converts tuple indices back to physical intertwiners before calling `wigner6j(...)`.

`src/utilities.jl` defines:

```julia
@inline function from_index_to_intertwiner(tuple, index)
  return tuple[1][1] + index - 1
end
```

Thus the physical intertwiner range advances in unit spin steps. For the frozen all-`j=1/2` 4-valent sectors, the relevant physical intermediate intertwiners are `i=0` and `i=1`, consistent with the already qualified ITER048 finite basis

`wigner_6j(1/2,1/2,a,1/2,1/2,b)`, `a,b in {0,1}`.

### Pinned Lorentzian backend standalone tool

`qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`

`tools/vertex-amplitude.c` explicitly documents CLI arguments

`folder Immirzi two_j1,...,two_j10 two_i1,...,two_i5 Dl`

and parses them into

```c
sl2cfoam_dspin two_js[10];
sl2cfoam_dspin two_is[5];
```

before calling

```c
sl2cfoam_vertex_amplitude(two_js, two_is, Dl);
```

Therefore this standalone C interface uses doubled labels.

## Exact conversion rule

When the same source physical labels are sent through `bin/vertex-amplitude`:

- physical `j=1/2` -> `two_j=1`;
- physical `i=0` -> `two_i=0`;
- physical `i=1` -> `two_i=2`.

Do **not** divide the ITER048/ITER049 physical `0/1` intertwiner labels by two. Do **not** pass physical `i=1` as C CLI `two_i=1`; that would represent physical `i=1/2`, i.e. a different object.

## Consequence for ITER050 history

ITER050's held-out algebra diagnostic used `S(ii[n])/2` inside the SU(2) Wigner-6j calculation. That changed physical `i=1` into `1/2` and produced triangle-relation errors. This remains an implementation artifact and cannot be read as a physical obstruction.

## Consequence for a future five-vertex retry

Only if ITER051 terminally validates the exact pinned runtime may a successor gate be opened. If that successor uses the standalone C `vertex-amplitude` tool, all source physical labels must be converted by the doubled-label rule above. If it instead uses the authors' Julia `vertex_compute` tensor interface, it must preserve the native `HalfInt`/tensor-index semantics and document the exact component extraction.

No conversion may be selected after inspecting amplitude values.

## Claim ceiling

This record establishes only interface/label identity. It does not establish a Lorentzian amplitude value, a five-vertex contraction, convergence, a refinement map, bridge credit or a candidate theory.