#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, re

ROOT_SHA='27e781f9ae9b36056a57b7747dc3c58b5b9c944dd0214041149843d8434e16c1'
EQ_HASH={
 'DVD2':'799f56dc22f55a09bf744d62c459ee95e38794e5be02c114a73d06c057d0e94c',
 'DVD3':'7d2fb958574c76f67e52d32ffea2cb22beb01c1e7d6583d383fce159b2eadfab'
}
TITLE=re.compile(r'\\title\{([^}]*)\}',re.S)

def root(src):
    rr=[]
    for f in Path(src).rglob('*.tex'):
        t=f.read_text(errors='ignore')
        if '\\documentclass' in t and '\\begin{document}' in t:
            mt=TITLE.search(t); title=re.sub(r'\s+',' ',mt.group(1)).strip() if mt else ''
            if re.search(r'Lorentzian',title,re.I) and re.search(r'Spin.?Foam',title,re.I): rr.append((f,t,title))
    return rr[0] if len(rr)==1 else (None,None,None)

def equation(t,label):
    lm=re.search(r'\\label\{'+re.escape(label)+r'\}',t)
    if not lm: return None
    starts=[m for m in re.finditer(r'\\begin\{equation\}',t[:lm.start()])]
    if not starts: return None
    s=starts[-1].start(); em=re.search(r'\\end\{equation\}',t[lm.end():])
    if not em: return None
    return t[s:lm.end()+em.end()]

def label_context(t,label,radius=900):
    lm=re.search(r'\\label\{'+re.escape(label)+r'\}',t or '')
    if not lm: return ''
    return (t or '')[max(0,lm.start()-radius):min(len(t or ''),lm.end()+radius)]

def h(raw): return hashlib.sha256(re.sub(r'\s+','',raw).encode()).hexdigest() if raw else None

def factors(raw):
    out=[]
    for gm in re.finditer(r'\\includegraphics(?:\[[^\]]*\])?\{_images/B4\.eps\}',raw or ''):
        starts=[m for m in re.finditer(r'\\begin\{array\}\{c\}',(raw or '')[:gm.start()])]
        if not starts: continue
        s=starts[-1].start(); em=re.search(r'\\end\{array\}',(raw or '')[gm.end():])
        if not em: continue
        chunk=(raw or '')[s:gm.end()+em.end()]
        mp={k:v.strip() for k,v in re.findall(r'\\psfrag\{([^}]+)\}\{\$([^$]+)\$\}',chunk)}
        out.append({'j':[mp.get(x) for x in 'abcd'],'l':[mp.get(x) for x in 'efgh'],'i':mp.get('i'),'k':mp.get('k')})
    return out

def compact(s): return re.sub(r'\s+','',s or '')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    f,t,title=root(a.source_dir)
    rsha=hashlib.sha256(t.encode()).hexdigest() if t else None
    raw2=equation(t,'DVD2') if t else None; raw3=equation(t,'DVD3') if t else None
    hashes={'DVD2':h(raw2),'DVD3':h(raw3)}
    fs2=factors(raw2); fs3=factors(raw3)
    expected2=[
      {'j':['j_1','j_2','j_3','j_4'],'l':['j_1','j_2','j_3','l_4'],'i':'t','k':"t'"},
      {'j':['j_1','j_2','j_3','j_4'],'l':['l_1','l_2','l_3','l_4'],'i':'i','k':"k'"},
      {'j':["j'_1","j'_2","j'_3","j'_4"],'l':["j'_1",'l_3','l_2','l_1'],'i':"i'",'k':"k'"}
    ]
    expected3=[
      {'j':['j_1','j_2','j_3','j_4'],'l':['j_1','j_2','l_3','l_4'],'i':'t','k':"t'"},
      {'j':['j_1','j_2','j_3','j_4'],'l':['l_1','l_2','l_3','l_4'],'i':'i','k':"t'"},
      {'j':["j'_1","j'_2","j'_3","j'_4"],'l':["j'_1","j'_2",'l_2','l_1'],'i':"i'",'k':"t'"}
    ]
    c2=compact(raw2); c3=compact(raw3); gctx=compact(label_context(t,'giorgio'))
    dvd2_tokens=[r"\sum_{k',l_a}","dk'",r"(-1)^{2(k'+t')}",r"\frac{\delta_{j'_3,l_4}}{d_{j'_3}}",r"\delta_{j_1,j'_1}",r"\delta_{j_2,j'_2}",r"\delta_{j_3,j'_3}"]
    dvd3_tokens=[r"\sum_{l_a}",r"\delta_{j_1,j'_1}",r"\delta_{j_2,j'_2}"]
    dvd2_token_status={x:(x in c2) for x in dvd2_tokens}; dvd3_token_status={x:(x in c3) for x in dvd3_tokens}
    # Exact source spelling uses the author macro \Deltal and, literally, j+\Deltal as the second upper bound.
    shell_tokens=[r'\label{giorgio}',r'C_{\Deltal}(j,j\')',r'\sum_{l=j}^{j+\Deltal}',r"\sum_{l'=j'}^{j+\Deltal}"]
    # The apostrophe token is awkward in a Python raw literal; replace the C token with a direct compact substring check below.
    shell_token_status={
      r'\label{giorgio}': r'\label{giorgio}' in gctx,
      r'C_{\Deltal}(j,j_prime)': r"C_{\Deltal}(j,j')" in gctx,
      r'\sum_{l=j}^{j+\Deltal}': r'\sum_{l=j}^{j+\Deltal}' in gctx,
      r"\sum_{l'=j'}^{j+\Deltal}": r"\sum_{l'=j'}^{j+\Deltal}" in gctx
    }
    token2=all(dvd2_token_status.values()); token3=all(dvd3_token_status.values()); shell_pattern=all(shell_token_status.values())
    ok=bool(rsha==ROOT_SHA and hashes==EQ_HASH and fs2==expected2 and fs3==expected3 and token2 and token3 and shell_pattern)
    out={
      'test':'LORENTZIAN_EPRL_DVD_MULTISHELL_SOURCE_MANIFEST','root_path':str(f) if f else None,'root_title':title,'root_sha256':rsha,
      'equation_hashes':hashes,'expected_equation_hashes':EQ_HASH,'dvd2_factor_mapping':fs2,'dvd3_factor_mapping':fs3,
      'dvd2_source_tokens_pass':token2,'dvd3_source_tokens_pass':token3,'dvd2_token_status':dvd2_token_status,'dvd3_token_status':dvd3_token_status,
      'same_paper_shell_pattern_pass':shell_pattern,'shell_token_status_context':shell_token_status,
      'source_literal_shell_formula':r"C_{\Deltal}(j,j')=\sum_{l=j}^{j+\Deltal}\sum_{l'=j'}^{j+\Deltal}C_{l,l'}(j,j')",
      'regulator_statement':"Finite DVD shell cutoff is a numerical regulator modeled on this same-paper shell pattern. On the frozen j=j'=1 boundary the literal second upper bound j+Delta_l equals j'+Delta_l. It is not asserted to be the source definition of a finite DVD sum.",
      'gate_pass':ok,'classification':'DVD_MULTISHELL_SOURCE_MANIFEST_PASS' if ok else 'DVD_MULTISHELL_SOURCE_MANIFEST_FAIL',
      'claim_lock':'Source authority and regulator provenance only. No numerical amplitude, refinement, continuum, bridge, or novelty claim.'
    }
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
    if not ok: raise SystemExit(2)
if __name__=='__main__': main()
