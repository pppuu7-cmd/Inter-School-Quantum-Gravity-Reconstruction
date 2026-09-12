# BH-004 — Projector–Measure Covariant Scale Transport

Status: `BRIDGE_HYPOTHESIS / ADMITTED FOR FALSIFICATION`  
Date: 2026-09-12  
Primary interface: `IF-04 COMPOSITION/GLUING`  
Secondary interfaces: `IF-08 CONTINUUM/COARSE-GRAINING`, `IF-07 MEASURE/NORMALIZATION`  
Parent motif: `RM-001_RETAINED_SECTOR_ORIENTATION_CLOSURE_DATA`  

## 1. Motivation

RM-001 established across independent realization chains that projected composition cannot in general be characterized by retained rank or operator spectra alone. The exact spectral-insufficiency theorem gives

`Delta = P C2 Q C1 P = (P C2 Q)(Q C1 P)`, `Q = I-P`,

and proves by shared-similarity counterexample that `Delta` changes when the composition operators are rotated relative to a frozen retained projector even though their spectra are unchanged.

Causal-set thinning adds a separate constraint: the source-defined retained subspace can remain strongly aligned under coarse change while the scalar spectral scale follows a different flow. Therefore sector orientation and scalar scale/measure cannot be assumed to be the same effective datum.

BH-004 is the minimal bridge hypothesis that responds to both facts without inventing a candidate QG dynamics.

## 2. Bridge object

At scale/refinement level `s`, represent the closure-relevant effective data by

`E_s = (P_s, mu_s)`

where

- `P_s` is a source-native retained physical projector/subspace;
- `mu_s` denotes the scalar scale/measure/normalization information required by the realization.

The notation is deliberately minimal. `P_s` and `mu_s` are not asserted to be fundamental variables.

A coarse/refinement map must provide

`T_{s->s'} : (P_s, mu_s) -> (P_{s'}, mu_{s'})`

without choosing `P_{s'}` or `mu_{s'}` by optimizing the target closure metric on the held-out scale.

## 3. Covariance requirement

For a physical change of representation by a common unitary/isometry `U`, closure data must transform covariantly:

`C -> U^† C U`,

`P -> U^† P U`.

If the operators transform while `P` is artificially frozen, the mixed blocks `Q C P` change and closure generally changes. This is not an optional convention: it follows from the RM-001 spectral-insufficiency theorem.

The bridge therefore distinguishes:

1. **representation covariance**, where `C` and `P` co-transform and closure is unchanged;
2. **physical scale/refinement transport**, where the relation between the source-native `P_s` and `P_{s'}` is nontrivial and must be predicted.

## 4. Closure observables

For one-step transport from `s` to `s'`, define a native leakage diagnostic

`L_{s->s'} = Q_{s'} C_{s->s'} P_s`.

For sequential transport `s -> s' -> s''`, define

`Delta_{s->s'->s''} = P_{s''} C_{s'->s''} Q_{s'} C_{s->s'} P_s`.

The bridge does not require these matrices to vanish exactly. It requires that the transport law for `(P,mu)` predict their scale dependence better than rank/spectrum-only baselines without per-scale retuning.

## 5. Separation of projector and measure flow

BH-004 explicitly forbids the identification

`projector transport == scalar cutoff running`

unless this is derived in the realization.

The causal-set BH-003 campaigns motivate this restriction: source-sector principal alignment remained high under thinning while the native eigenvalue-flow exponent differed strongly from the source spectral-cutoff exponent.

Thus a successful bridge may have

`P_{s'} ≈ transport(P_s)`

while

`mu_{s'}`

obeys a distinct normalization/density/RG law.

## 6. Cheapest decisive held-out test

Use at least three ordered scale/refinement levels `s0 < s1 < s2` in one source-defined realization.

### Training

Using only `s0` and `s1`:

1. construct `P_s` by a source-native rule independent of the target closure metric;
2. infer a transport law for subspace orientation from `P_s0 -> P_s1`;
3. infer any scalar `mu` flow independently of the held-out closure target;
4. freeze all transport parameters.

### Held-out prediction

At `s2`:

1. predict `P_s2` and `mu_s2` without refitting;
2. predict at least one leakage/return quantity built from `L` or `Delta`;
3. compare against:
   - rank-only baseline;
   - spectrum/cutoff-only baseline;
   - independently randomized orientation baseline;
   - where possible, a standard source-native coarse-graining baseline.

### Minimum success condition

BH-004 receives a positive scale/refinement result only if the frozen projector-aware transport:

- improves held-out closure prediction relative to rank/spectrum-only baselines;
- preserves source-native physical constraints required by the realization;
- does not require per-scale orientation rotation chosen from the closure target;
- does not introduce an unconstrained free function for `mu_s`.

## 7. Kill conditions

Reject or sharply weaken BH-004 if any of the following occurs in a suitable source-defined test:

1. **orientation irrelevance:** held-out closure is fully predicted by rank/spectrum data and projector orientation adds no reproducible information;
2. **nontransportability:** no frozen map from `P_s0,P_s1` predicts `P_s2` better than a rank-matched/random baseline;
3. **freedom-tax failure:** successful prediction requires an arbitrary scale-dependent unitary, free function, or retuning at each scale;
4. **constraint loss:** projector transport improves the diagnostic only by leaving the source physical/gauge/constraint sector;
5. **measure conflation:** apparent success disappears once normalization/density conventions are treated independently of projector orientation;
6. **nearest-framework absorption:** the entire effect is quantitatively reproduced by an existing standard effective-theory/subspace-tracking construction with no additional QG-specific structural consequence.

## 8. Nearest-known-framework audit

BH-004 is intentionally close to known ideas from projected effective dynamics, Feshbach/Schur-complement methods, adiabatic/subspace transport, tensor-network truncation and RG operator mixing.

Therefore **projector-aware transport is not itself claimed as new physics**.

Potential ISQGR novelty can arise only if a source-native QG realization forces a specific, non-arbitrary transport law tying together composition closure, causal/constraint structure and scale/measure flow, and that law survives held-out refinement tests while differing from the nearest standard framework in a falsifiable way.

## 9. Freedom tax

Current free structure:

- choice of source-native projector rule: must come from the realization, not from target closure fitting;
- transport law: currently unspecified and therefore `OPEN_BLOCKED` until derived/tested;
- `mu_s` flow: realization-dependent and may not be chosen to force closure.

Until the transport law is frozen from training scales, BH-004 is not promotable.

## 10. Relation to existing ISQGR hypotheses

- `BH-001` supplies the exact projected-composition defect structure.
- `BH-003` supplies the strongest current same-realization laboratory for separating subspace geometry from scalar spectral-scale flow.
- `RM-001` supplies the recurrent cross-realization requirement that orientation is independent closure data.
- `BH-004` converts those results into a falsifiable scale-transport bridge.

No candidate action, Hamiltonian, field equation or microscopic ontology is introduced here.

## 11. Promotion gate

Promote BH-004 from `BRIDGE_HYPOTHESIS` toward `BRIDGE_DERIVED` only after:

1. one held-out three-scale/refinement test succeeds with frozen transport parameters;
2. the source-native constraint/physical sector is preserved;
3. rank/spectrum-only baselines are beaten;
4. the nearest-known-framework explanation is explicitly tested;
5. the result is reproduced in a second sufficiently independent scale/refinement realization or an exact derivation removes the realization dependence.

Until then:

- candidate theory remains `UNFORMED`;
- `NEW_PHYSICS_CANDIDATE` remains unauthorized;
- RQIR/KMQGB candidate promotion remains unauthorized.
