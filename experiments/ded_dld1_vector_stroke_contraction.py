#!/usr/bin/env python3
import argparse,json,pathlib,re,math
p=argparse.ArgumentParser();p.add_argument('--ded',required=True);p.add_argument('--dld',required=True);p.add_argument('--output',required=True);a=p.parse_args()
NUM=r'[-+]?(?:\d+\.\d+|\d+|\.\d+)'
TOK=re.compile(rf'{NUM}|\b(?:m|l|c|h|S|f\*|f|n)\b')
def strokes(path):
 t=pathlib.Path(path).read_text(errors='ignore'); t=t[t.find('%%Page:'):]
 stack=[]; cur=[]; out=[]
 for z in TOK.findall(t):
  if re.fullmatch(NUM,z): stack.append(float(z)); continue
  if z=='m':
   if len(stack)>=2: cur.append(('m',stack[-2],stack[-1])); stack=[]
  elif z=='l':
   if len(stack)>=2: cur.append(('l',stack[-2],stack[-1])); stack=[]
  elif z=='c':
   if len(stack)>=6: cur.append(('c',*stack[-6:])); stack=[]
  elif z=='h': cur.append(('h',)); stack=[]
  elif z=='S': out.append(cur); cur=[]; stack=[]
  elif z in ('f','f*','n'): cur=[]; stack=[]
 return out
def endpoint(cmd):
 return (cmd[-2],cmd[-1])
def select(paths,roi):
 x0,x1,y0,y1=roi; rows=[]
 for q in paths:
  if len(q)!=2 or q[0][0]!='m' or q[1][0] not in ('l','c'): continue
  u=(q[0][1],q[0][2]); v=endpoint(q[1])
  if all(x0<=x<=x1 and y0<=y<=y1 for x,y in (u,v)): rows.append((u,v))
 return rows
def cluster(edges,tol=3.0):
 pts=[p for e in edges for p in e]; centers=[]; ids=[]
 for p in pts:
  found=None
  for i,c in enumerate(centers):
   if math.dist(p,c)<=tol: found=i; break
  if found is None: centers.append(p); found=len(centers)-1
  ids.append(found)
 # recompute centroids once and remap deterministically by y descending then x
 sums=[[0.,0.,0] for _ in centers]
 for p,i in zip(pts,ids): sums[i][0]+=p[0];sums[i][1]+=p[1];sums[i][2]+=1
 cent=[(s[0]/s[2],s[1]/s[2]) for s in sums]
 order=sorted(range(len(cent)),key=lambda i:(-cent[i][1],cent[i][0])); mp={old:new for new,old in enumerate(order)}
 ed=[]
 for k in range(0,len(ids),2): ed.append(tuple(sorted((mp[ids[k]],mp[ids[k+1]]))))
 C=[cent[i] for i in order]
 mult={}
 for e in ed: mult[e]=mult.get(e,0)+1
 deg=[0]*len(C)
 for (u,v),m in mult.items(): deg[u]+=m;deg[v]+=m
 return C,mult,deg
def canon(mult,n): return sorted((u,v,m) for (u,v),m in mult.items())
def contract(mult,n,u,v):
 # merge v into u then relabel by degree signature independent of source labels
 raw={}
 for (x,y),m in mult.items():
  x=u if x==v else x; y=u if y==v else y
  if x==y: continue
  e=tuple(sorted((x,y))); raw[e]=raw.get(e,0)+m
 used=sorted(set(sum(([x,y] for x,y in raw),[])))
 mp={x:i for i,x in enumerate(used)}
 return {(min(mp[x],mp[y]),max(mp[x],mp[y])):m for (x,y),m in raw.items()},len(used)
def signature(mult,n):
 deg=[0]*n
 for (u,v),m in mult.items(): deg[u]+=m;deg[v]+=m
 return sorted(deg),sorted(mult.values())
dedE=select(strokes(a.ded),(130,255,-10,135)); dldE=select(strokes(a.dld),(130,225,190,350))
dedC,dedM,dedD=cluster(dedE); dldC,dldM,dldD=cluster(dldE)
# unique DLD edge of multiplicity 1 joining the two degree-5 centers
cands=[(u,v) for (u,v),m in dldM.items() if m==1 and dldD[u]==5 and dldD[v]==5]
contract_ok=False; contracted=None
if len(cands)==1:
 cm,cn=contract(dldM,len(dldC),*cands[0]); contracted={'n':cn,'mult':canon(cm,cn),'signature':signature(cm,cn)}
 contract_ok=(signature(cm,cn)==signature(dedM,len(dedC)))
expected=(len(dedE)==8 and len(dedC)==3 and sorted(dedM.values())==[4,4] and sorted(dedD)==[4,4,8] and len(dldE)==9 and len(dldC)==4 and sorted(dldM.values())==[1,4,4] and sorted(dldD)==[4,4,5,5])
gate=bool(expected and len(cands)==1 and contract_ok)
out={'gate':'ITER006_DED_DLD1_VECTOR_STROKE_CONTRACTION','ded':{'selected_strokes':len(dedE),'cluster_count':len(dedC),'centers':dedC,'multiplicities':canon(dedM,len(dedC)),'degrees':dedD,'signature':signature(dedM,len(dedC))},'dld1':{'selected_strokes':len(dldE),'cluster_count':len(dldC),'centers':dldC,'multiplicities':canon(dldM,len(dldC)),'degrees':dldD,'central_edge_candidates':cands},'contracted_dld1':contracted,'expected_source_topologies_match':expected,'contraction_isomorphic_by_degree_and_multiplicity_signature':contract_ok,'gate_pass':gate,'classification':'DED_DLD1_VERTEX_GRAPH_CONTRACTION_SOURCE_VERIFIED' if gate else 'DED_DLD1_VECTOR_STROKE_CONTRACTION_FAIL','claim_lock':'Vertex-graph source geometry only; no V/E/F subfoam embedding, j_f=0 amplitude identity, cylindrical consistency, convergence, bridge or new-physics claim.'}
pathlib.Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if not gate: raise SystemExit(2)
