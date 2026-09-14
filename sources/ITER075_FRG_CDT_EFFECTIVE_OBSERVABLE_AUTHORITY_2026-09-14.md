# ITER075 source authority — FRG/CDT volume-profile and effective-action observable

Date: 2026-09-14
Gate: `ITER075_FRG_CDT_VOLUME_PROFILE_EFFECTIVE_ACTION_OBSERVABLE_AUTHORITY`
Frozen preregistration commit: `543f43be4a8ffa31578d3e9b0f01fca34751e491`
Workflow launch: `b9dfa82125e6cd19e685b08db1fb85c3e874283b`
Workflow/prereg binding: `b63bc64935d2c9968ef953192af61bf59d6c8953`
Authoritative extraction run: `34895738205`
Terminal result commit already present when this late audit was reconciled: `8753736b1d015fc7d4e98952e2b9aad4e0860de7`

## Frozen source stack

CDT:

1. arXiv:0807.4481 — J. Ambjorn, A. Goerlich, J. Jurkiewicz, R. Loll, *The Nonperturbative Quantum de Sitter Universe*.
2. arXiv:1403.5940 — J. Ambjorn, J. Gizbert-Studnicki, A. Görlich, J. Jurkiewicz, *The effective action in 4-dim CDT. The transfer matrix approach*.

FRG/QEG:

3. arXiv:1412.0468 — D. Becker, M. Reuter, *Towards a C-function in 4D quantum gravity*.
4. arXiv:2203.08003 — R. Ferrero, M. Reuter, *The Spectral Geometry of de Sitter Space in Asymptotic Safety*.

The successful CI run preserved all four source candidates. Per preregistration, it is not scientific PASS evidence by itself.

## Executive result

The frozen stack source-qualifies a genuine recurrent **de-Sitter / Einstein-Hilbert / minisuperspace functional motif** across the two programmes, but does not source-qualify a non-forgetful typed correspondence between the CDT reduced volume-history object and the FRG EAA/effective-background object.

The already-terminal scientific classification is therefore retained as authoritative:

**`FAIL_SCOPED_PHYSICAL_EFFECTIVE_ACTION_EQUIVALENCE_REJECTED`**

with retained positive sub-result:

**`COMMON_DE_SITTER_MINISUPERSPACE_FUNCTIONAL_STRUCTURE_ONLY`**.

The positive residual is the same scientific content that the late audit initially labelled `PASS_SCOPED_COMMON_FUNCTIONAL_FORM_ONLY`; this file is reconciled to the earlier terminal classification to avoid competing verdict labels.

## A — CDT observable/action definition

**PASS.**

The CDT sources explicitly define the reduced state/history variable as the discrete spatial three-volume at preferred discrete proper-time slices.

The 2008 source establishes that the ensemble-averaged volume profile of the emergent macroscopic universe is compatible with Euclidean de Sitter geometry and, crucially, reconstructs an effective action governing the measured quantum fluctuations from Monte Carlo data rather than merely fitting a mean `cos^3` curve.

The 2014 transfer-matrix source makes the reduction even more explicit:

- the effective transfer matrix is parametrized by total spatial three-volume `n_t` at a given discrete time;
- the mean profile `<n_t>` and covariance of fluctuations are measured;
- the inverse covariance / measured transfer matrix determines a pseudo-local reduced effective action;
- in the de-Sitter phase the resulting reduced model reproduces the full CDT volume profile and covariance to high accuracy.

Mandatory qualifier: the effective states `|n_t>` erase the detailed spatial triangulation data. This is a reduced volume-state object, not the full CDT triangulation-state transfer matrix qualified by ITER067.

## B — FRG effective object definition

**PASS.**

The 2014/2015 QEG source works explicitly in the Euclidean Effective Average Action framework, including background/quantum metric structure, RG trajectories, running gravitational couplings and split-symmetry considerations. Its proposed `C`-function is evaluated on self-consistent/gravitational-instanton backgrounds; positive-cosmological-constant crossover trajectories include de Sitter backgrounds.

The 2022 source makes the scale-dependent mean-field geometry especially explicit. It constructs a family of self-consistent de Sitter effective geometries along an FRG trajectory. The background/effective metric and its spectral data depend on the RG scale `k`; the scale is a coarse-graining/effective-description parameter, not cosmological proper time.

Thus the FRG side contains a source-defined EAA/effective-background object with running scale and couplings.

## C — domain/codomain compatibility

**NOT ESTABLISHED.**

The frozen stack does not define a source map

`{CDT reduced volume histories / |n_t>}`

`<->`

`{FRG EAA fields / self-consistent mean metrics at scale k}`.

CDT's reduced transfer object acts on a volume-labelled effective state space indexed by discrete proper time. The FRG object is a scale-indexed effective action/mean-field geometry defined through a regulated functional integral and tadpole/self-consistency condition.

A common minisuperspace/de-Sitter language can be imposed mathematically, but no frozen source derives the required typed identification between these domains.

## D — time/scale semantics

**NOT ESTABLISHED; NEGATIVE CONTROL ACTIVE.**

CDT's `t` is discrete proper-time slicing entering the volume history and transfer composition. FRG's `k` is an RG/coarse-graining scale. The 2022 source treats cosmological/effective-geometry time and RG scale as separate variables: for each `k` one has a scale-dependent effective de Sitter geometry whose proper/cosmological time dependence is then evaluated within that geometry.

