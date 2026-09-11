# Iter003 Result — Parallel Composition / Edge-Mode Obstruction

Status: `DERIVED_ISQGR + SOURCE_GROUNDED_CONTEXT`  
Date: 2026-09-12

## 1. Problem

Iteration 002 separated two operations that BH-001 had initially conflated:

- sequential/causal composition `circ`;
- parallel/subsystem composition `otimes`.

For ordinary factorizing quantum systems one might expect scale reduction to be monoidal:

`R_AB(Phi_A otimes Phi_B) = R_A(Phi_A) otimes R_B(Phi_B)`.

Gravity and gauge theory provide a direct reason not to assume this identity.

## 2. Source-grounded context

Donnelly and Freidel, *Local subsystems in gauge theory and gravity* (2016), arXiv:1601.04744, show that defining gauge-invariant subsystems associated with regions with boundaries requires additional boundary degrees of freedom. In general relativity these include codimension-2 surface location/frame data and associated surface symmetries.

Related gravitational-dressing work emphasizes that gauge-invariant gravitational observables do not generically organize into ordinary local commuting subalgebras.

These results do not prove any ISQGR candidate, but they rule out using naive Hilbert-space factorization as a universal gravity prior.

## 3. Monoidal defect

Let joint and subsystem scale maps be represented by encodings/decodings

`E_AB, D_AB, E_A, D_A, E_B, D_B`.

Define

`R_AB(Phi_AB)=D_AB o Phi_AB o E_AB`.

For independent microscopic evolution `Phi_A otimes Phi_B`, define

`Delta_parallel`

`= R_AB(Phi_A otimes Phi_B)`

`- R_A(Phi_A) otimes R_B(Phi_B)`.

Even before dynamics is considered, strict monoidality requires compatible factorization such as

`E_AB = E_A otimes E_B`

and

`D_AB = D_A otimes D_B`

on the physical domain.

Gauge constraints and boundary/edge data can violate these assumptions.

## 4. ISQGR interpretation

The correct bridge target is therefore not necessarily a strict monoidal functor. A viable gravitational scale map may instead require:

- explicit interface/edge objects `B_AB`;
- a gluing product over shared boundary data;
- a coherence map relating joint and separate reductions;
- constraint matching at the interface.

Schematically,

`R_AB(A glue_B B)`

rather than

`R_A(A) otimes R_B(B)`

may be the physically meaningful operation.

## 5. Candidate strengthening BH-001B

`BH-001B — boundary-aware compositional coherence`:

> A scale/refinement map for gravity should preserve sequential and parallel composition only after the interface data required by gauge/diffeomorphism constraints are retained explicitly. Apparent nonfactorization is not treated as error if it is carried by a finite, derived boundary/coherence object.

This is more restrictive than the generic statement that gravity has edge modes. ISQGR must show that the *same boundary-aware closure role* appears across independent realizations.

## 6. Cross-school test targets

### Spinfoam/LQG

Audit boundary spin-network/intertwiner data and coarse-graining interfaces: does retaining boundary representation data close gluing under scale change?

### CDT

Audit whether spatial-slice transfer composition contains all interface data needed under coarse graining or whether reduced volume transfer matrices hide memory variables.

### Holographic/QEC

Audit whether encoding-region boundaries and entanglement wedges provide a representation of the same abstract interface role without identifying them by analogy.

### Continuum GR/gauge formulations

Use surface-symmetry/edge-mode constructions as the comparator for what gauge-invariant gluing requires.

## 7. Falsification condition

BH-001B is weakened if every framework requires unrelated, arbitrarily extensible boundary variables with no common coherence law.

It becomes interesting only if independent realizations force a small shared algebraic structure — for example an interface object whose composition, positivity and scale transport obey common identities.

## 8. Current verdict

`BH-001B = ADMISSIBLE / SOURCE-MOTIVATED / NOT_YET_CROSS_REALIZATION`.

No recurrent motif is promoted by this result alone.

## Claim lock

Boundary degrees of freedom in continuum gravity are established context, not evidence that any specific spin-foam, CDT, holographic or ISQGR microscopic realization is correct.