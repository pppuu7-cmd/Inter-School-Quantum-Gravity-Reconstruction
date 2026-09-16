# ITER148 adversarial manual audit — canonical-bubble Jacobian/prefactor powers

Date: 2026-09-16
Gate: `ITER148_FIXED_GEODESIC_CURVATURE_M3_FULL_INVARIANT_BUBBLE_REDUCED_NUMERATOR`
Scope: independent critic audit only; **does not terminalize ITER148**.

## Reason for audit

The frozen ITER148 preregistration requires exact verification of the three canonical bubble loop maps **including Jacobian/prefactor powers**. The parallel aggregator checks the denominator substitutions for A/B/C but currently sets `L_canonical_jacobian_prefactor_powers=True` as a literal constant. Therefore green CI alone cannot be treated as evidence that prereg predicate L was executed.

This note supplies an independent equation-level audit of that omitted mathematical predicate without changing the frozen object, basis, tau grid, source, routing, classifier, thresholds, or claim ceiling.

## Frozen partial fraction coefficients

With

`D1=[q+(1-tau)k]^2`, `D2=k^2`, `D3=[q-tau k]^2`,

ITER148 freezes

`N/(D1 D2 D3)`
`= (tau/Q) N/(D2 D3)`
`+ ((1-tau)/Q) N/(D1 D2)`
`- (tau(1-tau)/Q) N/(D1 D3)`.

The following derivations are valid for nondegenerate `0<tau<1`; endpoint limits remain governed by the separately frozen ITER145 endpoint treatment.

## Bubble A

Frozen map: `l=-tau k`.

Hence

- `d^d k = tau^{-d} d^d l`;
- `D2=k^2=L/tau^2`;
- `D3=(q+l)^2`;
- partial-fraction coefficient is `tau/Q`.

Therefore

`(tau/Q) * d^d k /(D2 D3)`
`= (tau/Q) * tau^{-d} * tau^2 * d^d l/[l^2(q+l)^2]`
`= tau^(3-d)/Q * d^d l/[l^2(q+l)^2]`.

So the frozen A prefactor is exact.

## Bubble B

Frozen map: `l=(1-tau)k`.

Hence

- `d^d k=(1-tau)^{-d} d^d l`;
- `D2=L/(1-tau)^2`;
- `D1=(q+l)^2`;
- partial-fraction coefficient is `(1-tau)/Q`.

Therefore

`((1-tau)/Q) * d^d k /(D1 D2)`
`= (1-tau)^(3-d)/Q * d^d l/[l^2(q+l)^2]`.

So the frozen B prefactor is exact.

## Bubble C

Frozen map: `l=(1-tau)(tau k-q)`.

Solving for the old loop variable,

`k = q/tau + l/[tau(1-tau)]`,

so

`d^d k = [tau(1-tau)]^{-d} d^d l`.

The frozen denominator substitutions give

- `D1=(q+l)^2/tau^2`;
- `D3=l^2/(1-tau)^2`;
- partial-fraction coefficient is `-tau(1-tau)/Q`.

Thus

`-[tau(1-tau)]/Q * d^d k /(D1 D3)`
`= -[tau(1-tau)]/Q * [tau(1-tau)]^{-d} * tau^2(1-tau)^2 * d^d l/[l^2(q+l)^2]`
`= -[tau(1-tau)]^(3-d)/Q * d^d l/[l^2(q+l)^2]`.

So the frozen C prefactor, including its sign, is exact.

## Critic verdict

`MANUAL_PREDICATE_L_PASS_SCOPED`.

The mathematical Jacobian/prefactor predicate required by the ITER148 preregistration is independently verified. The implementation defect remains real: the aggregator does not compute this predicate and therefore machine `checks.L=true` is not itself evidence. This manual audit may be cited in terminal adjudication if and only if all other frozen ITER148 predicates are supported by immutable run outputs.

No bridge, new-physics, B1, EDT, general-d/O(epsilon), master-pole, subtraction, or candidate-theory claim is authorized by this audit. Candidate theory remains `UNFORMED / 0%`; bridge credit remains 0.
