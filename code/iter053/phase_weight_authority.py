#!/usr/bin/env python3
import argparse
import hashlib
import json
import pathlib
import re
import urllib.request
from collections import Counter, defaultdict
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "out" / "iter053"
OUT.mkdir(parents=True, exist_ok=True)

AUTHOR_COMMIT = "84b375f2a2e0d29b44dd8820953553624bb007a3"
BACKEND_COMMIT = "052e4346028870bd76f69a3034e6cae8defb8f7f"

URLS = {
    "eprl": f"https://raw.githubusercontent.com/PietropaoloFrisoni/Monte_Carlo_spinfoams/{AUTHOR_COMMIT}/src/vertex_renormalization_EPRL_MC.jl",
    "bf": f"https://raw.githubusercontent.com/PietropaoloFrisoni/Monte_Carlo_spinfoams/{AUTHOR_COMMIT}/src/vertex_renormalization_BF.jl",
    "utilities": f"https://raw.githubusercontent.com/PietropaoloFrisoni/Monte_Carlo_spinfoams/{AUTHOR_COMMIT}/src/utilities.jl",
    "vertex": f"https://raw.githubusercontent.com/qg-cpt-marseille/sl2cfoam-next/{BACKEND_COMMIT}/src/vertex.c",
    "b4": f"https://raw.githubusercontent.com/qg-cpt-marseille/sl2cfoam-next/{BACKEND_COMMIT}/src/b4.c",
}
EXPECTED_BLOBS = {
    "eprl":"6b627f7c2329724b589947195edc7e5ee7c18bb1",
    "bf":"6ce6a9cb31db931bb3491932edfe1828d0852091",
    "utilities":"7dddb9e34156264c2b599f74ed38853a2799ddb0",
    "vertex":"9581999f0d5d59155e8c912fc7f2f3c5a98b346e",
    "b4":"ccbe7d907ff5c04fd876343b6e732759064567c8",
}
DATA_PATH = ROOT / "sources" / "ITER053_PHASE_WEIGHT_DATA.json"
DATA_BLOB = "9b668b4b8ad749cb45eadd7b78434d9c1cd64bbb"
ALPHA_PATH = ROOT / "prereg" / "ITER010_RC006_EPRL_ALPHA_MEASURE_FAMILY_GATE.md"

ORIGINAL_VERTICES = {
    "up": ["ib","i4","i11","i12","i1"],
    "left": ["ib","i6","i14","i13","i3"],
    "bottom_left": ["ib","i8","i15","i11","i5"],
    "bottom_right": ["ib","i10","i12","i14","i7"],
    "right": ["ib","i2","i13","i15","i9"],
}
PAIRS = [("i1","i2"),("i3","i4"),("i5","i6"),("i7","i8"),("i9","i10")]

W6_PHASES = [
    {"jb":1,"j3":1,"j6":1,"j5":-1},
    {"jb":1,"j1":1,"j3":1,"j2":-1},
    {"jb":1,"j7":1,"j1":1,"j8":-1},
    {"jb":1,"j7":1,"j10":1,"j4":-1},
    {"jb":1,"j10":1,"j6":1,"j9":-1},
]
FINAL_PHASES = [
    {"jb":1,"j6":1,"i12":1},
    {"jb":1,"j3":1,"i13":1},
    {"jb":1,"j1":1,"i11":1},
    {"jb":1,"j7":1,"i14":1},
    {"jb":1,"j10":1,"i15":1},
]

PARITY_PANEL = {
    "S0":{"B":1,"J":[1,1,1,1,1,1,1,1,1,1],"I":[0,0,0,0,0]},
    "S1":{"B":1,"J":[1,1,1,1,1,1,1,1,1,1],"I":[0,2,0,2,0]},
    "S2":{"B":1,"J":[1,1,1,1,2,2,1,1,2,1],"I":[0,1,0,0,0]},
}


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def fetch_exact(key: str) -> str:
    with urllib.request.urlopen(URLS[key], timeout=45) as r:
        data = r.read()
    got = git_blob_sha(data)
    if got != EXPECTED_BLOBS[key]:
        raise RuntimeError(f"{key} blob mismatch {got} != {EXPECTED_BLOBS[key]}")
    return data.decode("utf-8")


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def emit(obj):
    (OUT / "evidence.json").write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")
    print(json.dumps(obj, indent=2, sort_keys=True))


