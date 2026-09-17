# ITER162 preregistration — open-G endpoint distributional R-operation and pole-tensor quotient

Date: 2026-09-17

Gate: `ITER162_OPEN_G_ENDPOINT_DISTRIBUTIONAL_R_OPERATION_AND_POLE_TENSOR`

Frozen parent: `e88c5299b5ff0977fc6fb7a6eca9311c4df1c640`.

## Frozen motivation

ITER161 has source-faithfully derived endpoint-selected open symmetric metric legs for the G-family graph before final scalar contraction:

- upper endpoint (`k` shrinking): `G1 = A_ab V_upper_ab`, with a symmetric q-side open metric pair;
- lower endpoint (`q` shrinking): `G1 = R_mu,ab W_lower_mu,ab`, with symmetric k-side open metric pairs and derivative label `mu` retained.

The complete endpoint pole tensor remains undefined because the unseparated open vertex contains cancelled-propagator endpoint distributions whose restriction/extension was left unresolved by ITER153, while ITER124 requires endpoint/line renormalization before contact separation.

The present gate asks a sharper question:

> after the full **allowed local distributional ambiguity span** is constructed at tensor level, does any nonzero quotient component of the open-G endpoint pole remain scheme-independent?

This gate is not allowed to set contacts to zero merely to obtain a pole tensor.

## Frozen upstream inputs

1. ITER118 endpoint basis `[R,S,DR,DS,BoxR,D2R,BoxS,D2S]`.
2. ITER122 source-faithful linearized symmetric metric vertices for `R`, `S` and derivative descendants.
3. ITER124 operation order; contact/polynomial separation is downstream of endpoint/line renormalization.
4. ITER140 exact arbitrary-integer-D indexed microscopic G engine.
5. ITER143 affine geometry: q-edge `tau L`, k-edge `(1-tau)L`; lower shrinks q, upper shrinks k.
6. ITER151 exact nonzero cancelled-propagator contact manifest, including the three upper G contacts.
7. ITER153 distributional extension blocker and `absence_is_zero=false` lock.
8. ITER154B scoped proper-subdivergence zero only.
9. ITER160 raw TWO_PROPAGATOR endpoint support residue `-525/(pi^4 L^10) * 1/epsilon` at each endpoint.
10. ITER161 endpoint-selected raw open-leg factorization, workflow run `35250000806`, artifact `10509541616`, open-leg JSON SHA256 `556889d417ee71b89d7478c8513afe72aae171cb02fdfe55d0edc2214e2fc101`.

## General-d and endpoint conventions

`d = 4 - 2 epsilon` remains frozen through pole extraction.

Upper endpoint uses local coordinate `u=1-tau`, shrinking momentum edge k and open q-side metric pair `(a,b)`.

Lower endpoint uses local coordinate `tau`, shrinking q edge and open k-side metric pair `(a,b)` with derivative label `mu` retained.

No lower/upper orientation sign is inferred from equality of the ITER160 scalar support magnitudes.

## Tensor-basis construction rule frozen before outcome

For the **upper** open vertex, `V_upper_ab` is symmetric and homogeneous of total momentum degree four after removing the open q-side curvature source `A_ab` of degree two from the degree-six G numerator. The source contains exactly two tangent vectors overall.

The candidate covariant symmetric-tensor span must be generated mechanically, not selected after coefficients are seen, from the symmetric seeds

- `delta_ab` (momentum degree 0, tangent count 0),
- `q_a q_b`, `q_(a k_b)`, `k_a k_b` (degree 2, tangent count 0),
- `q_(a n_b)`, `k_(a n_b)` (degree 1, tangent count 1),
- `n_a n_b` (degree 0, tangent count 2),

multiplied by scalar monomials in

`Q=q^2`, `K=k^2`, `S=q.k`, `a=n.q`, `b=n.k`

such that total momentum degree is exactly four and total tangent count is exactly two. The scalar monomial generator must use nonnegative integer powers only and must enumerate all solutions to those two degree equations up to degree four. Candidate columns may be removed only by exact rank/dependence tests on prospectively generated rational/integer-D fixtures; no column may be removed because its fitted coefficient happens to vanish.

The **lower** object retains `mu`; it may be analyzed for support and ambiguity, but no scalar ITER118 direction may be assigned unless `mu` is source-faithfully covariantized or cancelled by a frozen combination with other graph structures.

## Tensor-level support classification rule

Support classification must occur on the open tensor **before contraction with the external open curvature source**. The scalar ITER143 labels are consistency checks only.

For the upper endpoint:

- terms in `V_upper_ab / K` whose tensor numerator is exactly divisible by `K` are endpoint-local contact candidates on the shrinking k edge;
- terms not divisible by `K` remain in the genuine one-shrinking-propagator distributional kernel;
- a scalar contraction that later creates or cancels a `K` factor is not allowed to retroactively determine the tensor-level support class.

Exact polynomial divisibility must be tested algebraically or by a source-faithful reconstructed covariant formula, not by numerical near-zero thresholds.

## Distributional extension / ambiguity rule

For every endpoint-local polynomial tensor in the shrinking momentum, Fourier transformation gives a finite sum of ambient delta derivatives. The extension to the affine endpoint must be treated as a local renormalization problem.

