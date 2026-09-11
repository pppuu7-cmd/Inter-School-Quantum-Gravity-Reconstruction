# ISQGR Current Research Front

Updated: 2026-09-12  
Active iteration: `ITERATION_002` (**70%**)  
Project phase: `PHASE_0 / INTERFACE_ATLAS_BOOTSTRAP`

## Canonical status

- Overall scientific programme readiness: **12%**
- Source-grounded interface atlas: **20%**
- Bridge-principle validation: **12%**
- Executable cross-school obstructions: **15%**
- Candidate-theory construction: **0%**
- Candidate theory: `UNFORMED`
- Accepted recurrent motifs: **0**
- Active hypotheses:
  - `BH-001 Scale-Compatible Physical Composition (SCPC)`;
  - `BH-002 Causal–Entanglement Metric Reconstruction (CEMR)` — current lead.
- New physics: **NOT ESTABLISHED**
- RQIR/KMQGB promotion: **NOT AUTHORIZED**

Readiness values are roadmap-completion metrics, not probabilities of physical correctness.

## Result 1 — universal microscopic discreteness rejected as a synthesis prior

Cross-audit of:

- RC-001 Lorentzian EPRL,
- RC-002 4D CDT transfer matrix,
- RC-003 asymptotic-safety EAA/FRG,

shows that an inter-school parent principle intended to cover these realizations cannot assume microscopic discreteness as a universal primitive.

The surviving BH-001 layer is representation-independent compatibility between physical composition and scale/refinement evolution.

## Result 2 — composition must be multi-typed

RC-004 causal sets and RC-005 HaPPY/QEC show that a single undifferentiated composition `star` is too coarse.

At minimum distinguish:

- sequential/causal composition `circ`;
- parallel/subsystem composition `otimes`.

Future BH-001 work must search for a compatibility/interchange law between these operations instead of identifying them.

## Result 3 — BH-002 Causal–Entanglement Metric Reconstruction

In a controlled semiclassical overlap domain, causal information may determine a Lorentzian conformal class

`g = Omega^2 g_bar`,

while independent entanglement-derived area/metric information may constrain the missing scale `Omega`.

The leading RT-type inverse problem is schematically

`Area_{Omega^2 g_bar}(gamma_A[Omega]) = 4 G_N S(A)`.

BH-002 is a bridge hypothesis, not a model of quantum gravity.

## First executable ISQGR obstruction

For sufficiently local codimension-2 patches in `D` dimensions,

`A_i[g] ~= Omega^(D-2) A_i[g_bar]`.

Define

`r_i = log(A_i^obs/A_i[g_bar])`.

One local conformal factor requires all `r_i` to agree. The residual

`delta_i = r_i - mean(r)`

is invariant under changing the arbitrary conformal representative

`g_bar -> exp(2 chi) g_bar`

within the local-patch approximation.

This yields the first executable cross-school obstruction in:

- `results/ITER002_CEMR_LOCAL_CONFORMAL_CONSISTENCY.md`;
- `code/cemr_local_consistency.py`;
- `code/test_cemr_local_consistency.py`.

A failure rejects only the supplied CEMR mapping/domain, never an entire school.

## Why RM-001 is still locked

There is a promising cross-school bridge, but the recurrent-motif threshold requires more than a missing object or a toy-model analogy. No recurrent motif is accepted until independent source-grounded realization chains establish the same nontrivial interface structure.

## Active blockers

1. `DOMAIN_OVERLAP` — causal-order and entanglement reconstruction must apply to the same physical regime.
2. `REGION_CIRCULARITY` — region/surface labels must not already encode the scale being reconstructed.
3. `QES_CORRECTIONS` — generalized entropy can contaminate a pure area inversion.
4. `GLOBAL_INVERSION` — local constant-`Omega` patches must be upgraded to finite-surface inversion.
5. `DYNAMICS` — metric reconstruction remains kinematic until gravitational dynamics are derived.
6. `EPRL_REFINEMENT` — strengthen the source-defined refinement/coarse-graining chain.

## Next decisive computation

Construct a synthetic finite-surface CEMR inverse problem in a known conformally related Lorentzian geometry.

Required outputs:

1. identifiability of `Omega(x)` from redundant area data;
2. conditioning/stability under controlled nuisance terms;
3. an obstruction that distinguishes a wrong conformal class from an allowed conformal rescaling;
4. explicit failure when the input area data are anisotropically incompatible with any scalar conformal field.

In parallel, reformulate BH-001 using `circ` and `otimes` and test whether a nontrivial interchange/coherence law survives across causal-set, tensor-network, CDT/spinfoam and continuum-RG realizations.

## Candidate unlock condition

No ISQGR action, microscopic ontology or field equation is authorized yet.

Unlock candidate construction only after either:

- one source-grounded recurrent motif survives a falsification audit; or
- one mathematically nontrivial bridge theorem survives a cross-realization test and constrains gravitational structure beyond generic composition/RG language.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `docs/CONSTITUTION.md`
4. `protocol/INTERFACE_FAILURE_TAXONOMY.md`
5. `docs/INTERFACE_ATLAS_V0_1.md`
6. `hypotheses/BH-002_CAUSAL_ENTANGLEMENT_METRIC_RECONSTRUCTION.md`
7. `results/ITER002_CEMR_LOCAL_CONFORMAL_CONSISTENCY.md`
8. `hypotheses/BH-001_SCALE_COMPATIBLE_PHYSICAL_COMPOSITION.md`
9. `realizations/RC-004_CAUSAL_SET_BDG_ACTION.md`
10. `realizations/RC-005_HAPPY_HOLOGRAPHIC_QEC.md`
11. `research_log/ITERATION_002.md`
12. `research_log/ITERATION_001.md`
