# ITER025 prereg — RC006 exact qbar/R cited-source authority

Date: 2026-09-14

Frozen **before** the ITER025 source packages are downloaded or inspected by this iteration.

## Why this gate

ITER023 left two exact convention blockers for source-derived Eq.(27) component translation: qbar graph-to-index ordering and executable R/R^-1 convention. ITER024 attempted to resolve them but is terminal `INVALID_IMPLEMENTATION` because its code did not actually inspect the resolved cited sources or preserve formula locators. The highest-information admissible step is therefore one corrected source-authority gate, not an Eq.(27) contraction and not atlas expansion.

## Target realization and atlas coordinates

Concrete realization: `RC-006_EPRL_FK_TENSOR_COARSE_GRAINING`, reduced Euclidean `SU(2)_k x SU(2)_k` model.

Atlas coordinates under test: `S` state/intertwiner convention, `D` amplitude tensor definition, `C` graphical composition/dualization, `G` representation/duality structure, `M` normalization/contraction convention. This gate does not test continuum `X/E` or cross-school bridge survival.

## Frozen source set

Primary target:
- Dittrich, Schnetter, Seth, Steinhaus, *Coarse graining flow of spin foam intertwiners*, `arXiv:1609.02429v2`.

Resolved cited open sources:
- Dittrich, Martin-Benito, Steinhaus, *Quantum group spin nets: refinement limit and relation to spin foams*, `arXiv:1312.0905v2`.
- Dittrich, Kaminski, *Topological lattice field theories from intertwiner dynamics*, `arXiv:1311.1798v1`.

Resolved non-open/secondary authority in the target bibliography:
- L. C. Biedenharn and M. A. Lohe, *Quantum Group Symmetries and q-Tensor Algebras* (World Scientific, 1995).

The book may be recorded as a delegated authority but cannot count as exact formula closure unless the needed convention is actually available and source-locatable in evidence consumed by this gate. No formula may be reconstructed from the citation alone.

Known historical archive hashes that may be used only as provenance controls:
- `1609.02429v2`: `sha256:3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.
- `1312.0905v2`: `sha256:69334656117892b255ebb9b0c3855b6387bafc630bb9345b084e5434e22294c0`.

## HYPOTHESIS

`H025`: the exact cited authority chain contains source-locatable information sufficient to determine, without fitting or convention repair, both (a) the qbar dual map's graph-to-index ordering compatible with the already frozen target q-CG normalization and (b) the R/R^-1 crossing convention required for an Eq.(27) component translation.

This is a source-authority hypothesis, not a physics/bridge hypothesis.

## Frozen lanes

1. `provenance`: download exact versioned source archives, compute SHA256, decode without executing TeX, inventory source files, and verify the two historical hashes above where applicable.
2. `qbar`: inspect `1609.02429v2` and `1312.0905v2`; preserve every candidate formula as exact source file + 1-based line range + bounded literal TeX context. No boolean-only match can pass.
3. `r-crossing`: inspect `1609.02429v2` and `1311.1798v1`; preserve every candidate universal-R / crossing / inverse formula as exact source file + line range + bounded literal TeX context. No bibliography presence or lexical `R` mention can pass.
4. `controls`: positive control must recover a known explicit indexed cap/cup or coproduct formula from `1609.02429v2`; negative controls must reject bibliography-only evidence and a deliberately synthetic lexical-only R token.

The automation is evidence collection only. It must not emit a scientific PASS from regex booleans. Final classification is applied after consuming the raw artifacts under the rules below.

## Frozen PASS / BLOCKED / INVALID rules

### PASS — `RC006_EXACT_QBAR_R_SOURCE_AUTHORITY_COMPLETE`

All must hold:

1. provenance lane is valid;
2. qbar evidence contains an explicit indexed equality or equally explicit component definition that uniquely determines the input/output index ordering of the qbar dual map under the frozen target q-CG normalization;
3. R evidence contains an executable R formula **and** source text/definition sufficient to tie the relevant crossing/tensor-leg orientation to `R` versus `R^-1` without post-hoc choice;
4. each decisive item has exact source version, source file, and line/equation/appendix locator recoverable from the artifact;
5. no fitted phase, index permutation, sign, orientation, or branch is introduced.

Only this PASS may set `eq27_component_reconstruction_prereg_allowed=true`. It still does not authorize Eq.(29), Iter012, bridge credit, candidate formation, or new physics claims.

### BLOCKED — `BLOCKED_SOURCE_AUTHORITY`

Use if source transport/provenance is valid but either qbar ordering or R/R^-1 crossing assignment remains graphical-only, prose-only, delegated to inaccessible authority, multiply compatible, or otherwise not source-unique.

BLOCKED is valuable scientific metadata and is not evidence against the realization.

### INVALID

Use `INVALID_PROVENANCE` for version/hash/source-package failure and `INVALID_IMPLEMENTATION` if the evidence collector again fails to implement the frozen lanes/locators/controls. Network/transport failure with no scientific inspection is `INFRASTRUCTURE_FAIL`.

## Positive and negative controls

Positive control: recover at least one exact indexed target formula in the 1609.02429v2 package (cap/cup or coproduct) with source-file and line context.

Negative controls:
- bibliography entry alone must not qualify qbar or R authority;
- lexical `R`, `R matrix`, `mathcal{R}`, `dual`, or `bar{q}` without the decisive component/crossing definition must not pass;
- no result from one lane may alter another lane's frozen rule.

## Interpretation ceiling

Even a full PASS establishes only exact convention authority for this reduced Euclidean realization and authorizes a **separate preregistration** of a bounded Eq.(27) component translation/contraction. It is not bridge evidence, not Lorentzian EPRL evidence, not continuum/GR recovery, and not candidate-theory evidence.

## Locks

During ITER025: no Eq.(27) numerical contraction; no fitting; no Iter012 retry; no Eq.(29)/Lambda; no preferred alpha; no bridge credit; `candidate theory = UNFORMED`; `candidate_theory_authorized=false`; no new physics or all-schools claim.
