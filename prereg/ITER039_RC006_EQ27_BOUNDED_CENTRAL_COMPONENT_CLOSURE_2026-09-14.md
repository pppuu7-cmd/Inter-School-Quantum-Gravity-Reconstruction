# Preregistration — ITER039 RC006 Eq.(27) bounded central component closure

Date frozen: 2026-09-14

## Prerequisite

ITER038 must be terminal `RC006_EQ27_CENTRAL_COUPLING_DOMAIN_AUTHORITY_PASS`. ITER039 may use only source-qualified objects already validated in ITER019/021/026/031/037/038. No Eq.(29), Lambda, one-step TNR, fitted phase, fitted normalization, domain repair, or post-result convention selection is admissible.

## Scientific question

For the exact finite central domains authorized by ITER038, can the source-qualified q-CG / qbar / dual and braid primitives be evaluated consistently for **every** allowed central coupling `(J+,J-,l)` on the frozen primary and held-out diagonal panels, without retuning?

This is a bounded central/intermediate-index **component-closure** gate. It is not a full Eq.(27) amplitude and does not sum or fit a new physical kernel.

## Frozen panel

Use the ITER037 diagonal external-label cases unchanged. `diag_panel == primary` defines the primary panel and `diag_panel == heldout` defines held-out transfer. For each case:

1. map its frozen external label through the exact indexed simplicity map already qualified in ITER037;
2. enumerate `J+` from the finite SU(2)_k admissible coupling of `(j+,j+)`;
3. enumerate `J-` from `(j-,j-)`;
4. enumerate every central `l` allowed by the ITER038 finite-k admissibility rules for `(J+,J-)`;
5. do not prune a valid tuple after seeing numerical values.

## Frozen lanes

### Lane A — panel/domain provenance

PASS iff all prerequisites exist, both primary and held-out panels are non-empty, every frozen case has a finite non-empty complete central-domain list, and no forbidden Eq.(29)/Lambda dependency is imported by executable code.

Missing/ambiguous authority is BLOCKED; dependency/runtime defects are INFRASTRUCTURE FAIL.

### Lane B — primary central component closure

For every primary `(k, external-label, J+, J-, l)` tuple, evaluate the already source-qualified q-CG and direct-source qbar objects and the validated dual contraction. Frozen numerical predicates:

- source-qbar identity residual `< 2e-12`;
- qbar intertwiner residual `< 5e-9`;
- dual contraction residual `< 5e-8`;
- R/R^-1 residual `< 5e-8` wherever the already validated braid primitive is dimensionally applicable;
- all evaluated arrays/residuals finite.

PASS iff **every** primary tuple satisfies the applicable predicates. No tuple may be removed or retuned.

### Lane C — held-out non-retuned transfer

Apply the identical implementation, conventions and thresholds to every held-out tuple. PASS iff every held-out tuple satisfies the same applicable predicates. No held-out-specific phase, normalization, cutoff, tolerance or selector is allowed.

### Lane D — adversarial controls

Freeze three invalid constructions before production:

1. insert one central `l` immediately outside an allowed finite-k domain;
2. replace direct-source qbar by the legacy inverse-parameter qbar construction on a valid tuple;
3. replace R by R^-1 on a valid nontrivial braid tuple.

PASS iff all three controls are detected as invalid/different by the frozen domain/residual machinery (`3/3`). A control that is algebraically inapplicable must be replaced only before production, not after seeing gate results.

## Aggregate classification

- `RC006_EQ27_BOUNDED_CENTRAL_COMPONENT_CLOSURE_PASS` iff A/B/C/D all PASS and neither B nor C retunes anything.
- `SCIENTIFIC FAIL` iff source-qualified valid-domain objects execute but a frozen numerical predicate fails.
- `BLOCKED` iff required source/domain authority is absent or ambiguous.
- `NUMERICAL/INFRASTRUCTURE FAIL` iff execution/dependency/serialization prevents scientific evaluation.

Green CI alone is not scientific PASS.

## Authorization on PASS

A PASS may authorize a **separately preregistered bounded label-complete Eq.(27) network-assembly gate** using these already validated components. It does not authorize a full Eq.(27) amplitude claim, Eq.(29)/Lambda, one-step TNR, bridge credit, candidate action/Hamiltonian/field equations, or candidate-theory construction.

Programme readiness is not automatically increased by this gate. Candidate theory remains `0 / UNFORMED` unless a later constitution gate explicitly authorizes otherwise.
