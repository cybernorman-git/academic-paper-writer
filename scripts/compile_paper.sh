#!/usr/bin/env bash
# Compile a LaTeX paper with latexmk and report errors.
# Usage: ./compile_paper.sh [main.tex] [output_dir]
#
# Requirements: latexmk, pdflatex (or lualatex), bibtex/biber
# Install on macOS: brew install --cask mactex-no-gui
# Or: brew install texlive (Linux)

set -euo pipefail

TEX_FILE="${1:-main.tex}"
OUTPUT_DIR="${2:-.}"
LOG_FILE="${OUTPUT_DIR}/compile.log"

# Check latexmk is available
if ! command -v latexmk &>/dev/null; then
    echo "ERROR: latexmk not found."
    echo "Install: brew install --cask mactex-no-gui"
    exit 1
fi

TEX_DIR="$(dirname "$TEX_FILE")"
TEX_BASE="$(basename "$TEX_FILE" .tex)"

echo "=== Compiling $TEX_FILE ==="
echo "Output dir: $OUTPUT_DIR"
echo ""

# Run latexmk
latexmk \
    -pdf \
    -bibtex \
    -outdir="$OUTPUT_DIR" \
    -interaction=nonstopmode \
    -file-line-error \
    "$TEX_FILE" 2>&1 | tee "$LOG_FILE"

EXIT_CODE=${PIPESTATUS[0]}

if [ $EXIT_CODE -eq 0 ]; then
    PDF="${OUTPUT_DIR}/${TEX_BASE}.pdf"
    if [ -f "$PDF" ]; then
        PAGES=$(mdls -name kMDItemNumberOfPages "$PDF" 2>/dev/null | awk '{print $3}' || echo "?")
        SIZE=$(du -sh "$PDF" | cut -f1)
        echo ""
        echo "=== SUCCESS ==="
        echo "PDF: $PDF"
        echo "Pages: $PAGES | Size: $SIZE"
    fi
else
    echo ""
    echo "=== COMPILATION FAILED ==="
    echo "Extracting errors from log..."
    echo ""
    grep -n "^!" "$LOG_FILE" | head -20 || true
    grep -n "Error\|error\|undefined\|Undefined" "$LOG_FILE" | grep -v "^%" | head -20 || true
    echo ""
    echo "Full log: $LOG_FILE"
    exit 1
fi

# Check for common warnings
echo ""
echo "=== Warnings ==="
grep -c "Overfull .hbox" "$LOG_FILE" | xargs -I{} echo "Overfull hbox: {} occurrences" || true
grep -c "Citation.*undefined" "$LOG_FILE" | xargs -I{} echo "Undefined citations: {}" || true
grep -c "Reference.*undefined" "$LOG_FILE" | xargs -I{} echo "Undefined references: {}" || true
