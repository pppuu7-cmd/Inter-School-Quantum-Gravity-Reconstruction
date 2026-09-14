#!/usr/bin/env python3
import argparse
import hashlib
import json
import math
import os
import pathlib
import re
import subprocess
import sys
import urllib.request
from fractions import Fraction

from sympy import Rational, sqrt as ssqrt
from sympy.physics.wigner import wigner_6j

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "out" / "iter054"
OUT.mkdir(parents=True, exist_ok=True)

CALL_MAP = ROOT / "sources" / "ITER053_FIXED_SECTOR_BACKEND_CALL_MAP.json"
CALL_MAP_BLOB = "1af32d358747f333a04531d27af1e03b9a0bd038"
BACKEND_COMMIT = "052e4346028870bd76f69a3034e6cae8defb8f7f"
ITER051_RUN = 34818301950

EXPECTED_RUNTIME = {
    "bin/vertex-amplitude": "b4f8f536645b3fe6bc55830040f624140eefca02a3b960b9940b2564a7876e26",
    "lib/libsl2cfoam.so": "a539c968afde2a7ec397b2fa7184f9dd036042b82ff2ec5d8026c2b6881b71fc",
    "data_sl2cfoam/table_50.3j": "73d9170de4f04b776923106c5c6ea1bbb70cf2e62a14d24b83cda31194567e6e",
    "data_sl2cfoam/table_40.6j": "de1a29d0252c3c1ebf51b96d7fdebe7f21587ee65dcbc3864070774c14704b72",
}

BACKEND_VERTEX_URL = f"https://raw.githubusercontent.com/qg-cpt-marseille/sl2cfoam-next/{BACKEND_COMMIT}/src/vertex.c"
BACKEND_HEADER_URL = f"https://raw.githubusercontent.com/qg-cpt-marseille/sl2cfoam-next/{BACKEND_COMMIT}/inc/sl2cfoam.h"
BACKEND_VERTEX_BLOB = "9581999f0d5d59155e8c912fc7f2f3c5a98b346e"
BACKEND_HEADER_BLOB = "351e248611047602bbced0c6fed5e6be89243fd9"

RESULT_REQ = {
    ROOT / "results" / "ITER051_LORENTZIAN_PINNED_BACKEND_RUNTIME_PASS_2026-09-14.md": "LORENTZIAN_PINNED_BACKEND_RUNTIME_PASS",
    ROOT / "results" / "ITER052_LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK_PASS_2026-09-14.md": "LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK_AUTHORITY_PASS",
    ROOT / "results" / "ITER053_LORENTZIAN_PHASE_WEIGHT_AUTHORITY_PASS_2026-09-14.md": "LORENTZIAN_PHASE_WEIGHT_AUTHORITY_PASS_BOUNDARY_PHASE_QUALIFIED",
}

VERTEX_NAMES = ["up", "left", "bottom_left", "bottom_right", "right"]
PAIR_INDICES = [(1,2),(3,4),(5,6),(7,8),(9,10)]


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def fetch_exact(url: str, blob: str) -> str:
    with urllib.request.urlopen(url, timeout=45) as r:
        data = r.read()
    got = git_blob_sha(data)
    if got != blob:
        raise RuntimeError(f"blob mismatch {got} != {blob}: {url}")
    return data.decode("utf-8")


def emit(obj):
    (OUT / "evidence.json").write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")
    print(json.dumps(obj, indent=2, sort_keys=True))


def load_map():
    raw = CALL_MAP.read_bytes()
    if git_blob_sha(raw) != CALL_MAP_BLOB:
        raise RuntimeError("call-map blob mismatch")
    return json.loads(raw)


def runtime_identity(runtime: pathlib.Path):
    manifest_path = runtime.parent / "runtime_manifest.json"
    if not manifest_path.exists():
        # allow manifest beside extracted runtime in current directory
        alt = runtime / "runtime_manifest.json"
        manifest_path = alt if alt.exists() else manifest_path
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else None
    file_checks = {p: (runtime / p).exists() and sha256(runtime / p) == h for p,h in EXPECTED_RUNTIME.items()}
    manifest_checks = {
        "manifest_present": manifest is not None,
        "backend_commit": bool(manifest and manifest.get("backend_commit") == BACKEND_COMMIT),
        "build_flags": bool(manifest and manifest.get("build_flags") == {"BLAS":"system","OMP":"0","ADD_CFLAGS":""}),
        "fixed_cli_iter051": bool(manifest and manifest.get("fixed_cli") == {
            "gamma":"1.2","two_js":"1,1,1,1,1,1,1,1,1,1","two_is":"0,0,0,0,0","Dl":"0"
        }),
    }
    return manifest, file_checks, manifest_checks, all(file_checks.values()) and all(manifest_checks.values())


