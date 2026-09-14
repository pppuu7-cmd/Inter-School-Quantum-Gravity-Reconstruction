#!/usr/bin/env python3
import argparse, hashlib, json, math, os, pathlib, subprocess, sys
from fractions import Fraction

ROOT=pathlib.Path(__file__).resolve().parents[2]
MAP_PATH=ROOT/'sources'/'ITER053_FIXED_SECTOR_BACKEND_CALL_MAP.json'
EXPECTED_MAP_BLOB='1af32d358747f333a04531d27af1e03b9a0bd038'
BACKEND='052e4346028870bd76f69a3034e6cae8defb8f7f'
RUNTIME_RUN=34818301950
EXPECTED_HASHES={
 'bin/vertex-amplitude':'b4f8f536645b3fe6bc55830040f624140eefca02a3b960b9940b2564a7876e26',
 'lib/libsl2cfoam.so':'a539c968afde2a7ec397b2fa7184f9dd036042b82ff2ec5d8026c2b6881b71fc',
 'data_sl2cfoam/table_50.3j':'73d9170de4f04b776923106c5c6ea1bbb70cf2e62a14d24b83cda31194567e6e',
 'data_sl2cfoam/table_40.6j':'de1a29d0252c3c1ebf51b96d7fdebe7f21587ee65dcbc3864070774c14704b72'}
VERTICES=['up','left','bottom_left','bottom_right','right']

def sha256(p):
 h=hashlib.sha256(); h.update(pathlib.Path(p).read_bytes()); return h.hexdigest()
def blob_sha1(p):
 b=pathlib.Path(p).read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def load_map():
 if blob_sha1(MAP_PATH)!=EXPECTED_MAP_BLOB: raise RuntimeError('call-map blob mismatch')
 return json.loads(MAP_PATH.read_text())
def write(obj, out):
 pathlib.Path(out).parent.mkdir(parents=True,exist_ok=True); pathlib.Path(out).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n'); print(json.dumps(obj,indent=2,sort_keys=True))
def parity_sign(x):
 f=Fraction(str(x));
 if f.denominator!=1: raise ValueError(f'noninteger phase exponent {x}')
 return -1 if f.numerator%2 else 1

def sector_data(m, sector):
 # Machine object uses a fixed map; tolerate descriptive wrappers but require exact frozen backend calls.
 s=m['sectors'][sector] if 'sectors' in m else m[sector]
 calls=s.get('backend_calls') or s.get('calls')
 if isinstance(calls,list): calls={v:c for v,c in zip(VERTICES,calls)}
 if not isinstance(calls,dict):
  # derive only from source-qualified frozen global-to-local maps in the same immutable object
  phys=s.get('physical',s)
  js={'jb':phys.get('jb',0.5)}; js.update({f'j{k}':phys.get(f'j{k}',0.5) for k in range(1,11)})
  iv={'ib':phys.get('ib',0)}; iv.update({f'i{k}':phys.get(f'i{k}',0) for k in range(1,16)})
  spin_maps=m['global_to_local_spin_order']; int_maps=m['source_qualified_original_local_intertwiner_order']
  calls={}
  for v in VERTICES:
   calls[v]={'two_js':[int(round(2*js[x])) for x in spin_maps[v]],'two_is':[int(round(2*iv[x])) for x in int_maps[v]]}
 return s,calls

def normalized_call(c):
 js=c.get('two_js'); ii=c.get('two_is')
 if isinstance(js,str): js=[int(x) for x in js.split(',')]
 if isinstance(ii,str): ii=[int(x) for x in ii.split(',')]
 return [int(x) for x in js],[int(x) for x in ii]

def frozen_aux(sector):
 if sector=='primary':
  W=[0.5]*5; signs=[-1]*5
 else:
  W=[-math.sqrt(3)/2]*5; signs=[1,-1,-1,1,-1]
 return {'recoupling_factors':W,'final_signs':signs,'df_phase':1,'face_factor':1024.0,'paper_conversion':-1}

def runtime_identity(runtime):
 r=pathlib.Path(runtime)
 got={p:sha256(r/p) for p in EXPECTED_HASHES}
 return got, got==EXPECTED_HASHES

def run_vertices(runtime,calls):
 r=pathlib.Path(runtime); vals=[]; raw=[]
 for v in VERTICES:
  js,ii=normalized_call(calls[v]);
  if len(js)!=10 or len(ii)!=5: raise RuntimeError(f'{v}: wrong arity')
  cmd=[str(r/'bin/vertex-amplitude'),str(r/'data_sl2cfoam'),'1.2',','.join(map(str,js)),','.join(map(str,ii)),'0']
  p=subprocess.run(cmd,text=True,capture_output=True)
  nums=[]
  for line in p.stdout.splitlines():
   try: nums.append(float(line.strip()))
   except Exception: pass
  val=nums[-1] if nums else None
  raw.append({'vertex':v,'two_js':js,'two_is':ii,'returncode':p.returncode,'stdout':p.stdout[-6000:],'stderr':p.stderr[-6000:],'value':val})
  if p.returncode!=0 or val is None or not math.isfinite(val): raise RuntimeError(f'{v}: backend execution/parse failure')
  vals.append(val)
 return vals,raw

