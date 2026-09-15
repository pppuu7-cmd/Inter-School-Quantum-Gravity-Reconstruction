# ITER122 adversarial critic — linearized curvature / genuine-defect kernels

Date: 2026-09-15
Gate: `ITER122_LINEARIZED_CURVATURE_GENUINE_DEFECT_KERNEL_REDUCTION`
Source authority: `sources/ITER122_LINEARIZED_CURVATURE_GENUINE_DEFECT_KERNEL_REDUCTION_2026-09-15.md`

## Attack 1 — the de-Donder propagator convention fixes a physical sign

Only partly. With the frozen Euclidean Fourier convention, the displayed signs are internally exact. A different overall convention for the graviton propagator or Euclidean two-point function can flip a common normalization/sign. That does not alter the trace/traceless decomposition, angular-shape independence or projection rank. The `Box_perp` sign is explicitly frozen and must be changed consistently if another convention is used.

## Attack 2 — `R_nn` should include fluctuations of the geodesic tangent already at this stage

Rejected for this gate's purpose. ITER122 derives the **linearized local curvature kernel** contracted with the background unit tangent that labels the defect operator. Fluctuations of the geodesic embedding/tangent belong to the M/G localization sectors and the defect mixing calculation, not to the definition of this tree projector. Folding them into `B_mn` here would double-count localization corrections.

## Attack 3 — formal isotropic averaging proves the traceless defect is irrelevant

Rejected. The identity `u -> 1/d` kills the traceless projection only after a full isotropic angular average with no tangent-dependent weight. The fixed-geodesic line form factors depend on `q.n`; therefore the weight is not isotropic and the substitution cannot be made before the line/form-factor integration.

## Attack 4 — the two angular shapes are actually proportional in d=4

Rejected algebraically. In `d=4` the trace and traceless shapes are

`1-u`,

`(1-u)(u-1/4)`.

Their ratio `u-1/4` is not constant. The symbolic implementation checks the general-`d` version by differentiating the ratio with respect to `u`.

## Attack 5 — polynomial tree kernels already determine the separated B1 coefficient

Rejected. `K_RR`, `K_R,Rnn` and the `Box_perp` descendants are polynomial/contact tree kernels. The separated logarithm arises only after the one-loop/geodesic UV structure and defect renormalization are included. ITER122 supplies projectors, not pole residues.

## Attack 6 — the trace/traceless decomposition depends on the gauge

The decomposition `R_nn=R/d+(R_nn-R/d)` is geometric/algebraic. Individual tree contractions are evaluated with the frozen de-Donder propagator, but the exact identity

`K_JS=K_JR/d+K_JTF`

is preserved. The final renormalized fixed-geodesic observable still requires full gauge-consistency checks at loop level.

## Attack 7 — the first script invalidates the symbolic result

No. The first script's defect was a malformed Markdown-output string and it was never used as authoritative CI input. The corrected `v2` implementation contains the symbolic assertions and the workflow references only `v2`. The implementation defect is retained in Git history and documented in the source record.

## Critic verdict

**CONFIRMS `PASS_SCOPED_LINEARIZED_GENUINE_DEFECT_KERNEL_TWO_SHAPE_BASIS`.**

The tensor/projector problem is reduced to a trace-like angular shape and an independent tangent-traceless shape. Neither may be removed before the geodesic form-factor / UV pole calculation.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.