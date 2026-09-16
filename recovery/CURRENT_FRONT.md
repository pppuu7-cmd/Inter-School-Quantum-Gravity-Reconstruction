# Current front — ISQGR

Date: 2026-09-16.

Overall scientific programme: **50%**. Candidate theory: **0% / UNFORMED**. Bridge credit: **0**.

## Authoritative terminal closures

### ITER140 v6 — scoped scientific PASS
Commit `0be2f7a7e2f4e84b173dbb0a89f778b786c8cf52`, run `35040499084`, aggregate job `104671152184`, artifact `10431112965`, SHA256 `f2a51f9dc30365d7c03b68d10a0920bfb90aca66f56b0daad18325a9cd6126e1`. Classification `PASS_SCOPED_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION_CLOSED_POLE_INTEGRATION_OPEN`. Pole integration/noncancellation remains open; no bridge credit.

### ITER148 v3 — scoped scientific PASS
Commit `1b85eec35af8f157e2982040013a70836a49334f`, run `35044099632`, aggregate job `104677935357`, artifact `10431996892`, SHA256 `5617edf6b6d30db3599e67a86f97b8f7c31308550e94a5bff3f859b395a2ab94`. Classification `PASS_SCOPED_M3_FULL_D4_INVARIANT_AND_CANONICAL_BUBBLE_REDUCTION_CLOSED_GENERAL_D_POLES_OPEN`. General-D/O(epsilon), master poles, endpoint subtraction and bridge remain open.

### ITER149 — scoped scientific PASS
Commit `5544165988bf5d3f8350095001238f64f2400648`, run `35066093004`, job `104696596220`, artifact `10433884862`, artifact ZIP SHA256 `614dd604832583f584050092f81c2be6b46ec45011daff2138f5777fbb7e39e1`. Raw classification `PASS_SCOPED_ITER148_NO_REFIT_TAU_TRANSPORT_HELDOUTS`; A-E all true. All 12 preregistered exact no-refit blind comparisons pass with difference exactly zero at tau `3/10`, `5/12`, `7/13` across four frozen panels. This strengthens only D4 numerator transport/selector robustness. It does not close poles, endpoint subtraction, amplitude/refinement, or bridge derivation.

### ITER150 — scoped scientific PASS
Preregistered commit `71cd4031b23c8e7654d2c99c3364604e39af414f`, run `35140549227`, job `104943683326`, artifact `10465465110`, artifact ZIP SHA256 `9e99d4b6854847a83b62ffde5c68969c96e5ac8f7d2c132375e49a737619fcd9`. Classification `PASS_SCOPED_FIRST_MG_NONLOCAL_TWO_PROPAGATOR_MASTER_POLE_NONZERO_CONTACT_SUBTRACTION_OPEN`. Exact result JSON SHA256 `0748f4f29a684738ae019cd35e27cd51b5f2f37b6c6b956342eb51a6851cdc90`; deterministic rerun is byte-identical. In the frozen Q^0 K^0 connected-cross sector, all M simple-pole residues are zero while `G_R1_chi2_Gamma2_dR1 : b^2*S^2` contributes `-1050/(pi^4 L^10)` to the raw `1/epsilon` residue. This is not full `B1_total`: contact sectors, endpoint/bulk counterterms, subdivergence subtraction, full mixing and gauge/BRST consistency remain open. No bridge credit.

### ITER151 — contact manifest closed; full renormalization authority BLOCKED
Frozen scientific implementation commit `b674202300f3165772f32f64491526fd21ff9b08`; successful repaired run commit `184791e673a3c6c84486b5e609f2c00f9a1f9d67`, run `35146603418`, job `104964165476`, artifact `10467577601`, artifact ZIP SHA256 `b2d8581c8daf0b76dcfd33df3408b11d29afb719c056ac07a7a20925def5ce1f`. Result JSON SHA256 `a8dd586c9b092ec32ba520d265544e5a98bbf57672e8077eef6fb791ae4adb79`; deterministic rerun is byte-identical. Classification `BLOCKED_MISSING_SOURCE_FAITHFUL_FULL_RENORMALIZATION_AUTHORITY_AFTER_CONTACT_MANIFEST_CLOSED`. All A-I checks are true. Exactly seven nonzero one-propagator endpoint-contact survivors are extracted from the frozen ITER140 tables under the exact ITER143 support rules. Repository authority audit finds only the ITER124 required-output specification and no terminal PASS object supplying actual `B1_direct`, `beta_defect`, `B1_defect`, `B1_total`, and raw/subtracted simple/higher-pole coefficients. The blocker is not evidence that contact terms vanish and does not authorize full noncancellation. No bridge credit.

