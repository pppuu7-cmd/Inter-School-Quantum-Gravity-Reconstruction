# ITER163 preregistration — complete two-tangent covariant closure for the open-G upper tensor

Date: 2026-09-17

Gate: `ITER163_OPEN_G_COMPLETE_TWO_TANGENT_COVARIANT_CLOSURE`.

Frozen parent terminal result: ITER162 `SCIENTIFIC_FAIL_ITER162_FROZEN_TENSOR_COVARIANCE_OR_SUPPORT_IDENTITY_FALSE`, result commit `1ad62d919771e6f1984443d805c1442c2fda9563`.

Recovery parent: `d00263150bded8239690a1b7af2310d1bbbae269`.

## Motivation fixed before repaired source coefficients

ITER162 directly falsified its 36-column upper tensor generator. In the exact submanifold

`n=e0`, `n.q=n.k=0`, transverse open indices `i,j != 0`,

all 36 frozen covariants vanish while the microscopic source-derived `V_upper_ij` is nonzero. Independent Critic confirmed the contradiction in changed `D=4,5,6` cases.

The identified structural omission is that the two microscopic tangent vectors may saturate internally to `n^2`, leaving no explicit `a=n.q`, `b=n.k`, or free `n_a` factor. ITER162 did not allow scalar `n^2` in its tangent-count generator.

ITER163 prospectively repairs only that exact failed assumption. It does not alter ITER161 source machinery and does not import scalar ITER160 residues.

## Frozen source and geometry

Consume unchanged:

- ITER140 exact arbitrary-integer-D indexed microscopic G engine;
- ITER143 geometry and physical convention `n^2=1`;
- ITER161 exact upper open tensor `V_upper_ab` defined by `G1=sum_ab A_ab V_upper_ab`;
- upper endpoint has shrinking k edge and open q-side symmetric metric pair.

No scalar 28-invariant inverse is authorized.

## Complete two-tangent generator frozen prospectively

Use the same seven symmetric rank-two seeds:

- `delta_ab`, momentum degree 0, explicit tangent count 0;
- `q_a q_b`, `q_(a k_b)`, `k_a k_b`, momentum degree 2, explicit tangent count 0;
- `q_(a n_b)`, `k_(a n_b)`, momentum degree 1, explicit tangent count 1;
- `n_a n_b`, momentum degree 0, explicit tangent count 2.

Use scalar variables

- `Q=q^2`: momentum degree 2, tangent count 0;
- `K=k^2`: momentum degree 2, tangent count 0;
- `S=q.k`: momentum degree 2, tangent count 0;
- `a=n.q`: momentum degree 1, tangent count 1;
- `b=n.k`: momentum degree 1, tangent count 1;
- **`N=n^2`: momentum degree 0, tangent count 2**.

Generate mechanically all nonnegative integer exponent monomials such that

- seed momentum degree + scalar momentum degree = exactly 4;
- seed tangent count + scalar tangent count = exactly 2.

Because total tangent count is two, `N` can occur at most to first power.

Expected raw candidate count before exact dependence tests:

- old explicit-tangent sector: 36 columns;
- `N`-saturated tangent-neutral sector: 15 columns;
- total: **51 columns**.

This count is a preregistered structural expectation. A mechanical generator mismatch is implementation INVALID until repaired; it is not a source outcome.

`N` is retained symbolically for enumeration/provenance and then evaluated at the physical unit-tangent condition `N=1` in fixtures. Candidate columns may be removed only by exact rank/dependence proof on prospectively generated rational fixtures; no column may be removed because a source coefficient is zero.

## Why this repair is intended to be complete

The microscopic source contains exactly two tangent vectors overall. Under O(D)-covariant contractions, their possible disposition relative to the open symmetric rank-two tensor is exhausted by:

1. both tangent vectors in scalar contractions: `a^2`, `a b`, `b^2`;
2. one scalar tangent contraction and one free tangent index: `a q_(a n_b)`, `b q_(a n_b)`, `a k_(a n_b)`, `b k_(a n_b)` with allowed momentum monomials;
3. both tangent vectors as free indices: `n_a n_b`;
4. both tangent vectors internally saturated: `N=n^2` multiplying tangent-neutral rank-two seeds.

