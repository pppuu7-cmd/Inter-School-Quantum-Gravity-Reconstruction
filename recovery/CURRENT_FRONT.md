# ISQGR CURRENT FRONT

Date: 2026-09-12  
Active iteration: `ITERATION_006`  
Iteration completion: **57%**  
Overall scientific programme readiness: **44%**  
Candidate-theory construction: **0% — UNFORMED / constitutionally locked**

## Preserved blockers

RC006 contraction serialization remains terminal `SCIENTIFIC_FAIL_CONTRACTION_SERIALIZATION_UNSTABLE`: run `34700639086`, aggregate job `103571679523`, artifact `10300052796`; minimal Eq.(29) amplitude remains BLOCKED. RC008 remains source-only BLOCKED. RC009 remains `SCOPED BLOCKED`. Lorentzian Delta4 finite-cutoff/profile/scaling remains `SATURATED NEGATIVE/SCOPED` with no bridge credit.

## Genuine multi-vertex Lorentzian EPRL

Pinned source `arXiv:1801.03771` passed source qualification and exact extraction, but the frozen leave-one-anchor selection-robustness gate remains a preserved scientific/source-authority FAIL: run `34701317882`, aggregate `103573499012`, artifact `10299439561`, only 2/8 stable. The label-owner diagnostic run `34702654029` did not repair that generic source-lock.

### Explicit source-labelled DVD2/DVD3 Δl=0 path

The separately preregistered genuine two-vertex Lorentzian EPRL single-shell `Δl=0` pilot remains `SCIENTIFIC_PASS_SCOPED_DVD_DL0_TWO_VERTEX_PILOT`: run `34703528413`, head `cb21a8aaf938c8c893ec9ea58036522bfb382497`, aggregate job `103579476677`, artifact `10301595889`, digest `sha256:ef6ed6fa672b79eb259d8d348fe4aebb4983b8aa71966809d408ce8b63abc1d9`. Independent symbolic/source guard: run `34703574873`, job `103579481295`, artifact `10301042008`, `DVD_DL0_SYMBOLIC_GUARD_PASS`.

The held-out non-retuned gamma transport gate is now terminal scientific PASS:

- run `34703682106`, head `958514e1342b451511c40188b776e19e76d2a1d0`;
- aggregate job `103579890972`;
- aggregate artifact `10301416544`, digest `sha256:590b11ec27f3d41ae5265b0c41091eb77303fd6e4a28db3914a838e59b38a425`;
- classification `DVD_DL0_HELDOUT_GAMMA_PASS`;
- all `5/5` held-out gamma lanes (`0.3,0.8,1.6,2.5,3.0`) passed the frozen gate;
- repeat maximum relative difference was exactly `0.0` in every lane.

Durable result: `results/ITER006_DVD_DL0_HELDOUT_GAMMA_PASS.md` (result commit `447261e1eeaafcdce431cc4146846b6a5b8f4f3f`).

This closes only held-out transport/reproducibility of the same `Δl=0` source-labelled contraction. It does not establish a full spin sum, multi-shell convergence, refinement map, continuum limit, bridge derivation, or novelty.

### Active compute — frozen B4 multi-shell validity

The next source-relevant numerical prerequisite was frozen before execution in `protocol/ITER006_DVD_B4_MULTISHELL_PREREG.json` (prereg commit `513dc6f2f59d0e1af21eb5fa2918ade052af5907`). It tests the pinned Lorentzian EPRL B4 primitive on the uniform shell slice `j_a=1`, `l_a=1+Δl`, with `gamma={0.5,1.2,2.0}` and `Δl={0,1,2,3}`: 12 independent lanes, `fail-fast:false`, maximum safe parallelism 6.

Frozen validity criterion: upstream `b4_test` fast-vs-adaptive comparison must report at least one comparison, all relative errors finite, and maximum relative error `<=1e-5` in every lane. No monotonic shell-decay requirement is imposed or fitted.

Authoritative workflow launch commit: `40cfcff8932a19a2be8086f9bffaa863d26efdab`. Run `34706661403` (`ISQGR Lorentzian EPRL DVD B4 MultiShell`) is the active compute authority.

## Exact next gate / claim locks

Consume/classify run `34706661403` from raw artifacts/logs. A PASS authorizes only a separately preregistered implementation of the **labelled DVD2/DVD3 multi-shell contraction/shell sum**. A lane failure is first a `NUMERICAL/INFRASTRUCTURE` multi-shell-kernel validity failure until its causal source is localized; it is not a physical amplitude FAIL.

Only after a source-faithful multi-shell contraction is validated may convergence/shell-contribution diagnostics be interpreted. None of these steps is a refinement map. A bridge claim still requires an explicit coarse/refined amplitude map plus held-out non-retuned transfer.

Iteration completion is **57%**. Overall readiness remains **44%**. Candidate theory remains **0% / UNFORMED**.

`ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`, candidate equations and RQIR/KMQGB promotion remain forbidden.