### ITER152 — exact renormalization-authority gap frozen; BLOCKED
Preregistration commit `f78c9796f2174c0de0a5e9b87a4f9aa0675493e8`; implementation commit `adbc25004740673331998f0f04f8e9b4a5aaa603`; workflow/execution commit `32c26ffeb9ae990c6ce9019d31b618b2eafd9926`; run `35150505863`, job `104977321094`, artifact `10469210437`, artifact ZIP SHA256 `16a722046d8bcf498980b39b1da7920b2696b93d83c1ed89f3f47bf872ba1a46`. Exact ledger JSON SHA256 `0ee8ccdcb5eaef15e1a80e730bd2c40953dcc01941b4f7f48e7ccc339c327bd9`; deterministic rerun is byte-identical. Classification `BLOCKED_SOURCE_AUTHORITY_INCOMPLETE_EXACT_MISSING_SLOTS_FROZEN`. All A-H checks are true. Ten preregistered authority slots are exhaustively classified: slots 1-4 are closed at their stated scopes (finite line/endpoint basis; local pole-subtraction method; exact chi1/chi2 affine singular structure; scoped first-M/G raw/contact-support decomposition), while slots 5-10 remain open (actual seven-contact distributional extension/poles; graph-specific subdivergence subtraction values; endpoint counterterm coefficients; four-operator line-defect pole/mixing matrix; renormalized mapping of seven contacts; six terminal ITER124 values). This localizes the blocker to actual renormalization data/mappings rather than a generic missing formalism. No bridge credit.

## Persistent locks
RC006 numerical retry unauthorized; RC009 scoped blocked; Lorentzian Delta4 negative results preserved; BH004/BH004B source-faithful amplitude/refinement object unresolved; genuine multi-vertex Lorentzian EPRL refinement authority unresolved. Generic projector/orientation/envelope structure is absorbed by standard amplitude-level TNR and is not novelty. Forbidden claims remain `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`; candidate action/Hamiltonian/field equations remain unauthorized.

## Current workload / anti-idle
ITER152 has terminalized the renormalization-authority completeness ledger. Do not repeat ITER118/126/127/140/143/150/151/152 basis, local-subtraction-method, affine-weight, raw-pole, support, contact-manifest, or generic authority-audit calculations. The first missing primitive is now specifically the distributional extension/pole authority for the seven frozen ITER151 endpoint-contact structures. Full `B1_total` remains unauthorized until the downstream subdivergence, endpoint-counterterm, line-mixing and renormalized-mapping slots are also closed.

## Next admissible gates
1. `ITER153_FIXED_GEODESIC_CURVATURE_ENDPOINT_CONTACT_DISTRIBUTIONAL_EXTENSION_AUTHORITY`: derive, from the frozen general-d kernels and dimensional regularization, the distributional extension/pole data for the seven ITER151 endpoint contacts. Keep counterterm subtraction symbolic/source-qualified; do not form `B1_total` yet.
2. After slot 5 closes, close slots 6-9 prospectively: graph-specific bulk/local-composite subdivergence subtraction, divergent endpoint-counterterm coefficients, the four-operator line-defect pole/mixing matrix, and the mapping of seven contacts into the renormalized basis. Only then evaluate the six ITER124 terminal outputs.
3. In parallel, ITER148 general-D master-pole / endpoint-subtraction continuation only if a mathematically source-faithful dimensional object can be stated prospectively.
4. Independently, continue the PHASE_1 amplitude/refinement bridge search: BH004/BH004B source-faithful amplitude/refinement object, genuine multi-vertex Lorentzian EPRL refinement, or RC006 q-deformed EPRL/FK amplitude/TNR reconstruction when source-faithful authority exists.

Finite-cutoff/profile/scaling diagnostics alone cannot raise bridge status. Candidate theory remains 0/UNFORMED until a constitution gate explicitly authorizes construction.
