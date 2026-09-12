#!/usr/bin/env python3
"""Prospective named-anchor dependency audit for RC006 Eq.(29).

Uses only exact internal TeX labels already qualified by the previous 6/6
reference-chain gate.  It builds a label->reference graph by assigning each
\ref/\eqref/\autoref to its nearest preceding label. No figure geometry and no
relaxed lexical matching enter this object.
"""
from pathlib import Path
import argparse,json,re,collections

ANCHORS=(
 'app:EPRL-diagram','app:EPRL-norm','app:graph',
 'eq:BC-3-int','eq:BC-3-valent','eq:eprl-3-valent',
 'dependency_connectivity')
TARGETS={'6j-def','eq:recoupling-basis','eq:eprl-map','fig:recoupling','eq:SVD','eq:svd'}
STARTS={'app:EPRL-diagram','app:EPRL-norm','app:graph','eq:BC-3-int','eq:BC-3-valent','eq:eprl-3-valent'}

def lineno(t,p): return t.count('\n',0,p)+1

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--anchor',choices=ANCHORS,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    fs=list(Path(a.source_dir).rglob('*.tex'))
    if len(fs)!=1: raise SystemExit('monolithic source prerequisite violated')
    t=fs[0].read_text(errors='ignore')
    labs=[]
    for m in re.finditer(r'\\label\s*\{([^}]+)\}',t): labs.append((m.start(),m.group(1),lineno(t,m.start())))
    refs=[]
    for m in re.finditer(r'\\(?:ref|eqref|autoref)\s*\{([^}]+)\}',t): refs.append((m.start(),m.group(1),lineno(t,m.start())))
    labels_by_name=collections.defaultdict(list)
    for p,n,l in labs: labels_by_name[n].append((p,l))
    # nearest preceding label defines structural source node for each reference
    edges=collections.defaultdict(set)
    li=0; current=None
    events=sorted([(p,0,n,l) for p,n,l in labs]+[(p,1,n,l) for p,n,l in refs])
    for p,k,n,l in events:
        if k==0: current=n
        elif current is not None and n in labels_by_name: edges[current].add(n)
    if a.anchor!='dependency_connectivity':
        defs=labels_by_name.get(a.anchor,[])
        outgoing=sorted(edges.get(a.anchor,set()))
        if defs:
            p,l=defs[0]; lo=max(0,p-600); hi=min(len(t),p+1600); ctx=' '.join(t[lo:hi].split())
        else: l=None; ctx=''
        metrics={'definition_count':len(defs),'definition_line':l,'outgoing_resolved_refs':outgoing,'outgoing_count':len(outgoing),'context_excerpt':ctx[:1800]}
        ok=len(defs)==1 and len(ctx)>100
    else:
        # undirected reachability is frozen here because source cross-reference
        # membership is the object; directed semantic ordering is not asserted.
        adj=collections.defaultdict(set)
        for u,vs in edges.items():
            for v in vs: adj[u].add(v); adj[v].add(u)
        reached=set(STARTS); q=collections.deque(STARTS)
        while q:
            u=q.popleft()
            for v in adj[u]:
                if v not in reached: reached.add(v); q.append(v)
        hit=sorted(TARGETS & reached)
        metrics={'start_labels':sorted(STARTS),'target_labels':sorted(TARGETS),'reachable_targets':hit,'reachable_target_count':len(hit),'graph_nodes':len(set(labels_by_name)),'graph_edges':sum(len(v) for v in edges.values())}
        ok=all(s in labels_by_name for s in STARTS) and len(hit)>=1
    out={'test':'RC006_NAMED_ANCHOR_DEPENDENCY_AUDIT','anchor':a.anchor,'source':'official arXiv 1609.02429 monolithic TeX source','metrics':metrics,'frozen_gate_pass':bool(ok),'classification_if_pass':'PASS_NAMED_SOURCE_ANCHOR_DEPENDENCY_PREREQUISITE_ONLY','claim_lock':'Exact label/ref structure only; no figure geometry, unique tensor ordering, Eq29 amplitude, bridge or candidate-theory claim.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
    if not ok: raise SystemExit(2)
if __name__=='__main__': main()
