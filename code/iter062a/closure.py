#!/usr/bin/env python3
import argparse, hashlib, json, re
from pathlib import Path

EXPECTED_SOURCE_SHA256 = "78415347fa92b1d0bce1bbd4010faeb3cc939c5f5d6b14d72f340138e4c573ef"

def sha256_bytes(b): return hashlib.sha256(b).hexdigest()
def norm(s): return re.sub(r"\s+", " ", s).strip()

def equation_blocks(tex):
    pat = re.compile(r"\\begin\{(?:equation\*?|eqnarray\*?|align\*?)\}(.*?)\\end\{(?:equation\*?|eqnarray\*?|align\*?)\}", re.S)
    return [m.group(0) for m in pat.finditer(tex)]

def labelled(tex, label):
    blocks = equation_blocks(tex)
    out = [b for b in blocks if ("\\label{"+label+"}") in b]
    return out

def contexts(tex, patterns, radius=420):
    out=[]
    for p in patterns:
        m=re.search(p, tex, re.I|re.S)
        if m:
            a=max(0,m.start()-radius); b=min(len(tex),m.end()+radius)
            out.append({"pattern":p,"offset":m.start(),"context":norm(tex[a:b])[:1800]})
    return out

def explicit_definition(blocks, tokens):
    for b in blocks:
        if "=" in b and all(re.search(t,b,re.I|re.S) for t in tokens):
            return True, norm(b)[:4000]
    return False, ""

