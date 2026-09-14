#!/usr/bin/env python3
import argparse, json, math, re, time
from pathlib import Path
import numpy as np

MEASURE_TERMS=("faddeev","jacobian","measure","determinant")
TOPO_TERMS=("coarse","fine","embedding","gluing","glued","constraint","geometricity","refinement")
SOURCES={
 "1508.07961":"quantum-cuboid baseline",
 "1605.07649":"hypercuboidal RG letter",
 "1701.02311":"hypercuboidal renormalization detail",
 "1804.00023":"symmetry-restricted coarse/fine extension",
}

def area_with_grad(a,b,c,d):
    # each arg is (value, gradient vector)
    out=[]
    for x,y in [(b,c),(a,b),(a,c),(b,d),(c,d),(a,d)]:
        xv,xg=x; yv,yg=y
        out.append((xv*yv, xg*yv + yg*xv))
    return out

def const(v,n): return (float(v),np.zeros(n))
def var(v,n,i):
    g=np.zeros(n); g[i]=1.0; return (float(v),g)
def sub(x,y): return (x[0]-y[0],x[1]-y[1])

def segments(mode,q):
    q=np.asarray(q,float); n=len(q)
    X,Y,Z,TT=1.7,1.3,0.9,2.2
    if mode=='coarse2':
        t=var(q[0],n,0)
        return [[const(X,n)],[const(Y,n)],[const(Z,n)],[t,sub(const(TT,n),t)]]
    x=var(q[0],n,0); y=var(q[1],n,1); z=var(q[2],n,2)
    t1=var(q[3],n,3); t2=var(q[4],n,4); t3=var(q[5],n,5)
    return [[x,sub(const(X,n),x)],
            [y,sub(const(Y,n),y)],
            [z,sub(const(Z,n),z)],
            [t1,sub(t2,t1),sub(t3,t2),sub(const(TT,n),t3)]]

def embedding(mode,q):
    ss=segments(mode,q); vals=[]; grads=[]; cells=[]
    for ix,a in enumerate(ss[0]):
      for iy,b in enumerate(ss[1]):
       for iz,c in enumerate(ss[2]):
        for it,d in enumerate(ss[3]):
         areas=area_with_grad(a,b,c,d)
         vals.extend(v for v,g in areas); grads.extend(g for v,g in areas)
         cells.append((a[0],b[0],c[0],d[0]))
    return np.asarray(vals),np.asarray(grads),cells

def fd_jac(mode,q,h=1e-6):
    q=np.asarray(q,float); cols=[]
    for i in range(len(q)):
        qp=q.copy(); qm=q.copy(); qp[i]+=h; qm[i]-=h
        fp=embedding(mode,qp)[0]; fm=embedding(mode,qm)[0]
        cols.append((fp-fm)/(2*h))
    return np.stack(cols,axis=1)

def log_fp(a,b,c,d):
    j1=b*c; j2=a*b; j3=a*c; j4=b*d
    term=(j1**4*(j2*j2+j3*j3)*(j2*j2+j4*j4)
          +j3*j3*(j2*j2+j3*j3)*j4*j4*(j2*j2+j4*j4)
          +j1*j1*(j3*j3+j4*j4)*(j2**4+j3*j3*j4*j4))
    costh=(j1*j1*j2*j2)/math.sqrt(term)
    jac=a*b*b*c
    return math.log(jac)-math.log(costh)

def frozen_points(mode):
    if mode=='coarse2':
        return [[0.31],[0.58],[0.91],[1.27],[1.73]]
    return [
      [0.44,0.37,0.29,0.31,0.92,1.61],
      [0.71,0.49,0.34,0.27,1.08,1.74],
      [0.93,0.62,0.51,0.42,1.21,1.89],
      [1.11,0.83,0.41,0.36,0.84,1.53],
      [1.29,0.71,0.58,0.25,1.31,1.96],
    ]

def geometry(mode):
    rows=[]; ok=True
    for q in frozen_points(mode):
        vals,J,cells=embedding(mode,q); Jfd=fd_jac(mode,q)
        denom=np.maximum(1e-12,np.maximum(np.abs(J),np.abs(Jfd)))
        err=float(np.max(np.abs(J-Jfd)/denom))
        rank=int(np.linalg.matrix_rank(J,tol=1e-10))
        G=J.T@J; sign,ld=np.linalg.slogdet(G)
        row={'q':q,'outputs':int(len(vals)),'reduced_dim':int(len(q)),
             'jacobian_relative_error_max':err,'rank':rank,
             'gram_sign':float(sign),'gram_logdet':float(ld)}
        row['pass']=bool(err<=2e-5 and rank==len(q) and sign>0 and np.isfinite(ld))
        ok &= row['pass']; rows.append(row)
    return {'mode':mode,'classification':'DIAGNOSTIC_PASS_GEOMETRIC_PULLBACK' if ok else 'NUMERICAL_OR_IMPLEMENTATION_FAIL',
            'pass':bool(ok),'rows':rows,
            'claim_lock':'geometric embedding pullback diagnostic only; not the physical spin-foam measure; zero bridge credit'}

