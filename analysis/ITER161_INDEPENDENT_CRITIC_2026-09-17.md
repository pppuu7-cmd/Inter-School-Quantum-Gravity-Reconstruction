# ITER161 independent adversarial Critic

Date: 2026-09-17

Gate under review: `ITER161_G_B2S2_ENDPOINT_RAW_TENSOR_LIFT_TO_ITER118_OPERATOR_EQUATIONS`.

Preregistration commit: `e004e8ff0d4977676b3e70c34a78c438965dc62a`.

Producer/structural diagnostic commit: `e7be19d781e1121646913264cbe7f2da007f0ae0`.

## Independent question

Can the confirmed ITER160 raw endpoint support residue for

`G_R1_chi2_Gamma2_dR1 : b^2*S^2`

be promoted, using the currently frozen source chain, to a tensor-resolved equation for an ITER118 endpoint counterterm coefficient?

The Critic intentionally does not use the desired coefficient sign/value and does not solve any rank problem.

## Check 1 — exact index type before the final G scalarization

In the frozen ITER140 source, `G1_value` constructs

- `A = pmap(r1_tensor(-q),D)`, a propagated symmetric source matrix;
- for each derivative index `mu`, `R_mu = pmap(dr1_real(mu,-k),D)`, another propagated symmetric source matrix;
- `g2_real(A,q,R_mu,k,r,m,n,D)`, whose `g2r_cross` implementation sums the internal index `t` in

`A[r,t] * (k[m] R[t,n] + k[n] R[t,m] - k[t] R[m,n]) / 2`

plus the crossed ordering.

The G observable then sets `r=mu`, sums `mu`, and contracts `m,n` with `n^m n^n`.

Therefore the maximal directly retained post-`g2_real` object is naturally of connection/derivative type

`U[alpha,r,m,n]`,

not a local one-graviton symmetric metric vertex `V_ab`.

The producer's exact deterministic reconstruction checks at `D=4,5,6` verify that

`G1 = sum_{alpha,m,n} n_m n_n U[alpha,alpha,m,n]`.

This is useful new structural information, but it does not by itself identify any of the ITER118 directions.

**Critic check A: PASS.**

## Check 2 — scalar inversion is nonunique

For `n=e_0`, any perturbation of `U` supported on a component with `m != 0` or `n != 0` lies in the kernel of the final tangent contraction. An explicit witness is

`Delta[alpha=0,r=0,m=1,n=1]=1`,

whose contribution to the G scalar is exactly zero.

Thus the scalar `b^2*S^2` residue cannot be inverted to a unique pretrace tensor. The ITER161 preregistration correctly forbids treating the 28-scalar reconstruction as an invertible tensor map.

**Critic check B: PASS.**

## Check 3 — ITER118/ITER122 require a different object type

ITER118's endpoint basis is

`[R,S,DR,DS,BoxR,D2R,BoxS,D2S]`, with `S=R_nn`.

ITER122's source-faithful linearized curvature vertices are symmetric metric-source tensors, beginning with

`A_ab(R)=Q delta_ab-q_a q_b`

and

`B_ab(S)=1/2[Q n_a n_b+Q u delta_ab-(q.n)(q_a n_b+q_b n_a)]`.

Their derivative descendants multiply these same one-graviton vertices by the appropriate momentum factors. Hence an endpoint mixing equation requires a local one-graviton object with a free symmetric metric pair and fixed endpoint orientation/normalization.

The post-`g2_real` `U[alpha,r,m,n]` has no source-authorized identification of any two of its connection/derivative slots with that free metric pair.

Opening one of the two propagated matrices `A` or `R_mu` by hand would be an additional amputation/R-operation choice, not an algebraic consequence of the existing fully contracted graph.

**Critic check C: PASS.**

## Check 4 — the known `-525` endpoint number is not an operator-mixing residue

ITER160 only splits the already-separated ITER150 **TWO_PROPAGATOR** raw master. The confirmed support number at each endpoint is

`-525/(pi^4 L^10) * 1/epsilon`.

But ITER151 proves that the same G family also has three nonzero **upper-endpoint K-cancelled contact survivors**:

1. `K*S^2`, coefficient `-1/(2*d-4)`;
2. `a^2*K*S`, coefficient `(d-1)/(2*d-4)`;
3. `a*b*K*S`, coefficient `1/(d-2)`.

Therefore the two-propagator upper endpoint is not the complete raw G endpoint sector.

More importantly, ITER124 freezes the operation order: endpoint/counterterm and line renormalization occur **before** the final contact/polynomial separation.

ITER153 independently sharpened the exact missing primitive to a graph-level R-operation on the **unseparated** first-M/G amplitude and proved that the seven raw contact distributions do not have a canonically authorized pullback to the line under the existing source chain. Their pole values remain null/unknown, not zero.

Consequently the ITER160 number is a valid raw-support diagnostic but cannot be used as the normalization of an ITER118 endpoint coefficient before the missing graph-level R-operation is supplied.

**Critic check D: PASS.**

## Check 5 — could the lower endpoint escape the contact problem?

The absence of a listed G lower-endpoint contact survivor does not create an operator equation. Even there, the fully contracted two-propagator boundary residue still lacks the graph-level amputation/map that produces the required local one-graviton symmetric metric vertex. In addition, ITER124 defines renormalization for the complete observable rather than a coefficient-by-coefficient premature sector split.

Therefore it would be invalid to accept a lower-endpoint ITER118 coefficient merely because the explicit G contact survivors listed by ITER151 sit at the upper endpoint.

**Critic check E: PASS.**

## Exact blocker adjudication

The producer's proposed minimal primitive is accepted, with the following precise wording:

> a source-faithful **graph-level endpoint R-operation/amputation map on the unseparated `G_R1_chi2_Gamma2_dR1` amplitude before Q/K denominator cancellation**, which retains/produces the local one-graviton symmetric metric leg, combines the endpoint-local contact sectors under an authorized distributional extension, and outputs a tensor object directly comparable to the ITER118/ITER122 endpoint vertices.

This is one operation/map, not a request for an open-ended source list.

It is also consistent with the earlier ITER153 blocker but sharper for the present G tensor-lift scope.

## Critic verdict

**`PASS_CRITIC_ITER161_EXACT_TENSOR_LIFT_BLOCKER_SOUND`**

The correct scientific terminal class is:

`BLOCKED_SCOPED_ITER161_G_ENDPOINT_TENSOR_LIFT_EXACT_MISSING_PRIMITIVE`.

This is not a physical FAIL. It does not invalidate ITER160's raw support split and it sets no ITER118 coefficient to zero.

## Forbidden overclaims checked

- no scalar invariant was assigned a unique tensor preimage;
- no `-525` raw endpoint residue was re-labelled as a counterterm coefficient;
- no ITER153 contact pole was imported or set to zero;
- no ITER123 genuine-line projector was used;
- no rank/nullspace solve was attempted before an equation manifest exists;
- no `B1_total`, bridge, new-physics or candidate-theory claim follows.
