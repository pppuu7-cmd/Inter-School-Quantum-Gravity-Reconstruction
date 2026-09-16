# ITER154 preregistration — first-M/G graph-specific proper-subdivergence R-operation authority

Date: 2026-09-17
Frozen parent `main`: `d5ca2a3203b689964f50e2723b7bc6a30217708b`
Gate: `ITER154_FIXED_GEODESIC_FIRST_MG_GRAPH_SUBDIVERGENCE_R_OPERATION_AUTHORITY`

## Objective

Attack the exact primitive exposed by ITER153 without repeating the slot-5 pullback audit. Determine, for the three frozen connected-cross first-M/G families only, the **graph-specific ordinary bulk / local-composite proper-subdivergence subtraction map** required by ITER124 before endpoint/line renormalization.

This is ITER152 slot 6 for the current first-M/G cross-channel subset. Endpoint/geodesic counterterms, line-defect mixing, renormalized contact mapping and `B1_total` remain downstream and may not be inferred here.

## Frozen graph families and Wick edges

Consume `analysis/iter141_first_mg_wick_geometry_phase_strata.py` at the frozen parent byte-for-byte. The only in-scope connected-cross families are:

1. `M_R2_chi1_dR1`
   - sites: endpoint `x=0`, line point `z_tau=tau L n`, endpoint `y=L n`;
   - Wick edges: `R2_q -- chi1_minus_q` and `R2_k -- dR1_minus_k`;
   - affine edge separations: `tau L` and `L`.

2. `M_R1_chi1_dR2`
   - sites: `x`, `z_tau`, `y`;
   - Wick edges: `R1_minus_q -- dR2_q` and `chi1_minus_k -- dR2_k`;
   - affine edge separations: `L` and `(1-tau)L`.

3. `G_R1_chi2_Gamma2_dR1`
   - sites: `x`, `z_tau`, `y`;
   - Wick edges: `R1_minus_q -- Gamma2_q` and `Gamma2_k -- dR1_minus_k`;
   - affine edge separations: `tau L` and `(1-tau)L`.

ITER141's scope lock `local/self-pairing quadratic channel remains a separate renormalization sector` is binding. No self-pairing/tadpole may be silently inserted into this gate.

## Frozen topological hypothesis

Before outcome, freeze the following concrete hypothesis:

> For each of the three in-scope connected-cross first-M/G Wick graphs, after treating each local composite/geodesic insertion point as a vertex and each frozen cross Wick contraction as an edge, the graph has exactly `V=3`, `E=2`, one connected component and first Betti number `b1=E-V+1=0`. There is no action-interaction vertex (`S3/S4`), no closed momentum cycle, and no local/self-contraction. Therefore there is no proper ordinary bulk-loop or same-site local-composite **subdivergence subgraph** inside these three cross channels. Their nontrivial UV singular strata are only the already-frozen affine endpoint collisions of ITER141/143/153.

If the frozen graph data falsify this statement, classify `SCIENTIFIC_FAIL_SCOPED_ITER154_TOPOLOGICAL_PRIMITIVITY_HYPOTHESIS_FALSE` rather than repairing the hypothesis post-outcome.

## Exact distinction: subdivergence versus endpoint/overall divergence

A `proper subdivergence` in this gate means a strict proper subgraph requiring an ordinary bulk or same-site local-composite counterterm insertion before the endpoint/line renormalization step of ITER124.

The following are NOT to be called slot-6 proper subdivergences here:

- `tau -> 0` or `tau -> 1` affine endpoint collapse;
- the seven denominator-cancelled endpoint contacts of ITER151/153;
- endpoint/geodesic counterterms (slot 7);
- line-defect mixing (slot 8);
- local/self-pairing sectors explicitly excluded by ITER141;
- F-sector graphs with `S3/S4`, graviton/ghost self-energy, quartic/tadpole, or counterterm insertions from the broader ITER112/125 census.

Those remain separate sectors/dependencies.

## R-operation output

