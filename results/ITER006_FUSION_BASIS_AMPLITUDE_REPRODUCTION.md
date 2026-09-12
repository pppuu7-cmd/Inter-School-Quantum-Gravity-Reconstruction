# ITERATION 006 — Pinned Fusion-Basis Amplitude-Level Coarse-Graining Reproduction

Date: 2026-09-12  
GitHub Actions run: `34666262016`  
Status: `SUCCESS / CLEAN THREE-STEP REPRODUCTION / NEAREST-FRAMEWORK CONTROL`

## Source implementation

Pinned public implementation:

- repository: `ssteinhaus/Fusion-basis-coarse-graining`;
- commit: `bb4d1adb1aa81e5090f3ef25a3b9fb8845f19ff4`;
- branch used for the clean pilot: `half_int/no_torsion`;
- source constants: `p=8`, `k=2`.

The implementation performs genuine amplitude-level q-deformed coarse graining with two SVD stages per RG iteration. At each SVD it retains the leading singular direction as an explicit embedding map and uses that map in constructing the next coarse amplitude.

## Execution protocol

For reproducibility and cost control only:

- source RG iteration count was changed from its original value to `3`;
- the source-file autorun was disabled so that each matrix job invokes `main_vec(g)` exactly once;
- no SVD, gluing, amplitude, ribbon-observable, or truncation formula was changed.

Three independent coupling lanes were executed:

`g = 0.0, 0.5, 1.0`.

All three completed all three RG iterations successfully under Julia 1.10.

## Example amplitude-level output

For `g=0.5`, the normalized first-SVD block-leading singular-value matrix at the final iteration was

`[[1, 0, 6.2311e-5], [0, 7.9564e-3, 0], [6.2311e-5, 0, 6.3461e-5]]`,

and the final normalized second-SVD block-leading matrix was

`[[1, 0, 4.5415e-5], [0, 7.9564e-3, 0], [4.5415e-5, 0, 6.3630e-5]]`.

The same run also propagated and printed ribbon-operator expectation values at every RG step.

## Why this matters for ISQGR

This provides an executable amplitude-level **nearest-framework control**. Unlike the RC-006 support-combinatorics audit, this code really constructs coarse amplitudes and dynamical embedding maps via SVD.

It is particularly important as a novelty control because the algorithm explicitly requires the singular-vector embedding map `U`, not only singular values. Therefore a decisive ISQGR test is to preserve the current-step singular spectrum while changing only embedding orientation and observe whether later RG data change.

That counterfactual orientation-null campaign is preregistered separately.

## Claim lock

This source realization is a q-deformed lattice-gauge/fusion-basis coarse-graining model, not a 4D EPRL quantum-gravity amplitude. A positive orientation-null result here would **narrow** ISQGR novelty by showing that orientation-beyond-spectrum is standard amplitude-level TNR structure; it would not strengthen a quantum-gravity claim by itself.
