# RM-001 — Retained-Sector Orientation Is Composition-Closure Data

Date: 2026-09-12  
Status: `RECURRENT_MOTIF_ACCEPTED / BRIDGE NOT YET DERIVED`  
Primary interface class: `IF-04 COMPOSITION/GLUING`  
Secondary interface: `IF-08 CONTINUUM/COARSE-GRAINING`  
Claim level: `DERIVED_ISQGR + NUMERICALLY_VERIFIED`  

## Motif

A reduced description is not specified, for composition purposes, by retained dimension or operator spectrum alone. The **orientation of the retained/source-defined subspace relative to the dynamics/composition operators** carries independent information controlling discarded-sector leakage and return.

Equivalently, a viable coarse-graining map must in general transport at least

`(retained subspace orientation, scale/measure data)`

rather than only a scalar cutoff, rank, or spectrum.

This is a recurrent structural motif, not a theory equation and not a new-physics claim.

## Chain A — causal-set SSEE / Pauli–Jordan sector

Source lineage: causal-set spacetime entanglement, Pauli–Jordan/Wightman construction, with the frozen source spectral rule

`|lambda(iDelta)| >= sqrt(N)/(4*pi)`.

Relevant completed diagnostics:

1. **BH-001 × BH-003 spectral-closure bridge**: over 16 causal-set realizations, the source spectral sector beat every rank-matched Haar control for both one-step leakage and two-step return. Overall random/source improvement was about `3.20x` for leakage and `6.70x` for sequential return defect.
2. **Source-sector thinning**: under Bernoulli thinning, source-sector overlap remained about `0.976` and mean principal cosine about `0.988`, despite a nontrivial rank/scale shift.
3. **Corrected thinning scale-flow test**: native spectral scale transport inferred an exponent near `1.03`, not the source SSEE exponent `1/2`. Thus subspace geometry transfers substantially better than the raw scalar spectral scale.
4. **Held-out stability-to-closure prediction**: coefficients were fit on seeds `93,94,101,102` and scored on unseen seeds `201,202,203,204`. Adding mean principal cosine reduced held-out RMSE from `0.11822` to `0.08534` (`0.7218x` baseline), while normalized projector distance did not improve prediction (`1.0163x` baseline).
5. **Mass-deformation closure boundary**: the frozen massless source projector loses its rank-matched return advantage across the independently refined transition between roughly `mu=1.31` and `mu=1.44`, showing that the closure advantage has a finite deformation domain rather than being a universal projector artifact.

Interpretation of Chain A: the direction/orientation of the source sector contains closure-relevant information that is not captured by rank or a single scalar scale-flow law.

## Chain B — pinned SU(2) BF vertex orientation null

Source lineage: pinned `sethkasante/su2bf-TNAlgo` realization at commit `2460cda77b8fe27a4106e98bf39a94fa9059bc92`.

Construction:

- define the retained basis from the undeformed train vertex;
- construct paired holdout operators from independent boundary-state deformations;
- apply the **same unitary similarity** to both holdout operators.

The shared unitary preserves each holdout singular spectrum and their mutual pair structure while scrambling only their orientation relative to the frozen train-defined projector.

Completed campaign:

- spins `j=3, 4.5, 6`;
- six ordered deformation pairs per spin;
- `18` cases and `162` rank tests;
- return improvement over the orientation-scrambled null was `>1` in `100%` of rank tests;
- minimum return improvement `1.0148`;
- median improvement `2.6608`;
- mean improvement `3.6620`;
- in `98.77%` of rank tests, more than half of shared-unitary null draws had worse return than the source-aligned case.

Interpretation of Chain B: preserving operator spectra and pair structure is insufficient to preserve closure performance. Relative orientation to the retained source/train sector is an independent variable.

## Independence audit

The two chains are independent at the source-realization level:

- Chain A uses a causal-set Pauli–Jordan/Wightman realization and stochastic sprinklings;
- Chain B uses a pinned SU(2) BF tensor-network vertex implementation and boundary-state deformations;
- they do not share a continuum effective action, numerical ensemble, spectral cutoff, or source repository.

They **do** intentionally share the ISQGR closure diagnostic language (`P`, `Q=I-P`, leakage/return). This is a common comparator, not a shared physical derivation. Therefore the recurrence claim is limited to the common interface statement about retained-sector orientation.

SU(2) BF is not EPRL gravity, so Chain B may not be used to claim an EPRL or GR result.

## Same-semantic-level test

Both chains ask the same IF-04 question:

> after a retained sector is frozen from source-native data, does changing only its relative orientation to the composition/dynamics operators change discarded-sector return?

Chain A answers this through source-sector stability and held-out closure prediction; Chain B isolates orientation by a shared-unitary null that leaves spectra unchanged.

This is narrower than MC-001 (`physical constraint sector not automatically closed under scale flow`) and does not automatically promote MC-001.

## Falsifiable structural consequence

Any future bridge principle based on this motif must carry an explicit projector/subspace-transport law, not only a scalar cutoff or running coupling.

A minimal abstract object is

`E_s = (P_s, mu_s)`

with coarse-graining transport

`T_{s->s'} : (P_s, mu_s) -> (P_{s'}, mu_{s'})`,

where `P` transports retained-sector orientation and `mu` represents scale/measure/normalization data. This is notation for a requirement, not a proposed fundamental theory.

The motif would be weakened or rejected if independent source-defined realizations show that closure is fully predicted by rank/spectrum while orientation scrambling leaves leakage/return invariant, or if the causal held-out orientation signal fails under larger unseen density/mass/background campaigns.

## What RM-001 does not establish

- no claim that all known QG schools fail;
- no claim that a new QG theory is required;
- no claim that `(P,mu)` is fundamental or unique;
- no claim of GR/Lorentzian recovery;
- no claim of a new observable;
- no authorization for RQIR or KMQGB promotion;
- no `NEW_PHYSICS_CANDIDATE` label.

## Next decisive test

Use the corrected Lorentzian EPRL cross-shell gamma campaign as a stronger gravity-side test. If a pinned Lorentzian EPRL realization shows the same orientation-sensitive closure pattern robustly across Immirzi parameter values and shell changes, RM-001 gains a direct gravity-side realization. If not, keep RM-001 scoped to the two accepted chains and investigate why the EPRL map differs.
