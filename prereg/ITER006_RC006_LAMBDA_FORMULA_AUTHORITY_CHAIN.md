# Preregistration — ITER006 RC006 Lambda formula authority chain

Frozen before implementation/production on 2026-09-13.

## Scientific objective
Determine, without inventing a surrogate coefficient, whether the primary-source chain contains an explicit and executable definition of the quantum-Lorentz principal-series coefficient `Lambda^{JM}_{NL}(alpha)` sufficient to support a later finite low-spin numerical reconstruction of the Proposition 3.4 braiding law.

This is a source-authority/executability gate, not an amplitude gate.

## Frozen source chain
Four independent primary-source lanes:
1. Fairbairn–Meusburger, arXiv:1112.2511v1.
2. Fairbairn–Meusburger, arXiv:1012.4784v3.
3. Buffenoir–Roche, arXiv:q-alg/9710022v2 (`Harmonic Analysis on the quantum Lorentz group`).
4. Buffenoir–Roche, arXiv:math/9910147v1 (`Tensor Products of Principal Unitary Representations of Quantum Lorentz Group and Askey-Wilson Polynomials`).

The workflow must record the exact downloaded SHA256 for every source artifact used. Source retrieval or archive-format failure is infrastructure failure, not scientific evidence.

## Frozen questions per lane
Each lane must report, with exact textual/equation anchors where available:
- whether `Lambda`/the corresponding principal-series coefficient is explicitly present;
- whether the source only refers elsewhere for the coefficient formula;
- whether an explicit analytic-continuation / q-6j / Askey-Wilson expression is present rather than merely asserted;
- whether normalization/convention information required for numerical evaluation is present in the same source or referenced;
- whether the representation/domain labels needed to map to `Lambda^{JM}_{NL}(alpha)` are identifiable.

No coefficient values are to be fitted or inferred from downstream EPRL amplitudes.

## Frozen cross-source interpretation
- `QEPRL_LAMBDA_AUTHORITY_CHAIN_EXECUTABLE`: both EPRL sources map the same `Lambda^{JM}_{NL}(alpha)` object into the Buffenoir–Roche authority chain, and at least one Buffenoir–Roche lane exposes an explicit coefficient definition plus sufficient normalization/domain conventions to define a finite low-spin implementation without free fitted choices.
- `QEPRL_LAMBDA_AUTHORITY_CHAIN_PARTIAL`: the authority mapping is source-backed but the retrieved primary material does not yet expose all formula/normalization/domain ingredients needed for an unambiguous numerical implementation.
- `QEPRL_LAMBDA_AUTHORITY_CHAIN_UNSUPPORTED`: the required source mapping itself fails.
- Any fetch/archive/parser failure is `INFRASTRUCTURE_SOURCE_EXTRACTION_FAIL` and cannot be promoted to a scientific negative result.

## Controls and claim locks
- Positive controls: the known EPRL action formula and Proposition 3.4/braiding occurrence of `Lambda` must be located in the two EPRL lanes.
- Negative control: generic occurrences of the word/symbol `Lambda` unrelated to the principal-series coefficient do not count as an explicit coefficient definition.
- Historical pair-sign/braid projection is not an input.
- No post-result change of source versions, formula requirements or interpretation labels.
- Even `EXECUTABLE` authorizes only a separate prospectively preregistered finite low-spin coefficient implementation. It does not authorize Eq.(29), bridge credit, `BRIDGE_DERIVED`, candidate theory, `NEW_PHYSICS_FOUND`, or any RQIR/KMQGB promotion.
