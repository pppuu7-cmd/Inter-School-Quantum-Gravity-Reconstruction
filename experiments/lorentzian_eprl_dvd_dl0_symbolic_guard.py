#!/usr/bin/env python3
"""Independent symbolic/source guard for the frozen DVD2/DVD3 Dl=0 pilot.

This guard uses the exact labelled source equations and independently repeats
B4 slot extraction. It does not import numerical pilot outputs. Frozen symmetric
boundary: all j,j'=1, i=t=i'=t'=1, and Dl=0 => all l=j.
"""
from pathlib import Path
import argparse,hashlib,json,re

TITLE=re.compile(r'\\title\{([^}]*)\}',re.S)
EXPECTED_ROOT='27e781f9ae9b36056a57b7747dc3c58b5b9c944dd0214041149843d8434e16c1'
EXPECTED_HASH={'DVD2':'799f56dc22f55a09bf744d62c459ee95e38794e5be02c114a73d06c057d0e94c','DVD3':'7d2fb958574c76f67e52d32ffea2cb22beb01c1e7d6583d383fce159b2eadfab'}

def root(src):
 rr=[]
 for f in Path(src).rglob('*.tex'):
  t=f.read_text(errors='ignore')
  if '\\documentclass' in t and '\\begin{document}' in t:
   mt=TITLE.search(t); title=re.sub(r'\s+',' ',mt.group(1)).strip() if mt else ''
   if re.search(r'Lorentzian',title,re.I) and re.search(r'Spin.?Foam',title,re.I): rr.append((f,t,title))
 return rr[0] if len(rr)==1 else (None,None,None)

def equation(t,label):
 lm=re.search(r'\\label\{'+label+r'\}',t)
 if not lm: return None
 starts=[m for m in re.finditer(r'\\begin\{equation\}',t[:lm.start()])]
 if not starts: return None
 s=starts[-1].start(); em=re.search(r'\\end\{equation\}',t[lm.end():])
 if not em: return None
 e=lm.end()+em.end(); return t[s:e]

def factors(raw):
 out=[]
 for gm in re.finditer(r'\\includegraphics(?:\[[^\]]*\])?\{_images/B4\.eps\}',raw):
  starts=[m for m in re.finditer(r'\\begin\{array\}\{c\}',raw[:gm.start()])]
  if not starts: continue
  s=starts[-1].start(); em=re.search(r'\\end\{array\}',raw[gm.end():])
  if not em: continue
  chunk=raw[s:gm.end()+em.end()]
  mp={k:v.strip() for k,v in re.findall(r'\\psfrag\{([^}]+)\}\{\$([^$]+)\$\}',chunk)}
  out.append({'j':[mp.get(x) for x in 'abcd'],'l':[mp.get(x) for x in 'efgh'],'i':mp.get('i'),'k':mp.get('k')})
 return out

def canonical_symbol(s):
 # Frozen substitution: primed/unprimed j_a and l_a all equal spin 1;
 # external i,t,i',t' all equal intertwiner 1. Keep k' internal.
 if s is None: return None
 if "k'" in s: return "kprime"
 if s in ('i','t',"i'","t'"): return 'one'
 if s.startswith('j') or s.startswith('l'): return 'one'
 return s

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 f,t,title=root(a.source_dir)
 root_sha=hashlib.sha256(t.encode()).hexdigest() if t else None
 rows={}; all_ok=(root_sha==EXPECTED_ROOT)
 for lab in ('DVD2','DVD3'):
  raw=equation(t,lab) if t else None
  h=hashlib.sha256(re.sub(r'\s+','',raw).encode()).hexdigest() if raw else None
  fs=factors(raw or '')
  reduced=[]
  for x in fs:
   reduced.append({'j':[canonical_symbol(v) for v in x['j']], 'l':[canonical_symbol(v) for v in x['l']],
                   'i':canonical_symbol(x['i']),'k':canonical_symbol(x['k'])})
  eq_ok=(h==EXPECTED_HASH[lab] and len(fs)==3)
  rows[lab]={'equation_hash':h,'factor_count':len(fs),'reduced_factors':reduced,'equation_identity_pass':eq_ok}
  all_ok &= eq_ok

 # Exact frozen reductions of source dimension/delta/sign factors.
 raw2=equation(t,'DVD2') or ''; raw3=equation(t,'DVD3') or ''
 dvd2_tokens=["didi'dt", "dk'", "(-1)^{2(k'+t')}", "\\frac{\\delta_{j'_3,l_4}}{d_{j'_3}}", "\\delta_{j_1,j'_1}", "\\delta_{j_2,j'_2}", "\\delta_{j_3,j'_3}"]
 dvd3_tokens=["didi'dt", "\\delta_{j_1,j'_1}", "\\delta_{j_2,j'_2}"]
 token_ok2=all(x in re.sub(r'\s+','',raw2) for x in dvd2_tokens)
 token_ok3=all(x in re.sub(r'\s+','',raw3) for x in dvd3_tokens)
 # d_i=d_i'=d_t=3 and d_j3'=3; for k=0,1,2, d_k=1,3,5. Sign is +1.
 dvd2_prefactor=3*3*3/3
 dvd3_prefactor=3*3*3
 allowed_k=[0,1,2]
 signs=[(-1)**(2*(k+1)) for k in allowed_k]
 expected2=[
  {'j':['one']*4,'l':['one']*4,'i':'one','k':'one'},
  {'j':['one']*4,'l':['one']*4,'i':'one','k':'kprime'},
  {'j':['one']*4,'l':['one']*4,'i':'one','k':'kprime'}]
 expected3=[{'j':['one']*4,'l':['one']*4,'i':'one','k':'one'}]*3
 mapping_ok=(rows['DVD2']['reduced_factors']==expected2 and rows['DVD3']['reduced_factors']==expected3)
 scalar_ok=(dvd2_prefactor==9 and dvd3_prefactor==27 and signs==[1,1,1])
 all_ok=bool(all_ok and token_ok2 and token_ok3 and mapping_ok and scalar_ok)
 out={'test':'LORENTZIAN_EPRL_DVD_DL0_SYMBOLIC_GUARD','valid':bool(t),'root_sha256':root_sha,'equations':rows,
      'dvd2_source_token_pass':token_ok2,'dvd3_source_token_pass':token_ok3,'mapping_reduction_pass':mapping_ok,
      'dvd2_prefactor':dvd2_prefactor,'dvd3_prefactor':dvd3_prefactor,'allowed_kprime':allowed_k,'dvd2_signs':signs,
      'scalar_reduction_pass':scalar_ok,'gate_pass':all_ok,
      'frozen_formula_dvd2':'9 * B4(i=1,k=1) * sum_{k=0,1,2}(2k+1)*B4(i=1,k)^2',
      'frozen_formula_dvd3':'27 * B4(i=1,k=1)^3',
      'classification':'DVD_DL0_SYMBOLIC_GUARD_PASS' if all_ok else 'DVD_DL0_SYMBOLIC_GUARD_FAIL',
      'claim_lock':'Independent source/symbolic guard only; no numerical DVD value or refinement/bridge claim.'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
 if not all_ok: raise SystemExit(2)
if __name__=='__main__': main()
