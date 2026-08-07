#!/usr/bin/env python3
"""Post-process a pandoc-generated .docx for a printable bench copy.

All edits are made directly on the OOXML parts inside the .docx (a zip), using
only the Python standard library:

1. Page-number footer ("Page N of M").
2. `updateFields` flag so the table of contents and page numbers populate when
   the document is opened (pandoc leaves those fields empty).
3. Default body text set to 10pt (from 12pt).

Usage:  patch_docx.py <file.docx>
"""
import os
import re
import sys
import zipfile

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


def ensure_footer(parts, order):
    """Add the page-number footer if absent, referenced from the body section."""
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
    if FOOTER_PART not in order:
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
    else:  # no explicit default size: add one inside rPrDefault's rPr
        seg = seg.replace("<w:rPr>", '<w:rPr><w:sz w:val="20"/><w:szCs w:val="20"/>', 1)
    parts["word/styles.xml"] = (s[:i] + seg + s[j:]).encode("utf-8")


def patch(path):
    with zipfile.ZipFile(path) as z:
        parts = {i.filename: z.read(i.filename) for i in z.infolist()}
        order = [i.filename for i in z.infolist()]

    ensure_footer(parts, order)
    enable_update_fields(parts)
    set_default_10pt(parts)

    tmp = path + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for name in order:
            z.writestr(name, parts[name])
    os.replace(tmp, path)
    print(f"patched: {path}  (page-number footer, 10pt, auto-updating fields)")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".docx"):
        sys.exit("usage: patch_docx.py <file.docx>")
    patch(sys.argv[1])
