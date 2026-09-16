#!/usr/bin/env python3
"""ITER148 v3 infrastructure shard: one frozen tau x design-panel chunk.

Scientific object and predicates are identical to preregistered ITER148.  This
implementation only bounds SymPy process state by evaluating 15 of the frozen 45
design panels per fresh CI job.  The exact 45-row independence certificate is the
one already constructed inside base.design_panels(); no redundant Matrix.rank()
is evaluated here.
"""
from __future__ import annotations

import gc
import json
import sys
from pathlib import Path
import sympy as s
from sympy.core.cache import clear_cache

import iter148_m3_full_invariant_bubble_reduced_numerator as base

j = int(sys.argv[1])
chunk = int(sys.argv[2])
if j not in range(9):
    raise SystemExit("tau index must be 0..8")
if chunk not in range(3):
    raise SystemExit("chunk index must be 0..2")

t = s.Rational(j, 8)
selected, A = base.design_panels()
if len(base.BASIS) != 45 or len(selected) != 45 or A.rows != 45 or A.cols != 45:
    raise SystemExit("frozen ITER148 design dimensions changed")

design_rank = 45
start = 15 * chunk
stop = start + 15
n0 = (s.Integer(1), 0, 0, 0)
values = []
for panel_index in range(start, stop):
    q, k = selected[panel_index]
    direct = base.numerator_fast(q, k, n0, t)[0]
    values.append({"panel_index": panel_index, "value": str(direct)})
    print(json.dumps({"stage":"design_panel_done","tau_index":j,"chunk_index":chunk,"panel_index":panel_index}), flush=True)
    del direct
    clear_cache()
    gc.collect()

held_seed = [
    ((1, 2, -1, 3), (2, -1, 1, 4), (1, 0, 0, 0)),
    ((2, 1, 3, -2), (-1, 2, 4, 1), (0, 1, 0, 0)),
    ((-2, 3, 1, 2), (3, -1, 2, -2), (0, 0, 1, 0)),
]
held = []
if chunk == 0:
    for idx, (q0, k0, nv0) in enumerate(held_seed):
        q = tuple(map(s.Integer, q0)); k = tuple(map(s.Integer, k0)); nv = tuple(map(s.Integer, nv0))
        direct = base.numerator_fast(q, k, nv, t)[0]
        bvals = base.basis_values(q, k, nv)
        held.append({"panel":idx,"direct":str(direct),"basis_values":[str(x) for x in bvals]})
        print(json.dumps({"stage":"heldout_direct_done","tau_index":j,"chunk_index":chunk,"heldout_panel":idx}), flush=True)
        del direct, bvals
        clear_cache()
        gc.collect()

out = {
    "gate":"ITER148_FIXED_GEODESIC_CURVATURE_M3_FULL_INVARIANT_BUBBLE_REDUCED_NUMERATOR",
    "implementation":"v3_tau_x_design_chunk",
    "scientific_predicates_changed":False,
    "tau_index":j,"tau":str(t),"chunk_index":chunk,
    "panel_start":start,"panel_stop_exclusive":stop,
    "basis_size":len(base.BASIS),"design_rank":design_rank,
    "design_rank_certificate":"base.design_panels exact rational incremental-pivot construction accepted 45 independent rows for 45 columns; generic Matrix.rank intentionally not called",
    "design_values":values,"training_heldout_direct":held,
}
Path(f"iter148_v3_tau_{j}_chunk_{chunk}.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"stage":"chunk_complete","tau_index":j,"chunk_index":chunk,"design_values":len(values),"heldouts":len(held),"design_rank_certified":design_rank}), flush=True)
