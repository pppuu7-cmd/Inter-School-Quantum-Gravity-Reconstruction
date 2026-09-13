# ITER017 - RC006 phase / dual-pairing qualification

Date: 2026-09-14  
Preregistration commit: `fe11ca9c2b71e7561beb4aca12ee795dc909ca70`

## Terminal classification

`RC006_DUAL_PAIRING_AND_PHASE_GAUGE_SOURCE_QUALIFIED_EQ27_VISUAL_PENDING`

This is a scoped source/algebra PASS for the abstract dual-pairing and residual phase-gauge obligations, but **not** a completed Eq.(27) convention pin and not an implementation authorization. The exact Eq.(27) graph could not be visually inspected in this checkpoint because the PDF screenshot transport returned cache-miss errors. The text layer and the previously frozen TeX source establish the Appendix-B identities, but the exact topology of every contraction in Eq.(27) is not inferred from broken visual transport.

A second independent limitation is now explicit: Fairbairn-Meusburger's root-of-unity modular-category section assumes a primitive `r`th root with `r>2` odd. Under the cutoff dictionary `r=k+2`, it therefore directly covers odd target `k` only and **does not directly qualify the first non-trivial target case `k=12`**. No analytic continuation or even-r repair is silently imported.

Always false at this checkpoint: `implementation_validation_gate_authorized`, `bridge_credit`, `iter012_retry_authorized`, `eq29_amplitude_authorized`, `candidate_theory_authorized`.

## 1. Frozen target identities are stronger than the Iter014 parser reported

The target source is Dittrich, Schnetter, Seth and Steinhaus, arXiv:1609.02429v2.

Appendix A fixes:

- `q = exp(2*pi*i/(k+2))` and admissible `0 <= j <= k/2` in (A3)-(A4);
- the coproduct in (A5);
- the root-of-unity coupling conditions in (A7), including `j1+j2+j3 <= k`;
- the bilinear completeness/orthogonality conventions in (A8)-(A9).

Appendix B then supplies the missing duality data internally:

- (B1) interprets `qC` as a map `V_j1 tensor V_j2 -> V_j3`;
- (B2) defines the cap by `(-1)^(j-m) q^(m/2) delta_(m,-m')`;
- (B3)-(B4) define the cup by the requirement that cup/cap concatenation is the identity;
- (B5) constructs the Clebsch-Gordan map for inverse (complex-conjugate) deformation parameter `qbar` by bending a leg with cup/cap;
- (B6) returns to the original map;
- (B7) states that concatenating the dual pair is proportional to the identity;
- (B8)-(B11) use `qC` and `qbar C` together in the Haar projector and its dual.

This is categorical/bilinear duality data, not a prescription to take an ordinary Hilbert-space absolute square.

### Historical parser false negative

The frozen Iter014 cap/cup job downloaded the exact source panel successfully. Its recorded source archive hashes were:

- `1609.02429v2`: `sha256:3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`
- `1312.0905v2`: `sha256:69334656117892b255ebb9b0c3855b6387bafc630bb9345b084e5434e22294c0`
- `1506.04749v3`: `sha256:758e05bf73390015fb02f374c69892ad155c8edacb40a97876c12aa7f64c1e14`

Its raw-TeX anchor actually contains the sentence defining the inverse/complex-conjugate deformation parameter `\bar{q}` and the surrounding cup/cap diagrams. The old boolean `qbar_duality=false` was therefore a regex/parser false negative: the matcher accepted forms such as `\\bar q` but not the braced TeX form `\\bar{q}`. Historical Iter014 is **not** retroactively reclassified; its terminal blocker was the missing representation-action authority in any event.

## 2. Exact cap/cup identity check

[DERIVED_ISQGR, exact symbolic bookkeeping]

Using the target formulas

`cap(m,m') = (-1)^(j-m) q^(m/2) delta_(m,-m')`

and

`cup(m',m'') = (-1)^(j+m') q^(m'/2) delta_(m',-m'')`,

the two deltas force `m'=-m` and `m''=m`. The product then has

- sign exponent `(j-m)+(j-m)=2(j-m)`, an even integer;
- q exponent `m/2 + (-m)/2 = 0`.

Hence the concatenation is exactly `delta_m^(m'')`, independently of a numerical value of q wherever the displayed formulas are defined.

The bounded checker exhaustively verified all magnetic components for `j=0,1/2,...,6`: **819 cases, 0 failures**.

## 3. Bilinear normalization reduces phase freedom to a sign

[DERIVED_ISQGR from target (A9)]

The target orthogonality relation is bilinear in two copies of the same q-CG convention; it does not place a complex conjugation on one factor. For one normalized fusion channel, rephase

`C -> lambda C`.

The left side of (A9) then scales by `lambda^2`, while the fixed nonzero right side does not. Therefore preserving the target normalization requires

`lambda^2 = 1`,

so the allowed scalar freedom is reduced from a generic complex/U(1) phase to `lambda = +/-1`.

This matters for the phase-gauge question. The source-defined dual map in (B5)-(B6) is constructed from the same normalized channel using cup/cap. Under the surviving sign redefinition, both paired maps acquire the same sign, and a paired composition acquires `lambda^2=1`. Thus the abstract closed dual contraction is invariant under the remaining normalized sign gauge.

