# Preregistration — ITER058 Lorentzian refinement-transfer second-hop authority

Date frozen: 2026-09-14

## Inherited state

ITER057 is terminal **SCOPED BLOCKED — `LORENTZIAN_REFINEMENT_MAP_CITED_AUTHORITY_BLOCKED`**. The frozen first-hop Lorentzian EPRL sources define the 5→1/vertex-renormalization fine object but do not provide a separately pinned coarse object plus explicit variable-level refinement map. The Riemannian-holomorphic control arXiv:1412.8247 contains a genuine 5→1 homogeneity map but is model-mismatched and cannot be imported.

## Scientific question

Do the concrete renormalization/coarse-graining works explicitly cited by the Lorentzian EPRL numerical source arXiv:1903.12624 provide an exact source theorem, model transfer, or executable prescription that makes their coarse-graining map applicable to the Lorentzian EPRL 5→1 object without post-hoc substitution?

No amplitude execution is authorized.

## Frozen source panel

The panel is fixed before source retrieval/results:

1. arXiv `1409.2407` — Dittrich, Mizera, Steinhaus, *Decorated tensor network renormalization for lattice gauge theories and spin foam models*; explicitly cited by arXiv:1903.12624 for many-vertex/intertwiner renormalization context.
2. arXiv `1701.02311` — Bahr, Steinhaus, *Hypercuboidal renormalization in spin foam quantum gravity*; explicitly cited by arXiv:1903.12624 for minisuperspace renormalization context.
3. arXiv `1903.12624` citation-provenance lane, used only to prove these references are the cited second-hop authorities and to freeze the wording/context.
4. null controls.

No new source may be added inside ITER058 after outputs are seen.

## PASS object

**AUTHORITY PASS — `LORENTZIAN_REFINEMENT_TRANSFER_SECOND_HOP_PASS_SCOPED`** requires an exact statement or construction in the frozen chain that:

- identifies a coarse and fine object;
- defines the map/operator/coarse-graining transformation between them;
- explicitly applies that transformation to Lorentzian EPRL amplitudes of the relevant simplicial/5→1 object class, or proves an exact transfer theorem from the source model to that Lorentzian EPRL class;
- fixes every model-dependent normalization/weight needed for a later numerical test.

Generic tensor-network methodology, Euclidean/hypercuboidal truncation, analogy, shared boundary Hilbert spaces, or statements that a method “can be adapted” do not qualify.

## Independent lanes

Run `fail-fast:false`:

- `citation-provenance-1903`
- `dtnr-1409`
- `hypercuboidal-1701`
- `null-controls`

Each source lane must preserve exact arXiv source SHA256 and exact file/context provenance. Automated keyword/regex hits are candidates only; terminal classification requires raw-source inspection.

## Classification

`SCOPED BLOCKED — LORENTZIAN_REFINEMENT_TRANSFER_SECOND_HOP_BLOCKED` if sources are retrieved but no exact Lorentzian-EPRL transfer theorem/map exists.

`INFRASTRUCTURE FAIL` only for pre-authority retrieval/parsing failure.

No absence result is a scientific FAIL of EPRL.

## Locks

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory `UNFORMED / 0%`. No amplitude fitting, no thresholds, no candidate theory, no claim-lock release.