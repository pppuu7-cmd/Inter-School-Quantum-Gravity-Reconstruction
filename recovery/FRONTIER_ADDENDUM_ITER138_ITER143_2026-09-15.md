# ISQGR recovery frontier addendum — ITER138 through active ITER140/ITER143

Date: 2026-09-15
Repository: `pppuu7-cmd/Inter-School-Quantum-Gravity-Reconstruction`

This addendum follows `recovery/ITERATION_ID_RECONCILIATION_2026-09-15.md` and preserves the post-reconciliation original-calculation frontier.

Candidate theory: **UNFORMED / 0%**.
Bridge credit: **0**.
No B1 value, noncancellation result, EDT match, new physics or candidate theory is authorized.

## ITER138 — terminal

Classification:

`PASS_SCOPED_FIRST_MG_EXACT_NUMERATOR_KERNELS_CLOSED_ITER129_SINGLE_LINE_CEILING_REOPENED`.

Exact connected Gaussian D=4 numerators were closed for:

- `M_R2_chi1_dR1`: total degree 6, q-degree 3, k-degree 5;
- `G_R1_chi2_Gamma2_dR1`: total degree 6, q-degree 3, k-degree 4.

Independent ten-component Wick contractions and rational-unit-vector panels pass exactly. The M row proves that the old ITER129 row-specific N1=4 is too low although the global N1<=5 ceiling remains valid.

Terminal result: `7104b169ad2c4196b621a632f93ce2714858e0a7`.

## ITER139 — terminal

Classification:

`PASS_SCOPED_AFFINE_SINGLE_LINE_CEILING_REPAIR_CLOSED_ENDPOINT_POLES_OPEN`.

The second Gaussian M family `M_R1_chi1_dR2` was computed exactly: total degree 6, q-degree 5, k-degree 4, with exact direct-basis held-outs. The row-specific nonlinear allocation rule `N1=D_line_max+D_partner_max` is not generally conservative because nonlinear-vertex derivatives can concentrate on one internal line.

A prospective V2 table preserves the global affine bound 5:

- M1 exact 5;
- M2 exact 5;
- M3 conservative 5 pending exact S3 allocation;
- direct-Gamma2 G1 exact 4;
- previously unclosed old-4 G rows lifted conservatively to 5 unless exact allocation is available.

Historical ITER129 evidence is unchanged.

Terminal result: `a4149974b6f484dd9b3083addcd73b76cea27b73`.
Corrected table: `analysis/iter139_affine_single_line_ceiling_table_v2.json`.

## ITER141 — terminal geometry/phase authority

Classification:

`PASS_SCOPED_FIRST_MG_WICK_GEOMETRY_PHASE_AND_SINGULAR_STRATA_CLOSED_LOCAL_POLES_OPEN`.

Anchored geometry `x=0`, `y=L n`, `z(tau)=tau L n`, L>0, gives the actual connected-cross affine singular strata:

- M1: lower `tau->0` only; edge lengths `tau L` and `L`;
- M2: upper `tau->1` only; edge lengths `L` and `(1-tau)L`;
- G1: both endpoints; edge lengths `tau L` and `(1-tau)L`.

Exact Fourier phase factorizations were derived from field momenta and insertion coordinates, not chosen post hoc.

Terminal result: `6d3811bb30e08a6ca8fae42796c01d3a8c370e24`.

## ITER142 — terminal sharp shrinking-edge jets

Classification:

`PASS_SCOPED_FIRST_MG_SHRINKING_EDGE_DERIVATIVE_JETS_CLOSED_LOCAL_RESIDUES_OPEN`.

The relevant local derivative count is the degree on the Wick edge whose separation actually vanishes, not the maximum degree on any companion line:

- M1 lower uses q-degree 3 -> `m_raw<=5`, jet<=4;
- M2 upper uses k-degree 4 with `(1-tau)` suppression -> `m_raw<=6`, jet<=4;
- G1 lower uses q-degree 3 -> jet<=4;
- G1 upper uses k-degree 4 with suppression -> jet<=4.

