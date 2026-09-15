# ITER145 terminal result — interaction-dressed M3 routing and collinear triangle-to-bubble reduction

Date: 2026-09-15
Preregistration: `5fe7e068705e2c0af83b0d8af773146fef34a42f`
Implementation: `942aff57768b410b60ffd36eb9c8fb69e94e2813`
Workflow head: `8434cb22308273b92d5df612896db5a5ee9ab42b`
Authoritative run: `34959736173`
Job: `104350206614` (`m3-routing-audit`)
Artifact: `10392508439` (`iter145-m3-collinear-triangle-to-bubble-routing`)
Artifact SHA256: `ba4046c720ca36cf38de4b7c5e4910f284e5424b787af0b6626a55abd653e55e`

## Scientific classification

`PASS_SCOPED_M3_COLLINEAR_THREE_DENOMINATOR_REDUCES_TO_BUBBLES_ROUTING_CLOSED_NUMERATOR_OPEN`

All preregistered phase, momentum-routing, exact denominator-identity, partial-fraction, Q-sign, endpoint-degeneration and rational-interior controls passed.

## Generic interior topology

For the anchored interaction-dressed M3 graph with endpoint separation L, line insertion at `tau L`, and cubic interaction point integrated over spacetime, the representative routing is

`p = -Q-(1-tau)k`,
`r = Q-tau k`.

For generic `0<tau<1`, all three quadratic denominators depend on the same loop momentum k:

`D1 = [Q+(1-tau)k]^2`,
`D2 = k^2`,
`D3 = [Q-tau k]^2`.

Thus ITER145 explicitly rejects the stronger but unnecessary statement that one generic-interior line is fixed external.

## Exact collinear denominator identity

The three shifted denominators satisfy

`tau D1 + (1-tau) D3 - tau(1-tau) D2 = Q^2`.

For nonzero Euclidean `Q^2`, this gives the exact integrand identity

`1/(D1 D2 D3)`
`= tau/Q^2 * 1/(D2 D3)`
`+ (1-tau)/Q^2 * 1/(D1 D2)`
`- tau(1-tau)/Q^2 * 1/(D1 D3)`.

Therefore the visually three-propagator interaction-dressed M graph does not require an independent triangle master: its collinear shifts reduce it algebraically to bubble denominators. This supplies the explicit mechanism behind the relevant ITER125 topology statement.

## Endpoint controls

- at `tau=0`, `D3=Q^2` becomes fixed external and the reduction degenerates consistently;
- at `tau=1`, `D1=Q^2` becomes fixed external and the reduction degenerates consistently.

The same identity survives the global `Q -> -Q` convention relabeling.

## Scope boundary

The gate deliberately contains no S3 tensor numerator. ITER144 separately authorizes the cubic-graviton tensor structure; combining ITER144 with this routing is a prospective numerator-allocation step.

The `1/Q^2` algebraic reduction assumes nonzero external Euclidean Q. The `Q=0` limit is an IR/contact-degenerate case and is not used to infer the separated long-range UV pole.

## Claim ceiling

No master integral, `1/epsilon`, B1, noncancellation result, finite B0, EDT comparison, bridge, new physics or candidate theory is established. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
