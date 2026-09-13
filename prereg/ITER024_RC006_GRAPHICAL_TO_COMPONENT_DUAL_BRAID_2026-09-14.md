# ITER024 preregistration — graphical-to-component qbar dual and braiding

Date: 2026-09-14

## Basis
Authoritative ITER023 terminal aggregate is `RC006_QBAR_INDEX_ORDER_BLOCKED`: the target source contains the graphical cup/qbar and R relations, but does not print the full component index formulas. ITER024 prospectively derives those component formulas from the frozen graphical identities and tests them independently. ITER023 is not reclassified.

Primary source: arXiv:1609.02429v2, e-print SHA256 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

No external q-CG formula, phase fit, post-output sign table, Hermitian-adjoint substitution, or physics amplitude is allowed.

## Frozen derived component dictionary

### qbar dual
For ordered source labels `(j1,j2)->j`, the graphical split has geometric output order `(j2,j1)`. Construct the inverse-parameter embedding at `qbar=q^-1` on the reversed tensor product `(j2,j1)`. For source component indexing `(m1,m2)`, apply only the deterministic permutation from geometric `(m2,m1)` rows back to `(m1,m2)`.

Convert Appendix-A `C` to Appendix-B `mathcal C` by `1/sqrt(d_j)`.

Frozen checks:
1. `F_q(j1,j2->j) D_qbar(j->j1,j2) = (-1)^(j1+j2-j) d_j^-1 I`;
2. for `(j,j)->0`, `D_qbar = cup_j/sqrt(d_j)`;
3. geometric qbar embedding intertwines the qbar coproduct on reversed tensor order.

### R crossing
The source graphical R channel uses the same normalized q-CG channel on the lower and upper trivalent vertices. After cancelling the explicit source factor `d_j` against the two `1/sqrt(d_j)` graphical coefficients, the component crossing is prospectively fixed as

`R_ab = sum_j s_abj q^{-(C_a+C_b-C_j)/2} C_ba^j (C_ab^j)^T`,
where `s_abj=(-1)^(a+b-j)` is the graphical orientation sign inherited from the source q/qbar composition identity, and `C_x=j_x(j_x+1)`.

The source inverse uses the opposite exponent. No channel-dependent correction is allowed after production output.

## Frozen panels
Levels `k=6,10,12`.

qbar panel: all admissible outputs for `(1/2,1/2)`, `(1,1/2)`, `(2,1)` when labels fit, plus at k=12 `(4,2)` and `(3,3)`.

R panel: same pairs. Yang-Baxter panels, kept away from trace-zero pair sectors: `(1/2,1/2,1/2)`, `(1,1/2,1/2)`, `(1,1,1/2)` at k=6,10,12; plus `(2,1,1/2)` and `(2,1,1)` at k=10,12.

## Parallel lanes

A. `dual`: q/qbar composition, qbar intertwiner and cup-singlet checks. PASS thresholds all `<2e-9`.

B. `R`: crossing intertwining for Jz/J+/J- and source inverse composition. PASS thresholds all `<5e-9`.

C. `braid`: Yang-Baxter max residual `<2e-8`; undeformed q=1 construction equals ordinary tensor swap for frozen low-spin pairs `<2e-10`.

D. `null`: test four wrong variants: omit orientation sign; use qbar top vertex in R; use non-reversed qbar tensor order; flip the forward-source R exponent when checking the forward channel coefficient. PASS requires at least 3/4 wrong variants detected by residual `>1e-6`, while the correct control passes.

## Aggregate
Run A-D concurrently with `fail-fast:false`. Green CI is not scientific PASS.

Terminal classes:
- `RC006_GRAPHICAL_DUAL_BRAID_COMPONENT_PASS`
- `RC006_GRAPHICAL_QBAR_COMPONENT_FAIL`
- `RC006_GRAPHICAL_R_COMPONENT_FAIL`
- `RC006_GRAPHICAL_BRAID_COHERENCE_FAIL`
- `RC006_GRAPHICAL_DUAL_BRAID_CALIBRATION_FAIL`
- `RC006_GRAPHICAL_DUAL_BRAID_INFRASTRUCTURE_PARTIAL`

Only the full PASS may authorize a new executable Eq.(27) contraction preregistration. TNR, Eq.(29)/Lambda, alpha selection, bridge/candidate/new-physics claims remain forbidden.