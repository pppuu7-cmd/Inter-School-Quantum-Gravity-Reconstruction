#!/usr/bin/env python3
"""Audit whether the official Eq.(29) TikZ graphic geometrically assigns labels unambiguously.

This is a source-graphic authority test, not an amplitude evaluator.  A PASS may
qualify graphical label association; it does not by itself supply representation
orientation conventions absent from the source equations/text.
"""
from pathlib import Path
import argparse, hashlib, json, math, re

PHRASE='Before we discuss the behaviour of the EPRL model under coarse graining'
REQUIRED=('J^+','J^-','j','l_1','l_2')

def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def ln(t,p): return t.count('\n',0,p)+1

def parse_xy(s):
    a,b=[x.strip() for x in s.split(',',1)]; return (float(a),float(b))
def d2(a,b): return (a[0]-b[0])**2+(a[1]-b[1])**2

def line_dist(p,a,b):
    vx,vy=b[0]-a[0],b[1]-a[1]; den=vx*vx+vy*vy
    if den==0: return math.sqrt(d2(p,a))
    t=max(0,min(1,((p[0]-a[0])*vx+(p[1]-a[1])*vy)/den))
    q=(a[0]+t*vx,a[1]+t*vy); return math.sqrt(d2(p,q))

def normang(x): return x%360.0
def in_sweep(theta,a,b):
    # TikZ uses the directed angular interval from a to b; sample-free membership.
    theta,a,b=map(normang,(theta,a,b))
    delta=(b-a)%360.0
    return ((theta-a)%360.0) <= delta+1e-10

def arc_geom(start,spec):
    vals=[float(x.strip()) for x in spec.split(':')]
    if len(vals)!=3: raise ValueError(spec)
    a,b,r=vals
    center=(start[0]-r*math.cos(math.radians(a)),start[1]-r*math.sin(math.radians(a)))
    end=(center[0]+r*math.cos(math.radians(b)),center[1]+r*math.sin(math.radians(b)))
    return a,b,r,center,end

def arc_dist(p,arc):
    a,b,r,c,s,e=arc
    th=math.degrees(math.atan2(p[1]-c[1],p[0]-c[0]))
    radial=abs(math.sqrt(d2(p,c))-r)
    return radial if in_sweep(th,a,b) else min(math.sqrt(d2(p,s)),math.sqrt(d2(p,e)))

def find_env(root):
    for p in root.rglob('*.tex'):
        text=p.read_text(errors='ignore'); q=text.lower().find(PHRASE.lower())
        if q<0: continue
        b='\\begin{tikzpicture}'; e='\\end{tikzpicture}'; cand=[]; z=0
        while True:
            i=text.find(b,z)
            if i<0: break
            j=text.find(e,i)
            if j<0: break
            j+=len(e); dist=abs(ln(text,i)-ln(text,q))
            if dist<=80: cand.append((dist,i,j,text[i:j]))
            z=j
        if cand:
            _,i,j,env=min(cand,key=lambda x:x[0]); return p,text,q,i,j,env
    raise RuntimeError('source environment not found')

def tokenize(env):
    body='\n'.join(re.sub(r'(?<!\\)%.*$','',x) for x in env.splitlines())
    rx=re.compile(r'(?P<node>node\s*(?:\[[^\]]*\])?\s*\{[^{}]*\})|(?P<arc>arc\s*(?:\[[^\]]*\])?\s*\([^()]*\))|(?P<coord>\([^()]{1,100}\))|(?P<line>--)',re.S)
    out=[]
    for m in rx.finditer(body):
        k=m.lastgroup; raw=m.group(0); x={'kind':k}
        if k=='coord': x['coord']=raw[1:-1].strip()
        elif k=='arc': x['spec']=re.search(r'\(([^()]*)\)',raw,re.S).group(1).strip()
        elif k=='node': x['label']=' '.join(re.search(r'\{([^{}]*)\}',raw,re.S).group(1).replace('$','').split())
        out.append(x)
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--digits',type=int,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    root=Path(a.source_dir); p,text,q,i,j,env=find_env(root); toks=tokenize(env)
    prim=[]; labels=[]; cur=None; pending=None; last_coord=None
    for t in toks:
        if t['kind']=='coord':
            xy=tuple(round(v,a.digits) for v in parse_xy(t['coord'])); last_coord=xy
            if pending=='line' and cur is not None:
                prim.append({'kind':'line','a':cur,'b':xy}); cur=xy; pending=None
            else: cur=xy
        elif t['kind']=='line': pending='line'
        elif t['kind']=='arc':
            if cur is None: raise RuntimeError('arc without current point')
            aa,bb,r,c,end=arc_geom(cur,t['spec']); c=tuple(round(v,a.digits) for v in c); end=tuple(round(v,a.digits) for v in end)
            prim.append({'kind':'arc','a0':aa,'a1':bb,'r':r,'center':c,'start':cur,'end':end}); cur=end; pending=None
        elif t['kind']=='node':
            if last_coord is None: raise RuntimeError('node without position')
            labels.append({'label':t['label'],'position':last_coord})
    assigns=[]
    for L in labels:
        ds=[]
        for idx,g in enumerate(prim):
            if g['kind']=='line': d=line_dist(L['position'],g['a'],g['b'])
            else: d=arc_dist(L['position'],(g['a0'],g['a1'],g['r'],g['center'],g['start'],g['end']))
            ds.append((d,idx,g['kind']))
        ds.sort(); d0,i0,k0=ds[0]; d1=ds[1][0]
        assigns.append({'label':L['label'],'position':L['position'],'nearest_primitive':i0,'nearest_kind':k0,
                        'nearest_distance':d0,'second_distance':d1,'gap':d1-d0,'ratio':d1/max(d0,1e-12)})
    req=all(any(r in x['label'] for x in labels) for r in REQUIRED)
    margins=all(x['gap']>=0.05 and x['ratio']>=1.20 for x in assigns)
    out={'test':'RC006_EQ29_LABEL_GEOMETRY_AUTHORITY','digits':a.digits,'source':'official arXiv 1609.02429 source archive',
         'tex_path':str(p.relative_to(root)),'tex_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
         'environment_sha256':sha(env),'primitive_count':len(prim),'arc_count':sum(x['kind']=='arc' for x in prim),
         'label_count':len(labels),'required_labels_pass':req,'frozen_margin_threshold':{'absolute_gap':0.05,'ratio':1.20},
         'label_margin_pass':margins,'lane_pass':req and len(prim)>=10 and sum(x['kind']=='arc' for x in prim)>=2 and margins,
         'assignments':assigns,
         'claim_lock':'Graphical label-association audit only; no Eq.(29) amplitude, missing orientation convention, or BRIDGE_DERIVED claim is implied.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='assignments'},indent=2,sort_keys=True))
    if not out['lane_pass']: raise SystemExit(2)
if __name__=='__main__': main()
