# Current front — ISQGR

Date: 2026-09-17.

Overall scientific programme: **50%**. Candidate theory: **0% / UNFORMED**. Bridge credit: **0**.

GitHub repository state, frozen preregistrations, source-faithful derivations, immutable Actions artifacts, independent Critic results and terminal result files are the authority.

## Corrected authoritative chain

### ITER155 — superseded auto-PASS

Terminal scientific status:

`BLOCKED_SCOPED_ITER155_TENSOR_RESOLVED_FIRST_MG_ENDPOINT_RESIDUE_TO_ITER118_BASIS_PROJECTION_NOT_OPERATIONALLY_DEFINED`.

### ITER156 — endpoint system underdetermined

`BLOCKED_SCOPED_ITER156_ENDPOINT_COEFFICIENTS_UNDERDETERMINED`.

Admissible endpoint equation rank `0`, nullity `8`. Missing equations are not zero coefficients.

### ITER157 — pre-existing equation search exhausted

`BLOCKED_SCOPED_ITER157_NO_SOURCE_FAITHFUL_ENDPOINT_TENSOR_POLE_EQUATION_FOUND`.

### ITER158 — automated implementation invalid

`INVALID_ITER158`.

The runner checked repository/manifest presence instead of performing the frozen new-information derivation.

### ITER159 — source convention manifest incomplete

`BLOCKED_SCOPED_ITER159_SOURCE_CONVENTION_MANIFEST_INCOMPLETE_METRIC_SIGNATURE`.

### ITER160 — raw G two-propagator endpoint support PASS

`PASS_SCOPED_ITER160_RAW_G_B2S2_ENDPOINT_SUPPORT_SPLIT_INDEPENDENTLY_CONFIRMED`.

For `G_R1_chi2_Gamma2_dR1 : b^2*S^2`, each raw TWO_PROPAGATOR affine endpoint support residue is

`-525/(pi^4 L^10) * 1/epsilon`.

Actions run `35247996587`; artifact `10508931715`; ZIP SHA256 `95f99efaa328735ab1e99efebc99cf575301f074e8bba0c00dd2632e2779c2b1`.

This is raw scalar support, not an ITER118 coefficient or complete endpoint counterterm.

### ITER161 — endpoint-selected open metric leg derived

Structural PASS:

`PASS_STRUCTURAL_ITER161_ENDPOINT_SELECTED_OPEN_METRIC_LEG_FACTORIZATION`.

Source-faithful exact factorizations:

- upper endpoint (`k` shrinking): `G1 = sum_ab A_ab V_upper_ab`;
- lower endpoint (`q` shrinking): `G1 = sum_mu,ab R_mu,ab W_lower_mu,ab`.

The lower object retains derivative label `mu`.

Terminal classification:

`BLOCKED_SCOPED_ITER161_G_ENDPOINT_TENSOR_LIFT_EXACT_MISSING_PRIMITIVE`.

Actions run `35250000806`; artifact `10509541616`; terminal result commit `09e48b9dd61bdfdc6fc654c8af06eca1e9a528c7`.

The raw open tensor exists. ITER161 did not provide the complete distributionally renormalized pole tensor.

### ITER162 — frozen 36-column covariant span SCIENTIFIC FAIL

Preregistration:

`ITER162_OPEN_G_ENDPOINT_DISTRIBUTIONAL_R_OPERATION_AND_POLE_TENSOR`.

Initial structural enumeration run `35261892526`, artifact `10515090371`, classified only

`STRUCTURAL_ENUMERATION_ONLY_NOT_SCIENTIFIC_PASS`.

It prospectively froze:

- upper candidate columns: `36`;
- explicit-`K` columns: `10`.

#### Scoped structural K-divisibility result

Within the frozen 36-space, exact polynomial quotient algebra modulo `K=k^2` gave:

`PASS_STRUCTURAL_ITER162_COMPLETE_FROZEN_SPAN_TENSOR_K_DIVISIBILITY_KERNEL`.

Actions run `35266919815`, job `105356271332`, artifact `10517062876`, ZIP SHA256 `5bbd727348a117353062fb7b4d04e53277c831d96da5670b2d3f9953712af573`.

Exact in both `D=4` and `D=5`:

- quotient rank `26`;
- K-divisible kernel dimension `10`;
- kernel equals exactly the 10 explicit-`K` columns.

This remains true **inside the frozen 36-space**, but that space is not source-complete.

#### Source reconstruction falsifier

After implementation-only repairs enforcing frozen `n^2=1` and adequate exact fixture rank, the selected coefficient system had exact rank `36` and stable `D=9,10` continuation, but every changed-`q,k` overdetermined source held-out in `D=4..10` failed.

This was then reduced to a fit-free exact source counterexample.

Take

`n=e0`, `q0=k0=0`, hence `a=n.q=0`, `b=n.k=0`.

For transverse open indices `i,j != 0`, all 36 frozen covariants vanish identically by the preregistered explicit tangent-count rule.

The source-derived `V_upper_ij` is nonzero.

Researcher direct witness, run `35267891590`, job `105359526262`:

- `D=4`, `q=(0,1,2,0)`, `k=(0,2,-1,1)` gives exact values including `V_11=6`, `V_12=-3`, `V_13=3`, `V_22=3/2` while every frozen column is zero;
- 18 exact nonzero witness components occur across three independent Researcher cases.