No Levi-Civita/pseudotensor structure is introduced: the microscopic source chain is built from the background metric/delta and vectors and the gate preserves background O(D) covariance.

## Researcher reconstruction

After the 51-column generator is frozen:

1. build an exact design matrix from deterministic rational/integer q,k fixtures with exact unit tangent;
2. compute exact rank and exact dependencies before consuming source values;
3. select a full-rank row system prospectively by matrix pivots;
4. solve exact source coefficients at integer dimensions;
5. reconstruct general-d coefficient dependence using only a denominator/trace-degree bound justified by the microscopic pmap structure;
6. validate held-out dimensions not used for interpolation;
7. validate changed q,k fixtures not used in the coefficient solve;
8. validate rotated rational unit tangents.

If the exact candidate rank is less than 51, persist the exact kernel/dependency certificate and reconstruct only in a prospectively selected independent quotient basis derived from that kernel, not from source coefficient zeros.

## Independent Critic reconstruction

The Critic must independently:

- regenerate all 51 raw columns from the degree/tangent equations;
- use changed tangent orientation, q/k fixtures, row ordering, and linear algebra path;
- compute candidate rank independently;
- solve source coefficients independently modulo any proved structural dependencies;
- test rotated unit-tangent held-outs;
- confirm the source tensor lies in the repaired span exactly.

A shared coefficient JSON is not sufficient evidence.

## Direct regression witness

The exact ITER162 counterexample submanifold is a mandatory held-out regression:

`n=e0`, `n.q=n.k=0`, transverse `i,j != 0`.

The repaired span must be able to reproduce the nonzero source `V_ij` there through the `N`-saturated sector. Failure is a scientific failure of the repaired completeness hypothesis.

## Exact full tensor K-divisibility

Only after source containment is established, recompute tensor-level divisibility of the **complete repaired span** modulo the principal ideal `<K=k^2>`.

The gate must persist:

- full repaired span rank;
- quotient-map rank modulo K;
- K-divisible kernel dimension and exact basis;
- whether the K-divisible kernel equals the explicit-K column span or contains hidden combinations;
- the source coefficient projection into K-divisible and non-K quotient sectors.

No scalar external-source contraction may change tensor support classification post hoc.

## Outcomes

### PASS

`PASS_SCOPED_ITER163_COMPLETE_TWO_TANGENT_COVARIANT_CLOSURE_AND_SOURCE_RECONSTRUCTION`

iff:

- the 51-column raw generator is mechanically correct;
- exact rank/dependencies are certified prospectively;
- source-derived `V_upper_ab` lies exactly in the repaired span;
- independent Researcher/Critic reconstructions agree modulo proved dependencies;
- changed-q/k, held-out-D and rotated-unit-tangent tests pass;
- the direct ITER162 counterexample is reproduced;
- full repaired-span K-divisibility/support algebra is certified exactly.

This PASS repairs only the structural tensor stage. It does not compute the distributional Laurent pole, `A_local`, quotient, ITER118 coefficients, B1_total, bridge, or candidate theory.

### SCIENTIFIC_FAIL

`SCIENTIFIC_FAIL_ITER163_REPAIRED_TWO_TANGENT_COVARIANT_CLOSURE_FALSE`

iff the prospectively frozen repaired closure is contradicted by the source-derived tensor after implementation validity checks.

### INVALID

`INVALID_ITER163`

for generator/count defect, non-unit tangent fixtures, post-outcome basis selection, floating rank thresholds, use of ITER160 `-525` to choose tensor coefficients, scalar-map inversion, contact-zero shortcut, or premature ITER118 solve.

## Claim locks

`ITER160_minus525_consumed = false` during generator/reconstruction/support construction.

`contacts_set_zero = false`.

`ITER118_MATCHING_AUTHORIZED = false`.

`B1_total = UNAUTHORIZED`.

`BRIDGE_DERIVED = false`.

`NEW_PHYSICS_FOUND = false`.

Candidate theory remains `UNFORMED / 0%`.

## Downstream if PASS

Only after terminal ITER163 PASS may a new prospective gate return to the ITER162 scientific question that was not reached:

`unseparated source-complete open tensor -> distributional Laurent/R-operation -> complete A_local -> exact P_open/A_local quotient`.
