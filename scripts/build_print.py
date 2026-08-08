#!/usr/bin/env python3
"""Build a printable copy of the Homebrew Lab curriculum.

Combines the markdown course (syllabus, all experiments, project briefs, and
glossary) into one Word/LibreOffice document: a title page, a table of contents,
and each file as a chapter with a page break between them. Experiments are
auto-discovered in numeric order, so re-running picks up new ones automatically.

After conversion the .docx is patched (standard library only) to add a
"Page N of M" footer, set body text to 10pt, and flag its fields so the table of
contents and page numbers populate when the document is opened.

Cross-platform: runs on Windows, macOS, and Linux. Needs Python 3 and pandoc;
LibreOffice (soffice) is only needed for the optional .odt output.

Usage:
    python3 scripts/build_print.py                 # -> Homebrew-Lab.docx
    python3 scripts/build_print.py my-copy.docx    # choose the output name
    python3 scripts/build_print.py my-copy.odt     # native LibreOffice .odt
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FRONT_MATTER = """---
title: "Homebrew Lab"
subtitle: "An Electronics Curriculum — printable bench reference"
---

> **This curriculum is AI-generated.** Treat it as a starting map, not an authority. Verify component values and procedures — especially anything involving mains power or RF transmission — against trusted references (ARRL Handbook, datasheets, *The Art of Electronics*) before relying on them.
"""

PAGE_BREAK = '\n\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n'


# --------------------------------------------------------------------------- #
# Assemble + convert                                                          #
# --------------------------------------------------------------------------- #
def source_files():
    """Reading order: syllabus -> experiments (numeric) -> projects -> glossary."""
    experiments = sorted(ROOT.glob("experiments/[0-9]*.md"))
    return [ROOT / "syllabus.md", *experiments,
            ROOT / "projects/keyboard/README.md",
            ROOT / "projects/radio/README.md",
            ROOT / "glossary.md"]


def assemble_markdown():
    parts = [FRONT_MATTER]
    for f in source_files():
        parts += [PAGE_BREAK, f.read_text(encoding="utf-8")]
    return "".join(parts)


def run_pandoc(markdown, out_docx):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as tf:
        tf.write(markdown)
        tmp_md = tf.name
    try:
        subprocess.run(
            ["pandoc", tmp_md, "-f", "markdown", "-t", "docx",
             "--toc", "--toc-depth=1", "-o", str(out_docx)],
            check=True)
    finally:
        os.unlink(tmp_md)


def find_soffice():
    for name in ("soffice", "soffice.exe"):
        found = shutil.which(name)
        if found:
            return found
    for base in filter(None, (os.environ.get("ProgramFiles"),
                              os.environ.get("ProgramFiles(x86)"))):
        cand = Path(base) / "LibreOffice" / "program" / "soffice.exe"
        if cand.exists():
            return str(cand)
    return None


def convert_to_odt(docx, out_odt):
    soffice = find_soffice()
    if not soffice:
        sys.exit("error: .odt output needs LibreOffice (soffice), which was not found.\n"
                 "       Build a .docx instead, or install LibreOffice.")
    with tempfile.TemporaryDirectory() as work:
        subprocess.run([soffice, "--headless", "--convert-to", "odt",
                        "--outdir", work, str(docx)],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        shutil.move(str(Path(work) / (Path(docx).stem + ".odt")), str(out_odt))


# --------------------------------------------------------------------------- #
# .docx post-processing (edits the OOXML parts inside the zip)                #
# --------------------------------------------------------------------------- #
FOOTER_PART = "word/footer1.xml"
FOOTER_XML = b"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <w:p>
    <w:pPr><w:jc w:val="center"/></w:pPr>
    <w:r><w:t xml:space="preserve">Page </w:t></w:r>
    <w:r><w:fldChar w:fldCharType="begin"/></w:r>
    <w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>
    <w:r><w:fldChar w:fldCharType="separate"/></w:r>
    <w:r><w:t>1</w:t></w:r>
    <w:r><w:fldChar w:fldCharType="end"/></w:r>
    <w:r><w:t xml:space="preserve"> of </w:t></w:r>
    <w:r><w:fldChar w:fldCharType="begin"/></w:r>
    <w:r><w:instrText xml:space="preserve"> NUMPAGES </w:instrText></w:r>
    <w:r><w:fldChar w:fldCharType="separate"/></w:r>
    <w:r><w:t>1</w:t></w:r>
    <w:r><w:fldChar w:fldCharType="end"/></w:r>
  </w:p>
</w:ftr>
"""
FOOTER_REL_TYPE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer"
FOOTER_CT = "application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"


