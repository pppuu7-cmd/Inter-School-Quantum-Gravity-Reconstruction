# Iter003 Result — Scale/Composition Leakage Identity

Status: `DERIVED_ISQGR / ABSTRACT_PROXY`  
Date: 2026-09-12

## 1. Motivation

BH-001 initially required a scale/refinement map `R` to preserve physical composition. That requirement is too vague unless the obstruction to preservation is explicit.

Let:

- `E` be an encoding/embedding from a retained coarse physical description into a finer description;
- `D` be a decoding/coarse-graining map;
- `Phi1`, `Phi2` be composable fine dynamics;
- `P = E o D` be the fine-space reconstruction after coarse graining.

Define the induced coarse dynamics

`R(Phi) = D o Phi o E`.

## 2. Exact sequential-coherence identity

Direct substitution gives

`R(Phi2 o Phi1) = D o Phi2 o Phi1 o E`,

while

`R(Phi2) o R(Phi1) = D o Phi2 o E o D o Phi1 o E`

`= D o Phi2 o P o Phi1 o E`.

Therefore

`Delta_seq(Phi2,Phi1)`

`= R(Phi2 o Phi1) - R(Phi2) o R(Phi1)`

`= D o Phi2 o (I-P) o Phi1 o E`.

This identity is exact for any linear compositional setting where the maps are defined.

## 3. Interpretation

The obstruction is not generic "RG error". It is specifically the part of the intermediate fine evolution that leaves the retained/reconstructible sector and later becomes visible again after further dynamics.

Exact sequential functoriality holds if, in the relevant domain, any one of the following sufficient conditions applies:

1. `(I-P) o Phi1 o E = 0` — the retained sector is invariant under the first fine evolution;
2. `D o Phi2 o (I-P) = 0` — discarded information can never return to coarse observables after the second evolution;
3. a weaker cancellation makes the full defect vanish on the physical domain.

Thus a scale map that is approximately compatible with sequential dynamics requires a **closure/no-return condition**, not merely an associative microscopic composition law.

## 4. Why this matters for ISQGR

This gives BH-001 a non-tautological target.

For a quantum-gravity realization, an admissible refinement/coarse-graining scheme should identify which physical information is removed and demonstrate that this removed sector does not feed back into the retained observables in a way that violates the claimed effective composition law.

Potential native manifestations include:

- spinfoam simplicity/constraint data leaking under coarse graining;
- truncation operators generated under functional RG;
- microscopic causal/history information lost by a reduced transfer description;
- gauge/boundary/edge information preventing naive subsystem factorization.

These are research targets, not asserted equivalences.

## 5. Sequential versus parallel composition

Iteration 002 established that at least two composition types must be distinguished:

- sequential/causal composition `circ`;
- parallel/subsystem composition `otimes`.

The identity above addresses only `circ`.

For `otimes`, define the monoidal defect

`Delta_parallel(Phi_A,Phi_B)`

`= R_AB(Phi_A otimes Phi_B) - R_A(Phi_A) otimes R_B(Phi_B)`.

It vanishes automatically only if the relevant encodings/decodings and physical factorization are themselves compatible with the tensor/subsystem decomposition. In gauge theory and gravity this cannot be assumed without auditing constraints, boundaries and edge data.

## 6. Executable proxy

`code/scale_composition_coherence.py` implements a finite-dimensional CPTP proxy:

- a coarse qubit-like sector is isometrically embedded into a larger fine space;
- leakage is decoded into a fixed normalized state;
- random fine unitaries generically leave and re-enter the retained sector;
- block-preserving unitaries preserve it exactly.

The Monte Carlo campaign measures the normalized sequential defect and its correlation with leakage probability.

Expected control behavior:

- generic mixing: nonzero defect;
- invariant retained subspace: defect at floating-point zero.

This is a methodological regression test, not a simulation of spacetime.

## 7. Stronger BH-001A statement

A candidate scale map should be treated as physically coherent only if it forms an exact or controlled **(possibly lax) compositional functor** on the physical quotient. Any nonzero coherence defect must be represented by explicit retained memory/boundary variables or bounded as an effective correction.

Simply dropping the defect is equivalent to assuming Markovian closure of the coarse theory.

## 8. Falsification route

For each concrete QG realization:

1. specify native `E`, `D`, and physical composition;
2. compute or bound `Delta_seq`;
3. identify whether the defect is represented by known boundary/memory operators;
4. test whether enlarging the retained state closes the defect with finite added structure;
5. reject BH-001 as physically useful if every framework needs unrelated arbitrary closure variables.

## 9. Claim lock

This exact identity is elementary operator algebra. ISQGR novelty, if any, would lie only in demonstrating that the **same physically constrained closure structure** appears across independent quantum-gravity realizations and yields a new gravitational consequence.