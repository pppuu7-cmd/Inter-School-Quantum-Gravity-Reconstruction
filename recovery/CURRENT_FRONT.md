# Current front — ISQGR

Date: 2026-09-17.

Overall scientific programme: **50%**. Candidate theory: **0% / UNFORMED**. Bridge credit: **0**.

## Authoritative terminal closures

### ITER140 v6 — scoped scientific PASS
Commit `0be2f7a7e2f4e84b173dbb0a89f778b786c8cf52`, run `35040499084`, aggregate job `104671152184`, artifact `10431112965`, SHA256 `f2a51f9dc30365d7c03b68d10a0920bfb90aca66f56b0daad18325a9cd6126e1`. Classification `PASS_SCOPED_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION_CLOSED_POLE_INTEGRATION_OPEN`. Pole integration/noncancellation remains open; no bridge credit.

### ITER148 v3 — scoped scientific PASS
Commit `1b85eec35af8f157e2982040013a70836a49334f`, run `35044099632`, aggregate job `104677935357`, artifact `10431996892`, SHA256 `5617edf6b6d30db3599e67a86f97b8f7c31308550e94a5bff3f859b395a2ab94`. Classification `PASS_SCOPED_M3_FULL_D4_INVARIANT_AND_CANONICAL_BUBBLE_REDUCTION_CLOSED_GENERAL_D_POLES_OPEN`. General-D/O(epsilon), master poles, endpoint subtraction and bridge remain open.

### ITER149 — scoped scientific PASS
Commit `5544165988bf5d3f8350095001238f64f2400648`, run `35066093004`, job `104696596220`, artifact `10433884862`, artifact ZIP SHA256 `614dd604832583f584050092f81c2be6b46ec45011daff2138f5777fbb7e39e1`. Raw classification `PASS_SCOPED_ITER148_NO_REFIT_TAU_TRANSPORT_HELDOUTS`; 12/12 exact no-refit blind comparisons pass. No bridge credit.

### ITER150 — scoped scientific PASS
Preregistered commit `71cd4031b23c8e7654d2c99c3364604e39af414f`, run `35140549227`, job `104943683326`, artifact `10465465110`, artifact ZIP SHA256 `9e99d4b6854847a83b62ffde5c68969c96e5ac8f7d2c132375e49a737619fcd9`. Classification `PASS_SCOPED_FIRST_MG_NONLOCAL_TWO_PROPAGATOR_MASTER_POLE_NONZERO_CONTACT_SUBTRACTION_OPEN`. Exact result JSON SHA256 `0748f4f29a684738ae019cd35e27cd51b5f2f37b6c6b956342eb51a6851cdc90`; deterministic rerun byte-identical. Raw nonlocal pole is not full `B1_total`.

### ITER151 — contact manifest closed; full renormalization authority BLOCKED
Scientific commit `b674202300f3165772f32f64491526fd21ff9b08`; repaired run commit `184791e673a3c6c84486b5e609f2c00f9a1f9d67`, run `35146603418`, job `104964165476`, artifact `10467577601`, artifact ZIP SHA256 `b2d8581c8daf0b76dcfd33df3408b11d29afb719c056ac07a7a20925def5ce1f`. Result SHA256 `a8dd586c9b092ec32ba520d265544e5a98bbf57672e8077eef6fb791ae4adb79`. Classification `BLOCKED_MISSING_SOURCE_FAITHFUL_FULL_RENORMALIZATION_AUTHORITY_AFTER_CONTACT_MANIFEST_CLOSED`. Seven raw one-propagator endpoint contacts are frozen. Missing authority is not zero.

### ITER152 — exact renormalization-authority gap frozen; BLOCKED
Preregistration `f78c9796f2174c0de0a5e9b87a4f9aa0675493e8`; implementation `adbc25004740673331998f0f04f8e9b4a5aaa603`; execution `32c26ffeb9ae990c6ce9019d31b618b2eafd9926`; run `35150505863`, job `104977321094`, artifact `10469210437`, artifact ZIP SHA256 `16a722046d8bcf498980b39b1da7920b2696b93d83c1ed89f3f47bf872ba1a46`; ledger SHA256 `0ee8ccdcb5eaef15e1a80e730bd2c40953dcc01941b4f7f48e7ccc339c327bd9`. Classification `BLOCKED_SOURCE_AUTHORITY_INCOMPLETE_EXACT_MISSING_SLOTS_FROZEN`. Slots 1-4 closed; slots 5-10 open.

