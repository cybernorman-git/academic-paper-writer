# Academic Paper Writer

> **You bring the data. The agent builds the story, draws the figures, writes the LaTeX, and runs peer review.**

A data-first, story-driven paper writing workflow for experimental physicists, photonics researchers, and 2D materials scientists. Designed for researchers who run their experiments first, collect their data, and then need help turning results into a publication-ready manuscript.

---

## Who this is for

- Experimental researchers (photonics, condensed matter, 2D materials, nanophotonics)
- You have already collected your data: spectra, images, transport curves, etc.
- You want to target a specific journal (ACS Photonics, APL, eLight, Science Advances, AFM, etc.)
- You need help with: story structure, figure generation, LaTeX writing, consistency checking, and peer review simulation

**This is NOT for running computational experiments or ML training loops.** For that, use `autoresearch`.

---

## How it works

```
You provide                    Agent does
─────────────────────────────────────────────────────
Raw data files (CSV,           Audits data completeness
spectra, images, etc.)    →    Flags missing controls / weak stats

Target journal + scope    →    Loads journal rules, word/fig limits

Story discussion          →    Builds story.md: core claim, figure arc,
(what does your data show?)    novelty, significance

Approve figures           →    Generates publication-quality matplotlib
                               figures (journal style, colorblind-safe)

Review each section       →    Writes LaTeX section by section,
                               pauses for your feedback after each

Final check               →    Audits numbers, units, citations,
                               figure order, word count vs. limits

Review simulation         →    3 simulated peer reviewers
                               (novelty / data quality / clarity)

Reviewer response         →    Point-by-point response letter
                               + tracked revisions in paper.log.md
```

---

## Commands

| Command | What it does |
|---|---|
| `/paper setup` | Create `paper.config.md` — journal, scope, figure plan |
| `/paper audit` | Scan your data files, check completeness, flag gaps |
| `/paper story` | Build the narrative arc; confirm before any writing |
| `/paper figures` | Generate all figures from your data |
| `/paper draft` | Write LaTeX section by section |
| `/paper check` | Internal consistency audit (numbers, refs, limits) |
| `/paper review` | Simulate 3 peer reviewers |
| `/paper revise` | Address reviewer comments + response letter |
| `/paper pack` | Assemble final submission zip |

---

## Supported Journals

| Journal | Template |
|---|---|
| ACS Nano | `acs_template.tex` |
| Nano Letters | `acs_template.tex` |
| ACS Photonics | `acs_photonics_template.tex` |
| Phys. Rev. B (PRB) | `aps_template.tex` |
| Phys. Rev. Lett. (PRL) | `aps_template.tex` |
| Applied Physics Letters (APL) | `apl_template.tex` |
| Science Advances | `science_advances_template.tex` |
| eLight | `elight_template.tex` |
| Advanced Functional Materials (AFM) | `afm_template.tex` |
| Nature / Nature Photonics / Nature Comms | use article class |
| Advanced Materials | use article class |

---

## Project structure

```
project/
├── paper.config.md       ← journal, limits, figure plan
├── story.md              ← core claim, figure arc, novelty
├── paper.log.md          ← decision journal (every choice recorded)
├── data/
│   ├── raw/              ← your original data files
│   ├── processed/        ← cleaned/derived data
│   └── DATA_MANIFEST.md  ← inventory of every data file
├── figures/              ← matplotlib scripts + output PDFs
├── sections/             ← individual .tex files per section
├── main.tex              ← assembled LaTeX document
├── refs.bib              ← bibliography
├── SI.tex                ← supplementary (if needed)
└── review/               ← peer review reports + response letter
```

---

## Reference files

- `references/journal-styles.md` — format rules, word limits, style notes for each journal
- `references/figure-guidelines.md` — matplotlib templates, colorblind-safe palettes, figure types
- `references/physics-writing-guide.md` — academic writing conventions
- `references/latex-snippets.md` — LaTeX patterns for equations, figures, tables
