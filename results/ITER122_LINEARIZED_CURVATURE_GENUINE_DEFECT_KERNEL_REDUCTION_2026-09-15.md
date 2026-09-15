# ITER122 terminal result — linearized curvature / genuine-defect kernel reduction

Date: 2026-09-15
Gate: `ITER122_LINEARIZED_CURVATURE_GENUINE_DEFECT_KERNEL_REDUCTION`
Preregistration: `prereg/ITER122_LINEARIZED_CURVATURE_GENUINE_DEFECT_KERNEL_REDUCTION_2026-09-15.md`
Source authority: `sources/ITER122_LINEARIZED_CURVATURE_GENUINE_DEFECT_KERNEL_REDUCTION_2026-09-15.md`
Adversarial review: `results/ITER122_ADVERSARIAL_CRITIC_2026-09-15.md`
Authoritative implementation: `analysis/iter122_linearized_curvature_kernels_v2.py`
Workflow: `.github/workflows/iter122_linearized_curvature_kernels.yml`
Artifact: `iter122-linearized-curvature-kernels`

## Terminal classification

**`PASS_SCOPED_LINEARIZED_GENUINE_DEFECT_KERNEL_TWO_SHAPE_BASIS`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Reproducibility status

The authoritative `v2` symbolic implementation asserts the general-dimensional identities, writes JSON/Markdown outputs, and is executed by the dedicated GitHub Actions workflow. The named workflow artifact is present. The earlier non-authoritative script with a malformed Markdown-output tail is documented and is not used by CI.

A green symbolic workflow is infrastructure evidence only; the scientific result is the exact algebra below.

## Exact general-d kernels

With

`Q=q^2`, `u=(q.n)^2/Q`,

and de-Donder propagator conventions frozen in the preregistration,

`K_RR = -(d-1)/(d-2) Q`,

`K_R,Rnn = -Q/[2(d-2)] - Q u/2`,

`K_R,TF = (Q/2)(1/d-u)`.

For `Box_perp -> -Q(1-u)`, the genuine-defect kernels are

**`K_JR = [(d-1)/(d-2)] Q^2(1-u)`**,

**`K_JS = (Q^2/2)(1-u)[1/(d-2)+u]`**,

**`K_JTF = (Q^2/2)(1-u)(u-1/d)`**.

They satisfy identically

`K_JS=K_JR/d+K_JTF`.

## Two-shape basis

After common factors are removed, the exact angular basis is

`f_trace(u)=1-u`,

`f_TF(u)=(1-u)(u-1/d)`.

These are not proportional for generic fixed-geodesic kinematics. The formal isotropic substitution `u=1/d` kills the traceless term, but it is not allowed before line/form-factor integration because the fixed geodesic supplies a tangent-dependent weight.

## d=4 specialization

`K_RR=-(3/2)Q`,

`K_R,Rnn=-(Q/4)(1+2u)`,

`K_R,TF=(Q/8)(1-4u)`,

`K_JR=(3/2)Q^2(1-u)`,

`K_JS=(Q^2/4)(1-u)(1+2u)`,

`K_JTF=(Q^2/8)(1-u)(4u-1)`.

## Hard scope boundary

These are tree/projector kernels. They are contact-like before line integration and do not determine the one-loop pole residue or `B_1`. Geodesic embedding/tangent fluctuations remain in the M/G sectors and must not be folded into these local vertices twice.

## Exact successor

`ITER123_FIXED_GEODESIC_CURVATURE_DEFECT_LINE_FORM_FACTOR_MOMENT_BASIS`

Derive the exact Fourier form factor for the two genuine line operators along the straight reference geodesic and determine the minimum scalar angular-moment basis needed when `f_trace` and `f_TF` are weighted by tangent-dependent line factors. The successor must keep the distinction between external defect-projector moments and the still-uncomputed internal one-loop pole integrals.

## Claim ceiling

No loop pole residue, no `B_1`, no noncancellation theorem, no EDT fit or direct EDT/EFT conflict, no bridge, new physics or candidate theory follows.