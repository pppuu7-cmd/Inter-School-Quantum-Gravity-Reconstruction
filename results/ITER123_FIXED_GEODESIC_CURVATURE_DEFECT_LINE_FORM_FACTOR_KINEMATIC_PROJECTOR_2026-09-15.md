# ITER123 terminal result — fixed-geodesic curvature defect line form factor / kinematic projector

Date: 2026-09-15
Gate: `ITER123_FIXED_GEODESIC_CURVATURE_DEFECT_LINE_FORM_FACTOR_KINEMATIC_PROJECTOR`
Preregistration: `prereg/ITER123_FIXED_GEODESIC_CURVATURE_DEFECT_LINE_FORM_FACTOR_KINEMATIC_PROJECTOR_2026-09-15.md`
Source authority: `sources/ITER123_FIXED_GEODESIC_CURVATURE_DEFECT_LINE_FORM_FACTOR_KINEMATIC_PROJECTOR_2026-09-15.md`
Adversarial review: `results/ITER123_ADVERSARIAL_CRITIC_2026-09-15.md`
Implementation: `analysis/iter123_line_form_factor_projector.py`
Workflow: `.github/workflows/iter123_line_form_factor_projector.yml`
Artifact: `iter123-line-form-factor-projector`

## Terminal classification

**`PASS_SCOPED_TWO_POINT_KINEMATIC_PROJECTOR_FOR_GENUINE_DEFECT_RESIDUES`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Exact line form factor

For a centered straight segment,

`F_center=l Phi(z)`,

`Phi(z)=2 sin(z/2)/z`,

`z=(q.n)l`.

The endpoint-anchored representation differs only by `exp(i z/2)` when all insertions are translated consistently.

Both genuine line-defect operators share this same form factor at the linear projector level.

## General-d two-point projector

After dividing the known common `Q^2 F_center` factors and fixed normalization constants, write

`a(u)=rho_0(1-u)+rho_1(1-u)(u-1/d)`.

At

`u_0=0`, `u_1=1/2`,

the exact matrix has

**`det M_d=1/4`**.

Hence, before taking the dimensional-regularization limit,

**`rho_0=[(d-2)/d]a(0)+[4/d]a(1/2)`,**

**`rho_1=-2a(0)+4a(1/2)`.**

For `d=4`,

`rho_0=a(0)/2+a(1/2)`,

`rho_1=-2a(0)+4a(1/2)`.

## Exceptional points

- `u=1` is unusable because `Box_perp` kills both genuine shapes.
- Nonzero `z=2 pi k` are line-form-factor zeros and must be avoided.
- `u=0` is regular because `Phi(0)=1`.

## Scope boundary

This is a residue **extraction projector**, not the residue calculation. It becomes valid after the UV divergent amplitude has been reduced to the genuine defect basis and bulk/contact/redundant structures have been subtracted consistently.

Possible evanescent operator sectors in a future full `d=4-2 epsilon` loop calculation remain a separate consistency check; the present projector does not assume them away.

## Exact successor

`ITER124_FIXED_GEODESIC_CURVATURE_PROJECTED_RG_POLE_CALCULATION_SPEC`

Freeze the minimal `d=4-2 epsilon` calculation needed at the two projector kinematics. It must include all F/M/G pole contributions, bulk subdivergence subtraction, field-redefinition-redundant line directions as checks, the two genuine defect counterterms, and the mapping from their beta/pole data to the physical `B_1`. The specification must correct the earlier overstatement that `B_1` is necessarily determined by a highest/double pole alone.

## Claim ceiling

No UV residue, no `B_1`, no noncancellation theorem, no EDT fit or direct EDT/EFT conflict, no bridge, new physics or candidate theory follows.