# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**. Bridge credit remains zero.

## Newly closed

ITER038 is terminal **SCIENTIFIC PASS — `RC006_EQ27_CENTRAL_COUPLING_DOMAIN_AUTHORITY_PASS`**.

Frozen provenance: prereg `3cdcc41939aac89c4bd934c10fbd7bc48a8dd321`; implementation `6340ead5bd78bdc650261c4827298943eab1b7a5`; production `b68d479615b9f966c2628ba8c69c1a2336d5c1dc`; original run `34805710939`; A `103857072596`, B-original `103857072719`, C `103857072746`, D `103857072479`, aggregate-original `103857203026`.

Raw A/C/D pass the frozen topology, central-domain enumeration and 3/3 null predicates. The original B artifact was marked BLOCKED only because its parser omitted TeX `eqnarray` alignment ampersands even though the raw context already contained the exact frozen source conditions `j_I+j_K >= j_L`, `j_1+j_2+j_3 <= k`, admissible representations and `j_max=k/2`. Minimal parser-only repair commit `e1eb8a3b6fb8db1bef1caa9262d853bfee9bd387` changed no science. B-only recovery run `34805845056`, job `103857457176`, artifact `10333225494`, digest `sha256:af9dde495a26791a59f32f17cb2629ac740b0a8a92cfad9242b398c7407f04b6` is PASS. Result note commit `f9391713820703a0a2619222bd38d7485cf84e4e`.

The original aggregate artifact remains preserved (`10333122987`, `sha256:92f719ef482e7eac781246848bafc1b99efa5a41dea9dfb979e972f0d73b9d64`) and is not rewritten; its B blocker is superseded only as a technical parser result.

## Exact next gate

ITER038 PASS authorizes a separately preregistered **bounded central/intermediate-index Eq.(27) contraction** on the already source-supported primary+held-out diagonal panel. The new gate must freeze the panel and contraction object before implementation, use the validated finite SU(2)_k domains, forbid retuning/phase fitting/domain repair, include held-out transfer and adversarial invalid-domain/orientation controls, and remain below a full Eq.(27) amplitude claim.

Eq.(29)/Lambda, one-step TNR, refinement bridge and candidate-theory construction remain unauthorized.

## Other fronts / persistent locks

ITER028 remains terminal BLOCKED; ITER034 remains terminal BLOCKED with its over-permissive green run rejected; ITER036 remains historically BLOCKED. BH004/BH004B remains scoped-negative; genuine multivertex Lorentzian EPRL refinement remains source-blocked; RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope.

Still false: `full_eq27_amplitude_derived`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `BRIDGE_DERIVED`.
