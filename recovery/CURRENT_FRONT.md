# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**. Bridge credit remains zero.

## Terminal closed gates

ITER031: **SCIENTIFIC PASS — `RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_CORRECTED_STAGE_S_PASS`**. Authoritative run `34804179870`, aggregate job `103852685845`, aggregate artifact `10332821665`, digest `sha256:d690afd7ac1f3cd09c6c88df8361df1d24455b26f1e66f6d4ea5230c41366ccb`, result commit `3b2f8274647831965a3e06f13fb40072cef08e38`.

ITER032: **SCIENTIFIC PASS — `RC006_EQ27_TWO_FACTOR_BOUNDED_NETWORK_ASSEMBLY_PASS`**. Prereg `bda9c7c12a2f2e4886d4734b9d1835119a700491`; implementation `a369586e5d05b04e757f36468e58aaba00cb1253`; regex-only repair `43ed319f0047a3a71c9eed8962902c7b25ac97d5`; authoritative production head `e1c472ae48f9aeb0aae8419404f1f6382a37b045`; run `34804537344`; aggregate job `103853724474`; aggregate artifact `10333010977`, digest `sha256:9a36150c1efac2f20f3763088a80fdb9fc849232f6e64044776efd68ffd21f5a`; result commit `29e8b1cd197433eefa027231e44bbd5b5853765f`. Max factor residual `8.671119018262734e-16`; max two-factor residual `5.55287100034665e-16`; nulls 3/3. This remains bounded factorized composition, not a full Eq.(27) amplitude.

ITER033: **SCIENTIFIC PASS — `RC006_EQ27_SOURCE_SUMMATION_SCALAR_STRUCTURE_PASS`**. Prereg `d49e51f6fd75613c0ef32d0aea4c98f25f8ff18e`; implementation `c77af1903a9f647abe5ab2e1121b20142bcfa8a3`; production head `580088bdff30de000519a95665f69e9518c0b9d1`; run `34804648187`; jobs null `103854004300`, segmentation `103854004389`, scalar `103854004403`, binding `103854004437`, aggregate `103854032782`; aggregate artifact `10332517828`, digest `sha256:bd46e0c451957c4d0dbc640e6b85390d7882f6f2bd76a897fc0a66f158bf36cd`; result commit `ce4e18848d0846231dc393a91653079cca0ea5b1`. Exact source now uniquely isolates two sums plus the external prefactor `(-1)^(...) (d_l1 d_l2)^alpha d_l`; 3/3 syntax nulls rejected. This is source-structure authority only, not numerical full-amplitude evaluation.

## Active ITER034

`ITER034_RC006_EQ27_SOURCE_LABEL_DOMAIN_AUTHORITY` is prospectively frozen before numerical summation/scalar evaluation. Prereg commit `c0e19fd4c4b76c75bd7fa5d44ad134131d043fbd`; implementation `27af2114b453f93beb420c2ebbb3f2ab097078e8`.

First run `34804798801` exposed a pre-science YAML-only defect: unquoted matrix value `null` became an empty lane. This is **INFRASTRUCTURE FAIL for that lane only**, not scientific evidence. Repair commit `b1410793104f511a3daf199285c0e0ce9c2fc308` quotes `"null"` and changes no scientific predicate.

Authoritative recovery run: **34804823837**, production head `b1410793104f511a3daf199285c0e0ce9c2fc308`. Current jobs: external `103854517728`, factor1 `103854517736`, factor2 `103854517848`, null `103854517905`; at the latest snapshot all four are in progress.

Exact scientific question: whether every Eq.(27) source label needed for the explicit two sum weights and external prefactor has a source-qualified numerical/domain meaning without importing Eq.(29)/Lambda or fitting notation to output. Missing mappings are BLOCKED, not scientific FAIL.

## Exact next action

Consume all four ITER034 raw artifacts and the dependent aggregate against the frozen preregistration. Only `RC006_EQ27_SOURCE_LABEL_DOMAIN_AUTHORITY_PASS` may authorize a separately preregistered bounded numerical summation/scalar lift. If any required label/domain remains unqualified, preserve `RC006_EQ27_SOURCE_LABEL_DOMAIN_BLOCKED`; do not infer it post hoc.

## Locks / other fronts

ITER028 remains terminal BLOCKED. BH004/BH004B remains scoped-negative; genuine multivertex Lorentzian EPRL refinement remains source-blocked; RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope.

Still false: `full_eq27_amplitude_derived`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.
