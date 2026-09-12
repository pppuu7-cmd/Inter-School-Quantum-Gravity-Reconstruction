# ITER006 — RC-009 endpoint absolute-convergence audit

Date: 2026-09-12

## Purpose

Follow up the independent dense-grid reliability failure of RC-009 by separating the bounded oscillatory branch factor from the algebraic magnitude of the reduced isotemporal scan-center weight. The frozen diagnostic fits

`w_env(t) ~ t^p`

near the lower endpoint on logarithmic sequences. For a one-dimensional edge, simple absolute local integrability requires `p > -1`; for the simultaneous two-dimensional radial collision, the conservative radial criterion is `p > -2`.

This is an absolute-envelope diagnostic only. It does not test conditional oscillatory convergence, cancellations after a source-defined summation, a different physical measure, or full spin-foam cylindrical consistency.

## GitHub Actions authority

Run: `34669113055` — `ISQGR RC-009 Endpoint Power Audit`

Nine independent lanes plus aggregate completed successfully.

## Results

- coarse endpoint: `p = -141.7738501`, `R^2 = 0.9993982`, threshold `-1` — **FAIL absolute power criterion**;
- fine diagonal simultaneous collision: `p = -1200.151655`, `R^2 = 0.9999180`, threshold `-2` — **FAIL**;
- fine edge, anchor `0.05`: `p = -343.9798439`, `R^2 = 0.9989011` — **FAIL**;
- fine edge, anchor `0.10`: `p = -339.6860347`, `R^2 = 0.9991852` — **FAIL**;
- fine edge, anchor `0.20`: `p = -336.5591334`, `R^2 = 0.9993723` — **FAIL**;
- fine edge, anchor `0.50`: `p = -333.6898057`, `R^2 = 0.9995272` — **FAIL**;
- fine edge, anchor `1.00`: `p = -332.1878111`, `R^2 = 0.9996013` — **FAIL**;
- fine edge, anchor `2.00`: `p = -331.0960200`, `R^2 = 0.9996518` — **FAIL**;
- fine edge, anchor `4.00`: `p = -330.3256764`, `R^2 = 0.9996857` — **FAIL**.

All nine lanes are therefore incompatible with simple absolute endpoint integrability in this reduced coordinate diagnostic.

## Interpretation

The earlier deterministic midpoint-grid audit showed almost all normalized weight collapsing onto the lower boundary and severe resolution dependence. The endpoint-power audit now shows that this is not plausibly repaired by merely increasing grid density: after removing the bounded oscillatory branch factor, the algebraic envelope itself rises as an extremely negative endpoint power.

Therefore the current RC-009 reduced isotemporal amplitude cannot be used as an amplitude/refinement bridge authority under an ordinary positive absolute measure.

This does **not** prove the underlying Lorentzian EPRL amplitude divergent and does not invalidate the direct Delta4 tensor contraction reproduction. It localizes the missing ingredient: any rescue must come from a source-grounded conditional/oscillatory prescription, exact cancellation, or a different physical measure/domain—not from ordinary positive quadrature refinement.

## Classification

`RC009_REDUCED_ISOTEMPORAL_POSITIVE_ABSOLUTE_MEASURE_BRIDGE_BLOCKED_BY_ENDPOINT_POWER_DIVERGENCE__CONDITIONAL_OSCILLATORY_OR_SOURCE_DEFINED_MEASURE_ROUTE_REMAINS_OPEN`.

Claim locks remain unchanged: no `BRIDGE_DERIVED`, no `NEW_PHYSICS_FOUND`, no candidate-theory construction.
