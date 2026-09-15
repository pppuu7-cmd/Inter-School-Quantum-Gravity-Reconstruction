# ITER122 source authority — linearized curvature / genuine-defect kernel reduction

Date: 2026-09-15
Gate: `ITER122_LINEARIZED_CURVATURE_GENUINE_DEFECT_KERNEL_REDUCTION`
Preregistration: `prereg/ITER122_LINEARIZED_CURVATURE_GENUINE_DEFECT_KERNEL_REDUCTION_2026-09-15.md`
Authoritative symbolic implementation: `analysis/iter122_linearized_curvature_kernels_v2.py`
Workflow: `.github/workflows/iter122_linearized_curvature_kernels.yml`

## Technical implementation note

An earlier non-authoritative `analysis/iter122_linearized_curvature_kernels.py` contained a malformed Markdown-output string in its tail. It was detected before CI adjudication. The authoritative workflow uses only the corrected `v2` script. Scientific formulas below are independently asserted symbolically in that script.

## 1. Frozen conventions

Use Euclidean Fourier convention `partial_m -> i q_m`,

`Q := q^2`, `s:=q.n`, `u:=s^2/Q`, `n^2=1`.

The de-Donder numerator is

`P_mn,rs = 1/2(delta_mr delta_ns+delta_ms delta_nr) - delta_mn delta_rs/(d-2)`,

with propagator factor `1/Q`.

The Fourier multiplier for

`Box_perp := Box-D^2`

is

`-Q(1-u)`.

Overall common normalization/sign conventions outside this frozen Fourier choice do not affect the rank statements.

## 2. Linearized curvature vertices

The scalar-curvature vertex is

**`A_mn = Q delta_mn - q_m q_n`.**

For

`R_nn := R_mn n^m n^n`,

the linearized vertex is

**`B_mn = 1/2[Q n_m n_n + s^2 delta_mn - s(q_m n_n+q_n n_m)]`.**

Useful invariants are

`tr A = (d-1)Q`,
`A:A = (d-1)Q^2`,
`tr B = (Q/2)[1+(d-2)u]`,
`q_m q_n B_mn = 0`,
`A:B = Q tr B`.

Predicate A: **PASS**.

## 3. Exact general-d propagator contractions

For symmetric tensors,

`X:P:Y = X:Y - tr(X)tr(Y)/(d-2)`.

Including the propagator `1/Q`, the exact kernels are

**`K_RR = -(d-1)/(d-2) Q`.**

**`K_R,Rnn = -Q/[2(d-2)] - (Q u)/2`.**

For the traceless tangent-Ricci projection

`R_TF,nn := R_nn - R/d`,

**`K_R,TF = (Q/2)(1/d-u)`.**

The last expression is a useful exact check: a formal isotropic tangent substitution `u=1/d` kills the traceless projection.

Predicate B: **PASS**.

## 4. Genuine Box_perp defect kernels

Using `Box_perp -> -Q(1-u)`, define the projected kernels for

`J_R = int ds Box_perp R`,
`J_S = int ds Box_perp R_nn`,
`J_TF = int ds Box_perp(R_nn-R/d)`.

Then

**`K_JR = [(d-1)/(d-2)] Q^2(1-u)`.**

**`K_JS = (Q^2/2)(1-u)[1/(d-2)+u]`.**

**`K_JTF = (Q^2/2)(1-u)(u-1/d)`.**

Predicate C: **PASS**.

## 5. Exact trace/traceless decomposition

The symbolic implementation asserts identically

**`K_JS = K_JR/d + K_JTF`.**

The residual simplifies to zero in symbolic general dimension.

Predicate D: **PASS**.

## 6. Two independent angular shapes

After removing common powers/coefficient factors, a convenient angular basis is

`f_trace(u)=1-u`,

`f_TF(u)=(1-u)(u-1/d)`.

Their ratio is `u-1/d`, which depends on `u`; therefore the two genuine defect projections are not analytically proportional for generic fixed-geodesic kinematics.

Equivalently, `J_S` contains a trace contribution plus the independent traceless shape.

Predicate E: **PASS — TWO SHAPES**.

## 7. Why isotropic angular averaging is only a diagnostic check

The formal substitution

`u -> 1/d`

makes `K_R,TF` and `K_JTF` vanish, as expected for an isotropic average of a traceless tensor.

But the fixed-geodesic observable contains line form factors depending on `q.n`. Therefore this average cannot be performed **before** the line/form-factor integration and UV projection. Doing so would erase the very tangent-sensitive defect channel whose pole weight ITER121 left open.

Predicate F: **PASS_CONTROL**.
`PREMATURE_ISOTROPIC_AVERAGE_CONTROL`: **TRIGGERS**.

## 8. Four-dimensional specialization

For `d=4`:

`K_RR = -(3/2) Q`,

`K_R,Rnn = -(Q/4)(1+2u)`,

`K_R,TF = (Q/8)(1-4u)`,

`K_JR = (3/2) Q^2(1-u)`,

`K_JS = (Q^2/4)(1-u)(1+2u)`,

`K_JTF = (Q^2/8)(1-u)(4u-1)`.

These satisfy

`K_JS = K_JR/4 + K_JTF`.

## 9. What these kernels are — and are not

All kernels above are polynomial tree/projector objects. In ordinary position space they are contact-like. They do **not** give the physical separated `B_1` coefficient.

Their role is to reduce the tensor algebra of the UV defect mixing/pole calculation to two exact tangent-angular structures before the nonlocal geodesic form factors and loop integrals are evaluated.

Predicate H: **PASS_CONTROL**.
`TREE_KERNEL_LOOP_RESIDUE_SWAP_CONTROL`: **PASS_CONTROL**.

## Source classification

**`PASS_SCOPED_LINEARIZED_GENUINE_DEFECT_KERNEL_TWO_SHAPE_BASIS`**

The two genuine defect channels survive exact general-dimensional tensor reduction as two independent angular shapes. No symmetry shortcut removes the traceless channel before fixed-geodesic form-factor integration.

## Highest-information successor

Construct the UV pole integrand directly in this two-shape basis. The next gate should classify the required angular/geodesic moments of

`f_trace(u)` and `f_TF(u)`

against the one-/two-line form factors arising in M/G sectors. The goal is to determine the smallest scalar master-moment set needed for the projected `B_1` residue, without computing finite `B_0` terms.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No loop pole residue, no `B_1`, no noncancellation theorem, no EDT fit or direct EDT/EFT conflict, no bridge or new physics follows.