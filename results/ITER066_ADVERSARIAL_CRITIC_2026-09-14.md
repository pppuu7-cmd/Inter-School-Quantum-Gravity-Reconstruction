# ITER066 adversarial critic

Date: 2026-09-14
Target provisional conclusion: `SCOPED_BLOCKED_NO_SOURCE_FAITHFUL_AMPLITUDE_REFINEMENT_OBJECT`

The critic's task is to try to defeat the blocker, not to restate it.

## Attack 1 — Does Rideout's quantum transition amplitude already provide the required composition object?

Rideout Ch. 4.2 introduces a decoherence functional and proposes

`T(C'', C -> C') = D(C'',C') / D(C'',C)`

and discusses products of transition amplitudes along growth paths in the covariance condition.

**Strongest pro-PASS reading:** this is an explicit quantum amplitude attached to sequential growth and therefore may look like a quantum composition rule.

**Why the attack fails:** the section explicitly presents a *sketch* of how a quantal generalisation might be constructed. It still asks whether appropriate quantum analogues of the classical dynamical principles can be found and says the hope is that they would lead to a quantum causal-set dynamics. No source-defined scale/coarse/refinement map acts on the quantum measure/decoherence functional, and no physical coarse/fine comparator is supplied. The ratio defining one growth transition is not, by itself, a scale/refinement transform sufficient for the preregistered amplitude/refinement bridge test.

Verdict: `NOT_SUFFICIENT_FOR_GATE`.

## Attack 2 — Can the CSG cosmological-renormalisation map be applied directly to QSG?

The classical map is exact:

`M: {t_n} -> {t_n+t_{n+1}}`

(and its r-fold binomial form).

**Strongest pro-PASS reading:** QSG is described as a quantisation/generalisation of CSG, so perhaps the same coupling map can be reused.

**Why the attack fails:** Surya explicitly identifies finding a **quantum version of coupling constant renormalisation** as a future direction. Therefore lifting `M` from classical transition probabilities/couplings to `D`, `mu`, or complex amplitudes is not source-derived. Such a lift would be a new bridge assumption introduced by ISQGR after the source audit.

Verdict: `NEW_BRIDGE_ASSUMPTION_REQUIRED`.

## Attack 3 — Does the BDG action continuum limit supply the missing scale map?

Machet & Wang give a discrete action and a controlled continuum-limit result on the studied causal diamonds.

**Strongest pro-PASS reading:** a discrete-to-continuum limit is a scale relation, so this may be enough for a bridge test.

**Why the attack fails:** the result concerns expectation/continuum behaviour of the action. It does not define a map between quantum history measures/amplitudes at two scales and does not show preservation of decoherence-functional normalization, positivity, event observables, or transition amplitudes. `S_BDG -> S_EH + boundary` is not a QSG refinement/composition law.

Verdict: `ACTION_CONTINUUM_MAP_NOT_QUANTUM_REFINEMENT`.

## Attack 4 — Do cylinder-set inclusions count as refinement?

Cylinder events are built from finite stems and their future extensions. This gives a nested event-algebra structure.

**Strongest pro-PASS reading:** restriction/extension of cylinder sets resembles coarse/fine histories.

**Why the attack fails:** event inclusion is kinematical/set-theoretic unless the source defines the induced transport of the physical quantum measure/decoherence functional and its observables under the relevant coarse/refinement operation. The frozen stack does not provide that bridge object. Complex percolation additionally faces the measure-extension problem to the covariant sigma algebra.

Verdict: `KINEMATIC_EVENT_NESTING_NOT_DYNAMICAL_REFINEMENT`.

## Attack 5 — Could the effective path sum with BD action serve as the joint object?

Surya discusses an effective continuum-inspired causal-set partition function in addition to intrinsic QSG.

**Strongest pro-PASS reading:** it combines a quantum weight and a discrete action; one might coarse-grain the underlying causets.

**Why the attack fails:** the frozen source does not define the required coarse/refinement map for this path sum. Introducing one ourselves would fabricate dynamics/measure transport after observing the source gap.

Verdict: `NO_SOURCE_DEFINED_REFINEMENT_MAP`.

## Attack 6 — Is the blocker an overclaim about the whole causal-set literature?

Yes, it would be an overclaim if stated globally.

**Repair:** restrict the conclusion to the three frozen sources and the exact ITER066 bridge question. A later source-expansion gate may discover an explicit quantum coarse/refinement object elsewhere, but it cannot retroactively change this gate.

## Critic conclusion

The strongest apparent counterexamples separate into three different objects:

1. quantum measure/decoherence/transition-amplitude structures;
2. classical CSG renormalisation;
3. BDG action continuum recovery.

The frozen sources do not supply the mandatory mathematical arrow joining (1) to a physical scale/refinement operation. Treating (2) or (3) as that arrow requires an unstated assumption.

**Critic verdict:** provisional blocker survives.

`SCOPED_BLOCKED_NO_SOURCE_FAITHFUL_AMPLITUDE_REFINEMENT_OBJECT`

Claim lock: this is not `CAUSAL_SET_THEORY_FAIL`, not `NO_QUANTUM_DYNAMICS_EXISTS`, and not a universal no-go theorem.