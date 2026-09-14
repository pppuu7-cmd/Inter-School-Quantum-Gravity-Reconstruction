# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**. Bridge credit remains zero.

## Newly closed in this iteration

ITER031 is terminal **SCIENTIFIC PASS — `RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_CORRECTED_STAGE_S_PASS`**. Authoritative run `34804179870`; aggregate artifact `10332821665`, digest `sha256:d690afd7ac1f3cd09c6c88df8361df1d24455b26f1e66f6d4ea5230c41366ccb`; result commit `3b2f8274647831965a3e06f13fb40072cef08e38`.

ITER032 is terminal **SCIENTIFIC PASS — `RC006_EQ27_TWO_FACTOR_BOUNDED_NETWORK_ASSEMBLY_PASS`**. Prereg `bda9c7c12a2f2e4886d4734b9d1835119a700491`; implementation `a369586e5d05b04e757f36468e58aaba00cb1253`; regex-only technical repair `43ed319f0047a3a71c9eed8962902c7b25ac97d5`; authoritative production head `e1c472ae48f9aeb0aae8419404f1f6382a37b045`; run `34804537344`; aggregate job `103853724474`; artifact `10333010977`, digest `sha256:9a36150c1efac2f20f3763088a80fdb9fc849232f6e64044776efd68ffd21f5a`; result commit `29e8b1cd197433eefa027231e44bbd5b5853765f`. Max factor residual `8.671119018262734e-16`, max two-factor residual `5.55287100034665e-16`, frozen nulls 3/3. This is bounded factorized composition only, not a full Eq.(27) amplitude.

ITER033 is terminal **SCIENTIFIC PASS — `RC006_EQ27_SOURCE_SUMMATION_SCALAR_STRUCTURE_PASS`**. Prereg `d49e51f6fd75613c0ef32d0aea4c98f25f8ff18e`; implementation `c77af1903a9f647abe5ab2e1121b20142bcfa8a3`; production `580088bdff30de000519a95665f69e9518c0b9d1`; run `34804648187`; aggregate job `103854032782`; artifact `10332517828`, digest `sha256:bd46e0c451957c4d0dbc640e6b85390d7882f6f2bd76a897fc0a66f158bf36cd`; result commit `ce4e18848d0846231dc393a91653079cca0ea5b1`. Exact source uniquely isolates the two internal sums and external prefactor; this is source-structure authority only.

ITER034 is terminal **BLOCKED — `RC006_EQ27_SOURCE_LABEL_DOMAIN_BLOCKED`**, not scientific FAIL. The first YAML-null defect was infrastructure only. The later green run `34804823837` was explicitly rejected after raw-artifact review as `IMPLEMENTATION/VALIDATION FAIL PRE-SCIENCE — AUTHORITY EVIDENCE SCOPE TOO PERMISSIVE`; green CI was not promoted to scientific PASS. Validation repair `a2443d483fa8e981b0482203fead6c18600f26c8` restricted evidence to validated RC006 authority notes.

Authoritative ITER034 recovery: production head `7ea3e3f8fd894197dee7023742426e347e859954`, run `34804915740`; jobs null `103854787314`, factor1 `103854787466`, external `103854787479`, factor2 `103854787506`, aggregate `103854902730`; aggregate artifact `10332833015`, digest `sha256:d13f91e7b922ff5b81eb9213cddfb5189c63165c9c2daf36bc93eba3d99fa7a4`; result commit `09ee60bae60b90af3c6741f2fb00b1d646704e42`. External labels PASS and nulls PASS 3/3, but both factor lanes are BLOCKED: `j^+_2,j^-_1,j^+_1,j^-_2` occur lexically in Eq.(27) yet lack an accepted explicit source/domain map in the current restricted authority set. Numerical scalar/summation completion remains unauthorized.

## Active ITER035

`ITER035_RC006_INDEXED_SIMPLICITY_MAP_SOURCE_AUTHORITY` is prospectively frozen as an independent exact-source search for the missing indexed simplicity map/domain, without Eq.(29)/Lambda and without numerical fitting.

- prereg commit `865aa1901a54620b0cd296efd338268492caf787`
- implementation commit `87b4e23b8e9bb915bd8e328464102bb6ccfa7240`
- production head `ab1d30ef5446825d87ca07df00ba21129a401fd8`
- authoritative run `34805066706`
- jobs: B indexed-label inheritance `103855234205`, D provenance/null `103855234346`, C representation domain `103855234413`, A simplicity-map definition `103855234468`.

Latest snapshot: **2 in_progress / 2 queued**, so avoidable idle is false. No duplicate batch is admissible.

## Exact next action

Consume all four raw ITER035 artifacts and aggregate against the frozen preregistration. Only `RC006_INDEXED_SIMPLICITY_MAP_SOURCE_AUTHORITY_PASS` may authorize a separately preregistered bounded label-instantiation/consistency gate. If the exact source still does not explicitly connect the indexed `j_i^+,j_i^-` labels to the simplicity map/domain, preserve BLOCKED and do not infer it from notation or Eq.(29)/Lambda.

## Locks / other fronts

ITER028 remains terminal BLOCKED. BH004/BH004B remains scoped-negative; genuine multivertex Lorentzian EPRL refinement remains source-blocked; RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope.

Still false: `full_eq27_amplitude_derived`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.
