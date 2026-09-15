# ITER116 preregistration — corrected fixed-geodesic curvature `O(G^2)` single-log RG hierarchy authority

Date: 2026-09-15
Gate: `ITER116_FIXED_GEODESIC_CURVATURE_G2_SINGLE_LOG_RG_HIERARCHY_AUTHORITY`

## Motivation frozen before residue inference

Corrected ITER114 establishes the separated one-loop basis

`C(l;mu)=G^2 l^-8 [B_0(mu)+B_1(mu)L]+O(G^3)`,

`L=log(mu^2 l^2)`.

The superseded ITER115 was invalidated before adjudication. ITER116 asks what RG consistency fixes about `B_0,B_1` and whether the logarithmic coefficient can be obtained from the highest UV-pole/geodesic-renormalization residue without evaluating all finite one-loop integrals.

## Frozen authority

1. arXiv:1706.01891 — definitions and `mu` derivatives of `H^(1),H^(2)`, plus running finite geodesic renormalization.
2. Corrected ITER114 terminal `8fb4ca397617ed9f0a84e10422acee9088429a8c`.
3. ITER112-113 F/M/G census and nonlocal basis.
4. 2026 master-coordinate curvature result only for perturbative order/curvature-vertex authority; no coefficient import.

## Required predicates

A. Derive the nonzero-separation RG equations for `B_0,B_1`, retaining any running finite observable-specific counterterm.

B. Distinguish explicit `mu` dependence through `L` from implicit running of `B_0,B_1`.

C. Test whether `B_1` is RG invariant at the frozen `O(G^2)` order.

D. Establish whether `B_1 != 0` is sufficient to prove a nonzero separated `O(G^2)` tail independent of the finite constant `B_0`.

E. Determine from the fixed-geodesic renormalization template whether `B_1` is controlled by the highest UV-pole residue / coefficient of the `H^(2)`-type distribution.

F. The matter-scalar numerical residue may not be imported to curvature. In particular the separated tree-level curvature correlator is contact-only and this difference must remain explicit.

G. If `B_1` is not source-fixed, identify the cheapest curvature-specific calculation required to obtain it and whether it is strictly smaller than the full finite `B_0` calculation.

H. No EDT exponent may be used to choose or infer `B_1`.

## Frozen classifications

- `PASS_SCOPED_SINGLE_LOG_B1_NONZERO_PROTECTED_NONCANCELLATION` if A-H establish and source-fix `B_1 != 0`.
- `PASS_SCOPED_SINGLE_LOG_RG_HIERARCHY_HIGHEST_POLE_DIAGNOSTIC_B1_VALUE_OPEN` if the hierarchy and highest-pole diagnostic are established but curvature-specific `B_1` remains uncomputed.
- `PASS_SCOPED_RG_HIERARCHY_ONLY_B1_REQUIRES_FULL_FINITE_CALCULATION` if no residue shortcut exists.
- `BLOCKED_SOURCE_AUTHORITY` if consistent RG typing fails.

## Controls

- `MATTER_B1_CURVATURE_B1_SWAP_CONTROL`
- `TREE_NONCONTACT_ERASURE_CONTROL`
- `EXPLICIT_MU_RUNNING_SWAP_CONTROL`
- `HIGHEST_POLE_FINITE_CONSTANT_SWAP_CONTROL`
- `EDT_LOG_COEFFICIENT_FIT_CONTROL`

## Claim ceiling

Unless the first classification is reached, no noncancellation theorem follows. No EDT fit, direct EDT/EFT conflict, continuum EDT, `BRIDGE_DERIVED`, new physics or candidate theory is authorized.