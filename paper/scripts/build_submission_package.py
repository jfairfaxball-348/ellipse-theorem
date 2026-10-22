#!/usr/bin/env python3
"""Build a flat, reproducible Editorial Manager LaTeX submission archive."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import re

paper = Path(__file__).resolve().parents[1]
out = paper / "submission"
out.mkdir(exist_ok=True)
source = (paper / "main.tex").read_text(encoding="utf-8")
# Editorial Manager cannot process \input paths within subdirectories.
tex = source.replace(r"\input{figures/", r"\input{")
if tex == source:
    raise SystemExit("Expected figure input paths were not found")
name = "ellipse-theorem.tex"
(out / name).write_text(tex, encoding="utf-8")
assets = {name: tex.encode("utf-8")}
for figure in sorted((paper / "figures").glob("*.tikz")):
    assets[figure.name] = figure.read_bytes()
assets["references.bib"] = (paper / "references.bib").read_bytes()
assets["README_SUBMISSION.txt"] = (
    "Noncrossing Two-Nearest-Predecessor Orders on Nearly Circular Ellipses\n"
    "John Fairfax-Ball — LaTeX source package (22 October 2026)\n\n"
    "All files are in the ZIP root (no subdirectories), as recommended\n"
    "for Elsevier Editorial Manager. Upload this ZIP as LaTeX source files.\n"
    "For initial review, upload the separately supplied paper/main.pdf as\n"
    "the Manuscript if the journal's submission interface allows PDF.\n\n"
    "To compile: extract all ZIP contents in one folder, then run:\n"
    "  latexmk -pdf -interaction=nonstopmode -halt-on-error ellipse-theorem.tex\n\n"
    "Requirements: TeX Live with TikZ, AMS packages, natbib, hyperref,\n"
    "microtype, lmodern, and standard LaTeX extras. The bibliography\n"
    "is embedded in ellipse-theorem.tex; references.bib is supplied\n"
    "for convenient future conversion and is not required by latexmk.\n"
    "The five .tikz files are necessary and must remain beside the .tex.\n"
    "No 'elsarticle.cls' is bundled; this is a standards-based initial\n"
    "manuscript in the original article class, not a journal typeset proof.\n"
).encode("utf-8")
for included in re.findall(r"\\input\{([^}]+)\}",tex):
    if included not in assets:
        raise SystemExit("Unresolved LaTeX input: " + included)
zip_path = out / "ellipse-theorem-latex-source.zip"
with ZipFile(zip_path, "w", ZIP_DEFLATED) as archive:
    for filename, content in sorted(assets.items()):
        archive.writestr(filename, content)
print("Created",zip_path,"(",len(assets),"flat files )")
