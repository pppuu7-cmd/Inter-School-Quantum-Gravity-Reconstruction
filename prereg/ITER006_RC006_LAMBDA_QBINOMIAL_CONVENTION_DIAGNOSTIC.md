# Preregistration — ITER006 RC006 Lambda q-binomial convention diagnostic

Frozen before diagnostic implementation on 2026-09-13.

## Purpose
The already-preregistered low-spin Lambda convention panel requires an exact q-binomial/Pochhammer convention for the published `lambdaboundary` / `symetryLambda` controls. The production panel located those formulas but did not itself expose an explicit definition. This diagnostic is +0 scientific credit and must not convert a generic notation hit into a convention qualification.

Immutable source: Buffenoir–Roche `math/9910147v1`, SHA256 `316ab7737a6e201c9c5d988326077358b562e6f5d47cfffbf1d2935cdd9389bc`.

## Frozen lanes
1. `lexical-definition`: enumerate every source occurrence of q-binomial notation and any nearby explicit `binom`, q-Pochhammer, factorial, q-number, or notation-definition statement. No bounded-hit cap before enumeration.
2. `dependency-map`: independently enumerate all source definitions of `[x]`, `[x]_k`, `[k]!`, Pochhammer/infinite-product conventions, plus every `lambdaboundary`/`symetryLambda` occurrence; report whether an explicit source equation equates the q-binomial notation to those primitives.

## Frozen outputs
- `SOURCE_EXPLICIT_QBINOMIAL_CONVENTION_FOUND` only if the immutable source itself contains an explicit equality/definition fixing the q-binomial used in the boundary formula.
- `SOURCE_QBINOMIAL_CONVENTION_NOT_EXPLICIT` if boundary q-binomial notation is present but no explicit defining equality is found.
- `INFRASTRUCTURE_SOURCE_EXTRACTION_FAIL` only for fetch/archive/parser failure.

This diagnostic cannot authorize the low-spin numerical panel, Eq.(29), bridge credit, candidate theory, or any retuning. If the source convention is not explicit, a separately preregistered authority-resolution gate is required.