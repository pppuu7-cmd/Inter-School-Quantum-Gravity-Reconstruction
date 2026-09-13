# ITER016 - RC006 direct authority and convention audit

Date: 2026-09-14. Preregistration commit: `87d9a8a354d7a7e6d43eb262c81a4cdf954328df`.

## Terminal result

**PARTIAL: `RC006_ACTION_TEXT_LOCATED_CONVENTION_AND_VISUAL_QUALIFICATION_PENDING`.**

Explicit finite-dimensional actions were located, a parameter/generator dictionary was derived, and two narrowly scoped algebraic consistency checks were established. This is not a completed source-qualification PASS: several required PDF page images could not be retrieved. The native-HTML cross-check is readable but remains a cross-check, not a substitute independent authority or a finite-level model validation. No new physical model, bridge, amplitude, or Iter012 retry is authorized.

The preregistration follows exploratory candidate discovery. The two algebraic observations below arose during the convention audit; they are post-registration analytical findings, not prospectively enumerated numerical tests.

## 1. Preserve the actual Iter015 failure

Run `34782247507`, aggregate job `103791647383`, terminated with `RC006_OPEN_UQSU2_ACTION_AUTHORITY_DISCOVERY_INFRASTRUCTURE_FAIL`: three arXiv API timeouts and one HTTP 429. Every search lane had an empty `rows` array. Therefore the empty candidate set is not evidence that the required reference does not exist. The GitHub workflow's green status means the failure was recorded successfully; it is not scientific success.

Summary artifact `10325695571`, archive SHA256 `029acd36f96ee520b7bab767a9f68cada978add8490a2682200cf4d1bf4738ce`. Production head `b45e10f15f7793576ef3da8412a79a47fc266578`. Historical Iter013/014 classifications are unchanged.

## 2. Fixed source panel: locators and actual qualification

| Source | Material inspected | Disposition |
|---|---|---|
| V. N. Tolstoy, *Projection operator method for quantum groups*, arXiv:math/0104045v1 | PDF parsed text, printed p.12: (9.1)-(9.3), q-number definition; p.13: (9.13)-(9.14) | Text predicates satisfied: diagonal and both ladder actions, q-number and coproduct. Required page images failed to load; strict qualification **PARTIAL**. No generic coefficient formula imported into code. |
| W. J. Fairbairn and C. Meusburger, *Quantum deformation of two four-dimensional spin foam models*, arXiv:1012.4784v3 | PDF p.4: (1)-(7), visually inspected; p.5: (9)-(14), parsed text only | Action and real-q phase convention located. Page 5 image unavailable, and parsed first line of (9) has an unmatched plus/minus on the eigenvalue. Do not silently correct that line. **PARTIAL**. |
| A. Ballesteros et al., *Deformations of the symmetric subspace of qubit chains*, arXiv:2503.23554v2 | Native HTML, section IV: (61)-(66), (74) | Clear direct diagonal/ladder action and half-exponent q-number, restricted to q>0. **PASS for the isolated action cross-check only; not an independent authority promotion.** Printed HTML antipode sign in (65) fails the compatibility calculation below. |
| B. Dittrich et al., *Coarse graining flow of spin foam intertwiners*, arXiv:1609.02429v2 | Parsed PDF, printed pp.31-32: (A1)-(A9); Eq.(27) location p.22 | Target algebra and coproduct dictionary matched at text level. Required page images could not be retrieved; graphical Eq.(27) was not qualified. **PARTIAL**. |

Primary locators:
- https://arxiv.org/abs/math/0104045v1 ; https://arxiv.org/pdf/math/0104045
- https://arxiv.org/abs/1012.4784v3 ; https://arxiv.org/pdf/1012.4784
- https://arxiv.org/html/2503.23554v2#S4
- https://arxiv.org/pdf/1609.02429v2

The unversioned Tolstoy/Fairbairn PDFs identify v1/v3 in their parsed front matter. The other two target-panel references (1312.0905v2, 1506.04749v3) were not requalified in this checkpoint. External full-text bytes were not acquired in the local runtime, so no source-file SHA256 is claimed. The source locators are pinned, but byte-level source archival remains pending.

