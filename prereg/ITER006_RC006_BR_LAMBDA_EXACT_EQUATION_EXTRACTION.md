# Preregistration — ITER006 RC006 Buffenoir–Roche Lambda exact-equation extraction

Frozen before implementation/production on 2026-09-13.

## Objective
Resolve the `QEPRL_LAMBDA_AUTHORITY_CHAIN_PARTIAL` blocker by extracting the exact source equations and convention data in Buffenoir–Roche `math/9910147v1` needed to map their Lambda coefficients to the EPRL `Lambda^{JM}_{NL}(alpha)` object without fitted or invented choices.

## Immutable source
`math/9910147v1` source SHA256 must equal `316ab7737a6e201c9c5d988326077358b562e6f5d47cfffbf1d2935cdd9389bc`.

## Four independent evidence lanes
1. `macro-grammar`: extract exact definitions of all Lambda macros and their index/argument arity.
2. `definition-equalities`: extract non-macro source contexts in which Lambda coefficients occur in explicit equalities/definitions.
3. `analytic-6j`: extract exact contexts connecting the coefficients to analytically continued q-6j/q-Racah/Askey–Wilson objects.
4. `normalization-domain`: extract conventions, orthogonality/normalization conditions and principal-unitary label domains needed for numerical evaluation.

Every lane records source line numbers and verbatim bounded excerpts. Generic abstract-level mentions do not count as formula anchors.

## Frozen interpretation
- `BR_LAMBDA_EXACT_EQUATION_CHAIN_QUALIFIED`: the raw source exposes an exact coefficient-definition chain plus sufficient convention/domain information to define a finite low-spin numerical implementation with no free fitted convention.
- `BR_LAMBDA_EXACT_EQUATION_CHAIN_PARTIAL`: relevant exact equations exist but at least one normalization/domain/mapping ingredient remains unresolved.
- `BR_LAMBDA_EXACT_EQUATION_CHAIN_BLOCKED`: the source does not expose enough information to define the EPRL coefficient without importing another primary source or an arbitrary convention.
- Fetch/archive/parser failure is `INFRASTRUCTURE_SOURCE_EXTRACTION_FAIL`, not a scientific negative result.

The aggregate workflow only prepares evidence. Terminal scientific classification requires consuming all raw lane artifacts; green CI is not PASS.

## Claim locks
No outcome of this source gate authorizes Eq.(29), bridge credit, `BRIDGE_DERIVED`, candidate-theory construction or `NEW_PHYSICS_FOUND`. Only `QUALIFIED` may authorize a separate prospectively preregistered finite low-spin coefficient numerical gate.
