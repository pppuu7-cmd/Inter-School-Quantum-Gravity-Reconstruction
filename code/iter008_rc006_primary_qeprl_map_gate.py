#!/usr/bin/env python3
import argparse, json, math
from fractions import Fraction
import mpmath as mp

TOL=1e-12

def qnum_sine(k,n):
    return math.sin(math.pi*n/(k+2))/math.sin(math.pi/(k+2))

def qnum_complex(k,n):
    q=complex(math.cos(2*math.pi/(k+2)), math.sin(2*math.pi/(k+2)))
    return (q**(n/2)-q**(-n/2))/(q**0.5-q**(-0.5))

def mapped(l,g):
    jp=Fraction(1,2)*(1+g)*l
    jm=Fraction(1,2)*(1-g)*l
    return jp,jm

def integer_admissible(x,jmax):
    return x.denominator==1 and 0 <= x <= jmax

def stream_a():
    maxerr=0.0; positives=True; zeros=True
    for k in (6,10,12):
        for n in range(1,k+2):
            err=abs(qnum_complex(k,n).real-qnum_sine(k,n))+abs(qnum_complex(k,n).imag)
            maxerr=max(maxerr,err)
        zeros &= abs(qnum_sine(k,0))<=TOL and abs(qnum_sine(k,k+2))<=TOL
        for j in range(0,k//2+1):
            positives &= qnum_sine(k,2*j+1)>0
    ok=maxerr<=TOL and zeros and positives
    return {"stream":"A","max_abs_error":maxerr,"root_zeros":zeros,"positive_dims":positives,"pass":ok}

def stream_b():
    published=[(6,Fraction(1,3),{3:(2,1)}),(10,Fraction(3,5),{5:(4,1)}),(12,Fraction(1,3),{3:(2,1),6:(4,2)})]
    details=[]; ok=True
    for k,g,controls in published:
        jmax=k//2
        valid={}
        for l in range(jmax+1):
            jp,jm=mapped(Fraction(l),g)
            if integer_admissible(jp,jmax) and integer_admissible(jm,jmax): valid[l]=(int(jp),int(jm))
        for l,target in controls.items(): ok &= valid.get(l)==target
        details.append({"k":k,"gamma":str(g),"valid":valid,"controls":controls})
    return {"stream":"B","details":details,"pass":bool(ok)}

def stream_c():
    base=[(6,Fraction(1,3),3),(10,Fraction(3,5),5),(12,Fraction(1,3),6)]
    perturb_ok=True; pert=[]
    for k,g,l in base:
        jmax=k//2
        for delta in (Fraction(-1,60),Fraction(1,60)):
            gp=g+delta
            if not (0<gp<1): continue
            jp,jm=mapped(Fraction(l),gp)
            failed=not (integer_admissible(jp,jmax) and integer_admissible(jm,jmax))
            perturb_ok &= failed
            pert.append({"k":k,"gamma":str(gp),"l":l,"failed_endpoint":failed})
    mism=0; total=0
    for k in (6,10,12):
        qwrong=complex(math.cos(math.pi/(k+2)),math.sin(math.pi/(k+2)))
        for n in range(2,k+1):
            wrong=(qwrong**(n/2)-qwrong**(-n/2))/(qwrong**0.5-qwrong**(-0.5))
            if abs(wrong.real-qnum_sine(k,n))+abs(wrong.imag)>TOL: mism+=1
            total+=1
    frac=mism/total
    ok=perturb_ok and frac>=0.80
    return {"stream":"C","perturbations":pert,"wrong_q_mismatch_fraction":frac,"pass":ok}

def stream_d():
    mp.mp.dps=50; maxrel=0.0; maxsym=0.0
    for k in (6,10,12):
        den=mp.sin(mp.pi/(k+2))
        for n in range(1,k+2):
            hi=mp.sin(mp.pi*n/(k+2))/den
            lo=qnum_sine(k,n)
            rel=abs(float(hi)-lo)/max(abs(float(hi)),1e-30)
            maxrel=max(maxrel,rel)
            maxsym=max(maxsym,abs(qnum_sine(k,n)-qnum_sine(k,k+2-n)))
    ok=maxrel<=TOL and maxsym<=TOL
    return {"stream":"D","max_relative_discrepancy":maxrel,"max_symmetry_error":maxsym,"pass":ok}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=list('ABCD'),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    fn={'A':stream_a,'B':stream_b,'C':stream_c,'D':stream_d}[a.stream]
    r=fn(); r['classifier']='STREAM_PASS' if r['pass'] else 'SCIENTIFIC_FAIL_SOURCE_RECONSTRUCTION_MISMATCH'
    with open(a.out,'w') as f: json.dump(r,f,indent=2,sort_keys=True)
    print(json.dumps(r,sort_keys=True))
    raise SystemExit(0 if r['pass'] else 2)
if __name__=='__main__': main()
