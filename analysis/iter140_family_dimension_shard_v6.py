#!/usr/bin/env python3
"""ITER140 v6 shard: v5 exact family x dimension computation with rank-path repair.

Scientific predicates are identical to frozen ITER140 and v5. The only change is
infrastructure: do not call SymPy Matrix.rank() on the already certified 28x28
nonsingular design matrix. frozen.design_panels() itself checks det(A) != 0, so a
28x28 accepted matrix has exact rank 28. This avoids the SymPy 1.14 rank path that
caused every v5 shard to hit its 12-minute job timeout after exact work completed.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
import sympy as s

import iter140_first_mg_general_d_invariant_continuation as frozen
import iter140_first_mg_general_d_invariant_continuation_v2 as fast

D = int(sys.argv[1])
family = sys.argv[2]
if D not in range(3, 11):
    raise SystemExit("D must be 3..10")
if family not in fast.FAMILIES:
    raise SystemExit(f"unknown family {family}")

fn = fast.FAMILIES[family]
labels = frozen.basis_labels()
selected, A = frozen.design_panels()
if len(frozen.BASIS) != 28 or len(selected) != 28 or A.rows != 28 or A.cols != 28:
    raise SystemExit("frozen ITER140 design dimensions changed")
# frozen.design_panels() raises if A.det() == 0. For a 28x28 matrix this is an
# exact rank-28 certificate; do not call A.rank(), which is the v5 timeout path.
design_rank = 28
Ainv = A.inv(method="DM")
nvec = tuple([1] + [0] * (D - 1))

ys = []
for panel, (q3, k3) in enumerate(selected):
    direct = fast.to_sym(fn(fast.pad(q3, D), fast.pad(k3, D), nvec, D))
    ys.append(direct)
    print(
        json.dumps(
            {
                "progress_dimension": D,
                "family": family,
                "design_panel": panel,
            }
        ),
        flush=True,
    )
coeff = [s.factor(x) for x in (Ainv * s.Matrix(ys))]

held_seed = [
    ((1, 2, -1, 3), (2, -1, 1, 4)),
    ((2, 1, 3, -2), (-1, 2, 4, 1)),
    ((-2, 3, 1, 2), (3, -1, 2, -2)),
]
held = []
held_ok = True
for idx, (q4, k4) in enumerate(held_seed):
    qv = tuple(list(q4[: min(4, D)]) + [0] * max(0, D - 4))
    kv = tuple(list(k4[: min(4, D)]) + [0] * max(0, D - 4))
    bvals = fast.basis_values_full(qv, kv)
    direct = fast.to_sym(fn(qv, kv, nvec, D))
    recon = s.factor(sum(c * v for c, v in zip(coeff, bvals)))
    eq = bool(s.simplify(direct - recon) == 0)
    held_ok &= eq
    held.append(
        {
            "panel": idx,
            "q": list(qv),
            "k": list(kv),
            "basis_values": [str(x) for x in bvals],
            "direct": str(direct),
            "reconstructed": str(recon),
            "equal": eq,
        }
    )

authority_ok = True
authority_rows = []
if D == 4:
    manifest = json.loads(
        Path("analysis/iter140_d4_terminal_authority_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    for idx, row in enumerate(held):
        expected = s.sympify(manifest["panels"][idx][family])
        observed = s.sympify(row["direct"])
        eq = bool(observed == expected)
        authority_ok &= eq
        authority_rows.append(
            {
                "panel": idx,
                "observed": str(observed),
                "terminal_authority": str(expected),
                "equal": eq,
            }
        )

out = {
    "D": D,
    "family": family,
    "basis_size": len(frozen.BASIS),
    "design_rank": design_rank,
    "design_rank_certificate": (
        "28x28 matrix accepted by frozen.design_panels() exact nonzero-determinant check; "
        "SymPy Matrix.rank() intentionally not called"
    ),
    "scientific_predicates_changed": False,
    "coefficients": [str(x) for x in coeff],
    "heldouts": held,
    "heldouts_ok": bool(held_ok),
    "D4_terminal_authority": authority_rows,
    "D4_terminal_authority_ok": bool(authority_ok),
    "authority_manifest": "analysis/iter140_d4_terminal_authority_manifest.json",
}
name = family.replace("/", "_")
Path(f"iter140_v6_D{D}_{name}.json").write_text(
    json.dumps(out, indent=2) + "\n", encoding="utf-8"
)
print(
    json.dumps(
        {
            "D": D,
            "family": family,
            "heldouts_ok": held_ok,
            "D4_authority_ok": authority_ok,
            "design_rank_certified": design_rank,
        }
    ),
    flush=True,
)
if not held_ok or (D == 4 and not authority_ok):
    raise SystemExit(1)
