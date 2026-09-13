#!/usr/bin/env python3
"""ITER018 corrected audit worker.

This file intentionally leaves the first production run immutable.  It fixes two
observed parser defects only: (1) a false-negative q-number lexical predicate in
the independent SU(2)_k source, and (2) a selector that chose Eq.(24) instead of
the equation following the exact Eq.(27) prose anchor.  No physics acceptance
criterion is weakened.
"""
import argparse, json, pathlib, re, shutil, subprocess
import parallel_audit as v1

OUT = v1.OUT


def next_display_environment(text, pos, max_window=50000):
    tail = text[pos:pos+max_window]
    starts = []
    pats = [
        (r"\\begin\{equation\*?\}", "equation"),
        (r"\\begin\{align\*?\}", "align"),
        (r"\\be\b", "be"),
        (r"\\ba\b", "ba"),
        (r"\\bea\b", "bea"),
    ]
    for pat, kind in pats:
        m = re.search(pat, tail)
        if m:
            starts.append((m.start(), m.group(0), kind))
    if not starts:
        return None
    rel, marker, kind = min(starts, key=lambda x: x[0])
    start = pos + rel
    sub = text[start:start+max_window]
    end_pat = {
        "equation": r"\\end\{equation\*?\}",
        "align": r"\\end\{align\*?\}",
        "be": r"\\ee\b",
        "ba": r"\\ea\b",
        "bea": r"\\eea\b",
    }[kind]
    em = re.search(end_pat, sub)
    if not em:
        return None
    end = start + em.end()
    return text[start:end], start, end, marker


def lane_eq27():
    aid = "1609.02429v2"
    src, _ = v1.fetch(f"https://export.arxiv.org/e-print/{aid}")
    files, packing = v1.safe_tex_members(src)
    source_hash = v1.sha(src)

    anchor_re = re.compile(
        r"derivations\s+of\s+the\s+normali[sz]ation\s+and\s+the\s+diagrams\s+respectively",
        re.I,
    )
    hits = []
    for name, text in files.items():
        for m in anchor_re.finditer(text):
            env = next_display_environment(text, m.end())
            if env:
                snippet, s, e, marker = env
                hits.append({"file": name, "anchor_start": m.start(), "anchor_end": m.end(),
                             "marker": marker, "snippet": snippet, "start": s, "end": e})

    chosen = hits[0] if len(hits) == 1 else None
    if chosen:
        (OUT/"eq27_source_exact.tex").write_text(chosen["snippet"], encoding="utf-8")
        t = files[chosen["file"]]
        (OUT/"eq27_source_context.tex").write_text(
            t[max(0, chosen["anchor_start"]-800):min(len(t), chosen["end"]+1600)], encoding="utf-8")

    pdf, _ = v1.fetch(f"https://arxiv.org/pdf/{aid}")
    pdf_path = OUT/f"{aid}.pdf"
    pdf_path.write_bytes(pdf)
    p22 = ""
    p37 = ""
    p38 = ""
    if shutil.which("pdftotext"):
        for p, target in [(22,"eq27_page22.txt"),(37,"appendixE_page37.txt"),(38,"appendixF_page38.txt")]:
            subprocess.run(["pdftotext","-f",str(p),"-l",str(p),str(pdf_path),str(OUT/target)], check=False)
        if (OUT/"eq27_page22.txt").exists(): p22=(OUT/"eq27_page22.txt").read_text(errors="replace")
        if (OUT/"appendixE_page37.txt").exists(): p37=(OUT/"appendixE_page37.txt").read_text(errors="replace")
        if (OUT/"appendixF_page38.txt").exists(): p38=(OUT/"appendixF_page38.txt").read_text(errors="replace")
    rendered = {}
    if shutil.which("pdftoppm"):
        for p, base in [(22,"eq27_page22"),(37,"appendixE_page37"),(38,"appendixF_page38")]:
            subprocess.run(["pdftoppm","-f",str(p),"-l",str(p),"-png","-r","170","-singlefile",str(pdf_path),str(OUT/base)], check=False)
            rendered[str(p)] = (OUT/f"{base}.png").exists()

    snippet = chosen["snippet"] if chosen else ""
    exact_anchor_unique = len(hits) == 1
    source_graph_signal = (
        exact_anchor_unique and "eprl" in snippet.lower() and
        snippet.count("tikzpicture") >= 2 and snippet.count("\\draw") >= 10 and
        ("alpha" in snippet.lower() or "\\alpha" in snippet) and "\\sum" in snippet
    )
    pdf_eq27 = "(27)" in p22 and "normalization" in p22.lower() and "eprl" in p22.lower()
    appendix_e = "graphical identities" in p37.lower() and "appendix b" in p37.lower() and "(e3)" in p37.lower()
    appendix_f = "identities (b15)" in p38.lower() and "(f1)" in p38.lower() and "r matrices" in p38.lower()
    mech_pass = bool(source_graph_signal and pdf_eq27 and all(rendered.get(str(p), False) for p in (22,37,38)) and appendix_e and appendix_f)

    ev = {
        "lane":"eq27-graph", "worker":"v2", "source":aid,
        "eprint_sha256":source_hash, "packing":packing, "tex_file_count":len(files),
        "exact_prose_anchor_hits":len(hits), "exact_prose_anchor_unique":exact_anchor_unique,
        "chosen_file": chosen["file"] if chosen else None,
        "chosen_marker": chosen["marker"] if chosen else None,
        "source_graph_signal":source_graph_signal,
        "snippet_draw_count": snippet.count("\\draw"), "snippet_tikz_count":snippet.count("tikzpicture"),
        "pdf_sha256":v1.sha(pdf), "pdf_page22_text_confirms_eq27":pdf_eq27,
        "pdf_pages_rendered":rendered,
        "appendixE_graphical_B_to_E3_text_confirmed":appendix_e,
        "appendixF_B15_to_F1_Rmatrix_text_confirmed":appendix_f,
        "mechanical_recovery_pass":mech_pass,
        "scientific_topology_interpretation":"SOURCE_GRAPH_AND_RENDER_REVIEW_REQUIRED_BEFORE_FINAL_PROMOTION"
    }
    v1.write_json(ev)
    (OUT/"evidence.md").write_text("# Lane A v2 - exact Eq27 source graph\n\n```json\n"+json.dumps(ev,indent=2)+"\n```\n", encoding="utf-8")


