#!/usr/bin/env python3
import argparse
import hashlib
import json
import pathlib
import re
import urllib.request
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "out" / "iter052"
OUT.mkdir(parents=True, exist_ok=True)

AUTHOR_COMMIT = "84b375f2a2e0d29b44dd8820953553624bb007a3"
BACKEND_COMMIT = "052e4346028870bd76f69a3034e6cae8defb8f7f"

AUTHOR_VERTEX_URL = f"https://raw.githubusercontent.com/PietropaoloFrisoni/Monte_Carlo_spinfoams/{AUTHOR_COMMIT}/src/vertex_renormalization_EPRL_MC.jl"
AUTHOR_UTIL_URL = f"https://raw.githubusercontent.com/PietropaoloFrisoni/Monte_Carlo_spinfoams/{AUTHOR_COMMIT}/src/utilities.jl"
BACKEND_VERTEX_URL = f"https://raw.githubusercontent.com/qg-cpt-marseille/sl2cfoam-next/{BACKEND_COMMIT}/src/vertex.c"
BACKEND_JULIA_URL = f"https://raw.githubusercontent.com/qg-cpt-marseille/sl2cfoam-next/{BACKEND_COMMIT}/julia/SL2Cfoam.jl"

EXPECTED_BLOBS = {
    AUTHOR_VERTEX_URL: "6b627f7c2329724b589947195edc7e5ee7c18bb1",
    AUTHOR_UTIL_URL: "7dddb9e34156264c2b599f74ed38853a2799ddb0",
    BACKEND_VERTEX_URL: "9581999f0d5d59155e8c912fc7f2f3c5a98b346e",
    BACKEND_JULIA_URL: "0c5486ea817bd8da5ab18479a62cf930770e3be4",
}

DATA_PATH = ROOT / "sources" / "ITER052_EQ11_ROUTING_DATA.json"
DATA_BLOB = "71c450514555feabd663b71942b1f5d693399cdc"

CROSSWALK = {
    "rBCl":"i1", "rBCr":"i2", "rABl":"i3", "rABr":"i4",
    "rAEl":"i5", "rAEr":"i6", "rbl":"i7", "rbr":"i8",
    "rCDl":"i9", "rCDr":"i10", "rIul":"i11", "rIur":"i12",
    "rIu":"i13", "rIbl":"i14", "rIbr":"i15",
}

AUTHOR_ORIGINAL_R = {
    "up": ["ib","rABr","rIul","rIur","rBCl"],
    "left": ["ib","rAEr","rIbl","rIu","rABl"],
    "bottom_left": ["ib","rbr","rIbr","rIul","rAEl"],
    "bottom_right": ["ib","rCDr","rIur","rIbl","rbl"],
    "right": ["ib","rBCr","rIu","rIbr","rCDl"],
}

PAIR_R = [
    ("rBCl","rBCr"), ("rABl","rABr"), ("rAEl","rAEr"),
    ("rbl","rbr"), ("rCDl","rCDr"),
]

AUTHOR_PRE_R = {
    "up": ["ib","rABr","rIul","rIur","rBCr"],
    "left": ["ib","rAEr","rIbl","rIu","rABr"],
    "bottom_left": ["ib","rbr","rIbr","rIul","rAEr"],
    "bottom_right": ["ib","rCDr","rIur","rIbl","rbr"],
    "right": ["ib","rBCr","rIu","rIbr","rCDr"],
}

COMMENT_SIGS = [
    "#r_u = ((0, 0), rABr[1], rIul[1], rIur[1], rBCl[1])",
    "#r_l = ((0, 0), rAEr[1], rIbl[1], rIu[1], rABl[1])",
    "#r_bl = ((0, 0), rbr[1], rIbr[1], rIul[1], rAEl[1])",
    "#r_br = ((0, 0), rCDr[1], rIur[1], rIbl[1], rbl[1])",
    "#r_r = ((0, 0), rBCr[1], rIu[1], rIbr[1], rCDl[1])",
]

