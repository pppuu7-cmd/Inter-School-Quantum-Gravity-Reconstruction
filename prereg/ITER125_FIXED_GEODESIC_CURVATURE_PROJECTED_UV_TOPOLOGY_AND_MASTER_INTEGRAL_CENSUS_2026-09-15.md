# ITER125 preregistration — fixed-geodesic curvature projected UV topology / master-integral census

Date: 2026-09-15
Gate: `ITER125_FIXED_GEODESIC_CURVATURE_PROJECTED_UV_TOPOLOGY_AND_MASTER_INTEGRAL_CENSUS`

## Motivation frozen before topology pruning

ITER124 freezes the complete renormalized RG/pole calculation contract. Before evaluating poles, ITER125 asks whether the one-loop integral problem can be reduced to a small set of scalar denominator families.

The fixed-geodesic matter precedent shows that apparently complicated mixed/pure geodesic corrections reduce after tensor/parameter manipulations to products of massless propagators (`G_0^2`) and renormalized one-scale distributions. Curvature insertions add derivatives/tensor numerators but no new propagating field species or loop order.

## Frozen source/analytic authority

1. arXiv:1706.01891 — explicit one-loop fixed-geodesic field, mixed and pure-geodesic sectors; dimensional regularization; scaleless tadpoles; final reduction to `G_0^2`-type distributions.
2. arXiv:2510.11888 — one-loop scalar-curvature correlator, curvature vertices, graviton/ghost loop structure and contact/noncontact separation.
3. ITER112–124 for F/M/G closure, counterterm basis and projector order.

## Required predicates

A. Classify all ordinary F-sector one-loop two-point graph topologies after treating the curvature insertions as composite external vertices.

B. Determine whether loop-momentum-dependent denominators reduce to the massless two-propagator bubble family

`B_ab(q)=int d^d p /[(p^2)^a ((p+q)^2)^b]`

plus scaleless tadpoles / external propagator factors.

C. Test whether nonlinear curvature insertions plus cubic/quartic action vertices require a genuine triangle/box loop master with three or more independent loop-momentum denominators, rather than merely extra external/fixed propagators or numerator powers.

D. Classify M-sector geodesic dependence as at most one dimensionless line parameter at the operator level, with phase/coordinate factors dressing the same one-loop denominator topology.

E. Classify G-sector dependence as at most two line parameters (`chi_2` or `chi_1 chi_1`) at the frozen order.

F. Distinguish genuinely new **loop denominator topology** from new endpoint/line-parameter integrals. A new line moment is not to be called a triangle master merely because it contains another coordinate integration.

G. Include counterterm insertion graphs separately: their renormalized coefficients/beta functions are required, but a tree-level counterterm insertion is not a new loop master.

H. Identify the minimum scalar master families needed for projected pole extraction, including endpoint/line coincidence integrals that generate defect poles.

I. Retain evanescent/tensor numerator structures as numerator/projector data; do not let their possible existence silently expand or shrink the denominator topology.

J. No EDT target or desired coefficient may influence topology pruning.

## Frozen classifications

- `PASS_SCOPED_ONE_LOOP_BUBBLE_TOPOLOGY_PLUS_ONE_TWO_LINE_PARAMETER_MASTER_FAMILIES` if A-J show that no genuine triangle/box loop denominator is required.
- `PASS_SCOPED_FINITE_MASTER_CENSUS_INCLUDES_TRIANGLE_OR_HIGHER_TOPOLOGY` if additional denominator families are genuinely required.
- `BLOCKED_SOURCE_AUTHORITY` if the F/M/G graph count cannot adjudicate the topology.

## Controls

- `EXTERNAL_PROPAGATOR_TRIANGLE_SWAP_CONTROL`
- `LINE_PARAMETER_LOOP_TOPOLOGY_SWAP_CONTROL`
- `TADPOLE_NONZERO_CONTROL`
- `COUNTERTERM_GRAPH_LOOP_MASTER_CONTROL`
- `EVANESCENT_NUMERATOR_TOPOLOGY_CONTROL`
- `EDT_MASTER_SELECTION_CONTROL`

## Claim ceiling

A PASS only compresses the future pole calculation. It does not evaluate any master integral, pole residue, `B_1`, EDT fit, bridge, new physics or candidate theory.