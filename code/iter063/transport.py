#!/usr/bin/env python3
import argparse, importlib.util, json
from pathlib import Path

PARENT = Path(__file__).resolve().parents[1] / 'iter062b' / 'reconstruct.py'
spec = importlib.util.spec_from_file_location('iter062b_reconstruct', PARENT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

mod.BOUNDARIES = {
    'P1': (1.0,3.0,1.0,1.0),
    'P2': (1.0,1.0,3.0,1.0),
    'H1': (2.0,1.0,1.0,2.0),
    'H2': (2.0,3.0,1.0,1.0),
    'H3': (2.0,3.0,4.0,1.0),
    'H4': (1.0,2.0,3.0,2.0),
}
mod.SEEDS = [32452843,49979687,67867967]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--mode',choices=['calibration','boundary'],required=True)
    ap.add_argument('--boundary',choices=sorted(mod.BOUNDARIES))
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    if a.mode=='calibration':
        res=mod.calibration()
    else:
        if not a.boundary: raise SystemExit('--boundary required')
        res=mod.boundary_run(a.boundary)
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
    print(json.dumps(res if a.mode=='calibration' else {'boundary':a.boundary,'rows':len(res['rows'])},indent=2))

if __name__=='__main__': main()
