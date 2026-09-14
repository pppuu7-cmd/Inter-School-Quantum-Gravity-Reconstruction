# ITER062A — RC008 restricted amplitude-kernel source closure

Date: 2026-09-14

## Terminal scientific verdict

**SCIENTIFIC PASS — `RC008_RESTRICTED_AMPLITUDE_KERNEL_SOURCE_CLOSED`**

Scope is strictly the symmetry-restricted Riemannian EPRL-FK quantum-cuboid / hypercuboid construction. This PASS authorizes a separately preregistered restricted numerical reconstruction gate only. It gives zero bridge credit and does not establish full EPRL/FK refinement, Lorentzian refinement, a continuum limit, new physics, or a candidate theory.

## Frozen preregistration and provenance correction

Parent preregistration commit: `1fae03306aa134c06bdc0c486971cd2e7264fb97`.

Initial implementation commit: `50d22f2baa8370df34db9a12830d898ae2d9908e`.
Initial workflow/head: `1e6ad0d412e35020e10969f58d4ccac464d78cb0`.
Initial run: `34872500144`.

Run 1 was terminalized separately as **INVALID IMPLEMENTATION — source-set incomplete + adversarial replacement escape**, report commit `b7c3753ff288f86a82c093ded442a5c4105c6385`. Its emitted aggregate must not be treated as a scientific BLOCKED result.

The parent preregistration also transcribed the primary-source raw-file SHA incorrectly. Pre-existing ITER006 artifacts from run `34698656157` already fixed the exact official arXiv:1508.07961 `QuantumCuboids_article.tex` SHA256 as `ba973b02a05688c2b122c95a111b70b0fe03a126fac399b073725574afc7358b`: vertex snapshot artifact `10299427022` and 4-volume snapshot artifact `10299576801` independently contain this same raw-file hash. The provenance-only correction is durable at commit `044b756a77689c9b9835b058d39a8733a0984061`. No scientific predicate, threshold, formula, measure, normalization, lane or claim ceiling changed.

Dependency source remains arXiv:1701.02311 / `QuantumCuboidsLong_article.tex`, SHA256 `78415347fa92b1d0bce1bbd4010faeb3cc939c5f5d6b14d72f340138e4c573ef`.

A version probe run `34873206126` was launched while the mistyped hash was still being diagnosed. Its no-match result is obsolete as a scientific source-identity test because the tested target hash was the transcription error. It nevertheless confirmed that arXiv:1508.07961v2/current yields `ba973...`, exactly matching the pre-existing ITER006 source artifact.

## Valid scientific evidence reused from run 1

Dependency source identity:
- job `104071655294`;
- artifact `10358793287`;
- digest `sha256:d702d7bd75feda8ab2eb316ec613339c8f5f6d37477015962e2ddfe5b3c43109`;
- verdict `PASS_SOURCE_IDENTITY`.

Renormalized-amplitude closure:
- job `104071657342`;
- artifact `10359637554`;
- digest `sha256:fb29aa060d60be32592bd845eb6efb9b6cbecfb866c5f3c419cd6b064f02a679`;
- source checks include `Eq:RenormalizedAmplitude`, `d^{24}j`, the 16-vertex product, coarse/fine constraint product, normalization, and alpha-dependent vertex factor;
- verdict `PASS_RENORMALIZED_AMPLITUDE_CLOSURE`.

Gluing/index closure:
- job `104071657213`;
- artifact `10359717623`;
- digest `sha256:b69d7fafec26bee21a55c67cbad9a60519fe5996105650f200037f8e181aaba5`;
- verdict `PASS_GLUING_INDEX_CLOSURE`.

Manual source audit confirms that this is not merely a regex success: the source states that one coarse hypercuboid is subdivided as `2x2x2x2 = 16`, each of the six coarse faces is subdivided into four fine faces, coarse area equals the sum of the four fine areas through the embedding map, and the 16 fine vertex factors are multiplied under the coarse-face constraints. The geometric-sector reduction and the source-defined change from six spin variables per hypercuboid to four edge-length variables are also explicit, including the nontrivial measure/Jacobian warning.

## Repaired affected lanes

### Adversarial null

Parser-only replacement repair commit: `95e1765856b0c6b5317f86b1d74907a75bdb5fdc`.
Null-only workflow commit: `c6bd399667c5a691244141cc6190357a0b28c458`.
Run: `34872664624`.
Job: `104072130213`.
Artifact: `10360205125`.
Digest: `sha256:de4937981020c2688c7529ee1591357bb3ded2792f99e4edc0b34ded17710686`.

