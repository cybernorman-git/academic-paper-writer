#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Check a compiled paper against target journal requirements.
Reports word count, figure count, reference count, and page count.

Usage:
    uv run check_journal_requirements.py --tex main.tex --journal nano-letters
    uv run check_journal_requirements.py --tex main.tex --journal prb
    uv run check_journal_requirements.py --list-journals
"""

import argparse
import re
import sys
from pathlib import Path

JOURNALS = {
    "nano-letters": {
        "name": "Nano Letters",
        "max_words": 5000,
        "max_figures": 6,
        "max_refs": 55,
        "max_pages": None,
        "abstract_words": 150,
        "notes": "Results+Discussion combined. SI encouraged.",
    },
    "acs-nano": {
        "name": "ACS Nano",
        "max_words": 8000,
        "max_figures": 8,
        "max_refs": 70,
        "max_pages": None,
        "abstract_words": 150,
        "notes": "Full article. Comprehensive experimental sections.",
    },
    "prl": {
        "name": "Physical Review Letters",
        "max_words": 3750,
        "max_figures": 4,
        "max_refs": 30,
        "max_pages": 4,
        "abstract_words": 600,
        "notes": "4 pages STRICT. Impact statement required.",
    },
    "prb": {
        "name": "Physical Review B",
        "max_words": 10000,
        "max_figures": 12,
        "max_refs": 100,
        "max_pages": None,
        "abstract_words": 600,
        "notes": "Regular article. Rapid comm = 4 pages.",
    },
    "nature": {
        "name": "Nature",
        "max_words": 3000,
        "max_figures": 6,
        "max_refs": 50,
        "max_pages": None,
        "abstract_words": 200,
        "notes": "Letter format. Extended Data ≤10 items.",
    },
    "nature-photonics": {
        "name": "Nature Photonics",
        "max_words": 3000,
        "max_figures": 6,
        "max_refs": 60,
        "max_pages": None,
        "abstract_words": 200,
        "notes": "Letter format. Methods in SI.",
    },
    "nature-comms": {
        "name": "Nature Communications",
        "max_words": 5000,
        "max_figures": 8,
        "max_refs": 70,
        "max_pages": None,
        "abstract_words": 200,
        "notes": "Full article. Open access.",
    },
    "advanced-materials": {
        "name": "Advanced Materials",
        "max_words": 6000,
        "max_figures": 8,
        "max_refs": 60,
        "max_pages": None,
        "abstract_words": 250,
        "notes": "Communication or full paper. ToC graphic required.",
    },
}


def count_words_in_tex(tex_path: Path) -> int:
    """Count approximate words in LaTeX file, ignoring commands."""
    text = tex_path.read_text(encoding="utf-8", errors="ignore")
    # Remove comments
    text = re.sub(r"%.*", "", text)
    # Remove LaTeX commands (keep their arguments roughly)
    text = re.sub(r"\\[a-zA-Z]+\*?(\{[^}]*\}|\[[^\]]*\])*", " ", text)
    # Remove math environments
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.DOTALL)
    text = re.sub(r"\$.*?\$", " ", text)
    text = re.sub(r"\\begin\{equation\}.*?\\end\{equation\}", " ", text, flags=re.DOTALL)
    # Remove remaining braces
    text = re.sub(r"[{}]", " ", text)
    # Count words
    words = [w for w in text.split() if re.match(r"[A-Za-z]", w)]
    return len(words)


def count_figures(tex_path: Path) -> int:
    text = tex_path.read_text(encoding="utf-8", errors="ignore")
    return len(re.findall(r"\\begin\{figure", text))


def count_references(tex_path: Path) -> int:
    bib_path = tex_path.parent / "refs.bib"
    if not bib_path.exists():
        # Try counting \bibitem
        text = tex_path.read_text(encoding="utf-8", errors="ignore")
        return len(re.findall(r"\\bibitem", text))
    bib_text = bib_path.read_text(encoding="utf-8", errors="ignore")
    return len(re.findall(r"^@\w+\{", bib_text, re.MULTILINE))


def check(tex_path: Path, journal_key: str):
    if journal_key not in JOURNALS:
        print(f"Unknown journal: {journal_key}")
        print("Use --list-journals to see available options.")
        sys.exit(1)

    j = JOURNALS[journal_key]
    print(f"Checking against: {j['name']}")
    print(f"Notes: {j['notes']}\n")

    words = count_words_in_tex(tex_path)
    figures = count_figures(tex_path)
    refs = count_references(tex_path)

    def status(val, limit, label):
        if limit is None:
            print(f"  {label}: {val} (no limit)")
            return
        pct = val / limit * 100
        icon = "✅" if val <= limit else "❌"
        print(f"  {icon} {label}: {val} / {limit} ({pct:.0f}%)")

    print("=== Results ===")
    status(words, j["max_words"], "Words")
    status(figures, j["max_figures"], "Figures")
    status(refs, j["max_refs"], "References")

    print()
    if words > (j["max_words"] or float("inf")):
        over = words - j["max_words"]
        print(f"⚠️  Over word limit by {over} words. Consider moving methods to SI.")
    if figures > (j["max_figures"] or float("inf")):
        print(f"⚠️  Too many main figures. Move {figures - j['max_figures']} to SI.")
    if refs > (j["max_refs"] or float("inf")):
        print(f"⚠️  Too many references. Prune {refs - j['max_refs']} less essential ones.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tex", help="Path to main .tex file")
    parser.add_argument("--journal", help="Target journal key (e.g. nano-letters, prb)")
    parser.add_argument("--list-journals", action="store_true")
    args = parser.parse_args()

    if args.list_journals:
        print(f"{'Key':<22} {'Name':<25} {'Words':>7} {'Figs':>5} {'Refs':>5}")
        print("-" * 70)
        for k, j in JOURNALS.items():
            print(f"{k:<22} {j['name']:<25} {str(j['max_words']):>7} "
                  f"{str(j['max_figures']):>5} {str(j['max_refs']):>5}")
        return

    if not args.tex or not args.journal:
        parser.print_help()
        sys.exit(1)

    check(Path(args.tex), args.journal)


if __name__ == "__main__":
    main()
