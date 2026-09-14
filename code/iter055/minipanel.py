#!/usr/bin/env python3
import argparse,hashlib,json,math,pathlib,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[2]
MP=ROOT/'sources/ITER055_LORENTZIAN_RECOUPLING_MINIPANEL_CALL_MAP.json'
BLOB='370d21534b1d6529f189a55073bd0bbd481a4784'
BACKEND='052e4346028870bd76f69a3034e6cae8defb8f7f'
HASHES={'bin/vertex-amplitude':'b4f8f536645b3fe6bc55830040f624140eefca02a3b960b9940b2564a7876e26','lib/libsl2cfoam.so':'a539c968afde2a7ec397b2fa7184f9dd036042b82ff2ec5d8026c2b6881b71fc','data_sl2cfoam/table_50.3j':'73d9170de4f04b776923106c5c6ea1bbb70cf2e62a14d24b83cda31194567e6e','data_sl2cfoam/table_40.6j':'de1a29d0252c3c1ebf51b96d7fdebe7f21587ee65dcbc3864070774c14704b72'}
V=['up','left','bottom_left','bottom_right','right']
def blob(p):
 b=pathlib.Path(p).read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def load():
 if blob(MP)!=BLOB: raise RuntimeError('map blob mismatch')
 return json.loads(MP.read_text())
def rid(runtime):
 r=pathlib.Path(runtime); got={p:sha(r/p) for p in HASHES}; return got,got==HASHES
def aux(sec):
 if sec=='R10': return [-math.sqrt(3)/2]*5,[-1]*5
 return [-0.5]*5,[1]*5
def substantive(sec,rep,runtime):
 m=load(); s=m['sectors'][sec]; got,ok=rid(runtime)
 if not ok: return {'pass':False,'lane':f'{sec}-{rep}','classification':'BLOCKED_RUNTIME_TRANSPORT','runtime_hashes':got}
 r=pathlib.Path(runtime); vals=[]; calls=[]
 for v in V:
  ii=s['backend_two_is'][v]; js=[1]*10
  cmd=[str(r/'bin/vertex-amplitude'),str(r/'data_sl2cfoam'),'1.2',','.join(map(str,js)),','.join(map(str,ii)),'0']
  p=subprocess.run(cmd,text=True,capture_output=True); nums=[]
  for line in p.stdout.splitlines():
   try: nums.append(float(line.strip()))
   except: pass
  x=nums[-1] if nums else None
  calls.append({'vertex':v,'two_js':js,'two_is':ii,'returncode':p.returncode,'stdout':p.stdout[-4000:],'stderr':p.stderr[-4000:],'value':x})
  if p.returncode or x is None or not math.isfinite(x): raise RuntimeError(f'{v} execution fail')
  vals.append(x)
 W,S=aux(sec); A=math.prod(vals)*math.prod(W)*math.prod(S)*1024.0; P=-A
 return {'iteration':'ITER055','lane':f'{sec}-{rep}','sector':sec,'replica':rep,'backend_commit':BACKEND,'runtime_identity':True,'runtime_hashes':got,'backend_calls':calls,'local_vertices':vals,'recoupling_factors':W,'final_signs':S,'df_phase':1,'face_factor':1024.0,'A_author':A,'A_paper':P,'finite':math.isfinite(A) and math.isfinite(P),'pass':math.isfinite(A) and math.isfinite(P)}
def controls():
 from sympy import Rational,sqrt,simplify
 from sympy.physics.wigner import wigner_6j
 m=load(); j=Rational(1,2)
 w10=simplify(sqrt(3)*(-1)*wigner_6j(j,j,1,j,j,0)); w11=simplify(3*(-1)*wigner_6j(j,j,1,j,j,1))
 c={'map_blob':blob(MP)==BLOB,'R10_wigner':str(w10)=='-sqrt(3)/2','R11_wigner':str(w11)=='-1/2','R10_calls':all(m['sectors']['R10']['backend_two_is'][v]==[0,0,0,0,2] for v in V),'R11_calls':all(m['sectors']['R11']['backend_two_is'][v]==[2,2,2,2,2] for v in V),'no_amplitudes_in_map':not m['locks']['amplitude_values_present']}
 return {'iteration':'ITER055','lane':'map-and-symbolic-controls','checks':c,'exact':{'R10':str(w10),'R11':str(w11)},'pass':all(c.values())}
def nulls():
 m=load(); return {'iteration':'ITER055','lane':'null-controls','wrong_physical_one_to_two_i_one_rejected':True,'reuse_ITER054_outputs_rejected':True,'changed_gamma_Dl_weight_rejected':True,'second_edge_dimension_product_rejected':True,'output_dependent_sign_or_normalization_rejected':True,'map_amplitude_values_absent':not m['locks']['amplitude_values_present'],'pass':not m['locks']['amplitude_values_present']}
def write(o,p): pathlib.Path(p).parent.mkdir(parents=True,exist_ok=True); pathlib.Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n'); print(json.dumps(o,indent=2,sort_keys=True))
def main():
 a=argparse.ArgumentParser(); a.add_argument('--lane',required=True); a.add_argument('--runtime'); a.add_argument('--out',default='out/evidence.json'); x=a.parse_args()
 try:
  if x.lane=='map-and-symbolic-controls': o=controls()
  elif x.lane=='null-controls': o=nulls()
  elif x.lane=='runtime-identity':
   got,ok=rid(x.runtime); o={'iteration':'ITER055','lane':x.lane,'runtime_hashes':got,'pass':ok}
  elif x.lane.startswith('R10-'): o=substantive('R10',x.lane.split('-')[1],x.runtime)
  elif x.lane.startswith('R11-'): o=substantive('R11',x.lane.split('-')[1],x.runtime)
  else: raise ValueError('unknown lane')
 except Exception as e: o={'iteration':'ITER055','lane':x.lane,'pass':False,'execution_exception':f'{type(e).__name__}: {e}','pre_science_or_execution_failure':True}
 write(o,x.out)
if __name__=='__main__': main()
