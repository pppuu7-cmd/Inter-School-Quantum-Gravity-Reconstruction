#!/usr/bin/env python3
import hashlib, json, re, tarfile, urllib.request, pathlib, io
URL='https://export.arxiv.org/e-print/1706.01891v2'
out=pathlib.Path('artifacts'); out.mkdir(exist_ok=True)
req=urllib.request.Request(URL,headers={'User-Agent':'Mozilla/5.0','Accept':'*/*'})
raw=urllib.request.urlopen(req,timeout=60).read()
sha=hashlib.sha256(raw).hexdigest()
patterns={
'metric_signature':r'signature|mostly plus|mostly minus|Minkowski metric',
'metric_normalization':r'g_{\\mu\\nu}|metric.*kappa|\\kappa.*h_',
'gauge':r'gauge|alpha|beta',
'curvature_convention':r'Riemann|Ricci|R_{\\mu\\nu|R\\^',
'dimensional_regulator':r'dimensional|n ?=|d ?=|epsilon|varepsilon',
'fourier':r'Fourier|momentum space|int.*d\^n.*p',
'geodesic_parameter':r'geodesic|tau|affine',
'endpoint':r'endpoint|initial|boundary|x\\^\\mu|y\\^\\mu',
'renormalization':r'renormal|counterterm|wave.function'
}
inv=[]; hits={k:[] for k in patterns}
with tarfile.open(fileobj=io.BytesIO(raw),mode='r:*') as tf:
  for m in tf.getmembers():
    if not m.isfile() or not m.name.lower().endswith(('.tex','.sty','.bib')): continue
    b=tf.extractfile(m).read(); inv.append({'path':m.name,'sha256':hashlib.sha256(b).hexdigest()})
    if not m.name.lower().endswith('.tex'): continue
    text=b.decode('utf-8','replace'); lines=text.splitlines()
    for key,pat in patterns.items():
      rx=re.compile(pat,re.I)
      for i,line in enumerate(lines):
        if rx.search(line):
          a=max(0,i-2); z=min(len(lines),i+3)
          hits[key].append({'file':m.name,'line':i+1,'excerpt':'\n'.join(lines[a:z])[:1800]})
          if len(hits[key])>=12: break
result={'gate':'ITER159','source':'arXiv:1706.01891v2','url':URL,'archive_sha256':sha,'inventory':inv,'evidence':hits,'automatic_scientific_pass':False,'classification':'PENDING_MANUAL_SOURCE_CONVENTION_ADJUDICATION','claim_locks':{'bridge_derived':False,'new_physics_found':False,'candidate_theory_authorized':False}}
(out/'iter159_frob_convention_evidence.json').write_text(json.dumps(result,indent=2,ensure_ascii=False))
print(json.dumps({'source':result['source'],'archive_sha256':sha,'tex_files':len(inv),'hit_counts':{k:len(v) for k,v in hits.items()},'classification':result['classification']},indent=2))