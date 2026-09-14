# ITER102 adversarial critic — directional QRC traceless-Ricci route

Date: 2026-09-15
Gate: `ITER102_DIRECTIONAL_QRC_TRACELESS_RICCI_RELATIONAL_TENSOR_AUTHORITY`
Source authority: `473c0904e737f7dadd5314dae6605cddefe77acd`

## Attack 1 — the residual is just another scalar-curvature measurement

Rejected. The subtraction

`Q(v)-<Q>_Omega = -0.0469 delta^2 [Ric(v,v)-R/4] + O(delta^3)`

removes the trace contribution. For varying physical directions `v`, the leading residual probes the traceless symmetric Ricci tensor rather than `R`.

## Attack 2 — formal relational tensor semantics equal an explicit FRG flow

Rejected. The source explains how physical coordinate frames make tensor components relationally meaningful and says the formalism generalizes to other tensors. It does not compute the specific traceless-Ricci composite mixing/anomalous dimension. The classification must retain `FLOW_OPEN`.

## Attack 3 — a coordinate basis vector can stand in for the QRC direction

Rejected. The QRC direction is geometric: it is defined by the tangent to the geodesic connecting the sphere centres in the smooth limit. A relational implementation needs a physical-frame tangent/contraction. Abstract coordinate axes alone are gauge-dependent.

## Attack 4 — vanishing on the self-consistent S4 proves the quantum traceless channel vanishes

Rejected. The round FRG background has traceless Ricci zero, but the CDT/FRG quantum observable is an expectation of a tensor composite over fluctuations. `S[g_sc]=0` does not imply `<S[g]>=0` without expectation/operator authority.

## Attack 5 — equality of two measured directional classes would prove `S_ij=0`

Rejected in advance. Even exact equality between selected spacelike/timelike projections does not determine all independent components of a four-dimensional traceless symmetric tensor unless symmetry/isotropy assumptions are separately source-qualified.

## Attack 6 — coefficient is the renormalized tensor matching factor

Rejected. `0.0469` (or `0.0469/1.6524` in QRC normalization) is the smooth geometric expansion coefficient. A relational traceless-Ricci composite can have nontrivial renormalization/mixing. ITER102 establishes operator typing, not a completed renormalized matching factor.

## Critic verdict

**CONFIRMS `PASS_SCOPED_TRACELESS_RICCI_QRC_CHANNEL_FORMAL_RELATIONAL_TENSOR_ROUTE_FLOW_OPEN`.**

The channel is independent of the scalar leading term and worth preserving, but it does not yet support a quantum numerical crosswalk.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.