Raw result: `PASS_ADVERSARIAL_NULL`, detected `5/5` frozen mutations: remove 16 vertices, remove 24-dimensional measure, remove coarse/fine constraint, remove normalization, replace variance structure.

### Complete primary+dependency source set

Source-set repair implementation commit: `3ac2b58dc77b64baeee4c0ce68502ac7dffcab42`.
Corrected source-set workflow/head: `257b2b1e7266b730915d46e98d28c1dcaa10e984`.
Run: `34873452224`.

Primary source acquisition:
- job `104074755637`;
- artifact `10360195380`;
- digest `sha256:2ee29aaa438b3139dd05769fdcf91ab0b6c278dba530f5e3f8a5aeabdb57eae4`;
- exact primary SHA256 `ba973b02a05688c2b122c95a111b70b0fe03a126fac399b073725574afc7358b`.

Vertex-kernel closure:
- job `104074802935`;
- artifact `10359489242`;
- digest `sha256:dcc2c801c2684fd7acff0083edeb53ae9608ec0bfec6e887b49e0ac28e9e9d2a`;
- emitted verdict `PASS_VERTEX_KERNEL_CLOSURE`.

The raw parser field `hat_definition` by itself is not sufficient evidence because it captured a commented diagnostic ratio. A manual source audit was therefore required before scientific classification. That audit passes independently: the qualified sources explicitly define the face amplitude `A_f=((2j^++1)(2j^-+1))^alpha`, edge amplitude `A_e=1/||Y_e^gamma iota_e||^2`, EPRL-FK hypercuboid vertex group integral, large-j stationary-point/Hessian representation, and the dressed amplitude as the product of quarter-power incident face amplitudes, half-power incident edge amplitudes and the vertex amplitude. The primary source also defines the asymptotic dressed vertex through the full state sum. Thus the value-affecting alpha/face/edge/vertex chain is source-closed; no missing factor is supplied from generic practice.

Observable closure:
- job `104074802865`;
- artifact `10359434451`;
- digest `sha256:a558b7c1f5f378cc3903e324bd65622e427bf90ae03a7861f6c6641b8d88597b`;
- raw checks all true: observable variance, exact 4-volume formula, coarse-graining expectation, fixed-boundary context, alpha-flow context;
- verdict `PASS_OBSERVABLE_CLOSURE`.

The source also defines the normalization counting factor `d_J = binom(2J+3,3)` in the finite-spin normalization appendix and gives the large-lattice normalization form used in the coarse-grained amplitude. The geometric-sector measure is explicitly nontrivial: the source supplies the constraint-surface pullback / `1/cos(theta)` factor and the Jacobian for conversion to edge-length variables. These must be retained in the numerical successor rather than set to unity.

## Gate reconciliation

All five scientific closure lanes required by the preregistration are now source-qualified:

1. dependency/source identity — PASS;
2. vertex-kernel closure — PASS after complete-source exposure and manual source audit;
3. renormalized-amplitude closure — PASS;
4. gluing/index closure — PASS with manual geometry/incidence audit;
5. observable/fixed-boundary closure — PASS after complete-source exposure.

Adversarial null: PASS, `5/5` mutations detected.

Therefore the preregistered PASS predicate is satisfied.

## Readiness change

This closes only the executable-source-kernel prerequisite. It does **not** yet reproduce a coarse/fine numerical observable, alpha flow or fixed point. Overall programme readiness therefore remains `49%` until a numerical/rubric gate closes.

Candidate theory remains **0% / UNFORMED**. `bridge_credit=false`.

## Exact next admissible gate

Preregister and execute `ITER062B_RC008_RESTRICTED_HYPERCUBOID_COARSE_FINE_NUMERICAL_RECONSTRUCTION` with, before evaluation:

- the exact source equations and source hashes above;
- restricted geometric-sector construction only;
- explicit boundary states, including a primary state and held-out states fixed before outputs;
- source-defined coarse/fine complexes and geometric embedding;
- source-defined internal variables, constraints, integration domains and the nontrivial geometric-sector measure/Jacobian;
- source-defined dressed large-j hypercuboid amplitude;
- a prospectively frozen alpha panel;
- normalized 4-volume-variance observable;
- prospective numerical integration method, convergence diagnostics and tolerances;
- non-retuned held-out transport and adversarial/null controls.

A numerical PASS may count only as reproduction inside this restricted Riemannian quantum-cuboid truncation. It cannot by itself produce `BRIDGE_DERIVED`, full EPRL/FK refinement or candidate-theory authorization.
