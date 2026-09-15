# ITER129 preregistration — projected graph numerator derivative census

Date: 2026-09-15
Gate: `ITER129_FIXED_GEODESIC_CURVATURE_PROJECTED_GRAPH_NUMERATOR_DERIVATIVE_CENSUS`

## Motivation

ITER128 closes canonical single-propagator local jet bounds but leaves interaction-dressed two-propagator rows open because the derivative numerator assignment is graph-specific.

ITER129 enumerates the finite `O(kappa^4)` graph/operator families and assigns a conservative total derivative budget before explicit tensor reduction. This is an upper-bound census, not a pole calculation.

## Frozen operator derivative budgets

Count total spacetime derivatives in the local operator/interaction before integrations by parts:

- `R1,R2,R3`: 2 each;
- `partial R1`, `partial R2`: 3 each;
- `partial^2 R1`: 4;
- `Gamma1`: 1;
- `Gamma2`: 1 total on its quadratic metric structure;
- `partial Gamma1`: 2;
- Einstein-Hilbert cubic/quartic interaction vertices `S3,S4`: 2 total;
- ghost-graviton vertices: one derivative on each ghost line / two derivatives total per two-vertex self-energy pair, treated within the same one-loop bubble budget.

## Frozen graph families

### F sector

- `F_R2_R2`;
- `F_R1_R3` plus symmetric counterpart;
- `F_R1_R2_S3` plus symmetric counterpart;
- `F_R1_R1_S4`;
- `F_R1_R1_S3_S3`;
- graviton/ghost self-energy realization of the previous interaction families;
- standard counterterm insertions.

### M sector

- `M_R2_chi1_dR1`;
- `M_R1_chi1_dR2`;
- `M_R1_chi1_dR1_S3`;
- endpoint-initial versus bulk-chi1 subcases kept distinct for affine singularity bookkeeping.

### G sector

- `G_R1_chi2_Gamma2_dR1`;
- `G_R1_chi2_Gamma1_dchi1_dR1`;
- `G_R1_chi2_dGamma1_chi1_dR1`;
- `G_R1_chi1chi1_d2R1`;
- initial/bulk decompositions from ITER127 retained.

## Required predicates

A. Verify each family is compatible with overall `O(kappa^4)` field count/order.

B. Compute the conservative total derivative budget `D_total` for each family from the frozen operator list.

C. For affine singularity analysis, record the maximum derivative order carried by an individual line-connected operator leg (`D_line_max`) and by the local endpoint/interaction leg it can meet (`D_partner_max`).

D. Define the conservative one-propagator local bound `N1_max=D_line_max+D_partner_max` where applicable.

E. For a two-propagator product simultaneously approaching one affine stratum, define the raw conservative bound `N2_total<=D_total`; use `m_raw<=4+D_total` before exact source suppression.

F. Apply only source suppressions frozen by ITER127; do not assume tensor/angular cancellations.

G. Mark pure bulk F-sector rows as having no affine jet requirement even though they contribute to `B1_direct`.

H. Identify scaleless tadpole realizations separately from nonzero bubble/line families; do not infer that an entire operator family vanishes from one tadpole routing.

I. Produce a machine-readable finite table and arithmetic validator.

J. A full PASS requires finite graph-specific ceilings, not exact reduced numerators.

## Frozen classifications

- `PASS_SCOPED_GRAPH_DERIVATIVE_CEILINGS_CLOSED_EXACT_TENSOR_ALLOCATION_OPEN` if A-J close finite ceilings but exact per-propagator tensor allocation remains for loop implementation.
- `PASS_SCOPED_EXACT_GRAPH_DERIVATIVE_ALLOCATION_CLOSED` only if tensor reduction fixes the exact local derivative allocation without further loop algebra.
- `BLOCKED_GRAPH_FAMILY_INCOMPLETE` if an `O(kappa^4)` family cannot be classified.

## Controls

- `TOTAL_DERIVATIVE_EXACT_ALLOCATION_CONTROL`
- `BULK_AFFINE_JET_CONTROL`
- `TADPOLE_FAMILY_ERASURE_CONTROL`
- `SOURCE_SUPPRESSION_TENSOR_CANCELLATION_CONTROL`
- `TARGET_DERIVATIVE_SELECTION_CONTROL`

## Claim ceiling

No derivative ceiling is a nonzero pole. No `B1`, noncancellation result, EDT fit, bridge, new physics or candidate theory follows.