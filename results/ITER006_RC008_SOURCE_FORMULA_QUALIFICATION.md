# ITERATION 006 — RC008 official-source formula qualification

Date: 2026-09-12

## Classification

`PASS_SOURCE_FORMULA_QUALIFICATION + PASS_DEPENDENCY_CLOSURE + PASS_STRUCTURAL_AST / AMPLITUDE_REPRODUCTION_OPEN`

These gates qualify official-source implementation inputs for quantum-cuboid/hypercuboid amplitude/refinement reconstruction. They do not themselves recompute an amplitude, volume variance, RG flow, fixed point, or held-out transport result.

## Initial technical failure and source qualification

Initial run `34697983144` used an extractor that recognized only a narrow subset of TeX display environments. All frozen role keywords were present, but the amplitude source `1508.07961` and renormalization source `1701.02311` returned zero candidate equations. The phase source `1605.07649` passed.

Classification: `INFRASTRUCTURE/IMPLEMENTATION FAIL`, because the failure occurred in TeX syntax recognition before any physical quantity or frozen scientific threshold was evaluated.

The minimal fix broadened only source-native display syntax recognition. Frozen source qualification remained unchanged. Fix commit: `8ce783247216f600195b0a4cfd6c179ac7506e55`.

Authoritative rerun `34698110637` passed all three source lanes plus aggregate job `103565184050`; aggregate artifact `10298993915`, digest `sha256:8a74186a001f7b5730af162033043704975ad0b3d6deed842992127741594c0f`.

The amplitude source inventory found 30 candidate equation regions in `QuantumCuboids_article.tex`, including `Eq:VertexDefinition`, `Eq:AmplitudeIntegral`, `Eq:ComplexAction`, `Eq:OffDiagonalHessian`, `Eq:AsymptoticStateSum`, `Eq:4Volume`, and `Eq:QuantumCuboid`. The renormalization source inventory found 27 candidate regions in `QuantumCuboidsLong_article.tex`, including `Eq:EmbeddingMaps`, `Eq:RenormalizedAmplitude_abstract`, `Eq:Observable`, `Eq:RenormalizedAmplitude`, `Eq:FixedPoint01`, `Eq:FixedPoint02`, and `Eq:ExpectationValueCoarseGraining`.

Classification: `PASS_SOURCE_FORMULA_QUALIFICATION_ONLY`.

## Labelled formula dependency closure — PASS prerequisite

Prospective computation commit `874d964f1cbfd7ae945a3c19ce9e633321359eeb`; workflow/head `1fc3d49f33776427bb287d79c2b91806ec97c3f7`; authoritative run `34698443872`.

Jobs:

- `103565857971` — amplitude dependency closure — success;
- `103565858139` — observable closure — success;
- `103565858207` — embedding closure — success;
- `103565858096` — matching/fixed-point closure — success;
- aggregate `103565886990` — success.

Aggregate artifact `10298714927`, digest `sha256:beb68bc08e2db402bf0e97648e15a7d1e3b8733f2ae91a45d947c6fcdcfd2833`, records `lane_count=4`, exact roles `amplitude/observable/embedding/matching`, and `frozen_gate_pass=true`.

The amplitude raw artifact `10299491893`, digest `sha256:5b7485057682c3ddeeb45e76d4c47d38c40f446479ea997db1737fef9ef112db`, verifies all five frozen source labels and their immediate dependency sets. For example `Eq:AmplitudeIntegral` source context references `Eq:ComplexAction`, `Eq:QuantumCuboid`, and `Eq:CoherentInterwiner`; `Eq:AsymptoticStateSum` references `Eq:OffDiagonalHessian`, `Eq:QuantumCuboid`, and `Eq:SolutionVector`.

Classification: `PASS_SOURCE_DEPENDENCY_CLOSURE_ONLY`. This authorizes implementation sequencing; it is not amplitude evidence.

## Source equation structural AST — PASS prerequisite

Prospective computation commit `977580d1dadf408cf8a35940483c26ba07d0d9c4`; workflow/head `15bf47a5450411b1fa27d0c51f8f0d24929907ff`; authoritative run `34698546988`.

Six independent lanes passed:

- job `103566125239` — `Eq:VertexDefinition`;
- `103566125097` — `Eq:AmplitudeIntegral`;
- `103566125194` — `Eq:AsymptoticStateSum`;
- `103566125229` — `Eq:4Volume`;
- `103566125248` — `Eq:EmbeddingMaps`;
- `103566125266` — `Eq:ExpectationValueCoarseGraining`;
- aggregate `103566152634`.

Aggregate artifact `10299224016`, digest `sha256:fa0ff9253b0fd6714f3a8d39d233585497bd65c2bf8ae43ca39eeb1d956c2bb4`, records `lane_count=6`, `all_pass=true`, `frozen_gate_pass=true`.

Classification: `PASS_MACHINE_READABLE_SOURCE_STRUCTURE_ONLY`. It is the final structural/provenance layer before converting the selected equations into an executable restricted-hypercuboid kernel.

## Active implementation input extraction

Exact normalized equation snapshots were prospectively frozen after the dependency/AST gates. Computation commit `78a7290278a96f14865c3e0dc80c2e7f69021395`; workflow/head `0186308bc065a371de764c04b96d8147a56057d9`; run `34698656157`.

Six independent lanes extract exact normalized source equations for `Eq:VertexDefinition`, `Eq:QuantumCuboid`, `Eq:AmplitudeIntegral`, `Eq:AsymptoticStateSum`, `Eq:4Volume`, and `Eq:ExpectationValueCoarseGraining`, recording source and equation hashes. These artifacts are implementation inputs only and cannot be counted as scientific amplitude/refinement evidence.

## Scientific implication

RC008 source discovery is no longer the bottleneck. The next decisive layer is executable: implement the restricted hypercuboid amplitude and coarse/refined volume observable from the pinned source equations, reproduce at least two boundary-state calculations, freeze the inferred `alpha' -> alpha` map, and only then apply it to a held-out boundary state without retuning.

## Claim locks

- source qualification/dependency/AST/snapshots are not amplitude reproduction;
- the quantum-cuboid sector is a severe EPRL-FK truncation and not full quantum gravity;
- published fixed-point values are not to be used as fit targets for the executable reproduction;
- no `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, candidate theory, or continuum-limit claim follows.
