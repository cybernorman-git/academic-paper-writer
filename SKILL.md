---
name: academic-paper-writer
description: Data-driven academic paper writing workflow for experimental physics, photonics, 2D materials, and condensed matter. User provides experimental data; agent handles story architecture, figure generation, LaTeX writing, consistency checking, and simulated peer review. Use when: (1) user has experimental data and wants a full paper drafted; (2) user asks to write a paper targeting ACS Nano, Nano Letters, ACS Photonics, PRB, PRL, APL, Nature, Science, Science Advances, Nature Photonics, eLight, Advanced Materials, AFM, or similar journals; (3) user provides figures/data + paper structure and wants it written up; (4) user needs revisions based on reviewer comments.
---

# Academic Paper Writer

A data-first, story-driven workflow. The user brings experimental data and results.
The agent builds the story, generates publication-quality figures, writes the LaTeX, checks
consistency, and runs simulated peer review.

---

## Core Philosophy

1. **Data-first**: No writing until data is inventoried and audited.
2. **Story-first**: No LaTeX until the narrative arc is confirmed by the user.
3. **One section at a time**: Write, confirm, move on. Never race ahead.
4. **Log every decision**: `paper.log.md` is the paper's memory.
5. **Iterate, don't linear-pipeline**: Revision loops are first-class, not afterthoughts.

---

## Commands

```
/paper setup    → Create paper.config.md + data/DATA_MANIFEST.md
/paper audit    → Scan data, check completeness, flag gaps before writing
/paper story    → Build the figure arc and narrative spine; confirm with user
/paper figures  → Generate all figures from data (matplotlib, journal style)
/paper draft    → Write LaTeX section by section
/paper check    → Internal consistency audit (numbers, claims, refs, limits)
/paper review   → Spawn 3 simulated peer reviewers
/paper revise   → Address reviewer comments; log changes in paper.log.md
/paper pack     → Assemble and zip final submission package
```

If no command is given:
- If `paper.config.md` does not exist → run `/paper setup`
- If `paper.config.md` exists but `story.md` does not → run `/paper story`
- If `story.md` exists → ask user which stage to continue from

---

## Project Layout

```
project/
├── paper.config.md          ← journal, scope, word/figure limits, constraints
├── story.md                 ← core claim, figure arc, novelty, "so what"
├── paper.log.md             ← decision journal: every major choice recorded
├── data/
│   ├── raw/                 ← original data files exactly as received from user
│   ├── processed/           ← cleaned/derived data (do not overwrite raw/)
│   └── DATA_MANIFEST.md     ← inventory: what each file is, experiment conditions
├── figures/
│   ├── fig_01.py            ← matplotlib script for Figure 1
│   ├── fig_01.pdf           ← compiled figure (vector, journal-ready)
│   └── ...
├── sections/
│   ├── 00_abstract_stub.tex
│   ├── 01_intro.tex
│   ├── 02_methods.tex
│   ├── 03_results.tex
│   ├── 04_discussion.tex
│   ├── 05_conclusion.tex
│   └── 06_abstract_final.tex
├── main.tex                 ← assembled document
├── SI.tex                   ← supplementary information (if needed)
├── refs.bib                 ← bibliography
└── review/
    ├── round1_reports.md    ← simulated referee reports
    └── round1_response.tex  ← point-by-point response letter
```

---

## `/paper setup`

**Goal**: Define the project before touching any data or writing.

Ask the user for (or infer from context):

```
1. Research topic / working title
2. Target journal → look up in references/journal-styles.md for limits
3. Manuscript type (Article / Letter / Communication / Review)
4. Data available: list all files the user will provide (names, formats, brief description)
5. Rough figure count and what each figure should show
6. Any special constraints (co-author requirements, SI policy, page limit, submission deadline)
7. Prior work this paper extends or competes with (2–5 key references)
```

**Output — `paper.config.md`:**

