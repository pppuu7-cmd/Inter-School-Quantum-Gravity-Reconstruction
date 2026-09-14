# ITER057 — Lorentzian refinement-map cited-authority chain

Date: 2026-09-14

## Terminal classification

**SCOPED BLOCKED — `LORENTZIAN_REFINEMENT_MAP_CITED_AUTHORITY_BLOCKED`**

This is not a scientific FAIL of Lorentzian EPRL. It means the prospectively frozen literature panel does not supply the full model-matched authority object required to preregister a coarse↔fine numerical refinement test.

## Frozen gate

Prereg commit: `b255704c7aeff417add30ae4e9ca1d4715054935`.

Implementation commit: `e73eb39b4bfbf472def448d51ca198fedaf52b2d`.

Production/workflow head: `d1df80096f3fcbe80660ffb7300e55d9af398641`.

Authoritative run: **`34823253593`**.

Frozen sources: arXiv `2302.00072`, `1803.00835`, `0810.1714`, `1903.12624`, and `1412.8247` strictly as a Riemannian-holomorphic model-mismatch control.

## Jobs and artifacts

- radiative-0810: job `103909422280`; artifact `10338578502`; digest `sha256:31be1761c7bc82e95cb813224b9f48d933cedc63da715fe5433fbd634d918aa9`
- null-controls: job `103909422478`; artifact `10339287253`; digest `sha256:03bcc9511bc699477187a0dff8db3314efed2b6fdb70391559cd4df19750dc63`
- primary-source-chain: job `103909422479`; artifact `10339003024`; digest `sha256:15ddebed132a362399bcecf33667fb31bec596f1640a2628905aa02ed256537f`
- lorentzian-vertex-1903: job `103909422482`; artifact `10338503478`; digest `sha256:238b7d8bc08301874a06e5c3405f24b62d1690bcbda6cc7e4d86aea184b7cf89`
- holomorphic-control-1412: job `103909422495`; artifact `10339077854`; digest `sha256:fa65254218d67a5a5616b88c06e48bb07c6d77d254676deb633f21d03fc1f988`
- eprlfk-1803: job `103909422545`; artifact `10338843757`; digest `sha256:26fbbe60a777fb984d1711c6907cb6d43b9f4251c3b100111a702b7d40e41262`
- aggregate: job `103909476987`; artifact `10338893493`; digest `sha256:803e96f5ed313431486828c69dec893ae62bf8afdcf7a39baf2581db8fb4a9a3`

All source retrieval lanes completed. Green CI was not treated as scientific PASS. Raw source excerpts were manually classified against the frozen model-compatibility rule.

## Source-by-source classification

### arXiv:2302.00072 — Lorentzian EPRL primary source

Source-qualified as the Lorentzian EPRL vertex-renormalization / 5→1 fine object. The paper explicitly calls the diagram the `vertex renormalization (or 5-1 Pachner move) amplitude` and provides its fine amplitude/routing.

However, the frozen raw-source audit found **no explicit separate coarse/single-vertex comparison object and no variable-level refinement/coarse-graining map**. The phrase `vertex renormalization` does not itself define the required map.

### arXiv:1803.00835 — Lorentzian EPRL-FK divergence context

The raw source explicitly studies the self-energy and vertex-renormalization diagrams and discusses refinement/renormalization context. It does not provide an explicit fine→coarse variable-level map satisfying the gate.

### arXiv:0810.1714 — radiative correction / 1→5 ball

The source explicitly identifies the five-vertex ball as a 4-simplex expanded by a 1→5 move and associates its divergence with vertex renormalization. It gives the five-vertex amplitude but **no explicit coarse object plus mapping prescription** to that coarse object.

### arXiv:1903.12624 — Lorentzian EPRL vertex numerics

This source defines the Lorentzian EPRL vertex amplitude and mentions future/many-vertex renormalization methods. Automated relation candidates involving `embedding` were manually rejected: they refer to embedding boundary data in Euclidean/Lorentzian 4-simplex geometry or the EPRL representation embedding, not to a fine→coarse refinement map. Renormalization references are contextual, not an explicit map for the current 5→1 Lorentzian object.

### arXiv:1412.8247 — frozen Riemannian-holomorphic control

This control **does** contain an explicit `5-1 homogeneity map`, including the relation `H_{5-1}[A_{5-1}^tau]=A_{5-1}` and a detailed homogeneity prescription. That is real source-level algebraic structure.

It is nevertheless non-qualifying by the frozen preregistration because it belongs to a **Riemannian holomorphic spin-foam model**, not the Lorentzian EPRL object class. No source in the frozen panel supplies a theorem or exact transfer identifying that homogeneity map with the Lorentzian EPRL 5→1 amplitude. Importing it would be a post-hoc model substitution.

## Null controls

Passed. The classification rejects keyword-only matches, BF/Riemannian substitution, asymptotic analogy, fitted rescaling, visual equality and output-dependent source selection.

## Scientific interpretation

The evidence sharpens the blocker: the problem is no longer whether a 5→1 refinement-like algebraic map exists anywhere in spin-foam literature. One does exist in the Riemannian-holomorphic control. The unresolved question is whether an **explicit Lorentzian-EPRL-compatible transfer/refinement map** exists that connects the source-defined fine 5→1 object to a separately defined coarse object without us inventing the transfer.

Therefore:

- `refinement_map_derived=false`
- `bridge_credit=false`
- candidate theory remains `UNFORMED / 0%`
- no coarse↔fine numerical comparison is authorized from ITER057 alone.

## Next admissible direction

A new prospectively frozen second-hop authority gate may test the specific renormalization/coarse-graining works actually cited by the Lorentzian EPRL sources for an exact transfer theorem or model-matched map. The Riemannian-holomorphic map must remain a control unless such a transfer is explicitly source-proven.