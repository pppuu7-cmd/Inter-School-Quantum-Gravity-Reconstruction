# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**. Bridge credit remains zero.

## Closed — ITER039 scientific FAIL

ITER039 remains terminal **SCIENTIFIC FAIL — `RC006_EQ27_BOUNDED_CENTRAL_COMPONENT_CLOSURE_FAIL`**. Frozen run `34806079470` evaluated all 54 primary and 96 held-out central tuples without retuning; 7 primary and 23 held-out tuples failed. No threshold/domain/convention has been changed. Durable result commit `73bc362dce539c918c1a3b9344739c1d67316dd3`.

## Closed — ITER040 diagnostic complete

ITER040 is terminal **`RC006_CENTRAL_COMPONENT_VALIDITY_BOUNDARY_DIAGNOSTIC_COMPLETE`**. Prereg `7fe47cd180c9e2869d8aaaf445ad676a1bb53396`; implementation `4a69b1ae7e8c7685bac88e2145e04ef5ce6a4d54`; first run `34806258751` was INFRASTRUCTURE FAIL PRE-SCIENCE with no jobs; YAML-only repair `cf9bf1c442c6059ab2244e892ef563800b2499b5`; authoritative run `34806282247`; jobs C `103858683855`, D `103858683992`, B `103858683995`, A `103858684049`, aggregate `103858835458`; aggregate artifact `10333440520`, digest `sha256:1e81dc44316e0f7d735eaa95ef4a2ece4cf06f920b24c88260f95423965f0bb1`; result commit `d3e5a2752fa07ec5cc5beb97db96dc159f7b700f`.

The exact prior ITER027 ordered-pair scope passes **24/24** (12 primary + 12 held-out). All root-boundary tuples (`a+b>k`) are outside that prior scope and fail in ITER039: primary 3/3 and held-out 15/15, with large R/R^-1 residuals. However root boundary is not a complete explanation: outside prior scope but with `a+b<=k`, 4/39 primary and 8/69 held-out tuples still fail through the dual-contraction residual, up to `0.7137917357844189`, while their R/R^-1 residuals stay tiny. Therefore at least two source/domain questions remain; no post-hoc pruning is allowed.

## Active — ITER041 source-domain authority audit

ITER041 is a prospectively frozen **source-only** audit. It asks separately whether the exact ITER025-pinned sources state (1) the correct root-of-unity categorical/truncated/quotient domain for R/R^-1 when the naive tensor product crosses the finite cutoff, and (2) the exact domain/trace/duality qualification of the cap/cup dual-contraction identity used earlier.

Frozen source versions remain `1609.02429v2`, `1312.0905v2`, `1311.1798v1`; no later source may retroactively alter this gate.

- prereg commit `4884e9b784506db0c428decc808eaac2ffdb9831`
- implementation commit `a02700b58dafcc92e6b5d3fea3039dc3ae312020`
- production/workflow head `5464d07efb957dbc5476fd99baa2c4baae1b465b`
- authoritative run `34806469113`
- jobs: C dual-domain `103859206862`; D controls `103859206973`; A provenance `103859206982`; B R-domain `103859207036`.

Latest snapshot: **2 in_progress / 2 queued**, avoidable idle false.

## Exact next action

Consume all ITER041 raw source artifacts and classify against the frozen strict authority predicates. If both R-domain and dual-domain source authority are decisive, only a new separately preregistered numerical formulation may be considered. If either is not decisive, ITER041 is `SCOPED BLOCKED` and only prospective source expansion is admissible. **ITER039 remains scientific FAIL in either case.**

## Persistent locks / other fronts

Eq.(29)/Lambda, one-step TNR, full Eq.(27) amplitude, refinement bridge and candidate-theory construction remain unauthorized. ITER028 and ITER036 remain historically BLOCKED; ITER034 remains BLOCKED with its over-permissive green run rejected. BH004/BH004B remains scoped-negative; genuine multivertex Lorentzian EPRL refinement remains source-blocked; RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope.

Still false: `full_eq27_amplitude_derived`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `BRIDGE_DERIVED`.
