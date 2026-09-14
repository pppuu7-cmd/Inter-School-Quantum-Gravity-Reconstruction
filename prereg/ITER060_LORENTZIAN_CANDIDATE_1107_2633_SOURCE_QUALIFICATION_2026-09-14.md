# ITER060 — Lorentzian candidate 1107.2633 exact-source qualification

Date: 2026-09-14

## Frozen objective
Qualify metadata-discovery candidate arXiv:1107.2633 (Francesca Vidotto, *Many-nodes/many-links spinfoam: the homogeneous and isotropic case*) as a possible Lorentzian EPRL refinement/coarse-graining authority for the active multi-vertex bridge. This gate is source-authority only. It does not derive a refinement map, amplitude equality, bridge credit, or candidate theory.

## Frozen provenance
Candidate arose prospectively from ITER059 lane `lorentzian-eprl-refinement`, artifact 10342046556, run 34823751928, attempt 3. Metadata flags were Lorentzian-EPRL=true, boundary-amplitude-map=true, map-transform=false, simplicial-multivertex=false. ITER059 aggregate remained infrastructure-incomplete because three independent lanes failed before science.

## Frozen lanes
1. `exact-source`: retrieve the exact arXiv source/abstract for 1107.2633 and record cryptographic hashes and title/author identity.
2. `refinement-language`: source-only audit for explicit graph refinement/coarse/fine/embedding/cylindrical-consistency/map language, preserving exact snippets only as short evidence.
3. `object-match`: determine whether the source defines BOTH a fine Lorentzian EPRL object and a distinct coarse object together with an explicit fine↔coarse or refinement map applicable to the active simplicial/multi-vertex setting.
4. `null-controls`: reject metadata-only inference, equal-support/equal-semiclassical-limit inference, and graph-size comparison as substitutes for an explicit refinement map.

## Frozen scientific gate
PASS only if the exact source explicitly supplies all of:
- Lorentzian EPRL/FK/KKL amplitude/object identity relevant to the candidate;
- a distinct coarse and fine/refined object or boundary graph pair;
- an explicit map/embedding/refinement transformation connecting those objects;
- sufficient source detail to identify the map without fitting, convention choice, or numerical matching;
- applicability to the active simplicial/multi-vertex refinement question, not merely a homogeneous/isotropic truncation with common large-j support.

If Lorentzian EPRL amplitudes on multiple graphs are discussed but only common support/semiclassical behavior is established, classify `SCOPED_BLOCKED_NO_EXPLICIT_REFINEMENT_MAP`.
If source retrieval itself fails, classify `INFRASTRUCTURE_FAIL_PRE_SCIENCE`.
If the source explicitly contradicts the required map interpretation, classify `SCIENTIFIC_FAIL_AS_REFINEMENT_AUTHORITY_SCOPED` while preserving the negative result.

## Locks
No threshold or criterion may be weakened after source inspection. No bridge credit, no BRIDGE_DERIVED, no NEW_PHYSICS_FOUND, no candidate-theory construction. Candidate theory remains 0/UNFORMED. ITER059 failed discovery lanes may continue independently; ITER060 qualification does not imply ITER059 saturation or completion.
