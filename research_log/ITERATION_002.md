# ISQGR Iteration 002 — Causal order × entanglement geometry

Date: 2026-09-12  
Status: `ACTIVE / 70_PERCENT`

## Goal

Stress-test BH-001 on a conceptually different interface and determine whether causal-order and quantum-information geometry mechanisms yield a more specific, falsifiable bridge.

## Completed in this iteration

1. Added `RC-004_CAUSAL_SET_BDG_ACTION.md`.
2. Added `RC-005_HAPPY_HOLOGRAPHIC_QEC.md` as an exact toy-mechanism card with a strict scope firewall.
3. Found that BH-001's single generic composition symbol is semantically too coarse:
   - causal/sequential composition;
   - subsystem/parallel/tensor composition;
   must not be identified without an explicit compatibility structure.
4. Introduced `BH-002 Causal–Entanglement Metric Reconstruction (CEMR)`.
5. Derived the first executable ISQGR obstruction quantity:
   - causal structure supplies a conformal metric class;
   - independent leading-order entanglement/area data supply local scale estimates;
   - patch-to-patch disagreement is a necessary obstruction to one common conformal factor.
6. Proved within the local-patch approximation that the obstruction residual

   `delta_i = log(A_i^obs/A_i[g_bar]) - mean_j log(A_j^obs/A_j[g_bar])`

   is invariant under the arbitrary choice of conformal representative

   `g_bar -> exp(2 chi) g_bar`.
7. Added executable implementation `code/cemr_local_consistency.py`.
8. Added synthetic regression tests `code/test_cemr_local_consistency.py`.

## Scientific advance

Iteration 002 has moved ISQGR beyond a purely taxonomic synthesis.

The repository now contains a cross-school consistency relation that is neither a whole-school score nor a verbal analogy:

`causal conformal class + independent codim-2 area data -> one local conformal scale field`.

If independent patches in the same local causal neighborhood require different conformal scales after declared corrections/uncertainties, then the proposed CEMR mapping is locally inconsistent.

This is a **scoped obstruction**, not evidence that causal-set or holographic programmes are false.

## Why this is not yet new physics

The ingredients are individually known:

- Lorentzian causal order constrains conformal geometry;
- volume/counting can complete causal reconstruction in causal-set reasoning;
- RT-type entanglement/area relations and entanglement-based geometry reconstruction exist in controlled holographic regimes.

Potential novelty can arise only if the joint use of these channels yields a new theorem, uniqueness/stability result, obstruction class, dynamical constraint, or observable consequence not already contained in either input separately.

## Current blockers

1. `DOMAIN_OVERLAP`: identify a regime where the causal-order theorem and entanglement reconstruction apply to the same physical geometry.
2. `REGION_CIRCULARITY`: ensure entanglement-region labels do not already encode the metric scale being reconstructed.
3. `QES_CORRECTIONS`: quantify when generalized-entropy corrections spoil the leading area inversion.
4. `GLOBAL_INVERSION`: move from constant-local-Omega patches to a finite-surface nonlinear inverse problem.
5. `DYNAMICS`: reconstructed metric kinematics do not yet imply Einstein dynamics.
6. `EPRL_REFINEMENT`: the secondary Iter002 task of strengthening the EPRL refinement/coarse-graining source chain remains open.

## Internal readiness metrics

Roadmap completion only; not probabilities of truth.

- Repository/recovery bootstrap: **75%**
- Source-grounded inter-school atlas: **20%**
- Recurrent-motif discovery: **0%**
- Bridge-principle validation: **12%**
- Executable cross-school obstructions: **15%**
- Candidate-theory construction: **0%**
- Overall ISQGR scientific programme readiness: **12%**
- Iteration 002 completion: **70%**

## Next decisive task

Construct a finite-surface synthetic CEMR inversion in a known conformally related Lorentzian geometry and test three questions:

1. identifiability: can `Omega(x)` be recovered from redundant area data?
2. stability: how do perturbations/QES-like nuisance terms propagate into `Omega`?
3. incompatibility: can the obstruction distinguish a wrong conformal class from an allowed conformal rescaling?

In parallel, separate BH-001 into at least two compositions:

- `circ` — sequential/causal composition;
- `otimes` — parallel/subsystem composition;

and search for the compatibility/interchange law rather than forcing them into one operation.

## Candidate lock

No ISQGR field equation, action, microscopic ontology, or candidate theory is authorized yet.

Unlock condition: at least one source-grounded recurrent motif or one mathematically nontrivial bridge theorem must survive an explicit falsification test.