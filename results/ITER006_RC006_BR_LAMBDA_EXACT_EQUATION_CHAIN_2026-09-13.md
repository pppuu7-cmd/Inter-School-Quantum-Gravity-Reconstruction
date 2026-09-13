# ITER006 RC006 Buffenoir–Roche Lambda exact-equation chain — terminal result

Date: 2026-09-13

## Frozen gate
Preregistration commit: `35beb34283d3492a44a20cb378a9d5261e86b407`.
Frozen source: Buffenoir–Roche, arXiv:`math/9910147v1`, SHA256 `316ab7737a6e201c9c5d988326077358b562e6f5d47cfffbf1d2935cdd9389bc`.

Initial implementation head `ef72c0d007a86d9aa3fa3b59146c6bbf896f626a`, run `34746854011`, failed before scientific extraction because the immutable e-print payload was not a tar archive although its SHA matched exactly. Classification: `INFRASTRUCTURE_SOURCE_EXTRACTION_FAIL`; no science was changed.

Minimal unpacking-only repair head: `362143199837e8e6b7081f00b28da885b18d088a`.
Authoritative retry run: `34746885145`.
Jobs:
- analytic-6j `103696325188`
- macro-grammar `103696325200`
- definition-equalities `103696325281`
- normalization-domain `103696325294`
- aggregate `103696342737`

Artifacts:
- macro grammar `10314870348`, digest `sha256:3660b0d0031df1fed4ce219c232139811096fdfee5bf3f4f8eaff35ad8c8e1b9`
- analytic/6j `10314755898`, digest `sha256:e11f9f7fcf4ff8c2ee6bb9ebd509be23774fcbcac0bd493f6242cc9d8000251b`
- definition equalities `10314128321`, digest `sha256:07f99359aaad0a2963f8f655300b1e1d6b9c5ab0b8715a71dace5c5a0778d4d2`
- normalization/domain `10313928683`, digest `sha256:f589c77bf27bf457db2ad1db5c3b3f3601c3c0c10dea1bee09346279b51cb7c0`
- aggregate `10314422640`, digest `sha256:c8b8ffdf675ee01f78aadadea483650e8cb00959f03db2483088e219839161d3`

The aggregate machine evidence has all four modes present and all evidence signals true, but automatic scientific PASS was deliberately disabled; the classification below comes from consuming the raw source anchors.

## Raw source audit
The source defines the Lambda coefficient grammar explicitly and then gives the principal-unitary representation action in terms of `Lambda^{BD}_{EC}(X_0X_1)`.

The fundamental coefficient formula, source label `formlamb6j`, is explicit:
`Lambda^{BC}_{AD}(X_0X_1)` is a finite sum over `X_2` of a product of two source-defined `6j(1)` coefficients multiplied by the stated ribbon-factor ratio. This is an actual coefficient definition, not a downstream fit.

The same source independently defines the analytic continuation used for `6j(1)`. It gives the normalization factor and the continued 6j value as a terminating `{}_4 Phi_3`, discusses the complex square-root/sign prescription, gives selection rules and the domains of both families of `6j(1)`, and states their explicit expressions. The source also gives principal-unitary labels `(X_0,X_1)` and the `(m,rho)` parametrization/Plancherel context.

An alternative `lambda3j` expression later in the paper refers to BR1 for normalization factors `N^(A)`. That does not block the fundamental `formlamb6j` route, because the latter is already explicit in terms of source-defined `6j(1)` plus ribbon factors and does not require those alternative `N^(A)` factors.

The same source supplies independent coefficient constraints/special cases, including unitarity/conjugation, Plancherel identities, boundary formulas and recurrence/Casimir relations. These can serve as prospective numerical controls.

## Scientific classification
`BR_LAMBDA_EXACT_EQUATION_CHAIN_QUALIFIED`

This closes the source-formula/convention executability blocker for a finite low-spin Lambda implementation. It authorizes a separate prospectively preregistered low-spin numerical coefficient gate using the fundamental `formlamb6j` route and source-defined controls.

It does **not** authorize Eq.(29), the q-EPRL amplitude/refinement bridge, `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, or candidate-theory construction. It does not rewrite the historical pair-sign/braid-projection FAIL.