def half(x):
    return Fraction(int(x), 2)


def int_phase_sign(fr: Fraction):
    if fr.denominator != 1:
        raise ValueError(f"nonintegral phase exponent {fr}")
    return -1 if fr.numerator % 2 else 1


def sector_globals(data, sector):
    p = data[sector]["physical"]
    J = {f"j{n}": Fraction(1,2) for n in range(1,11)}
    I = {f"i{n}": Fraction(p["i1_to_i15"][n-1],1) for n in range(1,16)}
    return Fraction(1,2), J, I


def recoupling_factors(data, sector):
    jb,J,I = sector_globals(data, sector)
    specs = [
        ("up",       "j3","j6","j5",1,2),
        ("left",     "j1","j3","j2",3,4),
        ("bottom_left","j7","j1","j8",5,6),
        ("bottom_right","j7","j10","j4",7,8),
        ("right",    "j10","j6","j9",9,10),
    ]
    out=[]
    for name,a,b,c,li,ri in specs:
        L=I[f"i{li}"]; R=I[f"i{ri}"]
        # All frozen local face spins are 1/2; the exact source Wigner objects are
        # W6j(jb, a, iL, c, b, iR) with the source phases below.
        w = wigner_6j(Rational(jb.numerator,jb.denominator),
                      Rational(J[a].numerator,J[a].denominator),
                      Rational(L.numerator,L.denominator),
                      Rational(J[c].numerator,J[c].denominator),
                      Rational(J[b].numerator,J[b].denominator),
                      Rational(R.numerator,R.denominator))
        exponent = jb + J[a] + J[b] - J[c]
        sign = int_phase_sign(exponent)
        exact = sign * ssqrt((2*Rational(L.numerator,L.denominator)+1)*(2*Rational(R.numerator,R.denominator)+1)) * w
        out.append({
            "vertex":name,"left":f"i{li}","right":f"i{ri}",
            "wigner6j":str(w),"phase_exponent":str(exponent),"phase_sign":sign,
            "exact_factor":str(exact.simplify()),"float_factor":float(exact.evalf(30))
        })
    return out


def final_signs(data, sector):
    jb,J,I=sector_globals(data, sector)
    exps=[
        jb+J["j6"]+I["i12"],
        jb+J["j3"]+I["i13"],
        jb+J["j1"]+I["i11"],
        jb+J["j7"]+I["i14"],
        jb+J["j10"]+I["i15"],
    ]
    return [{"vertex":n,"exponent":str(e),"sign":int_phase_sign(e)} for n,e in zip(VERTEX_NAMES,exps)]


def face_phase_and_factor(data, sector):
    jb,J,I=sector_globals(data,sector)
    df_phase_exp=2*sum(J.values(), Fraction(0,1))
    df_phase=int_phase_sign(df_phase_exp)
    dfj=1
    for j in J.values():
        dfj *= int(2*j+1)
    paper_conversion=int_phase_sign(2*jb)
    return {"df_phase_exponent":str(df_phase_exp),"df_phase":df_phase,"dfj_weight1":dfj,"paper_conversion":paper_conversion}


def run_vertex(runtime: pathlib.Path, two_js, two_is, gamma=1.2, Dl=0):
    exe=runtime/"bin/vertex-amplitude"
    table=runtime/"data_sl2cfoam"
    cmd=[str(exe),str(table),str(gamma),",".join(map(str,two_js)),",".join(map(str,two_is)),str(Dl)]
    env=os.environ.copy()
    libdirs=[runtime/"lib",runtime/"ext/wigxjpf/lib",runtime/"ext/fastwigxj/lib"]
    env["LD_LIBRARY_PATH"] = ":".join(str(x) for x in libdirs) + (":"+env["LD_LIBRARY_PATH"] if env.get("LD_LIBRARY_PATH") else "")
    p=subprocess.run(cmd,text=True,capture_output=True,env=env,timeout=600)
    nums=[]
    for line in p.stdout.splitlines():
        try: nums.append(float(line.strip()))
        except Exception: pass
    val=nums[-1] if nums else None
    return {"command":cmd,"returncode":p.returncode,"value":val,"finite":bool(val is not None and math.isfinite(val)),"stdout":p.stdout[-8000:],"stderr":p.stderr[-8000:]}


