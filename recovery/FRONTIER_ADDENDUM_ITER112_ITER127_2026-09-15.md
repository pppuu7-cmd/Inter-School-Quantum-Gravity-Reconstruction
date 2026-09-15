# ISQGR recovery frontier addendum — ITER112 through active ITER127

Date: 2026-09-15
Repository: `pppuu7-cmd/Inter-School-Quantum-Gravity-Reconstruction`

This file supplements the older canonical `recovery/CURRENT_FRONT.md`, which predates the current original-calculation branch. It is additive to avoid an unsafe overwrite while the exact current blob SHA of the canonical recovery file is not carried in the active tool context.

Candidate theory: **UNFORMED / 0%**.
Bridge credit: **0**.
Overall programme roadmap readiness: **50% (no authorized increment)**.

## Persistent claim locks

No `BRIDGE_DERIVED`, no `UNIVERSAL_COMMON_PARENT_FOUND`, no `NEW_PHYSICS_FOUND`, no `FULL_QG`, no candidate theory, and no direct EDT/EFT conflict is authorized.

## Original fixed-geodesic curvature calculation branch

### ITER112

`PASS_SCOPED_FINITE_G2_OPERATOR_DIAGRAM_CENSUS_CALCULATION_READY`

Anchored fixed-geodesic `RR` through `O(G^2)` closes into finite F/M/G sectors:

- F: ordinary curvature/field/ghost/action sector;
- M: first-order geodesic localization;
- G: second-order geodesic localization.

This is calculation-ready for the anchored fixed-geodesic correlator, not yet the normalized EDT shell estimator.

### ITER113

`PASS_SCOPED_CONTACT_PRUNING_VALID_NONLOCAL_FMG_BASIS_REMAINS_CANCELLATION_OPEN`

Polynomial/contact structures and scaleless tadpoles can be removed from the separated-tail target only after renormalization. M/G line sectors remain nonlocal and cannot be pruned. No symmetry protects a nonzero final coefficient.

### ITER114 — corrected

Initial `log^2` separated basis was mathematically corrected before target use. The exact nonzero-separation identities

`Box[L/r^2] = -4/r^4`,

`Box[L^2/r^2] = 8(1-L)/r^4`

show that the one-loop separated basis is

**`C_RR^geo(l;mu)=G^2 l^-8[B_0(mu)+B_1(mu) log(mu^2 l^2)] + O(G^3)`**

plus contact terms.

Correct classification:

`PASS_SCOPED_G2_NONCONTACT_RADIAL_BASIS_L8_CONSTANT_PLUS_SINGLE_LOG`.

### ITER115

`INVALIDATED_PRE_ADJUDICATION_BY_ITER114_SEPARATED_LOG_DEGREE_CORRECTION`.

Scientific credit 0.

### ITER116

Valid RG hierarchy:

`mu dB_1/dmu = 0`,

`mu dB_0/dmu = -2 B_1`

at frozen order. `B_1 != 0` is sufficient to prove the `O(G^2)` separated function is not identically zero.

Later strategy correction: `B_1` is controlled by the complete projected RG/pole system, not necessarily a raw highest/double pole alone.

### ITER117

`PASS_SCOPED_ZCHI_SEPARATED_INACTIVE_CURVATURE_PRODUCT_COUNTERTERM_BASIS_OPEN`.

The matter-scalar geodesic `Z_chi` counterterm acts on a nonzero separated tree propagator. For curvature, lower-order separated `RR` is contact-only, so the analogous direct `Z_chi` variation is contact-only. Curvature-specific endpoint/line composite mixing had to be classified.

### ITER118

`PASS_SCOPED_FINITE_LINE_ENDPOINT_COUNTERTERM_BASIS_POWER_COUNTING_CLOSED`.

Finite one-loop/linear-curvature basis. Independent line-interior representatives before field-redefinition quotient:

- `int R`;
- `int R_nn`;
- `int Box_perp R`;
- `int Box_perp R_nn`.

### ITER119

`PASS_SCOPED_LINE_DEFECT_OBSERVABLE_PROJECTION_RANK_TWO_MAXIMAL`.

Internal line-renormalization can remain four-dimensional, but the separated scalar output has only two radial coefficients: finite projection to `B_0` and running/log projection to `B_1`.

### ITER120

`PASS_SCOPED_DIM2_LINE_SECTORS_FIELD_REDEFINITION_REDUNDANT_GENUINE_DEFECT_RANK_TWO`.

Under

