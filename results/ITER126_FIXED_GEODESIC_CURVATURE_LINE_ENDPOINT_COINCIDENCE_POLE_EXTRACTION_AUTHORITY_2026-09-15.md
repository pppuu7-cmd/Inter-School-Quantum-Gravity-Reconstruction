# ITER126 terminal result — fixed-geodesic curvature line endpoint/coincidence pole extraction authority

Date: 2026-09-15
Gate: `ITER126_FIXED_GEODESIC_CURVATURE_LINE_ENDPOINT_COINCIDENCE_POLE_EXTRACTION_AUTHORITY`
Preregistration: `prereg/ITER126_FIXED_GEODESIC_CURVATURE_LINE_ENDPOINT_COINCIDENCE_POLE_EXTRACTION_AUTHORITY_2026-09-15.md`
Source authority: `sources/ITER126_FIXED_GEODESIC_CURVATURE_LINE_ENDPOINT_COINCIDENCE_POLE_EXTRACTION_AUTHORITY_2026-09-15.md`
Adversarial review: `results/ITER126_ADVERSARIAL_CRITIC_2026-09-15.md`
Authoritative implementation: `analysis/iter126_defect_pole_prototypes_v2.py`
Workflow: `.github/workflows/iter126_defect_pole_prototypes.yml`
Artifact: `iter126-defect-pole-prototypes`

## Terminal classification

**`PASS_SCOPED_DEFECT_POLES_LOCAL_ENDPOINT_COINCIDENCE_ASYMPTOTIC_SUBTRACTION_AUTHORIZED`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Main result

After ordinary bulk/subgraph renormalization, the remaining fixed-geodesic defect poles are local in affine-parameter space. They arise from endpoint, line-line coincidence, and overlapping boundary strata; finite interior line regions do not determine the UV pole coefficients.

For a local model

`int_0^1 dx x^(-m+a epsilon) w(x)`,

the pole is controlled by the finite Taylor coefficient `w_(m-1)`:

**`Res = w_(m-1)/a`**

for that endpoint. Thus power-singular defect kernels require a finite local Taylor jet rather than merely the value `w(0)`.

## Verified prototypes

In `d=4-2 epsilon`:

### Endpoint-product prototype

`E=integral_0^1 [tau(1-tau)]^(-2+2 epsilon) d tau`

has

**`Res E = +2`.**

Each endpoint contributes `+1` through the linear Taylor coefficient of the opposite-end weight.

### Line-line coincidence prototype

`D=integral_0^1 d tau integral_0^1 d sigma |tau-sigma|^(-2+2 epsilon)`

has

**`Res D = -1`.**

The sign follows from the linear term of the effective diagonal weight `2(1-delta)`.

These are method-validation residues, not curvature coefficients.

## Authorized pole algorithm

For every projected M1-M3 master:

1. identify endpoint/diagonal/overlap singular strata;
2. determine the local singular exponent from the actual curvature/geodesic numerator;
3. Taylor-expand smooth weights only to the finite power-counting order needed for poles;
4. sector-decompose overlapping two-parameter regions;
5. integrate singular monomials analytically in `epsilon`;
6. subtract them from the exact line integrand;
7. set `epsilon=0` in the finite remainder;
8. combine with bulk/counterterm pole subtraction before the ITER123 genuine-defect projector.

This means the RG/pole problem does not require the complete finite oscillatory/Bessel dependence of the geodesic masters.

## Exact successor

`ITER127_FIXED_GEODESIC_CHI1_CHI2_PROJECTED_SINGULAR_STRATA_AUTHORITY`

Extract the explicit first- and second-order geodesic embedding kernels (`chi_1`, `chi_2`) from the frozen fixed-geodesic perturbative source, combine them with the ITER122 curvature projectors, and tabulate the actual endpoint/coincidence powers and Taylor orders for every M/G singular stratum. This is the last source/algebra stage before evaluating curvature-specific pole residues.

## Claim ceiling

The prototype residues are not `B_1`; no curvature pole coefficient, noncancellation theorem, EDT fit, direct discrepancy, bridge, new physics or candidate theory follows.