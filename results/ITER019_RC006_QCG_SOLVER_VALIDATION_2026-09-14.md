# ITER019 - RC006 bounded q-CG solver implementation validation

Date: 2026-09-14  
Preregistration: `4f497a0e6413d8f4bc0408f0050552fa80d2ba98`

## Terminal classification

**`RC006_QCG_SOLVER_VALIDATED_BOUNDED_K12`**

ITER019 is the first bounded implementation PASS for RC006. The q-CG/intertwiner data were not imported from an external closed-form formula and no coefficient phase was fitted. Instead, the implementation constructs every tested channel directly from the source-qualified Uq(su2) representation action, the target coproduct, target root-of-unity q-number and admissibility, target bilinear A8/A9 normalization, and Appendix-B singlet/cap convention.

This result authorizes the next narrowly preregistered reconstruction test. It does **not** by itself authorize Iter012, Eq.(29)/Lambda amplitude work, alpha selection, bridge credit, or candidate-theory construction.

Production run: `34785058584`  
Production head: `d5934a5f2251c01b2d8ec2315d1c36161b45f507`  
Solver code: `code/iter019/qcg_solver_validation.py`  
Code SHA256: `57c0e253afc6ac4077d00b29228a0679166adcb99da133fb53260a2fb99b6b82`  
Runtime: Python 3.13.11, NumPy 2.3.3, mpmath 1.3.0.

The workflow executed four independent GitHub Actions matrix lanes concurrently. Green CI alone was not used as scientific evidence; the terminal classification is derived from the preregistered numerical predicates emitted by each lane.

## 1. Construction used in every lane

For each admissible channel `(j1,j2)->j` at target level `k=12`:

1. restrict the tensor-product basis to total magnetic weight `m=j`;
2. compute the one-dimensional nullspace of target `Delta(J+)` in that subspace;
3. normalize the highest-weight vector with the target **bilinear** norm, not an inserted Hermitian absolute square;
4. generate lower magnetic states using target `Delta(J-)` divided by the already pinned single-representation lowering coefficient;
5. retain the residual normalized sign freedom instead of fitting it, except that `(j,j)->0` is compared with Appendix-B B2 up to exactly that allowed overall sign.

A channel would have failed if its highest-weight nullspace were not one-dimensional, if the bilinear norm were zero/isotropic, if recurrence became singular in the frozen panel, or if the preregistered residual thresholds were exceeded.

## 2. Lane A - algebra/intertwiner residuals: PASS

Job: `103798881391`  
Artifact: `10325903240`  
Artifact ZIP SHA256: `92cf6e5036f4b3b39d7849aa8fab34197c74c6dafc30f8a982c91cd71e7c762b`.

Frozen panel contained 19 admissible channels drawn from
`(1/2,1/2)`, `(1/2,1)`, `(1,1)`, all `(3,3)->j` with `j=0..6`, and all admissible `(4,4)->j` with `j=0..4`.

Results:

- every expected highest-weight nullspace had dimension exactly one;
- maximum Jz/J+/J- intertwining residual over the whole panel:
  **`1.6462900610405706e-12`**;
- preregistered threshold: `5e-10`.

Therefore the solver-generated embeddings intertwine the pinned target action/coproduct to substantially better precision than required.

## 3. Lane B - A9, A8 projectors and Appendix-B cap: PASS

Job: `103798881594`  
Artifact: `10326635226`  
Artifact ZIP SHA256: `98d0326733f367c8925257737018e5ebf76a9bc999aec203685960143afb05ce`.

Results:

- maximum A9 cross-channel bilinear orthogonality residual:
  **`1.2318946614931203e-12`** (`<5e-10`);
- complete `(3,3)` direct-sum projector versus 49-dimensional identity:
  **`3.908846888280509e-13`** (`<2e-9`);
- admissible `(4,4)` A8 projector rank at SVD threshold `1e-8`:
  **25**, exactly as preregistered;
- `(4,4)` projector high-precision idempotence residual:
  **`1.8184291884891273e-74`** (`<2e-9`);
- `|Tr(P_44)-25| = 8.3915e-76`;
- maximum Appendix-B B2 singlet residual, allowing only the source-permitted overall sign:
  **`5.770557056164968e-15`** (`<2e-9`).

