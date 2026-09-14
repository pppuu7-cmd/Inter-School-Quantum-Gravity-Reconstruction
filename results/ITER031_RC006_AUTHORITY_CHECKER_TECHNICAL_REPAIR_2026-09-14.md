# ITER031 authority-domain technical repair

Date: 2026-09-14

## Authoritative pre-repair run

Run: `34801212245`
Head: `523405f835757101659a259d2a50b7c452c7d084`
Jobs: null-controls `103844104789`; bounded-contraction `103844104851`; authority-domain `103844104861`; component-translation `103844104877`; aggregate `103844146488`.
Artifacts: authority-domain `10330808909` (`sha256:23404a51c578544dd81277c43a6dd5c2d8bd96456a4ec2d07ff8bb091a4e072c`); null-controls `10330948282` (`sha256:0e507123417fa2b1e5b04e0e6fed4e6b5ed08823350413a01b229515b72992d7`); aggregate `10331237247` (`sha256:2d8202cbd3d7bc39c6bf057f8f8141aa85c8937e02d528a99584732e7a32ef20`); bounded-contraction `10331373020` (`sha256:614c46239c02a7203422a9d32a2466a872743ef84a2f0de9629694a7b143e220`); component-translation `10331727071` (`sha256:9c3275c2a144b78e2256fac0704652846e42fa44397f139a403e08a1cff92614`).

## Classification

The aggregate emitted `RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_CORRECTED_STAGE_S_FAIL` only because lane A returned `pass=false`. Raw lane inspection shows this is **not a scientific failure**.

The inherited ITER027 `authority_domain()` implementation searched the raw source text of `code/iter027/eq27_bounded_component_contraction.py` for the forbidden tokens `formLambda6j`, `eq29_amplitude`, and `lambda_qbinomial`. Those tokens occur as string literals inside the checker itself, so the checker necessarily reported all three as forbidden dependencies even though there is no executable dependency on them. Required authoritative files were present and all primary/held-out admissible panels were non-empty.

Lanes B-D were substantively evaluated under frozen science and passed: component translation max qbar-intertwiner residual `3.839616566770844e-15` with max source-identity residual `0.0`; bounded contraction max dual residual `8.671119018262734e-16` and max R-inverse residual `7.247022734347215e-15`, both far below the frozen `5e-8` threshold; null controls detected 2/3 required wrong constructions. No held-out retuning occurred.

Therefore run `34801212245` is classified **NUMERICAL/INFRASTRUCTURE FAIL PRE-SCIENCE — AUTHORITY CHECKER FALSE POSITIVE**, with useful B-D diagnostics preserved. It is not a scientific PASS or FAIL for ITER031.

## Minimal repair

Repair commit `408405dca93bf4a8390bd33c49617e15b0b4634b` changes only the authority dependency detector from raw substring matching to AST executable-name/import matching. Frozen prerequisites, panels, alpha, conventions, thresholds, numerical kernels and null controls are unchanged.

Workflow-trigger commit `40616a4bf6cffc3138cda0587dbe63bc381dbd20` starts authoritative recovery run `34804179870` with the same four frozen lanes and `fail-fast:false`.

No claim lock is relaxed. Eq.(29)/Lambda, one-step TNR, bridge credit and candidate-theory construction remain unauthorized. Candidate theory remains `UNFORMED / 0%` and programme readiness remains 49% pending terminal recovery classification.
