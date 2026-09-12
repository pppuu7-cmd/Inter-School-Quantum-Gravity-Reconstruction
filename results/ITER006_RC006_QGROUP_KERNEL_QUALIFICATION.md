# ITERATION 006 — RC-006 q-group kernel qualification

Date: 2026-09-12
Status: **NUMERICAL KERNEL QUALIFIED FOR VALIDATED RECOUPLING/FUSION IDENTITIES; EPRL AMPLITUDE STILL OPEN**
Candidate theory: `UNFORMED`

## Purpose

Before reusing the independently published q-deformed numerical kernel from
`ssteinhaus/Fusion-basis-coarse-graining` (pinned at commit
`bb4d1adb1aa81e5090f3ef25a3b9fb8845f19ff4`) in a source-equation implementation
of RC-006 (`arXiv:1609.02429`), qualify the conventions used for SU(2)_k fusion
and recoupling.  This is a permission gate, not an EPRL amplitude/RG result.

The paper's source-listed nontrivial EPRL maps are:

- k=6, gamma=1/3: l=3 -> (j+,j-)=(2,1);
- k=10, gamma=3/5: l=5 -> (4,1);
- k=12, gamma=1/3: l=3 -> (2,1), l=6 -> (4,2).

## First qualification run — raw tetrahedral-symmetry gate

Implementation commits:

- initial qualification code: `870b43771183c50a04f08a874be018ca4f1bd5e0`;
- workflow: `601ca2150edd4b44ab96d1d948a4b123aa30d02e`;
- include-path-only fix: `5581a9f940178f2e934ee82ad4c7370fc4d7f8c4`;
- Julia soft-scope-only fix: `9392b86e6ad92888909695f08f9b85963411ddfe`.

Authoritative completed run: `34694452688`.
Aggregate job: `103555441761`.
Aggregate artifact: `10297988834`, SHA256
`21d89684220ddb0e82ff7a8e33643e3f145a3e93a1a8022e3c94cc020c42fa77`.

Common checks:

- exact fusion associativity: PASS at k=6,10,12;
- quantum-dimension fusion identity: PASS with max relative errors O(1e-15);
- source EPRL admissibility maps: exact PASS at k=6,10,12.

The initial bare tetrahedral-symmetry test passed at k=6 and k=10 but failed at
k=12: 53/5537 tested cases exceeded the 1e-9 threshold, with maximum relative
difference `0.007111994048949036`.  Therefore the original aggregate permission
gate returned false.

This was retained as a qualification failure and not silently removed.

## Convention audit — actual recoupling-matrix identity

Inspection of the pinned TNR implementation shows that `sixjr()` is used directly
as a normalized basis-transformation coefficient.  Since the implementation
already includes the relevant square-root quantum-dimension normalization in
`sixjr`, the convention-relevant self-consistency test is the orthogonality of the
admissible recoupling matrix, not an assumed bare Wigner-6j tetrahedral symmetry.

Frozen follow-up implementation:

- diagnostic code: `b87e2b8d409d78fa460b90dc681b5914352f7fcf`;
- workflow: `f7ee8b0e8cc08305723d5827789be8d36aac625c`.

Authoritative run: `34694602675`.
Aggregate job: `103555842825`.
Aggregate artifact: `10298547764`, SHA256
`a271a9de96dbf77dea0ec9b68b9480c0d0edd666c29ae7e3e89739eb93055f5e`.

Frozen gate:

`max(||M M^T-I||_inf, ||M^T M-I||_inf) <= 1e-9`

for every nontrivial square admissible recoupling block.

Result: **PASS 3/3 levels**.

- k=6: 16 nontrivial square blocks, 0 bad; max errors about 1.50e-15;
- k=10: 216 blocks, 0 bad; max errors about 3.72e-15;
- k=12: 505 blocks, 0 bad; max errors about 2.47e-15.

Thus the earlier k=12 raw tetrahedral-symmetry failure is classified as an
**inappropriate convention test for this normalized `sixjr` object**, not a
breakdown of the recoupling kernel.

## Permission granted / permission not granted

Granted:

- reuse this pinned kernel for SU(2)_k fusion rules, quantum dimensions,
  source-listed EPRL admissibility maps, and recoupling operations that are
  directly covered by the successful orthogonality qualification.

Not granted:

- claiming reproduction of Eq. (29), the EPRL initial tensor;
- claiming reproduction of Appendix-C renormalization flow;
- inventing graphical/phase conventions not explicitly mapped to the source;
- `BRIDGE_DERIVED`, continuum, or new-physics claims.

The next scientifically allowed RC-006 step is a source-faithful translation of
the Eq. (29) EPRL intertwiner graphical factor into the validated q-recoupling
objects, followed by a minimal k=12 amplitude check and only then Appendix-C
coarse graining/SVD.
