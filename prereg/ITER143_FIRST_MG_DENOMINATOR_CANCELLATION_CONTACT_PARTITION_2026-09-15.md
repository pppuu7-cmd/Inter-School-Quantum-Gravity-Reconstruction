# ITER143 preregistration — first M/G denominator-cancellation and separated-contact partition

Date: 2026-09-15
Gate: `ITER143_FIXED_GEODESIC_CURVATURE_FIRST_MG_DENOMINATOR_CANCELLATION_CONTACT_PARTITION`
Status: **FROZEN BEFORE ITER140 COEFFICIENTS ARE INSPECTED**

## Motivation

ITER138-142 close exact tensor numerators, row/global derivative allocation, Wick-edge geometry and the sharp shrinking-edge Taylor-jet ceilings for the first connected Gaussian M/G families. ITER140 is independently computing their general-`d` invariant continuation in the frozen 28-element basis.

Before any master integral or `1/epsilon` coefficient is evaluated, the numerator must be partitioned by algebraic cancellation of the two massless propagator denominators. This prevents a polynomial/contact term from being counted as a separated two-propagator tail and prevents a fixed-`L` contact from being mistaken for an affine endpoint divergence.

This preregistration is frozen while ITER140 is still running; no ITER140 coefficient value is known or used here.

## Frozen families and denominator convention

For each of

1. `M_R2_chi1_dR1`,
2. `M_R1_chi1_dR2`,
3. `G_R1_chi2_Gamma2_dR1`,

consume the ITER140 invariant numerator expansion in

`Q=q^2`, `K=k^2`, `S=q.k`, `a=q.n`, `b=k.n`, `n^2=1`,

with the connected Gaussian propagator denominator `Q K`.

No momentum-routing identity such as `S=(p^2-Q-K)/2`, no integration by parts, and no target-based cancellation may be used to change the frozen invariant representation before this partition.

## Frozen algebraic classes

For each ITER140 basis term

`c(d) * X * Q^i K^j S^l`,

where `X` is either `1`, `a^2`, `a b`, or `b^2`, classify solely by the explicit powers `i,j`:

- `TWO_PROPAGATOR`: `i=0`, `j=0`; denominator remains `Q K`.
- `Q_CANCELLED`: `i>=1`, `j=0`; the q propagator is cancelled and the q Fourier transform is a derivative of a contact distribution on the q Wick edge, while the k propagator remains.
- `K_CANCELLED`: `i=0`, `j>=1`; analogously contact on the k Wick edge with q propagator retained.
- `BOTH_CANCELLED`: `i>=1`, `j>=1`; both propagators cancel and the term is fully local/distributional in the two Wick-edge separations.

Extra powers `i>1` or `j>1` become additional derivatives of the corresponding contact distribution; they do not restore a nonlocal propagator.

The partition is applied coefficientwise both to the exact `c(d)` formula and to its `d=4-2 epsilon` expansion through O(epsilon) emitted by ITER140.

## Frozen separated-`L` support rule from ITER141

Use the anchored geometry `x=0`, `y=L n`, `z(tau)=tau L n`, with fixed `L>0`.

### M1 — `M_R2_chi1_dR1`

- q edge: `x-z = tau L`, shrinking only at lower endpoint.
- k edge: `x-y = L`, never shrinks for `L>0`.

Hence:

- `Q_CANCELLED`: allowed only as a lower-endpoint local/contact contribution times the nonlocal k line;
- `K_CANCELLED`: `SEPARATED_L_CONTACT_ZERO`, because it contains derivatives of `delta(x-y)=delta(L n)`;
- `BOTH_CANCELLED`: `SEPARATED_L_CONTACT_ZERO` for `L>0`;
- `TWO_PROPAGATOR`: remains a genuine nonlocal candidate, with lower-endpoint singularity governed by ITER142 q-edge jet <=4.

### M2 — `M_R1_chi1_dR2`

- q edge: `x-y = L`, fixed nonzero.
- k edge: `z-y = -(1-tau)L`, shrinking only at upper endpoint.

Hence:

- `Q_CANCELLED`: `SEPARATED_L_CONTACT_ZERO`;
- `K_CANCELLED`: allowed only as an upper-endpoint local/contact contribution times the nonlocal q line;
- `BOTH_CANCELLED`: `SEPARATED_L_CONTACT_ZERO`;
- `TWO_PROPAGATOR`: genuine nonlocal candidate, upper-endpoint singularity governed by ITER142 k-edge jet <=4.

### G1 — `G_R1_chi2_Gamma2_dR1`

- q edge: `x-z = -tau L`, shrinking at lower endpoint;
- k edge: `z-y = -(1-tau)L`, shrinking at upper endpoint.

Hence:

- `Q_CANCELLED`: lower-endpoint local/contact contribution; at the upper endpoint the q contact is at fixed `L` and has no support.
- `K_CANCELLED`: upper-endpoint local/contact contribution; at the lower endpoint the k contact is at fixed `L` and has no support.
- `BOTH_CANCELLED`: requires simultaneous support at `tau=0` and `tau=1` for fixed `L>0` and is therefore `SEPARATED_L_CONTACT_ZERO`.
- `TWO_PROPAGATOR`: genuine nonlocal candidate, with ITER142 jet <=4 at both endpoints.

## Frozen machine outputs

If ITER140 scientifically passes, ITER143 must emit for every family:

1. all 28 basis labels with their `(i,j,l,X)` metadata;
2. exact general-`d` coefficient and O(epsilon) coefficient pair;
3. algebraic class among the four frozen classes;
4. nonzero coefficient counts and coefficient sums grouped by class only as bookkeeping, never as a physical cancellation test;
5. separated-`L` support status at lower/upper endpoint according to the frozen geometry above;
6. a reduced manifest of terms that can contribute to a separated connected correlator:
   - all `TWO_PROPAGATOR` terms;
   - only the endpoint-local one-propagator classes on the edge that actually shrinks;
7. a manifest of terms pruned as fixed-`L` or incompatible double-contact distributions;
8. ITER142 sharp jet ceiling attached to each surviving singular endpoint;
9. exact reconstruction check: sum of all four algebraic classes reproduces the full ITER140 invariant numerator coefficientwise before any support pruning.

## Frozen stopping rules

- If ITER140 is not `PASS_SCOPED_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION_CLOSED_POLE_INTEGRATION_OPEN`, this gate is `BLOCKED_BY_ITER140_GENERAL_D_AUTHORITY` and no coefficient partition is interpreted physically.
- If class recombination fails or a basis label cannot be assigned uniquely, classify `SCIENTIFIC_FAIL_DENOMINATOR_CANCELLATION_PARTITION`.
- If all partitions, support rules, epsilon bookkeeping and recombination checks pass:
  `PASS_SCOPED_FIRST_MG_DENOMINATOR_CANCELLATION_CONTACT_PARTITION_CLOSED_MASTER_POLES_OPEN`.

## Claim ceiling

A PASS distinguishes genuine two-propagator numerator structures from endpoint contacts and separated-`L` contact zeros. It does not evaluate any loop/affine master integral, `1/epsilon` coefficient, `B1`, noncancellation result, finite `B0`, EDT comparison, bridge, new physics or candidate theory. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
