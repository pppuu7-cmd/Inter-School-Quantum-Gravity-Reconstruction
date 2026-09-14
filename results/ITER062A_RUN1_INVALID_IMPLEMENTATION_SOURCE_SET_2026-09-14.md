# ITER062A run 1 — invalid implementation, source-set incomplete

Date: 2026-09-14

## Frozen gate

Preregistration commit: `1fae03306aa134c06bdc0c486971cd2e7264fb97`.
Initial implementation commit: `50d22f2baa8370df34db9a12830d898ae2d9908e`.
Workflow/head commit: `1e6ad0d412e35020e10969f58d4ccac464d78cb0`.
Authoritative run-1 execution: `34872500144`.

## Raw run-1 provenance

Exact dependency source acquisition passed against frozen SHA256 `78415347fa92b1d0bce1bbd4010faeb3cc939c5f5d6b14d72f340138e4c573ef`; source artifact `10359033015`, digest `sha256:e75835ff7d3801ffa5b5a416ba34e90fa9c931eeb82ba10e54f5dcbf27fee8ae`.

Run-1 lane artifacts:

- dependency-source-identity: `10358793287`, digest `sha256:d702d7bd75feda8ab2eb316ec613339c8f5f6d37477015962e2ddfe5b3c43109` — predicate PASS;
- vertex-kernel-closure: `10359139340`, digest `sha256:365b3a1eac47f5e524f58f50edea6d9caeed9bc3c9f91f0b326e2604de102a7b` — emitted BLOCKED under the incomplete source exposure;
- renormalized-amplitude-closure: `10359637554`, digest `sha256:fb29aa060d60be32592bd845eb6efb9b6cbecfb866c5f3c419cd6b064f02a679` — predicate PASS;
- gluing-index-closure: `10359717623`, digest `sha256:b69d7fafec26bee21a55c67cbad9a60519fe5996105650f200037f8e181aaba5` — predicate PASS;
- observable-closure: `10358979600`, digest `sha256:5dffb902fbb42cfd4819cdd7d26136ed7d9e0db41a6152f606f52d32ddfbad3e` — emitted BLOCKED under the incomplete source exposure;
- aggregate: job `104071729689`, artifact `10358939786`, digest `sha256:3cf3b822ae793a43ea876c06b970533f3323c6661fe9f86138f6c14fb1f61dcf`.

The adversarial-null job `104071658893` failed before its frozen control predicate because Python interpreted a replacement string escape (`\mathcal`) during temporary mutation construction. This is a parser/implementation exception, not a scientific null failure.

## Manual audit and classification

Run 1 must **not** be classified as scientific BLOCKED despite the two emitted lane labels.

The preregistered frozen authority set explicitly contains both:

1. primary arXiv:1508.07961 / `QuantumCuboids_article.tex`, exact validated SHA256 `b7e0690f32cb7cc56f4e64cf5d1f7bc9da54405ed7275d28d4d97a35a148a8ee`;
2. dependency arXiv:1701.02311 / `QuantumCuboidsLong_article.tex`, exact validated SHA256 `78415347fa92b1d0bce1bbd4010faeb3cc939c5f5d6b14d72f340138e4c573ef`.

The run-1 workflow exposed only the dependency TeX to the predicates. The resulting `four_volume_formula=false` is therefore a known false negative because `Eq:4Volume` is one of the already validated ITER006 primary-source equations. The vertex-kernel lane likewise cannot be given scientific force until the primary and dependency formula chain is exposed together as preregistered.

Terminal run-1 classification:

**`INVALID IMPLEMENTATION — RC008_ITER062A_SOURCE_SET_INCOMPLETE + ADVERSARIAL_REPLACEMENT_ESCAPE`**

No scientific PASS/FAIL/BLOCKED credit is assigned from run 1.

## Minimal repairs only

Parser-only adversarial replacement repair commit: `95e1765856b0c6b5317f86b1d74907a75bdb5fdc`.
Null-only repair workflow commit: `c6bd399667c5a691244141cc6190357a0b28c458`.
Repair run: `34872664624`.
Repaired null job `104072130213` passed; artifact `10360205125`, digest `sha256:de4937981020c2688c7529ee1591357bb3ded2792f99e4edc0b34ded17710686`.
Repaired aggregate artifact `10359018499`, digest `sha256:6e94ab248f8016e14de146f93db3a86128ed3f8bd4c94c4b3b4a01547c58ba94`; it still contains the two run-1 false-negative source-set lanes and therefore is not a final scientific classification.

Source-set exposure repair commit: `f1bfd94702eeb43b1027801aaf1bd6e9ed6aecf2`.
Source-set repair workflow/head: `f549b4fb05f3422db3559d5b343bce2d4a3fc253`.
Repair run: `34872817658`.
Only the two affected frozen lanes (`vertex-kernel-closure`, `observable-closure`) are authorized to repeat over the complete primary+dependency source set; already valid run-1 science lanes are not to be repeated.

No frozen scientific predicate, threshold, amplitude model, source hash, normalization or claim ceiling has been changed after viewing run-1 outputs.

## Claim locks

Candidate theory remains `UNFORMED / 0%`. Bridge credit remains zero. This run does not establish amplitude reproduction, alpha flow/fixed point, full EPRL/FK refinement, Lorentzian refinement, continuum recovery, `NEW_PHYSICS_FOUND` or `BRIDGE_DERIVED`.
