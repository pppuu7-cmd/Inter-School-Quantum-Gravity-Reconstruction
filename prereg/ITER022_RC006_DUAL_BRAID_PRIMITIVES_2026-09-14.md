# ITER022 preregistration — RC006 cup/qbar-dual + R/braiding primitive qualification

Date: 2026-09-14

## Authorization basis

ITER021 terminal classification: `RC006_EQ27_COMPONENT_TRANSLATION_BLOCKED_MISSING_PRIMITIVE`.

The two unresolved implementation-level primitives are frozen as the only targets of this gate: (i) cup/qbar-dual translation and (ii) R/braiding in the Appendix-F derivation path. No Eq.(27) numerical amplitude is evaluated here.

## Frozen sources

Primary target source: arXiv:1609.02429v2, pinned e-print SHA256 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

Previously pinned supporting source candidates from the same research chain may be audited only for explicit formula authority; an absent formula is BLOCKED, not permission to import an external convention.

## Lane A — cap/cup executable identity

Implement exactly the source formulas

- cap: `(-1)^(j-m) q^(m/2) delta_(m,-m')`
- cup: `(-1)^(j+m) q^(m/2) delta_(m,-m')`

with the target root-of-unity q convention. Test concatenation to identity prospectively at `k={6,10,12}` and twice-spins `{1,2,3,4,5}` where admissible.

PASS: maximum entrywise identity residual `<1e-12`, no fitted phase/sign.

## Lane B — qbar-dual graphical translation

Recover the source statement that qbar-CG is obtained from target-q CG by cups/caps. Build the corresponding component translation from the validated q-CG embeddings and the Lane-A cup/cap matrices. Test involutive round-trip on a frozen channel panel `k={6,10,12}`, channels `(1,1)->0,2`, `(1,2)->1,3`, `(2,2)->0,2,4` where admissible.

PASS: source relation uniquely recovered; round-trip projector/embedding residual `<2e-9`; no channel-wise phase fit. If the graphical-to-index ordering is not uniquely recoverable, classify BLOCKED rather than choose one.

## Lane C — Appendix-F R/braiding necessity and authority

Mechanically recover Appendix-F context around identities B15/F1 and all lexical variants of R-matrix/braiding (`R matrix`, `R-matrix`, `R--matrix`, `R matrices`, `R--matrices`, `braid`). Determine whether the Eq.(27) derivation requires an explicit R action after all source-stated cancellations.

If explicit R survives, PASS requires a source-explicit executable formula or a source-proven reduction to already qualified primitives. If the source delegates the required R convention/formula elsewhere, this lane is `BLOCKED_EXTERNAL_R_AUTHORITY`.

## Lane D — adversarial dual/braid controls

Frozen wrong controls:

1. replace cup exponent `q^(m/2)` by `q^(-m/2)`;
2. replace cup sign exponent `j+m` by `j-m`;
3. treat qbar-dual as ordinary Hermitian conjugation without cups/caps.

PASS only if the correct cap/cup identity remains `<1e-12` and at least two wrong controls exceed `1e-6` on the fixed panel or violate the exact source graphical identity.

## Aggregate classes

- `RC006_DUAL_BRAID_PRIMITIVES_QUALIFIED`
- `RC006_DUAL_BRAID_BLOCKED_EXTERNAL_R_AUTHORITY`
- `RC006_QBAR_DUAL_TRANSLATION_BLOCKED`
- `RC006_DUAL_BRAID_NULL_CALIBRATION_FAIL`
- `RC006_DUAL_BRAID_INFRASTRUCTURE_PARTIAL`

Only full qualification may authorize a separately preregistered bounded Eq.(27) component contraction.

## Claim locks

Always false during ITER022: `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `eq29_amplitude_authorized`, `preferred_alpha_found`, `iter012_retry_authorized`.