## 3. Parameter and generator dictionary

[SOURCE_GROUNDED, textual qualification as above] Use different names for different conventions. Let r be the parameter in Tolstoy/Fairbairn-Meusburger and Q the target parameter in Appendix A of Dittrich et al. Then

\[
Q=r^2,\qquad [x]^{\rm T}_r=\frac{r^x-r^{-x}}{r-r^{-1}}
 =\frac{Q^{x/2}-Q^{-x/2}}{Q^{1/2}-Q^{-1/2}}=[x]^{\rm D}_Q.
\]

Tolstoy's (9.3), with H the weight operator, reads

\[
r^H|j,m\rangle=r^m|j,m\rangle,\qquad
E_\pm|j,m\rangle=\sqrt{[j\mp m]_r[j\pm m+1]_r}|j,m\pm1\rangle.
\]

The directly readable HTML cross-check (74) also states H|j,m> = m|j,m>. Interpreting an exponentiated Cartan action as H itself requires retaining this specified weight basis, not taking an arbitrary matrix logarithm at a root of unity.

[DERIVED_ISQGR, algebraic substitution] Both coproducts become

\[
\Delta(E_\pm)=r^{-H}\otimes E_\pm+E_\pm\otimes r^H
 =Q^{-H/2}\otimes E_\pm+E_\pm\otimes Q^{H/2}.
\]

The order of the two summands is irrelevant; **the tensor legs have not been swapped**. Neither an opposite coproduct nor r -> r^{-1} is required for this dictionary.

Fairbairn-Meusburger's ladder action carries r^{\mp1/2}. Defining

\[
E_+=r^{1/2}J^{\rm FM}_+,\qquad E_-=r^{-1/2}J^{\rm FM}_-
\]

removes those factors. The product of the two rescaling factors equals one, so the commutator is unchanged. Their coproduct (2) is linear and transforms to the same coproduct above. For real positive r their star structure (5) likewise gives E_+^*=E_-; this last statement is **not** continued as a tensor-product unitarity claim to complex r.

For the target root Q=exp(2*pi*i/(k+2)), the proposed branch is r=exp(pi*i/(k+2)); all powers are defined by that exponential, rather than an unspecified complex-square-root routine. This pins an algebraic candidate dictionary, not a proof about fusion truncation, pivotal structure, or the Eq.(27) contraction.

## 4. A useful analytic exclusion: the naive product adjoint

[DERIVED_ISQGR; exact conditional calculation, not a numerical physics run]
Assume H^dagger=H and E_+^dagger=E_- on individual factors, and use the ordinary factorwise Hilbert adjoint. Put K=r^H. At |r|=1 on the stated branch, K^dagger=K^{-1}. Consequently

\[
\Delta(E_+)^\dagger=K\otimes E_-+E_-\otimes K^{-1}
 =\Delta^{\rm op}(E_-),
\]

whereas

\[
\Delta(E_-)=K^{-1}\otimes E_-+E_-\otimes K.
\]

These are not equal in general. For example, with two spin-1/2 factors, let |+> have H-weight 1/2 and let E_-|+>=|->. For z=r^{1/2}, their difference acts on |++> as

\[
(\Delta(E_+)^\dagger-\Delta(E_-))|++\rangle
 =(z-z^{-1})(|+-\rangle-|-+\rangle).
\]

For the target roots with integer k>=2 this is nonzero. This is a counterexample only to retaining this coproduct **and** the naive factorwise adjoint unchanged. It is not a no-go theorem for a unitary fusion category, a ribbon/pivotal pairing, or q-EPRL. Its practical consequence is narrower: do not replace categorical cap/cup and dual contractions by an ordinary absolute square without an explicit compatibility proof.

## 5. Additional source-integrity finding: HTML antipode sign

