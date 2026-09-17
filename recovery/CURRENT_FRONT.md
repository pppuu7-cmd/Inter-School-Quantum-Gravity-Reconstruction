# Current front — ISQGR

Date: 2026-09-17.

Overall scientific programme: **50%**. Candidate theory: **0% / UNFORMED**. Bridge credit: **0**.

## Corrected authoritative chain

### ITER155 — auto-PASS superseded by independent audit

Correct scientific status:

`BLOCKED_SCOPED_ITER155_TENSOR_RESOLVED_FIRST_MG_ENDPOINT_RESIDUE_TO_ITER118_BASIS_PROJECTION_NOT_OPERATIONALLY_DEFINED`.

The green auto-PASS used broad lexical/projector evidence and did not operationally define the tensor-resolved first-M/G endpoint residue map to the immutable ITER118 basis

`[R,S,DR,DS,BoxR,D2R,BoxS,D2S]`.

No coefficient is thereby set to zero.

### ITER156 — exact identifiability BLOCKED

Run `35164455129`; job `105022290476`; artifact `10474390964`; ZIP SHA256 `0c71f1e6b966b3cad2769608c3888ff141aa66cf2cca15ab1a8da57b1b38ba93`.

Classification:

`BLOCKED_SCOPED_ITER156_ENDPOINT_COEFFICIENTS_UNDERDETERMINED`.

Admissible endpoint equation rank `0`, nullity `8`. Missing equations are not zero coefficients.

### ITER157 — pre-existing equation search exhausted

Preregistration `88aabc760dc01ad73585276d3345bfdf8a90aedf`; run `35176051421`; artifact `10479215087`; ZIP SHA256 `1c5aea020ed6338309132944fd2f3030cedff33d5f6feeee42ee9cd5e19a54c5`.

Seven lexical candidates were adjudicated in raw context; accepted `0/7`.

Terminal:

`BLOCKED_SCOPED_ITER157_NO_SOURCE_FAITHFUL_ENDPOINT_TENSOR_POLE_EQUATION_FOUND`.

### ITER158 — automated scientific implementation INVALID

Principal preregistration `e12634d544b345a4e309021cebbb251c9a549abd`; implementation `b93890fff1cf9e5ec03c12e479ba283c464bf9ed`; run `35183584814`; artifact `10481575859`.

Independent audit commit `f00f3cdf4a298798f5082e3b7dac9191f313e3f3`.

Adjudication:

`INVALID_ITER158`.

The auto runner performed repository regex-presence checks plus manifest-existence checks rather than the frozen new-information derivation/acquisition chain.

### ITER159 — exact primary-source manifest BLOCKED

Preregistration `d741d367345c5c620f8981fb8ed9fd0d87e8dc71`; source-acquisition run `35230270651`; artifact `10500703567`; ZIP SHA256 `0a6daac0e655b02c8898395ebb832e249b28938cbc863b486ab72547f6cc47dc`.

Terminal:

`BLOCKED_SCOPED_ITER159_SOURCE_CONVENTION_MANIFEST_INCOMPLETE_METRIC_SIGNATURE`.

Fröb arXiv:1706.01891v2 remains `REFERENCE_ONLY` for the curvature-composite first-M/G endpoint problem unless exact operator/topology equivalence is separately proved.

### ITER160 — raw G two-propagator endpoint support PASS

Preregistration `43fb329bbc9079d0f2b9413b4644b2658da53829`.

Classification:

`PASS_SCOPED_ITER160_RAW_G_B2S2_ENDPOINT_SUPPORT_SPLIT_INDEPENDENTLY_CONFIRMED`.

For `G_R1_chi2_Gamma2_dR1 : b^2*S^2`, the frozen total Beta residue `35` splits under the frozen local meromorphic prescription into `35/2` at each affine endpoint. With graph prefactor `-30/(pi^4 L^10)`, each raw TWO_PROPAGATOR endpoint support piece is

`-525/(pi^4 L^10) * 1/epsilon`.

GitHub Actions run `35247996587` later completed successfully. Artifact `10508931715`; ZIP SHA256 `95f99efaa328735ab1e99efebc99cf575301f074e8bba0c00dd2632e2779c2b1`. The pinned-SymPy CI outputs are byte-identical to the earlier exact local outputs:

- producer JSON SHA256 `424d8cdd936de13bddf745754ed13edf5da04eeee90249a84be7c64595007535`;
- Critic JSON SHA256 `fe6903f1d4bc2fdc5d85526fb7cb34b53ccc6b0b046e363aaa7380824cbeff2b`.

These are raw support residues, not ITER118 coefficients or endpoint counterterms.

### ITER161 — endpoint-selected open tensor derived; complete pole tensor BLOCKED

Preregistration `e004e8ff0d4977676b3e70c34a78c438965dc62a`.

Initial structural producer `e7be19d781e1121646913264cbe7f2da007f0ae0` established a post-`g2_real` pretrace object but initially overestimated the loss of metric-leg information.

