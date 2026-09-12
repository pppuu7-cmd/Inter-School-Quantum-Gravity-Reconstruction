# ITER006 — Lorentzian EPRL two-vertex equation-selection robustness FAIL

Date: 2026-09-12

## Frozen gate

After source qualification and exact math-environment extraction for arXiv:1801.03771, each of eight numerical targets had to select the identical nearest exact math object under every usable leave-one-anchor-pattern-out perturbation. Thresholds and lexical anchors were frozen before the result.

## Authoritative run

- workflow run: `34701317882`
- head: `531d0a21de4d6b136c9f1ed789061b72112f41d1`
- aggregate job: `103573499012`
- summary artifact: `10299439561`
- artifact digest: `sha256:58eabfe9e017b421349b1100f05e16981e213905bdd82bc8e8bbd9cf368a48c8`

## Result

Scientific classification: `SOURCE_EQUATION_SELECTION_ROBUSTNESS_FAIL`.

Only **2/8** targets were stable:

- `full_amplitude`: stable
- `correlation_observable`: stable

Unstable:

- `two_vertex_amplitude`
- `internal_face_sum`
- `simplified_amplitude`
- `large_spin_scaling`
- `immirzi`
- `cutoff_or_truncation`

Example: `two_vertex_amplitude` was valid but only 2/3 usable leave-one-anchor holdouts retained the full-selection hash `799f56dc22f55a09bf744d62c459ee95e38794e5be02c114a73d06c057d0e94c` (job `103573472701`, artifact `10300302989`).

## Interpretation

This is a **source-authority/source-selection FAIL**, not an infrastructure failure and not a failure of Lorentzian EPRL physics. It blocks numerical two-vertex reproduction under the frozen gate. No threshold or anchor is relaxed post hoc.

Permitted next work is diagnostic only: localize which anchors select which exact environments, identify equation labels/sections/files, and audit explicit source `\\eqref`/`\\ref` links. A later source-lock may be preregistered only if this independent source evidence supplies an unambiguous authority rule. The present FAIL remains preserved.

No numerical amplitude reproduction, refinement claim, bridge promotion, candidate theory, or new-physics claim is authorized by this result.
