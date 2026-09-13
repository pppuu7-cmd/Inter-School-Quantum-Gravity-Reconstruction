# ITER006 RC006 Lambda source qualification — terminal result

Date: 2026-09-13

## Frozen gate
Preregistration: `a18bb2e0ab8adda10aa16f14fdbef82341f6688e`.
Scientific objective and predicates were frozen before implementation. Immutable source: Fairbairn et al., arXiv:1112.2511v1, TeX SHA256 `d2dfda1a79b9978422b5a57387f9bbf1ebd4828327c656b59ed74c0acc98302c`, PDF SHA256 `b41866cdd69defdef1862416bfb40e8b4c39775b53a51718a7cae837fedf6667`.

## Technical attempts
Initial production head `8deca0c6390bdd0bd79d1b7be4e2efedef3534cf`, run `34744039075`, failed the two PDF lanes only on the `domain_note` tokenization predicate while all other frozen predicates passed. The aggregate artifact `10313323964` (`sha256:8c6af75d492221c45e7dce605528cfcf310b779cff17975e92bc308f38800acf`) reported the mechanical classifier `QEPRL_PROP34_LAMBDA_SOURCE_STRUCTURE_AMBIGUOUS`, but raw logs/artifacts localized the discrepancy to PDF text tokenization rather than source disagreement. This attempt is therefore retained as `INFRASTRUCTURE_PARSER_TOKENIZATION_FAIL`, not a scientific negative result.

A first dehyphenation-only repair, head `3ba7c45f62577a961cefe679d5274b379a348932`, run `34746508475`, remained insufficient for the PDF tokenization representation and is retained as a technical diagnostic only. No scientific predicate, source hash, threshold, or classifier was changed.

The final normalization-only repair removes non-letter separators only for matching the same frozen phrase. It does not alter the semantic predicate or canonical record.

## Authoritative production
Head: `639acff2f84468ee5462898a56b913d242df7a1b`
Run: `34746554509`
Jobs:
- PDF lexical `103695433732`
- TeX lexical `103695433809`
- TeX structural `103695433834`
- PDF structural `103695433846`
- aggregate `103695474938`

Raw artifacts:
- PDF structural `10314745658`, digest `sha256:06584140ed74a00f3027a37386338eaabb99d99fdd538b2d1da4ecbd58f083c6`
- TeX lexical `10314630878`, digest `sha256:59b51e2b93fb00a403ed770cadb30bcb32dd5ab56b9e4fe6c1684c992f47d887`
- TeX structural `10314102817`, digest `sha256:d5de414e1973b87b7fc263e9efa0484b10f61dfe4775be984ff3087dd1495f34`
- PDF lexical `10313898410`, digest `sha256:ef9c774729e29eaf2979fea0bb78b95c0ad9518b69b4fc23ca40ad832d1973c2`

Aggregate artifact: `10314366524`, digest `sha256:7761a3788e2d860ae0dd1156abd83217047d09c0c506e810fb540a77ab4fa7de`.

## Raw-result audit
All 4/4 raw lanes are valid. Every lane independently passes all frozen predicates and yields the same canonical record:
- braid inputs `(alpha2, alpha1)`;
- nontrivial summation over `K`;
- `Lambda` kernel present;
- labels `(K1, K, K2, J)`;
- `alpha1(K)` is not necessarily an EPRL representation;
- untouched outputs `alpha3(K3), alpha4(K4)`;
- braided outputs `alpha2(K2), alpha1(K)`.

Aggregate: `passing_lanes=4`, `canonical_agreement=true`.

## Scientific classification
`QEPRL_PROP34_LAMBDA_SOURCE_STRUCTURE_QUALIFIED`

This closes only the source/domain qualification rubric. It authorizes a separate prospectively preregistered low-spin source-faithful Lambda numerical implementation gate.

It does **not** authorize Eq.(29), amplitude/refinement bridge credit, `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, candidate-theory construction, or rewriting the historical braid-sensitive pair-sign FAIL.
