# ITER006 — Refinement source ladder: semantic classification

Date: 2026-09-12

Authoritative source-ladder run: `34710188640` (launch commit `f43e1a12b326bd4427b33dbc2834f1be806aadb4`).

The ladder was preregistered in `protocol/ITER006_REFINEMENT_SOURCE_LADDER_PREREG.json` specifically to prevent keyword-level splicing of maps that live at different semantic levels.

## Source-by-source classification

### arXiv:1205.6127 — `FORMAL_REFINEMENT_MAP_CANDIDATE` + `AMPLITUDE_CONSISTENCY_CANDIDATE`

The source explicitly orders boundaries by refinement, `b \prec b'`, associates configuration spaces to them, and defines injections

`iota_{bb'} : C_b -> C_{b'}`

whose images encode coarse boundary data inside a finer boundary space. It also imposes composition consistency across three refinement levels and formulates cylindrical consistency by pullback to the coarser boundary. The source explicitly presents this framework as a construction of cylindrically consistent transition amplitudes/dynamics.

This is the correct **formal semantic type** needed by the ISQGR refinement bridge. It is not, by itself, a Lorentzian EPRL/DVD implementation.

### arXiv:1407.7746 — `FORMAL_BACKGROUND_INDEPENDENT_RG_CANDIDATE`

The source defines coarse-graining projections `pi_{Gamma'Gamma}` from finer to coarser 2-complex data and states the cylindrical-consistency condition

`(pi_{Gamma'Gamma})_* mu_{Gamma'} = mu_Gamma` for `Gamma <= Gamma'`.

It also supplies boundary embedding maps between graph Hilbert spaces/configuration-function spaces and interprets the embedded 2-complexes as the background-independent analogue of scale.

This is a source-authoritative spin-foam/path-integral RG consistency framework. The paper itself also states a limitation relevant to ISQGR: its compact-gauge-group setup directly treats Riemannian-signature models; Lorentzian `SL(2,C)` full path-integral control is not supplied there. Therefore this source does not by itself authorize a Lorentzian DVD numerical bridge.

### arXiv:1609.02429 — `EXECUTABLE_COARSE_GRAINING_MAP_CANDIDATE`, semantic mismatch to DVD

The source implements coarse graining of q-deformed `SU(2)_k x SU(2)_k` BC/EPRL-FK analogue spin-net/intertwiner models with tensor-network renormalization. It explicitly describes fine 3-valent tensors being mapped into coarse tensors/edges and identifies inverse coarse-graining maps as embedding maps. SVD/variable transformations determine those maps dynamically.

This is the strongest executable fine↔coarse mechanism in the ladder and is already partly reproduced in ISQGR. But its model, signature/quantum-group setting, dimension and tensor-network state space are not the Lorentzian 4D DVD2/DVD3 amplitude space. It is therefore **not directly composable** with the DVD amplitude without an independent compatibility map.

### arXiv:2012.11536 — `KINEMATIC_REPRESENTATION_MAP_ONLY`

The source studies quantum-geometric embedding/projection maps between `SU(2)` cylindrical functions and Lorentz-covariant/projected cylindrical functions on a graph. It contains many embedding-map and Lorentzian-EPRL passages but no coarse-graining context in the frozen audit.

This is a same-graph representation/covariance/simplicity map, not a map from a coarser discretization to a finer one. It is a useful negative semantic control: **an EPRL embedding map is not automatically a refinement embedding map**.

### arXiv:2211.09578 — `REFINEMENT_FRAMEWORK_AND_ALGORITHM_BRIDGE_CANDIDATE`

The review gives the consistent-boundary construction with Hilbert spaces `H_b`, refinement embeddings, inductive-limit structure and cylindrically consistent amplitudes. In particular it states the amplitude condition

`A_b = iota^*_{b'b} A_{b'}`

and describes an iterative coarse-graining equation in which a refined amplitude is pulled back with a dynamics-informed embedding map to define an improved coarse amplitude. It further explains that tensor-network algorithms can compute dynamically adapted embedding maps by SVD/transfer-operator methods.

This is the best source for the **conceptual/formal bridge between consistent-boundary refinement and executable TNR**. It is still a framework/review, not an already supplied full Lorentzian DVD refinement operator.

## Source-chain verdict

The literature ladder contains all of the following separately:

1. explicit formal coarse→fine boundary embeddings and cylindrical consistency (`1205.6127`);
2. background-independent spin-foam RG consistency (`1407.7746`);
3. executable dynamically adapted TNR fine↔coarse maps (`1609.02429`);
4. Lorentzian EPRL kinematic `SU(2)↔SL(2,C)` geometric maps (`2012.11536`);
5. a modern framework explicitly connecting consistent-boundary amplitudes with dynamically determined TNR embedding maps (`2211.09578`).

However, **no source in this five-source ladder supplies a demonstrated map whose domain/codomain are the concrete Lorentzian DVD2/DVD3 boundary-amplitude spaces already computed in ISQGR**.

Terminal ladder classification:

`REFINEMENT_SEMANTIC_COMPONENTS_FOUND_BUT_LORENTZIAN_DVD_COMPATIBILITY_NOT_YET_ESTABLISHED`

## Claim locks

- No semantic splicing: formal, TNR, and Lorentzian representation maps remain separate until a compatibility gate proves matching domain/codomain and boundary/amplitude semantics.
- `DVD shell D != refinement`.
- No bridge credit is granted by this source ladder alone.
- `BRIDGE_DERIVED = false`.
- Candidate theory remains `UNFORMED / 0%`.
