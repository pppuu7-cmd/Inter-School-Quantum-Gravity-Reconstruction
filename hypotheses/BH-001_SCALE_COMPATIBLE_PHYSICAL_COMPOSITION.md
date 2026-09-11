# BH-001 — Scale-Compatible Physical Composition (SCPC)

Status: `BRIDGE_HYPOTHESIS`  
Date: 2026-09-12  
Origin: cross-audit of RC-001 EPRL, RC-002 4D CDT, RC-003 asymptotic-safety EAA.

## 1. Why H0 had to change

The Phase-0 meta-hypothesis H0 suggested that composition/refinement may be more primitive than continuum geometry.

RC-001 and RC-002 naturally expose regulated/discrete composition structures. RC-003 is natively continuum and organized by scale evolution of an effective average action. Therefore **discreteness cannot be part of the proposed common parent principle** without prejudging against a continuum realization.

The surviving common question is whether *physical composition and scale change obey one compatibility structure* independent of representation.

## 2. Minimal mathematical statement

Let each resolution/description level `lambda` carry:

- a physical observable algebra or operational structure `A_lambda`;
- an admissible physical-state space `S_lambda`;
- a composition law `star_lambda` on composable physical data;
- a scale/refinement map `R_{lambda->lambda'}`.

BH-001 requires a controlled domain in which

`R_{lambda->lambda'}(x star_lambda y)`

and

`R_{lambda->lambda'}(x) star_lambda' R_{lambda->lambda'}(y)`

represent the same physical composition, exactly or with a derived and quantitatively controlled defect.

Symbolically,

`R(x star y) = R(x) star' R(y) + E_R(x,y)`

with `E_R` fixed by the theory rather than fitted after comparison. The strongest form is `E_R=0`; weaker forms require a bounded/anomaly-like defect with its own consistency law.

## 3. Physical-state compatibility

Scale flow must not preserve only formal kinematics. For physical states `omega_lambda`, the induced map must preserve the theory's appropriate physical normalization/positivity condition:

`omega_lambda(1)=1, omega_lambda(a* a)>=0`

must descend to the corresponding condition at `lambda'`, or an explicitly defined generalized replacement must do so.

A bridge that maps amplitudes but loses the physical quotient is rejected.

## 4. Causal compatibility

BH-001 does not assume metric locality is fundamental.

It requires an operational causal structure `K_lambda` or causal relation on processes such that scale/refinement maps either:

1. preserve it; or
2. derive its controlled emergence in a stable phase/limit.

Deleting histories/branches by hand to recover causality is not allowed.

## 5. Geometry as representation of a stable sector

The strongest prospective consequence of BH-001 is:

> continuum Lorentzian geometry should correspond to a stable/fixed representation of the scale-compatible composition structure, not to an independently inserted target metric.

This is a hypothesis, not a result.

If a suitable stable sector exists, a metric-like object `g_eff` must be reconstructed from physical relational/operational data and then shown to obey GR or a bounded deformation in a controlled regime.

## 6. School-native representations to test

### RC-001 EPRL

Candidate native objects:
- spinfoam amplitudes;
- boundary-state composition/gluing;
- refinement/coarse-graining maps.

Test: does refinement commute with physical amplitude composition while preserving constraint/gauge information and a viable normalization structure?

### RC-002 CDT

Candidate native objects:
- transfer matrix between spatial geometries;
- multi-step transfer composition;
- blocking / continuum scaling near relevant phase structure.

Test: does coarse graining preserve the composition law in a way expressible independently of the preferred lattice representation?

### RC-003 Asymptotic Safety

Candidate native objects:
- effective average action `Gamma_k`;
- functional RG scale evolution;
- composition/physical-observable structure underlying the effective theory.

Test: can FRG evolution be represented as a map on a physical compositional structure, rather than merely an analogy with coarse graining?

## 7. Novelty firewall

BH-001 is **not yet new physics**. Associative composition, RG semigroups, categorical gluing, transfer matrices and coarse graining are known structures.

Novelty would require deriving a nontrivial common mathematical constraint that:

- applies to at least two independently grounded realizations;
- is not automatically true for generic theories;
- forces or forbids physical structures;
- yields a new recoverable consequence for causal structure, state space, GR recovery or an RQIR observable.

Until then the correct label remains `BRIDGE_HYPOTHESIS`.

## 8. Cheapest falsification tests

BH-001 is rejected or sharply weakened if:

1. EPRL physical gluing/refinement and CDT transfer composition cannot be embedded into any common associative/operational structure without deleting essential gauge/causal data;
2. asymptotic-safety RG flow admits no physical composition interpretation beyond generic Wilsonian language;
3. positivity/normalization fails to survive the same scale map in any two realizations;
4. causal structure requires mutually incompatible primitive data that cannot emerge as different phases/quotients;
5. the only common statement left is the tautology that "theories have scales and can be combined".

## 9. First possible strengthening

If BH-001 survives, test the stronger condition:

`SCPC-1: the physically relevant coarse-graining map is characterized by preservation of composition + physical positivity + causal consistency, and these conditions restrict the admissible fixed/stable sectors enough to select a gravitational continuum class.`

This would be the first point at which ISQGR may begin deriving candidate dynamics rather than cataloguing interfaces.

## 10. Current verdict

`BH-001 = ADMISSIBLE / UNTESTED_CROSS_REALIZATION`

No recurrent motif `RM-001` is accepted yet.