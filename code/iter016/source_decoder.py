"""Bounded offline source-container decoder. No formula qualification or network I/O.

Supports plain UTF-8/Latin-1 TeX and one gzip layer containing TeX or USTAR/PAX.
Does not extract paths or execute TeX. Scientific source review remains mandatory.
"""
from __future__ import annotations

import gzip
import hashlib
import io
import re
import tarfile
from dataclasses import dataclass
from pathlib import PurePosixPath


class SourceDecodeError(ValueError):
    """An input is incomplete, unsupported, or outside a resource bound."""


@dataclass(frozen=True)
class Limits:
    max_input: int = 16 * 1024 * 1024
    max_expanded: int = 64 * 1024 * 1024
    max_member: int = 8 * 1024 * 1024
    max_members: int = 1024


@dataclass(frozen=True)
class DecodedSource:
    transport: str
    files: dict[str, str]
    input_sha256: str
    expanded_sha256: str
    warnings: tuple[str, ...]


def _text(data: bytes, name: str, warnings: list[str]) -> str:
    probe = data.lstrip()[:1024].lower()
    if probe.startswith(b'%pdf-'):
        raise SourceDecodeError('PDF_NOT_TEX')
    if re.match(br'(?:<!doctype\s+html|<html\b|<head\b|<body\b)', probe):
        raise SourceDecodeError('HTML_NOT_TEX')
    if not data or any(b < 32 and b not in (9, 10, 12, 13) for b in data):
        raise SourceDecodeError('EMPTY_OR_BINARY_TEXT')
    try:
        text = data.decode('utf-8-sig')
    except UnicodeDecodeError:
        text = data.decode('latin-1')
        warnings.append('LATIN1_FALLBACK:' + name)
    # A transport sanity predicate, never a mathematical authority predicate.
    if not re.search(r'\\[A-Za-z]+', text):
        raise SourceDecodeError('NO_TEX_COMMAND')
    return text


def decode_source(data: bytes, *, expected_size: int | None = None,
                  known_truncated: bool = False,
                  limits: Limits = Limits()) -> DecodedSource:
    """Decode complete response bytes. Never silently clip or concatenate files.

    expected_size is the byte count for *these* bytes (not a pre-HTTP-decoding
    Content-Length). Plain-text truncation is undetectable without such metadata.
    """
    if not isinstance(data, bytes):
        raise TypeError('data must be bytes')
    if min(limits.max_input, limits.max_expanded, limits.max_member,
           limits.max_members) <= 0:
        raise ValueError('all limits must be positive')
    if known_truncated or (expected_size is not None and len(data) != expected_size):
        raise SourceDecodeError('INCOMPLETE_RESPONSE')
    if len(data) > limits.max_input:
        raise SourceDecodeError('INPUT_LIMIT')
    original_hash = hashlib.sha256(data).hexdigest()
    transport = 'plain'
    if data.startswith(b'\x1f\x8b'):
        try:
            with gzip.GzipFile(fileobj=io.BytesIO(data)) as stream:
                data = stream.read(limits.max_expanded + 1)
        except (OSError, EOFError) as exc:
            raise SourceDecodeError('INVALID_OR_TRUNCATED_GZIP') from exc
        transport = 'gzip'
    if len(data) > limits.max_expanded:
        raise SourceDecodeError('EXPANDED_LIMIT')
    warnings: list[str] = []
    files: dict[str, str] = {}
    if len(data) >= 512 and data[257:262] == b'ustar':
        transport = 'tar' if transport == 'plain' else 'gzip+tar'
        if len(data) % 512 or not data.endswith(b'\0' * 1024):
            raise SourceDecodeError('INCOMPLETE_TAR_TRAILER')
        try:
            with tarfile.open(fileobj=io.BytesIO(data), mode='r:') as archive:
                seen: set[str] = set()
                total = 0
                for count, member in enumerate(archive, 1):
                    if count > limits.max_members:
                        raise SourceDecodeError('MEMBER_COUNT_LIMIT')
                    path = PurePosixPath(member.name)
                    if path.is_absolute() or '..' in path.parts or '\\' in member.name:
                        raise SourceDecodeError('UNSAFE_MEMBER_PATH')
                    if member.isdir():
                        continue
                    if not member.isfile() or member.issparse():
                        raise SourceDecodeError('UNSUPPORTED_MEMBER_TYPE')
                    if str(path) in seen:
                        raise SourceDecodeError('DUPLICATE_MEMBER_PATH')
                    seen.add(str(path))
                    total += member.size
                    if member.size > limits.max_member or total > limits.max_expanded:
                        raise SourceDecodeError('MEMBER_SIZE_LIMIT')
                    if path.suffix.lower() not in ('.tex', '.ltx'):
                        continue
                    stream = archive.extractfile(member)
                    if stream is None:
                        raise SourceDecodeError('MISSING_MEMBER_BYTES')
                    with stream:
                        payload = stream.read(limits.max_member + 1)
                    if len(payload) != member.size:
                        raise SourceDecodeError('TRUNCATED_MEMBER')
                    files[str(path)] = _text(payload, str(path), warnings)
        except (tarfile.TarError, EOFError, OSError) as exc:
            raise SourceDecodeError('INVALID_OR_TRUNCATED_TAR') from exc
        if not files:
            raise SourceDecodeError('NO_TEX_MEMBERS')
    else:
        if len(data) > limits.max_member:
            raise SourceDecodeError('MEMBER_SIZE_LIMIT')
        files['source.tex'] = _text(data, 'source.tex', warnings)
    return DecodedSource(transport, files, original_hash,
                         hashlib.sha256(data).hexdigest(), tuple(warnings))
