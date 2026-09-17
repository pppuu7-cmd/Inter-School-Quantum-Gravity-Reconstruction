# ITER160 exploratory note — raw G `b^2*S^2` two-propagator endpoint split

Date: 2026-09-17

Status: **EXPLORATORY / HYPOTHESIS-GENERATING / NOT PREREGISTERED**.

This note records a calculation that was inspected before a confirmatory gate was frozen. It therefore receives no preregistered discovery credit. Its values may be used only as explicit predictions for a later independent confirmation test.

## Frozen upstream object consumed

ITER150 terminal classification:

`PASS_SCOPED_FIRST_MG_NONLOCAL_TWO_PROPAGATOR_MASTER_POLE_NONZERO_CONTACT_SUBTRACTION_OPEN`.

ITER150 result run: `35140549227`; job `104943683326`; artifact `10465465110`; artifact ZIP SHA256 `9e99d4b6854847a83b62ffde5c68969c96e5ac8f7d2c132375e49a737619fcd9`; exact result JSON SHA256 `0748f4f29a684738ae019cd35e27cd51b5f2f37b6c6b956342eb51a6851cdc90`.

The only nonzero simple-pole master among the frozen `Q^0 K^0` two-propagator inputs is

`G_R1_chi2_Gamma2_dR1 : b^2*S^2 -> -1050/(pi^4 L^10)`

multiplying `1/epsilon` in `d=4-2 epsilon`.

This is a raw separated connected-cross TWO_PROPAGATOR master pole. It is not an endpoint counterterm coefficient, not a contact residue, not a renormalized line-defect coefficient and not `B1_total`.

## Actual ITER150 affine integral

For the G-family `b^2*S^2` master, ITER150 freezes:

- route `r_x=tau`, `r_y=1-tau`;
- derivative orders `(o_x,o_y)=(2,4)`;
- source weight `(1-tau)`;
- `d=4-2 epsilon`;
- Beta parameters `a=1-d`, `b=-d`.

Therefore the affine factor is

`B(1-d,-d) = Integral_0^1 tau^(-d) (1-tau)^(-d-1) d tau`

by meromorphic continuation, i.e. at `d=4-2 epsilon`,

`Integral_0^1 tau^(-4+2 epsilon) (1-tau)^(-5+2 epsilon) d tau`.

ITER150 independently establishes total Beta residue `35`, so the graph prefactor multiplying the Beta factor is

`[-1050/(pi^4 L^10)] / 35 = -30/(pi^4 L^10)`.

## Exploratory lower-endpoint calculation

Near `tau=0`, treat `(1-tau)^(-5+2 epsilon)` as the smooth factor and minimally subtract its Taylor jet through degree 3, because the singular factor is `tau^(-4+2 epsilon)`.

At `epsilon=0`,

`(1-tau)^(-5) = Sum_{k>=0} binom(k+4,4) tau^k`.

The unique logarithmic local term is `k=3`, whose coefficient is

`binom(7,4)=35`.

Since `Integral_0 tau^(-1+2 epsilon) d tau` has residue `1/2`, the exploratory lower-endpoint Beta residue is

`r_lower = 35/2`.

## Exploratory upper-endpoint calculation

Set `u=1-tau`. Near `u=0`, the integrand is

`u^(-5+2 epsilon) (1-u)^(-4+2 epsilon)`.

The required smooth Taylor jet is through degree 4. At `epsilon=0`,

`(1-u)^(-4) = Sum_{k>=0} binom(k+3,3) u^k`.

The logarithmic term is `k=4`, with coefficient

`binom(7,3)=35`.

Hence

`r_upper = 35/2`.

The exploratory check is

`r_lower + r_upper = 35`,

exactly equal to the frozen ITER150 total Beta residue.

Multiplying by the frozen graph prefactor gives the exploratory raw support split

- lower endpoint: `-525/(pi^4 L^10) * 1/epsilon`;
- upper endpoint: `-525/(pi^4 L^10) * 1/epsilon`.

## Interpretation firewall

These numbers are only a proposed decomposition of the already-frozen raw TWO_PROPAGATOR master pole under minimal local endpoint Taylor subtraction.

They are **not**:

- coefficients of the ITER118 basis `[R,S,DR,DS,BoxR,D2R,BoxS,D2S]`;
- endpoint counterterms;
- a replacement for the unresolved ITER153 contact distributions;
- authorization to bypass the ITER124 subtraction order;
- evidence that either endpoint contribution survives full renormalization/mixing;
- `B1_total`.

Because this calculation was seen before a confirmatory preregistration, a separate gate must freeze these values as predictions and test them by an independent distributional derivation before they are promoted even to a confirmed raw-support statement.

## Claim locks

`B1_total = UNAUTHORIZED`; `BRIDGE_DERIVED=false`; `NEW_PHYSICS_FOUND=false`; candidate theory remains `UNFORMED / 0%`.
