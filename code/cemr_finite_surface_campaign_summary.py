#!/usr/bin/env python3
"""Aggregate the preregistered CEMR Stage-I campaign into auditable repo files.

This script does not tune thresholds or data. It reruns exactly the registered
4 scenarios x 3 seeds at epsilon=0.05 and sigma_log_area=0.003, applies the
classifications already encoded in cemr_finite_surface_inverse.py, and fails
closed if the registered structural expectations are not met.
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from cemr_finite_surface_inverse import fit_scenario

SEEDS = (101, 211, 307)
SCENARIOS = (
    "clean_calibrated",
    "global_scale_nuisance",
    "channel_anisotropy",
    "channel_profiled",
)
EXPECTED = {
    "clean_calibrated": "PASS_SCOPED",
    "global_scale_nuisance": "BLOCKED_NONIDENTIFIABLE",
    "channel_anisotropy": "INCOMPATIBLE_SCALAR_CONFORMAL_SCOPED",
    "channel_profiled": "PASS_SCOPED",
}
EPSILON = 0.05
SIGMA = 0.003


def main() -> int:
    results = []
    failures = []
    for scenario in SCENARIOS:
        for seed in SEEDS:
            r = fit_scenario(
                scenario,
                seed=seed,
                epsilon=EPSILON,
                sigma_log_area=SIGMA,
            )
            row = asdict(r)
            results.append(row)
            if r.classification != EXPECTED[scenario]:
                failures.append(
                    f"{scenario}/seed{seed}: expected {EXPECTED[scenario]}, got {r.classification}"
                )

    payload = {
        "protocol": "ITER002_CEMR_FINITE_SURFACE_INVERSION_PROTOCOL",
        "stage": "Stage-I fixed-surface conformal inverse",
        "epsilon": EPSILON,
        "sigma_log_area": SIGMA,
        "seeds": list(SEEDS),
        "expected_classifications": EXPECTED,
        "all_registered_expectations_met": not failures,
        "failures": failures,
        "results": results,
        "claim_lock": [
            "No full RT/QES inversion claim.",
            "No causal-order + entanglement sufficiency claim.",
            "No uniqueness or new-quantum-gravity claim.",
            "BLOCKED_NONIDENTIFIABLE is not physical failure.",
        ],
    }

    root = Path(__file__).resolve().parents[1]
    json_path = root / "results" / "ITER002_CEMR_FINITE_SURFACE_INVERSION.json"
    md_path = root / "results" / "ITER002_CEMR_FINITE_SURFACE_INVERSION.md"
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "# ITER002 — CEMR finite-surface inversion result",
        "",
        "Status: **AUDITED / DOMAIN_SCOPED**" if not failures else "Status: **AUDIT_FAILED / DO_NOT_INTERPRET**",
        "",
        f"Registered grid: 4 scenarios × 3 seeds; `epsilon={EPSILON}`, `sigma_log_area={SIGMA}`.",
        "",
        "| Scenario | Seed | Class | rank/npar | red. chi2 | max |theta-theta_true| | nuisance | condition |",
        "|---|---:|---|---:|---:|---:|---:|---:|",
    ]
    for r in results:
        red = "—" if r["reduced_chi2"] is None else f'{r["reduced_chi2"]:.6g}'
        nuisance = "—" if r["nuisance_fit"] is None else f'{r["nuisance_fit"]:.6g}'
        cond = "rank-deficient" if r["condition_number"] is None else f'{r["condition_number"]:.6g}'
        lines.append(
            f'| {r["scenario"]} | {r["seed"]} | {r["classification"]} | '
            f'{r["jacobian_rank"]}/{r["n_parameters"]} | {red} | '
            f'{r["max_abs_theta_error"]:.6g} | {nuisance} | {cond} |'
        )

    lines += [
        "",
        "## Registered interpretation",
        "",
        "- `clean_calibrated`: finite fixed-surface conformal parameters are recoverable in this controlled model.",
        "- `global_scale_nuisance`: absolute conformal scale is structurally non-identifiable without an independent scale/calibration anchor; this is `BLOCKED_NONIDENTIFIABLE`, not a failure of CEMR.",
        "- `channel_anisotropy`: duplicated identical geometric surfaces with opposite non-geometric distortions cannot be absorbed by a scalar conformal field in the registered test.",
        "- `channel_profiled`: when the nuisance signature is explicitly parameterized and identifiable, the false geometric tension can be profiled out.",
        "",
        "## Claim lock",
        "",
        "These results do **not** establish full RT/QES inversion, causal+entanglement sufficiency for a Lorentzian metric, uniqueness, a quantum-gravity theory, or new physics.",
        "",
        "The next authorized CEMR level is a preregistered metric-dependent/extremal-surface inverse problem with wrong-class and QES-like nuisance challenges.",
    ]
    if failures:
        lines += ["", "## Audit failures", ""] + [f"- {x}" for x in failures]

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "all_registered_expectations_met": not failures,
        "failures": failures,
        "json": str(json_path),
        "markdown": str(md_path),
    }, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
