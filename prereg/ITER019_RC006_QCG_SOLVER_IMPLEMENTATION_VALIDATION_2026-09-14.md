# ITER019 preregistration - bounded q-CG solver implementation validation

Date: 2026-09-14

## Authorization basis

ITER018 terminal class: `RC006_EQ27_GRAPH_AND_EVENK_CATEGORY_PINNED_IMPLEMENTATION_PREREG_ALLOWED`.

ITER019 is the separately preregistered bounded implementation-validation checkpoint permitted by that class. It does not authorize Iter012, Eq.(29)/Lambda amplitudes, alpha selection, bridge credit or candidate-theory construction.

## Fixed construction principle

Do **not** import a closed-form external q-Clebsch-Gordan coefficient formula and do not fit phases to expected answers. Construct the embedding coefficients in target convention directly from the already pinned algebra:

- target `q = exp(2*pi*i/(k+2))`;
- target q-number `[x] = (q^(x/2)-q^(-x/2))/(q^(1/2)-q^(-1/2))`;
- source-qualified basis action
  `Jz|j,m>=m|j,m>` and
  `J+|j,m>=sqrt([j-m][j+m+1])|j,m+1>`,
  `J-|j,m>=sqrt([j+m][j-m+1])|j,m-1>`;
- target coproduct (A5)
  `Delta(J+/-)=q^(-Jz/2) tensor J+/- + J+/- tensor q^(Jz/2)`;
- target admissibility A7;
- target bilinear A8/A9 convention, with no complex conjugation inserted by convenience;
- target cap B2/cup B4 for the singlet channel.

For an admissible channel `(j1,j2)->j`, obtain the highest-weight embedding vector as the one-dimensional null space of `Delta(J+)` in total weight `m=j`, normalize with the target bilinear norm, and generate lower weights by `Delta(J-)` divided by the source-qualified single-representation ladder coefficient. A channel with non-one-dimensional numerical nullspace, isotropic/zero bilinear norm, or unstable recurrence is BLOCKED/FAIL, not repaired by a fitted phase.

Residual scalar sign freedom is allowed where A9 leaves it. Only the `j tensor j -> 0` channel may be sign-pinned directly to B2. Other channel signs must not be fitted to recoupling expectations.

## Parallel lanes

### Lane A - algebra/intertwiner residuals at even k=12

Fixed channel panel:
- `(1/2,1/2)->0,1`;
- `(1/2,1)->1/2,3/2`;
- `(1,1)->0,1,2`;
- `(3,3)->j` for every `j=0,1,...,6`;
- `(4,4)->j` for every admissible `j=0,1,...,4` (root-of-unity trace-zero sector present in the discarded complement).

For every generated magnetic state test Jz, J+ and J- intertwining. PASS threshold: maximum absolute residual `< 5e-10`, and every expected highest-weight nullspace dimension equals one.

### Lane B - A9 / A8-projector / cap validation

At k=12:
- A9 bilinear orthogonality for every Lane-A channel;
- for `(3,3)` the complete direct-sum projector must equal the full 49-dimensional identity because all `j=0..6` channels exhaust the tensor product;
- for `(4,4)`, the A8 admissible projector built from `j=0..4` must be bilinear-idempotent with numerical rank 25, while the tensor-product space has dimension 81; no demand that it equal the identity is allowed;
- singlet embeddings `(j,j)->0` for `j=1/2,1,2,3,4` must agree with B2 after only the permitted overall sign choice.

PASS thresholds: A9 max residual `< 5e-10`; full `(3,3)` completeness max residual `< 2e-9`; `(4,4)` projector idempotence max residual `< 2e-9` and rank exactly 25 at singular-value threshold `1e-8`; B2 singlet residual `< 2e-9`.

### Lane C - recoupling/F invariant checks at k=12

Construct three-body coupling bases only from the solver q-CG embeddings. Fixed panels:
- `j1=j2=j3=1/2`, total `J=1/2`;
- `j1=j2=j3=1`, total `J=1`.

Build the recoupling matrix between `((j1 j2) j12, j3)->J` and `(j1, (j2 j3) j23)->J` by target bilinear overlap. Do not sign-fit rows/columns. The independent even-k source arXiv:2304.02527v2 states the F matrices can be chosen real and obey orthogonality; use only the sign-gauge-invariant obligations here.

PASS predicates:
- each recoupling matrix is square with the expected allowed intermediate channels;
- result is independent of final magnetic M to max difference `< 2e-9`;
- `F^T F = I` to max residual `< 2e-9`;
- maximum imaginary part `< 2e-9`.

If the solver convention produces a row/column sign-gauge equivalent real orthogonal F, that is PASS; no coefficient sign is altered to force an external matrix entry.

### Lane D - classical-limit structural check

Construct the same low-spin channel/projector data with an undeformed `q=1` action/coproduct using the same highest-weight algorithm, and compare to a large-k deformation `k=10000`. Do not compare sign-sensitive raw coefficient arrays. Compare the bilinear channel projectors for:
- `(1/2,1/2)->0,1`;
- `(1,1)->0,1,2`.

PASS if every projector Frobenius difference is `< 2e-3`; this is only a continuity sanity check, not evidence for a continuum quantum-gravity limit.

## Aggregate decision

All four lanes run independently/concurrently and emit JSON evidence. Green CI is not PASS by itself.

Terminal classes:
- `RC006_QCG_SOLVER_VALIDATED_BOUNDED_K12`
- `RC006_QCG_SOLVER_ALGEBRA_RESIDUAL_FAIL`
- `RC006_QCG_A8_A9_CAP_FAIL`
- `RC006_QCG_RECOUPLING_INVARIANT_FAIL`
- `RC006_QCG_CLASSICAL_LIMIT_SANITY_FAIL`
- `RC006_QCG_IMPLEMENTATION_INFRASTRUCTURE_PARTIAL`

Only `RC006_QCG_SOLVER_VALIDATED_BOUNDED_K12` may authorize preregistration of the next narrowly scoped physics/reconstruction test. It still does not by itself authorize Iter012 or Eq.(29)/Lambda amplitude work; that authorization must be stated explicitly in a later preregistration after examining the validation result.

## Fixed claim locks

Always false during ITER019: `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `iter012_retry_authorized`, `eq29_amplitude_authorized`, `preferred_alpha_found`.