# ITER042 — RC006 delegated authority source expansion

Date: 2026-09-14

## Terminal classification

**`DELEGATED_AUTHORITY_SOURCE_EXPANSION_CANDIDATES_FOUND`**

This is the positive terminal outcome of the frozen **discovery gate only**. It is **not** exact-formula qualification, does not reverse ITER039 `SCIENTIFIC_FAIL`, and does not authorize any numerical retry.

## Frozen preregistration

- prereg commit: `ce2e1c73a62ab416b8625b8934f7e598063bda5e`
- prereg path: `prereg/ITER042_RC006_DELEGATED_DUALITY_AUTHORITY_SOURCE_EXPANSION_2026-09-14.md`
- production head: `5ef1025bbae0f12e7374578fdeb9e1baf108102d`
- authoritative run: `34806737112`

## Jobs and validated artifacts

All four discovery lanes and the dependent aggregate completed. Green CI is not used as the scientific classification.

- books-Crossref job `103859971665`; artifact `10333306491`; digest `sha256:4cd092b6ea5e276470a2603a462d8633ca7353e19424ad9098da735e73269db7`
- root-OpenAlex job `103859971776`; artifact `10333346306`; digest `sha256:e9626fedcaa9706825048cd768860ec0b08312fe8b3e663b15db05a15b62f480`
- books-OpenLibrary job `103859971804`; artifact `10332693982`; digest `sha256:e901dddf8bededbf7e6588dc851a6d1644a195c82585ea86ef984feb946e0554`
- dual-OpenAlex job `103859971841`; artifact `10333520820`; digest `sha256:315494a90210079720ef053180c76126977c2c673bd764db03df4c10cf49e4fa`
- aggregate job `103860026831`; artifact `10332304276`; digest `sha256:ba3d0d24bd90d8d8d64687d76ffb3c0252f627710395e271939ec50b89d2b444`

Aggregate raw classification is `DISCOVERY_EVIDENCE_COLLECTED_REQUIRES_EXACT_FORMULA_QUALIFICATION`, with `numerical_retry_authorized=false`, `ITER039_remains_scientific_fail=true`, `bridge_credit=false`, and `candidate_theory_authorized=false`.

## Discovery evidence

### Delegated books

Crossref resolves the frozen delegated authorities without substituting other books:

1. L. C. Biedenharn and M. A. Lohe, *Quantum Group Symmetry and Q-Tensor Algebras*, DOI `10.1142/2815`, 1995; Crossref also exposes chapter metadata including *Quantum Groups at Roots of Unity*.
2. J. S. Carter, D. E. Flath and M. Saito, *The Classical and Quantum 6j-symbols*, DOI records `10.1515/9780691234670` / `10.2307/j.ctv1nxcv83`; chapter metadata includes *Quantum sl(2)*.

The discovery artifacts do **not** establish that these catalog/DOI records expose sufficient formula text. Metadata alone is not treated as authority.

### Open full-text candidates

The dual-OpenAlex frozen full-text search returned inspectable candidates, including:

- OpenAlex `W2131194795`, *Spin foam models for 3D quantum geometry*, with an open Nottingham thesis PDF;
- OpenAlex `W3021373932` / `W2100639234`, *Line operators in theories of class S, quantized moduli space of flat connections, and Toda field theory*, with arXiv `1505.05898` / open full text;
- additional lower-priority open candidates retained in the raw artifact.

The root-OpenAlex query returned zero candidates under its frozen query. Therefore ITER042 does **not** claim an independent root-domain source discovery from that lane.

Under the preregistered terminal semantics, at least one inspectable full-text candidate for the missing duality/domain question is enough for `...CANDIDATES_FOUND`; exact formulas must be qualified separately.

## Scientific interpretation

ITER041 remains `RC006_ROOT_UNITY_PRIMITIVE_DOMAIN_SOURCE_AUTHORITY_BLOCKED` on the dual/cap/cup normalization identity. ITER039 remains `RC006_EQ27_BOUNDED_CENTRAL_COMPONENT_CLOSURE_FAIL`. ITER042 only resolves the next source-search step: there are inspectable candidate texts worth exact formula/domain qualification.

No threshold, tuple domain, normalization, phase, convention, or failed ITER039 result has been changed.

## Locks

- numerical ITER039 retry: **NOT AUTHORIZED**
- full Eq.(27) amplitude: **NOT DERIVED**
- Eq.(29)/Lambda: **NOT AUTHORIZED**
- one-step TNR: **NOT AUTHORIZED**
- bridge credit: **0**
- candidate theory: **0 / UNFORMED**

## Exact next gate

Prospectively preregister a separate exact-formula/source-domain qualification over the frozen discovery candidates. It must preserve source excerpts/provenance and must not infer a convention from numerical agreement. Only a terminal exact-formula qualification PASS may authorize a later implementation/validation gate.