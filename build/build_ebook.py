"""Build the Tools, Not Theory ebook (EPUB) and a PDF proof from the production manuscript.

Usage: python3 build/build_ebook.py   (run from the repository root)
Needs: pandoc (pip install pypandoc_binary) and, for the PDF, Chromium.
"""
import pathlib, re, subprocess, sys
import pypandoc

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "Tools_Not_Theory_Production.md"
BUILD = ROOT / "build"
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)

text = SRC.read_text(encoding="utf-8")

# 1. The title block (everything before the first ---) becomes EPUB metadata, not a chapter.
_, rest = text.split("\n---\n", 1)

# 2. The copyright page gets its own unlisted section so it isn't glued to Read This First.
copyright_block, rest = rest.split("\n---\n", 1)
body = "# Copyright {.unlisted .unnumbered .copyright}\n" + copyright_block.strip() + "\n\n" + rest

# 3. Section separators (---) aren't needed: every chapter starts a new file in the EPUB.
#    Writing lines (long underscores) stay as horizontal rules, styled as lines to write on.
body = re.sub(r"(?m)^---\s*$", "", body)
body = re.sub(r"(?m)^_{10,}\s*$", "* * *", body)

# 4. EPUB is strict XHTML: line breaks inside table cells must be self-closing.
body = body.replace("<br>", "<br />")

(BUILD / "ebook-source.md").write_text(body, encoding="utf-8")

meta = [
    "--metadata=title:Tools, Not Theory",
    "--metadata=subtitle:A working manual for the gap between understanding a pattern and being able to move inside it",
    "--metadata=author:Mohammad Haris",
    "--metadata=lang:en-GB",
    "--metadata=publisher:Fieldwork Press",
    "--metadata=date:2026",
    "--metadata=rights:Copyright © 2026 Mohammad Haris. All rights reserved.",
    "--metadata=description:Evidence-informed tools for low mood, avoidance, perfectionism, rumination, and the days you can't start.",
]
common = ["--from=markdown+pipe_tables+backtick_code_blocks+raw_html-implicit_figures", "--split-level=1", "--toc-depth=2"]

epub = DIST / "Tools_Not_Theory.epub"
pypandoc.convert_file(str(BUILD / "ebook-source.md"), "epub3", outputfile=str(epub),
                      extra_args=common + meta + [f"--css={BUILD / 'ebook.css'}"])
print("EPUB:", epub, epub.stat().st_size, "bytes")

# PDF proof: one standalone HTML page printed by headless Chromium.
html = BUILD / "proof.html"
pypandoc.convert_file(str(BUILD / "ebook-source.md"), "html5", outputfile=str(html),
                      extra_args=common + meta + ["--standalone", "--embed-resources", f"--css={BUILD / 'ebook.css'}"])
chrome = next((p for p in ["/opt/pw-browsers/chromium-1194/chrome-linux/chrome", "chromium", "google-chrome"]
               if pathlib.Path(p).exists() or subprocess.run(["which", p], capture_output=True).returncode == 0), None)
if chrome:
    pdf = DIST / "Tools_Not_Theory_proof.pdf"
    subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", html.as_uri()], check=True, capture_output=True)
    print("PDF:", pdf, pdf.stat().st_size, "bytes")
else:
    print("Chromium not found; skipped the PDF proof.", file=sys.stderr)
