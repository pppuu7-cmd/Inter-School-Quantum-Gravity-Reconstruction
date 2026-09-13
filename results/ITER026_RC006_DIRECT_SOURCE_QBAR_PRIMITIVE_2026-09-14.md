# ITER026 terminal — RC006 direct-source qbar primitive

Date: 2026-09-14

## Terminal classification

`PASS — RC006_DIRECT_SOURCE_QBAR_PRIMITIVE_VALIDATED`

This is a bounded executable-primitive PASS in the RC-006 reduced Euclidean `SU(2)_k x SU(2)_k` realization only. It authorizes a separately preregistered bounded Eq.(27) component translation/contraction. It is not an Eq.(27) PASS, not a TNR PASS, not bridge evidence, and not candidate-theory evidence.

## Prospective contract

Preregistration: `prereg/ITER026_RC006_DIRECT_SOURCE_QBAR_IDENTITY_EXECUTION_2026-09-14.md`

Prereg commit: `17dd87a110645b2a7ca6cc22df52569758502a70`.

Frozen hypothesis: the exact cited q<->qbar component identity, applied directly to the already validated q-CG tensor with the source map order and a B2-fixed singlet residual `+-1` gauge only, yields a source-faithful executable qbar/dual primitive over the full frozen root-of-unity panel, including every prior ITER025A counterexample.

## Implementation and run chronology

Implementation: `code/iter026/direct_source_qbar_identity.py`
Implementation commit: `caf988b3313a9c7cf5f7c6b409e6eb3ef99f0215`.

The implementation constructs

`C_bar_src(a,b,c;k) = (-1)^((a+b-c)/2) * (J_a tensor J_b) * C_q(a,b,c;k) * J_c`

with no `m1<->m2` swap, and then realizes the bent-leg graph map by the prospectively frozen `ba -> ab` tensor-order permutation and `1/sqrt(d_c)` factor. It does not use the inverse-parameter qbar solver for construction.

### Non-authoritative run 1

Run `34789842824`, production head `be3de636b18b494c61c15179f67e6d1af8cf6634`, is terminal `INVALID_IMPLEMENTATION_PRE_SCIENCE` because the unquoted YAML token `null` was parsed as a null scalar and the frozen five-lane matrix contract was not instantiated correctly. No scientific lane output from that run was inspected or used. Durable note: `results/ITER026_RUN1_INVALID_IMPLEMENTATION_PRE_SCIENCE_2026-09-14.md`, commit `99f6424c42f144affd48840b6d6c4bb5c2edd598`.

The only repair was to quote the literal lane name `'null'`; no formula, source, panel, threshold, or verdict criterion changed.

### Authoritative corrected run

- production/workflow head: `d6a457f364feefd3fd4523ab84e09f8803590f3c`
- GitHub Actions run: `34789873827`
- algebra job: `103812003442`
- four-valent job: `103812003478`
- domain job: `103812003485`
- null-control job: `103812003488`
- cup job: `103812003489`
- aggregate job: `103812043906`

Artifacts:

- algebra: `10328475225`, digest `sha256:de7b6d8caa37a74503f239f8b89dade57934d06185e6f0ce19911756fbc2f40f`
- four: `10328385419`, digest `sha256:3a135dfc28d04f8c5cc1b652922328c96d2744c8ca8e848df06e0013d348b255`
- null: `10328295540`, digest `sha256:965a4f0f77cc11693466d1da425e78551ee18385c16427ea801bcd0ee2163179`
- cup: `10327548996`, digest `sha256:b4110f860d3620d49f03b34d2d6b18e2c7edf99e50b37b1b79e206e2b1cb3e34`
- domain: `10327359843`, digest `sha256:c8e7778759f33142cd321ffe00284524a031d812130f9ea5c18c262b011ee8ad`
- aggregate: `10328005590`, digest `sha256:f74355c6d101ee1728e01f7ddc953bac09d3b00a6d8678db51287e5ecfa98bad`

All five frozen lanes PASS.

## Domain/provenance lane

PASS.

Exact source record contains all frozen hashes and locators for `1609.02429v2`, `1312.0905v2`, and `1311.1798v1`. The complete cup panel contains 55 cases across `k = 6,7,9,10,11,12`, every `twice_j = 1,...,k`, and all eight known ITER025A counterexamples. Every tested singlet lies in the frozen target simple-object/admissibility domain and has nonzero quantum dimension. No high/root-boundary point was removed.

## Algebra lane

PASS.