This gate does **not** freeze any arbitrary finite renormalization coefficient to zero.

Instead it must construct the full local symmetric-tensor ambiguity span allowed simultaneously by:

1. the exact momentum degree/singular order of the source-derived endpoint tensor;
2. symmetry in `(a,b)`;
3. background rotations/covariance with the available `q`, `n`, and `delta` data;
4. the frozen derivative ceiling of ITER118 at the one-loop order;
5. endpoint locality and the ITER124 ordering.

If dimensional regularization/minimal subtraction uniquely fixes the **pole part** while leaving only finite local ambiguity, that uniqueness must be proved by an explicit distributional Laurent calculation on the unseparated open tensor. It may not be assumed from the scalar ITER160 Beta pole.

## Quotient test frozen before outcome

Let `P_open` denote the source-derived open endpoint pole-tensor space and `A_local` the exact allowed local ambiguity span.

The gate must compute the exact quotient image

`[P_open] in P_open / A_local`.

Three scientifically distinct outcomes are allowed:

### PASS_UNIQUE

`PASS_SCOPED_ITER162_UNIQUE_OPEN_G_ENDPOINT_POLE_TENSOR_DERIVED`

iff the complete unseparated tensor Laurent operation fixes the endpoint `1/epsilon` pole tensor uniquely, including the cancelled-propagator contributions, with no unresolved local pole ambiguity.

### PASS_QUOTIENT

`PASS_SCOPED_ITER162_NONZERO_SCHEME_INDEPENDENT_ENDPOINT_POLE_TENSOR_QUOTIENT`

iff the complete local ambiguity span is nontrivial but the source-derived pole tensor has an exact nonzero quotient component outside it. The quotient representative/basis and exact rank must be persisted. This PASS is only a scheme-independent tensor statement; ITER118 coefficients still require a separately frozen operator-matching manifest.

### BLOCKED_AMBIGUITY

`BLOCKED_SCOPED_ITER162_LOCAL_AMBIGUITY_SPANS_ALL_AVAILABLE_ENDPOINT_POLE_INFORMATION`

iff the entire presently derivable open-G endpoint pole information lies in the allowed local ambiguity span. The result must persist an explicit ambiguity basis and exact rank/kernel proof; a generic statement “scheme dependent” is insufficient.

### BLOCKED_MISSING_OPERATION

`BLOCKED_SCOPED_ITER162_UNSEPARATED_OPEN_TENSOR_LAURENT_OPERATION_NOT_CONSTRUCTED`

iff the current source chain is insufficient to define even the tensor-level Laurent/extension problem required for the quotient test. The single exact earliest missing primitive must be named.

### SCIENTIFIC_FAIL

`SCIENTIFIC_FAIL_ITER162_FROZEN_TENSOR_COVARIANCE_OR_SUPPORT_IDENTITY_FALSE`

iff a prospectively frozen exact structural identity in this preregistration is contradicted by the source-derived tensor object. The failed identity must remain recorded; do not repair it post-outcome inside ITER162.

### INVALID

`INVALID_ITER162`

for implementation error, hidden fit to the known `-525` scalar residue, treating contacts as zero, inverting the 28-scalar map to invent a tensor, post-outcome basis selection, importing ITER123 as an endpoint projector, or performing an ITER118 coefficient/rank solve before a complete pole-tensor manifest exists.

## Held-out consistency checks

At minimum:

- contracting the reconstructed upper covariant tensor with the exact ITER140 open source `A_ab` must reproduce `G1_value` on held-out integer-D configurations not used for coefficient reconstruction;
- the same reconstruction must be deterministic under a changed fixture set;
- tensor-level support classes must recombine exactly to the full open tensor;
- contraction of tensor support classes may be compared with scalar ITER143/151 labels, but mismatch is evidence about premature scalarization and must not be silently forced away;
- the known ITER160 two-propagator scalar support residue may be used only after tensor structure/support are frozen, as a normalization/check of the corresponding nonlocal scalar contraction; it must not determine the tensor basis or ambiguity span;
- no missing local pole is interpreted as zero.

## Equation/rank firewall

This gate may compute tensor-basis ranks and quotient ranks intrinsic to the open-G tensor/ambiguity problem.

It may **not** solve the eight ITER118 endpoint coefficients or claim slot-7 closure until a later preregistered operator-equation manifest consumes a complete pole tensor.

## Independent Critic requirements

The Critic must independently test:

- completeness/non-posthoc nature of the generated covariant tensor basis;
- exact reconstruction on held-out configurations and at multiple integer D;
- no use of `-525` to choose tensor coefficients;
- correct upper/lower shrinking-edge assignment;
- exact divisibility/support logic before external-source contraction;
- complete enumeration of local ambiguity structures under the frozen derivative ceiling;
- quotient rank with an independent linear-algebra route;
- no contact-zero, no ITER123 substitution, no premature ITER118 coefficient solve.

## Claim locks

`B1_total = UNAUTHORIZED`.

`BRIDGE_DERIVED = false`.

`NEW_PHYSICS_FOUND = false`.

Candidate theory remains `UNFORMED / 0%`.
