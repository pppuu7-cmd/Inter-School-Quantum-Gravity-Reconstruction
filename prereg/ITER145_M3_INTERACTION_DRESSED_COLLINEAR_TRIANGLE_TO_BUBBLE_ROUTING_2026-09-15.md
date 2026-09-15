# ITER145 preregistration — interaction-dressed M3 routing and collinear triangle-to-bubble reduction

Date: 2026-09-15
Gate: `ITER145_FIXED_GEODESIC_CURVATURE_M3_COLLINEAR_TRIANGLE_TO_BUBBLE_ROUTING`
Status: **FROZEN BEFORE MACHINE EVALUATION**

## Motivation

ITER139 leaves `M_R1_chi1_dR1_S3` on a conservative N1=5 ceiling pending exact interaction allocation. ITER144 now authorizes a pinned cubic-graviton S3 tensor structure (global Euclidean phase still open). Before contracting that tensor, the momentum topology of the nonlocal interaction-dressed M graph must be made explicit and reconciled with ITER125's claim that no genuine triangle master is required.

A hand derivation performed before this preregistration suggests that the generic interior line insertion produces three loop-dependent quadratic denominators, but because all shifts are collinear with the single endpoint Fourier momentum Q they satisfy an exact linear identity and reduce algebraically to bubbles. This gate is confirmatory/adversarial: failure of the identity reopens the relevant ITER125 M-sector topology statement.

## Frozen anchored graph

Coordinates:

- endpoint `x=0` carrying R1;
- endpoint `y=L` carrying dR1;
- chi1 metric insertion `z=tau L`, `0<=tau<=1`;
- cubic interaction point `w`, integrated over spacetime.

For one representative Wick assignment, let propagator momenta from the three operator fields toward S3 be `p`, `k`, `r`, respectively:

- x--w: p;
- z--w: k;
- y--w: r.

Integration over w imposes `p+k+r=0`.

The coordinate-space phase after w integration is frozen as

`exp[-i p.L - i(1-tau) k.L]`.

Fourier transform in the endpoint separation L with external momentum Q imposes, up to the single frozen overall Fourier-sign convention,

`p = -Q-(1-tau)k`,
`r = Q-tau k`.

Changing all Q signs simultaneously is a convention relabeling and must not alter the denominator identity.

## Frozen generic interior denominators

Define

`D1 = [Q+(1-tau)k]^2`,
`D2 = k^2`,
`D3 = [Q-tau k]^2`.

For generic `0<tau<1`, all three depend on k; therefore this gate must **not** claim that one is generically a fixed external propagator.

The preregistered exact identity to test is

`tau D1 + (1-tau) D3 - tau(1-tau) D2 = Q^2`.

For nonzero Euclidean `Q^2`, this implies the integrand-level partial fraction

`1/(D1 D2 D3)`
`= [tau/(Q^2)] 1/(D2 D3)`
` + [(1-tau)/(Q^2)] 1/(D1 D2)`
` - [tau(1-tau)/(Q^2)] 1/(D1 D3)`.

Thus a three-propagator-looking graph may have no independent triangle master even though all three denominators are loop-dependent before the reduction.

## Frozen checks

1. Derive the post-w phase from the four coordinates and the three Wick momenta rather than inserting it by hand.
2. Verify `p+k+r=0` and the endpoint-Fourier routing.
3. Expand D1,D2,D3 in invariants `K=k^2`, `X=k.Q`, `P=Q^2` and verify the exact linear denominator identity.
4. Verify the partial-fraction identity by common-denominator recombination.
5. Verify the same identity under `Q -> -Q` with the correspondingly relabeled p/r routing.
6. Endpoint controls:
   - tau=0: `D3=Q^2` is fixed external and the reduction degenerates consistently;
   - tau=1: `D1=Q^2` is fixed external and the reduction degenerates consistently.
7. Interior control at deterministic rational tau values, with generic symbolic K,X,P left independent.
8. No S3 tensor numerator, pole coefficient, EDT target or desired cancellation enters this topology gate.

## Frozen classifications

- All phase/routing/denominator/partial-fraction/endpoint controls pass:
  `PASS_SCOPED_M3_COLLINEAR_THREE_DENOMINATOR_REDUCES_TO_BUBBLES_ROUTING_CLOSED_NUMERATOR_OPEN`.
- Three-denominator identity or partial-fraction recombination fails:
  `SCIENTIFIC_FAIL_ITER125_M3_BUBBLE_TOPOLOGY_REOPENED`.
- Infrastructure failure before predicates are evaluated:
  `NUMERICAL_OR_INFRASTRUCTURE_FAIL`.

## Scope note

The `1/Q^2` in the algebraic reduction assumes nonzero external Euclidean Q. The Q=0 limit is an IR/contact-degenerate case and is not used here to infer the separated long-range UV pole.

## Claim ceiling

A PASS closes the M3 momentum routing/topology mechanism only. It does not compute the S3-dressed numerator, a master integral, `1/epsilon`, B1, noncancellation, B0, EDT comparison, bridge, new physics or candidate theory. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
