# ITER083B adversarial review — QRC ↔ relational scalar typed map

Date: 2026-09-15
Source-authority commit: `eb9ca64500ff377473e447381afdab7a1202331e`

## Strongest rescue attempts

### Rescue 1 — use the classical small-radius interpretation

Argument: `2006.06263` explicitly relates quantum Ricci curvature to continuum Ricci curvature and its directional average to scalar curvature, while `2112.02118` defines a relational Ricci scalar. Therefore the observables are already the same in the local limit.

Rejection: this supplies a common classical/local target, not a finite-radius typed map. QRC is defined from average distances between geodesic spheres and contains the nonuniversal constant `c_q`; the FRG observable is a local composite operator evaluated in a physical scalar-coordinate frame. The frozen stack does not derive the limiting normalization or expectation-value map connecting them.

### Rescue 2 — average the FRG relational scalar over a sphere

Argument: smear `R_hat(x_hat)` over relational spheres of radius `delta` and compare directly to `K_q(delta)`.

Rejection: such a smeared relational observable is mathematically plausible but is not defined or renormalized in the frozen FRG source. Its measure, relational radius, operator mixing and RG scale dependence would have to be specified prospectively. Introducing it post hoc would change the observable after seeing the target.

### Rescue 3 — use de Sitter agreement as calibration

Argument: both frameworks admit de Sitter-like effective geometries, so use the common constant-curvature background to identify the curvature observables.

Rejection: the preregistered de-Sitter control forbids this. Shape/background agreement does not identify QRC's finite-radius estimator with a relational composite operator, and it would erase the independent-observable requirement.

### Rescue 4 — identify `delta` with `1/k`

Argument: both are resolution scales, so set `delta ~ 1/k`.

Rejection: the sources do not derive this relation. `delta` is a geodesic/dual-link radius in a fluctuating CDT geometry; `k` is an FRG coarse-graining scale. Their operational semantics and normalization remain distinct.

### Rescue 5 — use scaling dimensions only

Argument: FRG scaling dimensions of relational curvature could be compared with scale dependence of QRC.

Rejection: a scaling dimension does not by itself provide a finite observable value map, and the CDT radius-to-physical-scale and FRG trajectory normalizations would still be needed.

## Adversarial verdict

The strongest source-qualified result is a common **local scalar-curvature target** with different finite-resolution realizations.

Terminal-strength classification remains:

**`PASS_SCOPED_LOCAL_LIMIT_CANDIDATE_NORMALIZATION_OPEN`**.

No frozen source supplies the reference-frame, smearing/averaging, normalization or scale map required for `PASS_SCOPED_QRC_RELATIONAL_TYPED_MAP`.

Bridge credit: **0**.
