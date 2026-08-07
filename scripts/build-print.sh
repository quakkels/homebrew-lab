#!/usr/bin/env bash
#
# build-print.sh — Build a printable copy of the Homebrew Lab curriculum.
#
# Combines the markdown course (syllabus, all experiments, project briefs, and
# glossary) into one Word/LibreOffice document with a title page, table of
# contents, and a page break before each chapter. Experiments are auto-discovered
# in numeric order, so re-running picks up newly added ones automatically.
#
# Usage:
#   ./scripts/build-print.sh                # -> Homebrew-Lab.docx (default)
#   ./scripts/build-print.sh my-copy.docx   # choose the output name
#   ./scripts/build-print.sh my-copy.odt    # native LibreOffice .odt
#
# Requires pandoc; the .odt option also needs LibreOffice (soffice).

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."        # repo root (this script is in scripts/)

OUT="${1:-Homebrew-Lab.docx}"
command -v pandoc >/dev/null || { echo "error: pandoc not installed (https://pandoc.org)" >&2; exit 1; }

# Reading order: syllabus -> experiments (numeric) -> project briefs -> glossary.
FILES=(syllabus.md experiments/[0-9]*.md
       projects/keyboard/README.md projects/radio/README.md glossary.md)

# Assemble one markdown file: front matter, then each source file preceded by a
# page break (a raw OpenXML break, applied when rendering to .docx).
TMP="$(mktemp --suffix=.md)"
trap 'rm -f "$TMP"' EXIT

cat > "$TMP" <<'FRONT'
---
title: "Homebrew Lab"
subtitle: "An Electronics Curriculum — printable bench reference"
---

> **This curriculum is AI-generated.** Treat it as a starting map, not an authority. Verify component values and procedures — especially anything involving mains power or RF transmission — against trusted references (ARRL Handbook, datasheets, *The Art of Electronics*) before relying on them.
FRONT

for f in "${FILES[@]}"; do
  printf '\n\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n'
  cat "$f"
done >> "$TMP"

# Render to docx and patch it (page-number footer, 10pt, auto-updating fields).
build_docx() {
  pandoc "$TMP" -f markdown -t docx --toc --toc-depth=1 -o "$1"
  python3 scripts/patch_docx.py "$1"
}

case "$OUT" in
  *.docx) build_docx "$OUT" ;;
  *.odt)
    command -v soffice >/dev/null || { echo "error: .odt needs LibreOffice (soffice)" >&2; exit 1; }
    WORK="$(mktemp -d)"; trap 'rm -rf "$TMP" "$WORK"' EXIT
    build_docx "$WORK/doc.docx"
    soffice --headless --convert-to odt --outdir "$WORK" "$WORK/doc.docx" >/dev/null 2>&1
    mv "$WORK/doc.odt" "$OUT"
    ;;
  *) echo "error: output must end in .docx or .odt (got: $OUT)" >&2; exit 1 ;;
esac

cat <<EOF
Built: $OUT
Open in Word or LibreOffice to print — page numbers are in the footer. The table
of contents fills in on open (Word updates it automatically; in LibreOffice choose
Tools > Update > Update All if it looks blank).
EOF
