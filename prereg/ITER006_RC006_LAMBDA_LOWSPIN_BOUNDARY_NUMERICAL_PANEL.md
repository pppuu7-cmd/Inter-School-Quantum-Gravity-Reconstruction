# Preregistration — ITER006 RC006 finite low-spin Lambda boundary numerical panel

Frozen on 2026-09-13 before implementation/production.

## Scientific objective
Numerically instantiate the published Buffenoir–Roche diagonal-boundary coefficient `lambdaboundary` in a finite low-spin principal-unitary panel, using only conventions already source-qualified by the previous gate. This is a boundary/special-case coefficient gate, not yet the general `formlamb6j` reconstruction and not Eq.(29).

Frozen source: Buffenoir–Roche arXiv:`math/9910147v1`, SHA256 `316ab7737a6e201c9c5d988326077358b562e6f5d47cfffbf1d2935cdd9389bc`.

## Frozen formula/conventions
For `q=exp(-hbar)`, `2X0+1=m+i rho`, `2X1+1=-m+i rho`, evaluate source Eq. `lambdaboundary`

`Lambda^(B,C)_(B+C) = sum_{k=-B}^B q^(-2 k (X0+X1+1)) * qbinom(B+C+X0-X1,B+k) * qbinom(B+C-X0+X1,B-k) / [(-1)^(2B) qbinom(2B+2C,2B)]`.

Use the generalized finite-product q-binomial for non-negative integer lower index `n`:
`qbinom(x,n)=prod_{j=0}^{n-1} [x-j]/[n-j]`, with `[z]=(q^z-q^-z)/(q-q^-1)`. An independent arithmetic route must evaluate the same `[z]` as `sinh(hbar*z)/sinh(hbar)` and rebuild the finite product independently.

No coefficient, phase, sign, threshold or label may be changed after production results are seen.

## Frozen panel
Eight lanes, all within `rho in (-pi/hbar,pi/hbar]`:
1. `H02_B0_C1_M0_R035`: hbar=.2, B=0, C=1, m=0, rho=.35 (exact B=0 identity control).
2. `H02_B05_C05_M0_R035`: hbar=.2, B=.5, C=.5, m=0, rho=.35.
3. `H02_B05_C1_M05_R080`: hbar=.2, B=.5, C=1, m=.5, rho=.80.
4. `H02_B1_C05_M05_R035`: hbar=.2, B=1, C=.5, m=.5, rho=.35.
5. `H04_B05_C05_M1_R035`: hbar=.4, B=.5, C=.5, m=1, rho=.35.
6. `H04_B1_C1_M0_R080`: hbar=.4, B=1, C=1, m=0, rho=.80.
7. `H04_B1_C05_M15_R035`: hbar=.4, B=1, C=.5, m=1.5, rho=.35.
8. `H04_B05_C1_M15_R080`: hbar=.4, B=.5, C=1, m=1.5, rho=.80.

Lanes 7–8 deliberately probe the source selection/boundary edge where factors may force zeros; they are not to be removed if numerically awkward.

## Frozen predicates
For every structurally admissible lane:
- direct q-exponential route vs independent sinh route absolute discrepancy <= `1e-11` and relative discrepancy <= `1e-10` when magnitude > `1e-10`;
- `rho -> -rho` must agree with complex conjugation to <= `1e-11` absolute;
- finite values only, no NaN/Inf;
- denominator magnitude >= `1e-14` or lane is `NUMERICAL_DOMAIN_BLOCKED`, not scientific FAIL.

Additional controls:
- lane 1 must equal `1+0i` to absolute error <= `1e-12`;
- for every half-integer-B lane with nonzero correct coefficient, deleting the published `(-1)^(2B)` denominator sign is a deliberately wrong control and must differ from the correct value by >= `1e-6` in at least three such lanes;
- lanes whose source selection factor is forbidden (`A=B+C`, `A-|m| notin N_0`) must have coefficient magnitude <= `1e-11`; admissible lanes are not required nonzero.

## Frozen scientific classifier
- `BR_LAMBDA_LOWSPIN_BOUNDARY_NUMERICAL_QUALIFIED_SCOPED`: all non-blocked lanes satisfy route/conjugation controls, B=0 identity passes, selection-forbidden lanes satisfy zero control, and >=3 wrong-sign controls are rejected.
- `SCIENTIFIC_FAIL_BR_LAMBDA_LOWSPIN_BOUNDARY_NUMERICAL`: structurally valid/source-domain lanes violate a frozen scientific predicate.
- `NUMERICAL_DOMAIN_BLOCKED`: a published denominator is numerically singular under the frozen finite panel; do not alter labels post hoc.
- implementation/fetch/serialization failure before predicates is `INFRASTRUCTURE_FAIL`.

## Scope locks
Even a PASS qualifies only this finite diagonal-boundary Lambda implementation. It does not establish the general `formlamb6j` coefficient, Eq.(29), an amplitude/refinement bridge, `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, or candidate theory. Historical braid-sensitive negative results remain unchanged.
