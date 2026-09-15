# ITER140 preregistration — first M/G general-d invariant continuation

Date: 2026-09-15
Gate: `ITER140_FIXED_GEODESIC_CURVATURE_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION`
Status: **FROZEN BEFORE AUTHORITATIVE PRODUCTION RUN**

## Motivation

ITER138/139 now provide exact D=4 tensor numerators and corrected affine single-line ceilings for the first Gaussian M/G families. The ITER124 physical pole contract, however, is defined in `d=4-2 epsilon` and requires higher-pole/subdivergence consistency. A D=4 numerator alone cannot authorize renormalized `1/epsilon` coefficients when O(epsilon) tensor terms may multiply higher poles.

This gate constructs an exact dimensionally continued invariant representation for the three already controlled Gaussian families before any pole extraction.

## Frozen families

1. `M_R2_chi1_dR1`;
2. `M_R1_chi1_dR2`;
3. `G_R1_chi2_Gamma2_dR1`.

No interaction-dressed or nested chi1/chi2 row enters this gate.

## Frozen arbitrary-d conventions

For each positive integer dimension `D>=3`:

- Euclidean flat metric;
- unit line direction `n`;
- de Donder propagator numerator acting on a symmetric source:
  `P_D[S]_ab = S_ab - delta_ab tr(S)/(D-2)`;
- canonical R1, Gamma1, Gamma2 and unreduced R2 formulas are the dimension-independent indexed formulas already frozen in ITER130/131;
- `dR2_mu = i(q+k)_mu R2`;
- no integration by parts, on-shell identity, target data or desired cancellation enters.

## Frozen invariant basis

Each scalar numerator has total momentum degree six and at most quadratic dependence on the unit line vector. Use

`Q=q^2`, `K=k^2`, `S=q.k`, `a=q.n`, `b=k.n`, `n^2=1`.

The candidate covariant basis has exactly 28 monomials:

- 10 monomials `Q^i K^j S^l` with `i+j+l=3`;
- 18 monomials `X Q^i K^j S^l` with `i+j+l=2` and `X in {a^2, a b, b^2}`.

No additional invariant is admitted after production data are seen. Failure of this basis is a scientific block, not permission to enlarge it post hoc.

## Frozen coefficient reconstruction

At each integer D:

1. set `n=e0` only as a coordinate frame;
2. use deterministic small-integer q/k panels;
3. choose a full-rank exact 28-panel invariant design matrix;
4. evaluate each tensor numerator by direct indexed contraction in that D;
5. solve exactly for the 28 invariant coefficients;
6. validate the invariant reconstruction on held-out q/k panels not used in the solve.

The two de Donder maps supply at most `(D-2)^-2`. After multiplying each coefficient by `(D-2)^2`, the frozen formal contraction bound is polynomial degree <=4 in D: there are at most two independent closed Kronecker-trace factors in these rank-2 scalar contractions in addition to the two projector denominators.

Use training dimensions `D=3,4,5,6,7` to fix the degree<=4 polynomial uniquely. Validate **without refitting** at `D=8,9,10`.

## Frozen cross-checks

- D=4 reconstruction must match the committed ITER138/139 tensor implementations on deterministic held-outs.
- Integer-D held-outs must match the reconstructed invariant formula exactly for all three families.
- The reconstructed coefficient functions must have no pole away from the expected de Donder `(d-2)^2` denominator within this representation.
- The epsilon expansion `d=4-2 epsilon` through O(epsilon) is emitted coefficientwise but is not yet multiplied by loop master poles.

## Frozen classifications

- All 28-basis solves full-rank; all held-outs exact; every `(d-2)^2 c(d)` has degree<=4; D=8,9,10 validations pass; D=4 agrees with ITER138/139:
  `PASS_SCOPED_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION_CLOSED_POLE_INTEGRATION_OPEN`.
- Basis/rank/dimensional held-out failure:
  `SCIENTIFIC_FAIL_GENERAL_D_INVARIANT_RECONSTRUCTION`.
- Required polynomial degree >4 or held-out dimensional continuation mismatch:
  `BLOCKED_GENERAL_D_TRACE_DEGREE_AUTHORITY`.
- Infrastructure failure before predicates are evaluated:
  `NUMERICAL_OR_INFRASTRUCTURE_FAIL`.

## Claim ceiling

A PASS supplies dimensionally continued numerator coefficients and their O(epsilon) expansion only. It is not a renormalized pole, B1, noncancellation result, B0, EDT comparison, bridge, new physics or candidate theory. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
