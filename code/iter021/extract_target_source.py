#!/usr/bin/env python3
import gzip
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import tarfile
import time
import urllib.request

OUT = Path('out')
OUT.mkdir(exist_ok=True)
ARXIV_ID = '1609.02429v2'
EXPECTED_SHA = '3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee'
UA = 'ISQGR-ITER021/1.0 source extraction'
SENTINELS = ['7.41492', '1.399277', '-1.931582', '-3.861564']


def fetch(url, attempts=5):
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:
            last = repr(e)
            time.sleep(2 * (i + 1))
    raise RuntimeError(f'fetch failed: {last}')


def unpack_source(data):
    files = {}
    try:
        with tarfile.open(fileobj=io.BytesIO(data), mode='r:*') as tf:
            for m in tf.getmembers():
                p = PurePosixPath(m.name)
                if p.is_absolute() or '..' in p.parts or not m.isfile():
                    continue
                if p.suffix.lower() not in {'.tex', '.sty', '.bib'}:
                    continue
                if m.size > 10_000_000:
                    continue
                f = tf.extractfile(m)
                if f is not None:
                    files[str(p)] = f.read().decode('utf-8', 'replace')
        if files:
            return files, 'tar'
    except tarfile.TarError:
        pass
    try:
        text = gzip.decompress(data).decode('utf-8', 'replace')
        return {'source.tex': text}, 'gzip-single'
    except Exception:
        pass
    return {'source.tex': data.decode('utf-8', 'replace')}, 'plain'


def context(text, pos, before=1800, after=3200):
    return text[max(0, pos-before):min(len(text), pos+after)]


def display_containing(text, pos):
    begins = []
    patterns = [
        (r'\\begin\{align\*?\}', r'\\end\{align\*?\}', 'align'),
        (r'\\begin\{equation\*?\}', r'\\end\{equation\*?\}', 'equation'),
        (r'\\begin\{gather\*?\}', r'\\end\{gather\*?\}', 'gather'),
        (r'\\ba\b', r'\\ea\b', 'ba'),
        (r'\\be\b', r'\\ee\b', 'be'),
        (r'\\bea\b', r'\\eea\b', 'bea'),
    ]
    for bp, ep, kind in patterns:
        for m in re.finditer(bp, text[:pos+1]):
            begins.append((m.start(), ep, kind))
    for start, ep, kind in sorted(begins, reverse=True)[:80]:
        em = re.search(ep, text[start:])
        if em:
            end = start + em.end()
            if start <= pos <= end:
                return text[start:end], start, end, kind
    return None


def section_blocks(text):
    ms = list(re.finditer(r'\\(?:sub)*section\*?\{([^}]*)\}', text, re.I))
    out = []
    for i, m in enumerate(ms):
        end = ms[i+1].start() if i+1 < len(ms) else len(text)
        out.append({'title': m.group(1), 'start': m.start(), 'end': end, 'text': text[m.start():end]})
    return out


def appendix_candidates(files):
    # Preserve any section whose title or content carries the known Appendix topics.
    keys = {
        'A': ['quantum group', 'su(2)_k', 'quantum group conventions'],
        'B': ['clebsch', 'graphical calculus', 'graphical identities', 'cups', 'caps'],
        'E': ['normalization', 'normalisation', 'eprl map'],
        'F': ['eprl', 'r-matrix', 'r matrix'],
    }
    found = {k: [] for k in keys}
    for name, text in files.items():
        for sec in section_blocks(text):
            title = sec['title'].lower()
            low = sec['text'].lower()
            for key, needles in keys.items():
                score = sum((n in title) for n in needles) * 4 + sum((n in low) for n in needles)
                # Prefer appendix-looking sections with equation/graph content.
                if score >= 2 and ('tikzpicture' in low or '\\label{' in sec['text'] or '\\begin{equation' in low):
                    found[key].append({'file': name, 'title': sec['title'], 'score': score, 'start': sec['start'], 'end': sec['end'], 'text': sec['text']})
    for key in found:
        found[key].sort(key=lambda x: x['score'], reverse=True)
    return found