- max direct source-identity residual: `0.0`
- max qbar coproduct/intertwiner residual: `1.5594956288365066e-12` versus `5e-9`
- max full B2 residual after the prospectively frozen singlet source-gauge calibration: `2.3525204118543076e-15` versus `2e-9`
- max `sigma^2 - 1` error: `1.5808793174773598e-14` versus `2e-9`
- max imaginary part of the singlet gauge ratio: `2.9643953935139677e-15` versus `2e-9`
- inverse-parameter qbar solver used for construction: `false`
- per-channel post-hoc repair: `false`

## Independent cup lane

PASS over all 55 prospectively frozen cases.

Global max residual: `2.3525204118543076e-15` versus `2e-9`.

All eight former ITER025A counterexamples now pass without exclusion:

| k | twice-j | ITER026 direct-source residual | ITER025A legacy residual in ITER026 null comparator |
|---:|---:|---:|---:|
| 6 | 6 | `1.1801832636420706e-15` | `2.000000000000003` |
| 7 | 7 | `1.0532500405730103e-15` | `2.0000000000000004` |
| 9 | 9 | `8.455206652451151e-16` | `2.0` |
| 10 | 8 | `1.0129834521696388e-15` | `1.210000667412112` |
| 10 | 9 | `1.8385843027689748e-15` | `1.4389414028445209` |
| 11 | 9 | `1.0778315928076987e-15` | `1.201485751692281` |
| 12 | 9 | `1.89247439205462e-15` | `1.0669863302706892` |
| 12 | 10 | `1.217454592664719e-15` | `1.1948152457885841` |

The legacy comparator was not used in constructing or tuning `D_src`.

## Independent four-valent lane

PASS.

- held-out levels present exactly as frozen: `k = 7,9,11`
- global max residual: `8.052062385546474e-13` versus `5e-8`
- the largest residual is the high-spin k=12 `(6,6,6,6)` panel and remains more than four orders of magnitude below threshold
- k=12 `(8,4,8,4)` residual: `1.7455869654730213e-13`
- held-out panels are at approximately `1e-15` scale.

## Null/adversarial lane

PASS: all three frozen structural wrong controls are decisively detected (`>1e-6`).

- omit output magnetic reversal `J_c`: residual `0.8342035043686545`
- force source sign `+1` where the source requires `-1`: residual `1.4322826978446357`
- omit graph `ba -> ab` tensor-order permutation: residual `1.0111494534766454`

The same lane independently re-ran the frozen legacy ITER025A construction on all eight prior counterexamples and reproduced its large residuals. Thus the new PASS is not explained by dropping difficult cases, relaxing thresholds, or changing the comparator.

## Adversarial interpretation

The evidence rejects the hypothesis that the ITER025A high/root-boundary cup failures reveal an intrinsic breakdown of the target qbar duality over the tested root-of-unity simple-object range. The exact same frozen counterexamples pass at numerical-noise scale when qbar is transported directly by the explicit source q<->qbar identity and the source-fixed singlet gauge.

The evidence instead localizes the ITER025A failure to its particular independent inverse-parameter/reversed-order highest-weight construction: that construction can satisfy its internal algebraic normalization while selecting a channel basis/gauge not globally compatible with the source graphical duality conventions.

This localization is scoped to RC-006 and does not assert a universal quantum-group convention or any cross-school principle.

## New structural fact

For the audited RC-006 source chain, qbar is not safely reconstructed as an independently solved inverse-q intertwiner plus a posterior source sign normalization. The source relation acts as a nontrivial representation/basis identification: transporting the already source-gauged q-CG tensor through the explicit q<->qbar magnetic-index identity is necessary for globally coherent cap/cup and 4-valent graphical composition across the tested root-of-unity domain.

## Authorization consequence

Set:

`eq27_component_reconstruction_prereg_allowed=true`.

This authorizes only a **new separately preregistered bounded Eq.(27) component translation/contraction** using the now validated source-direct qbar primitive, the already validated q-CG/cap/cup primitives, and the previously source-qualified R/R^-1 convention.

Still false / unauthorized:

- `iter012_retry_authorized`
- `eq29_amplitude_authorized`
- `one_step_tnr_authorized`
- `bridge_credit`
- `candidate_theory_authorized`
- `preferred_alpha_found`
- `new_physics_found`
- `ALL_KNOWN_SCHOOLS_FAIL`
- `NEW_QG_THEORY_REQUIRED`
- `UNIVERSAL_BRIDGE_FOUND`

Candidate theory remains `UNFORMED`.
