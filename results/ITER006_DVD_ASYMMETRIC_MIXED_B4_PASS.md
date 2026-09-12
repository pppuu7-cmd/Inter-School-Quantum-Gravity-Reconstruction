# ITER006 — asymmetric-boundary mixed-spin B4 prerequisite PASS

Date: 2026-09-12

## Scope

This validates representative mixed-spin `B4` numerical primitives required by the prospectively frozen asymmetric DVD2/DVD3 boundary. It does not evaluate the asymmetric DVD amplitudes themselves.

Pinned kernel: `qg-cpt-marseille/sl2cfoam-next` commit `052e4346028870bd76f69a3034e6cae8defb8f7f`.
Frozen prerequisite threshold: max fast-vs-accurate relative error `<= 1e-5`.

## Provenance

- preregistration: `protocol/ITER006_DVD_ASYMMETRIC_BOUNDARY_PREREG.json`
- run: `34708641965`
- aggregate job: `103593486884`
- aggregate artifact: `10302557098`
- artifact digest: `sha256:3a129d21d3d00c9ee4ec2c90e27c63a5ef40f0fe34c66e50ccb81410963d772b`
- classification: `B4_ASYMMETRIC_MIXED_AGGREGATE_PASS`

Each gamma lane tested six preselected source-relevant mixed-spin configurations and produced 52 fast-vs-accurate comparisons.

| gamma | comparisons | max relative error |
|---:|---:|---:|
| 0.5 | 52 | 1.33712e-9 |
| 1.2 | 52 | 7.04148e-9 |
| 2.0 | 52 | 2.49464e-8 |

All three lanes passed, with the worst error still roughly 400 times below the frozen threshold.

## Decision

`B4_ASYMMETRIC_MIXED_AGGREGATE_PASS = YES`.

This closes the numerical-primitive prerequisite for the already preregistered asymmetric boundary `j=(1,2,2,2)`, `j'=(1,2,2,1)`, `i=t=i'=t'=1`. It provides no direct refinement, continuum, bridge, novelty, or new-physics credit.