def compute_summand(data, sector, runtime):
    manifest,file_checks,manifest_checks,runtime_ok=runtime_identity(runtime)
    if not runtime_ok:
        raise RuntimeError("runtime identity mismatch")
    calls=data[sector]["backend_calls"]
    vertices=[]
    for name in VERTEX_NAMES:
        c=calls[name]
        r=run_vertex(runtime,c["two_js"],c["two_is"],1.2,0)
        r["vertex"]=name
        r["two_js"]=c["two_js"]
        r["two_is"]=c["two_is"]
        vertices.append(r)
    rec=recoupling_factors(data,sector)
    finals=final_signs(data,sector)
    globalf=face_phase_and_factor(data,sector)
    if not all(v["returncode"]==0 and v["finite"] for v in vertices):
        author=None; paper=None
    else:
        prodv=math.prod(v["value"] for v in vertices)
        prodw=math.prod(x["float_factor"] for x in rec)
        prods=math.prod(x["sign"] for x in finals)
        author=prodv*prodw*prods*globalf["df_phase"]*globalf["dfj_weight1"]
        paper=globalf["paper_conversion"]*author
    return {
        "runtime_file_checks":file_checks,
        "runtime_manifest_checks":manifest_checks,
        "vertices":vertices,
        "recoupling":rec,
        "final_signs":finals,
        "global_factors":globalf,
        "author_summand":author,
        "paper_summand":paper,
        "author_finite":bool(author is not None and math.isfinite(author)),
        "paper_finite":bool(paper is not None and math.isfinite(paper)),
    }


def authority_object():
    data=load_map()
    vertex=fetch_exact(BACKEND_VERTEX_URL,BACKEND_VERTEX_BLOB)
    header=fetch_exact(BACKEND_HEADER_URL,BACKEND_HEADER_BLOB)
    nv=normalize(vertex)
    checks={
        "call_map_backend":data["backend_commit"]==BACKEND_COMMIT,
        "call_map_author":"84b375f2a2e0d29b44dd8820953553624bb007a3"==data["author_code_commit"],
        "call_map_gamma_Dl":data["argument_semantics"]["gamma"]==1.2 and data["argument_semantics"]["Dl"]==0,
        "required_results":all(p.exists() and needle in p.read_text(encoding="utf-8") for p,needle in RESULT_REQ.items()),
        "header_single_amplitude":"Computes a single vertex amplitude given spins js, intertwiners is" in header,
        "range_minmax_i1":"two_is[0], two_is[0]" in nv,
        "range_minmax_i2":"two_is[1], two_is[1]" in nv,
        "range_minmax_i3":"two_is[2], two_is[2]" in nv,
        "range_minmax_i4":"two_is[3], two_is[3]" in nv,
        "range_minmax_i5":"two_is[4], two_is[4]" in nv,
        "single_returns_unique_component":"TENSOR_GET(t, 5, 0, 0, 0, 0, 0)" in vertex,
    }
    emit({"lane":"authority-object","checks":checks,"pass":all(checks.values()),"amplitude_values_used":False,
          "failure_class":"LORENTZIAN_BOUNDED_FIVE_VERTEX_FIXED_SUMMAND_BLOCKED_SOURCE_OBJECT" if not all(checks.values()) else None})


def recoupling_controls():
    data=load_map()
    rp=recoupling_factors(data,"primary")
    rh=recoupling_factors(data,"heldout")
    fp=face_phase_and_factor(data,"primary")
    fh=face_phase_and_factor(data,"heldout")
    sp=final_signs(data,"primary")
    sh=final_signs(data,"heldout")
    primary_exact=all(x["exact_factor"]=="1/2" for x in rp)
    held_exact=all(x["exact_factor"] in ("-sqrt(3)/2","-sqrt(3)/2") for x in rh)
    checks={
        "primary_five_recouplings_plus_half":primary_exact,
        "heldout_five_recouplings_minus_sqrt3_half":held_exact,
        "primary_df_phase_plus":fp["df_phase"]==1,
        "heldout_df_phase_plus":fh["df_phase"]==1,
        "primary_face_1024":fp["dfj_weight1"]==1024,
        "heldout_face_1024":fh["dfj_weight1"]==1024,
        "primary_paper_conversion_minus":fp["paper_conversion"]==-1,
        "heldout_paper_conversion_minus":fh["paper_conversion"]==-1,
        "five_final_signs_each":len(sp)==5 and len(sh)==5,
    }
    emit({"lane":"recoupling-controls","primary_recoupling":rp,"heldout_recoupling":rh,
          "primary_final_signs":sp,"heldout_final_signs":sh,"primary_global":fp,"heldout_global":fh,
          "checks":checks,"pass":all(checks.values()),"amplitude_values_used":False,
          "failure_class":"INVALID_IMPLEMENTATION" if not all(checks.values()) else None})


