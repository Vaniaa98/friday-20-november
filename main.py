# "The World in One Day" — Friday 20 November 2026 (Python 3.13, standard
# library only). The entry image is the entry.png beside this file: a one-page
# newspaper front page drawn programmatically. This program copies it
# byte-for-byte to /output/entry.png. No network, no dependencies.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


# A plain copy: the same input bytes always produce the same output bytes.
_src = HERE / "entry.png"
_dst = OUT / "entry.png"
shutil.copyfile(_src, _dst)
# Verify the copy so a truncated or failed write can never silently reach
# the grader: the output must be byte-identical to the source image.
if _sha256(_src) != _sha256(_dst):
    raise RuntimeError("entry.png copy failed integrity check")
