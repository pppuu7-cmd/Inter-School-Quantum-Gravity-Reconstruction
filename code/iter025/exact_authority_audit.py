#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import pathlib
import re
import sys
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code' / 'iter016'))
from source_decoder import decode_source, SourceDecodeError  # noqa: E402

OUT = ROOT / 'out' / 'iter025'
OUT.mkdir(parents=True, exist_ok=True)

SOURCES = {
    'target': {
        'arxiv': '1609.02429v2',
        'url': 'https://export.arxiv.org/e-print/1609.02429v2',
        'expected_sha256': '3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee',
    },
    'qspinnet': {
        'arxiv': '1312.0905v2',
        'url': 'https://export.arxiv.org/e-print/1312.0905v2',
        'expected_sha256': '69334656117892b255ebb9b0c3855b6387bafc630bb9345b084e5434e22294c0',
    },
    'wojtek': {
        'arxiv': '1311.1798v1',
        'url': 'https://export.arxiv.org/e-print/1311.1798v1',
        'expected_sha256': None,
    },
}

UA = {'User-Agent': 'ISQGR-ITER025-exact-authority-audit/1.0'}


def fetch(url: str, tries: int = 5) -> bytes:
    err = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as exc:  # transport classification happens in manifest
            err = exc
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(f'FETCH_FAILED:{url}:{err!r}')


def acquire(name: str) -> dict:
    meta = SOURCES[name]
    raw = fetch(meta['url'])
    sha = hashlib.sha256(raw).hexdigest()
    decoded = decode_source(raw)
    return {
        'name': name,
        'arxiv': meta['arxiv'],
        'url': meta['url'],
        'archive_sha256': sha,
        'expected_sha256': meta['expected_sha256'],
        'expected_hash_match': (sha == meta['expected_sha256']) if meta['expected_sha256'] else None,
        'transport': decoded.transport,
        'expanded_sha256': decoded.expanded_sha256,
        'warnings': list(decoded.warnings),
        'files': decoded.files,
    }


def line_context(source_name: str, path: str, text: str, start_line: int, end_line: int) -> dict:
    lines = text.splitlines()
    lo = max(1, start_line)
    hi = min(len(lines), end_line)
    snippet = '\n'.join(f'{i}: {lines[i-1]}' for i in range(lo, hi + 1))
    return {
        'source': source_name,
        'file': path,
        'start_line': lo,
        'end_line': hi,
        'snippet': snippet,
    }


def collect_hits(src: dict, patterns: list[tuple[str, str]], radius: int = 10, limit: int = 50) -> list[dict]:
    hits = []
    seen = set()
    for path, text in src['files'].items():
        line_starts = [0]
        for m in re.finditer('\n', text):
            line_starts.append(m.end())
        for label, pattern in patterns:
            for m in re.finditer(pattern, text, re.I | re.S):
                line = 1
                # bounded source packages; linear scan is fine and deterministic.
                for i, off in enumerate(line_starts):
                    if off > m.start():
                        break
                    line = i + 1
                key = (path, line, label)
                if key in seen:
                    continue
                seen.add(key)
                item = line_context(src['name'], path, text, line - radius, line + radius)
                item['pattern_label'] = label
                item['match'] = m.group(0)[:500]
                hits.append(item)
                if len(hits) >= limit:
                    return hits
    return hits


def source_manifest(srcs: dict[str, dict]) -> dict:
    return {
        name: {
            'arxiv': s['arxiv'],
            'url': s['url'],
            'archive_sha256': s['archive_sha256'],
            'expected_sha256': s['expected_sha256'],
            'expected_hash_match': s['expected_hash_match'],
            'transport': s['transport'],
            'expanded_sha256': s['expanded_sha256'],
            'warnings': s['warnings'],
            'source_files': sorted(s['files']),
        }
        for name, s in srcs.items()
    }