def run_lane(lane, tex, source_hash):
    eqs=equation_blocks(tex)
    base={"lane":lane,"source_sha256":source_hash,"expected_source_sha256":EXPECTED_SOURCE_SHA256,"source_identity_ok":source_hash==EXPECTED_SOURCE_SHA256,"claim_lock":"restricted Riemannian quantum-cuboid kernel closure only; zero bridge credit"}
    if not base["source_identity_ok"]:
        return {**base,"pass":False,"classification":"SOURCE_IDENTITY_MISMATCH"}

    if lane=="dependency-source-identity":
        return {**base,"pass":True,"classification":"PASS_SOURCE_IDENTITY"}

    if lane=="vertex-kernel-closure":
        # Conservative: require an explicit equality defining a hatted amplitude, alpha dependence,
        # and a source definition/use of the dimension factor rather than supplying either externally.
        hatted=[b for b in eqs if re.search(r"hat\s*\{?\\mathcal\s*\{?A",b,re.I)]
        hat_ok,hat_def=explicit_definition(hatted,[r"hat",r"mathcal",r"alpha"])
        dw_blocks=[b for b in eqs if re.search(r"d[_^]?\s*\{?W|mathrm\{dim\}|2j\+1",b,re.I)]
        dw_ok=bool(dw_blocks) or bool(re.search(r"d[_^]?\s*\{?W\s*\}?.{0,120}=",tex,re.I|re.S))
        # Require an asymptotic/dressed-amplitude dependency to be explicit somewhere in source.
        asym_ok=bool(re.search(r"asymptot|stationary phase|large[- ]?j|large spin",tex,re.I))
        ok=hat_ok and dw_ok and asym_ok
        return {**base,"pass":ok,"classification":"PASS_VERTEX_KERNEL_CLOSURE" if ok else "BLOCKED_VERTEX_KERNEL_DEPENDENCY","hat_definition_found":hat_ok,"dimension_factor_found":dw_ok,"asymptotic_dependency_found":asym_ok,"hat_definition":hat_def,"contexts":contexts(tex,[r"hat\s*\{?\\mathcal.{0,1000}?alpha",r"d[_^]?\s*\{?W",r"asymptot|stationary phase"])}

    if lane=="renormalized-amplitude-closure":
        blocks=labelled(tex,"Eq:RenormalizedAmplitude")
        b=blocks[0] if blocks else ""
        checks={
            "label":bool(blocks),
            "d24j":bool(re.search(r"d\s*\^\s*\{?24\}?\s*j|d\^\{24\}j",b)),
            "sixteen_vertices":bool(re.search(r"prod.*v\s*=\s*1.*16|prod.*16",b,re.S)),
            "constraint_product":bool(re.search(r"prod.*F.*J.*sum.*j",b,re.S)),
            "normalization":bool(re.search(r"N[_\\].*J|frac\s*\{?1\}?\s*\{?N",b,re.S)),
            "alpha_vertex":bool(re.search(r"alpha",b,re.I)),
        }
        ok=all(checks.values())
        return {**base,"pass":ok,"classification":"PASS_RENORMALIZED_AMPLITUDE_CLOSURE" if ok else "BLOCKED_RENORMALIZED_AMPLITUDE_OBJECT","checks":checks,"equation":norm(b)[:5000]}

    if lane=="gluing-index-closure":
        b=(labelled(tex,"Eq:RenormalizedAmplitude") or [""])[0]
        # Frozen minimum for executable incidence: 24 internal variables, six coarse faces,
        # sixteen refined vertices, and delta/constraint relation from fine faces to each coarse face.
        checks={
            "internal_count_24":bool(re.search(r"d\s*\^\s*\{?24\}?\s*j|d\^\{24\}j",b)),
            "sixteen_vertices":bool(re.search(r"prod.*v\s*=\s*1.*16|prod.*16",b,re.S)),
            "coarse_to_fine_constraint":bool(re.search(r"J[_\\].*sum.*f.*subset.*F.*j",b,re.S)),
            "source_refinement_language":bool(re.search(r"refin|coarse|fine|embedding|subdiv",tex,re.I)),
            "incidence_explanation":bool(re.search(r"24.{0,600}(spin|area|face)|sixteen|16.{0,500}(vertex|hypercub)",tex,re.I|re.S)),
        }
        ok=all(checks.values())
        return {**base,"pass":ok,"classification":"PASS_GLUING_INDEX_CLOSURE" if ok else "BLOCKED_GLUING_INDEX_INCIDENCE","checks":checks,"contexts":contexts(tex,[r"d\^\{24\}j",r"f\\subset F",r"16.{0,300}(vertex|hypercub)"])}

    if lane=="observable-closure":
        ob=(labelled(tex,"Eq:Observable") or [""])[0]
        vol=labelled(tex,"Eq:4Volume")
        exp=labelled(tex,"Eq:ExpectationValueCoarseGraining")
        checks={
            "observable_variance":bool(ob and re.search(r"Delta.*mathcal.*V|V.*langle.*V",ob,re.S)),
            "four_volume_formula":bool(vol),
            "coarse_graining_expectation":bool(exp),
            "fixed_boundary_context":bool(re.search(r"fixed.{0,120}boundar|boundar.{0,120}fixed|same.{0,120}boundar",tex,re.I|re.S)),
            "alpha_flow_context":bool(re.search(r"alpha.{0,180}(prime|flow|renorm|fixed)|alpha\s*'",tex,re.I|re.S)),
        }
        ok=all(checks.values())
        return {**base,"pass":ok,"classification":"PASS_OBSERVABLE_CLOSURE" if ok else "BLOCKED_OBSERVABLE_OR_BOUNDARY_OBJECT","checks":checks,"observable":norm(ob)[:3000],"volume":norm(vol[0])[:3000] if vol else "","expectation":norm(exp[0])[:3000] if exp else "","contexts":contexts(tex,[r"fixed.{0,120}boundar",r"alpha.{0,180}(flow|renorm|fixed)"])}

    if lane=="adversarial-null":
        rb=(labelled(tex,"Eq:RenormalizedAmplitude") or [""])[0]
        ob=(labelled(tex,"Eq:Observable") or [""])[0]
        mutations=[]
        tests=[
            ("remove_16_vertices", rb.replace("16","15",1), lambda x: bool(re.search(r"prod.*v\s*=\s*1.*16|prod.*16",x,re.S))),
            ("remove_24_measure", re.sub(r"d\s*\^\s*\{?24\}?\s*j|d\^\{24\}j","d^{23}j",rb,count=1), lambda x: bool(re.search(r"d\s*\^\s*\{?24\}?\s*j|d\^\{24\}j",x))),
            ("remove_coarse_fine_constraint", re.sub(r"\\prod_F.*?\\prod_{v",r"\\prod_{v",rb,count=1,flags=re.S), lambda x: bool(re.search(r"J[_\\].*sum.*f.*subset.*F.*j",x,re.S))),
            ("remove_normalization", re.sub(r"\\frac\s*\{1\}\s*\{N[^}]*\}","1",rb,count=1), lambda x: bool(re.search(r"N[_\\].*J|frac\s*\{?1\}?\s*\{?N",x,re.S))),
            ("variance_to_mean", re.sub(r"\\Big\(.*?\\Big\)\^2","\\mathcal{V}_1",ob,count=1,flags=re.S), lambda x: bool(re.search(r"\^2|squared",x,re.I))),
        ]
        for name,mut,pred in tests:
            detected=not pred(mut)
            mutations.append({"name":name,"detected":detected})
        detected=sum(x["detected"] for x in mutations)
        ok=detected==len(mutations)
        return {**base,"pass":ok,"classification":"PASS_ADVERSARIAL_NULL" if ok else "INVALID_NULL_SENSITIVITY","detected":detected,"total":len(mutations),"mutations":mutations}

    raise SystemExit("unknown lane")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--lane",required=True); ap.add_argument("--source",required=True); ap.add_argument("--out",required=True)
    a=ap.parse_args(); raw=Path(a.source).read_bytes(); tex=raw.decode("utf-8",errors="replace"); h=sha256_bytes(raw)
    res=run_lane(a.lane,tex,h); Path(a.out).write_text(json.dumps(res,indent=2,sort_keys=True)+"\n")
    print(json.dumps(res,indent=2,sort_keys=True))
    # Scientific BLOCKED is data, not CI failure. Only identity mismatch exits non-zero because predicates cannot be trusted.
    if res.get("classification")=="SOURCE_IDENTITY_MISMATCH": raise SystemExit(2)
if __name__=="__main__": main()
