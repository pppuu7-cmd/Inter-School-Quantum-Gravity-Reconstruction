#!/usr/bin/env python3
import argparse,json,math,re
from pathlib import Path
REF={
0.3:{0:(0.0013370736856606288,0.0013370736856606288),1:(0.0028458022680066296,0.002149585409405197),2:(0.004469055610314016,0.0025250529059879425)},
0.5:{0:(5.496983896037186e-4,5.496983896037186e-4),1:(1.160314452673374e-3,8.875229918840471e-4),2:(1.7502215813554412e-3,1.031647217053245e-3)},
0.8:{0:(1.0909544347890166e-4,1.0909544347890163e-4),1:(2.2659482141165434e-4,1.7754260592919106e-4),2:(3.191850084380049e-4,2.0293549353841454e-4)},
1.2:{0:(1.2780379206216302e-5,1.2780379206216303e-5),1:(2.5960000424492336e-5,2.100830367642193e-5),2:(3.3937577257182434e-5,2.3629590996910224e-5)},
1.6:{0:(1.922261779345611e-6,1.9222617793456108e-6),1:(3.83038125939682e-6,3.184216022753061e-6),2:(4.775818101610845e-6,3.5520992974538404e-6)},
2.0:{0:(3.7591052442651034e-7,3.759105244265104e-7),1:(7.376380837393899e-7,6.261295759045302e-7),2:(8.952613602454995e-7,6.959576595319952e-7)},
2.5:{0:(6.617261720924785e-8,6.617261720924784e-8),1:(1.2794685943063189e-7,1.1073827361572201e-7),2:(1.5279442434299682e-7,1.2289390947472375e-7)},
3.0:{0:(1.5100198765908135e-8,1.5100198765908135e-8),1:(2.8873191318115093e-8,2.5349339785565516e-8),2:(3.4291177056392442e-8,2.8120776336540529e-8)}
}
ROW=re.compile(r'^D=(\d+)\s+dvd2=([^\s]+)\s+dvd3=([^\s]+)\s+terms2=(\d+)\s+nonzero2=(\d+)\s+terms3=(\d+)\s+nonzero3=(\d+)\s+cache=(\d+)\s*$')
def parse(p):
    o={}
    for line in Path(p).read_text().splitlines():
        m=ROW.match(line.strip())
        if m:o[int(m.group(1))]={'dvd2':float(m.group(2)),'dvd3':float(m.group(3)),'terms2':int(m.group(4)),'nonzero2':int(m.group(5)),'terms3':int(m.group(6)),'nonzero3':int(m.group(7)),'cache':int(m.group(8))}
    return o
def rel(a,b):return abs(a-b)/max(abs(a),abs(b),1e-300)
ap=argparse.ArgumentParser();ap.add_argument('--run1',required=True);ap.add_argument('--run2',required=True);ap.add_argument('--gamma',type=float,required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
r1,r2=parse(a.run1),parse(a.run2);Ds=[0,1,2,3];shape=sorted(r1)==Ds and sorted(r2)==Ds
finite=shape and all(math.isfinite(r1[D][k]) and math.isfinite(r2[D][k]) for D in Ds for k in ('dvd2','dvd3'))
repeat=max([rel(r1[D][k],r2[D][k]) for D in Ds for k in ('dvd2','dvd3')]) if shape else float('inf')
reg=[]
if shape:
    for D in (0,1,2):
        reg.extend([rel(r1[D]['dvd2'],REF[a.gamma][D][0]),rel(r1[D]['dvd3'],REF[a.gamma][D][1])])
regmax=max(reg) if reg else float('inf')
diag=[]
for D in Ds if shape else []:
    x,y=r1[D]['dvd2'],r1[D]['dvd3'];diag.append({'D':D,'dvd2':x,'dvd3':y,'dvd2_over_dvd3':x/y if y else None,'normalized_split':rel(x,y),'dvd2_relative_increment':None if D==0 else rel(x,r1[D-1]['dvd2']),'dvd3_relative_increment':None if D==0 else rel(y,r1[D-1]['dvd3']),'terms2':r1[D]['terms2'],'nonzero2':r1[D]['nonzero2'],'terms3':r1[D]['terms3'],'nonzero3':r1[D]['nonzero3'],'cache':r1[D]['cache']})
pattern=bool(shape and diag[3]['dvd2_relative_increment']<diag[2]['dvd2_relative_increment'] and diag[3]['dvd3_relative_increment']<diag[2]['dvd3_relative_increment'])
numerical=bool(shape and finite and repeat<=1e-12 and regmax<=1e-12)
out={'test':'LORENTZIAN_EPRL_DVD_SYMMETRIC_D3_EXTENSION','gamma':a.gamma,'numerical_gate_pass':numerical,'repeat_max_relative_difference':repeat,'D012_regression_max_relative_error':regmax,'D3_stabilization_pattern_pass':pattern,'diagnostics':diag,'classification':'DVD_D3_EXTENSION_LANE_PASS' if numerical else 'DVD_D3_EXTENSION_LANE_NUMERICAL_FAIL','claim_lock':'D3 pattern support is another finite-cutoff diagnostic only; not convergence, refinement, continuum, bridge, novelty or new physics.'}
Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if not numerical:raise SystemExit(2)
