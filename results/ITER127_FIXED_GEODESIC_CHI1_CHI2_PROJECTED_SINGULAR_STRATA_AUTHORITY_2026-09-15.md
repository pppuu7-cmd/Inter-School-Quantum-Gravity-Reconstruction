# ITER127 terminal result — fixed-geodesic chi1/chi2 projected singular-strata authority

Date: 2026-09-15
Gate: `ITER127_FIXED_GEODESIC_CHI1_CHI2_PROJECTED_SINGULAR_STRATA_AUTHORITY`
Preregistration: `prereg/ITER127_FIXED_GEODESIC_CHI1_CHI2_PROJECTED_SINGULAR_STRATA_AUTHORITY_2026-09-15.md`
Source authority: `sources/ITER127_FIXED_GEODESIC_CHI1_CHI2_PROJECTED_SINGULAR_STRATA_AUTHORITY_2026-09-15.md`
Adversarial review: `results/ITER127_ADVERSARIAL_CRITIC_2026-09-15.md`
Machine table: `analysis/iter127_projected_singular_strata_table.json`
Exact-source artifacts:
- `iter127-frob-geodesic-kernel-authority`
- `iter127-frob-geodesic-structure`
- `iter127-frob-initial-tangent-coefficients`
- `iter127-frob-strict-source-assertions`

## Terminal classification

**`PASS_SCOPED_EXACT_CHI1_CHI2_WEIGHTS_SOURCE_QUALIFIED_SINGULAR_TABLE_CLOSED`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Exact source-qualified geodesic structure

At first perturbative order, suppressing tensor indices only for the affine-weight statement,

`chi1(t) = -(t/2) h(x).v - int_0^t ds (t-s) Gamma1(x+s v)[v,v]`.

At second order,

`chi2(t) = +(3t/8) h(x)^2.v`
`          - int_0^t ds (t-s)[Gamma2[v,v] + 2 Gamma1[v,d chi1] + (partial Gamma1)[chi1,v,v]]`.

The strict exact-source workflow verifies `-1/2` and `+3/8` in the same source equation environments as `chi1` and `chi2`, respectively, together with the affine Green-kernel and chi2-to-chi1 nesting.

## Closed affine-parameter structure

- `chi1` contains at most one independent line parameter.
- `chi2` contains at most two after substituting `chi1`.
- every outer endpoint Green integral contributes `(1-tau)` at final endpoint `t=1`;
- the nested `d chi1` bulk term has no surviving `(tau-sigma)` diagonal suppression;
- the nested `chi1` position term retains `(tau-sigma)` and therefore softens the diagonal by one power;
- the initial part of `chi1` inside `(partial Gamma1) chi1` contributes `tau(1-tau)`, suppressing both outer endpoints;
- `chi1 chi1` bulk-bulk gives `(1-tau)(1-sigma)` and does not suppress the line diagonal.

Initial-tangent terms remain endpoint-local and are not reclassified as line kernels.

## What is now ready

ITER126's local affine asymptotic-subtraction method can now be applied to the **actual source weights** rather than schematic geodesic kernels. The remaining missing ingredient for each row is curvature/projector derivative power counting and tensor cancellation.

## Exact successor

`ITER128_FIXED_GEODESIC_CURVATURE_PROJECTED_LOCAL_SINGULAR_DEGREE_CENSUS`

Combine:

- exact ITER127 affine weights;
- derivative content of `R1`, `Gamma1`, `Gamma2`, `chi1`, `chi2`;
- ITER122 genuine-defect projectors;
- ITER126 local residue formula.

For every singular stratum, compute a conservative superficial singular degree and the finite Taylor-jet order required to obtain poles. Keep power-counting upper bounds distinct from tensor cancellations; do not assign a nonzero residue merely from superficial degree.

## Claim ceiling

No curvature pole coefficient, no `B1`, no noncancellation theorem, no EDT fit or direct discrepancy, no bridge, new physics or candidate theory follows.