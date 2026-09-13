# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**; this is not a correctness probability.

## Reconciled lineage through ITER026

The historical ITER024/025 label collision is resolved by logical A/B aliases in `results/ITER024_025_AB_PROVENANCE_RECONCILIATION_2026-09-14.md`; historical files and commits remain unchanged.

- ITER024A: graphical dual/braid execution, terminal `RC006_GRAPHICAL_QBAR_COMPONENT_FAIL`; R/braid controls PASS, qbar dual FAIL.
- ITER024B: cited-authority parser, terminal `INVALID_IMPLEMENTATION` despite green CI because its code did not implement the frozen cited-source audit.
- ITER025A: inverse-parameter/reversed-order source-normalized qbar construction, run `34786242013`, terminal `RC006_QBAR_CUP_INDEPENDENT_FAIL`; construction and 4-valent lanes PASS, cup and held-out lanes FAIL at high/root-boundary spins.
- ITER025B: exact source audit, run `34788769863`, terminal `RC006_EXACT_QBAR_R_SOURCE_AUTHORITY_COMPLETE`; exact source chain fixes ordered q<->qbar component identity and R/R^-1 crossing convention.

ITER025B source authority did not erase ITER025A executable failure. That conflict motivated the prospectively frozen ITER026 direct-source execution gate.

## ITER026 terminal PASS

Preregistration: `prereg/ITER026_RC006_DIRECT_SOURCE_QBAR_IDENTITY_EXECUTION_2026-09-14.md`, commit `17dd87a110645b2a7ca6cc22df52569758502a70`.

Implementation: `code/iter026/direct_source_qbar_identity.py`, commit `caf988b3313a9c7cf5f7c6b409e6eb3ef99f0215`.

The new primitive constructs qbar directly from the exact source identity

`{}_q C^{j1 j2 j3}_{m1 m2 m3} = (-1)^(j1+j2-j3) {}_{bar q} C^{j1 j2 j3}_{-m1,-m2,-m3}`

using magnetic-index reversal with no m1/m2 swap, and uses target B2 only to fix the prospectively allowed residual singlet `+-1` q-CG gauge. It does not solve qbar independently at inverse q and does not apply per-channel post-hoc repair.

A first orchestration attempt, run `34789842824`, is terminal `INVALID_IMPLEMENTATION_PRE_SCIENCE`: unquoted YAML `null` prevented the five-lane matrix contract from being instantiated. No scientific outputs from that run were inspected or used. Only the YAML literal was repaired; the scientific contract was unchanged.

Authoritative corrected run: `34789873827`, production head `d6a457f364feefd3fd4523ab84e09f8803590f3c`.

Terminal classification:

**`PASS — RC006_DIRECT_SOURCE_QBAR_PRIMITIVE_VALIDATED`**.

All five prospectively frozen lanes PASS:

- `domain`: all exact source hashes/locators present; 55/55 cup cases retained across k=6,7,9,10,11,12; all eight ITER025A counterexamples retained; source-domain/root-boundary audit PASS.
- `algebra`: max source-identity residual `0.0`; max qbar intertwiner residual `1.5594956288365066e-12` vs `5e-9`; max B2 residual `2.3525204118543076e-15` vs `2e-9`; no inverse-parameter construction and no post-hoc channel repair.
- `cup`: 55/55 PASS; global max residual `2.3525204118543076e-15` vs `2e-9`.
- `four`: primary plus held-out k=7,9,11 PASS; global max residual `8.052062385546474e-13` vs `5e-8`.
- `null`: all 3/3 wrong structural controls detected with residuals `0.8342035043686545`, `1.4322826978446357`, `1.0111494534766454`.

Most importantly, all eight old high/root-boundary cup counterexamples now pass at approximately `1e-15`, while the frozen legacy ITER025A comparator in the same null lane continues to reproduce the old O(1) failures. Therefore the earlier failures are localized to the legacy inverse-parameter/reversed-order construction/gauge choice, not to an intrinsic breakdown of the audited source qbar duality over the tested root-of-unity simple-object range.

Durable report: `results/ITER026_RC006_DIRECT_SOURCE_QBAR_PRIMITIVE_2026-09-14.md`.

## New structural fact

For this RC-006 realization, the explicit q<->qbar source identity is not merely a phase convention. It acts as a representation/basis identification required for global consistency between q-CG, cap/cup duality, qbar intertwining and 4-valent graphical composition. Independently solving the qbar intertwiner at inverse q can satisfy internal equations while landing in a basis/gauge that is globally incompatible with the source graphical calculus.

This fact is scoped to the audited reduced Euclidean `SU(2)_k x SU(2)_k` realization. It is not yet bridge evidence.

## Authorization consequence

`eq27_component_reconstruction_prereg_allowed=true`.

The exact next admissible scientific gate is a **new separately preregistered bounded Eq.(27) component translation/contraction** using only:

- the validated q-CG solver;
- source-gauged cap/cup primitives;
- ITER026 source-direct qbar primitive;
- source-qualified R/R^-1 crossing convention;
- the already source-pinned Eq.(27) graph topology.

Before any contraction is evaluated, freeze exact tensor-leg ordering, internal channels, k/spin panel, normalization, R placements, positive controls, negative controls and PASS/FAIL/BLOCKED/INVALID criteria.

## Locks

Still false: `iter012_retry_authorized`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `preferred_alpha_found`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.

BH004/BH004B remains scoped-negative; genuine multivertex Lorentzian refinement remains source-blocked; RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope.
