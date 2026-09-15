# ITER122 preregistration — linearized curvature / genuine-defect kernel reduction

Date: 2026-09-15
Gate: `ITER122_LINEARIZED_CURVATURE_GENUINE_DEFECT_KERNEL_REDUCTION`

## Motivation frozen before symbolic evaluation

ITER121 leaves two genuine line-defect inputs for the single logarithmic output `B_1`:

`J_R = int ds Box_perp R`,
`J_S = int ds Box_perp R_nn`.

Before a one-loop pole calculation, the lowest-cost reproducible step is to derive the exact linearized curvature kernels in general dimension and reduce the genuine-defect projection to the smallest angular basis. This is tensor/projector preprocessing only; it does not evaluate any loop pole residue.

## Frozen conventions

- Euclidean flat background `g_mn = delta_mn + kappa h_mn`.
- Fourier convention `partial_m -> i q_m`.
- de Donder graviton numerator

  `P_mn,rs = 1/2(delta_mr delta_ns + delta_ms delta_nr) - 1/(d-2) delta_mn delta_rs`,

  with propagator numerator divided by `q^2`.
- Unit geodesic tangent `n^2=1`.
- `Q := q^2`, `s := q.n`, `u := s^2/Q`.
- `Box_perp := Box-D^2`, so in Fourier space `Box_perp -> -(Q-s^2)`.
- Overall common normalization factors `kappa`, propagator constants and the conventional global sign of the Euclidean two-point function are tracked separately from the angular/rank statements.

## Required predicates

A. Derive the linearized scalar-curvature vertex

`A_mn(q)`

and the tangent Ricci vertex

`B_mn(q,n)` corresponding to `R_nn`.

B. Contract `A` and `B` through the de-Donder propagator and obtain closed general-`d` kernels for

- `<R R>`;
- `<R R_nn>`;
- `<R (R_nn-R/d)>`.

C. Multiply by the frozen `Box_perp` factor and derive the genuine-defect kernels for `J_R` and `J_S`.

D. Verify the exact identity

`J_S = (1/d) J_R + J_TF`

at the projected kernel level, where `J_TF` uses `R_nn-R/d`.

E. Show that the two genuine defect kernels span at most two angular polynomial shapes in `u`, and record them explicitly without isotropically averaging `u` before the geodesic form-factor integration.

F. Verify that the traceless kernel vanishes under the **formal isotropic angular substitution** `u=1/d`, while explicitly retaining that this substitution is not allowed inside the fixed-geodesic observable before line/form-factor integration.

G. Produce a reproducible symbolic script and GitHub Actions artifact containing the general-`d` formulas and `d=4` specialization.

H. No loop residue, pole coefficient, `B_1`, EDT exponent or target value may be inferred from these tree/projector kernels.

## Frozen classifications

- `PASS_SCOPED_LINEARIZED_GENUINE_DEFECT_KERNEL_TWO_SHAPE_BASIS` if A-H pass and two independent angular shapes remain.
- `PASS_SCOPED_LINEARIZED_GENUINE_DEFECT_KERNEL_ONE_SHAPE_BASIS` only if the two projected kernels are analytically proportional in general `d,u`.
- `FAIL_SCOPED_KERNEL_CONVENTION_INCONSISTENT` if the symbolic derivation fails the decomposition/check identities.
- `INFRASTRUCTURE_FAIL` only for workflow/script failure.

## Controls

- `FOURIER_SIGN_CONVENTION_CONTROL`
- `TRACE_TRACELESS_DECOMPOSITION_CONTROL`
- `PREMATURE_ISOTROPIC_AVERAGE_CONTROL`
- `TREE_KERNEL_LOOP_RESIDUE_SWAP_CONTROL`
- `OVERALL_NORMALIZATION_RANK_CONTROL`
- `EDT_TARGET_KERNEL_FIT_CONTROL`

## Claim ceiling

A PASS supplies exact linearized projection kernels and reduces tensor algebra. It does not compute the one-loop defect mixing, `B_1`, noncancellation, any EDT/EFT comparison, `BRIDGE_DERIVED`, new physics or a candidate theory.