SPIN_CALL_SIGS = [
    "v_u = vertex_compute([jb, jb, jb, jb, jpink, jblue, jbrightgreen, jpurple, jgrassgreen, jred], Dl; result=result_return)",
    "v_l = vertex_compute([jb, jb, jb, jb, jbrown, jdarkgreen, jpink, jorange, jblue, jbrightgreen], Dl; result=result_return)",
    "v_bl = vertex_compute([jb, jb, jb, jb, jviolet, jpurple, jbrown, jgrassgreen, jdarkgreen, jpink], Dl; result=result_return)",
    "v_br = vertex_compute([jb, jb, jb, jb, jred, jorange, jviolet, jblue, jpurple, jbrown], Dl; result=result_return)",
    "v_r = vertex_compute([jb, jb, jb, jb, jbrightgreen, jgrassgreen, jred, jdarkgreen, jorange, jviolet], Dl; result=result_return)",
]

PAIR_SIGS = [
    ("rBCl[2], rBCr[2]", "rBCl_intertw", "rBCr_intertw"),
    ("rABl[2], rABr[2]", "rABl_intertw", "rABr_intertw"),
    ("rAEl[2], rAEr[2]", "rAEl_intertw", "rAEr_intertw"),
    ("rbl[2], rbr[2]", "rbl_intertw", "rbr_intertw"),
    ("rCDl[2], rCDr[2]", "rCDl_intertw", "rCDr_intertw"),
]

SHAPE_SIGS = [
    "vertex_up_pre_contracted = zeros(rBCr[2], rIur[2], rIul[2], rABr[2], boundary_dim)",
    "vertex_left_pre_contracted = zeros(rABr[2], rIu[2], rIbl[2], rAEr[2], boundary_dim)",
    "vertex_bottom_left_pre_contracted = zeros(rAEr[2], rIul[2], rIbr[2], rbr[2], boundary_dim)",
    "vertex_bottom_right_pre_contracted = zeros(rbr[2], rIbl[2], rIur[2], rCDr[2], boundary_dim)",
    "vertex_right_pre_contracted = zeros(rCDr[2], rIbr[2], rIu[2], rBCr[2], boundary_dim)",
]

FINAL_SIGS = [
    "vertex_up_pre_contracted[rBC_index, rIur_index, rIul_index, rAB_index, ib_index]",
    "vertex_left_pre_contracted[rAB_index, rIu_index, rIbl_index, rAE_index, ib_index]",
    "vertex_bottom_left_pre_contracted[rAE_index, rIul_index, rIbr_index, rb_index, ib_index]",
    "vertex_bottom_right_pre_contracted[rb_index, rIbl_index, rIur_index, rCD_index, ib_index]",
    "vertex_right_pre_contracted[rCD_index, rIbr_index, rIu_index, rBC_index, ib_index]",
]


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def fetch_exact(url: str) -> str:
    with urllib.request.urlopen(url, timeout=30) as r:
        data = r.read()
    got = git_blob_sha(data)
    exp = EXPECTED_BLOBS[url]
    if got != exp:
        raise RuntimeError(f"blob mismatch {url}: {got} != {exp}")
    return data.decode("utf-8")


def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def to_i(vals):
    return [v if v == "ib" else CROSSWALK[v] for v in vals]


def degree_census(vertices, pairs):
    c = Counter()
    for vals in vertices.values():
        for x in vals:
            if x != "ib":
                c[x] += 1
    for a,b in pairs:
        c[a] += 1
        c[b] += 1
    return {f"i{n}": int(c[f"i{n}"]) for n in range(1,16)}


def emit(obj):
    (OUT / "evidence.json").write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")
    print(json.dumps(obj, indent=2, sort_keys=True))