For each in-scope family, construct an exact graph record:

- vertex/site set;
- edge set;
- connected components;
- cycle rank / first Betti number;
- all strict proper connected edge-induced subgraphs;
- whether any proper subgraph contains a cycle;
- whether any proper subgraph contains a same-site self-contraction;
- whether an `S3/S4`/ghost/bulk interaction vertex occurs;
- list of endpoint singular strata from ITER141;
- slot-6 subtraction operator.

If the frozen topological hypothesis passes, the graph-specific proper-subdivergence counterterm map for these cross channels is exactly the identity:

`R_sub G = G`

with zero inserted **proper bulk/local-composite subdivergence counterterms** for this scoped family set. This is a derived zero about slot-6 subtractions only; it is not a zero contact pole, endpoint counterterm, line mixing coefficient or full renormalized graph.

## Independent methods

Require two independent exact routes:

A. graph-theoretic enumeration from the frozen ITER141 site/edge data, including explicit cycle-rank and strict proper-subgraph enumeration;

B. momentum/coordinate routing audit: verify there is no integrated action-interaction vertex or closed momentum-conservation loop and that at fixed `0<tau<1` every propagator separation is nonzero; singular support arises only when a line edge collapses at a frozen endpoint stratum.

These methods must agree before a derived-zero slot-6 subtraction is accepted.

## Controls

Reject/trigger for the correct reason:

- add a third edge closing a triangle among `x,z,y`;
- add an `S3` bulk interaction vertex and loop edges;
- add a same-site self-pairing at a quadratic vertex;
- misclassify endpoint `tau->0,1` collapse as an ordinary bulk subdivergence;
- drop a frozen Wick edge;
- change one of the three families;
- import ITER125's broader F-sector bubble/self-energy census into these cross channels;
- interpret `R_sub G=G` as contact pole zero;
- form `B1_total`.

## Decision rule

`PASS_SCOPED_SLOT6_FIRST_MG_CROSS_CHANNEL_PROPER_SUBDIVERGENCES_EMPTY` iff all three frozen graph records have `V=3`, `E=2`, one component, `b1=0`, no same-site self-pairing, no action/ghost interaction vertex, every strict proper connected subgraph is acyclic, both independent methods agree, controls pass, and the only UV singular strata are frozen endpoint collapses assigned downstream.

`BLOCKED_SCOPED_ITER154_GRAPH_SUBDIVIDENCE_AUTHORITY_INCOMPLETE` iff the exact graph topology is known but a required ordinary bulk/local-composite proper-subgraph coefficient exists and cannot be source-faithfully supplied.

`SCIENTIFIC_FAIL_SCOPED_ITER154_TOPOLOGICAL_PRIMITIVITY_HYPOTHESIS_FALSE` iff the frozen concrete topological hypothesis is falsified by the immutable parent graph data.

`INVALID_IMPLEMENTATION_ITER154` for changed graph set/edges, imported self-pairings/F-sector interactions, endpoint-vs-subdivergence conflation, hard-coded desired zeros, or missing lineage/provenance.

Infrastructure failure is not a scientific FAIL.

## Successor rule

If PASS, mark slot 6 closed **only for the current first-M/G connected-cross family set** and immediately open the minimal slot-7 divergent endpoint-counterterm coefficient gate. Do not close slot 5 numerically yet: ITER153 established that the endpoint local distribution is fixed only after endpoint/line renormalization data are included. Slot 7 must therefore carry the exact endpoint basis frozen by ITER118 and derive divergent coefficients without changing that basis.

## Claim ceiling

No contact pole value, endpoint counterterm coefficient, line-defect mixing, renormalized contact mapping, `B1_direct`, `beta_defect`, `B1_defect`, `B1_total`, noncancellation, EDT bridge, new physics or candidate theory follows from ITER154. `BRIDGE_DERIVED=false`, `NEW_PHYSICS_FOUND=false`, candidate theory remains `UNFORMED / 0%`.