Thus all first-three connected M/G singular endpoints require at most Taylor order 4 before denominator-cancellation/contact reduction. The global ITER139 bound remains unchanged for other rows.

Terminal result: `5c28b50517f1c3eefb705b6ca392e6ffc4e8a234`.

## ITER140 — active general-d authority

Gate:
`ITER140_FIXED_GEODESIC_CURVATURE_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION`.

Preregistration: `f91daaadedc4fed689fe56ad6a193c54b467ae67`.
Implementation: `1b68324cc4cd6a58b829e40dbcc163e3a00ec44d`.
Workflow head: `32436dcb39251dc4e6904870f1df62714e988f52`.
Authoritative run in progress: `34958007179`, job `104344580789`.

Frozen task: reconstruct exact general-d coefficients for M1/M2/G1 in the 28-element invariant basis `Q,K,S,a,b`, train on D=3..7, validate without refit on D=8..10, cross-check D=4 against ITER138/139, and emit O(epsilon) coefficients for `d=4-2 epsilon`. No pole integration occurs in ITER140.

Physical reason: ITER124 requires general d and higher-pole consistency; D=4 tensors alone cannot authorize a renormalized simple pole when O(epsilon) numerator pieces may multiply higher poles.

## ITER143 — preregistered, blocked on ITER140 output

Gate:
`ITER143_FIXED_GEODESIC_CURVATURE_FIRST_MG_DENOMINATOR_CANCELLATION_CONTACT_PARTITION`.

Preregistration: `090e5a779ca1a6e1802cf0c10eeb9abb4a0823ae`.

The frozen partition is fixed before ITER140 coefficients are inspected. For numerator basis term `Q^i K^j ...` over propagator denominator `Q K`:

- i=0,j=0: genuine two-propagator candidate;
- i>=1,j=0: q-edge contact with k propagator retained;
- i=0,j>=1: k-edge contact with q propagator retained;
- i>=1,j>=1: both propagators cancelled, fully local/distributional.

ITER141 geometry then decides separated-L support. Contact on an edge fixed at L>0 is zero in the separated correlator; only contact on the edge that actually shrinks can survive as an endpoint-local counterterm/mixing contribution. Fully cancelled terms have incompatible simultaneous endpoint support for fixed L>0 and are separated-contact zero.

## S3 interaction-dressed branch — prerequisite status

`M_R1_chi1_dR1_S3` remains on the conservative ITER139 global N1=5 ceiling; exact tensor allocation is open because no source-qualified cubic graviton `S3` authority has yet been imported into this repository.

Current external source candidates identified, but not yet credited:

- David Prinz, arXiv:2004.09543, explicit gravity-matter Feynman rules in linearized de Donder gauge;
- David Prinz, arXiv:2208.14166, explicit propagators and three-valent vertices and de Donder transversality identities;
- Gustav Uhre Jakobsen, arXiv:2010.08839, general n-graviton vertex framework with arbitrary-D applications;
- public `BorisNLatosh/FeynGrav` machine library, pinned tree observed at commit `91f697a1ca62fd051cbb297827cb1a491b393538`, including a machine-readable three-graviton `Libs/GravitonVertex_1` object. Its package documentation states that `GaugeFixingEpsilon` controls the propagator and does not enter `GravitonVertex`, so convention matching must be audited before use.

Do not reconstruct S3 from memory or consume these candidates as authority until a separate preregistered source/convention gate passes.

## Exact next actions

1. Finish/adjudicate ITER140 without changing its frozen 28-basis or degree<=4 trace bound.
2. If ITER140 passes, implement ITER143 from its exact general-d coefficient table and ITER141/142 geometry/jet authorities.
3. Only after ITER143 partition should any first M/G master pole be evaluated.
4. In an independent branch, preregister a cubic-graviton S3 source/convention authority before attempting the interaction-dressed M3 numerator.
