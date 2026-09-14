# Preregistration — ITER040 RC006 central-component validity-boundary diagnostic

Date frozen: 2026-09-14

## Status inherited

ITER039 is permanently terminal `RC006_EQ27_BOUNDED_CENTRAL_COMPONENT_CLOSURE_FAIL`. ITER040 is diagnostic only. It cannot change ITER039, remove failed tuples, relax `2e-12 / 5e-9 / 5e-8` thresholds, fit phases/normalizations, or authorize full Eq.(27), Eq.(29), Lambda, TNR, bridge credit, or candidate theory.

## Question

Do ITER039 failures concentrate outside the exact earlier bounded-component validation panel and/or at the SU(2)_k root-of-unity tensor-product boundary where the unprojected tensor product contains channels above the finite physical cutoff? Separately, are R/R^-1 and dual-contraction failures reproducible under identical code and orientation without held-out retuning?

## Frozen definitions

For a central physical-spin tuple `(J+,J-,l)`, numerical twice-spin labels are `(a,b,c)=(2J+,2J-,2l)`.

- `prior_iter027_pair_scope`: ordered `(a,b)` is exactly one of the frozen ITER027 pairs `(1,1),(2,1),(2,2),(4,2)`; no symmetrization is added after results.
- `root_tensor_boundary`: `a+b > k`. This flags tensor products whose naive highest output spin exceeds the finite SU(2)_k cutoff even though individual admissible channels may remain physical. It is a diagnostic flag, not a correction or exclusion rule.
- frozen residual thresholds remain those of ITER039.

## Lanes

### A — scope census
Reconstruct the complete primary+held-out ITER039 central tuple panel. Report counts and failure-independent membership in `prior_iter027_pair_scope` and `root_tensor_boundary`. PASS means census is complete and both panels are represented; it is not a physics PASS.

### B — primary boundary map
Recompute all primary residuals unchanged. Produce a 2x2-style breakdown by prior-scope flag and root-boundary flag, including tuple count, failure count, max R/R^-1 residual and max dual residual. Do not alter tuple membership. Diagnostic-complete iff every primary tuple is accounted for.

### C — held-out boundary map
Same as B with identical code/thresholds for held-out tuples. No held-out-specific convention or threshold.

### D — orientation/reproduction controls
On prospectively selected lexicographically first nontrivial tuples in each available boundary class, recompute: direct-source qbar identity, dual residual, R/R^-1 residual, and swapped `(a,b)` R/R^-1 residual where admissible. Report differences only. Also verify the frozen ITER039 negative-control tuple remains distinguishable. No correction is inferred from swap behavior.

## Aggregate

`RC006_CENTRAL_COMPONENT_VALIDITY_BOUNDARY_DIAGNOSTIC_COMPLETE` requires A-D to execute completely with no infrastructure failure. The aggregate must report patterns descriptively; it must not relabel ITER039 PASS.

A subsequent gate is allowed only if it is source-authority driven. If failures correlate with root-of-unity quotient/trace-zero structure, the next admissible gate is a source audit for the correct projector/quotient-domain R and dual identities before any new numerical closure attempt. If no such interpretable boundary exists, RC006 expanded-central closure remains scientifically failed/open without immediate retry.
