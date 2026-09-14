# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness: **50%**. Bridge credit remains zero.

## Persistent locks

RC006 numerical retry remains unauthorized. RC009 remains scoped blocked on its tested reduced isotemporal route. Lorentzian Delta4 negative results remain preserved. No full Eq.(27), full EPRL/FK refinement, Lorentzian refinement, q-deformed bridge derivation or candidate-theory construction is authorized.

Forbidden claims remain `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`.

## ITER062B terminal scoped PASS

Preregistered commit: `6fa9eb40d45be8facc952716bde83c57e962469d`.
Implementation commit: `8039a7e8a17aa2b62baead26452425971367ae9c`.
Production/workflow head: `3f4b1c89d5183cde99ae6f7cdfa9efe06ae6d829`.
Authoritative run: `34874113741`.
Aggregate job: `104077252124`.
Aggregate artifact: `10359819990`, digest `sha256:fd62c82a618b6ded0e4ab0013610f00a33a70551e9d3f76ab1188d1c2f44493b`.
Durable result commit: `19dbebcdcd32a3c2d1292a343d4e74a08a4ca362`.

Scientific verdict: **`SCIENTIFIC_PASS_RC008_RESTRICTED_COARSE_FINE_NUMERICAL_RECONSTRUCTION_SCOPED`**.

Calibration passed all frozen analytic/null predicates. With no boundary-specific retuning:

- B0 converged and crossed on `[0.50,0.55]` (report-only interpolation `0.534507642057044`);
- B1 converged and crossed on `[0.55,0.60]` (`0.5669524248350563`);
- B2 converged and crossed on `[0.50,0.55]` (`0.5277179126897538`);
- B3 converged but did not cross on the frozen panel; this held-out negative is preserved.

This raises only restricted RC008 numerical-reconstruction readiness. It does not supply bridge credit, full refinement, Lorentzian support or candidate-theory authorization.

## ITER063 active — held-out non-retuned transport / selector

The next gate was prospectively frozen before execution.

Prereg commit: `04dacfba44f2a59efb882dbe162cc5161c7e7795`.
Implementation commits: `a30bd8a3b4b06d61506411a18dd3d48dd2825318`, `8b248e50c19ae8829af98f00c74cf98acf0892df`.
Production head: `a6fa3c4d11b0b34298b3c3ac3e934721db757639`.
Authoritative Actions run: `34874671586`.

Frozen lanes use independent Sobol seeds and inherit the ITER062B amplitude, alpha grid, integration domains, sample powers, convergence thresholds and crossing rule unchanged.

Permutation controls: P1 `(1,3,1,1)`, P2 `(1,1,3,1)`.
New held-out anisotropies: H1 `(2,1,1,2)`, H2 `(2,3,1,1)`, H3 `(2,3,4,1)`, H4 `(1,2,3,2)`.

At launch inspection there were 7 scientifically useful jobs queued and no duplicated scientific batch. The dependent aggregate is allowed only after all lanes terminalize.

## Readiness

Overall scientific programme: **50%**. Candidate theory: **0% / UNFORMED**. Bridge credit: **0**.

## Exact next admissible action

Consume all ITER063 raw artifacts and logs after terminalization, then classify strictly against `prereg/ITER063_RC008_HELDOUT_NONRETUNED_TRANSPORT_SELECTOR_2026-09-14.md`. Green CI is not sufficient. If the gate scientifically passes, preserve any individual held-out negative lanes and only then choose the next independent PHASE_1 gate. If it fails numerically or scientifically, do not retune the frozen panel.
