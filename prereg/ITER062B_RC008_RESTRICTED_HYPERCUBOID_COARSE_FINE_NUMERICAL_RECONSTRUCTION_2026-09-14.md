# ITER062B — RC008 restricted hypercuboid coarse/fine numerical reconstruction

Date frozen: 2026-09-14
Parent gate: ITER062A `SCIENTIFIC PASS — RC008_RESTRICTED_AMPLITUDE_KERNEL_SOURCE_CLOSED`.

## Scientific scope

Reproduce, without fitting to the published fixed-point values, the **restricted geometric-sector Riemannian EPRL-FK quantum-cuboid coarse/fine 4-volume-fluctuation comparison** defined by the source-qualified Bahr–Steinhaus construction.

This gate is not full EPRL/FK refinement, not Lorentzian refinement, not q-deformed EPRL/FK, not a continuum-limit gate, and not a cross-school bridge.

## Frozen sources and formulas

- arXiv:1508.07961v2, `QuantumCuboids_article.tex`, SHA256 `ba973b02a05688c2b122c95a111b70b0fe03a126fac399b073725574afc7358b`;
- arXiv:1701.02311, `QuantumCuboidsLong_article.tex`, SHA256 `78415347fa92b1d0bce1bbd4010faeb3cc939c5f5d6b14d72f340138e4c573ef`;
- ITER061 refinement-complex/gluing authority PASS;
- ITER062A source-kernel closure PASS.

The executable large-j dressed hypercuboid amplitude must be constructed from the source chain and may discard only overall factors that are independent of every integration variable and therefore cancel identically in each normalized expectation value:

1. geometric hypercuboid areas
   `j1=Y Z, j2=X Y, j3=X Z, j4=Y T, j5=Z T, j6=X T`;
2. vertex large-j kernel `B_v=1/sqrt(det H)+c.c.` with the exact seven-factor source expression for `det H`;
3. `A_v=A_v^+ A_v^-` and the source large-j gamma prefactor; gamma-only global factors may be dropped only after an explicit cancellation audit;
4. face factor `A_f=((2j^+ +1)(2j^- +1))^alpha`, in the same large-j approximation used by the paper, giving the integration-variable-dependent factor `j^(2 alpha)` after dropping only source-identified gamma-only constants;
5. edge normalization from the source asymptotic cuboid norm, giving the integration-variable-dependent polynomial factors;
6. dressed vertex distribution `prod_{f superset v} A_f^(1/4) prod_{e superset v} A_e^(1/2) A_v`;
7. geometric-sector measure `Delta_FP = J/cos(theta)`, with exact source `cos(theta)` and `J=x y^2 z`;
8. observable `Delta V_1=(V_1-<V_1>)^2`, with symmetry-fixed `<V_1>=V_total/2`;
9. source-defined two-coarse-hypercuboid versus `2x2x2x4=32` fine-hypercuboid comparison at fixed coarse boundary.

No source-dependent factor that varies with an integration variable may be set to one.

## Frozen geometry / coordinates

A published boundary tuple `(X,Y,Z,T)` denotes two coarse hypercuboids whose total fourth-direction extent is `2T` and whose symmetric split is at `T`. This matches the source vertex-translation parametrization and two-coarse-hypercuboid observable construction.

Coarse integral: one internal split `tau in (0,2T)`, giving fourth-direction lengths `tau` and `2T-tau`.

Fine integral: six source-counted geometric variables — one split in each of X,Y,Z and three ordered splits in total extent `2T`. These generate `2x2x2x4=32` fine hypercuboids. The first two fine T-slabs comprise the embedded first coarse hypercuboid for `V_1`.

Lebesgue-domain constants introduced only by mapping unit Sobol coordinates to the source domain cancel in normalized expectations and must be reported rather than silently omitted.

## Frozen boundary states

No boundary is chosen after seeing outputs.

- primary: `B0=(X,Y,Z,T)=(1,1,1,1)`;
- independent reproduction/transport: `B1=(1,1,1,3)`;
- held-out transport 1: `B2=(3,1,1,1)`;
- held-out transport 2: `B3=(3,5,1,1)`.

The same implementation, alpha panel, seeds, sampling powers, convergence criteria and null controls apply to all four. No per-boundary retuning is allowed.

