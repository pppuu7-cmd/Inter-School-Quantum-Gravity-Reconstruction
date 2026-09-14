# ITER031 result — RC006 bounded Eq.(27) component contraction under corrected Stage-S

Date: 2026-09-14

Scientific classification: **PASS — `RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_CORRECTED_STAGE_S_PASS`**.

This is a bounded component-level PASS only. It authorizes one separately preregistered two-factor network-assembly successor. It does **not** authorize Eq.(29)/Lambda, one-step TNR, a full Eq.(27) amplitude claim, bridge credit, candidate theory, or new-physics claims.

## Frozen provenance

- preregistration commit: `38333cb3e5a912eb7e6be8b6e997dcb94d366279`
- implementation commit: `045a25241b37912199794385e6b4cd89b1f37b4f`
- dependency-only repairs: `38610cb655314328f74be0a9383ff9125abbf9fd`, `523405f835757101659a259d2a50b7c452c7d084`
- authority-checker technical repair: `408405dca93bf4a8390bd33c49617e15b0b4634b`
- recovery workflow trigger / authoritative production head: `40616a4bf6cffc3138cda0587dbe63bc381dbd20`
- authoritative run: `34804179870`

Jobs and validated artifacts:
- null-controls job `103852648035`; artifact `10332057066`; digest `sha256:fd5f57f2c98e6208793fc0dde09de83e402c15812a4460f5b9811968e8e2a78e`
- authority-domain job `103852648280`; artifact `10332691210`; digest `sha256:1ead0892d8cbf2ef154061b138e2b7f9c350ea92948050f03ae35bab917f3586`
- bounded-contraction job `103852648328`; artifact `10332132992`; digest `sha256:3adffa9cfdf1b8248d51ffa3b7d9a3685cf49b1379f8afa59a377d1896121c5d`
- component-translation job `103852648330`; artifact `10332866622`; digest `sha256:8ee94e7a6962501e8eb4010a71b50683add8e14091a66e5e6332026b0f8fed33`
- aggregate job `103852685845`; artifact `10332821665`; digest `sha256:d690afd7ac1f3cd09c6c88df8361df1d24455b26f1e66f6d4ea5230c41366ccb`

The earlier run `34801212245` is retained as `NUMERICAL/INFRASTRUCTURE FAIL PRE-SCIENCE — AUTHORITY CHECKER FALSE POSITIVE`, not as a scientific FAIL. Its lane-A raw-source substring checker matched its own forbidden-token string literals. The repair changed only that technical detector to AST executable-reference checking; frozen science was not changed.

## Scientific readout

All four frozen lanes PASS in the authoritative recovery run.

- Authority/domain: all required sources/results are present, all primary and held-out panels are non-empty, `alpha=0`, and executable forbidden dependencies are absent (`forbidden_dependencies=[]`).
- Component translation: max source-qbar identity residual `0.0`; max qbar-intertwiner residual `3.6860685022878984e-15`, versus frozen thresholds `2e-12` and `5e-9` respectively.
- Bounded contraction: max dual-contraction residual `5.551115123125783e-16`; max R-inverse residual `7.27366312472434e-15`, versus frozen `5e-8`; all values finite; held-out panel was not retuned.
- Frozen nulls: 2/3 required wrong constructions were detected. `legacy_inverse_parameter_qbar=1.6579164156537258`, `R_inverse_swap=0.621444172414215`, while the frozen wrong-magnetic-order construction happened to yield `0.0`; preregistration required at least 2/3, so the gate passes without changing the rule.

Primary levels remained `k={6,10,12}`; held-out levels remained `k={7,9,11}`; `alpha=0` throughout.

## Exact authorization and locks

The preregistered PASS class authorizes only a **new, separately preregistered two-factor network-assembly gate** using the immutable source dictionary and already validated bounded primitives. It does not authorize a full amplitude/TNR reconstruction.

Still false: `iter012_retry_authorized`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `preferred_alpha_found`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.

Candidate theory remains `UNFORMED / 0%`. Overall programme roadmap readiness remains 49% until a roadmap rubric/gate beyond this bounded layer is actually closed.
