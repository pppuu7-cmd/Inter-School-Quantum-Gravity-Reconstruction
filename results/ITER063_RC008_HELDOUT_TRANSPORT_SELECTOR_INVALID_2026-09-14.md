# ITER063 — RC008 held-out non-retuned transport / selector

Date: 2026-09-14

## Frozen provenance

- prereg commit: `04dacfba44f2a59efb882dbe162cc5161c7e7795`
- implementation commits: `a30bd8a3b4b06d61506411a18dd3d48dd2825318`, `8b248e50c19ae8829af98f00c74cf98acf0892df`
- production head: `a6fa3c4d11b0b34298b3c3ac3e934721db757639`
- authoritative run: `34874671586`
- aggregate job: `104078941713`
- aggregate artifact: `10360430809`
- aggregate digest: `sha256:a59a92d11b4d439b25eb17a380c03298dfe606186fa7fbd5187c4483c8ef3d00`

## Frozen verdict

**INVALID IMPLEMENTATION / SELECTOR GATE — `INVALID_IMPLEMENTATION_OR_SELECTOR_SYMMETRY_FAIL`**

This is neither SCIENTIFIC PASS nor SCIENTIFIC FAIL for RC008 transport.

Calibration passed unchanged. All six boundary lanes numerically converged under the preregistered central-alpha criteria.

Observed frozen outcomes:

- P1 `(1,3,1,1)`: converged, no robust crossing;
- P2 `(1,1,3,1)`: converged, no robust crossing;
- H1 `(2,1,1,2)`: converged, robust crossing `[0.50,0.55]`, report-only interpolation `0.5347251647651552`;
- H2 `(2,3,1,1)`: converged, robust crossing `[0.50,0.55]`, `0.5177223419981958`;
- H3 `(2,3,4,1)`: converged, no robust crossing;
- H4 `(1,2,3,2)`: converged, robust crossing `[0.50,0.55]`, `0.5249808090608553`.

The preregistered permutation-control requirement demanded both P1 and P2 reproduce the parent B2 crossing modulo the frozen adjacent-bracket allowance. They did not. Therefore the gate must stop at INVALID rather than cherry-picking the three positive H lanes.

## Interpretation lock

The H1/H2/H4 positives are preserved as diagnostic observations only and receive no gate credit because the selector-control prerequisite failed. H3 is preserved as a converged no-crossing negative.

The next admissible work is a prospectively frozen integral-level permutation/seed diagnostic to determine whether the failure comes from the source/implementation symmetry object, QMC coordinate orientation / seed transport, or inadequacy of the existing convergence criterion. No threshold or model may be changed retroactively.

Candidate theory remains `0 / UNFORMED`; bridge credit remains zero.
