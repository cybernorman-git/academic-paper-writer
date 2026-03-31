---
name: academic-paper-writer
description: End-to-end academic paper writing workflow for physics, 2D materials, optics, photonics, and condensed matter papers. Covers the full pipeline: literature collection into Zotero → PDF reading and synthesis → figure generation with Python → LaTeX writing in target journal style → compilation → simulated peer review. Use when: (1) user provides a research topic or dataset and wants a full paper drafted; (2) user asks to write a paper targeting ACS Nano, Nano Letters, ACS Photonics, PRB, PRL, APL, Nature, Science, Science Advances, Nature Photonics, eLight, Advanced Materials, Advanced Functional Materials (AFM), or similar journals; (3) user provides a paper outline and wants it filled in with proper academic content; (4) user needs figure scripts, LaTeX templates, or a compiled PDF output with reviewer comments.
---

# Academic Paper Writer

Full pipeline for drafting physics/2D materials/optics academic papers with Zotero integration, Python figure generation, LaTeX compilation, and simulated peer review.

## Workflow Overview

```
Stage 0: Initialize  →  Stage 1: Literature  →  Stage 2: Synthesis
     ↓                        ↓                        ↓
  [PAUSE]               [PAUSE: user               [PAUSE: user
 confirm scope          downloads PDFs]            confirms outline]
     ↓                        ↓                        ↓
Stage 3: Figures   →   Stage 4: Writing   →   Stage 5: Compile
     ↓                        ↓                        ↓
  [PAUSE]                [auto, section             [auto]
confirm figures            by section]                 ↓
                                                  Stage 6: Review
                                                       ↓
                                               Final Package Delivery
```

**Always pause at marked checkpoints before proceeding.**

---

## Stage 0 — Project Initialization

Collect from user:
- Research topic / title hint
- Target journal (see `references/journal-styles.md` — supported: ACS Nano, Nano Letters, ACS Photonics, PRB, PRL, APL, Nature, Science, Science Advances, Nature Photonics, Nature Communications, eLight, Advanced Materials, AFM)
- Available data files (CSV, numpy, images, raw figures)
- Paper outline (optional — generate one if absent)
- Special constraints (page limit, SI required, etc.)

**Output of Stage 0:**
1. `project/OVERVIEW.md` — novelty statement, target journal, figure list, section map
2. `project/outline.md` — section-by-section outline with ~1 paragraph description each
3. Confirm with user before proceeding.

---

## Stage 1 — Literature Collection (Zotero)

Target: **≥ 30 papers** in the specified Zotero collection.

Use the `zotero-scholar` skill to add papers. Strategy:
1. Search ArXiv + web for papers in 3 waves: (a) direct topic, (b) enabling methods, (c) competing/context work
2. Organize by theme: background, methodology, comparison, applications
3. Export `.bib` file — see `scripts/export_zotero_bib.py`
4. Save to `project/refs.bib`

**PAUSE: Wait for user to manually download PDFs into a local folder.**
Ask user: "Please download the PDFs and tell me the folder path."

---

## Stage 2 — Literature Synthesis

Read all PDFs. Strategy to manage context:
- **Deep read** (full text): 5–8 most relevant papers
- **Abstract read** (abstract + intro + conclusion): remaining papers
- Group into: Background | Methods | Results to compare | Applications

**Output of Stage 2:**
- `project/literature_notes.md` — per-paper 3-line summary + key claim
- `project/citation_matrix.md` — which papers support which claims
- `project/gap_analysis.md` — what is missing that this paper fills

**PAUSE: Share `outline.md` + `gap_analysis.md` with user for confirmation.**

---

## Stage 3 — Figure Generation

Read `references/figure-guidelines.md` for journal-specific style rules.

For each figure:
1. Write a Python script in `project/figures/fig_XX.py` using matplotlib
2. Run script to produce `project/figures/fig_XX.pdf` (vector, journal-ready)
3. For placeholder figures (no data yet): generate `\placeholder{Description}` macro in LaTeX

Data handling:
- CSV → pandas → matplotlib
- numpy arrays → load with `np.load` or `np.loadtxt`
- Experimental images → use as-is, add scale bar annotation

**PAUSE: Show user figure previews before writing.**

---

## Stage 4 — LaTeX Writing

Read `references/journal-styles.md` for target journal template and style notes.
Use template from `assets/templates/` matching the target journal.

**Writing order:**
1. Abstract (last, but stub first)
2. Introduction (establish gap → our approach → overview)
3. Methods / Experimental
4. Results and Discussion (section by section, tie to figures)
5. Conclusion
6. Abstract (final version)
7. Supplementary Information (if needed)

**Citation discipline:**
- Always cite using `\cite{key}` from `refs.bib`
- Cite 2–4 papers per key claim
- Use `\citep` for parenthetical, `\citet` for narrative

Write section by section. Save each as `project/sections/XX_intro.tex` etc., then assemble.

---

## Stage 5 — Compile

```bash
cd project && latexmk -pdf -bibtex main.tex
```

Or use `scripts/compile_paper.sh`. Troubleshoot common errors:
- Missing packages → add to preamble
- Bad citation keys → check `refs.bib` key consistency
- Overfull hbox → add `\sloppy` or reword

Final: check page count, figure count, reference count vs journal requirements.

---

## Stage 6 — Simulated Peer Review

Spawn a sub-agent with this prompt:
> "You are a peer reviewer for [TARGET JOURNAL]. Read this paper and write 3 detailed referee reports. Be specific: cite line numbers, equations, figures. Mix major and minor comments. Be critical but constructive. Style should match [TARGET JOURNAL]'s reviewer culture."

- Reviewer 1: methodology + novelty focus
- Reviewer 2: data quality + reproducibility focus  
- Reviewer 3: clarity + significance focus

Compile reviews into `project/review_reports.pdf` using `assets/templates/review_template.tex`.

---

## Final Delivery

Package and deliver:
```
project/
├── main.tex              ← full LaTeX source
├── main.pdf              ← compiled paper
├── refs.bib              ← bibliography
├── figures/              ← all figure scripts + PDFs
├── sections/             ← individual section .tex files
├── SI.tex                ← supplementary (if applicable)
├── review_reports.pdf    ← 3 simulated referee reports
└── OVERVIEW.md           ← project summary
```

Send as zip: `scripts/package_output.sh`

---

## Reference Files

- `references/journal-styles.md` — templates, word limits, figure rules per journal
- `references/figure-guidelines.md` — matplotlib style, color palettes, font sizes
- `references/physics-writing-guide.md` — academic writing conventions for physics/materials
- `references/latex-snippets.md` — common LaTeX patterns for equations, figures, tables

## Scripts

- `scripts/export_zotero_bib.py` — export .bib from Zotero collection
- `scripts/compile_paper.sh` — latexmk compile with error reporting
- `scripts/package_output.sh` — zip final deliverables
- `scripts/check_journal_requirements.py` — word count, fig count, ref count checker
