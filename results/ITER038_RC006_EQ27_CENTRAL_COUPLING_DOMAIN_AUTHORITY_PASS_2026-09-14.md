# ITER038 — RC006 Eq.(27) central coupling/domain authority

Date: 2026-09-14

## Terminal classification

**SCIENTIFIC PASS — `RC006_EQ27_CENTRAL_COUPLING_DOMAIN_AUTHORITY_PASS`**.

This result uses the prospectively frozen ITER038 preregistration without changing any scientific predicate, threshold, model, convention, or admissibility condition after observing the result.

## Frozen provenance

- preregistration commit: `3cdcc41939aac89c4bd934c10fbd7bc48a8dd321`
- implementation commit: `6340ead5bd78bdc650261c4827298943eab1b7a5`
- original production head: `b68d479615b9f966c2628ba8c69c1a2336d5c1dc`
- original authoritative run: `34805710939`
- original jobs:
  - A topology authority: `103857072596`
  - B finite-k domain authority: `103857072719`
  - C central-domain enumeration: `103857072746`
  - D null controls: `103857072479`
  - aggregate: `103857203026`
- original artifacts:
  - A: `10333220417`, `sha256:f504c8f1151ece4a8ce8c4cdba5416c063e64fc467e3404e0c28cdc1bedd4ac1`
  - B: `10332828921`, `sha256:7986da96d18272d78113c40b99386ee1a5ba64c554902069b89c6fed81d403ea`
  - C: `10333295010`, `sha256:02e5248a2349421631f1e7d590c785e589b750dc1df7db0d70e1e79a936a546a`
  - D: `10332609457`, `sha256:1e5d655bb6d545cf4d682db9c2941109a5643a7d156d47403b573bca4cf54952`
  - aggregate: `10333122987`, `sha256:92f719ef482e7eac781246848bafc1b99efa5a41dea9dfb979e972f0d73b9d64`

## Technical recovery of lane B

The original aggregate classified lane B as `BLOCKED_FINITE_K_DOMAIN_AUTHORITY`. Raw lane-B context, however, already contained the exact frozen source conditions, including the root-of-unity sum condition written in TeX `eqnarray` form as `j_1+j_2+j_3 &\\leq& k`, the triangle condition `j_I+j_K &\\geq& j_L`, the phrase `admissible representations`, and the finite cutoff `j_max=k/2`.

The original parser looked for the mathematical relation without allowing TeX alignment ampersands. This is a parser/wiring defect, not a scientific/source ambiguity. The minimal parser-only repair is commit `e1eb8a3b6fb8db1bef1caa9262d853bfee9bd387`; no frozen scientific predicate was weakened or changed.

A B-only recovery was used so terminal A/C/D computations were not duplicated:

- recovery workflow head: `67a27d01c20a05b99ed7ce7c4bcbfba39c91ccc4`
- recovery run: `34805845056`
- recovery job: `103857457176`
- recovery artifact: `10333225494`
- recovery digest: `sha256:af9dde495a26791a59f32f17cb2629ac740b0a8a92cfad9242b398c7407f04b6`
- recovered lane-B classification: `PASS`

A second small B-only trigger (`34805852414`) was accidentally created while the first delayed run had not yet appeared; it is not needed for scientific authority and is not used to increase evidence or confidence.

## Frozen gate results

- **A PASS**: source topology explicitly supports indexed `j_i^+ -> J^+`, indexed `j_i^- -> J^-`, followed by central `J^+,J^- -> l`; no Eq.(29)/Lambda inference is used.
- **B PASS after parser-only recovery**: source authority explicitly supplies finite SU(2)_k cutoff/admissibility and root-of-unity coupling-domain conditions required by the preregistration.
- **C PASS**: central `(J^+,J^-,l)` domains are finite and non-empty on both primary and held-out diagonal panels under the frozen admissibility rules.
- **D PASS**: all 3/3 frozen invalid-domain controls are rejected.

Therefore all preregistered ITER038 lanes pass scientifically. The original aggregate's B blocker is superseded only as a technical parser result; it is retained as provenance and is not retroactively rewritten.

## Scope / claim locks

This PASS authorizes only a separately preregistered **bounded central/intermediate-index Eq.(27) contraction gate** on the already frozen source-supported label panel. It does **not** derive the full Eq.(27) amplitude, Eq.(29), Lambda, one-step TNR, a refinement bridge, or a candidate QG theory.

Still false: `full_eq27_amplitude_derived`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `BRIDGE_DERIVED`.

Programme readiness remains **49%**. Candidate theory remains **0% / UNFORMED**.
