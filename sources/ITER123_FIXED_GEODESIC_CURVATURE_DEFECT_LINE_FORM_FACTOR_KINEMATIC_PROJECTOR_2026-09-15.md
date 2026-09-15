# ITER123 source authority — fixed-geodesic curvature defect line form factor / kinematic projector

Date: 2026-09-15
Gate: `ITER123_FIXED_GEODESIC_CURVATURE_DEFECT_LINE_FORM_FACTOR_KINEMATIC_PROJECTOR`
Preregistration: `prereg/ITER123_FIXED_GEODESIC_CURVATURE_DEFECT_LINE_FORM_FACTOR_KINEMATIC_PROJECTOR_2026-09-15.md`
Symbolic implementation: `analysis/iter123_line_form_factor_projector.py`
Workflow: `.github/workflows/iter123_line_form_factor_projector.yml`
Artifact: `iter123-line-form-factor-projector`

## 1. Exact straight-line Fourier factor

Center the reference segment by translation invariance,

`x(s)=s n`, `s in [-l/2,l/2]`.

For a local line density with momentum `q`,

`F_center(q.n,l) = int_{-l/2}^{l/2} ds exp(i s q.n)`

so with `z=(q.n)l`,

**`F_center = l Phi(z)`, `Phi(z)=2 sin(z/2)/z`.**

The continuous limit is `Phi(0)=1`.

For the endpoint-anchored segment `[0,l]`,

`F_[0,l] = exp(i z/2) F_center`.

When all insertions are translated consistently, this phase is exactly the translation phase; centering does not change the line-operator content.

Predicates A,C: **PASS**.

## 2. Common form factor for both genuine defect operators

At linear order, both

`J_R=int ds Box_perp R`,
`J_TF=int ds Box_perp(R_nn-R/d)`

are integrals over the same straight segment. Therefore both projected kernels acquire the same multiplicative `F_center`.

After common powers and fixed normalization constants are absorbed into residue definitions, the remaining angular shapes are exactly the ITER122 basis

`f_0(u)=1-u`,

`f_1(u)=(1-u)(u-1/d)`.

Thus the line integration does not collapse the two-shape basis by itself.

Predicate B: **PASS**.

## 3. Normalized divergent amplitude

Away from zeros of `F_center`, define the basis-reduced pole amplitude schematically by

`a(u) := A_div(q,n,l) / [Q^2 F_center(q.n,l) * common normalization]`.

Once bulk/redundant structures have been removed and the divergence is known to lie in the genuine defect subspace,

**`a(u)=rho_0 f_0(u)+rho_1 f_1(u)`.**

The unknown `rho_0,rho_1` are UV defect residues/projections, not values supplied by ITER123.

Predicate D: **PASS_SCOPED**.

## 4. Two-point kinematic projector in general dimension

Choose

`u_0=0`,
`u_1=1/2`.

Then

`f_0(0)=1`,
`f_1(0)=-1/d`,

`f_0(1/2)=1/2`,
`f_1(1/2)=(d-2)/(4d)`.

The projector matrix is

`M_d = [[1, -1/d], [1/2, (d-2)/(4d)]]`.

Its determinant is exactly

**`det M_d = 1/4`**

for generic finite `d`. Therefore the same kinematics are nonexceptional before taking `d -> 4`, which is preferable for dimensional-regularization pole extraction.

If

`a_0=a(0)`, `a_1=a(1/2)`,

the exact inverse is

**`rho_0 = [(d-2)/d] a_0 + [4/d] a_1`,**

**`rho_1 = -2 a_0 + 4 a_1`.**

Predicate E: **PASS_STRONGER_GENERAL_D**.

## 5. d=4 specialization verified by CI

At `d=4`,

`M_4=[[1,-1/4],[1/2,1/8]]`,

`det M_4=1/4`,

and

`rho_0=a_0/2+a_1`,

`rho_1=-2a_0+4a_1`.

The symbolic workflow asserts these formulas and the named artifact is present.

Predicate H: **PASS_INFRASTRUCTURE**.

## 6. Exceptional kinematics

`u=1` is forbidden for projection because `Box_perp` vanishes and both shapes are zero.

The centered line form factor vanishes for nonzero

`z=2 pi k`, `k in Z`.

The second kinematic point must therefore use a generic external `Q,l` such that its `z` does not land on a form-factor zero. `u=0` itself is regular because `Phi(0)=1`.

Predicate F: **PASS_CONTROL**.

## 7. Scope of the projector

The two-point inversion is valid **after** the divergent amplitude has been reduced to the genuine defect basis established by ITER118–122. It is not a license to evaluate the raw full F/M/G amplitude at two points and ignore bulk, field-redefinition-redundant, contact or gauge-bookkeeping structures that have not yet been separated.

This distinction is especially important in dimensional regularization: the general-`d` projector should be applied to pole coefficients before the final `d -> 4` specialization when evanescent structures could multiply poles.

Predicate G: **PASS_CONTROL**.
`PRE_BASIS_REDUCTION_PROJECTOR_CONTROL`: **PASS_CONTROL**.

## 8. Target independence

The kinematic points are selected solely for algebraic invertibility and nonexceptionality. No EDT datum enters their choice.

Predicate I: **PASS_CONTROL**.

## Source classification

**`PASS_SCOPED_TWO_POINT_KINEMATIC_PROJECTOR_FOR_GENUINE_DEFECT_RESIDUES`**

The two genuine line-defect residues can, in principle, be extracted from two scalar kinematic evaluations rather than a full angular-function reconstruction, provided the UV pole amplitude has first been consistently projected into the genuine defect sector.

## Highest-information successor

Construct the **projected highest-pole calculation specification** in general `d=4-2 epsilon`: identify the minimal F/M/G pole diagrams whose genuine-defect part must be evaluated at `u=0` and `u=1/2`, and define the subtraction order for bulk, field-redefinition-redundant and endpoint-contact sectors. This will turn the remaining `B_1` question into a finite pair of scalar pole computations.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No pole residue, no `B_1`, no noncancellation theorem, no EDT fit or direct EDT/EFT conflict, no bridge or new physics follows.