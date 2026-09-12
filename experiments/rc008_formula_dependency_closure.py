#!/usr/bin/env python3
"""Official-source labelled-formula dependency closure for RC008.

Records exact source labels, references and macro names needed for the executable
quantum-cuboid amplitude/refinement reconstruction. No numerical fitting occurs.
"""
from pathlib import Path
import argparse, hashlib, json, re

TARGETS={
 'amplitude':['Eq:VertexDefinition','Eq:QuantumCuboid','Eq:AmplitudeIntegral','Eq:ComplexAction','Eq:AsymptoticStateSum'],
 'observable':['Eq:4Volume','Eq:StateSum'],
 'embedding':['Eq:EmbeddingMaps','Eq:RenormalizedAmplitude_abstract','Eq:RenormalizedAmplitude'],
 'matching':['Eq:Observable','Eq:ExpectationValueCoarseGraining','Eq:FixedPoint01','Eq:FixedPoint02']
}
def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def norm(s): return ' '.join(re.sub(r'(?<!\\)%.*',' ',s).split())

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--role',required=True,choices=TARGETS); ap.add_argument('--output',required=True); a=ap.parse_args()
    root=Path(a.source_dir); files=[]
    for p in root.rglob('*.tex'):
        txt=p.read_text(errors='ignore')
        if any(('\\label{'+lab+'}') in txt for lab in TARGETS[a.role]): files.append((p,txt))
    found=[]
    for lab in TARGETS[a.role]:
        row={'label':lab,'found':False}
        for p,txt in files:
            needle='\\label{'+lab+'}'; pos=txt.find(needle)
            if pos<0: continue
            lo=max(0,pos-1800); hi=min(len(txt),pos+2200); ctx=txt[lo:hi]; nctx=norm(ctx)
            refs=sorted(set(re.findall(r'\\(?:eqref|ref)\{([^{}]+)\}',ctx)))
            macros=sorted(set(re.findall(r'\\([A-Za-z@]+)',ctx)))
            row.update({'found':True,'path':str(p.relative_to(root)),'file_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'context_sha256':sha(nctx),'references':refs,'macros':macros[:120]})
            break
        found.append(row)
    ok=all(x['found'] for x in found)
    out={'test':'RC008_FORMULA_DEPENDENCY_CLOSURE','role':a.role,'targets':TARGETS[a.role],'target_count':len(found),'all_targets_found':ok,'records':found,'frozen_gate_pass':ok,'claim_lock':'Dependency/provenance closure only; no amplitude, variance curve, RG flow or bridge claim.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2,sort_keys=True))
    if not ok: raise SystemExit(2)
if __name__=='__main__': main()
