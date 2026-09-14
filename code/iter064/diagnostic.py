#!/usr/bin/env python3
import argparse, importlib.util, json
from pathlib import Path
PARENT=Path(__file__).resolve().parents[1]/'iter062b'/'reconstruct.py'
spec=importlib.util.spec_from_file_location('iter062b_reconstruct',PARENT); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
BOUNDARIES={'B2':(3.0,1.0,1.0,1.0),'P1':(1.0,3.0,1.0,1.0),'P2':(1.0,1.0,3.0,1.0)}
SEEDS=[32452843,49979687,67867967,86028121,104395301,122949823,141650939,160481183]
POWERS=[16,18]
def run(name):
    bd=BOUNDARIES[name]; rows=[]
    for seed in SEEDS:
        for power in POWERS:
            rows.append({'boundary':name,'coords':bd,'seed':seed,'power':power,'coarse':m.coarse_samples(bd,seed,power),'fine':m.fine_samples(bd,seed,power)})
    return {'boundary':name,'coords':bd,'alphas':m.ALPHAS.tolist(),'seeds':SEEDS,'powers':POWERS,'rows':rows,'claim_lock':'diagnostic only; no bridge credit'}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--boundary',choices=sorted(BOUNDARIES),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    r=run(a.boundary); Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n'); print(json.dumps({'boundary':a.boundary,'rows':len(r['rows'])},indent=2))
if __name__=='__main__': main()