## Frozen alpha panel

`alpha = [0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80]`.

Published fixed-point numbers are not fit targets and are not used to tune this panel after execution. A posteriori comparison to the literature is allowed only after the gate is classified.

## Frozen numerical method

Use Owen-scrambled Sobol quasi-Monte Carlo with independent seeds
`[104729, 130363, 154858]`.

Nested sample powers per seed:
- coarse: `2^12`, `2^14`, `2^16`;
- fine: `2^12`, `2^14`, `2^16`.

All weights are accumulated in log space. Endpoints are not clipped or regularized beyond the intrinsic open sampling of scrambled Sobol points. No epsilon cutoff may be introduced after results are seen. Nonfinite source weights are counted and cause a numerical failure if encountered.

For every alpha, geometry and sample power emit: normalized volume fluctuation, effective sample size, replicate spread, finite-weight fraction and coarse-minus-fine difference.

## Frozen analytic/calibration lane

Before giving scientific credit to numerical lanes, independently check:

- source homogeneity `hat A(lambda j)/hat A(j) = lambda^(12 alpha - 9)` for 32 prospectively fixed anisotropic positive spin fixtures and `alpha=[0.50,0.65,0.80]`, tolerance `1e-10` in relative ratio;
- coordinate-axis relabelling invariance on 24 prospectively seeded geometric hypercuboids, tolerance `1e-10` in relative amplitude;
- `Delta_FP` positivity and finiteness on the same fixtures;
- a deliberately malformed area map must be detected by at least 23/24 anisotropic fixtures with relative shift >= `1e-3`.

Failure of calibration is `INVALID IMPLEMENTATION` unless the exact source algebra itself is shown inconsistent.

## Frozen convergence gate

Scientific convergence is judged on the central alpha subset `[0.55,0.60,0.65,0.70]` at each boundary.

At `2^16`:
- finite-weight fraction must equal `1.0` in all replicates;
- median effective-sample fraction across three seeds must be >= `1e-4` for both coarse and fine integrals;
- coefficient of variation across seed estimates must be <= `0.15` for both coarse and fine normalized observables;
- relative change of the three-seed mean from `2^14` to `2^16` must be <= `0.20` for both coarse and fine normalized observables.

Failure here is `NUMERICAL FAIL / CONVERGENCE NOT ESTABLISHED`, not a scientific failure of RC008.

## Frozen scientific reconstruction predicate

For a boundary whose convergence gate passes, define `D(alpha)=<Delta V_1>_fine - <Delta V_1>_coarse` from the `2^16` three-seed means.

A boundary has a source-reproduction crossing iff:
- `D(alpha)` has at least one sign change between adjacent alpha panel points;
- the sign change is not created solely by a point whose across-seed standard error overlaps both signs;
- linear interpolation is used only to report the bracketed crossing, not to fit or alter weights.

Primary scientific PASS requires B0 convergence + a robust crossing. Full ITER062B scoped PASS additionally requires at least **one of B1/B2/B3** to pass the same non-retuned convergence+crossing predicate. The remaining boundaries are reported as held-out PASS/FAIL/NUMERICAL FAIL without retuning.

If converged B0 has no crossing on the frozen panel, classification is `SCIENTIFIC FAIL — RC008_RESTRICTED_COARSE_FINE_CROSSING_NOT_REPRODUCED_ON_FROZEN_PANEL`.

If B0 crosses but none of B1/B2/B3 crosses under converged non-retuned transport, classification is `SCIENTIFIC FAIL — RC008_RESTRICTED_CROSSING_NOT_TRANSPORTED`.

## Claim locks

Even a full scoped PASS means only numerical reconstruction in the severe symmetry-restricted geometric large-j Riemannian quantum-cuboid truncation. It does not authorize:

- `ALL_KNOWN_SCHOOLS_FAIL`;
- `NEW_QG_THEORY_REQUIRED`;
- `NEW_PHYSICS_FOUND`;
- `BRIDGE_DERIVED`;
- full Riemannian EPRL/FK refinement;
- Lorentzian refinement;
- q-deformed reconstruction;
- candidate action/Hamiltonian/field equations;
- candidate theory construction.

Candidate theory remains `0 / UNFORMED`; bridge credit remains zero unless a later constitution/bridge gate explicitly changes that status.
