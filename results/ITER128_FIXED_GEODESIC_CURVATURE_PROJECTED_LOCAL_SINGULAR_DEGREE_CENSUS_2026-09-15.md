# ITER128 terminal result — projected local singular-degree / Taylor-jet census

Date: 2026-09-15
Gate: `ITER128_FIXED_GEODESIC_CURVATURE_PROJECTED_LOCAL_SINGULAR_DEGREE_CENSUS`
Preregistration: `prereg/ITER128_FIXED_GEODESIC_CURVATURE_PROJECTED_LOCAL_SINGULAR_DEGREE_CENSUS_2026-09-15.md`
Source authority: `sources/ITER128_FIXED_GEODESIC_CURVATURE_PROJECTED_LOCAL_SINGULAR_DEGREE_CENSUS_2026-09-15.md`
Adversarial review: `results/ITER128_ADVERSARIAL_CRITIC_2026-09-15.md`
Machine table: `analysis/iter128_local_singular_degree_table.json`
Validator: `analysis/iter128_validate_local_singular_degree_table.py`
Workflow artifact: `iter128-local-singular-degree-table`

## Terminal classification

**`PASS_SCOPED_CANONICAL_JET_BOUNDS_CLOSED_INTERACTION_SPECIFIC_ROWS_OPEN`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Local subtraction rule

For one residual massless propagator in `d=4-2 epsilon`,

`m_raw=2+N`,

where `N` is the total derivative count at the local singular stratum. If the exact ITER127 affine weight suppresses that stratum by `s` powers,

`m_eff=m_raw-s`,

and ITER126 requires at most the Taylor coefficient

**`k=m_eff-1`**

for a one-variable pole extraction.

For two-propagator local products the separate base is

`m_raw=4+N`.

## Closed canonical bounds

- `R1` ↔ `Gamma1`: lower endpoint `k=4`; upper endpoint with `(1-tau)` `k=3`.
- `R1` ↔ `partial Gamma1`: unsuppressed `k=5`; one Green suppression `k=4`.
- `Gamma1` ↔ `Gamma1` line diagonal: `k=3` if unsuppressed.
- `partial Gamma1` ↔ `Gamma1`: `k=4` unsuppressed, reduced to `k=3` by the source `(tau-sigma)` factor.
- `R1` ↔ `Box_perp R` or `Box_perp R_nn`: canonical endpoint ceiling `k=7`.

The last row is the strongest canonical one-propagator residual-defect jet requirement in the ITER118 dimension-four counterterm basis.

## Scope boundary

The finite `k<=7` ceiling applies to the **post-bulk-subtraction residual single-propagator defect sector**. Raw interaction-dressed F/M/G integrands can be more singular before the mandated ITER124 cancellations/subtractions.

Two-propagator products obey the finite rule

`k=3+N-s`,

but their actual `N` is graph-specific and remains open until the projected interaction numerator is assigned.

## Exact successor

`ITER129_FIXED_GEODESIC_CURVATURE_PROJECTED_GRAPH_NUMERATOR_DERIVATIVE_CENSUS`

Enumerate the interaction-dressed F/M/G graph families and assign, after the fixed projector conventions are imposed, how many derivatives act on each loop/line propagator. Produce a finite `(family, propagators, derivative allocation, affine suppression, local jet)` table. Do not evaluate loop integrals or infer nonzero residues from derivative count alone.

## Claim ceiling

No superficial bound is a pole residue. No `B1`, noncancellation theorem, EDT fit or direct discrepancy, bridge, new physics or candidate theory follows.