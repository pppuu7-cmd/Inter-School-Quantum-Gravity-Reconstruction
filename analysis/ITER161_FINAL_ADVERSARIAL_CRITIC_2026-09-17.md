# ITER161 final adversarial Critic — after endpoint-selected open-leg repair

Date: 2026-09-17

Preregistration: `e004e8ff0d4977676b3e70c34a78c438965dc62a`.

Initial structural producer: `e7be19d781e1121646913264cbe7f2da007f0ae0`.

Preliminary Critic: `c1d5fbbfe7c2e7ea65908901bddbb1c33148d46b` — **superseded in part**.

Self-correction: `c19f407f48de41978c73c04df634a8deddf86785`.

Endpoint-selected open-leg implementation: `3b47cbeaa5ec3ed8d3023b8774a8f8799aac02db`.

## 1. Does a raw tensor lift exist before the final scalar contraction?

**Yes, scoped and source-faithfully.**

The frozen G-family geometry selects the open leg without using the known pole coefficient:

- lower endpoint `tau -> 0`: q edge shrinks, retain the k-side metric leg;
- upper endpoint `tau -> 1`: k edge shrinks, retain the q-side metric leg.

This invalidates the preliminary Critic's stronger statement that choosing which propagated matrix to open is arbitrary.

The exact endpoint-selected implementation evaluates the ITER140 G functional on a symmetric matrix basis and proves:

### Upper endpoint

There is a unique symmetric matrix `V_upper_ab(q,k,n;D)` for the source functional such that

`G1 = sum_ab A_ab V_upper_ab`,

where `A_ab=pmap(R1_source)_ab` is the nonshrinking q-side propagated source.

### Lower endpoint

There are symmetric matrices `W_lower_mu,ab` such that

`G1 = sum_mu,ab R_mu,ab W_lower_mu,ab`,

where `R_mu,ab=pmap(dR1_source_mu)_ab` is the nonshrinking k-side propagated source. The residual derivative label `mu` is retained rather than silently forced into the scalar ITER118 basis.

Independent exact-Fraction test configurations at `D=4,5,6` give exact reconstruction of the original `G1_value` for both endpoint factorizations. The factorization calculation does not consume the ITER160 value `-525/(pi^4 L^10)` and therefore does not fit a tensor structure to the desired pole.

**Critic check A: PASS.**

## 2. Is the open-leg factorization already a tensor pole residue?

**No.**

`V_upper_ab(q,k,n;D)` and `W_lower_mu,ab(q,k,n;D)` are raw numerator/open-leg objects before the shrinking-edge distribution is renormalized. To obtain an endpoint pole tensor one still has to apply the endpoint extension/R-operation to the shrinking momentum/affine singularity.

The upper object schematically enters

`integral dk exp[i(1-tau)L n.k] V_upper_ab(q,k,n;D) / K`.

Because the full ITER140 numerator is unseparated, this contains both genuine `1/K` pieces and terms where `K` cancels.

**Critic check B: PASS.**

## 3. Can the cancelled-propagator terms be discarded before forming the pole tensor?

**No.**

ITER151 freezes three nonzero G-family upper-endpoint K-cancelled contact survivors:

1. `K*S^2`, coefficient `-1/(2*d-4)`;
2. `a^2*K*S`, coefficient `(d-1)/(2*d-4)`;
3. `a*b*K*S`, coefficient `1/(d-2)`.

ITER153 proves that, after cancellation, these are point-supported ambient delta derivatives whose ordinary canonical pullback to the geodesic is not authorized. Their `1/epsilon^2` and `1/epsilon` values remain null/unknown, with `absence_is_zero=false`.

ITER124 independently requires endpoint and line renormalization before the final contact/polynomial split.

Therefore a tensor pole computed only from the ITER150/160 TWO_PROPAGATOR sector would violate the frozen operation order.

**Critic check C: PASS.**

## 4. Does ITER154B remove this problem by proving no subdivergences?

**No.**

ITER154B closes only proper ordinary bulk/local-composite subdivergence insertions for the scoped primitive bubble topology. It does not define the affine-boundary distributional extension, endpoint composite-operator mixing, or the cancelled-propagator contact contribution.

The present missing operation is therefore not contradicted by ITER154B.

**Critic check D: PASS.**

## 5. Can the upper raw `-525` support residue be used merely as an overall normalization after deriving `V_upper`?

**Not yet.**

Although the open tensor structure is now derived independently of `-525`, the scalar `-525/(pi^4 L^10)` is the endpoint support residue of the separated TWO_PROPAGATOR master. The complete unseparated open-leg pole tensor can differ by the unresolved local contact/extension contribution before the ITER124 contact split.

Using `-525` to normalize the complete ITER118 operator tensor would therefore still assume the missing renormalization step.

**Critic check E: PASS.**

## 6. Exact minimal missing primitive

After the open-leg repair, the exact missing primitive is narrower than the preliminary Critic stated:

> a source-faithful **distributional endpoint R-operation/extension acting on the source-derived open-leg unseparated `G_R1_chi2_Gamma2_dR1` endpoint vertex before Q/K contact separation**, preserving the selected free symmetric metric leg and endpoint orientation while assigning the complete local pole tensor, including the cancelled-propagator endpoint distributions.

This one operation is sufficient to move from the new structural tensor lift to an object that can actually be compared with the ITER122 linearized vertices of `[R,S,DR,DS,BoxR,D2R,BoxS,D2S]`.

## 7. Terminal-class adjudication

The ITER161 PASS criterion requires not merely a raw open-leg numerator but at least one **tensor-resolved raw pole object and matching ITER118 tree-kernel equation**.

The open-leg numerator has now been derived, but the complete tensor pole is not source-faithfully defined because the distributional endpoint R-operation above is missing.

Therefore the correct terminal class is:

`BLOCKED_SCOPED_ITER161_G_ENDPOINT_TENSOR_LIFT_EXACT_MISSING_PRIMITIVE`.

This BLOCKED is materially narrower than ITER157/158-era blockers: the free symmetric metric leg is no longer missing. The remaining gap is specifically the distributional endpoint pole operation on that open tensor object.

## Final Critic verdict

**`PASS_CRITIC_ITER161_OPEN_LEG_DERIVED_POLE_EXTENSION_BLOCKER_SOUND`**

## Claim locks

- ITER160 raw endpoint support PASS remains valid and unchanged.
- No ITER118 coefficient has been derived or set to zero.
- No rank/nullspace solve is authorized.
- No contact residue is assumed zero.
- No ITER123 line projector is used.
- `B1_total=UNAUTHORIZED`.
- `BRIDGE_DERIVED=false`.
- `NEW_PHYSICS_FOUND=false`.
- Candidate theory remains `UNFORMED / 0%`.