def main():
    try:
        data = fetch(f'https://export.arxiv.org/e-print/{ARXIV_ID}')
        h = hashlib.sha256(data).hexdigest()
        files, packing = unpack_source(data)
        if h != EXPECTED_SHA:
            ev = {'stage':'source-extraction','infrastructure_failure':False,'provenance_mismatch':True,
                  'expected_sha256':EXPECTED_SHA,'fresh_sha256':h,'pass':False}
            (OUT/'evidence.json').write_text(json.dumps(ev, indent=2, sort_keys=True)+'\n')
            print(json.dumps(ev, indent=2, sort_keys=True))
            return

        eq27 = []
        for name, text in files.items():
            for m in re.finditer(r'\\label\{eq:eprl-3-valent\}', text):
                disp = display_containing(text, m.start())
                eq27.append({'file':name,'pos':m.start(),'context':context(text,m.start()),
                             'display': disp[0] if disp else None,
                             'display_kind': disp[3] if disp else None})

        sent = {}
        for s in SENTINELS:
            hits=[]
            variants = [s, s.replace('-', ' -'), s.replace('-', '$-$')]
            for name, text in files.items():
                for v in variants:
                    start=0
                    while True:
                        p=text.find(v,start)
                        if p < 0: break
                        hits.append({'file':name,'pos':p,'matched':v,'context':context(text,p,2200,4200)})
                        start=p+len(v)
            # de-duplicate same positions from variants
            uniq={(x['file'],x['pos']):x for x in hits}
            sent[s]=list(uniq.values())

        apps = appendix_candidates(files)

        # Write immutable extracted payloads for downstream jobs.
        if len(eq27)==1 and eq27[0]['display']:
            (OUT/'eq27_exact.tex').write_text(eq27[0]['display'])
            (OUT/'eq27_context.tex').write_text(eq27[0]['context'])

        app_manifest={}
        for key, rows in apps.items():
            app_manifest[key]=[]
            for i,row in enumerate(rows[:4]):
                fn=f'appendix_{key}_candidate_{i}.tex'
                (OUT/fn).write_text(row['text'])
                app_manifest[key].append({'file':row['file'],'title':row['title'],'score':row['score'],'artifact':fn,
                                          'labels':re.findall(r'\\label\{([^}]+)\}',row['text'])[:80]})

        sentinel_manifest={}
        for s,hits in sent.items():
            sentinel_manifest[s]=[]
            safe=s.replace('-','m').replace('.','p')
            for i,row in enumerate(hits[:10]):
                fn=f'sentinel_{safe}_{i}.tex'
                (OUT/fn).write_text(row['context'])
                sentinel_manifest[s].append({'file':row['file'],'pos':row['pos'],'matched':row['matched'],'artifact':fn})

        # Additional targeted context searches for lambda/l=3 and k=12.
        target_contexts=[]
        pats=[r'lambda',r'\\lambda',r'l\s*=\s*3',r'k\s*=\s*12',r'k=12']
        for name,text in files.items():
            low=text.lower()
            for pat in pats:
                for m in list(re.finditer(pat, low, re.I))[:20]:
                    c=context(text,m.start(),1800,3600)
                    if ('eprl' in c.lower() or 'alpha' in c.lower() or any(s in c for s in SENTINELS)):
                        target_contexts.append({'file':name,'pattern':pat,'pos':m.start(),'context':c})
        for i,row in enumerate(target_contexts[:40]):
            fn=f'lambda_k12_context_{i}.tex'; (OUT/fn).write_text(row['context']); row['artifact']=fn; row.pop('context')

        pass_pred = (
            len(eq27)==1 and bool(eq27[0]['display']) and
            all(len(sent[s])>=1 for s in SENTINELS) and
            all(len(apps[k])>=1 for k in ['A','B','E','F'])
        )
        ev={
            'stage':'source-extraction','source':ARXIV_ID,'fresh_sha256':h,'expected_sha256':EXPECTED_SHA,
            'packing':packing,'source_file_count':len(files),'eq27_hits':len(eq27),
            'eq27_unique_display':len(eq27)==1 and bool(eq27[0]['display']),
            'eq27_file':eq27[0]['file'] if len(eq27)==1 else None,
            'appendix_candidates':app_manifest,'sentinels':sentinel_manifest,
            'lambda_k12_contexts':target_contexts,
            'pass':bool(pass_pred)
        }
        (OUT/'evidence.json').write_text(json.dumps(ev, indent=2, sort_keys=True)+'\n')
        print(json.dumps(ev, indent=2, sort_keys=True))
    except Exception as e:
        ev={'stage':'source-extraction','infrastructure_failure':True,'scientific_negative':False,'error':repr(e),'pass':False}
        (OUT/'evidence.json').write_text(json.dumps(ev, indent=2, sort_keys=True)+'\n')
        print(json.dumps(ev, indent=2, sort_keys=True))

if __name__=='__main__':
    main()
