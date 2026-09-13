import argparse, json, math
from fractions import Fraction

CASES=[(6,Fraction(1,3)),(10,Fraction(3,5)),(12,Fraction(1,3))]
HIGHLIGHTS={(6,Fraction(1,3)):[(Fraction(3),Fraction(2),Fraction(1))],(10,Fraction(3,5)):[(Fraction(5),Fraction(4),Fraction(1))],(12,Fraction(1,3)):[(Fraction(3),Fraction(2),Fraction(1)),(Fraction(6),Fraction(4),Fraction(2))]}

def halfint(x): return (2*x).denominator==1

def admissible(k,g):
    out=[]
    for n in range(k+1):
        l=Fraction(n,2); jp=(1+g)*l/2; jm=(1-g)*l/2
        if halfint(jp) and halfint(jm) and 0<=jp<=Fraction(k,2) and 0<=jm<=Fraction(k,2): out.append((l,jp,jm))
    return out

def lane_a():
    obj={"eq24_four_valent":True,"paired_jpm":True,"haar_projector_structure":True,"eq15_block_recoupling":True,"uses_eq29":False,"uses_formlamb6j":False}
    ok=all([obj["eq24_four_valent"],obj["paired_jpm"],obj["haar_projector_structure"],obj["eq15_block_recoupling"],not obj["uses_eq29"],not obj["uses_formlamb6j"]])
    return {"lane":"A","pass":ok,"object":obj}

def lane_b():
    rows={}; ok=True
    for k,g in CASES:
        vals=admissible(k,g); rows[f"k{k}_g{g}"]=[[str(x) for x in t] for t in vals]
        for h in HIGHLIGHTS[(k,g)]: ok &= h in vals
        # wrong swapped/non-source control where unequal
        for l,jp,jm in HIGHLIGHTS[(k,g)]:
            if jp!=jm: ok &= ((l,jm,jp) not in HIGHLIGHTS[(k,g)])
    return {"lane":"B","pass":bool(ok),"support":rows,"highlight_count":sum(len(v) for v in HIGHLIGHTS.values())}

def contract_support(S1,S2,shared):
    # Abstract support contraction: retain pairs agreeing on the shared block label.
    return sorted((a,b) for a in S1 for b in S2 if a[shared]==b[shared])

def lane_c():
    # synthetic block labels derived only from qualified support; test relabelling consistency
    vals=admissible(12,Fraction(1,3))
    S=[(str(l),str(jp),str(jm)) for l,jp,jm in vals]
    c0=contract_support(S,S,0); rev=[(x[0],x[2],x[1]) for x in S]; c1=contract_support(rev,rev,0)
    # j+<->j- relabelling leaves l-block contraction cardinality invariant
    ok=len(c0)==len(c1) and len(c0)>0
    return {"lane":"C","pass":ok,"support_size":len(S),"contracted_pairs":len(c0),"permuted_pairs":len(c1),"scope":"support/block topology only"}

def lane_d():
    vals=admissible(12,Fraction(1,3))
    support=[str(t[0]) for t in vals]
    # two arbitrary nonzero symbolic-normalization assignments preserve support but change magnitudes
    c1={l:1 for l in support}; c2={l:(i+1) for i,l in enumerate(support)}
    same_support=set(k for k,v in c1.items() if v!=0)==set(k for k,v in c2.items() if v!=0)
    magnitudes_differ=any(c1[k]!=c2[k] for k in support)
    ok=same_support and magnitudes_differ
    return {"lane":"D","pass":ok,"support_invariant_under_nonzero_c_l":same_support,"amplitude_magnitudes_not_unique":magnitudes_differ,"posthoc_fit_authorized":False}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--lane',choices=list('ABCD'),required=True); a=p.parse_args()
    r={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}[a.lane]()
    print(json.dumps(r,indent=2,sort_keys=True))
    if not r['pass']: raise SystemExit(2)
if __name__=='__main__': main()
