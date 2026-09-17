# Current front — ISQGR

Date: 2026-09-17.

Overall scientific programme: **50%**. Candidate theory: **0% / UNFORMED**. Bridge credit: **0**.

## Corrected authoritative chain

### ITER155 — auto-PASS superseded by independent audit

The green auto result `PASS_SCOPED_ITER155_ENDPOINT_COUNTERTERM_AUTHORITY_IDENTIFIED_COEFFICIENT_DERIVATION_ALLOWED` is **not** accepted as the scientific terminal interpretation. Its implementation used broad lexical/projector evidence and did not operationally define the tensor-resolved first-M/G endpoint residue map to the immutable ITER118 basis.

Correct scientific status:

`BLOCKED_SCOPED_ITER155_TENSOR_RESOLVED_FIRST_MG_ENDPOINT_RESIDUE_TO_ITER118_BASIS_PROJECTION_NOT_OPERATIONALLY_DEFINED`.

Immutable endpoint basis:

`[R,S,DR,DS,BoxR,D2R,BoxS,D2S]`.

No coefficient is thereby set to zero.

### ITER156 — exact identifiability BLOCKED

Authoritative run `35164455129`; job `105022290476`; artifact `10474390964`; ZIP SHA256 `0c71f1e6b966b3cad2769608c3888ff141aa66cf2cca15ab1a8da57b1b38ba93`.

Classification:

`BLOCKED_SCOPED_ITER156_ENDPOINT_COEFFICIENTS_UNDERDETERMINED`.

There are zero admissible pre-existing tensor-resolved endpoint pole equations for the 8-dimensional ITER118 basis: rank `0`, nullity `8`. Missing equations are **not** eight zero coefficients.

### ITER157 — pre-existing source-equation audit BLOCKED

Preregistration `88aabc760dc01ad73585276d3345bfdf8a90aedf`; run `35176051421`; job `105057889040`; artifact `10479215087`; ZIP SHA256 `1c5aea020ed6338309132944fd2f3030cedff33d5f6feeee42ee9cd5e19a54c5`.

Seven lexical candidates were adjudicated in raw context; accepted `0/7`. Independent Critic: `PASS_CRITIC_ITER157_BLOCKED_CLASSIFICATION_SOUND`.

Terminal:

`BLOCKED_SCOPED_ITER157_NO_SOURCE_FAITHFUL_ENDPOINT_TENSOR_POLE_EQUATION_FOUND`.

This exhausts the pre-existing-equation search path only. It is not physical FAIL.

### ITER158 — automated scientific implementation INVALID

Principal preregistration: `e12634d544b345a4e309021cebbb251c9a549abd`.

Auto implementation: `b93890fff1cf9e5ec03c12e479ba283c464bf9ed`; run `35183584814`; artifact `10481575859`; artifact ZIP SHA256 `894882977d2cdd22c6cfc5ae736054366039010653401b5cb1755fd2cb19515a`.

Independent audit: `analysis/ITER158_AUTO_RESEARCH_ADVERSARIAL_AUDIT_2026-09-17.md`, commit `f00f3cdf4a298798f5082e3b7dac9191f313e3f3`.

Adjudication:

`INVALID_ITER158` — implementation error.

The auto runner performed repository regex-presence checks plus manifest existence checks, rather than the frozen new-information chain `microscopic tensors -> regulated endpoint kernel -> raw tensor pole -> support -> endpoint equation`. Its emitted BLOCKED label remains diagnostic only and is not the scientific terminal result of the principal gate.

### ITER159 — exact primary-source convention manifest BLOCKED

Preregistration: `d741d367345c5c620f8981fb8ed9fd0d87e8dc71`.

Latest source-acquisition run: `35230270651`; artifact `10500703567`; ZIP SHA256 `0a6daac0e655b02c8898395ebb832e249b28938cbc863b486ab72547f6cc47dc`; source archive SHA256 `b3c0137deb5e599912e0dfc96c2c6375c4715ad5e561c5cb795dae43902b03fd`.

Manual adjudication: `analysis/ITER159_MANUAL_SOURCE_CONVENTION_ADJUDICATION_2026-09-17.md`, commit `a382f94d03ab8f8cc80c897894479240ad4ec291`.

Terminal:

`BLOCKED_SCOPED_ITER159_SOURCE_CONVENTION_MANIFEST_INCOMPLETE_METRIC_SIGNATURE`.

The current exact evidence set has zero persisted source-evidence rows fixing the first frozen field `metric_signature`, and no source-only mathematical derivation of that field is persisted. This does not assert that the paper contains no recoverable convention. Fröb remains `REFERENCE_ONLY` for the curvature-composite first-M/G endpoint problem unless exact operator/topology equivalence is separately proved.