This proves only the **abstract phase-gauge cancellation for correctly paired source-defined dual maps**. It does not prove that every q-CG occurrence in the graphical Eq.(27) is paired in precisely this manner; that topology remains the visual gate.

## 4. Finite-level fusion rule: exact match, but a domain mismatch at even k

The target coupling conditions (A7) are equivalent to the familiar truncated fusion interval

`|j1-j2| <= j3 <= min(j1+j2, k-(j1+j2))`,

with the usual half-integer parity condition.

Fairbairn-Meusburger arXiv:1012.4784v3 gives at root of unity

`|I-J| <= K <= min(I+J, r-2-(I+J))`  (93),

for simple objects `0 <= J <= (r-2)/2`.

Under `r=k+2`, the intervals and label ranges coincide exactly. The bounded exhaustive checker compared every allowed spin triple for `k=1,...,16`: **23,408 cases, 0 mismatches**.

However Fairbairn-Meusburger explicitly assumes in this Euclidean root-of-unity section

`q = exp(2*pi*i/r), r>2 odd`.

Therefore `r=k+2` maps that independent source only to odd target `k`. The target paper explicitly identifies `k=12` as the smallest level where the non-trivial EPRL map relevant to its normalization appears. `k=12` corresponds to `r=14`, outside Fairbairn-Meusburger's stated odd-r scope.

Disposition: **fusion-form equivalence PASS algebraically; independent even-k convention authority remains PARTIAL/BLOCKED.**

## 5. Phase conventions from Fairbairn-Meusburger: useful but not silently transferable

In the generic-q section of arXiv:1012.4784v3, the authors impose a reality condition on Clebsch-Gordan coefficients and then Wigner's convention to fix the remaining sign ambiguity (13), followed by orthogonality relations (14). This is a genuine phase/sign convention source.

But that section assumes real positive `q=e^{-kappa}`. The root-of-unity section later changes the algebraic setting, star structure and representation category. It is therefore not source-qualified to simply carry the generic real-q reality condition unchanged to the target unit-modulus root, particularly at even target k outside the root section's odd-r domain.

The target paper itself states that its notation/conventions are taken from Biedenharn and Lohe, *Quantum Group Symmetries and q-Tensor Algebras* (1995), and its Appendix-B footnote states that its `qC` is a quantum-dimension modification of the standard coefficient defined there. This preserves the external-reference provenance already identified in ITER013; no inaccessible coefficient formula is imported here.

## 6. Eq.(27) and EPRL normalization: what is established and what is not

The target text layer locates Eq.(27) and states immediately afterward that the normalization constant is computed by contracting `T_EPRL` with itself, that the normalization depends only on quantum dimensions, and that the two displayed diagrams give the same expression. Appendix E evaluates this contraction with the graphical identities of Appendix B and obtains (E3), including explicit sign and quantum-dimension factors and a Kronecker delta; (E4) fixes the corresponding normalization.

This is strong evidence that the intended normalization is the source-defined graphical/bilinear one rather than an arbitrary Euclidean modulus square.

Nevertheless the acceptance criterion in the preregistration required readable visual evidence for the **specific topology** of Eq.(27). The web PDF text layer preserves labels and factors but not enough edge connectivity to certify every pairing. Screenshot calls for the relevant exact-version PDF pages returned cache-miss transport errors, and local PDF acquisition did not succeed. No diagram topology is reconstructed from guesswork.

Therefore the stronger terminal class `RC006_PHASE_DUAL_PAIRING_CONVENTION_PINNED_SCOPED` is **not** reached.

## 7. Executed checker

Command:

```sh
python iter017_check_phase_dual_pairing.py
```

Results:

- cap/cup exact identity: 819 component cases, 0 failures;
- A7 versus FM (93), with `r=k+2`: 23,408 spin-triple cases for `k=1..16`, 0 mismatches;
- normalized phase freedom from A9: residual `+/-1` sign;
- paired source-defined dual contraction under that residual sign: invariant;
- fitted phases: 0;
- physics amplitude runs: 0.

Code SHA256: `cbee9130e4cb1cecae28fb5fd2a3610f50c94bd70055e0f3972afb486912ab8f`.  
Run-log SHA256: `67cacf7279b8da0c2885c5b8b064f1705addc0bbede2505cedf07b223ec80c77`.

## 8. Scientific handoff

The broad RC006 blocker has narrowed again. It is no longer correct to say merely that cap/cup or qbar duality is absent from the open target source. Those identities are source-qualified. The remaining admissible gate is narrower:

1. obtain readable exact-version visual/source-graph evidence for Eq.(27) and translate its graph to an explicit component contraction without changing conventions;
2. verify that every convention-dependent q-CG sign in that contraction is paired/gauge-covariant as required by Appendix B;
3. for the physically first non-trivial level `k=12`, acquire an even-k root-of-unity convention authority or establish the needed convention directly from the target source without borrowing Fairbairn-Meusburger's odd-r restriction;
4. only then preregister a bounded q-CG implementation validation.

No Iter012 rerun, Eq.(29)/Lambda amplitude, alpha selection, bridge credit, candidate construction, RQIR promotion or KMQGB promotion is authorized.
