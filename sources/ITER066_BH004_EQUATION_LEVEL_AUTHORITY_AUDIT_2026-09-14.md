# ITER066 — BH004 equation-level source-authority audit

Date: 2026-09-14
Gate: `ITER066_BH004_CAUSAL_SET_AMPLITUDE_REFINEMENT_SOURCE_AUTHORITY`
Scope: frozen source stack only; no literature expansion may change this gate's verdict.

## Frozen sources

1. Sumati Surya, **The causal set approach to quantum gravity**, arXiv:1903.11544; Living Reviews in Relativity 22, 5 (2019), DOI 10.1007/s41114-019-0023-1.
2. Ludovico Machet, Jinzhao Wang, **On the continuum limit of Benincasa-Dowker-Glaser causal set action**, arXiv:2007.13192v2 (28 Jul 2020).
3. David P. Rideout, **Dynamics of Causal Sets**, arXiv:gr-qc/0212064v1 (14 Dec 2002), dissertation.

No source outside these three is used to promote the frozen ITER066 scientific result.

## A. Quantum dynamics / amplitude / measure object — ESTABLISHED, scoped

### Surya 2019

Section 6.3 defines the QSG quantum measure on the covariant growth sample space. For mutually disjoint events, Eq. (82) is the grade-2 quantum sum rule. Eq. (83) defines

`mu(alpha) = D(alpha, alpha)`

with decoherence functional `D`, together with Hermiticity, countable biadditivity, normalization `D(Omega,Omega)=1`, and strong positivity. QSG replaces CSG transition probabilities by the decoherence functional / quantum measure.

The same source gives complex percolation as a product decoherence functional

`D_tilde(alpha,beta) = A*(alpha) A(beta)`

on the cylinder-event algebra, where transition amplitudes are complex. It simultaneously records that the pre-measure need not extend to the full covariant sigma algebra; this is a scope limitation, not absence of a quantum object.

The continuum-inspired alternative is separately stated as an effective sum over causets with an action; it is not identified with a QSG refinement law.

### Rideout 2002

Chapter 4.2 explicitly sketches the quantal generalisation of classical sequential growth in terms of a quantum measure / decoherence functional. It states the properties

- positivity;
- additivity in each argument, Eq. (4.1);
- Hermiticity, Eq. (4.2);
- `mu(S)=D(S,S)`;
- the grade-2 quantum sum rule.

For finite cylinder events it proposes a transition-amplitude representation, including

`T(C'', C -> C') = D(C'', C') / D(C'', C)`.

However, Rideout repeatedly labels this part a **sketch**, says suitable quantum analogues of the classical principles still have to be found, and frames the resulting law as a hope/conjectural construction. Therefore it supports a quantum-measure candidate/object, but not a completed quantum scale/refinement law.

**Authority decision:** `QUANTUM_MEASURE_OR_AMPLITUDE_OBJECT_QUALIFIED_SCOPED = true`.

## B. Classical scale / renormalisation object — ESTABLISHED, but classical

Surya 2019 gives the post-induced effective CSG couplings explicitly as Eq. (81):

`tilde(t)_n^(r) = sum_{k=0}^r binom(r,k) t_{n+k}`.

Equivalently this is `r` iterations of the map

`M: T^(i) -> T^(i+1)`,  `t_n^(i+1) = t_n^(i) + t_{n+1}^(i)`.

The fixed points are the transitive-percolation family. Rideout 2002 likewise treats cosmological renormalisation as a process acting on the coupling constants of the **classical** stochastic sequential-growth dynamics.

**Authority decision:** `CLASSICAL_CSG_SCALE_MAP_QUALIFIED = true`.

This object is not silently promoted to the quantum measure/decoherence-functional level.

## C. BDG action and continuum object — ESTABLISHED, but not a refinement map

Machet & Wang arXiv:2007.13192v2 write a causal-set sum-over-histories motivation in Eq. (1.1), with causal-set action `S(C)`. In four dimensions Eq. (1.4) gives the finite-causet BDG action in terms of interval counts. Their result establishes that, in the continuum limit on the studied causally convex small causal diamonds, the action tends to the Einstein-Hilbert bulk contribution plus the codimension-two joint contribution.

This supplies an action / continuum-limit object. The paper does **not** define a map transporting a quantum measure, decoherence functional, or transition amplitudes between causal-set scales/refinements.

**Authority decision:** `BDG_ACTION_CONTINUUM_OBJECT_QUALIFIED = true`; `QUANTUM_REFINEMENT_MAP_FROM_BDG = false`.

## D. Mandatory quantum scale/composition/refinement object — MISSING

The frozen gate requires a source-defined object combining the quantum dynamics/measure side with an explicit scale/composition/refinement law sufficient for a later bridge test.

The three sources do not supply a map of the required type, schematically

`R_Q : (Omega, event algebra, D/mu/A)_fine -> (Omega, event algebra, D/mu/A)_coarse`

with source-defined domain, codomain, normalization/positivity compatibility, observable handling, and a stated dynamical interpretation.

Surya 2019 is especially diagnostic: after discussing QSG and the extension problem, it identifies finding **a quantum version of coupling-constant renormalisation** as an important future direction. Thus the classical Eq. (81) transform cannot be applied to the quantum decoherence functional as a derived source fact.

Rideout's quantum chapter also does not close this gap: it sketches a quantal growth dynamics and transition amplitudes but does not derive a cosmological-renormalisation/refinement transform on `D`, `mu`, or the amplitudes.

## E. Provenance-separated object table

| component | source school | source object | source scope | status |
|---|---|---|---|---|
| kinematics | causal set | locally finite causal order / growth histories | causal-set theory | ESTABLISHED |
| dynamics | causal set | QSG quantum measure / decoherence functional; effective action path-sum alternative | scoped / partially constructive | ESTABLISHED_SCOPED |
| measure | causal set | `mu=D(diagonal)`, positivity/normalization properties | QSG histories | ESTABLISHED_SCOPED |
| composition/growth | causal set | sequential birth / cylinder-event structure | regulated history construction | ESTABLISHED, not scale refinement |
| refinement / scale | causal set | post-induced `t_n -> t_n+t_{n+1}` map | classical CSG only | ESTABLISHED_CLASSICAL_ONLY |
| action / continuum | causal set | BDG action -> EH bulk + joint term in studied limit | small causally convex diamonds | ESTABLISHED_SCOPED |
| quantum scale/refinement | causal set | map transporting `D`, `mu`, or amplitudes across scale | required by ITER066 | **MISSING** |
| gauge/quotient | causal set | label covariance is discussed | does not close quantum scale map | PARTIAL |
| observables | causal set | measurable/covariant event issue; extension limitations | QSG | PARTIAL / LIMITATION |

## Source-authority conclusion

`SCOPED_BLOCKED_NO_SOURCE_FAITHFUL_AMPLITUDE_REFINEMENT_OBJECT`

The frozen causal-set stack contains a quantum-dynamics/measure object and contains classical scale/renormalisation plus action/continuum objects, but it does not contain the mandatory **quantum** scale/composition/refinement object connecting them.

Any use of the classical CSG transform `M` on QSG `D`, `mu`, or amplitudes would be a `NEW_BRIDGE_ASSUMPTION`, not a source-faithful derivation.

## Claim ceiling

This result does **not** imply that causal-set quantum gravity fails, that no such quantum map exists elsewhere in the literature, or that causal sets cannot participate in a future bridge. It says only that the frozen ITER066 authority stack does not define the object required for the proposed BH004 amplitude/refinement bridge test.