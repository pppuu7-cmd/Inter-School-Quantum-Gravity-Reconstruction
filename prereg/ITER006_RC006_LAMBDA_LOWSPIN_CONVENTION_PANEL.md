# Preregistration — ITER006 RC006 low-spin Lambda convention panel

Frozen before implementation/production on 2026-09-13.

## Objective
Freeze the exact published conventions required to turn the qualified Buffenoir–Roche Lambda coefficient formula into a finite low-spin numerical implementation. This gate is deliberately prior to numerical coefficient evaluation; no convention may be chosen after seeing numerical results.

Immutable source: Buffenoir–Roche `math/9910147v1`, SHA256 `316ab7737a6e201c9c5d988326077358b562e6f5d47cfffbf1d2935cdd9389bc`.

## Independent lanes
1. `principal-labels`: exact definition of the principal-unitary label set S and the map between `(X0,X1)` and `(m,rho)`, including allowed domains/equivalences.
2. `q-ribbon`: exact definitions/conventions for q-number/q-dimension and ribbon factors `v_X` used by `formlamb6j`.
3. `q-binomial-boundary`: exact q-binomial/Pochhammer convention needed by the source boundary formulas `lambdaboundary` and `symetryLambda`.
4. `controls`: exact source anchors for unitarity/conjugation, selection-rule zeros, boundary/symmetry formulas and at least one special-value/Plancherel control usable prospectively.

Each lane records exact source line anchors and bounded excerpts. Generic mentions do not count.

## Frozen interpretation
- `BR_LAMBDA_LOWSPIN_CONVENTIONS_QUALIFIED`: all four lanes expose sufficient exact convention/control information to freeze a numerical low-spin panel with no fitted/free convention.
- `BR_LAMBDA_LOWSPIN_CONVENTIONS_PARTIAL`: formula chain is executable but at least one convention/control mapping needed for the numerical panel remains unresolved.
- `BR_LAMBDA_LOWSPIN_CONVENTIONS_BLOCKED`: the primary source does not provide enough convention information and another explicit primary authority is required.
- Fetch/archive/parser failure is `INFRASTRUCTURE_SOURCE_EXTRACTION_FAIL`.

Green CI is not scientific PASS; terminal classification requires consuming all raw lane artifacts.

## Scope locks
Even `QUALIFIED` authorizes only a separate prospectively preregistered finite low-spin Lambda numerical panel. It does not authorize Eq.(29), amplitude/refinement bridge credit, `BRIDGE_DERIVED`, candidate theory, or `NEW_PHYSICS_FOUND`.
