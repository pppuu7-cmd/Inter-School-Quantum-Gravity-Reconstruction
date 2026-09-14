# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**; this is not a correctness probability.

## ITER028 terminal result

ITER028 Stage S is terminal:

**`BLOCKED — RC006_EQ27_SOURCE_GRAPH_COMPONENT_MAP_BLOCKED`**.

Prereg commit `73246639c6710ab3e7228c3e5f0f11ae654f32b7`; implementation `a56829c6beeee273d410c5dc87a7234aa76daef4`; production head `3661564138585ad990761371e8a2d1e980719433`; authoritative run/job `34794113275 / 103823792085`; artifact `10329326228`, digest `sha256:9d077dfe52a76033c6061de872e6068cdea1980f55ceda0bf8e25c976d4f7c03`.

Fresh source provenance passed exactly: archive SHA256 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`; exact Eq.(27) display SHA256 `88d2f7be9489980a763dd66b5c4900473c79900ccf72790095ae1675e9733b2d`.

The blocker is semantic/inventory-level: the exact Eq.(27) display has two `tikzpicture` environments and two internal sums, whereas ITER028 had frozen “four TikZ graphical blocks / source graphical factors”. That predicate cannot be changed after observing the terminal source extraction. Therefore lanes A–F were not authorized and ITER028 remains BLOCKED. Durable report: `results/ITER028_RC006_EQ27_STAGE_S_SOURCE_GRAPH_MAP_BLOCKED_2026-09-14.md`, commit `c9b783f9dedef67011bb3f54b45159d92f99a6e0`.

## ITER029 prospectively frozen and running

The next admissible gate has been prospectively preregistered as `ITER029_RC006_EQ27_SOURCE_SEMANTICS_RECONCILIATION` before its implementation/result.

Prereg commit: `fd3db7bc95a17dd3265e0ec7431a452df0503935`.

Implementation commit: `ab42e0adf64ef47878c8f410542c8e4d7769583c`.

Production/workflow head: `fab8522ca1e0b5ac36bff8255e04252f295b91c9`.

Authoritative run/job: `34794237347 / 103824140071` — currently queued.

Frozen hypothesis: the historical “four” count came from the exact ITER021 wording “two draw paths, four TikZ begin/end tokens” (two begin + two end tokens), while Eq.(27) itself contains two bracketed TikZ graphical factors / two environments. ITER029 audits source-token census, historical wording, structural two-factor decomposition and false-interpretation null controls. It performs no q-CG/R/qbar/amplitude contraction and cannot retrofit ITER028.

If all frozen lanes PASS, the maximum result is `RC006_EQ27_SOURCE_SEMANTICS_RECONCILED_SCOPED`, which only authorizes consideration of a fresh prospectively preregistered corrected Stage-S successor. If ambiguity remains, classification is BLOCKED; if exact source and durable records unambiguously contradict the hypothesis, classification is FAIL.

## Workload and next action

Scientifically useful jobs: **1 queued / 0 in_progress**. No competing Eq.(27) calculation is admissible until this dependent reconciliation gate terminalizes.

Exact next action: consume the raw ITER029 artifact and classify it against the frozen preregistration. Only a terminal PASS may open a new corrected topology compiler gate.

## Other fronts / locks

BH004/BH004B remains scoped-negative; genuine multivertex Lorentzian EPRL refinement remains source-blocked; RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope.

Still false: `iter012_retry_authorized`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `preferred_alpha_found`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.
