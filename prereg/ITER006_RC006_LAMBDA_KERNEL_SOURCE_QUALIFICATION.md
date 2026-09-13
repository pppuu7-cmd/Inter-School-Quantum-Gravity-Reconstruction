# Preregistration — ITER006 RC006 Lambda-kernel source qualification

Frozen before implementation/production on 2026-09-13.

## Scientific objective
Qualify the exact source-defined structural content of the Proposition 3.4 `Lambda` kernel needed for a later low-spin numerical implementation, without importing the historical pair-sign projection and without authorizing Eq.(29).

## Immutable source
Fairbairn et al., arXiv:1112.2511v1.
TeX tar SHA256: `d2dfda1a79b9978422b5a57387f9bbf1ebd4828327c656b59ed74c0acc98302c`.
PDF SHA256: `b41866cdd69defdef1862416bfb40e8b4c39775b53a51718a7cae837fedf6667`.

## Independent lanes
Four source lanes, `fail-fast:false` conceptually:
1. TeX lexical extraction.
2. TeX structure extraction with independent normalization.
3. PDF text lexical extraction.
4. PDF semantic structure extraction.

## Frozen predicates
Every lane must independently establish all of the following from Proposition 3.4/source context:
- braiding acts on ordered inputs `(alpha2, alpha1)`;
- a nontrivial sum over representation label `K` occurs;
- a `Lambda` coefficient/kernel is present in that transformation law;
- source-visible index/label incidence contains `K1`, `K`, `K2`, and `J` associated with the Lambda object/context;
- `alpha1(K)` is explicitly not guaranteed to be an EPRL representation;
- the untouched legs retain `alpha3(K3)` and `alpha4(K4)` while the braided output contains `alpha2(K2)` and `alpha1(K)`.

The two TeX lanes and two PDF lanes must each agree internally on the canonical structural record. Cross-format agreement is required on the canonical record fields above; typography/order differences outside those fields are ignored.

## Frozen interpretation
- 4/4 valid + canonical agreement: `QEPRL_PROP34_LAMBDA_SOURCE_STRUCTURE_QUALIFIED`.
- At least 2 valid but disagreement: `QEPRL_PROP34_LAMBDA_SOURCE_STRUCTURE_AMBIGUOUS`.
- Fewer than 2 valid: `QEPRL_PROP34_LAMBDA_SOURCE_STRUCTURE_UNSUPPORTED`.

Only the QUALIFIED outcome authorizes a separate prospective low-spin Lambda numerical implementation gate. No outcome authorizes Eq.(29), bridge credit, `BRIDGE_DERIVED`, candidate theory, or rewriting the historical braid-projection FAIL.

## Failure discipline
Network/source-fetch failure, parser/tokenization failure, missing system package, or serialization error is infrastructure/numerical failure and must be repaired minimally without altering these predicates or classifier.