[DERIVED_ISQGR / REFUTED_IN_SCOPE for the displayed formula set]
The native HTML of Ballesteros et al. gives the same coproduct in (64), but (65) displays S(E_+)=-Q^{-1/2}E_+. Let r=Q^{1/2}, K=Q^{H/2}; then K E_+=r E_+ K. The left antipode identity requires

\[
0=m(S\otimes\mathrm{id})\Delta(E_+)=S(E_+)K+K E_+.
\]

With the displayed minus exponent, the right-hand side instead is

\[
(r-r^{-1})E_+K,
\]

which is nonzero for generic Q>0, Q!=1 in a nontrivial representation. With the same coproduct, the compatible sign is S(E_+)=-r E_+, as in Tolstoy (9.2) and Fairbairn-Meusburger (4). Correspondingly S(E_-)=-r^{-1}E_-.

This establishes inconsistency of the **specific displayed HTML equation set**. Whether it is an original typographical error or a conversion issue was not established; no corrected version was silently substituted and no criticism of the paper's main physical results is inferred. The optional reference remains suitable as an isolated action cross-check, not a wholesale Hopf-convention authority.

## 6. Why the phase gate still exists

[DERIVED_ISQGR, linear algebra] Intertwining alone does not fix an intertwiner's scalar: if Delta(a)i=i*pi(a), then c*i satisfies the same equation. A Hermitian unit norm leaves a U(1) phase; a fixed bilinear self-normalization can reduce the scalar freedom to a sign. If independently specified injection i and projection p obey p*i=id, then i -> c*i, p -> c^{-1}*p preserves that identity.

Thus an action pin, a reality statement, and a dual-pairing identity are different obligations. Fairbairn-Meusburger's textual Wigner convention is not a proof of target Eq.(27) phase cancellation. A next audit must distinguish basis-covariant tensor components from invariant scalar contractions: asking that every tensor component be invariant under arbitrary basis rephasing would be too strong. No claim about the actual graphical contraction is made while its visual inspection is pending.

## 7. Transport defect and executed tests

Static inspection of the Iter015 workflow shows that downloaded e-print bytes are decoded with `src.decode('latin1','ignore')` before any gzip/tar unpacking. It also uses length >1000 as a source-success flag. Compressed source containers and HTML error pages therefore cannot be reliably qualified by that procedure. This is a **latent defect**, not the observed cause of run 34782247507, which stopped earlier at the API stage.

A separate offline decoder is supplied under `code/iter016/`. It bounds input/decompressed/member sizes, keeps source files separate, unpacks gzip and USTAR/PAX containers without filesystem extraction, rejects PDF/HTML/binary payloads, reports encoding fallback, and fails on supported truncation evidence or unsafe archive paths/types. It is not a formula parser or a mathematical authority classifier. Plain-text truncation cannot in general be detected without expected length or an external completeness signal.

Executed locally:

```sh
python -m unittest discover -s code/iter016 -p 'test_*.py' -v
```

**30 synthetic unit tests passed.** Actual stdout/stderr is in `ITER016_DECODER_TEST_RUN.txt`; code/test hashes and runtime are in `ITER016_EXECUTION_MANIFEST.json`. No arXiv network sweep, GitHub physics job, generic q-CG numerical implementation, finite-k physics experiment, q=1 amplitude test, or Iter012 retry was run. The historical workflow was not altered.

## 8. Handoff

Next checkpoint: acquire and visually inspect the missing exact-version equation pages; then qualify the fixed dictionary, finite-k admissibility, phase gauge, and categorical dual pairing against the target graphical identities. Byte-pin source files when retrieval succeeds. Only a subsequent completed convention gate may preregister bounded implementation validation. No automatic search rerun or unqualified coefficient import.

Claim flags remain false: bridge_credit, implementation_validation_gate_authorized, iter012_retry_authorized, eq29_amplitude_authorized, candidate_theory_authorized. Candidate theory remains UNFORMED. Existing administrative readiness values 49/49/0 are preserved; they are not measured probabilities of a successful theory and are not increased by acquiring references.
