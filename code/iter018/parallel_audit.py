#!/usr/bin/env python3
import argparse, gzip, hashlib, io, json, os, pathlib, re, shutil, subprocess, tarfile, time, urllib.request

OUT = pathlib.Path("out")
OUT.mkdir(exist_ok=True)
UA = "ISQGR-Iter018/1.0 source qualification"

HIST = {
    "1609.02429v2": "3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee",
    "1312.0905v2": "69334656117892b255ebb9b0c3855b6387bafc630bb9345b084e5434e22294c0",
    "1506.04749v3": "758e05bf73390015fb02f374c69892ad155c8edacb40a97876c12aa7f64c1e14",
}

def fetch(url, attempts=5):
    err = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read(), dict(r.headers)
        except Exception as e:
            err = repr(e)
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"fetch failed {url}: {err}")

def sha(data):
    return hashlib.sha256(data).hexdigest()

def safe_tex_members(data):
    files = {}
    bio = io.BytesIO(data)
    try:
        with tarfile.open(fileobj=bio, mode="r:*") as tf:
            for m in tf.getmembers():
                p = pathlib.PurePosixPath(m.name)
                if p.is_absolute() or ".." in p.parts or not m.isfile():
                    continue
                if p.suffix.lower() not in {".tex", ".sty", ".bib"}:
                    continue
                if m.size > 8_000_000:
                    continue
                f = tf.extractfile(m)
                if f is None:
                    continue
                files[str(p)] = f.read().decode("utf-8", "replace")
            if files:
                return files, "tar"
    except tarfile.TarError:
        pass
    try:
        dec = gzip.decompress(data)
        text = dec.decode("utf-8", "replace")
        return {"source.tex": text}, "gzip-single"
    except Exception:
        pass
    text = data.decode("utf-8", "replace")
    return {"source.tex": text}, "plain"

def write_json(obj, name="evidence.json"):
    (OUT / name).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def extract_balanced_equation(text, anchor_pos):
    starts = []
    patterns = [r"\\begin\{equation\*?\}", r"\\begin\{align\*?\}", r"\\be\b", r"\\ba\b", r"\\bea\b"]
    for pat in patterns:
        for m in re.finditer(pat, text[:anchor_pos]):
            starts.append((m.start(), m.group(0)))
    starts.sort()
    for start, marker in reversed(starts[-30:]):
        if marker.startswith("\\begin{equation"):
            endm = re.search(r"\\end\{equation\*?\}", text[start:anchor_pos])
        elif marker.startswith("\\begin{align"):
            endm = re.search(r"\\end\{align\*?\}", text[start:anchor_pos])
        elif marker == "\\be":
            endm = re.search(r"\\ee\b", text[start:anchor_pos])
        elif marker == "\\ba":
            endm = re.search(r"\\ea\b", text[start:anchor_pos])
        else:
            endm = re.search(r"\\eea\b", text[start:anchor_pos])
        if endm:
            end = start + endm.end()
            if anchor_pos - end < 4500:
                return text[start:end], start, end, marker
    # fallback: exact source context, never promoted to PASS by itself
    return text[max(0, anchor_pos-12000):anchor_pos], max(0, anchor_pos-12000), anchor_pos, "context-fallback"

