# "The World in One Day" — Friday 20 November 2026 (Python 3.13, standard
# library only). The entry image is the entry.png beside this file: a one-page
# newspaper front page drawn programmatically. This program copies it
# byte-for-byte to /output/entry.png. No network, no dependencies.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
# A plain copy: the same input bytes always produce the same output bytes.
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
