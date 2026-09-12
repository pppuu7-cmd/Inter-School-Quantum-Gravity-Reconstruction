#!/usr/bin/env python3
import argparse, hashlib, json, pathlib, re, sys

ENV_RE = re.compile(r"\\begin\{(?:equation\*?|align\*?|multline\*?|gather\*?)\}(.*?)\\end\{(?:equation\*?|align\*?|multline\*?|gather\*?)\}", re.S)
TOKEN_RE = re.compile(r"\\[A-Za-z]+|[A-Za-z]+(?:_[A-Za-z0-9{}]+)?|[0-9]+|[+\-*/=^_{}()\[\],]")

def sha256_file(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()

def load_tex(root):
    files=sorted(pathlib.Path(root).rglob('*.tex'))
    chunks=[]
    for p in files:
        try: t=p.read_text(encoding='utf-8',errors='replace')
        except Exception: continue
        chunks.append((str(p.relative_to(root)),t))
    return chunks

def norm(s):
    s=re.sub(r"(?<!\\)%.*", "", s)
    s=re.sub(r"\\(?:label|tag)\{[^}]*\}", "", s)
    s=re.sub(r"\s+", "", s)
    return s

def tokens(s): return TOKEN_RE.findall(norm(s))

def equations(chunks):
    out=[]
    for fn,t in chunks:
        for m in ENV_RE.finditer(t):
            pre=t[max(0,m.start()-1600):m.start()]
            post=t[m.end():min(len(t),m.end()+600)]
            out.append({'file':fn,'start':m.start(),'body':m.group(1),'context':pre+'\n'+post})
    return out

def classify_formula(e, kind):
    c=(e['context']+' '+e['body']).lower()
    if kind=='DED':
        key = bool(re.search(r"\bded\b|disconnected.*edge|one[- ]edge", c))
        other = bool(re.search(r"\bdld6\b|internal face", c))
    else:
        key = bool(re.search(r"\bdld6\b|\bdld\b|internal face", c))
        other = bool(re.search(r"\bded\b", c)) and not bool(re.search(r"\bdld6\b|\bdld\b", c))
    amp = bool(re.search(r"mathcal\s*\{?a\}?|\\a_|amplitude|w_", c))
    return key and amp and not other

def formula_lane(chunks, kind):
    eqs=equations(chunks)
    hits=[e for e in eqs if classify_formula(e,kind)]
    return {'kind':kind,'hit_count':len(hits),'unique':len(hits)==1,
            'hits':[{'file':h['file'],'start':h['start'],'norm_sha256':hashlib.sha256(norm(h['body']).encode()).hexdigest(),
                     'tokens':tokens(h['body'])} for h in hits[:8]]}

def find_jf(s):
    pats=[r"j_\{?f\}?",r"j_f",r"j\^f"]
    return sorted(set(x.group(0) for p in pats for x in re.finditer(p,s)))

def reduction(chunks):
    d=formula_lane(chunks,'DED'); l=formula_lane(chunks,'DLD6')
    jf=[]; explicit=[]
    if l['unique']:
        eq=[e for e in equations(chunks) if classify_formula(e,'DLD6')][0]
        jf=find_jf(eq['body'])
        c=eq['context']+' '+eq['body']
        explicit=re.findall(r".{0,90}j_?\{?f\}?\s*=\s*0.{0,140}",c,flags=re.I|re.S)[:8]
    # Frozen conservative rule: source must explicitly state jf=0 reduction and both formulae be unique.
    # No inferred permutation or normalization is allowed.
    mapping_unique=bool(d['unique'] and l['unique'] and len(jf)==1 and explicit)
    reduced_isomorphic=False
    unresolved=[]
    if not d['unique']: unresolved.append('DED_formula_not_unique')
    if not l['unique']: unresolved.append('DLD6_formula_not_unique')
    if len(jf)!=1: unresolved.append('internal_face_spin_not_unique')
    if not explicit: unresolved.append('no_explicit_source_jf0_reduction_identity')
    if mapping_unique:
        unresolved.append('boundary_label_preserving_isomorphism_not_source_explicit')
        mapping_unique=False
    return {'ded':d,'dld6':l,'jf_spellings':jf,'explicit_jf0_contexts':explicit,
            'mapping_unique':mapping_unique,'reduced_isomorphic':reduced_isomorphic,'unresolved':unresolved}

def context_control(chunks):
    hits={'DED':[],'DLD6':[]}
    for fn,t in chunks:
        low=t.lower()
        for kind,pat in [('DED',r'\bded\b'),('DLD6',r'\bdld6\b|\bdld\b')]:
            for m in re.finditer(pat,low):
                w=t[max(0,m.start()-700):min(len(t),m.end()+1300)]
                if re.search(r'amplitude|\\mathcal|\\sum|internal face',w,re.I):
                    hits[kind].append({'file':fn,'offset':m.start(),'window_sha256':hashlib.sha256(norm(w).encode()).hexdigest()})
    return {'context_hits':hits,'ded_context_present':bool(hits['DED']),'dld_context_present':bool(hits['DLD6'])}

def lane(args):
    chunks=load_tex(args.source_dir)
    if not chunks: raise RuntimeError('no TeX source files found')
    base={'lane':args.lane,'source_version':'1801.03771v2','tar_sha256':sha256_file(args.source_tar),'tex_file_count':len(chunks)}
    if args.lane=='ded_formula_ast': base['result']=formula_lane(chunks,'DED')
    elif args.lane=='dld6_formula_ast': base['result']=formula_lane(chunks,'DLD6')
    elif args.lane=='jf0_reduction': base['result']=reduction(chunks)
    elif args.lane=='independent_context_control': base['result']=context_control(chunks)
    else: raise ValueError(args.lane)
    pathlib.Path(args.output).write_text(json.dumps(base,indent=2,sort_keys=True),encoding='utf-8')

def aggregate(args):
    docs=[]
    for p in sorted(pathlib.Path(args.input_dir).rglob('*.json')):
        try:
            d=json.loads(p.read_text());
            if 'lane' in d: docs.append(d)
        except Exception: pass
    by={d['lane']:d for d in docs}
    required=['ded_formula_ast','dld6_formula_ast','jf0_reduction','independent_context_control']
    missing=[x for x in required if x not in by]
    hashes=sorted(set(d.get('tar_sha256') for d in docs))
    infra=bool(missing or len(hashes)!=1 or any(d.get('source_version')!='1801.03771v2' for d in docs))
    if infra:
        cls='INFRASTRUCTURE_OR_PARSE_FAIL'
    else:
        ded=by['ded_formula_ast']['result']; dld=by['dld6_formula_ast']['result']; red=by['jf0_reduction']['result']; ctl=by['independent_context_control']['result']
        source_objects=ded.get('unique') and dld.get('unique') and ctl.get('ded_context_present') and ctl.get('dld_context_present')
        if source_objects and red.get('mapping_unique') and red.get('reduced_isomorphic'):
            cls='PASS_SOURCE_ALGEBRAIC_ZERO_FACE_COLLAPSE_OBJECT_QUALIFIED'
        elif source_objects:
            cls='BLOCKED_SOURCE_ALGEBRAIC_ZERO_FACE_COLLAPSE_AMBIGUOUS'
        else:
            cls='BLOCKED_SOURCE_ALGEBRAIC_ZERO_FACE_COLLAPSE_AMBIGUOUS'
    out={'classification':cls,'lane_count':len(docs),'missing_lanes':missing,'tar_sha256s':hashes,
         'lanes':{k:v.get('result') for k,v in by.items()},'bridge_credit':0,
         'claim_locks':['NO_BRIDGE_DERIVED','NO_NEW_QG_THEORY_REQUIRED','NO_NEW_PHYSICS_FOUND','CANDIDATE_THEORY_UNFORMED']}
    pathlib.Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8')
    print(json.dumps({'classification':cls,'tar_sha256s':hashes,'missing':missing},sort_keys=True))

if __name__=='__main__':
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='mode',required=True)
    p=sub.add_parser('lane'); p.add_argument('--lane',required=True); p.add_argument('--source-dir',required=True); p.add_argument('--source-tar',required=True); p.add_argument('--output',required=True)
    q=sub.add_parser('aggregate'); q.add_argument('--input-dir',required=True); q.add_argument('--output',required=True)
    a=ap.parse_args(); lane(a) if a.mode=='lane' else aggregate(a)
