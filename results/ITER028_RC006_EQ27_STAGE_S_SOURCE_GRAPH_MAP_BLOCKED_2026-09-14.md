# ITER028 — RC006 Eq.(27) Stage-S source graph map

Date: 2026-09-14

## Terminal scientific classification

**BLOCKED — `RC006_EQ27_SOURCE_GRAPH_COMPONENT_MAP_BLOCKED`**

This is not a physical/scientific FAIL of RC006, not a numerical failure, and not an infrastructure failure. The GitHub Actions job was green, but the scientific verdict is BLOCKED under the frozen preregistration.

## Frozen authority

Preregistration: `prereg/ITER028_RC006_EQ27_TOPOLOGY_FAITHFUL_CONTRACTION_2026-09-14.md`

Prereg commit: `73246639c6710ab3e7228c3e5f0f11ae654f32b7`

Implementation commit: `a56829c6beeee273d410c5dc87a7234aa76daef4`

Workflow/production head: `3661564138585ad990761371e8a2d1e980719433`

Authoritative run: `34794113275`

Authoritative job: `103823792085`

Artifact: `10329326228` (`iter028-stage-s-evidence`)

Artifact digest: `sha256:9d077dfe52a76033c6061de872e6068cdea1980f55ceda0bf8e25c976d4f7c03`

Graph dictionary digest: `sha256:c6ced1ae5348d6ff57571b7007c50b061a3296b4ee75b2e584c2a0dfaf482216`

## Raw Stage-S findings

The fresh source provenance checks passed exactly:

- arXiv target: `1609.02429v2`;
- fresh archive SHA256: `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`;
- required archive SHA256: identical;
- exactly one source display carrying `eq:eprl-3-valent` was recovered from `bc-spin-nets.tex`;
- fresh Eq.(27) display SHA256: `88d2f7be9489980a763dd66b5c4900473c79900ccf72790095ae1675e9733b2d`;
- required historical source-snippet SHA256: identical.

Therefore provenance is not the blocker.

The exact byte-pinned Eq.(27) display mechanically contains:

- two explicit `\sum_j` structures;
- primed and unprimed `J^+` / `J^-` labels;
- the expected `j`, `j_i^+`, `j_i^-`, `l`, `l_1`, `l_2` labels and scalar prefactors;
- **two `tikzpicture` graphical factors**, not four separate TikZ blocks.

The ITER028 preregistration froze an inventory requiring **four TikZ graphical blocks / source graphical factors as historically extracted**. Because the source-pinned Eq.(27) display, under the exact frozen hashes, mechanically reproduces only two TikZ environments, Stage S cannot satisfy the preregistered inventory predicate without changing the contract after observing the source extraction.

No such post-hoc change was made.

## Consequence

Under the frozen rule, Stage S terminalizes `RC006_EQ27_SOURCE_GRAPH_COMPONENT_MAP_BLOCKED`; post-Stage-S numerical lanes A–F are **not authorized** and were not launched.

This preserves the negative result: the historical interpretation of “four graphical blocks” is not mechanically identical to “four TikZ environments” in the exact Eq.(27) display. A future gate may investigate whether the historical count meant subfactors/components inside the two diagrams, but that requires a **new prospectively preregistered source-semantics reconciliation gate**. It may not retroactively repair ITER028.

## Claim locks

No bridge credit. Eq.(29)/Lambda and one-step TNR remain unauthorized. No preferred alpha, Lorentzian EPRL, GR recovery, new physics, inter-school bridge, parent principle, or candidate theory is established.

Candidate theory remains **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**.
