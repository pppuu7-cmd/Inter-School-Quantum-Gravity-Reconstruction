#!/usr/bin/env python3
"""Source-native TikZ inline-node attachment audit for RC006 Eq.(29).

Unlike the rejected geometry-nearest heuristic, TikZ nodes occurring inside a
path are syntactically attached to that path position. This audit reconstructs
those attachments from official source and checks invariance under lexical
normalizations. It still does not infer missing representation orientations.
"""
from pathlib import Path
import argparse,hashlib,json,re

PHRASE='Before we discuss the behaviour of the EPRL model under coarse graining'
REQ=('J^+','J^-','j','l_1','l_2')
def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def ln(t,p): return t.count('\n',0,p)+1
def clean(x): return ' '.join(x.replace('$','').split())

def find_env(root):
    for p in root.rglob('*.tex'):
        t=p.read_text(errors='ignore'); q=t.lower().find(PHRASE.lower())
        if q<0: continue
        b='\\begin{tikzpicture}';e='\\end{tikzpicture}'; cand=[];z=0
        while 1:
            i=t.find(b,z)
            if i<0: break
            j=t.find(e,i)
            if j<0: break
            j+=len(e); cand.append((abs(ln(t,i)-ln(t,q)),i,j,t[i:j])); z=j
        if cand:
            _,i,j,env=min(cand,key=lambda x:x[0]); return p,t,q,env
    raise RuntimeError('not found')

def normalize(s,mode):
    s='\n'.join(re.sub(r'(?<!\\)%.*$','',x) for x in s.splitlines())
    if mode=='raw': return s
    if mode=='trim': return '\n'.join(x.strip() for x in s.splitlines())
    if mode=='spaces': return re.sub(r'[ \t]+',' ',s)
    if mode=='lines': return re.sub(r'\s*\n\s*',' ',s)
    raise ValueError(mode)

def chunks(env):
    # Semicolon delimits complete TikZ paths in this source environment.
    return [x for x in env.split(';') if re.search(r'\\(?:draw|path)\b',x)]

def parse(chunk):
    rx=re.compile(r'(?P<coord>\([^()]{1,100}\))|(?P<node>node\s*(?:\[[^\]]*\])?\s*\{[^{}]*\})|(?P<arc>arc\s*(?:\[[^\]]*\])?\s*\([^()]*\))|(?P<line>--)|(?P<vh>\|-)|(?P<hv>-\|)|(?P<to>\bto\b(?:\s*\[[^\]]*\])?)|(?P<controls>\.\.\s*controls\s*[^.]{0,160}?\.\.)',re.S)
    toks=[]
    for m in rx.finditer(chunk):
        d={'kind':m.lastgroup}
        if m.lastgroup=='coord': d['value']=clean(m.group(0)[1:-1])
        elif m.lastgroup=='node': d['label']=clean(re.search(r'\{([^{}]*)\}',m.group(0),re.S).group(1))
        elif m.lastgroup=='arc': d['value']=clean(m.group(0))
        toks.append(d)
    return toks

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source-dir',required=True);ap.add_argument('--mode',required=True,choices=['raw','trim','spaces','lines']);ap.add_argument('--output',required=True);a=ap.parse_args()
    root=Path(a.source_dir);p,t,q,env=find_env(root); body=normalize(env,a.mode)
    attachments=[]; path_index=0
    for ch in chunks(body):
        ts=parse(ch); primitive=-1; current_coord=None
        for idx,x in enumerate(ts):
            if x['kind']=='coord': current_coord=x['value']
            elif x['kind'] in {'line','vh','hv','to','controls','arc'}: primitive+=1
            elif x['kind']=='node':
                attachments.append({'path':path_index,'token_index':idx,'label':x['label'],'attached_after_primitive':primitive,'current_coordinate':current_coord})
        path_index+=1
    labels=[x['label'] for x in attachments]
    required=all(any(r in x for x in labels) for r in REQ)
    # Every label must be syntactically inside a path and attached after at least one path primitive.
    attached=bool(attachments) and all(x['attached_after_primitive']>=0 for x in attachments)
    signature=sha(json.dumps(attachments,sort_keys=True,separators=(',',':')))
    out={'test':'RC006_EQ29_INLINE_NODE_ATTACHMENT','mode':a.mode,'source':'official arXiv 1609.02429 source archive','tex_path':str(p.relative_to(root)),'tex_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'environment_sha256':sha(env),'path_count':path_index,'attachment_count':len(attachments),'required_labels_pass':required,'all_nodes_path_attached_pass':attached,'attachment_signature':signature,'attachments':attachments,'lane_pass':required and attached,'claim_lock':'TikZ grammar attachment only; no Eq29 amplitude or unstated orientation convention is inferred.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='attachments'},indent=2,sort_keys=True))
    if not out['lane_pass']: raise SystemExit(2)
if __name__=='__main__':main()
