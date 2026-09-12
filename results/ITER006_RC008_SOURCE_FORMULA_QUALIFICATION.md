# ITERATION 006 — RC008 official-source formula qualification

Date: 2026-09-12

## Classification

`PASS_SOURCE_FORMULA_QUALIFICATION_ONLY / AMPLITUDE_REPRODUCTION_OPEN`

This gate qualifies the official source material needed for the quantum-cuboid/hypercuboid amplitude/refinement reproduction. It does not itself recompute an amplitude, volume variance, RG flow, fixed point, or held-out transport result.

## Initial technical failure

Initial run `34697983144` used an extractor that recognized only a narrow subset of TeX display environments. All frozen role keywords were present, but the amplitude source `1508.07961` and renormalization source `1701.02311` returned zero candidate equations. The phase source `1605.07649` passed.

Classification: `INFRASTRUCTURE/IMPLEMENTATION FAIL`, because the failure occurred in TeX syntax recognition before any physical quantity or frozen scientific threshold was evaluated.

The minimal fix broadened only source-native display syntax recognition to include `eqnarray`, `alignat`, `split`, `IEEEeqnarray`, `\\[...\\]` and `$$...$$` in addition to the already supported environments. Frozen source qualification remained: every role must contain its preregistered keywords and at least one equation-bearing source region.

Fix commit: `8ce783247216f600195b0a4cfd6c179ac7506e55`.

## Authoritative rerun

Run `34698110637` — all three independent source lanes plus aggregate completed successfully.

Jobs:

- `103564997995` — arXiv `1508.07961`, amplitude role — success;
- `103564997792` — arXiv `1605.07649`, phase role — success;
- `103564997981` — arXiv `1701.02311`, renormalization role — success;
- aggregate `103565184050` — success.

Artifacts:

- amplitude `10299421571`, digest `sha256:fd2aeb91ccca82e0c617e985698d8ad37b18fd0fc580d1bd489102bd9151edd8`;
- phase `10298904022`, digest `sha256:8a7caf32f26bd4ac9193df94f6d1d79e6cd50f8e1b4712595936d5d7119ba61f`;
- renormalization `10299636244`, digest `sha256:8e0a1a67c7d4e1553d90121909791493cb4131903de8c195e8b610bde3736f38`;
- aggregate `10298993915`, digest `sha256:8a74186a001f7b5730af162033043704975ad0b3d6deed842992127741594c0f`.

Aggregate frozen gate: `lane_count=3`, roles exactly `amplitude/phase/renormalization`, `frozen_gate_pass=true`.

The amplitude source inventory found 30 candidate equation regions in `QuantumCuboids_article.tex`, including source labels `Eq:VertexDefinition`, `Eq:AmplitudeIntegral`, `Eq:ComplexAction`, `Eq:OffDiagonalHessian`, `Eq:AsymptoticStateSum`, `Eq:4Volume`, and `Eq:QuantumCuboid`.

The renormalization source inventory found 27 candidate equation regions in `QuantumCuboidsLong_article.tex`, including `Eq:EmbeddingMaps`, `Eq:RenormalizedAmplitude_abstract`, `Eq:Observable`, `Eq:RenormalizedAmplitude`, `Eq:FixedPoint01`, `Eq:FixedPoint02`, and `Eq:ExpectationValueCoarseGraining`.

## Scientific implication

RC008 now has a source-authorized formula inventory sufficient to begin an executable reconstruction without fitting to previously audited fixed-point values. The next allowed RC008 step is to extract the dependency closure for the labelled amplitude, embedding, observable and expectation-value formulas, implement the restricted hypercuboid amplitude/variance calculation, reproduce at least two source boundary states, freeze the resulting `alpha' -> alpha` map, then test a held-out boundary state without retuning.

## Claim locks

- source qualification is not amplitude reproduction;
- the quantum-cuboid sector is a severe EPRL-FK truncation and not full quantum gravity;
- no `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, candidate theory, or continuum-limit claim follows.