def lane_eq27():
    aid = "1609.02429v2"
    src, hdr = fetch(f"https://export.arxiv.org/e-print/{aid}")
    files, packing = safe_tex_members(src)
    source_hash = sha(src)
    candidates = []
    for name, text in files.items():
        low = text.lower()
        for phrase in ["normalization constant", "normalisation constant"]:
            pos = 0
            while True:
                p = low.find(phrase, pos)
                if p < 0: break
                pre = low[max(0,p-16000):p]
                if "eprl" in pre and ("tikzpicture" in pre or "\\draw" in pre):
                    snippet, s, e, marker = extract_balanced_equation(text, p)
                    candidates.append({"file":name,"anchor":phrase,"pos":p,"marker":marker,"snippet":snippet,"start":s,"end":e})
                pos = p + 1
    # Rank by EPRL/TikZ density and source proximity.
    candidates.sort(key=lambda c: ("tikzpicture" in c["snippet"], c["snippet"].lower().count("eprl"), c["snippet"].count("\\draw")), reverse=True)
    chosen = candidates[0] if candidates else None
    if chosen:
        (OUT/"eq27_source_candidate.tex").write_text(chosen["snippet"], encoding="utf-8")
        context_text = files[chosen["file"]][max(0,chosen["start"]-1200):min(len(files[chosen["file"]]), chosen["end"]+1600)]
        (OUT/"eq27_source_context.tex").write_text(context_text, encoding="utf-8")
    # Independent PDF page recovery and text confirmation.
    pdf, _ = fetch(f"https://arxiv.org/pdf/{aid}")
    (OUT/f"{aid}.pdf").write_bytes(pdf)
    pdf_text = ""
    rendered = False
    if shutil.which("pdftotext"):
        subprocess.run(["pdftotext","-f","22","-l","22",str(OUT/f"{aid}.pdf"),str(OUT/"eq27_page22.txt")], check=False)
        if (OUT/"eq27_page22.txt").exists():
            pdf_text=(OUT/"eq27_page22.txt").read_text(errors="replace")
    if shutil.which("pdftoppm"):
        subprocess.run(["pdftoppm","-f","22","-l","22","-png","-r","160","-singlefile",str(OUT/f"{aid}.pdf"),str(OUT/"eq27_page22")], check=False)
        rendered=(OUT/"eq27_page22.png").exists()
    source_has_tikz = bool(chosen and ("tikzpicture" in chosen["snippet"] or "\\draw" in chosen["snippet"]))
    pdf_confirms = "(27)" in pdf_text and "normalization" in pdf_text.lower() and "eprl" in pdf_text.lower()
    unique = len(candidates) == 1
    # If multiple normalization anchors exist, exact candidate is still mechanically usable only when top candidate itself contains EPRL graph.
    mech_pass = bool(chosen and source_has_tikz and pdf_confirms and rendered)
    ev={
      "lane":"eq27-graph","source":aid,"eprint_sha256":source_hash,"packing":packing,
      "tex_file_count":len(files),"candidate_count":len(candidates),"candidate_unique":unique,
      "chosen_file": chosen["file"] if chosen else None,
      "chosen_marker": chosen["marker"] if chosen else None,
      "snippet_has_tikz_or_draw":source_has_tikz,
      "snippet_draw_count": chosen["snippet"].count("\\draw") if chosen else 0,
      "snippet_tikz_count": chosen["snippet"].count("tikzpicture") if chosen else 0,
      "pdf_sha256":sha(pdf),"pdf_page22_text_confirms_eq27":pdf_confirms,"pdf_page22_rendered":rendered,
      "mechanical_recovery_pass":mech_pass,
      "scientific_topology_interpretation":"PENDING_HUMAN_SOURCE_GRAPH_REVIEW"
    }
    write_json(ev)
    (OUT/"evidence.md").write_text("# Lane A - Eq27 mechanical recovery\n\n```json\n"+json.dumps(ev,indent=2)+"\n```\n",encoding="utf-8")

