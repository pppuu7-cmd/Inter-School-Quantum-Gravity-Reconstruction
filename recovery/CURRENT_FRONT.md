# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**; this is not a correctness probability. Bridge credit remains zero.

## ITER030 terminal result

ITER030 is terminal **SCIENTIFIC PASS — `RC006_EQ27_CORRECTED_STAGE_S_COMPONENT_MAP_PASS`**.

Frozen provenance: prereg `bec01d4995043e6aa02148ad78ae38c9e5975b8e`; implementation `34e2f0b832d46c0be67d6e57ae3bbd208cc26e95`; production `19ded19077db5dc84f4ec7ed7d8aaa78cc536e55`; run `34797567102`; aggregate job `103834119032`; aggregate artifact `10330087985`; digest `sha256:b23c40284ee7ddaf6046aa13b9687e405eea18dee40f2dceeb90759676a6f4f1`; result-note commit `cdf8cac16aac6cbe0302950ef1c79f286113b0c8`.

All four raw lanes were consumed against the preregistration. The aggregate returned `scientific_pass=true`, `claim_locks_preserved=true`, and `numerical_contraction_authorized=true`. This authorizes only a separately preregistered bounded component contraction; it does not authorize Eq.(29)/Lambda, one-step TNR or bridge/candidate claims.

## ITER031 prospectively frozen and active

Successor: `ITER031_RC006_EQ27_BOUNDED_CONTRACTION_CORRECTED_STAGE_S`.

Preregistration commit: `38333cb3e5a912eb7e6be8b6e997dcb94d366279`.
Implementation commit: `045a25241b37912199794385e6b4cd89b1f37b4f`.

Initial run `34801076904` stopped before science because `numpy` was absent. First repair commit `38610cb655314328f74be0a9383ff9125abbf9fd` installed numpy only; recovery run `34801143752` then stopped before science because frozen kernel also imports `mpmath`. Both are `NUMERICAL_OR_INFRASTRUCTURE_FAIL_PRE_SCIENCE`, not scientific FAIL; neither changed a model, threshold or convention.

Second dependency-only repair commit: `523405f835757101659a259d2a50b7c452c7d084`, installing exactly `numpy` and `mpmath`. Current authoritative run: **34801212245**.

Four independent scientifically useful lanes are in progress with `fail-fast:false`:
- null-controls `103844104789`;
- bounded-contraction `103844104851`;
- authority-domain `103844104861`;
- component-translation `103844104877`.

The frozen primary panel remains `k={6,10,12}` and held-out panel `k={7,9,11}`, with `alpha=0`. Numerical thresholds/null controls are unchanged from the preregistered kernel; no phase/sign/tensor permutation/R-orientation/qbar-orientation/normalization or held-out parameter may be retuned.

## Workload and exact next action

Scientifically useful workload at the latest check: **0 queued / 4 in_progress**. Avoidable idle is false and no duplicate batch is admissible.

Exact next action: consume all terminal raw ITER031 lane artifacts and the dependent aggregate from run `34801212245`. Only a frozen aggregate PASS may authorize a separately preregistered two-factor network-assembly successor. A substantive threshold breach is scientific FAIL and cannot be repaired by retuning; missing authority is BLOCKED; pre-science technical failure remains infrastructure only.

## Other fronts / locks

ITER028 remains terminal BLOCKED and is not retrofitted. BH004/BH004B remains scoped-negative; genuine multivertex Lorentzian EPRL refinement remains source-blocked; RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope.

Still false: `iter012_retry_authorized`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `preferred_alpha_found`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.
