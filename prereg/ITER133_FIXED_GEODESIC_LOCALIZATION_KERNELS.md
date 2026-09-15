# ITER133 — fixed-geodesic localization-kernel prerequisite gate

Status: **PREREGISTERED BEFORE PRODUCTION COMPUTE**

## Question
Can the missing straight-background fixed-geodesic objects needed by frozen ITER132 be represented as explicit target-blind 4D momentum/tensor kernels without introducing a scalar proxy?

## Frozen scope
Two independent lanes: (A) differentiated linear curvature insertions `dR1`, `d2R1` obtained by exact momentum multiplication of the validated linearized curvature tensor; (B) first geodesic/world-function localization kernel `chi1` on a straight Euclidean segment, retaining its affine parameter and endpoint-reversal transformation. `chi2` is not claimed closed by this gate.

## Frozen checks
A. D=4 symmetric graviton basis. B. exact momentum homogeneity (`R1:2`, `dR1:3`, `d2R1:4`). C. `chi1` remains an affine line kernel, not a local scalar replacement. D. endpoint reversal maps `tau -> 1-tau`, `p -> -p` consistently. E. at least two integer held-out evaluations agree with direct definitions. F. no EDT/B1 target is present.

## Classification
All A–F for the covered objects: `PASS_SCOPED_DERIVATIVE_AND_CHI1_KERNELS_CLOSED_CHI2_OPEN`. Any exact algebraic mismatch: `SCIENTIFIC_FAIL_LOCALIZATION_KERNEL_CONSTRUCTION` unless a purely technical defect is identified. Missing mathematically specified object: `BLOCKED_MISSING_PREREQUISITE`.

PASS does not reopen full ITER132 until `chi2` and all required differentiated localization variants are separately frozen and validated. Candidate theory remains 0/UNFORMED; bridge credit 0.