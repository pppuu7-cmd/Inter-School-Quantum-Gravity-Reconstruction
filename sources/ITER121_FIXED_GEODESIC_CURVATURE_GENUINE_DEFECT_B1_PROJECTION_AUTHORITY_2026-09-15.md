# ITER121 source authority — genuine-defect projection onto B1

Date: 2026-09-15
Gate: `ITER121_FIXED_GEODESIC_CURVATURE_GENUINE_DEFECT_B1_PROJECTION_AUTHORITY`
Preregistration: `6695ff2cd161e6252d45937c5939350a5a77dd46`

## 1. Genuine defect input space

ITER120 leaves two nonredundant line directions at the frozen order:

`J_R = int ds Box_perp R`,
`J_S = int ds Box_perp R_nn`.

They are not related by the local metric field-redefinition quotient that removed `int R` and `int R_nn`.

Predicate A: **PASS**.

## 2. Logarithmic observable output is one-dimensional

Corrected ITER114 gives the complete separated one-loop radial form

`C(l;mu)=G^2 l^-8[B_0+B_1 L]`,

`L=log(mu^2 l^2)`.

Thus every pole/running contribution from the genuine defect subspace to the separated logarithmic sector must collapse to the single scalar coefficient `B_1`.

Writing the two renormalized pole projections as `rho_R,rho_S`, the most general contribution is

`Delta B_1 = w_R rho_R + w_S rho_S`,

for two tensor/projection weights `w_R,w_S` determined by the actual defect kernels.

Predicate B: **PASS**.

## 3. Trace/traceless decomposition does not fix the two weights

Decompose

`R_nn = R/4 + S_nn`,

where `S_mn` is traceless Ricci in four dimensions.

This rewrites

`J_S = (1/4) J_R + int ds Box_perp S_nn`.

The second term is an independent tangent-sensitive scalar. The fixed geodesic supplies a physical direction `n`, so it is not removed by residual rotations around the line.

A full isotropic average over `n` would kill the traceless projection, but the fixed-geodesic observable does **not** perform such an average: its tangent is part of the relational definition.

Therefore trace/traceless decomposition changes basis but does not reduce the genuine input rank to one.

Predicate C: **NO WEIGHT RELATION FROM TRACE**.
`GEODESIC_TANGENT_ISOTROPIC_AVERAGE_CONTROL`: **TRIGGERS**.
`TRACE_TRACELESS_RELATION_CONTROL`: **PASS_CONTROL**.

## 4. Bianchi identities do not relate the two transverse Laplacians

The contracted Bianchi identity constrains divergences of Ricci and was already used in ITER118 to reduce mixed derivative operators. It does not identify

`Box_perp R`

with

`Box_perp R_nn`

on a generic off-shell fluctuating metric. Such an identification would require an Einstein-space/isotropy condition not present in the perturbative path integral.

Thus Bianchi identities do not fix `w_R/w_S`.

## 5. Line reversal does not remove the traceless channel

Both `R` and `R_nn` are even under `n -> -n`, and `Box_perp` is also even. Hence line-reversal symmetry preserves both operators and supplies no relative sign/value constraint.

## 6. Minimum explicit UV calculation

No symmetry in the frozen stack determines `w_R rho_R + w_S rho_S` from one of the two channels alone.

The minimum equivalent calculations are therefore either:

1. determine the two projected pole matrix elements separately and combine them; or
2. construct the already-projected scalar RR defect insertion and compute its single combined pole residue directly, while retaining enough tensor information to verify field-redefinition and gauge consistency.

The second route is computationally preferable but is still a genuine loop/UV calculation.

Predicate E: **PASS_MINIMUM_DATA_DEFINED**.

## 7. Redundant sectors remain checks, not inputs

The `int R` and `int R_nn` directions quotiented in ITER120 should be retained in intermediate calculations to verify invariance under local metric field-coordinate changes. They do not add independent physical weights to `B_1`.

Predicate F: **PASS_CONTROL**.
`FIELD_REDEFINITION_REDUNDANT_INPUT_CONTROL`: **PASS_CONTROL**.

## 8. Target independence

No EDT datum fixes `w_R,w_S` or the pole residues.

Predicate G: **PASS_CONTROL**.
`EDT_LINEAR_COMBINATION_FIT_CONTROL`: **PASS_CONTROL**.

## Source classification

**`PASS_SCOPED_GENUINE_DEFECT_B1_OUTPUT_ONE_DIMENSION_TWO_INPUT_WEIGHTS_OPEN`**

The physical leading-log defect output is one number, but no source/analytic symmetry determines it from a single genuine defect channel. The remaining irreducible task is a projected one-loop UV residue calculation.

## Highest-information successor

Build the directly projected UV integrand for the scalar `B_1` combination, rather than the full 2x2 defect matrix. The gate should enumerate the minimal F/M/G + genuine-defect pole diagrams contributing to that projection and, if feasible, implement symbolic tensor reduction as a reproducible workflow.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No `B_1` value, noncancellation theorem, EDT fit, direct EDT/EFT conflict, bridge or new physics follows.