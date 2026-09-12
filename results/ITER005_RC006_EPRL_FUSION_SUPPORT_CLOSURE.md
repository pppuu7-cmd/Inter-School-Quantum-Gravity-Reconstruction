# ITERATION 005 — RC-006 EPRL/FK Fusion-Support Closure

Date: 2026-09-12  
GitHub Actions run: `34665801653`  
Status: `SUCCESS / SEMANTIC BH-004B SUPPORT / AMPLITUDE CLAIM LOCKED`

## Source realization

Reduced Euclidean `SU(2)_k x SU(2)_k` EPRL/FK-type intertwiner model of Dittrich–Schnetter–Seth–Steinhaus, arXiv:1609.02429.

The source simplicity map used here is

`Y_gamma(l)=((1+gamma)l/2,(1-gamma)l/2)`

for the explicitly non-trivial integer-spin examples discussed in the source.

## Exact support audit

For each source-allowed pair of labels, exact finite `SU(2)_k` fusion support was enumerated in the diagonal label `l` and the `j+`,`j-` sectors. A raw coarse recoupling state `(l,J+,J-)` was retained whenever `l` appears in the `SU(2)_k` fusion support of `(J+,J-)`.

The resulting raw envelope was compared with the source simplicity image `Y_gamma(l)`.

| source case | raw events | leaked events | raw support leak fraction | source target captured | local selector recovery |
|---|---:|---:|---:|:---:|:---:|
| `k=6, gamma=1/3` | 6 | 2 | 0.3333 | YES | YES |
| `k=10, gamma=3/5` | 6 | 2 | 0.3333 | YES | YES |
| `k=12, gamma=1/3` | 71 | 60 | 0.8451 | YES | YES |

All preregistered support-level questions are positive:

- raw recoupling envelope is strictly larger than the source simplicity image in all three cases;
- nonzero support leakage occurs in all three cases;
- every defined source target remains contained in the envelope;
- reapplying the same source-native simplicity selector restores the source support without any closure-target fit.

## Interpretation

At the level of exact fusion support, the reduced EPRL/FK realization exhibits the same *architecture* suggested by causal-set BH-004B:

`physical source support -> overcomplete coarse envelope -> source-native local selector`.

This is a genuine cross-realization semantic recurrence of the envelope/selector decomposition.

## Claim lock

This result does **not** reproduce the q-deformed tensor amplitudes, singular values, or tensor-network RG flow of the source paper. It is a necessary-condition/support-level audit only.

Therefore it does not by itself establish amplitude-level BH-004B universality or a spin-foam continuum/refinement law.
