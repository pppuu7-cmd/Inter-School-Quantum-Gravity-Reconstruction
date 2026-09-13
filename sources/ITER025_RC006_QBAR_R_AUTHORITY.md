# ITER025 source authority — RC006 qbar index ordering and R/R^-1 crossing

Date: 2026-09-14

Status: `SOURCE_AUTHORITY_COMPLETE_SCOPED`

Scope: reduced Euclidean `SU(2)_k x SU(2)_k` realization RC-006 only. This record is convention/source authority, not bridge evidence and not a Lorentzian-EPRL statement.

## Exact source packages

### Target

Dittrich, Schnetter, Seth, Steinhaus, *Coarse graining flow of spin foam intertwiners*, `arXiv:1609.02429v2`.

Exact e-print archive SHA256:
`3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`

Decoded source file: `bc-spin-nets.tex`.

### qbar cited source

Dittrich, Martin-Benito, Steinhaus, *Quantum group spin nets: refinement limit and relation to spin foams*, `arXiv:1312.0905v2`.

Exact e-print archive SHA256:
`69334656117892b255ebb9b0c3855b6387bafc630bb9345b084e5434e22294c0`

Decoded source file: `qg_spinnet_20140616.tex`.

### R/crossing cited source

Dittrich, Kaminski, *Topological lattice field theories from intertwiner dynamics*, `arXiv:1311.1798v1`.

Exact e-print archive SHA256:
`d6804794d3f4589f77a2e11d2a143c1125a900160e0c632ed3b3e471598af3f7`

Decoded source file: `arxiv20131107.tex`.

The Biedenharn-Lohe book citation is retained as delegated authority but is not needed for the scoped closure below; no unseen book formula is inferred.

## qbar authority

Target source `bc-spin-nets.tex` lines 1432-1464 states that cups/caps construct the inverse/complex-conjugate deformation coefficient and writes

`{}_{\bar q} C^{j_1 j_2 j_3}_{m_1 m_2 m_3}`

equal to the displayed bent-leg graph. The graph labels the upper legs `j_2` (left) and `j_1` (right), lower leg `j_3`, and the text immediately after the equation states that the map is

`V_{j_3} -> V_{j_1} \otimes V_{j_2}`.

Thus the tensor-product order is source-stated rather than selected after calculation.

The cited q-spinnet source independently gives an explicit indexed component identity at `qg_spinnet_20140616.tex:1101`:

`{}_q C^{j_1 j_2 j_3}_{m_1 m_2 m_3} = (-1)^{j_1+j_2-j_3} {}_{\bar q} C^{j_1 j_2 j_3}_{-m_1,-m_2,-m_3}`.

This fixes the qbar component ordering relative to the already frozen q-CG convention: no `m_1 <-> m_2` swap, no representation permutation, and no fitted phase/orientation is needed. The same cited source also reproduces the bent-leg qbar graph at lines 451-465.

## R / R^-1 authority

Target source `bc-spin-nets.tex:956-987` explicitly states that over-/undercrossings are related by the `\mathcal R` matrix, labels one crossing as `\mathcal R`, and gives the channel weight with exponent

`q^{-1/2 [j_1(j_1+1)+j_2(j_2+1)-j(j+1)]}`.

The opposite crossing is explicitly labelled `\mathcal R^{-1}` and carries the opposite exponent sign

`q^{+1/2 [j_1(j_1+1)+j_2(j_2+1)-j(j+1)]}`.

The cited source `arxiv20131107.tex:1668-1682` independently states that the strand crossing cannot be ignored because it exchanges tensor-product factors and defines the crossing as `R` with the same negative exponent sign. Lines 1707-1718 define the inverse anti-crossing as `R^{-1}` with the positive exponent sign. The strand labels `1` and `2` are present in the diagrams.

Therefore the source set fixes both the executable channel factor and which of the two crossing orientations is `R` versus `R^{-1}`. No post-hoc crossing choice is required.

## Controls and provenance

ITER025 Actions artifact `10326669550` contains `source_manifest.json`, `qbar_evidence.json`, `r_crossing_evidence.json`, `controls.json`, `provenance.json`, and `aggregate.json`; artifact digest:

`sha256:cb1e40dc31495eb1b21d38315fb28dcc70b35f6d0505f7cd81091c0ecd4afba5`.

The collector confirmed the frozen historical hashes for `1609.02429v2` and `1312.0905v2`. The positive control recovered exact indexed target cap/cup/coproduct evidence with source-file/line context. The automation deliberately emitted only `EVIDENCE_COLLECTED_REQUIRES_MANUAL_VERDICT`, not scientific PASS.

## Scoped conclusion

Both ITER023 missing authorities are source-locatable and convention-unique within the frozen RC-006 source set. The source gate therefore passes as:

`RC006_EXACT_QBAR_R_SOURCE_AUTHORITY_COMPLETE`.

This authorizes only a **separately preregistered bounded Eq.(27) component translation/contraction**. It gives no bridge credit, no continuum/GR claim, no Lorentzian-EPRL claim, no Eq.(29) authorization, and no candidate-theory authorization.