def tex_authority():
    data_bytes = DATA_PATH.read_bytes()
    got_blob = git_blob_sha(data_bytes)
    d = json.loads(data_bytes)
    expected_literal = {
        "up":["ib","i4","i11","i12","i2"],
        "left":["ib","i6","i13","i14","i4"],
        "bottom_left":["ib","i8","i15","i11","i6"],
        "bottom_right":["ib","i10","i12","i14","i15"],
        "right":["ib","i2","i13","i15","i10"],
    }
    expected_pairs = [["i1","i2"],["i3","i4"],["i5","i6"],["i7","i8"],["i8","i10"]]
    checks = {
        "data_blob_match": got_blob == DATA_BLOB,
        "main_tex_sha_match": d["source"]["main_tex_sha256"] == "bff93f3a7857658264a04eb23521bb935a68eccb7760b284589ff5ec4073f063",
        "raw_artifact_digest_match": d["source"]["recovery_artifact_digest"] == "sha256:191262f0c2a6d5c5b3ac6f1036caacd6808735c4bc38ecc73c45da49b2c53cb9",
        "literal_vertices_match": d["literal_eq11_vertex_intertwiners"] == expected_literal,
        "literal_pairs_match": d["literal_eq11_6j_intertwiner_pairs"] == expected_pairs,
        "crosswalk_match": d["source_comment_crosswalk"] == CROSSWALK,
    }
    emit({"lane":"tex-authority","checks":checks,"pass":all(checks.values()),"failure_class":"INVALID_PROVENANCE" if not all(checks.values()) else None})


def author_code():
    src = fetch_exact(AUTHOR_VERTEX_URL)
    util = fetch_exact(AUTHOR_UTIL_URL)
    ns = normalize(src)
    comment = {s: s in src for s in COMMENT_SIGS}
    spins = {s: normalize(s) in ns for s in SPIN_CALL_SIGS}
    pairs = {}
    for dims,left,right in PAIR_SIGS:
        key=f"{left}->{right}"
        pairs[key] = dims in src and left in src and right in src
    shapes = {s: normalize(s) in ns for s in SHAPE_SIGS}
    finals = {s: normalize(s) in ns for s in FINAL_SIGS}
    util_checks = {
        "ordered_tensor_loop": "for i5 in axes(tensor_pre_contracted, 1), i4 in axes(tensor_pre_contracted, 2), i3 in axes(tensor_pre_contracted, 3), i2 in axes(tensor_pre_contracted, 4), i1 in axes(tensor_pre_contracted, 5)" in normalize(util),
        "left_to_right_axis_contraction": "original_tensor[k_r, i4, i3, i2, i1] * W6j_matrix[k_r, i5]" in normalize(util),
        "unit_intertwiner_index_step": "return tuple[1][1] + index - 1" in normalize(util),
    }
    all_checks = list(comment.values())+list(spins.values())+list(pairs.values())+list(shapes.values())+list(finals.values())+list(util_checks.values())
    emit({
        "lane":"author-code",
        "author_commit":AUTHOR_COMMIT,
        "comment_signatures":comment,
        "spin_call_signatures":spins,
        "pair_signatures":pairs,
        "shape_signatures":shapes,
        "final_contraction_signatures":finals,
        "utility_checks":util_checks,
        "pass":all(all_checks),
        "failure_class":"LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK_BLOCKED_SOURCE_AXIS_CONVENTION" if not all(all_checks) else None,
    })


def backend_axis():
    vc = fetch_exact(BACKEND_VERTEX_URL)
    jl = fetch_exact(BACKEND_JULIA_URL)
    nvc, njl = normalize(vc), normalize(jl)
    checks = {
        "c_tensor_axis_order_i5_to_i1": "TENSOR_CREATE(vertex, t_full, 5, i5_size, i4_size, i3_size, i2_size, i1_size);" in nvc,
        "julia_wrap_preserves_c_dims": "unsafe_wrap(Array, ctens.d, ctens.dims; own = false)" in njl,
        "single_amplitude_takes_five_intertwiners": "Computes a single vertex amplitude given 10 spins (j12, ...), 5 intertwiners (i1,...) and number of shells." in njl,
        "single_amplitude_passes_ordered_is": "ctwo.(js), ctwo.(is), Dl" in njl,
        "doubled_conversion": "ctwo(j) = trunc(Cint, twice(j))" in njl,
    }
    emit({"lane":"backend-axis","backend_commit":BACKEND_COMMIT,"checks":checks,"pass":all(checks.values()),"failure_class":"LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK_BLOCKED_SOURCE_AXIS_CONVENTION" if not all(checks.values()) else None})


