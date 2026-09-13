# ITER017 preregistration - RC006 phase / dual-pairing qualification

Date: 2026-09-14
Parent checkpoint: ITER016, commit 631cc86c5c42f1a4784ff0a80692ce19c03f33ce.

## Status at registration
Preliminary source-location checks confirmed that the exact-version text layer of arXiv:1609.02429v2 contains Appendix-B cap/cup and qbar-duality identities and that arXiv:1012.4784v3 contains a reality condition plus Wigner sign convention for generic-q Clebsch-Gordan coefficients. Web PDF screenshot retrieval failed with cache-miss errors before this registration. No numerical q-CG implementation, phase fit, Eq.(27) component reconstruction, or Iter012 retry has been run.

## Fixed source panel
Primary target: Dittrich, Schnetter, Seth, Steinhaus, arXiv:1609.02429v2, especially Eq.(27), Appendix A (A1-A9), Appendix B (B1-B15), Appendix E (E1-E4), Appendix F (F1).
Convention cross-check: Fairbairn-Meusburger, arXiv:1012.4784v3, especially Eqs.(9)-(14), root-of-unity fusion Eqs.(92)-(99).
Representation-action authority: Tolstoy, arXiv:math/0104045v1, especially Eqs.(9.1)-(9.14).
No additional coefficient formula may be imported merely to obtain a desired result.

## Frozen questions
1. Does the target source itself define a cap/cup dual pairing that is inverse under concatenation and relate qbar-CG to q-CG without an ordinary Hilbert absolute-square assumption?
2. Is the remaining scalar phase/sign convention independently fixed by a standard-reference convention compatible with the target parameter/generator dictionary?
3. Under an abstract rephasing C_ab^c -> exp(i phi_ab^c) C_ab^c, do the source-defined dual maps carry the inverse scalar needed for invariant closed contractions? Distinguish this categorical gauge statement from componentwise invariance.
4. Can Eq.(27)'s actual graphical contraction be qualified from readable visual evidence strongly enough to establish phase cancellation for that specific expression? If not, report visual-source BLOCKED rather than infer the diagram from text extraction.
5. Are finite-level admissibility/cutoff conditions consistent between the target A7 and Fairbairn-Meusburger root-of-unity fusion rule, after parameter relabeling?

## Fixed acceptance levels
- `RC006_DUAL_PAIRING_AND_PHASE_GAUGE_SOURCE_QUALIFIED_EQ27_VISUAL_PENDING`: source identities and abstract phase cancellation are proved, but Eq.(27) image-level structure is not independently visible.
- `RC006_PHASE_DUAL_PAIRING_CONVENTION_PINNED_SCOPED`: all above plus readable Eq.(27) visual qualification.
- `RC006_PHASE_DUAL_PAIRING_INCOMPATIBLE_SCOPED`: a concrete convention contradiction is found after the fixed dictionary.
- `RC006_PHASE_DUAL_PAIRING_SOURCE_BLOCKED`: source material is insufficient for even abstract dual-pairing qualification.

Only the second category may authorize a separate preregistration for bounded q-CG implementation validation. It still does not authorize Iter012, Eq.(29)/Lambda, preferred alpha, bridge credit, candidate theory, or any new-physics claim.

## Algebraic checks allowed in this checkpoint
Exact symbolic substitution and low-spin hand/symbolic counterexamples are allowed only to verify source-defined identities and phase transformation laws. No fitted phase, no amplitude scan, and no physics parameter optimization.

## Stop rule
Stop after the phase/dual-pairing checkpoint, write a source-by-source ledger and recovery update, and preserve every historical classification. Administrative readiness percentages do not increase automatically from a source qualification.