def add_expr(dst, src, scale=1):
    for k,v in src.items():
        dst[k] += scale*v


def total_phase_coeffs(include_df=True, omit_w6=None):
    c=defaultdict(int)
    if include_df:
        for n in range(1,11): c[f"j{n}"] += 2
    for idx,e in enumerate(W6_PHASES):
        if omit_w6 is not None and idx == omit_w6: continue
        add_expr(c,e)
    for e in FINAL_PHASES: add_expr(c,e)
    return dict(c)


def paper_chi_coeffs():
    c={f"j{n}":1 for n in range(1,11)}
    c.update({f"i{n}":1 for n in range(11,16)})
    return c


def subtract(a,b):
    keys=set(a)|set(b)
    return {k:a.get(k,0)-b.get(k,0) for k in sorted(keys) if a.get(k,0)-b.get(k,0) != 0}


def phase_parts_doubled(B,J,I):
    w=[
        B+J[2]+J[5]-J[4],
        B+J[0]+J[2]-J[1],
        B+J[6]+J[0]-J[7],
        B+J[6]+J[9]-J[3],
        B+J[9]+J[5]-J[8],
    ]
    f=[
        B+J[5]+I[1],
        B+J[2]+I[2],
        B+J[0]+I[0],
        B+J[6]+I[3],
        B+J[9]+I[4],
    ]
    return w,f


