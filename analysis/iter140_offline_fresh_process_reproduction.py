#!/usr/bin/env python3
"""Offline fresh-process reproduction of frozen ITER140 v6.

Infrastructure only. Runs the already committed v6 exact shard implementation for
all 24 (D,family) pairs in fresh Python processes, then runs the unchanged v6
aggregator. No basis, dimension, heldout, degree, authority, classification, or
claim-ceiling predicate is changed.

This exists so ITER140 can be reproduced independently of GitHub Actions runner
availability. The authoritative frozen scripts remain:
  analysis/iter140_family_dimension_shard_v6.py
  analysis/iter140_aggregate_v6.py
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

FAMILIES = [
    "M_R2_chi1_dR1",
    "M_R1_chi1_dR2",
    "G_R1_chi2_Gamma2_dR1",
]


def scientific_payload(o: dict) -> dict:
    return {
        "D": o["D"],
        "family": o["family"],
        "coefficients": o["coefficients"],
        "heldouts": [
            {
                "panel": h["panel"],
                "direct": h["direct"],
                "reconstructed": h["reconstructed"],
                "equal": h["equal"],
            }
            for h in o["heldouts"]
        ],
        "D4_terminal_authority": o["D4_terminal_authority"],
        "D4_terminal_authority_ok": o["D4_terminal_authority_ok"],
    }


def sha256_payload(o: dict) -> str:
    b = json.dumps(scientific_payload(o), sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="iter140_offline_reproduction")
    args = ap.parse_args()

    repo = Path(__file__).resolve().parents[1]
    out = (repo / args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    shard_script = repo / "analysis" / "iter140_family_dimension_shard_v6.py"
    agg_script = repo / "analysis" / "iter140_aggregate_v6.py"

    with tempfile.TemporaryDirectory(prefix="iter140-offline-") as td:
        shard_dir = Path(td)
        manifest = []
        for D in range(3, 11):
            for family in FAMILIES:
                name = f"iter140_v6_D{D}_{family}.json"
                transient = repo / name
                transient.unlink(missing_ok=True)
                cp = subprocess.run(
                    [sys.executable, str(shard_script), str(D), family],
                    cwd=repo,
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                )
                (out / f"D{D}_{family}.log").write_text(cp.stdout, encoding="utf-8")
                if cp.returncode != 0 or not transient.exists():
                    raise SystemExit(f"shard failed D={D} family={family} rc={cp.returncode}")
                target = shard_dir / name
                shutil.move(str(transient), target)
                o = json.loads(target.read_text(encoding="utf-8"))
                manifest.append(
                    {
                        "D": D,
                        "family": family,
                        "scientific_payload_sha256": sha256_payload(o),
                    }
                )

        aggregate_transient = repo / "iter140_first_mg_general_d_invariant_continuation_v6.json"
        aggregate_transient.unlink(missing_ok=True)
        cp = subprocess.run(
            [sys.executable, str(agg_script), str(shard_dir)],
            cwd=repo,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        (out / "aggregate.log").write_text(cp.stdout, encoding="utf-8")
        if not aggregate_transient.exists():
            raise SystemExit(f"aggregate produced no JSON rc={cp.returncode}")
        result = json.loads(aggregate_transient.read_text(encoding="utf-8"))
        shutil.move(str(aggregate_transient), out / aggregate_transient.name)
        certificate = {
            "gate": "ITER140_OFFLINE_FRESH_PROCESS_EXACT_REPRODUCTION",
            "scientific_predicates_changed": False,
            "aggregate_exit_code": cp.returncode,
            "classification": result.get("classification"),
            "max_observed_trace_polynomial_degree": result.get("max_observed_trace_polynomial_degree"),
            "checks": result.get("checks"),
            "shard_scientific_payload_hashes": manifest,
            "claim_ceiling": result.get("claim_ceiling"),
        }
        (out / "certificate.json").write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(certificate, indent=2))
        return cp.returncode


if __name__ == "__main__":
    raise SystemExit(main())
