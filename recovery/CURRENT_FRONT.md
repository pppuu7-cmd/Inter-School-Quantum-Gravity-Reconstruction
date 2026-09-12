# ISQGR CURRENT FRONT

Date: 2026-09-12  
Active iteration: `ITERATION_006`  
Iteration completion: **72%**  
Amplitude/refinement cross-realization validation: **43%**  
Overall scientific programme readiness: **49%**  
Candidate-theory construction: **0% — UNFORMED / constitutionally locked**

## Preserved blockers

RC006 contraction serialization remains terminal `SCIENTIFIC_FAIL_CONTRACTION_SERIALIZATION_UNSTABLE`; minimal Eq.(29) amplitude remains BLOCKED. RC008 remains source-only BLOCKED. RC009 remains `SCOPED BLOCKED`. Lorentzian Delta4 finite-cutoff/profile/scaling remains `SATURATED NEGATIVE/SCOPED` with no bridge credit.

Generic orientation/projector/envelope effects remain absorbed by standard amplitude-level TNR. Candidate theory remains locked until an actual source-authorized bridge/falsification layer exists.

## Genuine two-vertex Lorentzian EPRL — DVD finite-shell route

Pinned source: arXiv:1801.03771, source root SHA256 `27e781f9ae9b36056a57b7747dc3c58b5b9c944dd0214041149843d8434e16c1`. Pinned kernel: `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`.

Closed numerical layers:

- genuine Dl0 two-vertex pilot PASS: `34703528413`;
- Dl0 held-out gamma PASS 5/5: `34703682106`;
- B4 multishell kernel PASS 12/12: authoritative `34707794670`, worst fast-vs-adaptive relative error `1.05909e-7 < 1e-5`;
- symmetric finite DVD shell-sum PASS: `34708369655`;
- held-out multishell gamma strong support 5/5: `34708554742`;
- asymmetric mixed-spin B4 PASS 3/3: `34708641965`, worst relative error `2.49464e-8 < 1e-5`;
- asymmetric finite-shell DVD2/DVD3 PASS: `34708800382`;
- asymmetric held-out gamma strong support 5/5: `34709003568`, repeat max relative difference `0.0`;
- symmetric D3 extension strong support **8/8**: `34708941068`, aggregate `103594246242`, artifact `10302319200`, digest `sha256:8672e8509a11d5f61d0cc5ed37c49b41b341bcb0afe1bb3bd762d67ac764e949`; every frozen gamma passed `|D2→D3 change| < |D1→D2 change|` for DVD2 and DVD3, with exact D0–D2 regression and repeat difference `0.0`.

The D3 result is decreasing finite-cutoff change magnitude, **not monotonic convergence**: some DVD2 lanes change direction between D2 and D3.

## Closed semantic result — DVD source does not contain the required refinement map

Run `34709790323` audited the pinned DVD source under the preregistered explicit-map rule. Terminal semantic classification:

`SOURCE_REFINEMENT_AUTHORITY_NOT_FOUND`

The only map-like source passages were (a) the fixed-foam dynamical projection/amplitude functional and (b) the EPRL `Y` representation map. Neither maps a coarse boundary discretization to a finer one.

The DVD source itself states that it studies multiple different foams **at fixed boundary graph**, choosing a boundary consisting of two 4-link dipoles. Therefore DVD2 and DVD3 are different internal foams associated with the same boundary and are not a `b < b'` pair.

Locked classification:

`DVD2_DVD3_FIXED_BOUNDARY_FOAMS_NOT_DIRECT_REFINEMENT_PAIR`

Thus `DVD2=coarse`, `DVD3=fine`, internal-face count, foam complexity and booster shell depth `D` are all forbidden substitutes for a genuine boundary refinement map.

## Refinement source ladder — semantic components found, compatibility gap remains

Authoritative run `34710188640` audited five primary/framework sources. Terminal semantic classification is recorded in `results/ITER006_REFINEMENT_SOURCE_LADDER_SEMANTIC_CLASSIFICATION.md`:

`REFINEMENT_SEMANTIC_COMPONENTS_FOUND_BUT_LORENTZIAN_DVD_COMPATIBILITY_NOT_YET_ESTABLISHED`

Key separation:

- arXiv:1205.6127 gives explicit coarse→fine boundary injections and cylindrical-consistency/pullback conditions;
- arXiv:1407.7746 gives background-independent spin-foam RG/projective-measure consistency;
- arXiv:1609.02429 gives executable dynamically determined fine↔coarse TNR maps for q-deformed EPRL/FK analogue spin-net/intertwiner models;
- arXiv:2012.11536 gives Lorentzian EPRL `SU(2)↔SL(2,C)` quantum-geometric maps on a graph, classified as kinematic representation maps rather than discretization refinement;
- arXiv:2211.09578 explicitly connects consistent-boundary amplitudes with dynamics-informed embedding maps and TNR, but does not itself provide a ready-to-run full Lorentzian DVD refinement operator.

These pieces must not be spliced merely because they use the word `embedding`.

## Active gate — Lorentzian/EPRL graph refinement authority

A narrower source gate is now active to search the literature closest to the DVD setting for an explicit graph/foam refinement or subdivision operation **together with amplitude consistency**:

- arXiv:0909.0939 — KKL arbitrary-graph EPRL;
- arXiv:1010.5227 — local spin foams, locality/composition/cylindrical consistency;
- arXiv:1010.5437 — `summing is refining`, combinatorial refinement/continuum limit.

Preregistered protocol: `protocol/ITER006_LORENTZIAN_GRAPH_REFINEMENT_SOURCE_GATE.json` (`a12020b1274d0596b2accb8909624e200632d3d7`). Launch commit: `8a1f41b76a3323156a76540a4b1603da80328c06`. Authoritative run: `34710443728`, currently active.

Positive promotion requires more than arbitrary-graph support: an explicit mathematical refinement/subdivision map or equivalence relation, an amplitude-invariance/consistency rule under that operation, and semantic compatibility with the two-4-link-dipole Lorentzian EPRL boundary.

## Exact next gate / claim locks

1. Consume `34710443728` and semantically classify the three primary sources.
2. If a Lorentzian/EPRL-compatible graph/subdivision refinement operation with amplitude consistency exists, freeze the **minimal two-dipole boundary refinement** before evaluating any amplitudes.
3. Only then build a held-out, non-retuned coarse/refined amplitude test. If the source operation cannot be implemented on the DVD boundary, record the compatibility blocker rather than importing a Euclidean/q-deformed map by analogy.
4. Do not spend further compute on simple D4/D5 cutoff extension unless a new independent mathematical question specifically requires it.

Iteration completion is **72%**. Amplitude/refinement cross-realization validation is **43%**. Overall readiness remains **49%** because no actual refinement bridge has yet passed. Candidate theory remains **0% / UNFORMED**.

`ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`, candidate action/Hamiltonian/field equations, and RQIR/KMQGB promotion remain forbidden.