def lane_evenk():
    aid = "2304.02527v2"
    src, _ = v1.fetch(f"https://export.arxiv.org/e-print/{aid}")
    files, packing = v1.safe_tex_members(src)
    alltex = "\n".join(files.values())
    low = alltex.lower()

    p_positive = "positive integer" in low
    p_q = bool(re.search(r"q\s*=\s*e\s*\^?\s*\{?\s*2\\?pi\s*i\s*/\s*\(?k\+2\)?", alltex, re.I)) or (p_positive and "root of unity" in low and "k+2" in alltex)
    p_labels = bool(re.search(r"k\s*/\s*2|\\frac\{k\}\{2\}", alltex))
    p_cutoff = bool(re.search(r"j_?\{?1\}?\s*\+\s*j_?\{?2\}?\s*\+\s*j_?\{?3\}?.{0,100}(?:\\leq|<=)\s*k", alltex, re.S)) or ("fusion" in low and "k" in alltex)
    # Formula-level predicate: the supplemental source explicitly defines [n] using q^(+/- n/2)
    # and, equivalently, a sine ratio with k+2.  No lexical phrase "q-number" is required.
    qn_formula = bool(re.search(r"\[n\].{0,500}q.{0,120}n\s*/\s*2", alltex, re.S|re.I))
    qn_sine = bool(re.search(r"sin.{0,160}n.{0,160}k\s*\+\s*2", alltex, re.S|re.I))
    p_qnum = qn_formula and (qn_sine or "k+2" in alltex)
    p_f = ("f-matri" in low or "f--matri" in low) and ("6j" in low or "6 j" in low)
    p_ortho = "orthogonality" in low and ("f-matri" in low or "f--matri" in low)
    p_real = (("all $f$" in low or "all f" in low) and "real" in low)
    odd_k = bool(re.search(r"k.{0,40}(odd|uneven)|(?:odd|uneven).{0,40}k", low, re.S))
    category_pass = all([p_q,p_positive,p_labels,p_cutoff,p_qnum,p_f,p_ortho]) and not odd_k

    ev = {"lane":"evenk-category","worker":"v2","source":aid,"eprint_sha256":v1.sha(src),"packing":packing,"tex_file_count":len(files),
          "positive_integer_k":p_positive,"q_root_k_plus_2":p_q,"labels_through_k_over_2":p_labels,"fusion_cutoff":p_cutoff,
          "q_number_formula_signal":qn_formula,"q_number_sine_signal":qn_sine,"q_number_convention":p_qnum,
          "f_matrix_q6j":p_f,"f_orthogonality":p_ortho,"f_reality_text":p_real,
          "odd_k_restriction_detected":odd_k,"category_even_k_pass":category_pass,
          "k12_within_declared_domain":bool(category_pass and p_positive),
          "qcg_component_phase_authority":False,"scope":"independent even-k category/fusion cross-check; not q-CG component phase authority"}
    v1.write_json(ev)
    contexts=[]
    for pat in ["positive integer","fusion","orthogonality","[n]"]:
        p=low.find(pat.lower())
        if p>=0: contexts.append(alltex[max(0,p-1400):p+2600])
    (OUT/"evenk_contexts.tex").write_text("\n\n%%%% CONTEXT %%%%\n\n".join(contexts),encoding="utf-8")
    (OUT/"evidence.md").write_text("# Lane B v2 - independent even-k category audit\n\n```json\n"+json.dumps(ev,indent=2)+"\n```\n",encoding="utf-8")


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--lane",required=True,choices=["eq27-graph","evenk-category","provenance"]); a=ap.parse_args()
    try:
        if a.lane == "eq27-graph": lane_eq27()
        elif a.lane == "evenk-category": lane_evenk()
        else: v1.lane_provenance()
    except Exception as e:
        ev={"lane":a.lane,"worker":"v2","infrastructure_failure":True,"error":repr(e),"scientific_negative":False}
        v1.write_json(ev)
        (OUT/"evidence.md").write_text("# Lane infrastructure failure\n\n```json\n"+json.dumps(ev,indent=2)+"\n```\n",encoding="utf-8")

if __name__ == "__main__": main()
