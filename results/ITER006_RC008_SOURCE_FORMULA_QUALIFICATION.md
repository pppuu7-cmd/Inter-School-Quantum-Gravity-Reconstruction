# ITERATION 006 — RC008 official-source formula qualification

Date: 2026-09-12

## Classification

`PASS_SOURCE_FORMULA_QUALIFICATION + PASS_DEPENDENCY_CLOSURE + PASS_STRUCTURAL_AST + PASS_SOURCE_DERIVED_HESSIAN_KERNEL + PASS_EQ4VOLUME_REFINEMENT_PREREQUISITE / AMPLITUDE_REPRODUCTION_OPEN`

These gates qualify official-source implementation inputs, the source-derived stationary-phase Hessian kernel, and the source-native hypercuboid 4-volume/refinement observable prerequisite. They do not themselves reproduce the full vertex amplitude, volume-variance RG flow, fixed point, or held-out transport result.

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

Classification: `PASS_SOURCE_DEPENDENCY_CLOSURE_ONLY`. This authorizes implementation sequencing; it is not amplitude evidence.

## Source equation structural AST — PASS prerequisite

Prospective computation commit `977580d1dadf408cf8a35940483c26ba07d0d9c4`; workflow/head `15bf47a5450411b1fa27d0c51f8f0d24929907ff`; authoritative run `34698546988`.

Six independent lanes passed: `Eq:VertexDefinition`, `Eq:AmplitudeIntegral`, `Eq:AsymptoticStateSum`, `Eq:4Volume`, `Eq:EmbeddingMaps`, and `Eq:ExpectationValueCoarseGraining`; aggregate job `103566152634`, artifact `10299224016`, digest `sha256:fa0ff9253b0fd6714f3a8d39d233585497bd65c2bf8ae43ca39eeb1d956c2bb4`, `frozen_gate_pass=true`.

Classification: `PASS_MACHINE_READABLE_SOURCE_STRUCTURE_ONLY`.

## Exact source snapshots — PASS implementation input

Primary equation snapshot run `34698656157`, head `0186308bc065a371de764c04b96d8147a56057d9`, aggregate job `103566457190`, artifact `10300010002`, digest `sha256:92e656e4e1d8b9591d6c27586330fa9c2e5a3ca6c60895c96587e51229716469`, passed. Dependency snapshot run `34698849889`, aggregate job `103566977773`, artifact `10299144588`, also passed. These exact normalized equations and hashes are implementation inputs only.

## Source-derived stationary-phase Hessian kernel — SCIENTIFIC PASS prerequisite

Prospective script commit `5ee9caaa384d7794e1ecbac57f9f4c2583c43e3b`; workflow/head `026838089ce084555c9d9b2e7d225a5c48ba72f2`; authoritative run `34698968902`.

Eight independent fixtures plus aggregate completed. Aggregate job `103567272522`, artifact `10300145140`, digest `sha256:5512bf1cc4ec5d79c586a013d2b96897309c9de992945d2ed79a9e7de974f72d` records:

- `lane_count = 8`, `passes = 8`;
- `worst_symmetry_error = 0.0` against frozen `1e-12`;
- `worst_logdet_scaling_error = 1.0658141036401503e-14` against frozen `1e-9`;
- exact source-implied linear homogeneity of the gauge-fixed 21-dimensional Hessian is also required lane-by-lane.

Classification: `PASS_SOURCE_DERIVED_STATIONARY_PHASE_HESSIAN_KERNEL_HOMOGENEITY_ONLY`.

This qualifies the pinned `Eq:OffDiagonalHessian` kernel and the `det H ~ lambda^21` stationary-phase scaling prerequisite. It is explicitly not a full vertex-amplitude reproduction and gives no bridge credit by itself.

## Eq:4Volume hypercuboid refinement prerequisite — SCIENTIFIC PASS prerequisite

Prospective computation commit `f2f80d0b5130c4c9aa39842b9e5fab09fa75c8ae`; workflow/head `7a8390780e84a4513c5bc82d1a01ed28264b170a`; authoritative run `34699223422`.

All 24 independently seeded anisotropic hypercuboid lanes and aggregate job `103567987044` passed the frozen gate. Aggregate artifact `10300335297`, digest `sha256:ef13f1cfc8ef579dcd84d2ef9410b97a4a1f3c1f2dae50eb0034ae0bca19aeb6`, records:

- `lane_count = 24`, `passes = 24`, `frozen_gate_pass = true`;
- worst `Eq:4Volume` geometric consistency error `2.045697690782737e-16` versus frozen `1e-12`;
- worst uniform 4-volume homogeneity error `5.875395533044386e-16` versus frozen `1e-12`;
- worst non-retuned axis-slicing/refinement conservation error `5.203796573403926e-16` versus frozen `1e-12`;
- minimum independent-face-area negative-control shift `0.01639635681485324` versus frozen minimum `1e-3`.

Classification: `PASS_SOURCE_FAITHFUL_HYPERCUBOID_VOLUME_REFINEMENT_PREREQUISITE_ONLY`.

This closes the geometric observable/refinement prerequisite for the pinned `Eq:4Volume`; it is not the published volume-variance calculation and does not reproduce the restricted EPRL-FK vertex amplitude or the `alpha' -> alpha` RG map.

## Scientific implication

RC008 source discovery, Hessian-kernel qualification, and the source-native hypercuboid volume/refinement prerequisite are no longer the bottleneck. The next decisive layer is the actual restricted hypercuboid amplitude: implement it from the pinned source equations without fitting published `alpha_*`, reproduce at least two coarse/refined boundary-state calculations, freeze the inferred `alpha' -> alpha` map, and only then apply it to a held-out boundary state without retuning.

## Claim locks

- source qualification/dependency/AST/snapshots/Hessian/volume prerequisite are not full amplitude reproduction;
- the quantum-cuboid sector is a severe EPRL-FK truncation and not full quantum gravity;
- published fixed-point values are not to be used as fit targets for executable reproduction;
- no `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, candidate theory, or continuum-limit claim follows.
