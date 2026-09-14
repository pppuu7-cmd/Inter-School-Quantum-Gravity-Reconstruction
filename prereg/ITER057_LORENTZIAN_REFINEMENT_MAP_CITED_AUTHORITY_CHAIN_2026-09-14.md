# Preregistration — ITER057 Lorentzian refinement-map cited-authority chain

Date frozen: 2026-09-14

## Inherited terminal state

ITER056 is terminal **SCOPED BLOCKED — `LORENTZIAN_REFINEMENT_MAP_SOURCE_AUTHORITY_BLOCKED`**: the exact author repository pins a fine EPRL 5→1 / vertex-renormalization object, but no separately qualified coarse EPRL object and no explicit refinement/coarse-graining map were established.

ITER056 is not retrofitted and no amplitude calculation is authorized by this successor.

## Scientific question

Does the explicit cited/source authority chain around the Lorentzian EPRL vertex-renormalization calculation contain a model-matched, variable-level coarse/fine map and both corresponding objects that were absent from the implementation repository?

This is a source-authority gate only. It must remain amplitude-blind.

## Frozen source panel

Primary source:

- arXiv `2302.00072` — Donà & Frisoni, *Summing bulk quantum numbers with Monte Carlo in spin foam theories*.

Prospectively fixed candidate authority sources to test only if they are actually connected by citation/subject provenance:

- arXiv `1803.00835` — EPRL-FK infrared divergences / self-energy and vertex-renormalization context;
- arXiv `0810.1714` — self-energy and five-vertex radiative correction context;
- arXiv `1903.12624` — numerical Lorentzian EPRL vertex-amplitude conventions/runtime context;
- arXiv `1412.8247` — analytic 5→1 Pachner/vertex-renormalization equation in a **Riemannian holomorphic** model, included strictly as a model-mismatch control and never sufficient by itself to qualify a Lorentzian EPRL map.

No source may be added after seeing results inside ITER057.

## Required authority object

AUTHORITY PASS requires all of the following in a Lorentzian EPRL-compatible source chain:

1. a separately identifiable fine 5→1 object;
2. a separately identifiable coarse/single-vertex object;
3. an explicit variable-level correspondence/embedding/coarse-graining/refinement relation connecting their boundary data and required weights/normalization;
4. provenance showing the map is meant for the same Lorentzian EPRL object class, not merely BF, Riemannian holomorphic, asymptotic, or analogy-level evidence.

A statement that a 5→1 expression is a “vertex renormalization” or a plotted scaling relation is not sufficient.

## Independent lanes

Run with `fail-fast:false`:

1. `primary-source-chain`: retrieve exact arXiv source for `2302.00072`, inventory its source files and references relevant to vertex renormalization / 5→1 / radiative correction, and emit exact hashes plus citation keys/IDs.
2. `eprlfk-1803`: retrieve `1803.00835` and extract exact passages/equations defining the vertex-renormalization object and any coarse comparison/map.
3. `radiative-0810`: same for `0810.1714`, with explicit model-compatibility labeling.
4. `lorentzian-vertex-1903`: search `1903.12624` for any explicit coarse/fine or embedding map; runtime/vertex conventions alone do not qualify.
5. `holomorphic-control-1412`: extract the 5→1 renormalization relation but mark it non-qualifying unless a source itself supplies an explicit Lorentzian-EPRL transfer theorem (none may be inferred by us).
6. `null-controls`: reject keyword-only matches, BF/Riemannian substitution, asymptotic analogy, fitted rescaling, visual equality, and output-dependent source selection.

## Frozen classification

**AUTHORITY PASS — `LORENTZIAN_REFINEMENT_MAP_CITED_AUTHORITY_PASS_SCOPED`** only if an exact Lorentzian EPRL source chain pins fine object + coarse object + explicit map + normalization/weight convention.

**SCOPED BLOCKED — `LORENTZIAN_REFINEMENT_MAP_CITED_AUTHORITY_BLOCKED`** if the fixed sources are retrievable but the required Lorentzian EPRL map is absent or only analogy-level/model-mismatched.

`INFRASTRUCTURE FAIL` only for source retrieval/parsing failure before authority evaluation. Green CI is not scientific PASS.

## Locks

No amplitude execution, no shell-convergence escalation, no map fitting, no threshold changes, and no candidate-theory construction.

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory `UNFORMED / 0%`.