def add_footer(parts, order):
    """Add the page-number footer, referenced from the body section."""
    if FOOTER_PART in parts:
        return
    rels_name = "word/_rels/document.xml.rels"
    rels = parts[rels_name].decode("utf-8")
    used = [int(n) for n in re.findall(r'Id="rId(\d+)"', rels)]
    rid = "rId%d" % ((max(used) + 1) if used else 1)

    ct = parts["[Content_Types].xml"].decode("utf-8")
    if "footer1.xml" not in ct:
        ct = ct.replace("</Types>",
                        f'<Override PartName="/{FOOTER_PART}" ContentType="{FOOTER_CT}"/></Types>')
        parts["[Content_Types].xml"] = ct.encode("utf-8")

    rels = rels.replace("</Relationships>",
                        f'<Relationship Id="{rid}" Type="{FOOTER_REL_TYPE}" Target="footer1.xml"/></Relationships>')
    parts[rels_name] = rels.encode("utf-8")

    doc = parts["word/document.xml"].decode("utf-8")
    footref = f'<w:footerReference w:type="default" r:id="{rid}"/>'
    tags = list(re.finditer(r"<w:sectPr\b[^>]*?/?>", doc))
    if not tags:
        sys.exit("error: no <w:sectPr> in document.xml.")
    t = tags[-1]  # body-level section
    tag = t.group()
    if tag.endswith("/>"):
        doc = doc[:t.start()] + tag[:-2] + ">" + footref + "</w:sectPr>" + doc[t.end():]
    else:
        doc = doc[:t.end()] + footref + doc[t.end():]
    parts["word/document.xml"] = doc.encode("utf-8")

    parts[FOOTER_PART] = FOOTER_XML
    order.append(FOOTER_PART)


def enable_update_fields(parts):
    s = parts.get("word/settings.xml", b"").decode("utf-8")
    if s and "w:updateFields" not in s:
        s = re.sub(r"(<w:settings\b[^>]*>)", r'\1<w:updateFields w:val="true"/>', s, count=1)
        parts["word/settings.xml"] = s.encode("utf-8")


def set_default_10pt(parts):
    """Set the document default font size to 10pt (20 half-points)."""
    s = parts["word/styles.xml"].decode("utf-8")
    i, j = s.find("<w:docDefaults>"), s.find("</w:docDefaults>")
    if i < 0 or j < 0:
        return
    seg = s[i:j]
    if "<w:sz " in seg:
        seg = re.sub(r'(<w:sz w:val=")\d+(")', r"\g<1>20\g<2>", seg)
        seg = re.sub(r'(<w:szCs w:val=")\d+(")', r"\g<1>20\g<2>", seg)
    else:
        seg = seg.replace("<w:rPr>", '<w:rPr><w:sz w:val="20"/><w:szCs w:val="20"/>', 1)
    parts["word/styles.xml"] = (s[:i] + seg + s[j:]).encode("utf-8")


def patch_docx(path):
    with zipfile.ZipFile(path) as z:
        parts = {i.filename: z.read(i.filename) for i in z.infolist()}
        order = [i.filename for i in z.infolist()]

    add_footer(parts, order)
    enable_update_fields(parts)
    set_default_10pt(parts)

    tmp = str(path) + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for name in order:
            z.writestr(name, parts[name])
    os.replace(tmp, path)


# --------------------------------------------------------------------------- #
# Entry point                                                                 #
# --------------------------------------------------------------------------- #
def main(argv):
    out = Path(argv[1]) if len(argv) > 1 else ROOT / "Homebrew-Lab.docx"
    if out.suffix.lower() not in (".docx", ".odt"):
        sys.exit(f"error: output must end in .docx or .odt (got: {out.name})")

    markdown = assemble_markdown()
    try:
        if out.suffix.lower() == ".docx":
            run_pandoc(markdown, out)
            patch_docx(out)
        else:
            with tempfile.TemporaryDirectory() as work:
                docx = Path(work) / "doc.docx"
                run_pandoc(markdown, docx)
                patch_docx(docx)
                convert_to_odt(docx, out)
    except FileNotFoundError:
        sys.exit("error: pandoc not installed — see https://pandoc.org/installing.html")
    except subprocess.CalledProcessError as e:
        sys.exit(f"error: {e.cmd[0]} failed (exit {e.returncode}).")

    print(f"Built: {out}")
    print("Open in Word or LibreOffice to print — page numbers are in the footer.\n"
          "The table of contents fills in on open (Word updates it automatically;\n"
          "in LibreOffice choose Tools > Update > Update All if it looks blank).")


if __name__ == "__main__":
    main(sys.argv)