def graph_incidence():
    orig_i = {k:to_i(v) for k,v in AUTHOR_ORIGINAL_R.items()}
    pair_i = [(CROSSWALK[a],CROSSWALK[b]) for a,b in PAIR_R]
    pre_i = {k:to_i(v) for k,v in AUTHOR_PRE_R.items()}
    deg = degree_census(orig_i,pair_i)
    degree2 = all(v == 2 for v in deg.values())
    replacements = {}
    names = list(AUTHOR_ORIGINAL_R)
    for name,(left,right) in zip(names,PAIR_R):
        before=AUTHOR_ORIGINAL_R[name]
        after=AUTHOR_PRE_R[name]
        replacements[name] = before[:-1] == after[:-1] and before[-1] == left and after[-1] == right
    emit({
        "lane":"graph-incidence",
        "author_original_i":orig_i,
        "pair_i":pair_i,
        "precontracted_i":pre_i,
        "degree_census":deg,
        "all_degree_two":degree2,
        "replacement_checks":replacements,
        "pass":degree2 and all(replacements.values()),
        "failure_class":"LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK_STRUCTURAL_FAIL" if not (degree2 and all(replacements.values())) else None,
    })


def null_controls():
    d=json.loads(DATA_PATH.read_text())
    literal=d["literal_eq11_vertex_intertwiners"]
    literal_pairs=[tuple(x) for x in d["literal_eq11_6j_intertwiner_pairs"]]
    lit_deg=degree_census(literal,literal_pairs)
    repaired_pairs=literal_pairs[:-1]+[("i9","i10")]
    rep_deg=degree_census(literal,repaired_pairs)

    # N3 preserves incidence but violates the exact ordered author-code signature.
    n3={k:list(v) for k,v in {k:to_i(v) for k,v in AUTHOR_ORIGINAL_R.items()}.items()}
    n3["left"]=["ib","i6","i13","i14","i3"]
    n3_deg=degree_census(n3,[(CROSSWALK[a],CROSSWALK[b]) for a,b in PAIR_R])

    src=fetch_exact(AUTHOR_VERTEX_URL)
    correct_left="#r_l = ((0, 0), rAEr[1], rIbl[1], rIu[1], rABl[1])"
    swapped_left="#r_l = ((0, 0), rAEr[1], rIu[1], rIbl[1], rABl[1])"
    checks={
        "N1_literal_fails_degree2": not all(v==2 for v in lit_deg.values()),
        "N1_i9_missing": lit_deg["i9"] == 0,
        "N2_6j_only_repair_still_fails_degree2": not all(v==2 for v in rep_deg.values()),
        "N3_preserves_degree2": all(v==2 for v in n3_deg.values()),
        "N3_correct_order_present": correct_left in src,
        "N3_swapped_order_absent": swapped_left not in src,
    }
    emit({
        "lane":"null-controls",
        "literal_degree_census":lit_deg,
        "sixj_only_repair_degree_census":rep_deg,
        "left_swap_degree_census":n3_deg,
        "checks":checks,
        "pass":all(checks.values()),
        "failure_class":"INVALID_IMPLEMENTATION" if not all(checks.values()) else None,
    })


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--lane",required=True,choices=["tex-authority","author-code","backend-axis","graph-incidence","null-controls"])
    lane=ap.parse_args().lane
    fn={
        "tex-authority":tex_authority,
        "author-code":author_code,
        "backend-axis":backend_axis,
        "graph-incidence":graph_incidence,
        "null-controls":null_controls,
    }[lane]
    try:
        fn()
    except Exception as e:
        emit({"lane":lane,"pass":False,"infrastructure_failure":True,"error":repr(e),"failure_class":"INVALID_PROVENANCE"})

if __name__ == "__main__":
    main()