```markdown
# Paper Configuration

## Identity
- Working title: [title]
- Target journal: [journal]
- Manuscript type: [Article / Letter / Communication]
- Submission deadline: [date or TBD]

## Journal Limits (from journal-styles.md)
- Word limit: [X words]
- Figure limit: [N figures]
- Reference limit: [~N refs]
- Abstract limit: [N words]
- Template file: assets/templates/[template].tex

## Data Inventory (preliminary)
- [filename]: [brief description]
- [filename]: [brief description]

## Planned Figures
- Fig 1: [what it shows]
- Fig 2: [what it shows]
- ...

## Key Prior Work
- [Author Year]: [one-line summary]
- ...

## Constraints
- [any special constraints]
```

**Output — `data/DATA_MANIFEST.md`:** (skeleton; filled during `/paper audit`)

**Output — `paper.log.md`:** Initialize with date + journal + core scope.

**→ PAUSE: Confirm paper.config.md with user before proceeding.**

---

## `/paper audit`

**Goal**: Understand the data completely before building any figures or narrative.
This is the most important stage. Catches missing data before writing begins.

Steps:

1. **Read all data files** the user has provided (CSV, spectra, images, numpy arrays, raw figures).
2. **Fill in `data/DATA_MANIFEST.md`** with full detail:

```markdown
# Data Manifest

## [filename.csv]
- Type: PL spectra / Raman / transport / SEM image / ...
- Sample: [sample ID, material, conditions]
- Experiment: [what was measured, how]
- Key values: [peak positions, intensities, key numbers]
- Quality notes: [n replicates, noise level, any caveats]
- Supports claim: [which story.md claim this data backs up]
```

3. **Run the audit checklist:**

```
□ Every planned figure has data behind it
□ Every key quantitative claim has a data source
□ Error bars / statistics: n is stated and appropriate
□ Control / reference samples present where needed
□ Units are consistent across all files
□ Any unexplained outliers flagged
□ Missing data explicitly noted (not silently ignored)
```

4. **Report findings to user:**
   - ✅ Data that is complete and ready
   - ⚠️ Data that is present but weak (low n, no control, high noise)
   - ❌ Claims in the plan that have no supporting data

**→ PAUSE: Show audit report. If any ❌ gaps exist, discuss with user before proceeding.**

Log the audit summary in `paper.log.md`.

---

## `/paper story`

**Goal**: Define the narrative spine of the paper. No LaTeX until story is confirmed.

The story is the answer to: **"What is the one thing this paper proves, and how do the figures lead the reader there?"**

Build `story.md`:

```markdown
# Paper Story

## Core Claim (one sentence)
[The single most important finding. E.g.:
"We demonstrate that [material X] exhibits [property Y] due to [mechanism Z],
achieving [quantified result] which enables [application]."]

## Novelty vs. Prior Work
- Prior work showed: [what was known]
- Gap: [what was missing / not demonstrated]
- This paper adds: [specific new contribution]

## "So What" (significance)
[Why does this matter to the field? What does it enable?]

## Figure Arc (the story in N figures)
- Fig 1 — [Setup/Context]: Shows [what] to establish [why it's the right system]
- Fig 2 — [Main result]: Demonstrates [key finding] quantified as [number]
- Fig 3 — [Mechanism/Evidence]: Explains [why] via [supporting data]
- Fig 4 — [Generality/Application]: Shows [broader relevance or device demo]
- Fig 5 — [if needed]

## Section Map
- Introduction: establishes gap, previews our approach
- [Methods/Experimental]: [key techniques]
- Results: follows figure arc exactly
- Discussion: interprets mechanism, compares to literature
- Conclusion: restates core claim + outlook

## Keywords (5–6)
[keyword1, keyword2, ...]
```

**→ PAUSE: Share story.md with user. Do not proceed until story is explicitly approved.**
Log the approved story in `paper.log.md`.

---

## `/paper figures`

**Goal**: Generate all figures from data. Figures define what gets written.

Read `references/figure-guidelines.md` for matplotlib style standards.
Read the target journal entry in `references/journal-styles.md` for size/format rules.

For each figure:

1. **Write script** `figures/fig_XX.py` using the standard matplotlib template
2. **Run script** to produce `figures/fig_XX.pdf` (vector) + `figures/fig_XX.png` (preview)
3. **Review with user**: show the PNG preview, confirm panel content and labels
4. **Finalize**: adjust after feedback, log changes in `paper.log.md`

Figure discipline:
- Every panel must map directly to a claim in `story.md`
- Panel labels: **(a) (b) (c)** bold, top-left, consistent across all figures
- All axes labeled with units; all spectra labeled (X⁰, X⁻, etc.)
- Error bars mandatory if data is statistical; state n in caption
- Color: use Wong colorblind-safe palette from `references/figure-guidelines.md`
- No 3D plots unless absolutely necessary; prefer 2D projections

Raw experimental images (SEM, AFM, optical):
- Use as-is from `data/raw/`
- Add scale bar in matplotlib if not already embedded
- Do not alter contrast/brightness beyond what is physically justified

**→ PAUSE: All figures must be user-approved before drafting begins.**

---

## `/paper draft`

**Goal**: Write the LaTeX, section by section, tightly coupled to `story.md` and approved figures.

Read `references/journal-styles.md` for the target journal style.
Use the correct template from `assets/templates/` (see `paper.config.md`).

**Writing order:**

```
1. Abstract stub          (placeholder; final version written last)
2. Introduction           (gap → prior work → our approach → paper outline)
3. Experimental / Methods (what was done, how, equipment, parameters)
4. Results (+ Discussion if combined)  ← longest section; one subsection per figure
5. Discussion             (if separate: mechanism, comparison, implications)
6. Conclusion             (restate core claim + numbers + outlook)
7. Abstract — final       (written after everything else; follow journal word limit)
8. SI                     (if needed; reference from main text)
```

**Per-section rules:**

- Every results paragraph follows: *[topic sentence] → [key number + units] → [physical interpretation] → [Figure reference] → [implication]*
- Every claim cites ≥2 references from `refs.bib`
- Every figure is introduced by text *before* it appears in the document
- Do not write a section until the figure(s) for that section are approved
- Save each section as `sections/XX_sectionname.tex`; assemble into `main.tex`

**→ PAUSE after each section**: Show draft, wait for user feedback, revise, then log changes before moving to the next section.

**Citation discipline:**
- Build `refs.bib` as you write; use `zotero-scholar` skill if literature search needed
- Key: `AuthorYYYY` format (e.g., `Zhang2023`)
- Cite 2–4 papers per key claim; do not over-cite filler statements

---

## `/paper check`

**Goal**: Internal consistency audit before peer review. Catches embarrassing errors.

Run through every item in this checklist and report findings:

```
NUMBERS & CLAIMS
□ Every number in the abstract appears verbatim in the main text
□ Every quantitative claim in Results is supported by a figure or table
□ Units are consistent (SI throughout; no mixing nm/Å, meV/cm⁻¹ without conversion)
□ All equations are numbered if referenced; unnumbered if not

FIGURES
□ Figures are cited in order (Fig. 1 before Fig. 2, etc.)
□ Every figure is cited at least once in the text
□ Every panel label (a,b,c) is described in the caption
□ Figure captions are self-contained (reader shouldn't need the main text)

REFERENCES
□ Every \cite{key} in main.tex has an entry in refs.bib
□ No duplicate reference entries
□ All prior work mentioned in Introduction is cited

JOURNAL LIMITS (from paper.config.md)
□ Abstract word count ≤ limit
□ Main text word count ≤ limit (run: texcount main.tex)
□ Figure count ≤ limit
□ Reference count ≈ expected range

STRUCTURE
□ Abstract follows the journal formula (see journal-styles.md)
□ Methods/Experimental section has enough detail for reproducibility
□ Acknowledgments include funding grant numbers
□ Author contributions / conflict of interest included if required
```

Report: ✅ passes, ⚠️ warnings, ❌ errors.
Fix all ❌ before moving to `/paper review`.
Log check results in `paper.log.md`.

---

## `/paper review`