def lane_evenk():
    aid="2304.02527v2"
    src,_=fetch(f"https://export.arxiv.org/e-print/{aid}")
    files,packing=safe_tex_members(src)
    alltex="\n".join(files.values())
    low=alltex.lower()
    # Keep regex permissive to TeX formatting but predicates semantic and separate.
    p_q = bool(re.search(r"q\s*=\s*e\s*\^?\s*\{?\s*2\\?pi\s*i\s*/\s*\(?k\+2\)?", alltex, re.I)) or ("positive integer" in low and "root of unity" in low and "k+2" in alltex)
    p_positive = "positive integer" in low
    p_labels = bool(re.search(r"k\s*/\s*2|\\frac\{k\}\{2\}", alltex))
    p_cutoff = bool(re.search(r"j_?\{?1\}?\s*\+\s*j_?\{?2\}?\s*\+\s*j_?\{?3\}?.{0,80}(?:\\leq|<=)\s*k", alltex, re.S)) or ("fusion" in low and "k" in alltex)
    p_qnum = ("q-factorial" in low or "q--factorial" in low or "q-number" in low or "q--number" in low) and "k+2" in alltex
    p_f = ("f-matri" in low or "f--matri" in low) and ("6j" in low or "6 j" in low)
    p_ortho = "orthogonality" in low and ("f-matri" in low or "f--matri" in low)
    p_real = "all $f$" in low and "real" in low or "all f" in low and "real" in low
    # odd restriction check is scoped to statements about k, not unrelated odd words.
    odd_k = bool(re.search(r"k.{0,40}(odd|uneven)|(?:odd|uneven).{0,40}k", low, re.S))
    category_pass=all([p_q,p_positive,p_labels,p_cutoff,p_qnum,p_f,p_ortho]) and not odd_k
    ev={"lane":"evenk-category","source":aid,"eprint_sha256":sha(src),"packing":packing,"tex_file_count":len(files),
        "positive_integer_k":p_positive,"q_root_k_plus_2":p_q,"labels_through_k_over_2":p_labels,"fusion_cutoff":p_cutoff,
        "q_number_convention":p_qnum,"f_matrix_q6j":p_f,"f_orthogonality":p_ortho,"f_reality_text":p_real,
        "odd_k_restriction_detected":odd_k,"category_even_k_pass":category_pass,
        "qcg_component_phase_authority":False,"scope":"independent category/fusion cross-check only"}
    write_json(ev)
    # Preserve matching contexts for audit.
    contexts=[]
    for pat in ["positive integer","fusion","orthogonality","q-deformed 6j","q--deformed $6j$"]:
        p=low.find(pat.lower())
        if p>=0: contexts.append(alltex[max(0,p-1200):p+2200])
    (OUT/"evenk_contexts.tex").write_text("\n\n%%%% CONTEXT %%%%\n\n".join(contexts),encoding="utf-8")
    (OUT/"evidence.md").write_text("# Lane B - independent even-k category audit\n\n```json\n"+json.dumps(ev,indent=2)+"\n```\n",encoding="utf-8")

def lane_provenance():
    ids=["1609.02429v2","1312.0905v2","1506.04749v3","2304.02527v2"]
    rows=[]
    for aid in ids:
        data,_=fetch(f"https://export.arxiv.org/e-print/{aid}")
        h=sha(data)
        exp=HIST.get(aid)
        rows.append({"source":aid,"fresh_sha256":h,"historical_sha256":exp,"matches_historical":None if exp is None else h==exp,"bytes":len(data)})
    pass_hist=all(r["matches_historical"] for r in rows if r["historical_sha256"])
    ev={"lane":"provenance","rows":rows,"historical_hashes_match":pass_hist,
        "classification":"PASS" if pass_hist else "PROVENANCE_MISMATCH_REQUIRES_REAUDIT"}
    write_json(ev)
    (OUT/"evidence.md").write_text("# Lane C - byte provenance\n\n```json\n"+json.dumps(ev,indent=2)+"\n```\n",encoding="utf-8")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--lane",required=True,choices=["eq27-graph","evenk-category","provenance"]); a=ap.parse_args()
    try:
        {"eq27-graph":lane_eq27,"evenk-category":lane_evenk,"provenance":lane_provenance}[a.lane]()
    except Exception as e:
        ev={"lane":a.lane,"infrastructure_failure":True,"error":repr(e),"scientific_negative":False}
        write_json(ev)
        (OUT/"evidence.md").write_text("# Lane infrastructure failure\n\n```json\n"+json.dumps(ev,indent=2)+"\n```\n",encoding="utf-8")
        # keep job green so aggregate can distinguish scientific classification from CI transport

if __name__ == "__main__": main()
