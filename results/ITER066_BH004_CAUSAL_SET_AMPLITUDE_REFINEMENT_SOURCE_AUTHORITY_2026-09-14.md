# ITER066 terminal result — BH004 causal-set amplitude/refinement source authority

Date: 2026-09-14
Gate: `ITER066_BH004_CAUSAL_SET_AMPLITUDE_REFINEMENT_SOURCE_AUTHORITY`

## Terminal scientific classification

**`SCOPED_BLOCKED_NO_SOURCE_FAITHFUL_AMPLITUDE_REFINEMENT_OBJECT`**

Equivalent reason class: `BLOCKED_SOURCE_AUTHORITY` / `BLOCKED_MISSING_REQUIRED_OBJECT` in the frozen ITER066 scope.

## Run validity

### Run 1

GitHub Actions run `34878725306`, head `915255cfae8d13a10b37f95742fe61cfd9f6e6ad`, ended workflow `failure`.

Scientific extraction was not the failing layer for Rideout: the `gr-qc/0212064` job completed `Frozen exact-PDF source audit` and failed only during artifact upload. Because its JSON was not preserved, the aggregate had an incomplete frozen set. Run 1 is therefore classified separately as:

`ARTIFACT_PRESERVATION_FAILURE_AFTER_SOURCE_AUDIT`

and receives no scientific terminal verdict.

Durable record: `results/ITER066_RUN1_ARTIFACT_PRESERVATION_FAILURE_2026-09-14.md`.

### Provenance-preserving repair

Only the transport artifact label was changed:

- extractor input remained `gr-qc/0212064`;
- safe artifact label became `gr-qc-0212064`;
- frozen source set unchanged;
- `code/iter066/source_gate.py` unchanged;
- extraction terms/selectors unchanged;
- aggregate classifier unchanged;
- scientific question and claim ceiling unchanged.

Repair commit: `1caebf07c29bc90eedec67180f28683e031e5a14`.

### Run 2

GitHub Actions run `34884258757`, head `1caebf07c29bc90eedec67180f28683e031e5a14`, completed `success`.

All four jobs completed successfully:

- source `1903.11544`: job `104110845769`;
- source `2007.13192`: job `104110846021`;
- source `gr-qc/0212064`: job `104110846063`;
- aggregate: job `104110964059`.

All four immutable artifacts are present:

- `iter066-1903.11544`, id `10364096901`, digest `sha256:4511be323df93e6a4b1f501b383297749a13291db7b477ed2dacf5a0cddbb70e`;
- `iter066-2007.13192`, id `10363594110`, digest `sha256:ca12b21a09ace5b6c029f9fafeae5bd2ee9fa05dbf1c6c76baa3e2c80867e213`;
- `iter066-gr-qc-0212064`, id `10363534922`, digest `sha256:563acd87d322ae7d99873c66ec248ee4a30b0817557ab0f1021131f6db8a24ba`;
- `iter066-aggregate`, id `10363514903`, digest `sha256:256c7ecc69b926716c36b0f9e4091fdcbe099b3f4c8c983740dd5b526b9296b6`.

Run 2 closes the run-1 preservation defect. `CI_SUCCESS` is recorded only as implementation/provenance validity, not scientific PASS.

## Manual equation-level audit

Durable source record: `sources/ITER066_BH004_EQUATION_LEVEL_AUTHORITY_AUDIT_2026-09-14.md`.

### Mandatory object 1 — explicit quantum dynamics / amplitude / measure

**QUALIFIED_SCOPED.**

The frozen sources provide explicit quantum-measure/decoherence-functional structure. Surya 2019 gives the QSG grade-2 quantum sum rule (Eq. 82), `mu(alpha)=D(alpha,alpha)` (Eq. 83), normalization/positivity properties, and a complex-percolation product decoherence functional from transition amplitudes. Rideout Ch. 4.2 gives a quantal-growth sketch in terms of `D`, `mu`, and an explicit proposed transition-amplitude ratio.

This is enough to reject the statement `NO_QUANTUM_OBJECT_IN_FROZEN_STACK`, but it is not enough to establish a complete physical causal-set quantum dynamics in unrestricted scope.

### Mandatory object 2 — explicit scale/composition/refinement object sufficient for the bridge test

**NOT QUALIFIED.**

What is source-defined:

- a classical CSG cosmological-renormalisation map, including `t_n -> t_n+t_{n+1}` and the r-fold binomial map;
- sequential/cylinder-set growth structures;
- the BDG action and a scoped discrete-to-continuum action result.

What is not source-defined:

- a quantum coarse/refinement/scale map transporting the QSG decoherence functional, quantum measure, or amplitudes while specifying the physical domain/codomain and preserving the required normalization/observable structure.

Surya 2019 explicitly describes finding a **quantum version of coupling-constant renormalisation** as a future direction. Rideout's quantum construction is explicitly a sketch and does not derive a quantum version of the classical cosmological-renormalisation transform.

## Why apparent candidates do not pass

1. **Classical CSG growth/renormalisation** cannot be silently promoted to QSG quantum dynamics.
2. **Rideout transition amplitudes** define a proposed quantal growth step, not a source-qualified physical coarse/refinement map; the construction is explicitly incomplete/sketched.
3. **Cylinder-set nesting** is an event-algebra structure, not by itself a dynamics-preserving refinement law.
4. **BDG action continuum recovery** constrains an action in a continuum limit but does not transport `D`, `mu`, or quantum amplitudes between scales.
5. **Effective BDG path sum** has no frozen-source coarse/refinement map sufficient for this gate.

The adversarial review in `results/ITER066_ADVERSARIAL_CRITIC_2026-09-14.md` attempted each of these promotions and failed to derive the required arrow without an additional assumption.

## Exact missing object

A source-faithful causal-set quantum map of the form, schematically,

`R_Q : Q_fine -> Q_coarse`

where `Q` contains the physical quantum history structure (`D`, `mu`, or amplitudes), with explicit:

- domain and codomain;
- coarse/refinement or scale relation;
- normalization/positivity handling;
- covariance/gauge-equivalence handling;
- event/observable transport;
- dynamical interpretation.

The frozen stack does not define this object.

## New structural fact

The previous causal-set ambiguity can now be factored into three non-equivalent layers:

1. **quantum history measure/amplitude layer** — present, scoped;
2. **classical sequential-growth scale flow** — present, explicit;
3. **quantum scale/refinement transport joining 1 and 2** — missing in the frozen authority stack.

This factorisation is more informative than a generic statement that 'causal-set refinement is missing'.

## Downstream decision

- BH004 numerical amplitude/refinement gate: **NOT AUTHORIZED** from ITER066.
- Reusing the classical CSG map on QSG objects: **forbidden unless preregistered as `NEW_BRIDGE_ASSUMPTION` in a separate branch**.
- Same-route repeated search within the same frozen sources: **not authorized**.
- An orthogonal Phase-1 front with explicit physical objects should receive priority.

## Claim ceiling

This terminal result does not establish:

- failure of causal-set quantum gravity;
- absence of a quantum coarse/refinement object in all causal-set literature;
- failure of Corridor B;
- a universal no-go theorem;
- any inter-school bridge;
- new physics;
- a new QG theory.

`CANDIDATE_THEORY = UNFORMED`

`THEORY_ESTABLISHED = 0%`

`BRIDGE_CREDIT = 0`