The preliminary Critic `c1d5fbbfe7c2e7ea65908901bddbb1c33148d46b` was self-corrected before terminalization in commit `c19f407f48de41978c73c04df634a8deddf86785`: affine endpoint geometry fixes which graviton leg is shrinking and which must remain open.

Endpoint-selected producer `3b47cbeaa5ec3ed8d3023b8774a8f8799aac02db` then derived exact source-faithful factorizations:

- upper endpoint (`k` shrinking): `G1 = sum_ab A_ab V_upper_ab`, with a symmetric open q-side metric pair;
- lower endpoint (`q` shrinking): `G1 = sum_mu,ab R_mu,ab W_lower_mu,ab`, with symmetric open k-side metric pairs and the derivative label `mu` retained.

Exact `D=4,5,6` Fraction fixtures reconstruct `G1_value` identically in both factorizations. This derivation does not consume the known ITER160 `-525` pole normalization.

Structural sub-result:

`PASS_STRUCTURAL_ITER161_ENDPOINT_SELECTED_OPEN_METRIC_LEG_FACTORIZATION`.

Final Critic commit `168ed215e8cf9bb167d3cb6efaf633a58e1cb1c6`, verdict:

`PASS_CRITIC_ITER161_OPEN_LEG_DERIVED_POLE_EXTENSION_BLOCKER_SOUND`.

Workflow head `fc33a5b677ab608b2f46aaad019aceb5f03bf18b`; run `35250000806` **success**; artifact `10509541616`; ZIP SHA256 `7a925baee50236385ed85936d7ffa8174da67bb7bed0de7100e3a331081ab5a5`.

Exact artifact payloads:

- pretrace diagnostic JSON SHA256 `40e7a5ff9f04cd1f0a83dda33ce0c1a6d015497e2e688f83a43ba9ce4688d6a8`;
- open-leg factorization JSON SHA256 `556889d417ee71b89d7478c8513afe72aae171cb02fdfe55d0edc2214e2fc101`.

Terminal result commit `09e48b9dd61bdfdc6fc654c8af06eca1e9a528c7`.

Terminal classification:

`BLOCKED_SCOPED_ITER161_G_ENDPOINT_TENSOR_LIFT_EXACT_MISSING_PRIMITIVE`.

The blocker is now precise and narrower: the free symmetric metric leg exists, but the **complete endpoint pole tensor** does not. The missing primitive is a source-faithful distributional endpoint R-operation/extension acting on the source-derived open-leg **unseparated** G endpoint vertex before Q/K contact separation, preserving the selected free metric leg/orientation and assigning the cancelled-propagator contact contributions.

This is required because ITER151 has three nonzero G upper-endpoint K-cancelled contacts and ITER153 leaves their line restriction/poles unauthorized; ITER124 requires endpoint/line renormalization before contact separation.

## Slot status

Slots 1–4: CLOSED.

Slot 5: `CHARACTERIZED_NUMERICALLY_OPEN`.

Slot 6: `CLOSED_SCOPED_FIRST_MG_CONNECTED_CROSS`.

Slot 7: **OPEN / PARTIALLY ADVANCED** — raw open metric-leg tensor factorization now derived, but complete distributionally renormalized endpoint pole tensor and ITER118 coefficient equations remain blocked.

Slot 8: `OPEN_LINE_DEFECT_MIXING`.

Slot 9: `OPEN_RENORMALIZED_CONTACT_MAPPING`.

Slot 10: `OPEN_ITER124_TERMINAL_OUTPUTS`.

No `B1_total`.

## Current scientific frontier

The useful information chain is now:

1. ITER140: exact arbitrary-integer-D indexed first-M/G machinery.
2. ITER150: nonzero raw G `b^2*S^2` simple pole.
3. ITER160: exact affine endpoint support split of that TWO_PROPAGATOR pole.
4. ITER161: exact endpoint-selected open symmetric metric-leg factorization before final scalar contraction.
5. Remaining bottleneck: define the **distributionally renormalized pole tensor on that open leg before contact separation**.

The old statement “tensor information is simply missing” is no longer correct.

## Next admissible gate

`ITER162_OPEN_G_ENDPOINT_DISTRIBUTIONAL_R_OPERATION_AND_POLE_TENSOR`.

It must start from the ITER161 open-leg tensors, not from the scalar 28-invariant table. It must test whether a prospectively frozen local/covariant extension prescription determines the endpoint `1/epsilon` tensor residue uniquely or leaves explicit local ambiguity parameters. If an ambiguity remains, it must be exhibited as an exact tensor/operator span rather than hidden in a generic BLOCKED label.

No ITER118 coefficient solve or rank claim is allowed until a complete pole-tensor manifest exists.

## Persistent locks

`B1_total = UNAUTHORIZED`.

`ALL_KNOWN_SCHOOLS_FAIL = false`.

`NEW_QG_THEORY_REQUIRED = false`.

`NEW_PHYSICS_FOUND = false`.

`BRIDGE_DERIVED = false`.

Candidate action/Hamiltonian/field equations remain unauthorized. Candidate theory remains **UNFORMED / 0%**.