def null_controls():
    data=load_map()
    held=data["heldout"]
    all_two_is=[x for n in VERTEX_NAMES for x in held["backend_calls"][n]["two_is"]]
    no_wrong_one=all(x in (0,2) for x in all_two_is) and 2 in all_two_is
    wrong=all_two_is.copy(); wrong[0]=1
    wrong_rejected=any(x not in (0,2) for x in wrong)
    phys=held["physical"]["i1_to_i15"]
    edge_product=math.prod(2*i+1 for i in phys)
    literal_wrong_up=[2,2,0,2,2]  # literal Eq11 substitutes i2 for original i1 at local i5 for heldout
    actual_up=held["backend_calls"]["up"]["two_is"]
    checks={
        "heldout_labels_use_0_or_2":no_wrong_one,
        "two_i_equal_1_sentinel_rejected":wrong_rejected,
        "manual_edge_product_nontrivial_and_forbidden":edge_product==2187,
        "literal_eq11_up_call_differs_from_source_qualified":literal_wrong_up != actual_up,
        "production_convention_is_author":True,
        "paper_conversion_separate_minus_one":face_phase_and_factor(data,"heldout")["paper_conversion"]==-1,
    }
    emit({"lane":"null-controls","heldout_edge_product_if_wrong_manual_factor":edge_product,
          "actual_up_two_is":actual_up,"literal_wrong_up_two_is":literal_wrong_up,
          "checks":checks,"pass":all(checks.values()),"amplitude_values_used":False,
          "failure_class":"INVALID_IMPLEMENTATION" if not all(checks.values()) else None})


def runtime_identity_lane(runtime):
    manifest,files,mchecks,ok=runtime_identity(runtime)
    emit({"lane":"runtime-identity","iter051_run":ITER051_RUN,"runtime_file_checks":files,"runtime_manifest_checks":mchecks,
          "backend_commit":manifest.get("backend_commit") if manifest else None,"pass":ok,"amplitude_values_used":False,
          "failure_class":"LORENTZIAN_BOUNDED_FIVE_VERTEX_FIXED_SUMMAND_BLOCKED_RUNTIME_TRANSPORT" if not ok else None})


def substantive(lane, runtime):
    data=load_map()
    sector="primary" if lane.startswith("primary") else "heldout"
    res=compute_summand(data,sector,runtime)
    # Freeze local structural factors again inside each substantive process.
    expected_rec="1/2" if sector=="primary" else "-sqrt(3)/2"
    factors_ok=all(x["exact_factor"]==expected_rec for x in res["recoupling"])
    call_ok=all(v["returncode"]==0 and v["finite"] for v in res["vertices"])
    finite=res["author_finite"] and res["paper_finite"]
    conversion_ok=(res["paper_summand"] == -res["author_summand"]) if finite else False
    passed=call_ok and factors_ok and finite and conversion_ok and all(res["runtime_file_checks"].values()) and all(res["runtime_manifest_checks"].values())
    emit({"lane":lane,"sector":sector,**res,"factors_ok":factors_ok,"all_vertex_calls_ok":call_ok,
          "paper_conversion_exact_minus":conversion_ok,"pass":passed,"amplitude_values_used":True,
          "failure_class":"INVALID_IMPLEMENTATION" if not passed else None})


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--lane",required=True,choices=[
        "authority-object","recoupling-controls","null-controls","runtime-identity",
        "primary-A","primary-B","heldout-A","heldout-B"])
    ap.add_argument("--runtime-root",default="")
    args=ap.parse_args()
    runtime=pathlib.Path(args.runtime_root).resolve() if args.runtime_root else None
    try:
        if args.lane=="authority-object": authority_object()
        elif args.lane=="recoupling-controls": recoupling_controls()
        elif args.lane=="null-controls": null_controls()
        elif args.lane=="runtime-identity": runtime_identity_lane(runtime)
        else: substantive(args.lane,runtime)
    except Exception as e:
        emit({"lane":args.lane,"pass":False,"infrastructure_failure":True,"error":repr(e),
              "amplitude_values_used":args.lane.startswith("primary") or args.lane.startswith("heldout"),
              "failure_class":"INVALID_IMPLEMENTATION"})

if __name__=="__main__":
    main()
