# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**; this is not a correctness probability. Bridge credit remains zero.

## ITER031 terminal result

ITER031 is terminal **SCIENTIFIC PASS — `RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_CORRECTED_STAGE_S_PASS`**.

Frozen preregistration: `38333cb3e5a912eb7e6be8b6e997dcb94d366279`. Original implementation: `045a25241b37912199794385e6b4cd89b1f37b4f`. The initial missing-numpy/missing-mpmath runs were infrastructure-only. Run `34801212245` was also retained as infrastructure/pre-science because the inherited authority checker matched its own forbidden-token string literals; repair commit `408405dca93bf4a8390bd33c49617e15b0b4634b` changed only that detector to executable AST-reference checking, with no science/threshold/model change.

Authoritative production head: `40616a4bf6cffc3138cda0587dbe63bc381dbd20`. Authoritative run: **34804179870**.

Jobs/artifacts:
- null-controls `103852648035` -> artifact `10332057066`, digest `sha256:fd5f57f2c98e6208793fc0dde09de83e402c15812a4460f5b9811968e8e2a78e`;
- authority-domain `103852648280` -> `10332691210`, `sha256:1ead0892d8cbf2ef154061b138e2b7f9c350ea92948050f03ae35bab917f3586`;
- bounded-contraction `103852648328` -> `10332132992`, `sha256:3adffa9cfdf1b8248d51ffa3b7d9a3685cf49b1379f8afa59a377d1896121c5d`;
- component-translation `103852648330` -> `10332866622`, `sha256:8ee94e7a6962501e8eb4010a71b50683add8e14091a66e5e6332026b0f8fed33`;
- aggregate `103852685845` -> `10332821665`, `sha256:d690afd7ac1f3cd09c6c88df8361df1d24455b26f1e66f6d4ea5230c41366ccb`.

The aggregate returned `scientific_pass=true`, `failed_lanes=[]`, `infrastructure_lanes=[]` and preserved claim locks. The numerical maxima were: source-qbar identity `0.0`; qbar-intertwiner `3.6860685022878984e-15`; dual contraction `5.551115123125783e-16`; R-inverse `7.27366312472434e-15`. These are below the frozen thresholds without held-out retuning. Null controls detected the preregistered required 2/3 wrong constructions.

Result note commit: `3b2f8274647831965a3e06f13fb40072cef08e38`.

## Exact authorization

ITER031 authorizes only a **new, separately preregistered two-factor Eq.(27) network-assembly gate** under the immutable corrected Stage-S dictionary and validated bounded primitives. It does not authorize Eq.(29)/Lambda, one-step TNR, full amplitude/TNR reconstruction, bridge credit, or candidate-theory construction.

Primary levels remain `k={6,10,12}`; held-out levels remain `k={7,9,11}`; `alpha=0`; no phase/sign/permutation/R/qbar orientation/normalization or held-out parameter may be fitted.

## Workload and exact next action

At this terminal snapshot: **0 queued / 0 in_progress**, avoidable idle is true only because the newly authorized successor must first be prospectively preregistered. Exact next action: preregister and launch a bounded two-factor network-assembly gate with source/topology authority, primary+held-out transport and frozen adversarial nulls. It must remain below Eq.(29)/Lambda and one-step TNR.

## Other fronts / locks

ITER028 remains terminal BLOCKED and is not retrofitted. BH004/BH004B remains scoped-negative; genuine multivertex Lorentzian EPRL refinement remains source-blocked; RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope.

Still false: `iter012_retry_authorized`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `preferred_alpha_found`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.
