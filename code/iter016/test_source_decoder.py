"""Synthetic transport tests only; they confer no physics validation credit."""
import gzip
import io
import tarfile
import unittest
from source_decoder import decode_source, SourceDecodeError, Limits

TEX = b'\\documentclass{article}\n\\begin{document}J_z\\end{document}\n'


def tar_bytes(entries, fmt=tarfile.USTAR_FORMAT):
    out = io.BytesIO()
    with tarfile.open(fileobj=out, mode='w', format=fmt) as archive:
        for name, body, kind in entries:
            info = tarfile.TarInfo(name)
            info.type = kind
            info.size = len(body) if kind == tarfile.REGTYPE else 0
            if kind == tarfile.SYMTYPE:
                info.linkname = '../../escape'
            archive.addfile(info, io.BytesIO(body) if info.isfile() else None)
    return out.getvalue()


class SourceTests(unittest.TestCase):
    def reject(self, data, code, **kw):
        with self.assertRaisesRegex(SourceDecodeError, code):
            decode_source(data, **kw)

    def test_plain(self):
        self.assertEqual(decode_source(TEX).files['source.tex'], TEX.decode())

    def test_gzip(self):
        self.assertEqual(decode_source(gzip.compress(TEX)).transport, 'gzip')

    def test_tar(self):
        data = tar_bytes([('a.tex', TEX, tarfile.REGTYPE)])
        self.assertEqual(decode_source(data).files, {'a.tex': TEX.decode()})

    def test_gzip_tar(self):
        data = gzip.compress(tar_bytes([('a.tex', TEX, tarfile.REGTYPE)]))
        self.assertEqual(decode_source(data).transport, 'gzip+tar')

    def test_keep_members_separate(self):
        data = tar_bytes([('a.tex', TEX, tarfile.REGTYPE),
                          ('nested/b.tex', TEX, tarfile.REGTYPE)])
        self.assertEqual(len(decode_source(data).files), 2)

    def test_pax(self):
        name = 'nested/' + 'a' * 120 + '.tex'
        data = tar_bytes([(name, TEX, tarfile.REGTYPE)], tarfile.PAX_FORMAT)
        self.assertIn(name, decode_source(data).files)

    def test_pdf(self):
        self.reject(b'%PDF-1.7\nbody', 'PDF_NOT_TEX')

    def test_html(self):
        self.reject(b'  <!DOCTYPE html><html>429</html>', 'HTML_NOT_TEX')

    def test_gzip_html(self):
        self.reject(gzip.compress(b'<html>error</html>'), 'HTML_NOT_TEX')

    def test_binary(self):
        self.reject(b'\\hello\x00\x01', 'EMPTY_OR_BINARY_TEXT')

    def test_no_tex(self):
        self.reject(b'Service unavailable', 'NO_TEX_COMMAND')

    def test_truncated_gzip(self):
        self.reject(gzip.compress(TEX)[:-5], 'INVALID_OR_TRUNCATED_GZIP')

    def test_bad_gzip_checksum(self):
        data = bytearray(gzip.compress(TEX))
        data[-8] ^= 1
        self.reject(bytes(data), 'INVALID_OR_TRUNCATED_GZIP')

    def test_truncated_tar(self):
        data = tar_bytes([('a.tex', TEX * 50, tarfile.REGTYPE)])
        self.reject(data[:900], 'INCOMPLETE_TAR_TRAILER')

    def test_declared_truncation(self):
        self.reject(TEX, 'INCOMPLETE_RESPONSE', known_truncated=True)

    def test_wrong_size(self):
        self.reject(TEX, 'INCOMPLETE_RESPONSE', expected_size=len(TEX) + 1)

    def test_correct_size(self):
        self.assertTrue(decode_source(TEX, expected_size=len(TEX)).files)

    def test_input_limit(self):
        self.reject(TEX, 'INPUT_LIMIT', limits=Limits(max_input=4))

    def test_expansion_limit(self):
        self.reject(gzip.compress(TEX * 100), 'EXPANDED_LIMIT',
                    limits=Limits(max_expanded=100))

    def test_member_limit(self):
        self.reject(tar_bytes([('a.tex', TEX, tarfile.REGTYPE)]),
                    'MEMBER_SIZE_LIMIT', limits=Limits(max_member=4))

    def test_member_count(self):
        data = tar_bytes([('a.tex', TEX, tarfile.REGTYPE),
                          ('b.tex', TEX, tarfile.REGTYPE)])
        self.reject(data, 'MEMBER_COUNT_LIMIT', limits=Limits(max_members=1))

    def test_traversal(self):
        self.reject(tar_bytes([('../a.tex', TEX, tarfile.REGTYPE)]),
                    'UNSAFE_MEMBER_PATH')

    def test_absolute_path(self):
        self.reject(tar_bytes([('/a.tex', TEX, tarfile.REGTYPE)]),
                    'UNSAFE_MEMBER_PATH')

    def test_symlink(self):
        self.reject(tar_bytes([('a.tex', b'', tarfile.SYMTYPE)]),
                    'UNSUPPORTED_MEMBER_TYPE')

    def test_duplicate(self):
        data = tar_bytes([('a.tex', TEX, tarfile.REGTYPE)] * 2)
        self.reject(data, 'DUPLICATE_MEMBER_PATH')

    def test_no_tex_in_tar(self):
        self.reject(tar_bytes([('a.txt', b'hello', tarfile.REGTYPE)]),
                    'NO_TEX_MEMBERS')

    def test_latin1_warning(self):
        self.assertTrue(decode_source(TEX + b'% caf\xe9').warnings)

    def test_utf8_bom(self):
        self.assertEqual(decode_source(b'\xef\xbb\xbf' + TEX).files['source.tex'],
                         TEX.decode())

    def test_hashes(self):
        self.assertEqual(len(decode_source(TEX).input_sha256), 64)

    def test_invalid_limits(self):
        with self.assertRaises(ValueError):
            decode_source(TEX, limits=Limits(max_input=0))


if __name__ == '__main__':
    unittest.main(verbosity=2)
