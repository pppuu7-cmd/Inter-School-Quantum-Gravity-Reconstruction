# ITER062A provenance-only correction — primary source SHA256

Date: 2026-09-14
Parent preregistration: `prereg/ITER062A_RC008_RESTRICTED_AMPLITUDE_KERNEL_CLOSURE_2026-09-14.md`, commit `1fae03306aa134c06bdc0c486971cd2e7264fb97`.

## Classification of this amendment

This is a **pre-existing-authority provenance transcription correction**, not a scientific threshold/model/source change.

The parent preregistration accidentally wrote the primary `QuantumCuboids_article.tex` SHA256 as:

`b7e0690f32cb7cc56f4e64cf5d1f7bc9da54405ed7275d28d4d97a35a148a8ee`.

That value is contradicted by the already-existing validated ITER006 source-equation artifacts that the same preregistration names as its authority.

Before ITER062A existed, ITER006 run `34698656157` had frozen exact source snapshots from arXiv:1508.07961. Two independently relevant artifacts are:

- vertex snapshot artifact `10299427022`: `record.path = QuantumCuboids_article.tex`, `record.file_sha256 = ba973b02a05688c2b122c95a111b70b0fe03a126fac399b073725574afc7358b`, `Eq:VertexDefinition` equation hash `8f00e971eb572b8aa83f4b19926cb4f67f78749c5e25f3bbcba0238beff0d5d9`;
- 4-volume snapshot artifact `10299576801`: the same `record.file_sha256 = ba973b02a05688c2b122c95a111b70b0fe03a126fac399b073725574afc7358b`, with `Eq:4Volume` equation hash `f318b141c6f12f1c4e79afde56721c975704190eb62b9532433bc8fee70287f1`.

The historical ITER006 workflow itself fetched official arXiv source directly and hashed the raw TeX file; no normalization was applied to `file_sha256`.

On 2026-09-14, an independent version-recovery probe also retrieved arXiv:1508.07961v2 / current source with raw `QuantumCuboids_article.tex` SHA256 `ba973b02a05688c2b122c95a111b70b0fe03a126fac399b073725574afc7358b` (79,595 bytes), agreeing exactly with the pre-existing ITER006 artifact rather than with the mistyped parent-preregistration value.

## Correct frozen primary source identity

The authoritative primary-source SHA256 for ITER062A is therefore corrected to the value that was frozen by ITER006 **before ITER062A was designed**:

`ba973b02a05688c2b122c95a111b70b0fe03a126fac399b073725574afc7358b`.

Dependency-source SHA256 remains unchanged:

`78415347fa92b1d0bce1bbd4010faeb3cc939c5f5d6b14d72f340138e4c573ef`.

## What does not change

No formula, scientific predicate, closure requirement, lane, amplitude model, measure, normalization, incidence relation, observable, numerical threshold, PASS/BLOCKED criterion, claim lock, or successor authorization is changed.

Run `34872817658`, which rejected the correct pre-existing primary source only because it compared against the mistyped hash, is classified **INVALID IMPLEMENTATION / PROVENANCE TRANSCRIPTION MISMATCH PRE-SCIENCE**, not scientific BLOCKED/FAIL.

The only permitted repair is to expose the exact `ba973...` primary source together with the already frozen dependency source and rerun only the two lanes whose run-1 outputs were invalidated by incomplete source exposure: `vertex-kernel-closure` and `observable-closure`. Existing valid run-1 `source-identity`, `renormalized-amplitude`, `gluing-index`, and repaired adversarial-null evidence must be reused rather than recomputed for scientific credit.

Candidate theory remains `0 / UNFORMED`; bridge credit remains zero.
