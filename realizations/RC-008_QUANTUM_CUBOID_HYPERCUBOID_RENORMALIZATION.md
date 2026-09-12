# RC-008 — Quantum-Cuboid Hypercuboidal Spin-Foam Renormalization

Status: `SOURCE_GROUNDED / AMPLITUDE_REFINEMENT_TARGET`  
Family: `F04 spinfoam/LQG`  
Date: 2026-09-12

## Primary sources

- B. Bahr, S. Steinhaus, *Investigation of the Spinfoam Path integral with Quantum Cuboid Intertwiners*, Phys. Rev. D 93, 104029 (2016), arXiv:1508.07961.
- B. Bahr, S. Steinhaus, *Numerical evidence for a phase transition in 4d spin foam quantum gravity*, Phys. Rev. Lett. 117, 141302 (2016), arXiv:1605.07649.
- B. Bahr, S. Steinhaus, *Hypercuboidal renormalization in spin foam quantum gravity*, Phys. Rev. D 95, 126006 (2017), arXiv:1701.02311.
- S. Steinhaus, *Coarse Graining Spin Foam Quantum Gravity — A Review*, Front. Phys. 8, 295 (2020), arXiv:2007.01315.

Evidence class: `SOURCE_GROUNDED / SYMMETRY_RESTRICTED_4D_EPRL_FK`.

## Native definition

The realization is a symmetry-restricted Euclidean/Riemannian EPRL-FK spin-foam path integral on a hypercubic two-complex.

- boundary/geometric states are restricted to quantum-cuboid coherent intertwiners;
- opposite faces of each cuboid carry equal areas;
- the vertex amplitude is a restricted EPRL-FK amplitude, studied in an asymptotic/semi-classical regime;
- the model remains part of the 4D spin-foam path-integral programme, but the restriction removes generic curvature degrees of freedom in the cuboid sector.

This is closer to a true amplitude-level 4D gravity coarse-graining test than RC-006 support combinatorics, while still being a severe truncation of full EPRL-FK gravity.

## Coarse/refinement map

The cited renormalization setup compares a coarse spin foam with a refined spin foam representing the same fixed coarse boundary geometry.

Source-grounded structure:

1. a **geometric embedding map** distributes coarse face areas over fine faces subject to the condition that fine areas sum to the coarse area;
2. internal/fine degrees of freedom are integrated over in the path integral;
3. a physical observable — most prominently the variance of one hypercuboid's 4-volume — is evaluated on coarse and refined foams;
4. the renormalized parameter `alpha` is obtained by matching the observable between discretizations.

The review emphasizes that the embedding map is chosen on geometric grounds rather than dynamically optimized, and that the coarse-graining flow is defined for a fixed boundary transition rather than the full boundary Hilbert space.

## Reported source behavior

- the coarse and refined volume-variance curves are monotonic in `alpha` and intersect at a fixed point;
- the fixed point is repulsive along the `alpha` flow and separates two phases;
- its location is close to the parameter region where the model's restricted diffeomorphism/vertex-translation symmetry is approximately restored;
- the precise fixed-point location changes with the coarse boundary state/approximation, while the qualitative behavior is reported as robust.

These are source-paper results, not new ISQGR computations.

## ISQGR relevance

RC-008 is a strong test of BH-004/BH-004B because it already separates two objects:

`geometric embedding/transport map`

from

`projection back to an effective amplitude family using a local observable`.

This resembles the ISQGR envelope/selector decomposition at a semantic level, but importantly the selector is **observable matching in theory-parameter space**, not the same source-native local constraint selector used in causal-set BH-004B.

Therefore RC-008 can distinguish:

- a generic coarse-graining architecture common to background-independent RG;
- from any more specific ISQGR claim about constraint-defined local selection inside a transported physical envelope.

## Interface audit

- IF-02 state space: `MAPPED_PARTIAL`
- IF-03 dynamics/amplitude: `MAPPED_PARTIAL`
- IF-04 composition/gluing: `MAPPED_PARTIAL`
- IF-06 gauge/diffeomorphism structure: `MAPPED_PARTIAL`
- IF-07 measure/normalization: `MAPPED_PARTIAL`
- IF-08 continuum/coarse graining: `MAPPED_PARTIAL`
- IF-09 Lorentzian recovery: `NOT_APPLICABLE_TO_THIS_EUCLIDEAN_RESTRICTED_REALIZATION`
- IF-10 GR recovery: `OPEN_BLOCKED`
- IF-12 UV/IR identity: `MAPPED_PARTIAL`
- IF-13 observable/comparator closure: `MAPPED_PARTIAL`

## Cheapest decisive ISQGR reproduction

1. Reconstruct the asymptotic restricted hypercuboid amplitude from the published formulas.
2. Reproduce the coarse/refined 4-volume variance curves for at least two boundary states.
3. Infer `alpha' -> alpha` without fitting to any RM-001/BH-004B metric.
4. Freeze the resulting embedding/observable map and test a held-out boundary state.
5. Compare the effective transport information with a scalar-parameter-only baseline.

A successful held-out amplitude-level reproduction would be a substantially stronger independent refinement test than RC-006 support closure or one-vertex Lorentzian `Dl` shell changes.

## Claim lock

- symmetry-restricted quantum cuboids are not full EPRL-FK gravity;
- the cuboid sector cannot represent generic curvature;
- a fixed point in the truncated one-parameter flow is not a proof of a full continuum limit;
- a semantic resemblance to BH-004B is not a new-physics claim;
- no candidate-theory promotion is authorized from this card alone.
