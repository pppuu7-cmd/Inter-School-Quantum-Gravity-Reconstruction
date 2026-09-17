# ITER161 self-correction — endpoint geometry fixes the open-leg choice

Date: 2026-09-17

This note preserves and corrects an overstrong statement in the preliminary document `analysis/ITER161_INDEPENDENT_CRITIC_2026-09-17.md` (commit `c1d5fbbfe7c2e7ea65908901bddbb1c33148d46b`). That document was written before ITER161 was terminalized and must **not** be treated as the final Critic verdict.

## What remains correct

The post-`g2_real` pretrace object

`U[alpha,r,m,n]`

is not itself a free symmetric metric-pair endpoint vertex, and the final scalar `G1_value` cannot be inverted uniquely to recover such a tensor. The explicit scalarization-null witness remains valid.

The ITER124 ordering and ITER153 contact-extension blocker also remain fully valid: the ITER160 `-525/(pi^4 L^10)` raw TWO_PROPAGATOR endpoint piece cannot by itself be re-labelled as an ITER118 counterterm coefficient.

## What was too strong

The preliminary Critic said that opening either propagated matrix `A` or `R_mu` would be an arbitrary amputation/R-operation choice.

That is not correct once the frozen affine geometry is used.

For the G family, ITER143 freezes

- q-edge separation `tau L`;
- k-edge separation `(1-tau)L`.

Therefore:

- at the **lower endpoint** `tau -> 0`, the q edge is the shrinking/local edge and the k-side graviton leg is the nonshrinking leg to retain;
- at the **upper endpoint** `tau -> 1`, the k edge is the shrinking/local edge and the q-side graviton leg is the nonshrinking leg to retain.

Thus endpoint geometry prospectively determines which leg should remain open in an endpoint OPE/amputation construction. This is not desired-sign fitting and does not use the known pole value.

## Exact upper-endpoint factorization

At the upper endpoint, keep the q-side propagated matrix `A` arbitrary and contract the shrinking k-side `dR1` source through the `Gamma2` bilinear. Because the G numerator is linear in `A`, there exists a unique symmetric matrix `V_upper_ab(q,k,n;D)` such that

`G1_value = sum_ab A_ab V_upper_ab`

for every symmetric `A`.

`V_upper` can be constructed source-faithfully by evaluating the exact ITER140 G functional on a symmetric matrix basis. The off-diagonal coefficient is half the response to `E_ab+E_ba`; diagonal coefficients are direct responses to `E_aa`.

A deterministic exact-Fraction implementation was tested on independent configurations at `D=4,5,6`; in all three cases the reconstructed scalar equals `G1_value` exactly and `V_upper` is symmetric.

This proves that a source-faithful **raw open symmetric metric leg does exist before the final scalar contraction**.

## Lower-endpoint factorization

At the lower endpoint, keep the k-side propagated `R_mu` matrix open. The corresponding source-faithful factorization is naturally vector-valued in the derivative label `mu`:

`G1_value = sum_mu,ab R_mu,ab W_lower_mu,ab`.

This is again a legitimate raw tensor lift, but a single G graph does not by itself prove that the remaining `mu` dependence is already one of the scalar ITER118 endpoint directions; covariance may require combination with the other M/G endpoint structures.

## What still blocks an ITER118 pole equation

The existence of an open tensor leg does **not** resolve the pole/mixing problem.

For the upper endpoint, the unseparated open vertex is schematically

`Integral dk exp[i(1-tau)L n.k] V_upper_ab(q,k,n;D) / K`.

The exact ITER140/151 numerator contains both genuine `1/K` two-propagator pieces and terms in which `K` cancels. The latter are ambient delta-derivative contact distributions supported exactly at the affine endpoint. ITER153 proves that their restriction to the geodesic requires an additional distributional extension / graph-level renormalization datum, and ITER124 forbids separating them before endpoint/line renormalization is complete.

Hence ITER161 has produced a sharper partial tensor object, but **no source-faithful tensor pole residue can yet be formed from the complete unseparated upper endpoint vertex**.

## Corrected minimal missing primitive candidate

The minimal primitive is therefore narrower than the preliminary Critic stated:

> a source-faithful **distributional endpoint R-operation/extension acting on the already source-derived open-leg unseparated G endpoint vertex**, before Q/K contact separation, that assigns the local pole tensor (including the K-cancelled endpoint contacts) while preserving the free symmetric metric leg and endpoint orientation.

Only after that operation exists can the resulting pole tensor be compared to ITER122's `A_ab(R)`, `B_ab(S)` and their derivative descendants.

No ITER118 coefficient is set to zero or nonzero by this correction.

## Status

This is an in-gate correction before terminal ITER161 classification. The earlier preliminary Critic verdict is superseded; its valid subchecks remain evidence, but its claim that the open-leg choice is arbitrary is rejected.

Claim locks remain unchanged: `B1_total=UNAUTHORIZED`, `BRIDGE_DERIVED=false`, `NEW_PHYSICS_FOUND=false`, candidate theory `UNFORMED / 0%`.