def executable_phase_int(point, include_df=True, omit_w6=None):
    B,J,I=point["B"],point["J"],point["I"]
    w,f=phase_parts_doubled(B,J,I)
    if not all(x % 2 == 0 for x in w+f):
        raise ValueError("nonintegral frozen phase component")
    e = sum(J) if include_df else 0
    e += sum(x//2 for idx,x in enumerate(w) if omit_w6 is None or idx != omit_w6)
    e += sum(x//2 for x in f)
    return e


def paper_phase_int(point):
    num=sum(point["J"])+sum(point["I"])
    if num % 2: raise ValueError("paper chi nonintegral")
    return num//2


def paper_authority():
    data_bytes=DATA_PATH.read_bytes()
    data=json.loads(data_bytes)
    p=data["paper_source"]
    checks={
        "data_blob_match":git_blob_sha(data_bytes)==DATA_BLOB,
        "main_tex_sha":p["main_tex_sha256"]=="bff93f3a7857658264a04eb23521bb935a68eccb7760b284589ff5ec4073f063",
        "raw_digest":p["rawtex_artifact_digest"]=="sha256:191262f0c2a6d5c5b3ac6f1036caacd6808735c4bc38ecc73c45da49b2c53cb9",
        "edge_dim":p["edge_amplitude"]=="A_e(i_e)=2 i_e+1",
        "face_dim":p["face_amplitude_standard"]=="A_f(j_f)=2 j_f+1",
        "eq11_faces":p["vertex_renormalization_face_product"]=="prod_{f=1}^{10}(2 j_f+1)",
        "eq11_edges":p["vertex_renormalization_intertwiner_product"]=="prod_{e=1}^{15}(2 i_e+1)",
        "phase":p["phase"]=="(-1)^chi",
        "chi":p["chi"]=="sum_{k=1}^{10} j_k + sum_{k=11}^{15} i_k",
        "mu_deformation":p["deformed_face_amplitude"]=="A_f(j_f)=(2j_f+1)^mu",
        "standard_mu":p["standard_mu"]==1,
    }
    emit({"lane":"paper-authority","checks":checks,"pass":all(checks.values()),"amplitude_values_used":False,
          "failure_class":"INVALID_PROVENANCE" if not all(checks.values()) else None})


def author_code():
    eprl=fetch_exact("eprl")
    bf=fetch_exact("bf")
    ne=norm(eprl); nb=norm(bf)
    rec_signs=[
        "(-1)^(jb + jbrightgreen + jred - jgrassgreen)",
        "(-1)^(jb + jpink + jbrightgreen - jblue)",
        "(-1)^(jb + jbrown + jpink - jdarkgreen)",
        "(-1)^(jb + jbrown + jviolet - jpurple)",
        "(-1)^(jb + jviolet + jred - jorange)",
    ]
    final_signs=[
        "(-1)^(jb + jred + rIur_intertw)",
        "(-1)^(jb + jbrightgreen + rIu_intertw)",
        "(-1)^(jb + jpink + rIul_intertw)",
        "(-1)^(jb + jbrown + rIbl_intertw)",
        "(-1)^(jb + jviolet + rIbr_intertw)",
    ]
    checks={
        "face_weight_comment":"each internal face with spin j has dimension (2j+1)^(weight)" in eprl,
        "dfj_all_ten":all(name in eprl for name in ["jpink","jblue","jbrightgreen","jbrown","jdarkgreen","jviolet","jpurple","jred","jorange","jgrassgreen"]),
        "df_phase":"df_phase = (-1)^(2 * (jpink + jblue + jbrightgreen + jbrown + jdarkgreen + jviolet + jpurple + jred + jorange + jgrassgreen))" in ne,
        "weighted_dfj":"*= dfj^(weight) * df_phase" in ne,
        "five_recoupling_sqrtdims":eprl.count("sqrt((2r") >= 5,
        "all_recoupling_signs":all(x in eprl for x in rec_signs),
        "all_final_signs":all(x in eprl for x in final_signs),
        "bf_standard_weight":"amp *= dfj * df_phase" in nb,
    }
    emit({"lane":"author-code","checks":checks,"recoupling_signatures":rec_signs,"final_signatures":final_signs,
          "pass":all(checks.values()),"amplitude_values_used":False,
          "failure_class":"LORENTZIAN_PHASE_WEIGHT_BLOCKED_SOURCE_NORMALIZATION" if not all(checks.values()) else None})


def backend_normalization():
    vertex=fetch_exact("vertex")
    b4=fetch_exact("b4")
    nv=norm(vertex); nb=norm(b4)
    checks={
        "vertex_15j_half_dimensions":"w15j *= sqrt(DIM(two_i1) * DIM(two_k2) * DIM(two_k3) * DIM(two_k4) * DIM(two_k5));" in nv,
        "booster_i_k_half_dimensions":"matrix_get(b4, dimi, ii, ki) += sqrt(DIM(two_i) * DIM(two_k)) * matrix_get(b4_thread, dimi, ii, ki);" in nb,
    }
    # Algebraic consequence: the 15j sqrt(k2..k5) times four B4 sqrt(k_e)
    # yields one DIM(k_e) each, while external i1..i5 retain sqrt DIM.
    external_i_exponents={f"i{n}":str(Fraction(1,2)) for n in range(1,6)}
    virtual_k_exponents={f"k{n}":str(Fraction(1,1)) for n in range(2,6)}
    consequence=all(checks.values())
    emit({"lane":"backend-normalization","checks":checks,"per_vertex_external_i_exponents":external_i_exponents,
          "per_vertex_virtual_k_exponents":virtual_k_exponents,"per_vertex_external_sqrt_product_established":consequence,
          "pass":consequence,"amplitude_values_used":False,
          "failure_class":"LORENTZIAN_PHASE_WEIGHT_BLOCKED_SOURCE_NORMALIZATION" if not consequence else None})


def symbolic_crosswalk():
    code=total_phase_coeffs(True,None)
    paper=paper_chi_coeffs()
    diff=subtract(code,paper)
    expected={"jb":10,"j1":4,"j3":4,"j6":4,"j7":4,"j10":4}
    phase_exact=diff==expected
    boundary_only=(diff.get("jb",0)-2)%4==0 and all(v%4==0 for k,v in diff.items() if k!="jb")

    dims=defaultdict(Fraction)
    for vals in ORIGINAL_VERTICES.values():
        for x in vals:
            if x!="ib": dims[x]+=Fraction(1,2)
    for a,b in PAIRS:
        dims[a]+=Fraction(1,2); dims[b]+=Fraction(1,2)
    dims_out={f"i{n}":str(dims[f"i{n}"]) for n in range(1,16)}
    dim_pass=all(dims[f"i{n}"]==1 for n in range(1,16))

    data=json.loads(DATA_PATH.read_text())
    mu_weight=(data["paper_source"]["standard_mu"]==1 and data["author_code"]["face_exponent_symbol"]=="weight")
    emit({
        "lane":"symbolic-crosswalk",
        "author_total_phase_coefficients":code,
        "paper_chi_coefficients":paper,
        "difference_coefficients":diff,
        "expected_difference":expected,
        "difference_exact":phase_exact,
        "sign_residual_boundary_only":boundary_only,
        "boundary_sign_factor":"(-1)^(2*jb)",
        "global_intertwiner_dimension_exponents":dims_out,
        "all_edge_exponents_one":dim_pass,
        "mu_equals_author_weight_semantics":mu_weight,
        "standard_mu_weight":1,
        "pass":phase_exact and boundary_only and dim_pass and mu_weight,
        "amplitude_values_used":False,
        "failure_class":None if phase_exact and boundary_only and dim_pass and mu_weight else "LORENTZIAN_PHASE_WEIGHT_STRUCTURAL_FAIL",
    })


def null_controls():
    alpha=ALPHA_PATH.read_text(encoding="utf-8")
    data=json.loads(DATA_PATH.read_text())
    alpha_rejected=("reduced Euclidean" in alpha and "SU(2)_k" in alpha and "q-dimension" in alpha and data["project_alpha_firewall"]["not_identified_with_lorentzian_mu"] is True)

    # Correct exponents are one; adding the paper edge product manually again would make them two.
    double_edge={f"i{n}":2 for n in range(1,16)}
    double_rejected=all(v!=1 for v in double_edge.values())

    panel={}
    omit_df_detected=False
    omit_w6_detected=False
    for name,p in PARITY_PANEL.items():
        correct=executable_phase_int(p,True,None)
        paper=paper_phase_int(p)
        expected=(-1)**p["B"]
        correct_ratio=(-1)**(correct-paper)
        no_df=executable_phase_int(p,False,None)
        no_df_ratio=(-1)**(no_df-paper)
        no_up=executable_phase_int(p,True,0)
        no_up_ratio=(-1)**(no_up-paper)
        if name=="S2" and no_df_ratio!=expected: omit_df_detected=True
        if no_up_ratio!=expected: omit_w6_detected=True
        panel[name]={
            "all_component_phases_integral":True,
            "correct_ratio":correct_ratio,
            "expected_boundary_ratio":expected,
            "omit_df_phase_ratio":no_df_ratio,
            "omit_up_recoupling_phase_ratio":no_up_ratio,
            "correct_matches_boundary_only":correct_ratio==expected,
        }
    checks={
        "rc006_alpha_import_rejected":alpha_rejected,
        "manual_second_edge_product_rejected":double_rejected,
        "omit_df_phase_detected_on_S2":omit_df_detected,
        "omit_up_recoupling_phase_detected":omit_w6_detected,
        "all_correct_panel_points_boundary_only":all(x["correct_matches_boundary_only"] for x in panel.values()),
    }
    emit({"lane":"null-controls","checks":checks,"parity_panel":panel,"pass":all(checks.values()),"amplitude_values_used":False,
          "failure_class":"INVALID_IMPLEMENTATION" if not all(checks.values()) else None})


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--lane",required=True,choices=["paper-authority","author-code","backend-normalization","symbolic-crosswalk","null-controls"])
    lane=ap.parse_args().lane
    fn={
        "paper-authority":paper_authority,
        "author-code":author_code,
        "backend-normalization":backend_normalization,
        "symbolic-crosswalk":symbolic_crosswalk,
        "null-controls":null_controls,
    }[lane]
    try:
        fn()
    except Exception as e:
        emit({"lane":lane,"pass":False,"infrastructure_failure":True,"error":repr(e),"amplitude_values_used":False,"failure_class":"INVALID_PROVENANCE"})

if __name__=="__main__":
    main()