Artifact `10517765160`, `iter162-fast-n2-witness`, ZIP SHA256 `ce81455b9833ac95b5c70b48b28c075611d11ca90431675cbfee7c897c789704`.

Independent direct Critic, same run, job `105359526273`, uses changed `D=4,5,6` configurations and no Researcher JSON. It independently finds nonzero source transverse components in every case while all 36 frozen covariants vanish.

Critic verdict:

`PASS_CRITIC_ITER162_DIRECT_N2_FROZEN_SPAN_FALSIFIER_CONFIRMED`.

Artifact `10517556166`, ZIP SHA256 `429a1685c5cc7235c786bf2abb70d0d0b415b1c2d39c3364b0ccf54d26692996`.

Exact defect mechanism: the two microscopic tangent vectors `n_m n_n` may contract internally to `n^2=1`, leaving tangent-neutral momentum-degree-four symmetric rank-two structures. The frozen 36 generator carried tangent count only through `a=n.q`, `b=n.k`, or free `n_a`, and therefore omitted the internally saturated `n^2` sector.

Terminal classification:

**`SCIENTIFIC_FAIL_ITER162_FROZEN_TENSOR_COVARIANCE_OR_SUPPORT_IDENTITY_FALSE`**.

Terminal result commit:

`1ad62d919771e6f1984443d805c1442c2fda9563`.

The failed identity is preserved. The 36-column basis is **not repaired inside ITER162**.

## ITER162 downstream status

Because the source tensor is outside the prospectively frozen span, ITER162 terminates before a source-complete support/Laurent calculation.

Therefore:

- covariant reconstruction in frozen 36-space: `SCIENTIFICALLY_FALSIFIED_AS_INCOMPLETE`;
- held-out reconstruction: `FAIL_EXACT_SOURCE_HELDOUTS`;
- tensor K-divisibility: `PASS_STRUCTURAL_WITHIN_FROZEN_36_ONLY_NOT_SOURCE_COMPLETE`;
- distributional Laurent operation: `NOT_REACHED_AFTER_TERMINAL_SCIENTIFIC_FAIL`;
- local ambiguity dimension: `UNDEFINED_NOT_COMPUTED`;
- pole tensor dimension: `UNDEFINED_NOT_COMPUTED`;
- quotient rank: `UNDEFINED_NOT_COMPUTED`;
- ITER118 matching: `UNAUTHORIZED`.

No missing pole/contact is interpreted as zero.

## Slot status

Slots 1–4: CLOSED.

Slot 5: `CHARACTERIZED_NUMERICALLY_OPEN`.

Slot 6: `CLOSED_SCOPED_FIRST_MG_CONNECTED_CROSS`.

Slot 7: **OPEN / STRUCTURALLY ADVANCED** — source-faithful endpoint-selected open tensor exists, but the first prospectively frozen covariant reconstruction basis was falsified before Laurent/quotient completion.

Slot 8: `OPEN_LINE_DEFECT_MIXING`.

Slot 9: `OPEN_RENORMALIZED_CONTACT_MAPPING`.

Slot 10: `OPEN_ITER124_TERMINAL_OUTPUTS`.

No `B1_total`.

## Current scientific frontier

The useful chain is now:

1. ITER140: exact arbitrary-integer-D indexed first-M/G machinery.
2. ITER160: exact raw affine TWO_PROPAGATOR endpoint support.
3. ITER161: exact endpoint-selected source-derived open metric leg.
4. ITER162: direct source counterexample proves the first 36-column covariant ansatz incomplete.

The current earliest missing primitive is therefore **not yet the Laurent operation**. It is:

> a prospectively complete degree-four symmetric covariant basis for `V_upper_ab` that allows all contractions of the two tangent vectors, including internally saturated `n^2` structures, before source coefficient reconstruction or support classification.

A diagnostic-only omitted sector contains 15 `n^2`-saturated tangent-neutral candidate columns. That diagnostic is not an ITER162 repair and must be frozen prospectively in a new gate before its source coefficients are interpreted.

## Next admissible gate

A new prospective post-ITER162 gate is now authorized.

It must:

1. derive/enumerate the complete two-tangent covariant closure including `n^2` saturation before outcome;
2. prove exact basis rank/dependencies under `n^2=1`;
3. independently reconstruct `V_upper_ab` with changed fixtures and held-outs;
4. recompute full tensor-level K-divisibility on the source-containing complete span;
5. only after those PASS, return to the unseparated distributional Laurent/R-operation, full `A_local`, and quotient.

No ITER118 coefficient/rank solve is allowed before a complete source-authoritative pole-tensor/quotient manifest exists.

## Persistent locks

`B1_total = UNAUTHORIZED`.

`ALL_KNOWN_SCHOOLS_FAIL = false`.

`NEW_QG_THEORY_REQUIRED = false`.

`NEW_PHYSICS_FOUND = false`.

`BRIDGE_DERIVED = false`.

`ITER118_MATCHING_AUTHORIZED = false`.

Candidate action/Hamiltonian/field equations remain unauthorized. Candidate theory remains **UNFORMED / 0%**.