### ITER153 — seven-contact distributional object characterized; slot 5 still BLOCKED on graph R-operation
Frozen parent `d44245c8a1387df197489e95296096c3f004451e`; preregistration `bbcb9021e0245f3a506efa072d90cff992177126`; scientific implementation `139fa221d61a9650b29c9bd140a2771d2efb8120`; independent Critic/execution HEAD `f7efddec2fa1b1548d06a936fd122414526b7ec1`; run `35153011242`, job `104985687348`, artifact `10470051348`, artifact ZIP SHA256 `1cb8c2ef156e74ba6076dad776adf68f295df5dfebbf74494edd732f88d606b3`; result JSON SHA256 `23fd1f191a7baf5bbab965678724d3d930e8297b9fadaedacde780cd5ebda8bf`; Critic JSON SHA256 `c24c9221f1b72a6d3c421d9bd5f53c52cd8ba99ff5aa1ce36490f33a0d496e75`. Deterministic second pass is byte-identical. Classification `BLOCKED_SCOPED_SLOT5_REQUIRES_NEW_DISTRIBUTIONAL_EXTENSION_OR_RENORMALIZATION_INPUT`; Critic `PASS_CRITIC_ITER153_SCOPED_BLOCKER_LOGIC_SOUND`.

New data: the seven cancelled-momentum contact orders are exactly `[1,1,2,2,2,1,2]`; they are ambient first-/second-derivative delta contacts. For all seven, the delta-derivative wavefront cone meets the frozen geodesic line normal set, so the standard canonical Hörmander pullback is not licensed. An independent transverse-mollifier restriction exposes codimension-three divergence `~eta^-3/L` before derivatives. A premature dimensional-scaleless-zero shortcut is explicitly rejected because setting the frozen endpoint phase to one first assumes the disputed `s=0` pullback. ITER124 independently requires bulk/local-composite subtraction, endpoint/geodesic counterterms and full line mixing before contact/polynomial separation.

Therefore the minimal missing primitive is now exact: a source-qualified **graph-level R-operation/renormalization map on the unseparated first-M/G amplitude**. All seven renormalized contact pole values remain `null`, not zero. Slot 5 is not numerically closed; full `B1_total` remains unauthorized.

## Persistent locks
RC006 numerical retry unauthorized; RC009 scoped blocked; Lorentzian Delta4 negative results preserved; BH004/BH004B source-faithful amplitude/refinement object unresolved; genuine multi-vertex Lorentzian EPRL refinement authority unresolved. Generic projector/orientation/envelope structure remains absorbed by standard amplitude-level TNR and is not novelty. Forbidden claims remain `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`; candidate action/Hamiltonian/field equations remain unauthorized.

## Current workload / anti-idle
Do not repeat ITER118/126/127/140/143/150/151/152/153 basis, generic subtraction, affine-geometry, numerator, support, raw-pole, contact-manifest, completeness-ledger, or isolated contact-pullback audits. ITER153 terminalized the isolated seven-contact distributional question as far as the current source stack permits. The productive direct front is now the graph-level R-operation on the **unseparated** first-M/G amplitude, because ITER124 forbids contact separation before the required renormalization steps.

## Next admissible gates
1. Prospectively freeze and execute `ITER154_FIXED_GEODESIC_FIRST_MG_GRAPH_SUBDIVERGENCE_R_OPERATION_AUTHORITY`: enumerate the exact current first-M/G graphs/subgraphs, freeze bulk/local-composite counterterm inputs and forest/R-operation rules, and derive actual graph-specific subtraction maps/values where source-qualified. Endpoint and line-mixing coefficients remain symbolic dependencies until independently closed. No `B1_total`.
2. Use ITER154 to recompute the dependency DAG. If graph-specific bulk/local subtractions close, proceed prospectively to the divergent endpoint-counterterm and line-mixing gates required before any contact split.
3. In parallel, ITER148 general-D master-pole/endpoint-subtraction continuation only if a source-faithful dimensional object is prospectively frozen.
4. Independently, continue source acquisition for BH004/BH004B, genuine multi-vertex Lorentzian EPRL refinement, or RC006 only when fresh source authority actually exists.

Finite-cutoff/profile/scaling diagnostics alone cannot raise bridge status. Candidate theory remains `UNFORMED / 0%` until a constitution gate explicitly authorizes construction.
