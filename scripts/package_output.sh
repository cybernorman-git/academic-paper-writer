#!/usr/bin/env bash
# Package the final paper deliverables into a zip archive.
# Usage: ./package_output.sh [project_dir] [output_name]

set -euo pipefail

PROJECT_DIR="${1:-project}"
OUTPUT_NAME="${2:-paper_package}"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
ZIP_FILE="${OUTPUT_NAME}_${TIMESTAMP}.zip"

echo "=== Packaging paper deliverables ==="
echo "Source: $PROJECT_DIR"
echo "Output: $ZIP_FILE"
echo ""

# Verify required files exist
REQUIRED=(
    "${PROJECT_DIR}/main.tex"
    "${PROJECT_DIR}/refs.bib"
)
MISSING=()
for f in "${REQUIRED[@]}"; do
    if [ ! -f "$f" ]; then
        MISSING+=("$f")
    fi
done

if [ ${#MISSING[@]} -gt 0 ]; then
    echo "WARNING: Missing files:"
    for f in "${MISSING[@]}"; do
        echo "  - $f"
    done
fi

# Create zip
zip -r "$ZIP_FILE" "$PROJECT_DIR" \
    --exclude "*.aux" \
    --exclude "*.log" \
    --exclude "*.bbl" \
    --exclude "*.blg" \
    --exclude "*.fdb_latexmk" \
    --exclude "*.fls" \
    --exclude "*.synctex.gz" \
    --exclude "*/.DS_Store" \
    --exclude "*/__pycache__/*" \
    --exclude "*.pyc"

echo ""
echo "=== Contents ==="
zip -sf "$ZIP_FILE"

echo ""
SIZE=$(du -sh "$ZIP_FILE" | cut -f1)
echo "=== Done ==="
echo "Package: $ZIP_FILE ($SIZE)"
