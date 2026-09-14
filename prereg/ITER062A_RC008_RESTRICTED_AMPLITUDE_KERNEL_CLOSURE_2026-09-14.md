# ITER062A — RC008 restricted amplitude-kernel closure preregistration

Date frozen: 2026-09-14
Scope: RC008 only — symmetry-restricted Riemannian EPRL-FK quantum-cuboid / hypercuboid sector.
Parent authority gate: ITER061 PASS (`RC008_COMPANION_REFINEMENT_COMPLEX_GLUING_AUTHORITY_COMPLETE`).

## Purpose

This is the first executable subgate of `RC008_RESTRICTED_HYPERCUBOID_COARSE_FINE_AMPLITUDE_RECONSTRUCTION`. It tests whether the exact source formulas needed for a source-faithful coarse/fine numerical reconstruction can be closed into an executable kernel without inventing any missing factor, measure, normalization, gluing rule, or observable.

A PASS here authorizes a separately frozen numerical reconstruction gate. It is not itself reproduction of the coarse/fine amplitude, alpha flow, fixed point, full EPRL/FK refinement, Lorentzian refinement, or a cross-school bridge.

## Frozen authorities

Primary source: Bahr & Steinhaus, arXiv:1508.07961, validated ITER006 source snapshot `QuantumCuboids_article.tex`, SHA256 `b7e0690f32cb7cc56f4e64cf5d1f7bc9da54405ed7275d28d4d97a35a148a8ee`.

Renormalization/dependency source: Bahr & Steinhaus, arXiv:1701.02311, validated ITER006 dependency snapshot `QuantumCuboidsLong_article.tex`. The workflow must recover and record its exact SHA256 and must reject a source mismatch against the validated ITER006 metadata/artifacts rather than silently accepting a different source.

Companion complex/gluing authority: ITER061 corrected run `34869227590`, aggregate artifact `10357629198`, digest `sha256:b3521aacdb952c45e74feaaae29a7fcbe3e6aa5a2f9c0d2489185f0d1ecf4273`.

Frozen source equations already qualified by ITER006 include:

- `Eq:VertexDefinition`: Lorentzian/EPRL vertex-definition snapshot used only as provenance context; no Lorentzian claim is imported into RC008.
- `Eq:AmplitudeIntegral`: state-sum face/edge/vertex product.
- `Eq:AsymptoticStateSum`: asymptotic vertex integral.
- `Eq:EmbeddingMaps`: `iota_{b'b}: H_b -> H_{b'}` with composition law.
- `Eq:Observable`: normalized embedded observable comparison.
- `Eq:RenormalizedAmplitude`: restricted hypercuboid renormalized amplitude, including the twelve internal integrations over `k_i^1,k_i^2 in [0,2j_i]`, the dimension factors, and product over 16 refined vertices.

## Frozen reconstruction object

The successor numerical gate is allowed only if this subgate source-closes all symbols appearing in `Eq:RenormalizedAmplitude` that affect numerical values, including at minimum:

1. the explicit definition of the dressed/asymptotic restricted vertex factor denoted by `\hat{\mathcal A}^{(\alpha)}_{\mathfrak n}` (or source-equivalent notation);
2. every face/edge/dimension factor entering that object, including `d_W` if used;
3. alpha dependence and any fixed source normalization retained in the published calculation;
4. the 16-vertex refined-complex indexing/gluing relation and the mapping from boundary `j_1,...,j_6` plus internal `k_i^1,k_i^2` to each refined vertex;
5. the fixed coarse-boundary prescription and geometric embedding relation supplied by the qualified ITER061 source object;
6. the exact 4-volume observable used for the coarse/fine comparison, including normalization required for variance;
7. all source-stated integration/summation domains and measure factors.

No unspecified factor may be replaced by 1, absorbed into an arbitrary proportionality constant if it affects normalized observables, or supplied from generic spin-foam practice.

## Frozen lanes

Run independently with `fail-fast: false`:

- `dependency-source-identity`: recover the exact arXiv:1701.02311 source archive/file, emit hash/provenance, and verify source identity against durable ITER006 metadata.
- `vertex-kernel-closure`: extract the complete formula chain defining the restricted dressed/asymptotic vertex and all numerical dependencies.
- `renormalized-amplitude-closure`: extract `Eq:RenormalizedAmplitude`, integration domains, dimension factors and the 16-vertex product; build a machine-readable symbol/dependency graph.
- `gluing-index-closure`: source-check that every boundary/internal variable required by the 16 refined vertices has a non-ambiguous source-defined incidence/index assignment compatible with ITER061.
- `observable-closure`: extract the source-defined 4-volume observable/variance and fixed-boundary comparison needed for the RG matching.
- `adversarial-null`: mutate one required incidence/domain/dependency in a temporary copy; the validator must detect the mutation. This lane is a control and can never rescue a failed scientific lane.

## PASS predicate

`SCIENTIFIC PASS — RC008_RESTRICTED_AMPLITUDE_KERNEL_SOURCE_CLOSED` iff all five scientific closure lanes are terminal PASS, all required source snippets/hashes/dependency graphs are emitted as artifacts, no value-affecting symbol is unresolved, and the adversarial-null lane detects every frozen mutation.

## BLOCKED predicate

`SCOPED BLOCKED — RC008_RESTRICTED_AMPLITUDE_KERNEL_INCOMPLETE_SOURCE_OBJECT` if the exact qualified source lacks or leaves ambiguous any value-affecting kernel, measure, normalization, incidence/gluing relation, fixed-boundary prescription, or 4-volume observable required for numerical reconstruction.

## Infrastructure / implementation classification

Network/rate-limit/archive extraction failures before predicates are `INFRASTRUCTURE FAIL PRE-SCIENCE`. Parser false negatives or validator defects are `INVALID IMPLEMENTATION` and may receive a minimal parser-only repair without changing this preregistration. Green CI alone is never scientific PASS.

## Numerical successor frozen now

Only after scientific PASS may ITER062B be preregistered. ITER062B must freeze before evaluation: exact executable formulas from these artifacts, boundary state, coarse/fine complexes, embedding relation, all internal variables/domains, an alpha panel chosen prospectively from source-defined or explicitly diagnostic values, normalization, 4-volume observable, quadrature/sampling method, numerical tolerances, held-out boundary states, and adversarial/null controls. No threshold may be changed after results are seen.

## Claim locks

A PASS gives only source/executable-kernel closure inside the restricted Riemannian quantum-cuboid sector. It gives zero bridge credit and does not authorize `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`, a candidate theory, a candidate action/Hamiltonian/field equations, full EPRL/FK refinement, or Lorentzian refinement.
