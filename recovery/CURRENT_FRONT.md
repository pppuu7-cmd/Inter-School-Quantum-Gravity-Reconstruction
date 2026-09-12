# ISQGR CURRENT FRONT

Date: 2026-09-12  
Active iteration: `ITERATION_006`  
Iteration completion: **64%**  
Amplitude/refinement cross-realization validation: **39%**  
Overall scientific programme readiness: **47%**  
Candidate-theory construction: **0% — UNFORMED / constitutionally locked**

## Preserved blockers

RC006 contraction serialization remains terminal `SCIENTIFIC_FAIL_CONTRACTION_SERIALIZATION_UNSTABLE`; minimal Eq.(29) amplitude remains BLOCKED. RC008 remains source-only BLOCKED. RC009 remains `SCOPED BLOCKED`. Lorentzian Delta4 finite-cutoff/profile/scaling remains `SATURATED NEGATIVE/SCOPED` with no bridge credit.

The generic lexical/proximity source-selector route for arXiv:1801.03771 also remains a preserved source-authority FAIL: run `34701317882`, only 2/8 targets stable. It has not been repaired or promoted. The active route instead uses exact source labels `DVD2` and `DVD3` plus pinned equation hashes.

## Genuine two-vertex Lorentzian EPRL — source-labelled DVD2/DVD3 path

Pinned paper root SHA256: `27e781f9ae9b36056a57b7747dc3c58b5b9c944dd0214041149843d8434e16c1`.
Pinned numerical kernel: `qg-cpt-marseille/sl2cfoam-next` commit `052e4346028870bd76f69a3034e6cae8defb8f7f`.

### Closed prerequisites

The genuine `Dl0` two-vertex pilot remains PASS: run `34703528413`. The independent symbolic/source guard remains PASS: run `34703574873`. The non-retuned held-out `Dl0` gamma transport remains PASS 5/5: run `34703682106`.

The 12-lane B4 multi-shell primitive qualification is now terminal PASS. The original run `34706661403` was infrastructure-invalid before science because of a Makefile race. Build ordering alone was repaired; the scientific grid and threshold were unchanged. Authoritative repaired run `34707794670`, aggregate job `103591135360`: all 12 gamma × shell lanes passed the frozen `1e-5` fast-vs-accurate threshold. Worst observed error was `1.05909e-7` at gamma=2.0, Dl=3. Durable result: `results/ITER006_DVD_B4_MULTISHELL_KERNEL_PASS.md`.

### Source-gated finite DVD shell sums — new terminal PASS

The prospectively frozen finite shell-sum calculation is now terminal `DVD_FINITE_MULTISHELL_SUM_AGGREGATE_PASS`:

- authoritative run `34708369655`;
- source-manifest job `103592473582`: PASS before numerical jobs were released;
- gamma jobs: `103592489921` (0.5), `103592489940` (1.2), `103592489928` (2.0): all PASS;
- aggregate job `103592649819`: PASS;
- aggregate artifact `10302776275`, digest `sha256:0ec040025f6cb55953cedbb6f79c28ab142a3563b09a41be039867e422693796`;
- repeat maximum relative difference: exactly `0.0` in all lanes;
- worst Dl0 regression relative error against the previous genuine two-vertex pilot: `1.4083e-16`.

Frozen symmetric boundary: `j_a=j'_a=1`, `i=t=i'=t'=1`; gamma `{0.5,1.2,2.0}`; finite auxiliary cutoffs `D={0,1,2}`.

Observed, but not promoted to a convergence theorem: for **both DVD2 and DVD3 at all three calibration gammas**, the relative D1→D2 shell increment is smaller than the D0→D1 increment. DVD2 and DVD3 also separate immediately for D>0, so the exact Dl0 equality is a special weighted-B4/normalization property rather than equality of auxiliary support.

Durable result: `results/ITER006_DVD_FINITE_MULTISHELL_SUM_PASS.md`.

The finite cutoff is a numerical regulator modeled on the same paper's labelled shell pattern. It is **not** a source-defined refinement map. Three pre-numerical source-gate attempts were correctly blocked before any gamma amplitude ran; their parser corrections are preserved in `protocol/ITER006_DVD_MULTISHELL_SOURCE_GATE_AMENDMENT.json`.

### Auxiliary-support audit

Response-blind combinatorics run `34708207163` preserved its prewritten classification `DVD_SUPPORT_COMBINATORICS_INCONCLUSIVE`, because its specific hypothesis was false. Raw support counts are nevertheless informative: DVD2 vs DVD3 admissible term counts are `3 vs 1` at D0, `21 vs 16` at D1, `66 vs 49` at D2, and `147 vs 100` at D3. Hence the Dl0 numerical equality is not explained by identical support cardinality. Durable note: `results/ITER006_DVD_AUXILIARY_SUPPORT_COMBINATORICS.md`.

## Active compute — two independent fronts

### 1. Inherited held-out gamma transport of the multi-shell pattern

Run `34708554742` is active. Exact held-out gamma set `{0.3,0.8,1.6,2.5,3.0}` was inherited from the earlier Dl0 held-out test, before any D1/D2 held-out response existed. The source-manifest has already passed. The preregistered hypothesis is that for both amplitudes the D1→D2 relative shell increment is smaller than D0→D1. Strong support requires 5/5 lanes; natural support requires at least 4/5. Even strong support licenses only finite-cutoff pattern transport, not convergence.

Protocol: `protocol/ITER006_DVD_MULTISHELL_HELDOUT_GAMMA_PREREG.json`.

### 2. Asymmetric-boundary prerequisite

A source-compatible asymmetric boundary was frozen before numerical response:

`j=(1,2,2,2)`, `j'=(1,2,2,1)`, `i=t=i'=t'=1`.

This choice satisfies the exact DVD2 deltas and shared D0 auxiliary-shell constraints while breaking the fully symmetric boundary. Before computing any asymmetric DVD amplitude, run `34708641965` is validating six representative mixed-spin B4 configurations at gamma `{0.5,1.2,2.0}` against adaptive integration with the unchanged `1e-5` threshold.

Protocol: `protocol/ITER006_DVD_ASYMMETRIC_BOUNDARY_PREREG.json`.

## Exact next gate / claim locks

1. Consume/classify held-out run `34708554742`.
2. Consume/classify mixed-B4 prerequisite `34708641965`.
3. Only if the mixed-B4 prerequisite passes, implement the already frozen asymmetric finite-shell DVD2/DVD3 calculation. No parameter retuning is allowed after seeing the mixed-B4 values.
4. A shell cutoff is not a refinement map. A bridge still requires an explicit coarse/refined amplitude map plus held-out non-retuned transfer.

Iteration completion is **64%**. Amplitude/refinement cross-realization readiness is **39%**. Overall readiness is **47%**. Candidate theory remains **0% / UNFORMED**.

`ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`, candidate equations and RQIR/KMQGB promotion remain forbidden.
