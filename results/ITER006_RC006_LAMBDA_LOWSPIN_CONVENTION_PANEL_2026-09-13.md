# ITER006 RC006 low-spin Lambda convention panel — terminal result

Date: 2026-09-13

## Frozen gate
Preregistration commit: `e6096df9a399305f8749480847077629c3f181e4`.
Frozen source: Buffenoir–Roche, arXiv:`math/9910147v1`, SHA256 `316ab7737a6e201c9c5d988326077358b562e6f5d47cfffbf1d2935cdd9389bc`.
Implementation/head: `e361f96ad200d8cdd2620810a03324969c8d43b9`.
Authoritative run: `34747075146`.

Jobs:
- principal-labels `103696850297`
- controls `103696850531`
- q-ribbon `103696850785`
- q-binomial-boundary `103696850848`
- aggregate `103696875774`

Artifacts:
- principal-labels `10314348162`, digest `sha256:fd862b57f8d50a4f1f7f7c1ee96d315369ab855d52ac510af04e6c21aebe7621`
- controls `10314083694`, digest `sha256:fca994f5596a6e237c30194ab6d2e8013e9f2130c41d21929ea396be05d96e21`
- q-ribbon `10313923937`, digest `sha256:878d49740c8b553f32af048ccaf65cc2fee7134c06238988bfdd355c01ef2e53`
- q-binomial-boundary `10314521554`, digest `sha256:abee0f83b7fc8b753ec0c1dc1f776c7a70d7300658282b857ed0c552efb498a0`
- aggregate `10314348181`, digest `sha256:e8bc4c4bdd07486906fdffa73bcac366d9787d1004ee846a30a657057d791385`

The aggregate reports four modes present and four evidence signals true, but deliberately sets `automatic_scientific_pass=false`; the classification below comes from raw source anchors and not from green CI.

## Raw source audit
The principal-label lane gives the exact principal-unitary convention
`2 X0 + 1 = m + i rho`, `2 X1 + 1 = -m + i rho`, with `m in 1/2 Z`, `rho in (-pi/hbar,pi/hbar]`, hence `m_X=X0-X1` and `i rho_X=X0+X1+1`. This is sufficient to freeze numerical label generation without a fitted map.

The q/ribbon lane gives `q=exp(-hbar)` and the chosen central ribbon eigenvalue `v_K = exp(2 pi i K) q^{-2K(K+1)}` (including the source sign convention), together with the source q-dimension notation used in the Lambda identities.

The boundary lane gives explicit finite q-binomial formulas for diagonal boundary Lambda coefficients, source label `lambdaboundary`, and the independent symmetry identity `symetryLambda`, including the factor `v_X0/v_X1`. These provide source-faithful finite low-spin numerical targets and cross-checks without coefficient fitting.

The controls lane independently exposes selection-rule zeros, the fundamental `formlamb6j` route, boundary/symmetry identities, unitarity/conjugation material and Plancherel/special-value controls. The alternative `lambda3j` normalization factors from BR1 are not needed for the already-qualified fundamental route.

## Scientific classification
`BR_LAMBDA_LOWSPIN_CONVENTIONS_QUALIFIED`

This closes the convention/boundary blocker and authorizes a separate prospectively preregistered finite low-spin numerical Lambda gate. It does not itself numerically validate general `Lambda^{BC}_{AD}`, Eq.(29), q-EPRL amplitude/refinement bridge credit, `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, or candidate-theory construction.
