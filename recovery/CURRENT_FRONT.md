# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**; this is not a correctness probability. Bridge credit remains zero.

## ITER031 terminal result

ITER031 is terminal **SCIENTIFIC PASS — `RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_CORRECTED_STAGE_S_PASS`**.

Authoritative production head: `40616a4bf6cffc3138cda0587dbe63bc381dbd20`; run `34804179870`; aggregate job `103852685845`; aggregate artifact `10332821665`; digest `sha256:d690afd7ac1f3cd09c6c88df8361df1d24455b26f1e66f6d4ea5230c41366ccb`; result-note commit `3b2f8274647831965a3e06f13fb40072cef08e38`.

All four frozen lanes pass without held-out retuning. Max source-qbar identity residual `0.0`; qbar-intertwiner `3.6860685022878984e-15`; dual contraction `5.551115123125783e-16`; R-inverse `7.27366312472434e-15`. Null controls satisfy the prospectively frozen 2/3 criterion.

Run `34801212245` remains separately classified as `NUMERICAL/INFRASTRUCTURE FAIL PRE-SCIENCE — AUTHORITY CHECKER FALSE POSITIVE`; no result or threshold was altered to turn it into a PASS.

## ITER032 prospectively frozen and active

Successor: **`ITER032_RC006_EQ27_TWO_FACTOR_NETWORK_ASSEMBLY`**.

- preregistration commit: `bda9c7c12a2f2e4886d4734b9d1835119a700491`
- implementation commit: `a369586e5d05b04e757f36468e58aaba00cb1253`
- production/workflow head: `5f624a8a9f08a1aa75b3031e954cba2e66bcd859`
- authoritative run: **34804399944**

The gate is deliberately bounded and factorized: before numerical composition, Lane A must mechanically confirm the byte-pinned Eq.(27) source contains two distinct bracketed multiplicative graph factors with separate sums. The numerical lanes then use only the already validated ITER031 bounded primitive, deterministic adjacent-row pairing, primary `k={6,10,12}`, held-out `k={7,9,11}`, `alpha=0`, and the unchanged `5e-8` bounded threshold. It is explicitly not a full Eq.(27) amplitude/TNR claim.

Four independent lanes were launched with `fail-fast:false`:
- source-factorization authority job `103853284855`;
- independent factor reconstruction job `103853284954`;
- two-factor bounded assembly job `103853284982`;
- frozen adversarial nulls job `103853285020`.

At the launch snapshot these were **4 queued / 0 in_progress**, so avoidable idle is false. No duplicate batch is admissible.

## Exact next action

Consume all raw ITER032 lane artifacts and the dependent aggregate against the frozen preregistration. Source-factorization ambiguity is BLOCKED, not scientific FAIL. A numerical threshold breach after valid authority is SCIENTIFIC FAIL and may not be repaired by retuning. Only a frozen ITER032 PASS may authorize a new separately preregistered gate toward the remaining source summation/scalar structure; Eq.(29)/Lambda and one-step TNR remain forbidden.

## Other fronts / locks

ITER028 remains terminal BLOCKED and is not retrofitted. BH004/BH004B remains scoped-negative; genuine multivertex Lorentzian EPRL refinement remains source-blocked; RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope.

Still false: `iter012_retry_authorized`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `preferred_alpha_found`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`, `full_eq27_amplitude_derived`.
