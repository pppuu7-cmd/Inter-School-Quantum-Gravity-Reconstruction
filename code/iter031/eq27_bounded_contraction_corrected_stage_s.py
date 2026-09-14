#!/usr/bin/env python3
import argparse, ast, hashlib, importlib.util, pathlib

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

# Technical repair only: the inherited ITER027 authority check searched raw source
# text and therefore matched the forbidden-token *string literals in its own
# checker*.  Inspect executable AST references instead; frozen prerequisites,
# panels, alpha and numerical thresholds are unchanged.
def authority_domain():
    missing=[str(p.relative_to(ROOT)) for p in k.REQ if not p.exists()]
    texts={str(p.relative_to(ROOT)):p.read_text(encoding='utf-8') for p in k.REQ if p.exists()}
    forbidden_names={'formLambda6j','eq29_amplitude','lambda_qbinomial'}
    forbidden=[]
    for path in (ROOT/'code/iter027/eq27_bounded_component_contraction.py', pathlib.Path(__file__)):
        tree=ast.parse(path.read_text(encoding='utf-8'))
        used=set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                used.add(node.id)
            elif isinstance(node, ast.Attribute):
                used.add(node.attr)
            elif isinstance(node, ast.Import):
                used.update(a.name.split('.')[-1] for a in node.names)
            elif isinstance(node, ast.ImportFrom):
                used.update(a.name for a in node.names)
        forbidden.extend(sorted(forbidden_names & used))
    forbidden=sorted(set(forbidden))
    panels={str(level):[list(x) for x in k.admissible_rows(level)] for level in k.PRIMARY+k.HELDOUT}
    provenance={name:hashlib.sha256(text.encode()).hexdigest() for name,text in texts.items()}
    ok=(not missing and not forbidden and all(panels[str(level)] for level in k.PRIMARY+k.HELDOUT))
    k.write({'lane':'authority-domain','missing':missing,'forbidden_dependencies':forbidden,'alpha':0,'panels':panels,'provenance_sha256':provenance,'pass':bool(ok)})

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--lane',required=True,choices=['authority-domain','component-translation','bounded-contraction','null-controls'])
    a=ap.parse_args()
    try:
        {'authority-domain':authority_domain,
         'component-translation':k.translation,
         'bounded-contraction':k.contraction,
         'null-controls':k.null_controls}[a.lane]()
    except Exception as e:
        k.write({'lane':a.lane,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e),'pass':False})

if __name__=='__main__': main()
