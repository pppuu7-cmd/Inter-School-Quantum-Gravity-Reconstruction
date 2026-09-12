# ITERATION 004 — BH-004 Nearest-Known-Framework Audit

Date: 2026-09-12  
Status: `NOVELTY DOMAIN NARROWED / NEW-PHYSICS CLAIM FORBIDDEN`

## Purpose

BH-004 proposes that closure-aware scale transport must carry retained-subspace orientation together with independent scale/measure data. Before treating this as an ISQGR-specific structural advance, compare it against established projected effective dynamics and tensor-network/spin-foam coarse graining.

## 1. Tensor-network renormalization

Evenbly and Vidal, *Tensor Network Renormalization* (arXiv:1412.0732), explicitly insert optimized unitary and isometric tensors during coarse graining in order to remove short-range correlations and obtain a meaningful RG flow in tensor space.

This already demonstrates a mature setting in which **orientation/isometry data of a retained subspace are part of the coarse-graining map**, not merely a scalar running coupling.

Consequence: the generic BH-004 idea “transport more than the spectrum/rank” is not novel by itself.

## 2. Environment-aware tensor truncation

Zhao et al., *Renormalization of tensor-network states* (arXiv:1002.1405), emphasize environment information and projection/truncation structure in determining effective tensor-network states.

Consequence: a claim that closure improves when the retained subspace is chosen with contextual/environmental information has clear prior analogues. BH-004 cannot claim novelty merely because projector orientation matters numerically.

## 3. Spin-foam coarse graining

Steinhaus, *Coarse graining spin foam quantum gravity — a review* (arXiv:2007.01315), frames spin-foam renormalization as deriving effective descriptions on coarser discretizations and stresses the role of boundary data and tensor-network methods in background-independent coarse graining.

Consequence: the use of boundary/subspace data across scale changes is already native to the spin-foam renormalization literature. The direct Lorentzian EPRL orientation-null result is therefore best interpreted as an **ISQGR diagnostic inside an existing broad coarse-graining paradigm**, not as an independent new principle of quantum gravity.

## 4. Projected effective dynamics / Schur-complement logic

Standard projection-operator and effective-Hamiltonian constructions split a state space into retained `P` and discarded `Q=I-P` sectors; effective dynamics generally depend on mixed `P-Q` blocks and resolvent/self-energy corrections. This is structurally close to the exact ISQGR identity

`Delta = P C2 Q C1 P`.

Consequence: the RM-001 spectral-insufficiency theorem is mathematically useful for the ISQGR programme, but its abstract algebraic content is not a claim of new mathematical physics.

## 5. What remains potentially distinctive

After this audit, the only defensible possible novelty domain is much narrower:

1. a **source-native** quantum-gravity realization must define `P_s` without closure-target optimization;
2. `P_s` orientation transport and scalar measure/normalization flow must separate empirically or analytically;
3. a frozen transport law inferred at training scales must predict closure on an unseen refinement level;
4. the law must preserve the realization's physical/gauge/causal constraints;
5. it must outperform standard rank/spectrum-only and relevant tensor-network/effective-theory baselines;
6. a second independent QG realization must reproduce the same nontrivial transport law or an exact derivation must explain why the law is universal.

Only a result at this narrower level could become a credible ISQGR-specific bridge contribution.

## 6. Current verdict

`BH-004_GENERIC_PROJECTOR_AWARENESS = KNOWN_STRUCTURE`

`BH-004_QG_SPECIFIC_TRANSPORT_LAW = OPEN`

`NEW_PHYSICS = NOT ESTABLISHED`

`CANDIDATE_THEORY = UNFORMED`

The active scientific value of BH-004 is therefore not the statement that projectors matter. It is the **held-out, source-native, constraint-preserving scale-transport test** that can determine whether a non-arbitrary QG-specific law exists.

## Sources

- G. Evenbly, G. Vidal, *Tensor Network Renormalization*, arXiv:1412.0732.
- H. H. Zhao et al., *Renormalization of tensor-network states*, arXiv:1002.1405.
- S. Steinhaus, *Coarse graining spin foam quantum gravity — a review*, arXiv:2007.01315.
