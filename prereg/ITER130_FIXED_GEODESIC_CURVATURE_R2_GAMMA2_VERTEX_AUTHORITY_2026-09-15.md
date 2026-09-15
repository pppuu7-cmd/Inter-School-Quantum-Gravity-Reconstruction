# ITER130 preregistration — fixed-geodesic curvature R2 / Gamma2 nonlinear vertex authority

Date: 2026-09-15
Gate: `ITER130_FIXED_GEODESIC_CURVATURE_R2_GAMMA2_VERTEX_AUTHORITY`

## Motivation frozen before nonlinear-vertex derivation

ITER129 closes graph derivative ceilings but exact pole-relevant numerator jets for the Gaussian M/G families require explicit second-order geometric vertices. Starting a symbolic jet generator with only derivative counts would be under-specified.

ITER130 freezes and validates the exact conventions for:

- the second-order Christoffel symbol `Gamma2[h,h]` entering the source-qualified Fröb `chi2` kernel;
- the second-order scalar-curvature operator `R2[h,h]` entering the Gaussian F/M families.

## Frozen conventions

- `g_mn = delta_mn + kappa h_mn` with no independent `kappa^2` metric field;
- indices raised/lowered by `delta_mn` in perturbative coefficients;
- Euclidean Fourier convention `partial_m -> i q_m` for later momentum vertices;
- geometric definitions

  `Gamma^r_mn = 1/2 g^{rs}(partial_m g_sn + partial_n g_sm - partial_s g_mn)`,

  `R = g^{mn}(partial_r Gamma^r_mn - partial_n Gamma^r_mr + Gamma^r_rs Gamma^s_mn - Gamma^r_ns Gamma^s_mr)`

  with one fixed Riemann-sign convention used consistently.

## Required predicates

A. Expand `g^{-1}` through `O(kappa^2)` and derive source-convention `Gamma1` and `Gamma2` explicitly.

B. Verify that, because `g=delta+kappa h`, `Gamma2` arises from the `-kappa h^{rs}` inverse-metric correction multiplying the first derivative of `h`; no independent second-order metric field is present.

C. Expand scalar curvature through

`R = kappa R1 + kappa^2 R2 + O(kappa^3)`

and derive an explicit position-space `R2` formula before integrations by parts.

D. Verify `R1 = partial_m partial_n h^mn - Box h` in the frozen sign convention, matching ITER122 up to the already frozen Fourier/global-sign convention.

E. Construct a bilinear momentum-space representation of `R2` with two graviton momenta `p,k` and total external momentum `q=p+k`. Preserve Bose symmetry under exchange of the two graviton legs.

F. Derive the bilinear momentum representation of `Gamma2` needed in the `chi2` line kernel and verify symmetry in its lower Christoffel indices.

G. Produce symbolic tests of:

- inverse-metric multiplication through `O(kappa^2)`;
- Christoffel lower-index symmetry;
- `R2` graviton-leg Bose symmetry;
- agreement of the linear `R1` vertex with ITER122;
- derivative budgets `D(R2)=2`, `D(Gamma2)=1` used by ITER129.

H. Keep total-derivative rearrangements separate: the generator must use one canonical unreduced vertex representation so graph-level integration-by-parts identities can be tested later rather than silently assumed.

I. No loop pole, `B1`, EDT target or desired cancellation may be used to select a vertex representation.

## Frozen classifications

- `PASS_SCOPED_R2_GAMMA2_VERTEX_AUTHORITY_SYMBOLICALLY_CLOSED` if A-I pass with reproducible symbolic formulas/tests.
- `PASS_SCOPED_POSITION_VERTICES_CLOSED_MOMENTUM_TENSOR_GENERATOR_OPEN` if A-D/G pass but E-F require a separate tensor-generator implementation.
- `FAIL_SCOPED_VERTEX_CONVENTION_MISMATCH` if R1/ITER122 consistency fails.

## Controls

- `RIEMANN_SIGN_CONVENTION_CONTROL`
- `INTEGRATION_BY_PARTS_VERTEX_SWAP_CONTROL`
- `SECOND_ORDER_METRIC_FIELD_CONTROL`
- `BOSE_SYMMETRY_CONTROL`
- `DERIVATIVE_BUDGET_CONTROL`
- `TARGET_VERTEX_SELECTION_CONTROL`

## Claim ceiling

A PASS supplies exact nonlinear geometric vertices only. It does not compute a loop pole, `B1`, noncancellation, EDT fit, bridge, new physics or candidate theory.