**Goal**: Simulate peer review before actual submission.

Spawn a sub-agent for each reviewer with this prompt template:

> "You are Reviewer [N] for [TARGET JOURNAL]. Your expertise is [focus area].
> Read the following paper carefully and write a detailed referee report.
> Structure: Summary (2–3 sentences) → Major concerns (numbered) → Minor concerns (numbered) → Recommendation.
> Be specific: cite figure numbers, line numbers, equations. Mix major and minor.
> Be critical but constructive. Match the culture of [TARGET JOURNAL]."

Reviewer assignments:
- **Reviewer 1** — Novelty & significance: Is the advance real? Is it impactful?
- **Reviewer 2** — Data quality & reproducibility: Are the controls adequate? Is n sufficient? Are the conclusions overreaching the data?
- **Reviewer 3** — Clarity & presentation: Is the story clear? Are figures readable? Is the writing precise?

Save all three reports in `review/round1_reports.md`.

**→ PAUSE: Share reports with user. Discuss which comments to address.**

---

## `/paper revise`

**Goal**: Address reviewer comments systematically, with a tracked response letter.

Steps:

1. For each reviewer comment, classify:
   - **Address fully** (revise the paper)
   - **Address partially** (explain limitation in response)
   - **Politely decline** (defend original approach with evidence)

2. For every revision made to the paper:
   - Edit the relevant `sections/XX.tex` file
   - Note the change in `paper.log.md` with format:
     ```
     [REVISION] Rev1 Comment 3 → Changed Fig 2c to show error bars (n=5). Added sentence to Methods.
     ```

3. Write `review/round1_response.tex` — point-by-point response letter:
   ```
   Reviewer 1, Comment 1:
   [Quote the comment]
   Response: [Your response]
   Changes: [What was changed, where in the manuscript]
   ```

4. After all revisions: re-run `/paper check` to ensure no new inconsistencies.

**→ PAUSE after drafting the response letter. Confirm with user before finalizing.**

---

## `/paper pack`

**Goal**: Assemble the final submission package.

Run `scripts/compile_paper.sh` to produce `main.pdf`.
Run `scripts/check_journal_requirements.py` for final word/figure/ref count.

Package contents:
```
submission/
├── main.tex              ← full LaTeX source
├── main.pdf              ← compiled paper
├── refs.bib              ← bibliography
├── figures/              ← all figure PDFs
├── sections/             ← individual section .tex files
├── SI.tex + SI.pdf       ← supplementary (if applicable)
├── cover_letter.tex      ← cover letter draft
└── review/               ← response letter (for revisions)
```

Run `scripts/package_output.sh` to create `submission.zip`.

Cover letter must include (for ACS/Wiley/Springer):
- Why this work is suitable for [TARGET JOURNAL]
- Key advance vs. state of the art (2–3 bullet points)
- Statement that the work is original and not under review elsewhere
- Suggested reviewers (optional but recommended)

---

## Reference Files

- `references/journal-styles.md` — templates, word limits, figure rules, tone for each journal
- `references/figure-guidelines.md` — matplotlib setup, color palettes, figure types
- `references/physics-writing-guide.md` — academic writing conventions
- `references/latex-snippets.md` — common LaTeX patterns

## Scripts

- `scripts/compile_paper.sh` — latexmk compile with error reporting
- `scripts/package_output.sh` — zip final deliverables
- `scripts/check_journal_requirements.py` — word count, fig count, ref count checker
- `scripts/export_zotero_bib.py` — export .bib from Zotero (if literature search needed)

## Templates

See `assets/templates/` for journal-specific LaTeX templates:
- `acs_template.tex` — ACS Nano, Nano Letters, ACS Materials Lett.
- `acs_photonics_template.tex` — ACS Photonics
- `aps_template.tex` — PRB, PRL
- `apl_template.tex` — Applied Physics Letters
- `science_advances_template.tex` — Science Advances
- `elight_template.tex` — eLight
- `afm_template.tex` — Advanced Functional Materials
- `review_template.tex` — reviewer response letter
