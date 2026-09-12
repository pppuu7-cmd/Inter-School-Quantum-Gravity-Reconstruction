# ITER006 — asymmetric-boundary DVD2/DVD3 finite shell sum PASS

Date: 2026-09-12

## Scope

Prospectively frozen asymmetric-boundary robustness test of the source-labelled Lorentzian EPRL two-vertex amplitudes `DVD2` and `DVD3`.

Frozen boundary:
- `j=(1,2,2,2)`
- `j'=(1,2,2,1)`
- `i=t=i'=t'=1`
- finite auxiliary cutoffs `D={0,1,2}`
- gamma `{0.5,1.2,2.0}`

No DVD2/DVD3 equality and no convergence direction were preregistered.

## Provenance

- preregistration: `protocol/ITER006_DVD_ASYMMETRIC_BOUNDARY_PREREG.json`
- mixed-B4 prerequisite: run `34708641965`, PASS 3/3
- amplitude run: `34708800382`
- source-manifest: PASS
- aggregate job: `103593818869`
- aggregate artifact: `10301904355`
- aggregate artifact digest: `sha256:80ef723faff1fde9a7e6865a53cb316306166aa7076ac68aaa113c5c8f0081f6`
- classification: `DVD_ASYMMETRIC_FINITE_SHELL_SUM_AGGREGATE_PASS`
- repeat max relative difference: `0.0` for every gamma

## Results

### gamma = 0.5

| D | DVD2 | DVD3 | DVD2/DVD3 | DVD2 relative increment | DVD3 relative increment |
|---:|---:|---:|---:|---:|---:|
| 0 | 7.054920017927195e-5 | 1.175295907849978e-4 | 0.600268 | — | — |
| 1 | 1.4348309242276066e-4 | 2.3135517937372972e-4 | 0.620185 | 0.508310 | 0.491995 |
| 2 | 2.139049610710966e-4 | 3.008590700657641e-4 | 0.710981 | 0.329220 | 0.231018 |

### gamma = 1.2

| D | DVD2 | DVD3 | DVD2/DVD3 | DVD2 relative increment | DVD3 relative increment |
|---:|---:|---:|---:|---:|---:|
| 0 | 1.984613680342901e-6 | 3.3057787362148153e-6 | 0.600347 | — | — |
| 1 | 4.000049892607925e-6 | 6.916710326963572e-6 | 0.578317 | 0.503853 | 0.522059 |
| 2 | 5.5184545742073735e-6 | 9.035419864245794e-6 | 0.610758 | 0.275150 | 0.234489 |

### gamma = 2.0

| D | DVD2 | DVD3 | DVD2/DVD3 | DVD2 relative increment | DVD3 relative increment |
|---:|---:|---:|---:|---:|---:|
| 0 | 6.103837202749626e-8 | 1.0166226066891141e-7 | 0.600403 | — | — |
| 1 | 1.2239211184291574e-7 | 2.212672394201547e-7 | 0.553142 | 0.501288 | 0.540545 |
| 2 | 1.6315965287115186e-7 | 2.9044488217968727e-7 | 0.561758 | 0.249863 | 0.238178 |

## Allowed observations

1. The exact DVD2=DVD3 equality of the fully symmetric D0 boundary is broken decisively: `DVD2/DVD3 ≈ 0.6003` at all three tested gamma values.
2. Therefore the symmetric D0 equality is boundary-specific rather than a generic identity between the source-labelled amplitudes.
3. Although no stabilization direction was preregistered for this asymmetric test, **descriptively** the D1→D2 relative increment is smaller than D0→D1 for both DVD2 and DVD3 at all three gamma values.
4. That descriptive recurrence motivates, but does not itself count as, a held-out asymmetric-gamma pattern test.

## Claim lock

This is asymmetric-boundary robustness of finite shell sums only. It is not a convergence proof, refinement map, cylindrical consistency result, continuum limit, bridge derivation, novelty or new physics.
