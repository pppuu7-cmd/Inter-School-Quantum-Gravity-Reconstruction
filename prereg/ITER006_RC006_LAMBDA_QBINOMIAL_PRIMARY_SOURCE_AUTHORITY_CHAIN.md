# Preregistration — ITER006 RC006 Lambda q-binomial primary-source authority chain

Frozen prospectively on 2026-09-13 before implementation or production evidence.

## Purpose
The immutable Buffenoir–Roche source `math/9910147v1` uses q-binomial notation in the Lambda boundary formula but the completed diagnostic found no explicit in-source definition. The successful finite low-spin numerical panel therefore cannot establish source-faithful convention authority by itself.

This gate tests provenance only. It must not choose, fit, infer, or retune a convention from numerical agreement.

## Authoritative source set
Primary target: Buffenoir–Roche, *Tensor Products of Principal Unitary Representations of Quantum Lorentz Group and Askey-Wilson Polynomials*, arXiv `math/9910147v1`.

Prior same-author source to audit: Buffenoir–Roche, *Harmonic Analysis on the quantum Lorentz group*, arXiv `q-alg/9710022` / published CMP 207 (1999) 499–555. The downloaded source hash must be recorded before parsing; fetch/hash failure is infrastructure failure.

No secondary textbook/Wikipedia convention can authorize this gate.

## Frozen independent lanes
1. `import-chain`: inspect the complete `math/9910147v1` source for explicit statements that notation/conventions/results are imported from or defined as in the prior Buffenoir–Roche harmonic-analysis paper. Record all references/nearby context. Mere bibliography presence is insufficient.
2. `prior-explicit-definition`: inspect the complete prior primary source for an explicit equality/definition of the same q-binomial notation (or an unambiguous equivalent notation explicitly mapped to the bracket q-number/factorial primitives). Enumerate all candidates; no bounded hit cap.
3. `symbol-compatibility`: independently verify that any candidate definition uses the same q-number normalization relevant to the current source, including the symmetric bracket convention `[z]=(q^z-q^-z)/(q-q^-1)` or an explicitly algebraically identical normalization. This lane may reject incompatibility but may not infer missing provenance.

## Frozen classifier
- `SOURCE_AUTHORITY_CHAIN_ESTABLISHED`: only if (a) the prior primary source contains an explicit convention definition, (b) the current source contains an explicit import/reference statement sufficient to carry that convention into the notation used here, and (c) the q-number normalization is explicitly compatible.
- `BLOCKED_SOURCE_AUTHORITY_CHAIN_NOT_ESTABLISHED`: source retrieval succeeds but any of (a)–(c) is absent or ambiguous.
- `INFRASTRUCTURE_PRIMARY_SOURCE_AUDIT_FAIL`: fetch/archive/parser/hash failure prevents the frozen audit.

## Interpretation lock
A PASS authorizes only the q-binomial convention provenance needed to reclassify the already-completed finite low-spin boundary implementation as source-faithful at that scoped level. It does **not** authorize Eq.(29), general `formlamb6j`, amplitude/refinement bridge credit, candidate theory, or any fitted convention.

A BLOCKED result must remain BLOCKED. Do not replace it by numerical inference from the 8-lane panel.
