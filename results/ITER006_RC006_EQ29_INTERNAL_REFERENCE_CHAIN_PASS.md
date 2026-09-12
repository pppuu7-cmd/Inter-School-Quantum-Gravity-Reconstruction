# ITERATION 006 — RC006 Eq.(29) internal source reference-chain

Date: 2026-09-12

## Provenance

Prospective script commit: `b5ae442a985e1013a14c6b2fd179eb96b4a28815`  
Workflow/head: `40cd1ffbe8fce3a10e7e4481189a472e1b134cd3`  
Authoritative run: `34699660419`  
Aggregate job: `103569079457`  
Aggregate artifact: `10299976524`  
Aggregate digest: `sha256:fbb40074f54c69b8c53b73b88a44d5b29ba1523e0342e0ccb05ee65463a94d54`

This gate was frozen after the independent TeX-structure audit established that the official arXiv source is monolithic but has machine-readable internal headings, labels/references, graphics, Eq.(29) and recoupling components. It is a distinct source object and does not relax either the failed lexical gate or the failed include-graph gate.

## Raw result

All six independent roles passed the frozen gate:

- `eq29_local_refs`;
- `recoupling_local_labels`;
- `eq29_figure_links`;
- `eq29_equation_links`;
- `recoupling_equation_links`;
- `shared_reference_component`.

Aggregate: `6/6 PASS`, `all_pass=true`.

The shared-reference lane found 13 source labels/names present in both the Eq.(29)-local reference set and the recoupling reference/label set:

- `app:EPRL-diagram`;
- `app:EPRL-norm`;
- `app:graph`;
- `eq:BC-3-int`;
- `eq:BC-3-valent`;
- `eq:eprl-3-valent`;
- `fig:eprl-plots`;
- `fig:phase-lines`;
- `fig:sv-plots`;
- `sec:intertwiners`;
- `sec:optimization`;
- `sec:qg-models`;
- `sec:scope`.

The shared-component artifact is `10299298419`, digest `sha256:03448e13e3bc7b56f904e5c33bf25c137921cfed81c19abf2099b16f07b0bd1f`.

## Scientific classification

`PASS_INTERNAL_SOURCE_REFERENCE_CHAIN_OBJECT_ONLY`.

This is a real source-authority prerequisite: Eq.(29) and the recoupling/EPRL derivation are demonstrably connected through explicit internal labels/references rather than picture proximity. It materially narrows the mapping problem to a finite set of named source anchors.

It is **not yet** a unique oriented/braided contraction map. A shared reference component can contain multiple identities and diagrams, and the exact tensor-index ordering/crossing prescription must still be extracted from the definitions of those named anchors before a numerical Eq.(29) amplitude is authorized.

## Next allowed gate

Build a prospectively frozen named-anchor dependency graph from the exact definitions/contexts of the shared source anchors, with separate lanes for EPRL diagram, normalization, graph definition, 3-valent EPRL/BC identities and recoupling-basis/6j identities. The gate must establish exact source dependency closure and preserve ambiguity if more than one contraction ordering remains. Only an unambiguous contraction-ready mapping may unlock the minimal `k=12, gamma=1/3` Eq.(29) amplitude.

## Claim locks

No Eq.(29) numerical amplitude, Appendix-C TNR flow, refinement bridge, continuum limit, `BRIDGE_DERIVED`, new physics, or candidate theory follows from this PASS.