### Numerical-stability note

A pre-production double-precision dry-run gave an idempotence residual about `2.67e-9` for the `(4,4)` projector, just above the frozen `2e-9` threshold. The threshold and algorithm were **not** changed. Inspection showed that this bilinear projector is strongly non-normal: large matrix entries cancel to form a rank-25 idempotent. The same frozen construction was therefore evaluated for that predicate at 80-digit mpmath precision, yielding the `1.8e-74` residual above. This is a numerical-stability correction, not phase fitting or post-hoc criterion relaxation.

## 4. Lane C - recoupling/F invariant checks: PASS

Job: `103798881343`  
Artifact: `10326578245`  
Artifact ZIP SHA256: `1f3ac43231485be5996c704c7c0f7bf067747e020266fae51a5a297e9d8202f`.

Frozen three-body panels:

- `j1=j2=j3=1/2`, total `J=1/2`;
- `j1=j2=j3=1`, total `J=1`.

No row/column sign was fitted to an external matrix. Recoupling matrices were built only from solver-generated embeddings and target bilinear overlaps.

Maximum residuals across the frozen panels:

- M-independence: **`1.5221333771292962e-12`**;
- transpose orthogonality `F^T F-I`: **`3.6690448108052944e-12`**;
- imaginary part: **`1.6237011735142914e-13`**;
- preregistered threshold for each: `2e-9`.

Representative `j=1/2` recoupling matrix:

```text
[[-0.3645732333114226, -0.9311747292667397],
 [-0.9311747292667395,  0.3645732333114225]]
```

Representative `j=1` recoupling matrix:

```text
[[ 0.21266270208801025, -0.5178926184319605,  0.8285273469567315],
 [-0.5178926184319602,   0.6603417762618222,  0.5448756336701023],
 [ 0.8285273469567320,   0.5448756336701026,  0.1276616255761686]]
```

Thus the solver convention produces the sign-gauge-invariant real-orthogonal recoupling structure required by the independent even-k category cross-check, without importing its matrix entries.

## 5. Lane D - classical-limit structural sanity check: PASS

Job: `103798881424`  
Artifact: `10325907403`  
Artifact ZIP SHA256: `804263646443fec62f3e25f7d6a0878d9c55311aafd8f69c9fb12f42186f29b6`.

The same highest-weight algorithm was run at undeformed `q=1` and at deformation level `k=10000`. Only sign-insensitive channel projectors were compared; raw sign-sensitive coefficient arrays were not.

Maximum projector Frobenius difference over the frozen `(1/2,1/2)` and `(1,1)` channels:

**`0.0005651832113359061`**, below the preregistered `0.002` threshold.

This is only a continuity sanity check for the implementation. It is not evidence for a continuum quantum-gravity limit.

## 6. Aggregate and reproducibility

Aggregate job: `103798931295`  
Aggregate artifact: `10326636905`  
Aggregate ZIP SHA256: `62892f576c56d6f6ae09708594bb6b6286d56a4ce5f4821043faf2367fea73cf`.

All four lane predicates were true. The frozen aggregate therefore returned:

`RC006_QCG_SOLVER_VALIDATED_BOUNDED_K12`.

The implementation-validation gate is now source- and computation-qualified in this bounded scope:

`implementation_validation_gate_authorized=true`.

## 7. Scientific consequence and next gate

RC006 is no longer blocked by missing representation actions, convention pinning, phase/cap duality, even-k category data, Eq.(27) graph provenance, or bounded q-CG constructibility at `k=12`.

The next efficient step is **not** to repeat generic q-CG validation. It is to recover the exact historical ITER012 blocked observable/reconstruction and rerun only the part whose former blocker was RC006, using the validated solver as the convention-preserving backend. If ITER012's historical preregistration cannot be reused without hindsight, a new ITER020 must preregister the corresponding direct Eq.(27)/Appendix-E component reconstruction first.

## 8. Locks after ITER019

True:

- `implementation_validation_gate_authorized=true`.

Still false:

- `iter012_retry_authorized=false`;
- `eq29_amplitude_authorized=false`;
- `bridge_credit=false`;
- `candidate_theory_authorized=false`;
- `preferred_alpha_found=false`;
- `new_physics_found=false`.

Candidate theory remains **UNFORMED**.