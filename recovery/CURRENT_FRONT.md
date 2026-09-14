# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**. Bridge credit remains zero.

## Newly closed — ITER039

ITER039 is terminal **SCIENTIFIC FAIL — `RC006_EQ27_BOUNDED_CENTRAL_COMPONENT_CLOSURE_FAIL`**. This is a failure of the frozen expanded central-component closure gate, not an infrastructure failure and not a global falsification of RC006.

Provenance: prereg `b40ff1765bd5c5c73f578a943dca72ea031f08e4`; implementation `d05819e58f86994e08043708d67b465a343a48c1`; production `bb21fda2081ca81a691bf58cac2073645201b17f`; run `34806079470`; jobs C `103858118898`, B `103858118927`, D `103858118961`, A `103858119040`, aggregate `103858164412`; aggregate artifact `10333415213`, digest `sha256:abc8db20556142a54f467311268f061cb21eb5dbf857994788f5ed74f2974807`; result commit `73bc362dce539c918c1a3b9344739c1d67316dd3`.

Lane A PASS and lane D PASS (3/3 invalid controls detected). Lane B evaluates 54 primary tuples with no retuning and fails 7; lane C evaluates 96 held-out tuples identically and fails 23. Representative R/R^-1 residual is `16.48528137423864` for `(k=6,J+=2,J-=2,l=0)` versus frozen `5e-8`; held-out maximum is `2349.968022439629`. Some k=12 tuples also fail the frozen dual-contraction predicate with residual up to `0.7137917357844189`. Direct-source qbar identity remains zero in the recorded rows and qbar-intertwiner residual remains below its `5e-9` threshold.

No threshold, phase, normalization, tuple selection or domain rule is changed. ITER039 remains FAIL permanently under its frozen gate.

## Exact next gate

The only admissible immediate RC006 continuation is an **independent component-validity-boundary diagnostic**. It may determine whether the failed tuples lie outside the previously source-qualified/validated primitive domain or coincide with root-of-unity trace-zero/quotient boundaries, and must separately reproduce the R and dual residual patterns. It may not remove failed tuples, alter thresholds, reinterpret ITER039 as PASS, or directly authorize a full Eq.(27) amplitude.

## Persistent locks / other fronts

Eq.(29)/Lambda, one-step TNR, full Eq.(27) amplitude, refinement bridge and candidate-theory construction remain unauthorized. ITER028 and ITER036 remain historically BLOCKED; ITER034 remains BLOCKED with its over-permissive green run rejected. BH004/BH004B remains scoped-negative; genuine multivertex Lorentzian EPRL refinement remains source-blocked; RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope.

Still false: `full_eq27_amplitude_derived`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `BRIDGE_DERIVED`.
