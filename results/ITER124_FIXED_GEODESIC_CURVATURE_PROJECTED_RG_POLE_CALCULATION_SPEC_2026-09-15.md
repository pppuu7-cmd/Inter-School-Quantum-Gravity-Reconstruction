# ITER124 terminal result — fixed-geodesic curvature projected RG/pole calculation specification

Date: 2026-09-15
Gate: `ITER124_FIXED_GEODESIC_CURVATURE_PROJECTED_RG_POLE_CALCULATION_SPEC`
Preregistration: `prereg/ITER124_FIXED_GEODESIC_CURVATURE_PROJECTED_RG_POLE_CALCULATION_SPEC_2026-09-15.md`
Source authority: `sources/ITER124_FIXED_GEODESIC_CURVATURE_PROJECTED_RG_POLE_CALCULATION_SPEC_2026-09-15.md`
Adversarial review: `results/ITER124_ADVERSARIAL_CRITIC_2026-09-15.md`
Manifest: `analysis/iter124_projected_rg_pole_manifest.json`
Validator: `analysis/iter124_validate_rg_pole_manifest.py`
Workflow: `.github/workflows/iter124_projected_rg_pole_manifest.yml`
Artifact: `iter124-projected-rg-pole-manifest`

## Terminal classification

**`PASS_SCOPED_PROJECTED_RG_POLE_CALCULATION_SPEC_CLOSED`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Main result

The remaining logarithmic-coefficient problem has a frozen finite calculation contract in `d=4-2 epsilon`.

The calculation must retain the complete F/M/G sectors, endpoint/local-composite renormalization, all line operators during mixing, and the ITER120 field-redefinition redundancy as a consistency check. The two genuine line directions are projected only after subdivergence subtraction and line-mixing renormalization.

## Correct physical target

The accepted output is

**`B1_total = B1_direct + B1_defect`**,

not a raw highest pole of one class.

The contract requires both simple and higher pole data, defect beta/mixing information, and the explicit noncontact logarithmic loop contribution. The split is bookkeeping; only the complete fixed-observable `B1_total` is a physical acceptance target.

## General-d extraction

The genuine-defect pole sector is extracted at

`u=0`, `u=1/2`

with the ITER123 general-dimensional projector, determinant `1/4`, before taking `d -> 4`.

Premature isotropic averaging, strict-four-dimensional pole projection and application of the projector before basis reduction are forbidden.

## Acceptance checks

A physical coefficient requires:

- gauge/BRST consistency of the complete relational observable;
- invariance under the ITER120 local metric field-redefinition redistribution;
- trace/traceless kernel identities of ITER122;
- validation of the two-point projector against a fuller angular representation on at least a subset;
- consistent higher-pole/subdivergence cancellation;
- target-data independence.

Any residual gauge or field-redefinition dependence reopens the renormalization basis rather than producing a physics claim.

## Stopping rule

- If `B1_total != 0` exactly, the binary noncancellation question is closed without computing finite `B0`.
- If `B1_total = 0`, a finite-constant `B0` calculation is mandatory.
- No EDT interpretation is allowed merely from the sign/value of `B1` without the later shell-estimator/continuum mapping.

## Exact successor

`ITER125_FIXED_GEODESIC_CURVATURE_PROJECTED_UV_TOPOLOGY_AND_MASTER_INTEGRAL_CENSUS`

Enumerate the minimal loop/topology families that survive the ITER124 contract after projector insertion. Separate ordinary massless bubble masters from one-/two-geodesic-parameter masters and counterterm insertion graphs, with the goal of producing an implementation-ready scalar integral basis rather than a tensor-diagram list.

## Claim ceiling

No `B1` value, no noncancellation theorem, no EDT fit or direct EDT/EFT discrepancy, no bridge, new physics or candidate theory follows.