### ITER160 — raw G two-propagator endpoint support PASS

Exploratory producer values were explicitly recorded before confirmation and receive no blind-discovery credit.

Confirmatory preregistration: `43fb329bbc9079d0f2b9413b4644b2658da53829`.

Producer implementation: `6b6f91caffd7c41dec19a4635c74e7c7b56b0770`.

Independent Critic implementation: `f4a70ad87a7c5623ea15c696bb1a8f39f362f8f1`.

Terminal result: `analysis/ITER160_RESULT_2026-09-17.md`, commit `10e6af612962db80ecd99c074a09aac32027ffff`.

Classification:

`PASS_SCOPED_ITER160_RAW_G_B2S2_ENDPOINT_SUPPORT_SPLIT_INDEPENDENTLY_CONFIRMED`.

For the already-frozen ITER150 raw TWO_PROPAGATOR master

`G_R1_chi2_Gamma2_dR1 : b^2*S^2`,

the Beta residue `35` splits under the frozen local meromorphic prescription into

- lower endpoint: `35/2`;
- upper endpoint: `35/2`.

With frozen graph prefactor `-30/(pi^4 L^10)`, the raw simple-pole support pieces are

- lower: `-525/(pi^4 L^10) * 1/epsilon`;
- upper: `-525/(pi^4 L^10) * 1/epsilon`.

Their sum is the ITER150 raw master pole `-1050/(pi^4 L^10) * 1/epsilon`.

Producer checks `10/10` pass. Independent incomplete-Beta recurrence Critic checks `12/12` pass with verdict `PASS_CRITIC_ITER160_RAW_ENDPOINT_SUPPORT_SPLIT_SOUND`.

GitHub Actions run `35247996587`, job `105292991900`, was still `queued` when ITER160 was terminalized; this infrastructure queue state is not a scientific BLOCKED/FAIL and was not used to manufacture PASS.

Crucial ceiling: the two raw endpoint residues are **not** ITER118 coefficients and **not** endpoint counterterms. No ITER153 contact is imported or zeroed, no ITER123 projector is used, and survival through the full ITER124 renormalization sequence remains open.

## Slot status

Slots 1–4: CLOSED.

Slot 5: `CHARACTERIZED_NUMERICALLY_OPEN`.

Slot 6: `CLOSED_SCOPED_FIRST_MG_CONNECTED_CROSS`.

Slot 7: **OPEN / BLOCKED at tensor lift**. A nonzero raw endpoint-supported pole is now confirmed for the G `b^2*S^2` two-propagator master, but no source-faithful free-index map from that raw endpoint tensor to the immutable ITER118 endpoint basis has yet been derived.

Slot 8: `OPEN_LINE_DEFECT_MIXING`.

Slot 9: `OPEN_RENORMALIZED_CONTACT_MAPPING`.

Slot 10: `OPEN_ITER124_TERMINAL_OUTPUTS`.

No `B1_total`.

## Current scientific frontier

The generic source-search loop is closed. The useful new information is now sharper:

1. ITER140 already contains an exact arbitrary-integer-`D` indexed first-M/G contraction engine before its final 28-scalar-invariant reconstruction.
2. ITER150 establishes the nonzero raw G `b^2*S^2` simple pole.
3. ITER160 establishes where that raw pole is supported: exactly half at each endpoint under the frozen local prescription.
4. What is still missing is the **tensor-resolved lift before scalar contraction** that connects the supported raw G pole to an operator equation in the ITER118 endpoint basis.

## Next admissible gate

`ITER161_G_B2S2_ENDPOINT_RAW_TENSOR_LIFT_TO_ITER118_OPERATOR_EQUATIONS`.

The gate must start from the indexed general-`D` machinery, retain the relevant free tensor indices through the pole-producing G-family contraction, carry lower/upper endpoint orientation separately, and only then test decomposition onto `[R,S,DR,DS,BoxR,D2R,BoxS,D2S]`.

It must not invert the 28-scalar invariant reconstruction as though it preserved lost tensor information. If the lift is not unique, terminalize BLOCKED with the exact kernel/null directions or earliest lossy map. No rank solve is authorized before a complete tensor equation manifest is frozen.

## Persistent locks

`B1_total = UNAUTHORIZED`.

`ALL_KNOWN_SCHOOLS_FAIL = false`.

`NEW_QG_THEORY_REQUIRED = false`.

`NEW_PHYSICS_FOUND = false`.

`BRIDGE_DERIVED = false`.

Candidate action/Hamiltonian/field equations remain unauthorized. Candidate theory remains **UNFORMED / 0%**.
