#!/usr/bin/env bash
#
# build-print.sh — Build a printable copy of the Homebrew Lab curriculum.
#
# Combines the markdown course (syllabus, all experiments, project briefs, and
# the glossary) into a single Word/LibreOffice document with a title page, a
# table of contents, and a page break before each chapter. Re-run it any time
# the curriculum changes — the experiment files are auto-discovered in numeric
# order, so newly added experiments are included automatically.
#
# Usage:
#   ./scripts/build-print.sh                 # -> Homebrew-Lab.docx  (default)
#   ./scripts/build-print.sh my-copy.docx    # choose the output name
#   ./scripts/build-print.sh my-copy.odt     # native LibreOffice .odt
#
# A .docx opens and prints from both Microsoft Word and LibreOffice, so it is
# the recommended default; .odt is offered for convenience.
#
# Requires: pandoc (https://pandoc.org). The .odt option also needs LibreOffice
# (the `soffice` command).

set -euo pipefail

# --- locate the repo root (this script lives in <repo>/scripts) ---------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT"

OUT="${1:-Homebrew-Lab.docx}"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "error: pandoc is not installed — see https://pandoc.org/installing.html" >&2
  exit 1
fi

# --- reading order ------------------------------------------------------------
# syllabus -> experiments (numeric, auto-discovered) -> project briefs -> glossary
mapfile -t EXPERIMENTS < <(ls experiments/[0-9]*.md | sort)
FILES=(
  "syllabus.md"
  "${EXPERIMENTS[@]}"
  "projects/keyboard/README.md"
  "projects/radio/README.md"
  "glossary.md"
)

# --- assemble one markdown file with a title block and chapter page breaks ----
TMP="$(mktemp --suffix=.md)"
trap 'rm -f "$TMP"' EXIT

cat > "$TMP" <<'FRONT'
---
title: "Homebrew Lab"
subtitle: "An Electronics Curriculum — printable bench reference"
---

> **This curriculum is AI-generated.** Treat it as a starting map, not an authority. Verify component values and procedures — especially anything involving mains power or RF transmission — against trusted references (ARRL Handbook, datasheets, *The Art of Electronics*) before relying on them.
FRONT

# A raw OpenXML page break (applied when rendering to .docx).
PAGEBREAK='```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```'

for f in "${FILES[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "error: expected file not found: $f" >&2
    exit 1
  fi
  {
    printf '\n\n%s\n\n' "$PAGEBREAK"
    cat "$f"
  } >> "$TMP"
done

# --- render -------------------------------------------------------------------
# Build the docx, then patch it: add a "Page N of M" footer and set the flag
# that makes the table of contents and page numbers populate on open (pandoc
# leaves those fields empty, which is why an unpatched TOC looks blank).
render_docx() {
  pandoc "$TMP" -f markdown -t docx --toc --toc-depth=1 -o "$1"
  python3 "$SCRIPT_DIR/patch_docx.py" "$1"
}

case "$OUT" in
  *.odt)
    if ! command -v soffice >/dev/null 2>&1; then
      echo "error: building .odt needs LibreOffice (soffice)." >&2
      echo "       Build a .docx instead, or install LibreOffice." >&2
      exit 1
    fi
    WORK="$(mktemp -d)"
    render_docx "$WORK/doc.docx"
    soffice --headless --convert-to odt --outdir "$WORK" "$WORK/doc.docx" >/dev/null 2>&1
    mv "$WORK/doc.odt" "$OUT"
    rm -rf "$WORK"
    ;;
  *.docx)
    render_docx "$OUT"
    ;;
  *)
    echo "error: output must end in .docx or .odt (got: $OUT)" >&2
    exit 1
    ;;
esac

echo "Built: $OUT"
echo
echo "Open it in Word or LibreOffice to print. Page numbers are in the footer."
echo "The table of contents fills in when the file is opened: Word updates it"
echo "automatically; in LibreOffice, if it shows blank, choose"
echo "Tools > Update > Update All (or select all and press F9)."
