from pathlib import Path
import json,re
ROOT=Path('.')
BASIS=['R','S','DR','DS','BoxR','D2R','BoxS','D2S']
EXCLUDE=('ITER157','recovery/state.json','recovery/CURRENT_FRONT.md','.git/')
text_ext={'.md','.txt','.py','.json','.yml','.yaml','.tex','.csv'}
# Deliberately conservative: candidates only; every candidate is emitted with provenance for adjudication.
pole=re.compile(r'(?i)(1\s*/\s*(?:epsilon|eps)|pole|residue|divergen|counterterm)')
endpoint=re.compile(r'(?i)(endpoint|geodesic|fixed[-_ ]?geodesic)')
explicit=re.compile(r'(=|->|→|:=|coefficient|coeff\b)',re.I)
basis_re={b:re.compile(r'(?<![A-Za-z0-9_])'+re.escape(b)+r'(?![A-Za-z0-9_])') for b in BASIS}
rows=[]
scanned=0
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or p.suffix.lower() not in text_ext: continue
    s=p.as_posix()
    if any(x in s for x in EXCLUDE): continue
    try: lines=p.read_text(errors='ignore').splitlines()
    except Exception: continue
    scanned+=1
    for i,line in enumerate(lines,1):
        if pole.search(line) and endpoint.search(line) and explicit.search(line):
            dirs=[b for b,r in basis_re.items() if r.search(line)]
            if dirs:
                rows.append({'path':s,'line':i,'basis':dirs,'text':line[:1000]})
# Audit is intentionally candidate-generating; scientific adjudication must inspect whether each is a real equation/derivation.
out={'gate':'ITER157','basis':BASIS,'files_scanned':scanned,'candidate_count':len(rows),'candidates':rows,
     'automatic_scientific_pass':False,
     'note':'Candidates require raw provenance adjudication; lexical hit alone is never scientific PASS.'}
Path('compute_results').mkdir(exist_ok=True)
Path('compute_results/iter157_endpoint_tensor_source_audit.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
