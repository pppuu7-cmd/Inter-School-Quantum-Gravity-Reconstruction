# ITERATION 006 — RC-006 Appendix-B13 source-to-kernel mapping

Date: 2026-09-12  
Status: **PASS — SOURCE/CONVENTION BRIDGE FOR B13/B16 USE ONLY**  
Candidate theory: `UNFORMED`

## Frozen question

Does an independent source-side implementation of Appendix-B Eq. (B13) agree with the pinned normalized `sixjr()` recoupling object from `ssteinhaus/Fusion-basis-coarse-graining` at the source-relevant levels k=6,10,12?

Frozen per-case gate:

`absolute_error <= 1e-11 OR relative_error <= 1e-11`

for every admissible integer-sector sextuple.

## Provenance

- source-mapping implementation precursor: `442f3bb3304cc9b07947cf980db1499cd3880dc1`;
- authoritative workflow head: `b5d8f709d4200e71b41137c67c3c89bd40ab1682`;
- GitHub Actions run: `34694997395`;
- aggregate job: `103556894034`;
- aggregate artifact: `10298094519`;
- aggregate artifact SHA256: `ecb16a4dac552d6427aacda7f66048da4bb674e47628e5dd0cf42005e03629b1`.

## Results

- k=6: 224 admissible sextuples, 0 bad, max absolute error about `1.17e-15`;
- k=10: 2248 sextuples, 0 bad, max absolute error about `3.22e-15`;
- k=12: 5537 sextuples, 0 bad, max absolute error about `3.72e-15`.

Total: **8009 tested, 0 frozen-gate violations**.

The relatively large reported maximum relative error for k=12 occurs only where both compared coefficients are essentially zero; the prospectively frozen OR gate is satisfied by the absolute-error branch, so this is not a post-hoc tolerance rescue.

## Permission granted

The pinned `sixjr()` may be used for source graph factors that have been explicitly reduced through the paper's Appendix-B B13/B16 identities.

## Permission not granted

This result does not authorize treating the full Eq. (29) EPRL graphical factor as a simple product of `sixjr()` objects. The source states that the EPRL diagrams are nontrivial; Appendix F derives them using B15 plus the R-matrix identity. The full oriented/braided graph must therefore be mapped before a numerical Eq. (29) amplitude is claimed.

No Appendix-C RG/TNR result, refinement law, continuum statement, bridge derivation, or new-physics claim follows from this qualification.
