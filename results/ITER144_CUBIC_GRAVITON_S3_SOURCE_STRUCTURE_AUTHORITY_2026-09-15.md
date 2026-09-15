# ITER144 terminal result — cubic graviton S3 source-structure authority

Date: 2026-09-15
Preregistration: `b5cca192140f7c811de4204b7ad7bb2bddc0e923`
Initial implementation: `323067f4566e1e33875869ca4da28255259426c2`
Initial workflow: `8ec2d58de9b38bd264932c1088bc788b57dc44b3`
Initial run: `34959264987`, job `104348687916`
Initial artifact: `10392527445`, SHA256 `783a31f7c15b6c2c661c2cee6b3ef37dc68280f2f0d4da5ba1a88449ff3530bc`
Parser-only correction: `352036749146ddc3e3e81eaa8c897861b357f1b1`
Authoritative retry workflow head: `49a502591e8fa7832a71f1cb8fd8fa4069fc7a69`
Authoritative retry run: `34959433249`
Job: `104349227963` (`s3-source-structure-audit-retry`)
Artifact: `10392756699` (`iter144-cubic-graviton-s3-source-structure-authority-retry`)
Artifact SHA256: `769e4fca32dff3bddc3024fed05d0b58f97d5858c47ad52808e8525c86fa159c`

## Scientific classification

`PASS_SCOPED_CUBIC_GRAVITON_S3_TENSOR_STRUCTURE_SOURCE_AUTHORITY_GLOBAL_PHASE_OPEN`

## Source integrity

Pinned machine source:

- repository `BorisNLatosh/FeynGrav`;
- commit/tree head `91f697a1ca62fd051cbb297827cb1a491b393538`;
- file `Libs/GravitonVertex_1`;
- expected Git blob SHA `98297aac3b640a93ac80c2cc72a8275280819954`;
- observed Git blob SHA `98297aac3b640a93ac80c2cc72a8275280819954`.

The machine source contains 231 parsed terms after stripping the common `I*kappa` factor.

Published convention context remains David Prinz, arXiv:2004.09543 and arXiv:2208.14166. The FeynGrav package documentation states that its conventional gravity gauge parameter controls the propagator and does not enter `GravitonVertex`; this gate therefore credits only the cubic pure-gravity vertex tensor structure, not a propagator normalization.

## Frozen structural checks

All pass exactly:

- pinned source hash;
- parser accepts only the preregistered Pair/LorentzIndex/Momentum grammar;
- exactly three graviton leg index-pairs and momenta `p1,p2,p3` occur;
- every source term has total momentum degree 2;
- all six graviton-leg permutations agree on deterministic momentum-conserving panels;
- each graviton pair is symmetric under `m_i <-> n_i`;
- at least three nonzero independent source/EH panel ratios exist;
- the source-to-independent-Einstein-Hilbert ratio is one constant nonzero value on all such panels;
- target-blind construction.

## Independent Einstein-Hilbert check

The independent lane reconstructs the cubic coefficient of the Gamma-Gamma form of `sqrt(g) R` using three plane-wave perturbations and momentum conservation, without calling or rewriting the FeynGrav expression. Comparison panels use purely spatial momenta and spatial polarization indices in D=4 so the spatial Minkowski/Euclidean signature signs occur in even contraction count and do not generate relative panel-dependent signs.

The exact constant ratio is

`FeynGrav_source / independent_GammaGamma_cubic = -2`.

The constancy, rather than its sign, is the scientific result of this gate. The factor is consistent across all nonzero held-out panels and leg permutations.

## Attempt-1 adjudication

The initial run returned `BLOCKED_CUBIC_GRAVITON_SOURCE_INTEGRITY_OR_SYNTAX` even though the pinned blob hash matched. Artifact inspection showed that the only issue was a technical nested-comma parser defect: the generic Pair regex split inside `LorentzIndex[...,D]`. The retry changed only Pair parsing within the already frozen grammar. No source, panel, physical predicate or acceptance threshold changed.

## What is now authorized

The pinned three-graviton S3 **tensor structure** may now be used prospectively for interaction-dressed derivative allocation and numerator construction.

The absolute Euclidean action/Feynman-rule phase/sign/normalization remains open. A later convention gate must combine the action sign, Wick rotation and propagator normalization before any physical B1 sign or coefficient can use the overall factor.

## Claim ceiling

No loop pole, B1, noncancellation result, finite B0, EDT comparison, bridge, new physics or candidate theory is established. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
