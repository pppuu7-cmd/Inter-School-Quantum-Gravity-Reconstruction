#!/usr/bin/env python3
"""Local CEMR conformal-consistency obstruction test.

Input JSON schema (minimal):
{
  "dimension": 4,
  "G_N": 1.0,
  "sigma_G_N": 0.0,
  "patches": [
    {
      "id": "p1",
      "reference_area": 2.0,
      "entropy": 1.0,
      "sigma_reference_area": 0.02,
      "sigma_entropy": 0.01
    }
  ]
}

Natural units are assumed for A_obs = 4 G_N S. This code tests only the
local leading-semiclassical obstruction derived in
results/ITER002_CEMR_LOCAL_CONFORMAL_CONSISTENCY.md.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List


def _positive(name: str, value: Any) -> float:
    try:
        x = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be numeric") from exc
    if not math.isfinite(x) or x <= 0.0:
        raise ValueError(f"{name} must be finite and > 0")
    return x


def _nonnegative(name: str, value: Any) -> float:
    try:
        x = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be numeric") from exc
    if not math.isfinite(x) or x < 0.0:
        raise ValueError(f"{name} must be finite and >= 0")
    return x


def evaluate(payload: Dict[str, Any]) -> Dict[str, Any]:
    D = int(payload.get("dimension", 4))
    if D <= 2:
        raise ValueError("dimension must be > 2 for the codimension-2 scaling test")

    G = _positive("G_N", payload.get("G_N"))
    sigma_G = _nonnegative("sigma_G_N", payload.get("sigma_G_N", 0.0))

    raw_patches = payload.get("patches")
    if not isinstance(raw_patches, list) or len(raw_patches) < 2:
        raise ValueError("patches must be a list with at least two entries")

    rows: List[Dict[str, float | str]] = []
    all_have_positive_sigma = True

    for idx, patch in enumerate(raw_patches):
        if not isinstance(patch, dict):
            raise ValueError(f"patches[{idx}] must be an object")

        pid = str(patch.get("id", f"patch_{idx}"))
        Aref = _positive(f"{pid}.reference_area", patch.get("reference_area"))
        S = _positive(f"{pid}.entropy", patch.get("entropy"))
        sigma_Aref = _nonnegative(
            f"{pid}.sigma_reference_area", patch.get("sigma_reference_area", 0.0)
        )
        sigma_S = _nonnegative(
            f"{pid}.sigma_entropy", patch.get("sigma_entropy", 0.0)
        )

        Aobs = 4.0 * G * S
        ratio = Aobs / Aref
        r = math.log(ratio)
        omega = math.exp(r / (D - 2))

        sigma_r = math.sqrt(
            (sigma_G / G) ** 2 + (sigma_S / S) ** 2 + (sigma_Aref / Aref) ** 2
        )
        if sigma_r <= 0.0:
            all_have_positive_sigma = False

        rows.append(
            {
                "id": pid,
                "reference_area": Aref,
                "entropy": S,
                "observed_area_from_entropy": Aobs,
                "log_area_ratio_r": r,
                "omega_estimate": omega,
                "sigma_r_diagonal": sigma_r,
            }
        )

    if all_have_positive_sigma:
        weights = [1.0 / float(row["sigma_r_diagonal"]) ** 2 for row in rows]
        rbar = sum(w * float(row["log_area_ratio_r"]) for w, row in zip(weights, rows)) / sum(weights)
        chi2 = sum(
            ((float(row["log_area_ratio_r"]) - rbar) / float(row["sigma_r_diagonal"])) ** 2
            for row in rows
        )
        dof = len(rows) - 1
        mode = "WEIGHTED_DIAGONAL"
    else:
        rbar = sum(float(row["log_area_ratio_r"]) for row in rows) / len(rows)
        chi2 = None
        dof = None
        mode = "UNWEIGHTED_NO_ERROR_MODEL"

    residuals = []
    for row in rows:
        delta = float(row["log_area_ratio_r"]) - rbar
        residuals.append(delta)
        row["delta_r"] = delta

    rms_delta = math.sqrt(sum(x * x for x in residuals) / len(residuals))
    max_abs_delta = max(abs(x) for x in residuals)
    omega_common = math.exp(rbar / (D - 2))

    # Fail-closed classification. Numerical thresholds are descriptive only unless
    # the caller supplies an uncertainty model. For weighted mode, reduced chi2 is
    # used as a simple screening diagnostic rather than a publication-grade p-value.
    if chi2 is not None and dof and dof > 0:
        reduced = chi2 / dof
        if reduced <= 1.0:
            verdict = "PASS_LOCAL"
        elif reduced <= 4.0:
            verdict = "TENSION_LOCAL"
        else:
            verdict = "INCOMPATIBLE_LOCAL"
    else:
        reduced = None
        verdict = "UNCLASSIFIED_NO_ERROR_MODEL"

    return {
        "test": "CEMR_LOCAL_CONFORMAL_CONSISTENCY",
        "status": verdict,
        "domain": "leading_semiclassical_local_patch",
        "dimension": D,
        "G_N": G,
        "sigma_G_N": sigma_G,
        "mode": mode,
        "common_log_area_ratio": rbar,
        "common_omega_estimate": omega_common,
        "rms_delta_r": rms_delta,
        "max_abs_delta_r": max_abs_delta,
        "chi2": chi2,
        "dof": dof,
        "reduced_chi2": reduced,
        "patches": rows,
        "claim_lock": (
            "A local incompatibility rejects only the supplied CEMR mapping/domain; "
            "it is not a family-level refutation of causal-set or holographic approaches."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="JSON input file")
    parser.add_argument("--output", type=Path, default=None, help="optional JSON output file")
    args = parser.parse_args()

    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        result = evaluate(payload)
    except Exception as exc:  # fail closed at CLI boundary
        print(json.dumps({"status": "ERROR", "error": str(exc)}, indent=2), file=sys.stderr)
        return 2

    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
