# ITER047 — Lorentzian EPRL 5→1 assembly authority

Date: 2026-09-14

## Terminal classification

**SCIENTIFIC PASS — `LORENTZIAN_5TO1_ASSEMBLY_AUTHORITY_PASS`**.

This gate closes the source/assembly authority layer for a bounded fixed-cutoff 5→1 Lorentzian EPRL implementation. It does **not** compute the full multi-vertex amplitude, prove Pachner/refinement invariance, or earn bridge credit.

## Frozen provenance

- prereg commit: `87ca4ffc54ac061288c1d9ad5db6e1559a273b5b`
- workflow/production head: `2adacb08693365cf6eba0fdf4605e772d5f38b70`
- authoritative run: `34808646324`
- jobs: backend-map-shell `103865407445`; formula-2302 `103865407524`; formula-1803 `103865407527`; assembly-null `103865407568`; aggregate `103865459089`
- artifacts:
  - formula-2302 `10333916785`, digest `sha256:0748b4be055151dde203062ceae05f19e7e1b85b8fe2bb994103f724e640ca50`
  - formula-1803 `10333389196`, digest `sha256:903aa46ce967cee96ebbbaf4796e4a28550bbd0fb9cdb16e99ebd3af13dbb46`
  - backend-map-shell `10333334393`, digest `sha256:a96dcade318c6110860b1c1adcf8ed31327508520323efb6e2b51dad41948b8a`
  - assembly-null `10333431697`, digest `sha256:65cfd28dbfd873ccb62edf60347ce3e4f32b996472ee0b61fc17c43540f2f21e`
  - aggregate `10333309252`, digest `sha256:27ed8392ecabe0156f17dcb0ea707b7b090b174bac7cea257982548229f040cdd`

## Source-formula authority — PASS

arXiv `2302.00072` provides the general spin-foam amplitude as a sum over bulk face spins and edge intertwiners with face, edge and vertex amplitudes, and explicitly describes sl2cfoam-next as the single-vertex backend used inside the gluing/summation procedure.

More importantly, its Eq.(11) gives the specific vertex-renormalization / 5→1 amplitude with:

- ten bulk spins `j1...j10`;
- fifteen internal intertwiners `i1...i15`;
- five explicit Lorentzian EPRL vertex amplitudes `A_v` with routed local arguments;
- five 6j-symbol factors;
- the explicit phase `(-1)^(2 phi)`;
- the required bulk summation structure.

The surrounding source text identifies five vertices, five boundary edges, ten bulk edges, ten boundary faces and ten bulk faces.

Independently, arXiv `1803.00835`, Eq.(70), gives the 1→5 Pachner amplitude with sums over ten internal spins/intertwiners, products of face/edge dimension factors and five EPRL-FK vertex amplitudes. The two frozen sources therefore agree on the source classes required for a source-faithful bounded implementation.

`ASSEMBLY_FORMULA_SOURCE_PASS=true`.

## Backend global→local map and held-out shell transport — PASS

Exact backend remains `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`.

The global 1→5 incidence was mapped deterministically to local vertex slots using lexicographically sorted triangle/tetrahedron labels, frozen without consulting amplitudes. Backend API provenance confirms the ten-face/five-intertwiner vertex interface.

Frozen `Dl=1` transport, with the same `gamma=1.2` and ten `j=1` inputs as ITER046:

- primary `i=0`: `2.54326111467e-10` on both repetitions;
- held-out `i=1`: `-1.82359605133e-09` on both repetitions.

All values are finite and repeat within the frozen tolerance. Their sign, magnitude and ratio to ITER046 `Dl=0` are **not** PASS predicates and are not interpreted as shell convergence.

`BACKEND_GLOBAL_LOCAL_MAP_PASS=true`; `DL1_TRANSPORT_PASS=true`.

## Null controls — PASS

The frozen controls continue to reject:

- a bare product of five vertex values as the full 5→1 amplitude when required internal sums/weights are absent;
- cutoff/profile behaviour as a refinement map;
- `Dl=0`/`Dl=1` finiteness as shell convergence;
- numerical agreement as authority for an otherwise unsourced ordering.

`ASSEMBLY_NULL_PASS=true`.

## Consequence

A separately preregistered **bounded fixed-cutoff multi-vertex implementation/contraction** is now scientifically admissible. Prefer the authors' published reference implementation when available rather than rewriting Eq.(11) from scratch.

Still not authorized: unbounded ten-face summation, amplitude/refinement invariance, bridge credit, zero-face deletion, or candidate-theory construction.

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory = `0 / UNFORMED`.
