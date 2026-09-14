# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**. Bridge credit remains zero.

## Newly closed — ITER038

ITER038 is terminal **SCIENTIFIC PASS — `RC006_EQ27_CENTRAL_COUPLING_DOMAIN_AUTHORITY_PASS`**.

Frozen authority: prereg `3cdcc41939aac89c4bd934c10fbd7bc48a8dd321`; implementation `6340ead5bd78bdc650261c4827298943eab1b7a5`; production `b68d479615b9f966c2628ba8c69c1a2336d5c1dc`; original run `34805710939`. A/C/D passed directly. The original B blocker was a TeX-alignment parser defect: raw source already contained all frozen finite-k predicates. Minimal parser-only repair `e1eb8a3b6fb8db1bef1caa9262d853bfee9bd387` changed no science. B-only recovery run/job `34805845056 / 103857457176`, artifact `10333225494`, digest `sha256:af9dde495a26791a59f32f17cb2629ac740b0a8a92cfad9242b398c7407f04b6`, is PASS. Durable result commit `f9391713820703a0a2619222bd38d7485cf84e4e`.

The original aggregate is preserved and not retrofitted. ITER038 PASS only authorizes a bounded central/intermediate-index component gate, not a full Eq.(27) amplitude.

## Active ITER039

`ITER039_RC006_EQ27_BOUNDED_CENTRAL_COMPONENT_CLOSURE` was preregistered before implementation. It evaluates every source-authorized central `(J+,J-,l)` tuple from ITER038 on the unchanged primary and held-out diagonal panels using previously validated q-CG/qbar/dual/braid primitives. Physical integer-spin central labels are converted to the existing twice-spin numerical representation without changing the source domain.

Frozen thresholds are inherited from the validated primitive layer: source-qbar identity `<2e-12`, qbar intertwiner `<5e-9`, dual contraction `<5e-8`, R/R^-1 `<5e-8`. No tuple pruning, retuning, phase fitting, normalization fitting, Eq.(29), Lambda or TNR is permitted.

- prereg commit `b40ff1765bd5c5c73f578a943dca72ea031f08e4`
- implementation commit `d05819e58f86994e08043708d67b465a343a48c1`
- production/workflow head `bb21fda2081ca81a691bf58cac2073645201b17f`
- authoritative run `34806079470`
- jobs: C held-out transfer `103858118898`; B primary closure `103858118927`; D nulls `103858118961`; A provenance/domain `103858119040`.

Latest snapshot: **3 in_progress / 1 queued**, avoidable idle false.

## Exact next action

Consume all four raw ITER039 lane artifacts and dependent aggregate against the frozen preregistration. Only `RC006_EQ27_BOUNDED_CENTRAL_COMPONENT_CLOSURE_PASS` may authorize a separately preregistered bounded label-complete Eq.(27) network-assembly gate. A valid-source frozen residual failure is SCIENTIFIC FAIL; missing authority is BLOCKED; execution/dependency failure is NUMERICAL/INFRASTRUCTURE FAIL.

## Persistent locks / other fronts

Eq.(29)/Lambda, one-step TNR, full Eq.(27) amplitude, refinement bridge and candidate-theory construction remain unauthorized. ITER028 and ITER036 remain historically BLOCKED; ITER034 remains BLOCKED with its over-permissive green run rejected. BH004/BH004B remains scoped-negative; genuine multivertex Lorentzian EPRL refinement remains source-blocked; RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope.

Still false: `full_eq27_amplitude_derived`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `BRIDGE_DERIVED`.
