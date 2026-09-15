# ITER128 source authority — projected local singular-degree / Taylor-jet census

Date: 2026-09-15
Gate: `ITER128_FIXED_GEODESIC_CURVATURE_PROJECTED_LOCAL_SINGULAR_DEGREE_CENSUS`
Preregistration: `prereg/ITER128_FIXED_GEODESIC_CURVATURE_PROJECTED_LOCAL_SINGULAR_DEGREE_CENSUS_2026-09-15.md`
Machine table: `analysis/iter128_local_singular_degree_table.json`
Validator: `analysis/iter128_validate_local_singular_degree_table.py`
Workflow artifact: `iter128-local-singular-degree-table`

## 1. Local power-counting rule

For a massless propagator in `d=4-2 epsilon`,

`G_d(r) ~ r^(-2+2 epsilon)`.

If a local singular kernel has `N` total derivatives acting across one propagator, its superficial one-variable affine behavior is

`x^[-(2+N)+2 epsilon]`.

Thus

`m_raw=2+N`.

If the exact ITER127 Green/affine weight supplies `s` powers of suppression at that stratum,

`m_eff=m_raw-s`.

By ITER126, the one-variable Taylor coefficient potentially controlling the logarithmic pole is then

`k=m_eff-1`.

For a two-propagator local product, the correct separate base is

`m_raw=4+N`.

Predicates A-D: **PASS**.

## 2. Canonical endpoint examples

### Anchor R1 against line Gamma1

Derivative count:

`N=2+1=3`, hence `m_raw=5`.

- lower endpoint `tau->0`, no source suppression: `m_eff=5`, jet order `k=4`;
- upper endpoint `tau->1`, outer source weight `(1-tau)` gives `s=1`: `m_eff=4`, `k=3`.

### Anchor R1 against line partial-Gamma1

`N=2+2=4`, hence `m_raw=6`.

- unsuppressed endpoint: `k=5`;
- endpoint with one Green weight: `m_eff=5`, `k=4`.

Predicate G/H: **PASS_CANONICAL**.

## 3. Canonical line-line diagonal examples

### Gamma1 against Gamma1

`N=1+1=2`, `m_raw=4`.

For the ITER127 sectors where the diagonal is not Green-suppressed, `m_eff=4` and the required local Taylor order is `k=3`.

### partial-Gamma1 against Gamma1

`N=2+1=3`, `m_raw=5`.

- without an inner Green factor: `k=4`;
- in the ITER127 `(partial Gamma1) chi1_bulk` term, the exact `(tau-sigma)` weight gives `s=1`, hence `m_eff=4`, `k=3`.

This explicitly quantifies the gain from the source-qualified nested Green kernel.

Predicates B/H: **PASS_CANONICAL**.

## 4. Genuine defect endpoint ceiling

The linear genuine defect representatives have four derivatives at the line insertion:

`Box_perp R`, `Box_perp R_nn`.

Against anchor `R1` with two derivatives,

`N=6`, `m_raw=8`.

With no extra source Green suppression for the uniform line counterterm insertion, the canonical endpoint jet requirement is

**`k=7`.**

This is the strongest canonical one-propagator local jet bound in the retained dimension-4 defect basis.

## 5. Global residual defect one-variable ceiling

After ordinary bulk subdivergences are removed, ITER118 bounds the residual line/endpoint counterterm basis to linear geometric dimension four. Therefore a line operator carries at most four derivatives, and with the anchor curvature at most six derivatives act across a single residual propagator.

Consequently, within the counterterm-projected residual single-propagator sector,

`N_max=6`, `m_max=8`, `k_max=7`.

This is a **post-subtraction residual-defect ceiling**, not a statement that every raw F/M/G integrand is no more singular than `x^-8`.

Predicate F: **PASS_CONTROL**.

## 6. Two-propagator products remain graph-specific

For a product of two local propagators approaching one singular stratum,

`m_eff=4+N-s`,
`k=m_eff-1`.

However the actual `N` depends on how curvature, action and geodesic derivatives are distributed across the two propagators in a specific interaction-dressed F/M/G graph.

ITER128 does **not** have enough graph-specific numerator authority to assign one universal integer jet order to every such row without constructing those projected integrands.

Therefore the full interaction-dressed table is still open, even though the rule and all canonical one-propagator bounds are closed.

Predicate C/E: **PASS_RULE / GRAPH-SPECIFIC INPUT OPEN**.

## 7. Superficial degree is not a residue

A nonnegative superficial pole opportunity can disappear because of:

- tensor contractions;
- Bianchi identities;
- odd angular structures;
- gauge cancellations;
- vanishing local Taylor coefficients;
- subtraction against endpoint/line counterterms.

No row in the machine table is therefore marked as a nonzero `B1` contribution.

Predicate F/J: **PASS_CONTROL**.

## Source classification

**`PASS_SCOPED_CANONICAL_JET_BOUNDS_CLOSED_INTERACTION_SPECIFIC_ROWS_OPEN`**

ITER128 closes the local-subtraction complexity for the source-geodesic and genuine-defect canonical kernels, with a finite residual single-variable jet ceiling of seven. Interaction-dressed two-propagator rows still require the actual projected graph numerator assignment.

## Highest-information successor

`ITER129_FIXED_GEODESIC_CURVATURE_PROJECTED_GRAPH_NUMERATOR_DERIVATIVE_CENSUS`

Enumerate each interaction-dressed F/M/G graph family from ITER112/125 and assign how many derivatives land on each loop/line propagator after the ITER123 projector. The output should be a finite per-graph `(propagator count,N,s,jet)` table, not a loop integral evaluation.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No superficial bound is a pole residue; no `B1`, noncancellation theorem, EDT fit, direct discrepancy, bridge or new physics follows.