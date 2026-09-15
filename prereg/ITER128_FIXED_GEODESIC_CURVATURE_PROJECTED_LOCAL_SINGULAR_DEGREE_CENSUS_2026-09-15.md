# ITER128 preregistration — projected local singular-degree / Taylor-jet census

Date: 2026-09-15
Gate: `ITER128_FIXED_GEODESIC_CURVATURE_PROJECTED_LOCAL_SINGULAR_DEGREE_CENSUS`

## Motivation

ITER126 gives the local residue rule once the singular exponent and smooth weight are known. ITER127 supplies exact affine polynomial weights. ITER128 determines the derivative-induced local singular degree needed to know how deep the Taylor expansion must go before any actual curvature pole coefficient is calculated.

## Frozen scope

This gate classifies **residual endpoint/line-defect kernels after ordinary bulk subdivergences have been subtracted** according to ITER124. It does not replace the full interaction/tensor calculation.

For a massless propagator in `d=4-2 epsilon`,

`G_d(r) ~ r^(-2+2 epsilon)`.

A total of `N` derivatives acting across a single propagator gives the local scaling upper bound

`partial^N G_d(l x) ~ x^[-(2+N)+2 epsilon]`.

For a product of two propagators approaching the same local stratum,

`G_d^2` starts at `x^(-4+4 epsilon)` before derivatives.

## Frozen derivative content

- local `R1`: two derivatives of one metric field;
- `Gamma1`: one derivative of one metric field;
- `partial Gamma1`: two derivatives of one metric field;
- the residual linear part of `Gamma2` after subdivergence/operator reduction carries at most one derivative on the line-connected field;
- `Box_perp R`: four derivatives of one metric field at linear order;
- source Green weights/suppressions are exactly those frozen by ITER127.

## Required predicates

A. For each one-propagator endpoint kernel, compute the raw `m=2+N` and effective `m_eff=m-s`, where `s` is the exact source polynomial suppression order at that stratum.

B. For line-line single-propagator kernels, apply the same rule using the derivative orders at the two line insertions.

C. For two-propagator local products, use the separate base rule `m=4+N`; do not alias them to the one-propagator formula.

D. Translate every integer `m_eff>=1` into the ITER126 Taylor-jet requirement `k=m_eff-1` for a local one-variable stratum.

E. Keep overlapping two-variable/corner strata separate: the one-variable jet order is only a sector ingredient; forest/sector subtraction remains mandatory.

F. Distinguish **superficial upper bound** from actual pole: tensor contractions, Bianchi identities, gauge cancellations, odd-parity angular factors or vanishing Taylor coefficients can lower or eliminate a residue.

G. Compute at least the following canonical residual bounds:

- anchor `R1` ↔ line `Gamma1`;
- anchor `R1` ↔ line `partial Gamma1`;
- line `Gamma1` ↔ line `Gamma1`;
- line `partial Gamma1` ↔ line `Gamma1`;
- anchor `R1` ↔ genuine defect `Box_perp R` / `Box_perp R_nn`.

H. Apply the ITER127 suppressions to upper endpoints/ordered diagonals and record the resulting jet orders.

I. Produce a machine-readable table and validator.

J. No superficial degree may be promoted to a nonzero `B1` contribution without the actual tensor/pole coefficient.

## Frozen classifications

- `PASS_SCOPED_RESIDUAL_DEFECT_SINGULAR_DEGREE_AND_TAYLOR_JET_CENSUS_CLOSED` if A-J close a finite jet budget.
- `PASS_SCOPED_CANONICAL_JET_BOUNDS_CLOSED_INTERACTION_SPECIFIC_ROWS_OPEN` if canonical bounds close but some interaction-dressed row requires graph-specific derivative assignment.
- `FAIL_SCOPED_UNBOUNDED_LOCAL_TAYLOR_JET` if no finite jet ceiling exists at the frozen order.

## Controls

- `ONE_TWO_PROPAGATOR_BASE_POWER_CONTROL`
- `SUPPRESSION_NONZERO_RESIDUE_CONTROL`
- `BULK_SUBDIVERGENCE_DEFECT_DEGREE_CONTROL`
- `OVERLAP_SINGLE_VARIABLE_CONTROL`
- `TARGET_POLE_INFERENCE_CONTROL`

## Claim ceiling

A PASS only bounds local subtraction complexity. It does not compute any curvature pole residue, `B1`, noncancellation result, EDT fit, bridge, new physics or candidate theory.