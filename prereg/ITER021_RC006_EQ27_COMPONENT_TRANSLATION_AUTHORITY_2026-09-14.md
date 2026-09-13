# ITER021 preregistration — RC006 Eq.(27) executable component-translation authority

Date: 2026-09-14

## Authorization basis

ITER020 terminal classification: `RC006_QCG_HELDOUT_TRANSPORT_PASS`.

The validated solver is now robust enough that the next blocker is no longer generic q-CG construction. Before evaluating an Eq.(27) amplitude, this checkpoint asks whether the **exact target source graph and its Appendix-B/E/F normalization chain can be translated unambiguously into an executable component contraction** without inventing an orientation, dual, braiding, sign, normalization or phase convention.

This is deliberately an authority/translation gate. It does not claim a bridge and does not authorize Eq.(29)/Lambda.

## Frozen source

Primary target: Dittrich, Schnetter, Seth, Steinhaus, arXiv:1609.02429v2, exact e-print hash historically pinned as `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

The gate must recover from fresh source bytes the unique display immediately following the exact prose anchor for normalization/diagram derivations, labelled `eq:eprl-3-valent`, together with the Appendix-B dual/cap/cup material and Appendix-E/F derivation context. A byte mismatch or unavailable source is INFRASTRUCTURE/PROVENANCE BLOCKED, not a scientific negative.

## Lane A — exact source topology and edge-label inventory

Recover the exact Eq.(27) TeX environment and mechanically inventory, without graphical guesswork:

- unique `eq:eprl-3-valent` display;
- exactly two closed graphical factors / two l-loop occurrences in the recovered display;
- primed `(J^+)',(J^-)'` and unprimed `J^+,J^-` pairs;
- internal-j sums and every explicitly written scalar prefactor/symbol around the graphs;
- no unaccounted open magnetic leg in the displayed reduced amplitude.

PASS only if the display is unique and the inventory is deterministic from source text. The lane emits the exact source snippet hash.

## Lane B — executable primitive dictionary

Build a machine-readable dictionary linking every primitive required by the recovered source structure to an already qualified executable object:

- q-number and quantum dimension;
- admissibility/A7;
- q-CG embedding from ITER019/020 solver;
- coproduct/action;
- Appendix-B cap, cup and qbar-dual operation;
- bilinear A8/A9 contraction;
- R/braiding requirement if the recovered Eq.(27)/Appendix-F path actually uses it;
- any normalization scalar or sign appearing in the source derivation.

No primitive may be marked implemented merely by name similarity. PASS requires every required primitive to be either `EXECUTABLE_QUALIFIED` or, if its numerical use cancels algebraically before the intended bounded contraction, `SOURCE_PROVEN_CANCELLED` with an explicit source derivation anchor. Any remaining `MISSING` primitive makes the aggregate BLOCKED.

## Lane C — Appendix-E normalization closure

Recover the target statement/derivation for `T_EPRL o T_EPRL` through Eq.(E3) and audit the component translation obligations. Frozen predicates:

- source explicitly connects the closed graph evaluation to Appendix-B graphical identities;
- the recovered closure includes the source delta in the outer label and all explicit quantum-dimension/sign factors;
- the translation plan uses the bilinear categorical contraction and does not substitute a Hermitian absolute square;
- for the singlet/cap subchannel, the already validated solver reproduces the source B2 convention up to only the preregistered residual overall sign gauge.

This lane may PASS as an authority/translation closure without numerically evaluating the full Eq.(27) graph.

## Lane D — adversarial translation/null controls

On the recovered source inventory, deliberately generate three wrong translation manifests:

1. remove a required quantum-dimension factor;
2. replace qbar-dual/cap-cup pairing by ordinary Hermitian conjugation;
3. erase primed/unprimed distinction or one required orientation/braiding marker.

PASS only if the structural validator rejects at least 2/3 wrong manifests and accepts the unmodified manifest. This is false-positive calibration, not evidence for physics.

## Aggregate classes

Four lanes run independently with `fail-fast:false`. Green CI is not scientific PASS.

Terminal classes:

- `RC006_EQ27_COMPONENT_TRANSLATION_AUTHORITY_COMPLETE`
- `RC006_EQ27_COMPONENT_TRANSLATION_BLOCKED_MISSING_PRIMITIVE`
- `RC006_EQ27_SOURCE_TOPOLOGY_AMBIGUOUS`
- `RC006_EQ27_APPENDIXE_NORMALIZATION_TRANSLATION_FAIL`
- `RC006_EQ27_TRANSLATION_NULL_CALIBRATION_FAIL`
- `RC006_EQ27_TRANSLATION_INFRASTRUCTURE_PARTIAL`

Only `...AUTHORITY_COMPLETE` may authorize a separately preregistered bounded numerical Eq.(27) component contraction. It does not itself produce bridge credit.

## Locks

Always false during ITER021: `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `eq29_amplitude_authorized`, `preferred_alpha_found`, `iter012_retry_authorized`.