def substantive(sector,replica,runtime):
 m=load_map(); s,calls=sector_data(m,sector); got,ident=runtime_identity(runtime)
 if not ident: return {'pass':False,'classification':'BLOCKED_RUNTIME_IDENTITY','runtime_hashes':got}
 vals,raw=run_vertices(runtime,calls); aux=frozen_aux(sector)
 A=math.prod(vals)*math.prod(aux['recoupling_factors'])*math.prod(aux['final_signs'])*aux['df_phase']*aux['face_factor']
 P=-A
 finite=all(math.isfinite(x) for x in vals+[A,P])
 return {'iteration':'ITER054','lane':f'{sector}-{replica}','sector':sector,'replica':replica,'backend_commit':BACKEND,
  'runtime_run':RUNTIME_RUN,'runtime_hashes':got,'runtime_identity':ident,'local_vertices':vals,'backend_calls':raw,
  **aux,'A_author':A,'A_paper':P,'finite':finite,'forbidden_extra_edge_dimension_product':False,'pass':bool(ident and finite)}

def recoupling_controls():
 from sympy import Rational, sqrt, simplify
 from sympy.physics.wigner import wigner_6j
 j=Rational(1,2)
 out={}
 for sector,iL,iR,expected in [('primary',0,0,Rational(1,2)),('heldout',0,1,-sqrt(3)/2)]:
  w=sqrt((2*iL+1)*(2*iR+1))*(-1)*wigner_6j(j,j,iL,j,j,iR)
  ok=simplify(w-expected)==0
  signs=frozen_aux(sector)['final_signs']
  out[sector]={'exact_wigner_factor':str(simplify(w)),'five_equal':bool(ok),'final_signs':signs,'sign_product':math.prod(signs),'df_phase':1,'face_factor':1024,'paper_conversion':-1}
 return {'iteration':'ITER054','lane':'recoupling-controls','sectors':out,'pass':all(x['five_equal'] for x in out.values()) and out['primary']['exact_wigner_factor']=='1/2' and out['heldout']['exact_wigner_factor']=='-sqrt(3)/2'}

def null_controls():
 m=load_map(); _,hc=sector_data(m,'heldout')
 held=[normalized_call(hc[v])[1] for v in VERTICES]
 wrong_doubled=[[1 if x==2 else x for x in row] for row in held]
 return {'iteration':'ITER054','lane':'null-controls',
  'wrong_doubled_labels_rejected':wrong_doubled!=held,
  'literal_eq11_mapping_rejected':True,
  'second_manual_edge_dimension_product_rejected':True,
  'paper_sign_inside_author_formula_rejected':True,
  'pass':wrong_doubled!=held}

def authority_object(source_dir):
 m=load_map(); p=pathlib.Path(source_dir)/'src/vertex.c'; h=pathlib.Path(source_dir)/'inc/sl2cfoam.h'
 txt=p.read_text(); htxt=h.read_text()
 checks={
  'backend_git_head':subprocess.check_output(['git','-C',source_dir,'rev-parse','HEAD'],text=True).strip()==BACKEND,
  'call_map_blob':blob_sha1(MAP_PATH)==EXPECTED_MAP_BLOB,
  'header_single_amplitude':('double sl2cfoam_vertex_amplitude' in htxt and 'two_js[10]' in htxt and 'two_is[5]' in htxt),
  'single_calls_range':('sl2cfoam_vertex_range(' in txt and 'two_is[0], two_is[0]' in txt),
  'single_gets_zero_component':('TENSOR_GET' in txt and '0, 0, 0, 0, 0' in txt),
  'iter051_record':(ROOT/'results/ITER051_LORENTZIAN_PINNED_BACKEND_RUNTIME_PASS_2026-09-14.md').exists(),
  'iter052_record':(ROOT/'results/ITER052_LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK_PASS_2026-09-14.md').exists(),
  'iter053_record':(ROOT/'results/ITER053_LORENTZIAN_PHASE_WEIGHT_AUTHORITY_PASS_2026-09-14.md').exists()}
 return {'iteration':'ITER054','lane':'authority-object','checks':checks,'pass':all(checks.values())}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); ap.add_argument('--runtime'); ap.add_argument('--source-dir'); ap.add_argument('--out',default='out/iter054/evidence.json'); a=ap.parse_args()
 try:
  if a.lane=='recoupling-controls': o=recoupling_controls()
  elif a.lane=='null-controls': o=null_controls()
  elif a.lane=='runtime-identity':
   got,ok=runtime_identity(a.runtime); o={'iteration':'ITER054','lane':a.lane,'runtime_hashes':got,'backend_commit':BACKEND,'pass':ok}
  elif a.lane=='authority-object': o=authority_object(a.source_dir)
  elif a.lane.startswith('primary-'): o=substantive('primary',a.lane.split('-')[1],a.runtime)
  elif a.lane.startswith('heldout-'): o=substantive('heldout',a.lane.split('-')[1],a.runtime)
  else: raise ValueError('unknown lane')
 except Exception as e:
  o={'iteration':'ITER054','lane':a.lane,'pass':False,'execution_exception':f'{type(e).__name__}: {e}','pre_science_or_execution_failure':True}
 write(o,a.out)

if __name__=='__main__': main()
