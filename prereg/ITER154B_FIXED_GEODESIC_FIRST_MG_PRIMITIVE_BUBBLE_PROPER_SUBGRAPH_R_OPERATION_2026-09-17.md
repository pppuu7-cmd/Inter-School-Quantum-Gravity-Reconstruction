# ITER154B preregistration — corrected operator-level primitive-bubble proper-subgraph R-operation

Date: 2026-09-17
Frozen parent `main`: `a85276e5bf8a7518dc037a33d5eb8c9a02ca14f5`
Gate: `ITER154B_FIXED_GEODESIC_FIRST_MG_PRIMITIVE_BUBBLE_PROPER_SUBGRAPH_R_OPERATION`

## Why a repair gate is required

ITER154 prospectively equated the three-site geometric incidence Betti number with loop-momentum topology. Frozen ITER125 contradicts that equivalence: the M-sector loop-dependent core is a two-propagator bubble with at most one independent loop momentum, and the connected G two-point loop likewise reduces to a bubble denominator. ITER154's old hypothesis is not edited; ITER154B freezes the correct graph representation before evaluating its new outcome.

## Scoped scientific question

For the same three immutable ITER141 connected-cross families

- `M_R2_chi1_dR1`,
- `M_R1_chi1_dR2`,
- `G_R1_chi2_Gamma2_dR1`,

is the operator-level one-loop two-propagator bubble **primitive with respect to strict proper ordinary bulk/local-composite UV subgraphs**?

This is still ITER152 slot 6 for the scoped first-M/G connected-cross set. Endpoint/line renormalization remains downstream.

## Frozen operator-level topology

Consume both authorities without conflating them:

- ITER125: loop-dependent core = two-propagator bubble, at most one independent loop momentum; connected G two-point loop also bubble-reduced.
- ITER141: exactly two cross Wick propagator edges for each family; no local/self-pairing in scope; affine endpoint singular strata fixed separately.

Represent the loop core as an effective two-vertex multigraph with two parallel propagator edges:

`V_eff=2`, `E=2`, connected components `C=1`, whole-graph `b1=E-V+C=1`.

The effective vertices are external/composite operator structures; no `S3/S4` action-interaction vertex, ghost loop insertion, self-energy insertion, or same-site self-pairing is present in this scoped cross channel.

## Prospectively frozen hypothesis

> Every strict proper nonempty edge subgraph of the two-edge bubble contains exactly one propagator, has `b1=0`, and cannot be a closed loop subdivergence. Because ITER141 also excludes local/self-pairing and the scoped graph contains no action/ghost interaction insertion, the forest of strict proper ordinary bulk/local-composite subdivergences is empty. Therefore the scoped slot-6 proper-subdivergence operation is `R_sub G = G`.

This derived zero concerns only strict proper subdivergence counterterm insertions. The whole one-loop bubble can still have an overall UV/endpoint divergence and the frozen affine endpoint collisions remain nontrivial downstream objects.

If the immutable ITER125/141 data reveal any strict proper cyclic subgraph, self-energy/tadpole insertion, same-site self-pairing, or additional interaction vertex, classify scientific FAIL rather than retuning.

## Independent methods

A. Effective multigraph enumeration: whole bubble `b1=1`; enumerate every strict proper edge subset and compute its `b1`.

B. Denominator/routing audit: the loop core has exactly the two bubble denominators and one loop momentum; pinching either propagator removes the closed two-edge loop. Verify no nested denominator pair or interaction insertion remains. Independently preserve ITER141 endpoint strata as endpoint/defect, not slot-6 proper subgraphs.

## Controls

Reject: a third propagator/self-energy insertion; a local tadpole/self-pairing; imported S3/S4 or ghost vertex; treating the whole bubble as a *proper* subgraph of itself; treating endpoint collapse as bulk subdivergence; dropping one frozen family; promoting slot-6 zero to contact zero; forming `B1_total`.

## Decision

`PASS_SCOPED_SLOT6_FIRST_MG_PRIMITIVE_BUBBLES_NO_PROPER_SUBDIVERGENCES` iff whole-graph bubble topology is `b1=1`, every strict proper nonempty subgraph is acyclic, no excluded insertion exists, both methods agree, and endpoint strata remain downstream.

`SCIENTIFIC_FAIL_SCOPED_ITER154B_PRIMITIVE_BUBBLE_HYPOTHESIS_FALSE` iff a frozen strict proper UV loop/self-pairing/interaction subgraph exists.

`BLOCKED_SCOPED_ITER154B_SUBGRAPH_AUTHORITY_INCOMPLETE` iff topology requires a proper subtraction but its coefficient is unavailable.

`INVALID_IMPLEMENTATION_ITER154B` for changed sources/scope, geometric-site b1 reused as loop count, endpoint conflation, or claim leakage.

## Successor

If PASS, close slot 6 only for these three cross channels and immediately open slot 7 in the immutable ITER118 endpoint basis. Do not set the seven contacts to zero and do not form `B1_total`.

## Claim ceiling

No contact pole, endpoint coefficient, line mixing, renormalized mapping, terminal ITER124 output, bridge or new physics. Candidate theory remains `UNFORMED / 0%`.