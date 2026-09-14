#!/usr/bin/env python3
"""ITER062A implementation-only repair: expose both preregistered source files to unchanged lane predicates.

Primary identity is corrected by prereg/ITER062A_PROVENANCE_HASH_CORRECTION_2026-09-14.md
from pre-existing ITER006 artifacts; no scientific predicate changes.
"""
import argparse, hashlib, importlib.util, json
from pathlib import Path

PRIMARY_EXPECTED_SHA256="ba973b02a05688c2b122c95a111b70b0fe03a126fac399b073725574afc7358b"
DEPENDENCY_EXPECTED_SHA256="78415347fa92b1d0bce1bbd4010faeb3cc939c5f5d6b14d72f340138e4c573ef"

def h(raw): return hashlib.sha256(raw).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['vertex-kernel-closure','observable-closure']); ap.add_argument('--dependency',required=True); ap.add_argument('--primary',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    dep_raw=Path(a.dependency).read_bytes(); pri_raw=Path(a.primary).read_bytes()
    dep_sha=h(dep_raw); pri_sha=h(pri_raw)
    if dep_sha!=DEPENDENCY_EXPECTED_SHA256 or pri_sha!=PRIMARY_EXPECTED_SHA256:
        raise SystemExit(f'SOURCE_IDENTITY_MISMATCH dependency={dep_sha} primary={pri_sha}')
    spec=importlib.util.spec_from_file_location('closure',Path(__file__).with_name('closure.py')); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    corpus=dep_raw.decode('utf-8',errors='replace')+'\n\n% --- PRIMARY SOURCE FOLLOWS ---\n'+pri_raw.decode('utf-8',errors='replace')
    res=mod.run_lane(a.lane,corpus,dep_sha)
    res['implementation_repair']='SOURCE_SET_COMPLETE_PRIMARY_PLUS_DEPENDENCY_WITH_PREEXISTING_ITER006_HASH_CORRECTION'
    res['primary_source_sha256']=pri_sha
    res['dependency_source_sha256']=dep_sha
    Path(a.out).write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
    print(json.dumps(res,indent=2,sort_keys=True))

if __name__=='__main__': main()