def cv_from_logs(logs):
    a=np.exp(np.asarray(logs)-np.max(logs)); return float(np.std(a)/np.mean(a))

def sentinel():
    out={}
    for mode in ['coarse2','fine32']:
        logs=[]; rows=[]
        for q in frozen_points(mode):
            _,J,cells=embedding(mode,q); sign,ld=np.linalg.slogdet(J.T@J)
            lp=sum(log_fp(*c) for c in cells)
            lr=lp-0.5*ld
            logs.append(lr); rows.append({'q':q,'log_local_product_over_pullback':float(lr)})
        cv=cv_from_logs(logs)
        out[mode]={'ratio_cv':cv,'nonconstant':bool(cv>1e-2),'rows':rows}
    return {'mode':'sentinel','classification':'ADVERSARIAL_SENTINEL_REJECTS_CONSTANT_LOCAL_PRODUCT_EQUIVALENCE' if all(v['nonconstant'] for v in out.values()) else 'SENTINEL_INCONCLUSIVE',
            'comparisons':out,'claim_lock':'does not determine the correct quantum measure'}

def source_audit(arxiv_id):
    import requests
    from pypdf import PdfReader
    import io
    urls=[f'https://arxiv.org/pdf/{arxiv_id}',f'https://export.arxiv.org/pdf/{arxiv_id}']
    data=None; errors=[]
    for url in urls:
        for k in range(3):
            try:
                r=requests.get(url,timeout=45,headers={'User-Agent':'ISQGR-source-audit/1.0'})
                if r.status_code==200 and r.content[:4]==b'%PDF': data=r.content; break
                errors.append(f'{url}:HTTP{r.status_code}')
            except Exception as e: errors.append(f'{url}:{type(e).__name__}:{e}')
            time.sleep(2*(k+1))
        if data is not None: break
    if data is None:
        return {'mode':'source_authority','arxiv_id':arxiv_id,'classification':'INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION','errors':errors}
    try:
        rd=PdfReader(io.BytesIO(data)); text='\n'.join((p.extract_text() or '') for p in rd.pages)
    except Exception as e:
        return {'mode':'source_authority','arxiv_id':arxiv_id,'classification':'INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION','errors':[repr(e)]}
    low=text.lower(); snippets=[]
    for mt in MEASURE_TERMS:
        for m in re.finditer(mt,low):
            lo=max(0,m.start()-600); hi=min(len(text),m.end()+600); sn=text[lo:hi]
            sl=sn.lower(); topo=[t for t in TOPO_TERMS if t in sl]
            if topo:
                snippets.append({'measure_term':mt,'topology_terms':topo,'snippet':re.sub(r'\s+',' ',sn)[:1400]})
    # deterministic de-duplication, capped but raw full text metadata retained
    uniq=[]; seen=set()
    for s in snippets:
        key=s['snippet'][:240]
        if key not in seen: seen.add(key); uniq.append(s)
    return {'mode':'source_authority','arxiv_id':arxiv_id,'label':SOURCES[arxiv_id],
            'classification':'SOURCE_AUTHORITY_CANDIDATE_PRESENT' if uniq else 'NO_AUTOMATED_CANDIDATE_PASSAGE',
            'pdf_bytes':len(data),'pages':len(rd.pages),'candidate_passages':uniq[:30],
            'claim_lock':'automated text hits require manual equation-level audit; no gate credit'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mode',required=True,choices=['coarse2','fine32','sentinel','source']); ap.add_argument('--source'); ap.add_argument('--out',required=True); a=ap.parse_args()
    if a.mode in ('coarse2','fine32'): res=geometry(a.mode)
    elif a.mode=='sentinel': res=sentinel()
    else:
        if a.source not in SOURCES: raise SystemExit('frozen source id required')
        res=source_audit(a.source)
    p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in res.items() if k not in ('candidate_passages','rows','comparisons')},indent=2))
if __name__=='__main__': main()
