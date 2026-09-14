# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**. Bridge credit remains zero.

## Terminal RC006 chain now closed through ITER035

ITER031 is terminal **SCIENTIFIC PASS — `RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_CORRECTED_STAGE_S_PASS`**. Authoritative run `34804179870`; aggregate artifact `10332821665`, digest `sha256:d690afd7ac1f3cd09c6c88df8361df1d24455b26f1e66f6d4ea5230c41366ccb`; result commit `3b2f8274647831965a3e06f13fb40072cef08e38`.

ITER032 is terminal **SCIENTIFIC PASS — `RC006_EQ27_TWO_FACTOR_BOUNDED_NETWORK_ASSEMBLY_PASS`**. Authoritative run `34804537344`; aggregate artifact `10333010977`, digest `sha256:9a36150c1efac2f20f3763088a80fdb9fc849232f6e64044776efd68ffd21f5a`; result commit `29e8b1cd197433eefa027231e44bbd5b5853765f`. This is bounded factorized composition only.

ITER033 is terminal **SCIENTIFIC PASS — `RC006_EQ27_SOURCE_SUMMATION_SCALAR_STRUCTURE_PASS`**. Authoritative run `34804648187`; aggregate artifact `10332517828`, digest `sha256:bd46e0c451957c4d0dbc640e6b85390d7882f6f2bd76a897fc0a66f158bf36cd`; result commit `ce4e18848d0846231dc393a91653079cca0ea5b1`.

ITER034 remains terminal **BLOCKED — `RC006_EQ27_SOURCE_LABEL_DOMAIN_BLOCKED`**, not scientific FAIL. Its over-permissive green run was explicitly rejected after raw-evidence review. Authoritative recovery run `34804915740`, aggregate artifact `10332833015`, digest `sha256:d13f91e7b922ff5b81eb9213cddfb5189c63165c9c2daf36bc93eba3d99fa7a4`, result commit `09ee60bae60b90af3c6741f2fb00b1d646704e42`.

ITER035 resolves that narrow authority blocker and is terminal **SCIENTIFIC PASS — `RC006_INDEXED_SIMPLICITY_MAP_SOURCE_AUTHORITY_PASS`**. Prereg `865aa1901a54620b0cd296efd338268492caf787`; implementation `87b4e23b8e9bb915bd8e328464102bb6ccfa7240`; production head `ab1d30ef5446825d87ca07df00ba21129a401fd8`; run `34805066706`; aggregate job `103855261464`; aggregate artifact `10332861829`, digest `sha256:da69480c7864f0b99185a03622e26d107bfa2af18d2257ed28df869426b842e6`; result commit `bc14b296cae425a599c693130a5a4941a5cf0f24`.

Raw A/B/C/D evidence was inspected. The exact source explicitly gives `(j^+,j^-)=((1+gamma)l/2,(1-gamma)l/2)`, declares indexed maps `l_i -> (j_i^+,j_i^-)`, gives `j_max=k/2`/integer-representation finite-level restrictions and root-of-unity coupling conditions, and rejects all 3/3 frozen false authorities. This is source authority only; no Eq.(27) sum has yet been promoted to a full amplitude.

## Active ITER036

`ITER036_RC006_EPRL_MAP_LABEL_INSTANTIATION_CONSISTENCY` is prospectively frozen before execution. It mechanically uses only non-trivial `(k,gamma)` cases explicitly listed by the byte-pinned source; gamma may not be chosen by performance.

- prereg commit `be603f7b288a60b0feb76d3bfc723523f6723754`
- implementation commit `d9350854500b2d31c53f08fdbc325908909d9ef0`
- production head `862736b45047cadef8f696e79e15815f67dd559b`
- authoritative run `34805398376`
- jobs: B map integrality/cutoff `103856182955`; C indexed exponent instantiation `103856183065`; D algebraic nulls `103856183071`; A source-list extraction `103856183212`.

Latest snapshot: **3 in_progress / 1 queued**, avoidable idle false. No duplicate batch is admissible.

ITER036 tests exact rational map identities, finite-k cutoff/integrality, deterministic primary/held-out transport from the source-listed panel, common admissible internal-j support for the two Eq.(27) exponent factors, and 3/3 frozen wrong-map controls. It remains below numerical Eq.(27) summation/scalar evaluation.

## Exact next action

Consume all raw ITER036 artifacts and aggregate against the frozen preregistration. Source-list/panel insufficiency is BLOCKED; a valid-panel exact-identity/null failure is SCIENTIFIC FAIL. Only `RC006_EPRL_MAP_LABEL_INSTANTIATION_CONSISTENCY_PASS` may authorize a separately preregistered bounded numerical Eq.(27) summation/scalar-lift gate.

## Locks / other fronts

ITER028 remains terminal BLOCKED. BH004/BH004B remains scoped-negative; genuine multivertex Lorentzian EPRL refinement remains source-blocked; RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope.

Still false: `full_eq27_amplitude_derived`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.
