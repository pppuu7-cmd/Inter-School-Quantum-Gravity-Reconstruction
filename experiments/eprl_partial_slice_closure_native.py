#!/usr/bin/env python3
"""Fail-closed partial-slice closure diagnostic for stored sl2cfoam EPRL tensors.

Input tensors are written by the upstream `vertex-fulltensor` executable from a
pinned sl2cfoam-next commit.  The .sl2t format is parsed according to the
upstream TENSOR_STORE macro: 128 size_t dimension slots, 1024 tag bytes, then
column-major Float64 data.  For the all-j=1/2 case the full vertex tensor is
2x2x2x2x2.

We keep tensor axes 0 and 1 open as a 2x2 partial operator and fix axes 2..4 to
several boundary slices.  A rank-1 retained sector is learned once from the
Dl=0 (0,0,0) slice and frozen for all heterogeneous holdouts.  Rank-matched
complex Haar sectors provide the null/control ensemble.

This is an operator-level source-native diagnostic, not a full two-complex
spinfoam gluing theorem and not a quantum-gravity model claim.
"""
from __future__ import annotations

import argparse, json, math, struct
from pathlib import Path
import numpy as np

HEADER_DIMS = 128
TAG_BYTES = 1024


def load_sl2t(path: Path) -> np.ndarray:
    raw = path.read_bytes()
    word = struct.calcsize("P")
    header = HEADER_DIMS * word + TAG_BYTES
    if len(raw) < header:
        raise RuntimeError(f"short sl2t file: {path} ({len(raw)} bytes)")
    fmt = "=" + ("Q" if word == 8 else "I") * HEADER_DIMS
    dims_all = struct.unpack_from(fmt, raw, 0)
    dims = tuple(int(x) for x in dims_all[:5])
    if dims != (2, 2, 2, 2, 2):
        raise RuntimeError(f"expected 2^5 EPRL tensor, got dims={dims} from {path}")
    n = math.prod(dims)
    need = header + 8 * n
    if len(raw) != need:
        raise RuntimeError(f"unexpected sl2t size {len(raw)} != {need} for {path}")
    data = np.frombuffer(raw, dtype=np.float64, count=n, offset=header).copy()
    if not np.all(np.isfinite(data)):
        raise RuntimeError(f"non-finite EPRL tensor entries in {path}")
    if not np.any(data != 0.0):
        raise RuntimeError(f"all-zero EPRL tensor in {path}")
    return data.reshape(dims, order="F")


def haar_basis(n: int, r: int, rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(n, r)) + 1j * rng.normal(size=(n, r))
    q, _ = np.linalg.qr(z)
    return q[:, :r]


def top_right_singular_basis(a: np.ndarray, r: int) -> np.ndarray:
    _, _, vh = np.linalg.svd(np.asarray(a, dtype=np.complex128), full_matrices=False)
    return vh.conj().T[:, :r]


def metrics(a1: np.ndarray, a2: np.ndarray, v: np.ndarray) -> tuple[float, float]:
    a1 = np.asarray(a1, np.complex128); a2 = np.asarray(a2, np.complex128)
    a1v = a1 @ v
    qa1v = a1v - v @ (v.conj().T @ a1v)
    leak = np.linalg.norm(qa1v) / max(np.linalg.norm(a1v), np.finfo(float).eps)
    num = v.conj().T @ (a2 @ qa1v)
    den = v.conj().T @ (a2 @ (a1 @ v))
    ret = np.linalg.norm(num) / max(np.linalg.norm(den), np.finfo(float).eps)
    return float(leak), float(ret)


def slice2(t: np.ndarray, fixed: tuple[int, int, int]) -> np.ndarray:
    # axes 0,1 remain open; axes 2,3,4 are fixed.  Labels are zero-based.
    return np.asarray(t[:, :, fixed[0], fixed[1], fixed[2]], dtype=float)


def run(t0: np.ndarray, t1: np.ndarray, nrandom: int, seed: int) -> dict:
    triples = {
        "000": (0,0,0), "100": (1,0,0), "010": (0,1,0),
        "001": (0,0,1), "111": (1,1,1),
    }
    s0 = {k: slice2(t0, v) for k,v in triples.items()}
    s1 = {k: slice2(t1, v) for k,v in triples.items()}
    train = s0["000"]
    p = top_right_singular_basis(train, 1)
    cases = [
        ("Dl0_100_to_010", s0["100"], s0["010"]),
        ("Dl0_010_to_001", s0["010"], s0["001"]),
        ("Dl1_100_to_010", s1["100"], s1["010"]),
        ("cross_Dl0_100_to_Dl1_010", s0["100"], s1["010"]),
        ("cross_Dl1_001_to_Dl0_111", s1["001"], s0["111"]),
    ]
    rng = np.random.default_rng(seed)
    rows=[]
    for label,a1,a2 in cases:
        pl,pr = metrics(a1,a2,p)
        rl=[]; rr=[]
        for _ in range(nrandom):
            r=haar_basis(2,1,rng)
            x,y=metrics(a1,a2,r); rl.append(x); rr.append(y)
        rl=np.asarray(rl); rr=np.asarray(rr)
        rows.append({
            "label":label,
            "operator_relative_difference":float(np.linalg.norm(a2-a1)/max(np.linalg.norm(a1),np.finfo(float).eps)),
            "source_leakage":pl,
            "source_return_defect":pr,
            "mean_random_leakage":float(rl.mean()),
            "mean_random_return_defect":float(rr.mean()),
            "leakage_improvement":float(rl.mean()/max(pl,np.finfo(float).eps)),
            "return_improvement":float(rr.mean()/max(pr,np.finfo(float).eps)),
            "fraction_random_worse_leakage":float(np.mean(rl>pl)),
            "fraction_random_worse_return":float(np.mean(rr>pr)),
        })
    return {
        "test":"LORENTZIAN_EPRL_PARTIAL_SLICE_CLOSURE_NATIVE",
        "status":"PASS_EXECUTION",
        "train_matrix":train.tolist(),
        "train_singular_values":np.linalg.svd(train,compute_uv=False).tolist(),
        "tensor_dl0_norm":float(np.linalg.norm(t0)),
        "tensor_dl1_norm":float(np.linalg.norm(t1)),
        "relative_shell_change":float(np.linalg.norm(t1-t0)/max(np.linalg.norm(t0),np.finfo(float).eps)),
        "n_random_per_case":nrandom,
        "cases":rows,
        "claim_lock":"Pinned Lorentzian EPRL 4-simplex vertex tensor partial-slice operator diagnostic. It is not yet full two-vertex spinfoam gluing, continuum refinement, or evidence of a complete QG theory."
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--dl0',type=Path,required=True); p.add_argument('--dl1',type=Path,required=True)
    p.add_argument('--n-random',type=int,default=2048); p.add_argument('--seed',type=int,default=20260912)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    out=run(load_sl2t(a.dl0),load_sl2t(a.dl1),a.n_random,a.seed)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
