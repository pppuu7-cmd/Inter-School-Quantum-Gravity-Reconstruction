# Current front - ISQGR

Date: 2026-09-14. Latest closed checkpoint: ITERATION_017 (100% checkpoint completion; **scoped source/algebra PASS, visual/convention qualification still pending**).

Candidate theory: **UNFORMED**. Administrative readiness values remain 49% amplitude/refinement cross-realization validation, 49% overall programme, 0% candidate construction. These are unchanged bookkeeping values, not measured probabilities.

## RC006

Terminal classification: `RC006_DUAL_PAIRING_AND_PHASE_GAUGE_SOURCE_QUALIFIED_EQ27_VISUAL_PENDING`.

Preregistration: `fe11ca9c2b71e7561beb4aca12ee795dc909ca70`. Report: `results/ITER017_RC006_PHASE_DUAL_PAIRING_2026-09-14.md`. Checker and provenance: `code/iter017/check_phase_dual_pairing.py`, `results/ITER017_CHECK_RUN.txt`, `results/ITER017_EXECUTION_MANIFEST.json`.

### What moved

The target arXiv:1609.02429v2 Appendix B explicitly defines the cap and cup, requires their concatenation to be the identity, constructs the inverse/complex-conjugate-q Clebsch-Gordan map by bending a leg, and identifies it as the dual map. Therefore categorical qbar duality is present in the frozen open target source. The old Iter014 `qbar_duality=false` was a regex false negative for the braced TeX form `\\bar{q}`; historical Iter014 remains unchanged because its terminal blocker was representation-action authority.

Exact symbolic bookkeeping verifies the source cap/cup identity for 819 magnetic-component cases through j=6 with zero failures. Target bilinear orthogonality (A9) also removes a generic scalar phase of a normalized fusion channel: `C -> lambda C` preserves A9 only for `lambda^2=1`, leaving a sign. In a properly paired source-defined dual contraction that residual sign appears twice and cancels. This qualifies the **abstract phase gauge**, not the exact graphical Eq.(27) contraction.

The target A7 cutoff and Fairbairn-Meusburger Eq.(93) are algebraically identical under `r=k+2`; 23,408 spin triples for k=1..16 were checked with zero mismatches. A new scope restriction is decisive: Fairbairn-Meusburger explicitly assumes `r>2` odd in its root-of-unity Euclidean section. Hence the mapping directly covers odd target k only and does **not** independently qualify k=12 (`r=14`), while the target paper identifies k=12 as its first non-trivial level for the EPRL normalization map.

Fairbairn-Meusburger's generic-q reality condition plus Wigner convention fixes phase/sign in the real-positive-q section, but that condition is not silently continued to the unit-modulus even-k root. The target itself points to Biedenharn-Lohe for its standard q-CG convention; no inaccessible external coefficient formula has been imported.

### Preserved source provenance

Historical Iter014 logs pin the downloaded archive hashes:

- `1609.02429v2`: `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`
- `1312.0905v2`: `69334656117892b255ebb9b0c3855b6387bafc630bb9345b084e5434e22294c0`
- `1506.04749v3`: `758e05bf73390015fb02f374c69892ad155c8edacb40a97876c12aa7f64c1e14`

The archives are not currently materialized in the local runtime; these are historical frozen-run hashes, not newly downloaded bytes.

### What remains blocked

Eq.(27)'s text layer and Appendices E/F show a graphical/bilinear normalization with explicit sign and quantum-dimension factors, but the exact edge topology of Eq.(27) was not certified: exact-version PDF screenshot calls returned cache-miss transport errors and local PDF acquisition did not succeed. No diagram was reconstructed from guesswork.

Therefore `implementation_validation_gate_authorized=false`. The next admissible gate is `EXACT_EQ27_GRAPH_COMPONENT_TRANSLATION_AND_EVEN_K_CONVENTION_QUALIFICATION`: obtain readable exact graph/source evidence for Eq.(27), translate it to components without convention changes, prove the remaining signs are paired/gauge-covariant there, and independently qualify the even-k case (especially k=12) or derive the needed convention directly from the target source. Only then may a bounded q-CG implementation-validation gate be preregistered.

## Preserved history and claim locks

ITER016 remains `RC006_ACTION_TEXT_LOCATED_CONVENTION_AND_VISUAL_QUALIFICATION_PENDING`; ITER015 remains infrastructure failure (timeouts/HTTP 429), not a no-source result; ITER014 and ITER013 retain their recorded classifications. No historical classification was rewritten.

BH004/BH004B remains scoped-negative. Multi-vertex Lorentzian EPRL refinement remains blocked by source algebraic zero-face-collapse ambiguity. RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope. These fronts were not rerun.

`bridge_credit=false`; `iter012_retry_authorized=false`; `eq29_amplitude_authorized=false`; `candidate_theory_authorized=false`. No q-CG numerical implementation, fitted phase, amplitude scan, preferred-alpha, new-physics, all-schools-fail, new-theory-required or bridge-derived claim was made in ITER017.
