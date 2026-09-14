# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness: **50%**. Bridge credit remains zero.

## Persistent locks

RC006 numerical retry remains unauthorized. RC009 remains scoped blocked on its tested reduced isotemporal route. Lorentzian Delta4 negative results remain preserved. No full EPRL/FK refinement, Lorentzian refinement, q-deformed bridge derivation or candidate-theory construction is authorized.

Forbidden claims remain `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`.

## ITER062B — terminal scoped scientific PASS

Authoritative run `34874113741`; aggregate job `104077252124`; aggregate artifact `10359819990`, digest `sha256:fd62c82a618b6ded0e4ab0013610f00a33a70551e9d3f76ab1188d1c2f44493b`; durable result commit `19dbebcdcd32a3c2d1292a343d4e74a08a4ca362`.

Verdict: `SCIENTIFIC_PASS_RC008_RESTRICTED_COARSE_FINE_NUMERICAL_RECONSTRUCTION_SCOPED`.

B0, B1 and B2 converged with robust non-retuned crossings; B3 converged without a crossing and remains a preserved held-out negative.

## ITER063 — terminal INVALID, no gate credit

Prereg commit `04dacfba44f2a59efb882dbe162cc5161c7e7795`; production head `a6fa3c4d11b0b34298b3c3ac3e934721db757639`; authoritative run `34874671586`; aggregate job `104078941713`; aggregate artifact `10360430809`, digest `sha256:a59a92d11b4d439b25eb17a380c03298dfe606186fa7fbd5187c4483c8ef3d00`; durable report commit `d0c35b572bd803b841d0a6917676fcbaf809dbfe`.

Frozen verdict: **`INVALID_IMPLEMENTATION_OR_SELECTOR_SYMMETRY_FAIL`**. This is not a scientific failure of RC008.

All six boundary lanes numerically converged. H1/H2/H4 showed frozen-panel crossings, H3 did not. However both preregistered spatial-permutation selector controls P1 and P2 converged without crossings, violating the gate prerequisite. Those positive H lanes therefore receive no scientific gate credit and may not be cherry-picked.

## ITER064 — active permutation / seed stability diagnostic

Purpose: distinguish QMC/seed instability from an integrated spatial-permutation mismatch without changing the amplitude, observable, alpha panel or endpoint treatment.

Prereg commit: `aa2179c06bbbc3d54fbd917e1809e335839d30ed`.
Implementation commits: `03e0118bafdd0a1c3d05a383a160f506b5ea2b8e`, `35680dd447cb997793d0bd1c2eeab79eb67582ef`.
Production head: `be911ba4e7a847049f4882fbe615d0f25774b3ad`.
Authoritative run: `34874915843`.

Frozen geometries are B2 `(3,1,1,1)`, P1 `(1,3,1,1)` and P2 `(1,1,3,1)`, using the same eight prospectively frozen Sobol seeds and powers `2^16`, `2^18`. No denser retry is authorized by this preregistration.

Current scientifically useful compute: **0 queued / 3 in_progress** — jobs `104079605579` (P1), `104079605734` (P2), `104079605838` (B2). The dependent aggregate is not yet eligible.

## Readiness

Overall scientific programme: **50%**. Current ITER064 diagnostic completion: **~25%**. Candidate theory: **0% / UNFORMED**. Bridge credit: **0**.

## Exact next admissible action

Wait only for the three already-running ITER064 lanes to terminalize, then consume their raw artifacts and the dependent aggregate against the frozen diagnostic classifications. Do not launch a competing RC008 gate while these lanes are active. No threshold/model retuning is permitted after the result.
