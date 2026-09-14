# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**. Bridge credit remains zero.

## Persistent locks

RC006 numerical retry remains unauthorized. RC009 remains SCOPED BLOCKED. Lorentzian Delta4 negative results remain preserved. No full Eq.(27), Eq.(29), Lambda, one-step TNR, bridge derivation or candidate-theory construction is authorized.

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory `0 / UNFORMED`.

Forbidden claims remain `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`.

## Lorentzian frontier summary

ITER054 is a scoped SCIENTIFIC PASS for two bounded five-vertex fixed summands. ITER055 is a scoped SCIENTIFIC PASS completing transport over the four low-spin recoupling classes without retuning. These results do not establish a full sum or refinement invariance.

ITER056 is `SCOPED BLOCKED — LORENTZIAN_REFINEMENT_MAP_SOURCE_AUTHORITY_BLOCKED`: the pinned author implementation qualifies the fine EPRL 5→1 object but no separate coarse object or explicit map.

ITER057 is `SCOPED BLOCKED — LORENTZIAN_REFINEMENT_MAP_CITED_AUTHORITY_BLOCKED`, authoritative run `34823253593`, aggregate `10338893493`, durable result commit `9adf888c7abe76f841a23597462251fbbebf34f0`. The Riemannian-holomorphic control has a genuine 5→1 homogeneity map, but no source-qualified transfer to Lorentzian EPRL.

## ITER058 terminal SCOPED BLOCKED

Prereg `4da059da6b8639158d4f298869e968c75c577b5f`; implementation `e6c41bad1c2a0e46d4d58c94b251bba1ec1af47c`; production head `731201da41118368f65b21891142d24bd3e192eb`; authoritative run **`34823516850`**.

Classification: **`SCOPED BLOCKED — LORENTZIAN_REFINEMENT_TRANSFER_SECOND_HOP_BLOCKED`**.

The second-hop sources contain real coarse-graining machinery, but not the required model transfer:

- arXiv:1701.02311 explicitly defines a normalized fine↔coarse embedding map for quantum cuboids, but in a drastically restricted EPRL-FK hypercuboidal/Euclidean sector, not the Lorentzian simplicial 5→1 object;
- arXiv:1409.2407 defines decorated tensor-network coarse graining for lattice gauge/spin-foam models and explicitly distinguishes technically harder Lorentzian models; it does not give the exact Lorentzian EPRL 5→1 transfer theorem;
- arXiv:1903.12624 cites both only as future/simplification renormalization directions.

Artifacts: citation-provenance `10339028584` (`sha256:d70bf835ea8af5fbc534f7a081758cf8ee2abde3cc88bb9c40a799f573f95bbc`); hypercuboidal `10338973724` (`sha256:fddf9e13f29affce3e0103b515affda0e7192a4119760d2fcecde77f2f2a05b4`); DTNR `10338553866` (`sha256:380aaf347b2404d1cd87e72c47f3675d27b229be3ee96943779ef5585c58294e`); null `10338933813` (`sha256:99a9efa5748da9a5109e887111752c973353ddde15af97e5c6280889e330f649`); aggregate `10338824044` (`sha256:9b9cd4534d9a6361ee331902cbd58abd7883836236c8d4a7b9dadeb8c4022025`). Durable result commit `63847888c8ff02f1782b5e252b9dff8a60fd85a0`.

## ITER059 active — open authority discovery

Because the fixed cited chain is now saturated, ITER059 performs a prospectively frozen, metadata-only arXiv discovery for **new** Lorentzian-EPRL-compatible refinement/coarse-graining authority. It does not execute amplitudes and cannot itself produce authority PASS.

Frozen queries cover: Lorentzian EPRL + refinement/coarse graining; Lorentzian spin foam + embedding/coarse graining; EPRL renormalization + simplicial/Pachner; EPRL refinement/embedding map. Already consumed sources are deduplicated as saturation controls.

Prereg commit `c80a38a78e0ce99633dc9738281ab5a46bbd5b87`; implementation `5ee7fdc6f65594656f130c1c5e223d0390bda686`; production/workflow head `369f366c2c81f186c72c8e0f3a1eaea1e82511d3`; authoritative run **`34823751928`**.

The first terminal attempt was **INFRASTRUCTURE FAIL PRE-SCIENCE**, not a scientific result: all four live discovery lanes hit HTTP 429 from the arXiv metadata endpoint. The null/provenance lane succeeded and produced artifact `10339278252` (`sha256:c782087855a7097a9a9015462d46d08569260ce0595f37c933f08ddc74cbf215`). The resulting partial aggregate `10338604250` is stale/non-authoritative for scientific classification.

Frozen science was not changed. Only the four failed jobs were re-run. Current retry workload is **4 queued / 0 in_progress**: `103915277099` eprl-refinement-map; `103915277287` lorentzian-spin-foam-map; `103915277359` lorentzian-eprl-refinement; `103915277417` eprl-rg-simplicial. No duplicate batch is running. Recovery update commit for this infra event: `7cb62a2079d2078d25d4cc8dc6eb4f0a7f284308`.

## Exact next admissible action

Consume the four ITER059 retry artifacts plus a fresh aggregate. If genuinely new metadata candidates satisfy the frozen inclusion rule, freeze their exact source IDs in a separate qualification gate before inspecting source-level results. If no new candidates survive, classify discovery saturation and preserve the refinement-map blocker. No coarse↔fine numerical test is authorized yet.