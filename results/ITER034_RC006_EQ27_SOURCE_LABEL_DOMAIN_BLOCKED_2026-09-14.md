# ITER034 result — Eq.(27) source label/domain authority

Date: 2026-09-14

Scientific classification: **BLOCKED — `RC006_EQ27_SOURCE_LABEL_DOMAIN_BLOCKED`**.

This is not a scientific failure of RC006. It is a source-authority blocker: the currently validated RC006 authority set does not explicitly qualify the factor-specific simplicity labels needed by both Eq.(27) sum weights. Numerical scalar/summation completion is therefore not authorized.

## Frozen provenance

- preregistration commit: `c0e19fd4c4b76c75bd7fa5d44ad134131d043fbd`
- initial implementation commit: `27af2114b453f93beb420c2ebbb3f2ab097078e8`
- YAML-only repair: `b1410793104f511a3daf199285c0e0ce9c2fc308`
- run `34804823837` is retained as **IMPLEMENTATION/VALIDATION FAIL PRE-SCIENCE — AUTHORITY EVIDENCE SCOPE TOO PERMISSIVE**, despite green CI; validation repair commit `a2443d483fa8e981b0482203fead6c18600f26c8`, repair-note commit `a385f2ec22eba17f3340e3f1043c35bc9f83b3eb`
- authoritative production head: `7ea3e3f8fd894197dee7023742426e347e859954`
- authoritative recovery run: `34804915740`

Authoritative jobs/artifacts:
- null job `103854787314` -> artifact `10332092914`, digest `sha256:ff227258b42f5a8cea036ef55dc3f6995e1761dd0b19813fb18991ede96624e4`
- factor1 job `103854787466` -> artifact `10332533245`, digest `sha256:2d2da1c0edfc2b64115630da9022ef4011d18baafed9f3232628f1a139bc1479`
- external job `103854787479` -> artifact `10332588189`, digest `sha256:15779186fee83e8c744f0df590c171611ef442523cae16e74a30835a70c7922a`
- factor2 job `103854787506` -> artifact `10332262311`, digest `sha256:35659141571854df5a1057bb84355905e4c907e9ec7568e8038c9b97666636c7`
- aggregate job `103854902730` -> artifact `10332833015`, digest `sha256:d13f91e7b922ff5b81eb9213cddfb5189c63165c9c2daf36bc93eba3d99fa7a4`

## Scientific readout

The repaired, restricted authority audit gives:
- external prefactor labels: PASS in the currently validated authority set;
- factor-1 sum labels: **BLOCKED**;
- factor-2 sum labels: **BLOCKED**;
- frozen domain-null controls: PASS, 3/3 insufficient substitutes rejected.

The unresolved labels are specifically the factor-indexed simplicity labels entering the source exponents:
- factor 1: `j^+_2` and `j^-_1` have lexical occurrences in Eq.(27), but no accepted explicit source/domain mapping in the restricted validated authority set;
- factor 2: `j^+_1` and `j^-_2` likewise lack accepted explicit source/domain mapping.

The internal sum label `j`, quantum dimension `d_j`, and q convention are qualified. The external `l,l_1,l_2,alpha`/dimension structure is qualified in scope. The blocker is therefore narrower than a generic Eq.(27) source failure: it is the indexed simplicity-label/domain map needed to instantiate the two source q-exponents without inference.

The aggregate correctly reports `blocked_lanes=[factor1,factor2]`, `scientific_pass=false`, no infrastructure lanes, and preserves `full_eq27_amplitude_derived=false`, `eq29_amplitude_authorized=false`, `one_step_tnr_authorized=false`, `bridge_credit=false`.

## Exact authorization

No bounded numerical scalar/summation lift is authorized from ITER034. The next admissible step is an independent prospectively preregistered source-internal authority discovery gate over the exact byte-pinned arXiv source, looking for the explicit simplicity map/domain of the indexed `j_i^+,j_i^-` labels in sections preceding/defining Eq.(27). It must not use Eq.(29)/Lambda to fill the map and must not infer the map from numerical output.

Candidate theory remains `UNFORMED / 0%`; overall roadmap readiness remains 49%; bridge credit remains zero.