No frozen source derives `t_CDT <-> 1/k`, `t_CDT <-> log k`, or any equivalent substitution.

`RG_TIME_PROPER_TIME_SWAP_CONTROL` therefore rejects a strong map.

## E — measure/normalization preservation

**NOT ESTABLISHED.**

The CDT reduced effective transfer matrix is induced from a lattice state-sum/Monte-Carlo measure and then projected onto the total three-volume variable. The FRG EAA is generated from a regulator-dependent functional integral with background/quantum metric and cutoff structure.

The frozen sources define these structures separately but do not derive a mapping that preserves or translates:

- CDT transfer/state-sum normalization and projection;
- FRG regulator/background dependence and EAA normalization.

Erasing both structures would leave only a generic reduced action form and is forbidden by the preregistration.

## F — dynamical/effective-action equivalence

**COMMON FUNCTIONAL FORM ONLY; STRONG EQUIVALENCE REJECTED IN THE FROZEN SCOPE.**

Both source stacks connect positive-cosmological-constant gravity with de Sitter/four-sphere effective geometry and Einstein-Hilbert/minisuperspace-type dynamics.

On the CDT side, the measured three-volume profile and covariance support a reduced kinetic-plus-potential effective action whose semiclassical trajectory is de-Sitter-like. On the FRG side, EAA trajectories with positive cosmological constant admit scale-dependent self-consistent de Sitter backgrounds.

What the frozen stack does **not** supply is a single source-defined term-by-term crosswalk of:

- reduced variables;
- time coordinate normalization;
- fixed-volume/boundary conditions;
- kinetic-term sign/conformal prescription;
- coefficients and Newton/cosmological couplings;
- operational interpretation of the action;
- regulator/projection structure.

Therefore the commonality is retained as a reduced functional motif, not a source-qualified physical effective-action equivalence.

## G — observable correspondence

**NOT ESTABLISHED UNDER A SINGLE MAP.**

CDT's operational observables are the measured spatial-volume profile, covariance/fluctuations and reduced transfer-matrix elements. The FRG sources use self-consistent mean fields/effective geometries, spectral data and an EAA-derived `C`-function/trajectory object.

The frozen stack does not define these as counterparts under one explicit correspondence. Similar de Sitter geometry does not close this predicate.

## H — regulator/reduction robustness

**PASSES AS A NEGATIVE SCOPE LOCK; STRONG MAP FAILS.**

Both non-erasable structures are explicit:

- CDT: finite lattice regulator and volume-state reduction/projection;
- FRG: cutoff/regulator and background/dynamical metric structure.

Keeping these structures visible prevents the common functional motif from being promoted to full physical equivalence.

## Mandatory controls

- `DE_SITTER_SHAPE_IDENTITY_CONTROL`: **triggered**. A common de Sitter/`cos^3` profile is insufficient.
- `MINISUPERSPACE_FORM_CONTROL`: **triggered**. Shared Einstein-Hilbert/minisuperspace form alone is insufficient.
- `RG_TIME_PROPER_TIME_SWAP_CONTROL`: **triggered**. `k` remains distinct from CDT proper time.
- `EAA_MONTE_CARLO_ACTION_SWAP_CONTROL`: **triggered**. A regulator-dependent EAA and a covariance/transfer-reconstructed lattice effective action are not identical by nomenclature.
- `REGULATOR_ERASURE_CONTROL`: **triggered**. FRG regulator/background and CDT lattice/state-sum structures remain explicit.
- `FULL_REDUCED_STATE_SWAP_CONTROL`: **triggered**. `|n_t>` is not the full triangulation-state object.
- `COEFFICIENT_RETUNING_CONTROL`: **passes**. No post-hoc coefficient fitting is used to manufacture a frozen-stack map.
- `OBSERVABLE_ERASURE_CONTROL`: **passes**. Operational observables on each side remain typed and distinct.

## Source-authority classification

**`FAIL_SCOPED_PHYSICAL_EFFECTIVE_ACTION_EQUIVALENCE_REJECTED`**

Retained positive sub-result:

**`COMMON_DE_SITTER_MINISUPERSPACE_FUNCTIONAL_STRUCTURE_ONLY`**.

Established in scope:

- explicit CDT reduced spatial-volume observable and reconstructed effective action;
- explicit FRG EAA/effective de Sitter background family;
- nontrivial recurrence of positive-cosmological-constant / de-Sitter / Einstein-Hilbert-minisuperspace structure.

Not established:

- a source-defined domain/codomain map;
- proper-time/RG-scale equivalence;
- measure/regulator-preserving correspondence;
- coefficient/variable/boundary-condition crosswalk;
- observable equality under one typed map;
- equality of full CDT and full FRG dynamics.

## Post-prereg literature lock

A later direct comparison paper, arXiv:2408.07808, was identified **after** the ITER075 source stack had already been frozen. It contains materially stronger direct CDT/FRG reduced-action comparison machinery and therefore cannot be used to upgrade ITER075 retroactively.

It is reserved for a separately preregistered successor gate.

## Claim ceiling

ITER075 rejects physical effective-action equivalence in the frozen scope while retaining a common reduced functional motif. It creates no bridge credit, no microscopic equivalence, no universal parent and no candidate theory.