`delta g_mn = kappa^2[a R_mn+b g_mn R]`,

`delta l=(kappa^2/2)[a int R_nn+b int R]`.

Thus `int R` and `int R_nn` are local metric field-coordinate redundant directions when action+observable transform consistently. Genuine line-defect quotient:

- `int Box_perp R`;
- `int Box_perp R_nn`.

### ITER121

`PASS_SCOPED_GENUINE_DEFECT_B1_OUTPUT_ONE_DIMENSION_TWO_INPUT_WEIGHTS_OPEN`.

The physical log output is one number `B_1`, but trace/traceless, Bianchi and line-reversal symmetries do not determine the relative weights of the two genuine defect inputs.

### ITER122

`PASS_SCOPED_LINEARIZED_GENUINE_DEFECT_KERNEL_TWO_SHAPE_BASIS`.

Exact de-Donder general-`d` projectors with `Q=q^2`, `u=(q.n)^2/Q`:

`K_RR=-(d-1)Q/(d-2)`,

`K_R,Rnn=-Q/[2(d-2)]-Qu/2`,

`K_R,TF=(Q/2)(1/d-u)`.

After `Box_perp -> -Q(1-u)`:

`K_JR=[(d-1)/(d-2)]Q^2(1-u)`,

`K_JTF=(Q^2/2)(1-u)(u-1/d)`.

Two independent angular shapes remain. Symbolic GitHub Actions artifact exists.

### ITER123

`PASS_SCOPED_TWO_POINT_KINEMATIC_PROJECTOR_FOR_GENUINE_DEFECT_RESIDUES`.

Centered line form factor:

`F_center=l*2 sin(z/2)/z`, `z=(q.n)l`.

For the two angular shapes, kinematic points `u=0,1/2` give general-`d` determinant `1/4` and exact inverse

`rho_0=[(d-2)/d] a(0)+[4/d] a(1/2)`,

`rho_1=-2 a(0)+4 a(1/2)`.

Project only after basis reduction/subtraction; avoid `u=1` and line-form-factor zeros.

### ITER124

`PASS_SCOPED_PROJECTED_RG_POLE_CALCULATION_SPEC_CLOSED`.

Machine-readable calculation contract freezes F/M/G, endpoint and line sectors, subtraction order, general-`d` projector, gauge/BRST and field-redefinition checks, and outputs

`B1_total = B1_direct + B1_defect`.

If `B1_total != 0`, binary noncancellation is closed; if exactly zero, finite `B_0` must be calculated.

### ITER125

`PASS_SCOPED_ONE_LOOP_BUBBLE_TOPOLOGY_PLUS_ONE_TWO_LINE_PARAMETER_MASTER_FAMILIES`.

No genuine triangle/box bulk loop denominator is required. Master categories:

- ordinary massless bubble;
- one-parameter phase-dressed bubble;
- two-parameter phase-dressed bubble;
- one-propagator line-line self-contraction with coincidence poles;
- counterterm/projector insertions.

### ITER126

`PASS_SCOPED_DEFECT_POLES_LOCAL_ENDPOINT_COINCIDENCE_ASYMPTOTIC_SUBTRACTION_AUTHORIZED`.

After bulk subtraction, residual defect poles are local in affine-parameter boundary strata. For

`int_0^1 dx x^(-m+a epsilon) w(x)`,

the endpoint pole is controlled by the Taylor coefficient `w_(m-1)`:

`Res = w_(m-1)/a`.

Verified scalar prototypes:

- endpoint product residue `+2`;
- line-line coincidence residue `-1`.

These are method-validation residues, not curvature coefficients.

## Active gate — ITER127

`ITER127_FIXED_GEODESIC_CHI1_CHI2_PROJECTED_SINGULAR_STRATA_AUTHORITY`.

Exact arXiv source package `1706.01891` has been downloaded/audited through GitHub Actions. Artifact:

`iter127-frob-geodesic-kernel-authority`.

The artifact contains archive/TeX SHA256 hashes and short equation-only evidence with both `chi` and line-integral formulas.

**Current status: source extraction completed; scientific interpretation of exact `chi_1/chi_2` affine weights pending.**

No memory-reconstructed weights are authorized to substitute for the source equations.

## Exact next action

Read the extracted first-/second-order geodesic equations, separate initial-tangent/vierbein terms from bulk line integrals, and populate the ITER126 singular-strata table with the exact polynomial suppression orders. Only then evaluate curvature-specific pole residues.