def main() -> int:
    try:
        srcs = {name: acquire(name) for name in SOURCES}
    except (RuntimeError, SourceDecodeError, OSError) as exc:
        (OUT / 'infrastructure_failure.json').write_text(
            json.dumps({'classification': 'INFRASTRUCTURE_FAIL', 'scientific_negative': False, 'error': repr(exc)}, indent=2) + '\n'
        )
        print(repr(exc))
        return 2

    manifest = source_manifest(srcs)
    (OUT / 'source_manifest.json').write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n')

    provenance = {
        'lane': 'provenance',
        'classification': 'EVIDENCE_COLLECTION_ONLY',
        'target_hash_match': manifest['target']['expected_hash_match'],
        'qspinnet_hash_match': manifest['qspinnet']['expected_hash_match'],
        'wojtek_hash_recorded': bool(manifest['wojtek']['archive_sha256']),
        'all_exact_versions_requested': True,
        'manifest_file': 'source_manifest.json',
    }
    (OUT / 'provenance.json').write_text(json.dumps(provenance, indent=2, sort_keys=True) + '\n')

    qbar_patterns = [
        ('bar_q', r'\\bar\s*\{?q\}?'),
        ('inverse_q', r'q\s*\^\s*\{?\s*-\s*1\s*\}?'),
        ('complex_conjugate', r'complex.{0,40}conjugat'),
        ('inverse_deformation', r'inverse.{0,80}deformation'),
        ('cup_cap', r'\\(?:cup|cap)|\bcup\b|\bcap\b'),
        ('dual_map', r'\bdual\b.{0,160}(?:Clebsch|intertwiner|map|coefficient|q)'),
        ('magnetic_indices', r'm_?1.{0,180}m_?2.{0,180}m_?3'),
    ]
    qbar_hits = []
    for key in ('target', 'qspinnet'):
        qbar_hits.extend(collect_hits(srcs[key], qbar_patterns, radius=12, limit=80))
    qbar = {
        'lane': 'qbar',
        'classification': 'EVIDENCE_COLLECTION_ONLY',
        'sources_inspected': ['1609.02429v2', '1312.0905v2'],
        'hit_count': len(qbar_hits),
        'hits': qbar_hits,
        'manual_rule': 'PASS only if decisive evidence uniquely fixes qbar input/output index ordering under frozen target q-CG normalization; graphical/prose/lexical-only remains BLOCKED_SOURCE_AUTHORITY.',
    }
    (OUT / 'qbar_evidence.json').write_text(json.dumps(qbar, indent=2, sort_keys=True) + '\n')

    r_patterns = [
        ('mathcal_R', r'\\mathcal\s*\{R\}'),
        ('R_inverse', r'(?:\\mathcal\s*\{R\}|\bR\b)\s*\^\s*\{?\s*-\s*1\s*\}?'),
        ('R_matrix', r'R[- ]{0,2}matrix'),
        ('braid', r'braid(?:ing)?'),
        ('crossing', r'cross(?:ing|ed|es)'),
        ('over_under', r'overcross|undercross|over-cross|under-cross'),
        ('tensor_order', r'(?:V_|V\^|tensor|\\otimes).{0,200}(?:R|\\mathcal\{R\})'),
    ]
    r_hits = []
    for key in ('target', 'wojtek'):
        r_hits.extend(collect_hits(srcs[key], r_patterns, radius=14, limit=100))
    r_ev = {
        'lane': 'r-crossing',
        'classification': 'EVIDENCE_COLLECTION_ONLY',
        'sources_inspected': ['1609.02429v2', '1311.1798v1'],
        'hit_count': len(r_hits),
        'hits': r_hits,
        'manual_rule': 'PASS only if decisive evidence gives executable R and source-unique R versus R^-1 crossing/tensor-leg assignment. Universal-R formula without crossing assignment remains BLOCKED_SOURCE_AUTHORITY.',
    }
    (OUT / 'r_crossing_evidence.json').write_text(json.dumps(r_ev, indent=2, sort_keys=True) + '\n')

    target = srcs['target']
    positive_patterns = [
        ('coproduct', r'\\Delta\s*\([^\n]{0,160}J'),
        ('cap_or_cup_indexed', r'(?:cap|cup).{0,500}(?:delta|\\delta).{0,300}m'),
    ]
    pos_hits = collect_hits(target, positive_patterns, radius=10, limit=20)
    synthetic = 'SYNTHETIC_ONLY_R_MATRIX_TOKEN_WITHOUT_FORMULA'
    source_concat = '\n'.join(target['files'].values())
    controls = {
        'lane': 'controls',
        'classification': 'EVIDENCE_COLLECTION_ONLY',
        'positive_control_hit_count': len(pos_hits),
        'positive_control_hits': pos_hits,
        'synthetic_negative_token': synthetic,
        'synthetic_negative_absent_from_source': synthetic not in source_concat,
        'bibliography_only_is_not_authority': True,
        'lexical_only_is_not_authority': True,
    }
    (OUT / 'controls.json').write_text(json.dumps(controls, indent=2, sort_keys=True) + '\n')

    aggregate = {
        'classification': 'EVIDENCE_COLLECTED_REQUIRES_MANUAL_VERDICT',
        'scientific_pass_emitted_by_automation': False,
        'candidate_theory_authorized': False,
        'bridge_credit': False,
        'iter012_retry_authorized': False,
        'eq29_amplitude_authorized': False,
        'eq27_component_reconstruction_prereg_allowed': False,
        'new_physics_found': False,
        'provenance': provenance,
        'qbar_hit_count': len(qbar_hits),
        'r_hit_count': len(r_hits),
        'positive_control_hit_count': len(pos_hits),
    }
    (OUT / 'aggregate.json').write_text(json.dumps(aggregate, indent=2, sort_keys=True) + '\n')
    print(json.dumps(aggregate, indent=2, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
