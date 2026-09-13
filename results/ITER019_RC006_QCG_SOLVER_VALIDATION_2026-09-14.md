# ITER019 — RC006 bounded q-CG solver implementation validation

Date: 2026-09-14  
Preregistration: `4f497a0e6413d8f4bc0408f0050552fa80d2ba98`

## Terminal classification

**`RC006_QCG_SOLVER_VALIDATED_BOUNDED_K12`** — SCIENTIFIC PASS in the preregistered bounded scope.

ITER019 is the first bounded implementation PASS for RC006. The q-CG/intertwiner data were constructed from the source-qualified Uq(su2) representation action, target coproduct, target root-of-unity q-number/admissibility, bilinear A8/A9 normalization and Appendix-B singlet/cap convention. No external closed-form q-CG coefficient formula and no fitted coefficient phase were used.

This result authorizes only the next narrowly preregistered robustness/reconstruction test. It does **not** by itself authorize historical Iter012, Eq.(29)/Lambda amplitude work, alpha selection, bridge credit, or candidate-theory construction.

## Authoritative production provenance

- production run: `34785058584`
- production head: `d5934a5f2251c01b2d8ec2315d1c36161b45f507`
- algebra job `103798900360`; artifact `10326068204`; digest `sha256:86ff5cb700c222d24497edd1fdb45761f4933e2c9d3d6d24d415a7debc40a049`
- recoupling job `103798900429`; artifact `10325843872`; digest `sha256:677ba71640ced1fec15cb4760c15dbb7453f21b8ccae5494028b275bc17c8530`
- projector-cap job `103798900448`; artifact `10326526775`; digest `sha256:7d0bd4fe1a5f0436be259f77c39c1be5e7099b66167815a439ed056334aaaf0f`
- classical-limit job `103798900462`; artifact `10326073163`; digest `sha256:633c9c5729e9eda083ad0fb8c717c17925fd6abeb3e4cce58585fbe593f7156c`
- aggregate job `103798931295`; artifact `10326466098`; digest `sha256:66208c6a95c1c2e7375edf21e8172680a42b36a697c7d5a6ecc921f96dc4f025`

All four raw lane artifacts and the frozen aggregate were consumed before classification. Green CI was not treated as scientific PASS.

## Frozen-lane results

### Algebra/intertwiner — PASS

19 preregistered channels were generated at `k=12`. Every expected highest-weight nullspace had dimension one. Maximum Jz/J+/J- intertwiner residual was `1.5625802476324566e-12`, below the frozen `5e-10` threshold.

### A8/A9/projector/cap — PASS

Maximum A9 residual: `1.183923065063617e-12`. Full `(3,3)` completeness residual: `2.698451684154921e-13`. The `(4,4)` admissible A8 projector had rank exactly 25 at SVD tolerance `1e-8`; its 80-digit idempotence residual was `3.821302597164378e-74`, and `|Tr(P)-25|=9.853078709590306e-77`. Maximum B2 singlet residual up to the preregistered permitted overall sign was `1.056171682913856e-15`.

### Recoupling — PASS

No row/column phase or sign fit was performed. Maximum final-M dependence: `6.667118051786499e-16`; maximum `F^T F-I` residual: `1.2228665433368622e-15`; maximum imaginary part: `1.3877787807814457e-16`; each is below the frozen `2e-9` threshold.

### Classical-limit structural sanity — PASS in scope

Maximum projector Frobenius difference between undeformed `q=1` and `k=10000` on the frozen low-spin panel was `8.883991123583906e-4`, below `2e-3`. Raw sign-sensitive coefficient arrays were not compared. This is only an implementation continuity sanity check, not evidence for a continuum quantum-gravity limit.

## Scientific consequence and locks

`implementation_validation_gate_authorized=true` in this bounded solver-validation scope.

Still false: `iter012_retry_authorized`, `eq29_amplitude_authorized`, `bridge_credit`, `candidate_theory_authorized`, `preferred_alpha_found`, `new_physics_found`.

Candidate theory remains **UNFORMED**. ITER020 is separately prospectively preregistered as a held-out/non-retuned transport robustness gate before any direct Eq.(27) reconstruction promotion.