#!/usr/bin/env python3
"""Exact normalized source-equation snapshots needed for executable RC008 reconstruction.

Artifacts are implementation inputs. They are not scientific results and do not
count as amplitude/refinement evidence.
"""
from pathlib import Path
import argparse,hashlib,json,re

def sha(s):return hashlib.sha256(s.encode()).hexdigest()
def locate(text,label):
    pos=text.find('\\label{'+label+'}')
    if pos<0:return None
    begins=list(re.finditer(r'\\begin\{(equation\*?|align\*?|alignat\*?|eqnarray\*?|multline\*?|gather\*?)\}',text[:pos],re.S))
    if begins:
        b=begins[-1]; env=b.group(1); end=re.search(r'\\end\{'+re.escape(env)+r'\}',text[pos:],re.S)
        if end:return b.start(),pos+end.end()
    l=text.rfind('\\[',0,pos); r=text.find('\\]',pos)
    if l>=0 and r>=0:return l,r+2
    return max(0,pos-1200),min(len(text),pos+1200)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source-dir',required=True);ap.add_argument('--label',required=True);ap.add_argument('--output',required=True);a=ap.parse_args();root=Path(a.source_dir)
    rec=None
    for p in root.rglob('*.tex'):
        t=p.read_text(errors='ignore');loc=locate(t,a.label)
        if not loc:continue
        s,e=loc; body=t[s:e]
        # Remove comments and normalize whitespace while preserving TeX semantics.
        clean='\n'.join(re.sub(r'(?<!\\)%.*$','',x) for x in body.splitlines())
        clean=' '.join(clean.split())
        rec={'label':a.label,'path':str(p.relative_to(root)),'file_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'equation_sha256':sha(clean),'normalized_tex':clean,'references':sorted(set(re.findall(r'\\(?:eqref|ref)\{([^{}]+)\}',clean)))};break
    ok=rec is not None and ('\\label{'+a.label+'}') in rec['normalized_tex']
    out={'test':'RC008_SOURCE_EQUATION_SNAPSHOT','label':a.label,'record':rec,'frozen_gate_pass':ok,'claim_lock':'Implementation input only; no amplitude/refinement evidence.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'label':a.label,'found':rec is not None,'frozen_gate_pass':ok,'equation_sha256':rec['equation_sha256'] if rec else None},indent=2))
    if not ok:raise SystemExit(2)
if __name__=='__main__':main()
