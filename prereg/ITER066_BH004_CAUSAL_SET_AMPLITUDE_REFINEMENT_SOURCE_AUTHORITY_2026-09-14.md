# ITER066 — BH004/RC004 causal-set amplitude/refinement source-authority gate

Date frozen: 2026-09-14

## Purpose
After ITER065 closed the current RC008 crossing route as source-blocked, move to the independent causal-set/BH front without retuning prior selector tests. RC-004 explicitly leaves IF-03 dynamics/amplitude and IF-07 quantum measure open. Before any new causal-set amplitude/refinement computation, test whether the already source-grounded RC-004 authority stack contains an explicit source-faithful quantum amplitude/measure plus a coarse-graining/refinement/composition object.

## Frozen source set
Only the sources already listed in `realizations/RC-004_CAUSAL_SET_BDG_ACTION.md` are admissible in this gate:
- arXiv:1903.11544 — Surya, causal-set QG review;
- arXiv:2007.13192 — Machet & Wang, continuum limit of BDG action;
- arXiv:gr-qc/0212064 — Rideout, causal-set dynamics.

No source may be added after observing results without a new preregistration.

## Frozen extraction predicates
For each exact PDF, preserve passages around these object classes:
- quantum dynamics: `quantum measure`, `decoherence functional`, `sum over histories`, `path integral`, `amplitude`, `partition function`;
- scale/composition: `coarse grain`, `coarse-grain`, `renormal`, `refinement`, `growth`, `sequential`, `composition`, `cylinder`;
- native action: `Benincasa`, `Dowker`, `Glaser`, `action`.

Automated hits only nominate passages. A scientific PASS is forbidden without terminal manual equation-level audit.

## Source classification
- `SOURCE_CANDIDATE_AMPLITUDE_REFINEMENT_PRESENT`: at least one frozen source has an exact extracted local passage containing a quantum-dynamics term together with a scale/composition term. Requires manual equation-level audit.
- `SOURCE_CANDIDATE_QUANTUM_DYNAMICS_ONLY`: quantum-dynamics authority is present but no same-source explicit coarse/refinement/composition passage is found in the local audit windows. Requires manual audit; no amplitude/refinement gate authorized.
- `SCOPED_BLOCKED_NO_SOURCE_FAITHFUL_AMPLITUDE_REFINEMENT_OBJECT`: all PDFs extract successfully and no candidate survives manual audit.
- `INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION`: any frozen PDF cannot be retrieved/extracted. No scientific conclusion.

## Locks
This gate cannot establish BH004/BH004B, a new QG theory, a bridge, or new physics. Classical sequential growth is not to be promoted to the final quantum dynamics. BDG action continuum recovery alone is not an amplitude/refinement derivation.

## Next rule
Only if a source-faithful quantum amplitude/measure and explicit scale/composition object are jointly qualified may a numerical BH004 amplitude/refinement gate be preregistered. Otherwise causal-set amplitude/refinement remains source-blocked and compute moves to another independent PHASE_1 front.