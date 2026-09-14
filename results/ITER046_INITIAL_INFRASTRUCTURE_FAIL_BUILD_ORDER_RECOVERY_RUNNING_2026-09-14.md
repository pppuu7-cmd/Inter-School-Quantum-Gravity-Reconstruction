# ITER046 — initial infrastructure failure; build-order recovery running

Date: 2026-09-14

## Initial run classification

**`INFRASTRUCTURE_FAIL PRE-SCIENCE`** for the numerical lane only. The frozen Lorentzian EPRL amplitudes were not evaluated, so there is no scientific numerical FAIL.

- prereg commit: `f648ceff1082b98f44b8e1715e530c529862de62`
- original production head: `86eac7ecd3eeb069b414c6dfd6a74edf0b5f840b`
- original run: `34808304690`
- jobs: face map `103864431152`; numerical `103864431259`; backend source control `103864431342`; semantic null `103864431377`; aggregate `103864534957`

Validated control artifacts:

- semantic null `10334041954`, `sha256:d3dd2c1691e52672897e798add45f0ce96f3542b56799f4089e91a91136af31c`
- vertex face map `10333498333`, `sha256:dfc5e769515fca0a036284cca9892a8fe70c80d3ef7b6d59042b4e809ed15094`
- backend source control `10333199568`, `sha256:98025c30ff53a8c3c0f26e75630e8d5d8355b82bd13b45f2f22874e0ee17ac88`
- aggregate `10333957322`, `sha256:6e00d6169a54fbd7382eb6981a5fa13c59fcb5ecc31c134fe1a5fa84c7fc388f`

## Causal failure

The exact pinned backend and both external Wigner libraries compiled successfully far enough to produce `lib/libsl2cfoam.so`. The command `make BLAS=system OMP=0 -j2` then started test linking in parallel and `bin/lib_test` failed with undefined references to `sl2cfoam_init_conf` and `sl2cfoam_vertex_fullrange` before any `vertex-amplitude` CLI invocation.

Therefore N1–N5 were not evaluated.

## Minimal repair

The frozen backend SHA, scientific flags and all inputs remain unchanged. Repair commit `3b770691c33385cf10a6007d260db6f589d5dac0` changes build ordering only:

1. `make BLAS=system OMP=0 lib`
2. then `make BLAS=system OMP=0 tools`

No backend source patch, Y-map change, spin/intertwiner change, shell change, threshold change or amplitude-target condition is introduced.

Recovery run `34808387189`, numerical job `103864666854` is authoritative for the pending N1–N5 evaluation.

Until it terminalizes, bounded multi-vertex successor remains unauthorized. `refinement_map_derived=false`; `bridge_credit=false`; candidate theory = `0 / UNFORMED`.