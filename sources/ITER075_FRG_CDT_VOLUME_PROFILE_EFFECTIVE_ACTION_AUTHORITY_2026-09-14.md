# ITER075 source authority — FRG/CDT volume profile and effective action

Date: 2026-09-14
Preregistration commit: `543f43be4a8ffa31578d3e9b0f01fca34751e491`
Workflow production head: `b9dfa82125e6cd19e685b08db1fb85c3e874283b`
Authoritative run: `34895709898`

## Validated exact-PDF artifacts

- arXiv:0807.4481 — job `104149022134`, artifact `10368636863`, digest `sha256:8c5d77f6ef14ebb1dd4985ba5c6e83ee2651115a1c6f6c972485da88941d1033`, extracted PDF SHA256 `9d23d42f9cf9d7407898d39ec0a2a21ac95eeb68f027a04efb67f013bb54f049`.
- arXiv:1403.5940 — job `104149022259`, artifact `10369295621`, digest `sha256:31c8b81edf7a4bdc02d74f7c519a748207c9c1208258bf5183147515ee31fe29`, extracted PDF SHA256 `0287b00bae583e46e82bdf664045f9d3a19df26a62746b014136d6f4645dca64`.
- arXiv:1412.0468 — job `104149022182`, artifact `10369315618`, digest `sha256:12fe0e379ce7542e0f12a1b57c7a656aba894d4fb0278e4ecf1a35183e69eec8`.
- arXiv:2203.08003 — job `104149021813`, artifact `10368986070`, digest `sha256:ea4f59deb5e9dd0c5e374544a3b47f2c016b0c85ca95e10a474e69143580a6ed`, extracted PDF SHA256 `f9513ed9748229392489420b915b6829e8e736742ffd9695117a2103d4027a8a`.
- aggregate job `104149123835`, artifact `10369105991`, digest `sha256:986836da406e10a20134154689f47c880a78505c3b12d5e8f4874cccbcbe0799`.

All source jobs and aggregate completed successfully. This is extraction success only; scientific classification follows the preregistered predicates below.

## Predicate audit

### A — CDT observable/action definition: PASS

The CDT stack explicitly defines the spatial three-volume at discrete proper time, its ensemble expectation value and fluctuations. arXiv:0807.4481 gives the `cos^3` de-Sitter volume profile, continuum identification, covariance analysis and reconstructed reduced minisuperspace action. arXiv:1403.5940 independently parameterizes the measured reduced transfer matrix by spatial volume and reconstructs a phase-dependent effective action.

### B — FRG effective object definition: PASS

The FRG stack explicitly defines scale-dependent EAA/background-geometry objects. arXiv:1412.0468 evaluates EAA-derived quantities on self-consistent backgrounds and keeps the RG trajectory/background structure explicit. arXiv:2203.08003 studies a scale-dependent effective de-Sitter geometry and its spectral flow, with `k` as RG/coarse-graining scale.

### C — domain/codomain compatibility: FAIL FOR PHYSICAL EQUIVALENCE

No source-defined map in the frozen stack identifies CDT's reduced history/state variable `N_3(t)` / transfer-matrix volume state with the FRG effective field/background configuration at scale `k`. The mathematical objects live in different operational domains.

### D — time/scale semantics: FAIL FOR PHYSICAL EQUIVALENCE

CDT uses a discrete foliation/proper-time variable. FRG uses theory-space/coarse-graining scale `k`. The frozen stack does not derive an identification between them. `t <-> k^{-1}` remains forbidden.

### E — measure/normalization preservation: FAIL FOR PHYSICAL EQUIVALENCE

CDT retains a triangulation state-sum/automorphism-weighted path integral and reduced transfer object. FRG retains regulator/background-field/EAA structure. No source-defined mapping transports one measure/normalization package into the other.

### F — dynamical/effective-action equivalence: COMMON FORM ONLY

Both stacks exhibit Einstein-Hilbert/de-Sitter/minisuperspace-related structures. CDT reconstructs a reduced action from Monte-Carlo volume fluctuations/transfer data; FRG computes a scale-dependent effective average action and self-consistent backgrounds. The frozen sources do not equate coefficients, variables, boundary conditions or operational meaning across the two constructions.

### G — observable correspondence: NOT ESTABLISHED

A common de-Sitter geometry motif is present, but no source-defined observable map sends the CDT measured volume-history distribution to an FRG observable with preserved operational semantics.

### H — regulator/reduction robustness: FAIL FOR EQUIVALENCE / CONTROL PASSES

Keeping the CDT lattice/reduced-state projection and FRG cutoff/background dependence explicit destroys any naive one-object identification. This is the intended failure control, not an infrastructure problem.

## Scientific classification

**`FAIL_SCOPED_PHYSICAL_EFFECTIVE_ACTION_EQUIVALENCE_REJECTED`**

Retained positive sub-result:

**`COMMON_DE_SITTER_MINISUPERSPACE_FUNCTIONAL_STRUCTURE_ONLY`**

The shared de-Sitter/minisuperspace/EH-like functional motifs are real but forgetful. They are insufficient to identify the underlying effective actions or observables.

## Locks

- `RG_TIME_PROPER_TIME_SWAP_CONTROL`: triggered successfully.
- `EAA_MONTE_CARLO_ACTION_SWAP_CONTROL`: triggered successfully.
- `REGULATOR_ERASURE_CONTROL`: triggered successfully.
- `FULL_REDUCED_STATE_SWAP_CONTROL`: triggered successfully.
- `COEFFICIENT_RETUNING_CONTROL`: no retuning performed.
- `BRIDGE_DERIVED = false`.
- candidate theory remains `UNFORMED / 0%`.
