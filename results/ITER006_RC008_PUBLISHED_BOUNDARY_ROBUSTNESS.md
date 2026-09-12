# ITERATION 006 — RC-008 Published Boundary-State Robustness Audit

Date: 2026-09-12  
GitHub Actions run: `34666680657`  
Status: `SUCCESS / SOURCE-DATA ROBUSTNESS AUDIT / AMPLITUDE REPRODUCTION STILL OPEN`

## Scope

This audit uses the boundary-specific renormalization fixed points `alpha_*` and vertex-translation critical values `alpha_c` reported by Bahr & Steinhaus in *Hypercuboidal renormalization in spin foam quantum gravity* (arXiv:1701.02311, Sec. V.1–V.2).

It is not a recomputation of the 16-hypercuboid path integral.

Published values used:

| coarse boundary state | `alpha_*` | `alpha_c` |
|---|---:|---:|
| `X=Y=Z=T=1` | `0.628` | `0.606670` |
| `X=Y=Z=1, T=3` | `0.662` | `0.549942` |
| `X=3, Y=Z=T=1` | `0.614` | `0.557808` |
| `X=3, Y=5, Z=T=1` | `0.607` | `0.539846` |

## Fixed-point robustness across boundary/truncation choices

For the four reported `alpha_*` values:

- mean: `0.62775`;
- standard deviation: `0.02445`;
- coefficient of variation: `0.03894` (~`3.9%`);
- full range: `0.055`;
- maximum relative deviation from the mean: `0.05456` (~`5.5%`).

Thus the one-parameter RG fixed point is qualitatively fairly stable across the four reported coarse boundary choices, while not being numerically identical.

## `alpha_*` is not identical to the symmetry-restoration diagnostic `alpha_c`

Across the same four boundary states:

- median absolute gap `|alpha_* - alpha_c|`: `0.061673`;
- median relative gap: `0.10651` (~`10.7%`);
- maximum absolute gap: `0.112058`;
- all four pairs are non-identical.

The descriptive Pearson correlation over only four points is `0.0531`; because `n=4`, this number is reported only as a warning against treating numerical proximity in one boundary state as evidence of a universal identity.

## ISQGR interpretation

RC-008 remains attractive as an independent amplitude/refinement target because it already contains:

`coarse boundary data -> geometric embedding map -> refined amplitude -> observable matching -> effective parameter flow`.

However, the source data show that two distinct diagnostics must remain distinct:

1. the RG matching fixed point `alpha_*`;
2. the approximate vertex-translation/symmetry critical value `alpha_c`.

They may be nearby in some boundary configurations, but the published values do not justify an identity `alpha_* = alpha_c`.

This is directly relevant to ISQGR methodology: a robust scale-flow object must not be promoted to a physical/gauge-restoration object merely because both occur in the same parameter region.

## Next decisive test

Reconstruct the restricted hypercuboid amplitude and reproduce at least two coarse/refined volume-variance curves, then freeze the inferred `alpha' -> alpha` map and test it on a held-out boundary state.

That would convert RC-008 from a source-data audit into an independent amplitude-level refinement gate for BH-004/BH-004B.

## Claim lock

- published-data audit only;
- no fresh path-integral amplitude has yet been evaluated;
- quantum-cuboid truncation is not full EPRL-FK gravity;
- fixed-point stability here is not a continuum-limit proof;
- no `NEW_PHYSICS`, `BRIDGE_DERIVED`, or candidate-theory promotion follows from this audit.
