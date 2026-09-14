#!/usr/bin/env python3
import argparse, importlib.util, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('iter027_kernel', ROOT/'code/iter027/eq27_bounded_component_contraction.py')
k = importlib.util.module_from_spec(spec); spec.loader.exec_module(k)

k.OUT = ROOT/'out'/'iter031'
k.OUT.mkdir(parents=True, exist_ok=True)
k.REQ = [
    ROOT/'prereg/ITER031_RC006_EQ27_BOUNDED_CONTRACTION_CORRECTED_STAGE_S_2026-09-14.md',
    ROOT/'results/ITER030_RC006_EQ27_CORRECTED_STAGE_S_PASS_2026-09-14.md',
    ROOT/'results/ITER021_RC006_EQ27_COMPONENT_TRANSLATION_2026-09-14.md',
    ROOT/'results/ITER026_RC006_DIRECT_SOURCE_QBAR_PRIMITIVE_2026-09-14.md',
    ROOT/'sources/ITER025_RC006_QBAR_R_AUTHORITY.md',
]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--lane',required=True,choices=['authority-domain','component-translation','bounded-contraction','null-controls'])
    a=ap.parse_args()
    try:
        {'authority-domain':k.authority_domain,
         'component-translation':k.translation,
         'bounded-contraction':k.contraction,
         'null-controls':k.null_controls}[a.lane]()
    except Exception as e:
        k.write({'lane':a.lane,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e),'pass':False})

if __name__=='__main__': main()
