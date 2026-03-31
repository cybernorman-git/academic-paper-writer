# Journal Styles Reference

## Quick Reference Table

| Journal | Template file | LaTeX class | Word Limit | Figures | Refs | Format |
|---------|--------------|-------------|-----------|---------|------|--------|
| ACS Nano | acs_template.tex | achemso (ancac3) | 6000–8000 | 5–8 | ~60 | 2-col |
| Nano Letters | acs_template.tex | achemso (nalefd) | 4000–5000 | 4–6 | ~50 | 2-col |
| **ACS Photonics** | **acs_photonics_template.tex** | **achemso (apchd5)** | **5000–7000** | **5–8** | **~60** | **2-col** |
| Phys. Rev. B (PRB) | aps_template.tex | revtex4-2 (prb) | ~8000 | 6–10 | ~80 | 2-col |
| Phys. Rev. Lett. (PRL) | aps_template.tex | revtex4-2 (prl) | ~3500 | 4 | ~30 | 2-col |
| **APL** | **apl_template.tex** | **revtex4-2 (aip,apl)** | **≤4 pages** | **≤3** | **~30** | **2-col** |
| Nature | — | article + natbib | ~3000 body + SI | 4–6 | ~50 | 1-col |
| Science | — | article | ~4500 | 4–6 | ~40 | 2-col |
| **Science Advances** | **science_advances_template.tex** | **article (AAAS)** | **no hard limit** | **5–8** | **~60** | **1-col** |
| Nature Photonics | — | article + natbib | ~3000 + SI | 4–6 | ~60 | 1-col |
| Nature Communications | — | article + natbib | ~5000 | 6–8 | ~60 | 1-col |
| Advanced Materials | — | wiley/article | ~5000 | 4–8 | ~60 | 2-col |
| **Adv. Functional Mater. (AFM)** | **afm_template.tex** | **article (Wiley)** | **Full: ~8000 / Comm: ~4000** | **4–6** | **~60** | **2-col** |
| **eLight** | **elight_template.tex** | **sn-jnl (Springer)** | **~5000** | **5–8** | **~60** | **1-col** |
| ACS Materials Lett. | acs_template.tex | achemso | 3500 | 4 | ~35 | 2-col |

---

## ACS Journals (Nano Letters, ACS Nano)

**Template:** `achemso` package

```latex
\documentclass[journal=nalefd,manuscript=article]{achemso}
% For ACS Nano: journal=ancac3
```

**Style notes:**
- American English
- Title case for title
- Abstract: ≤150 words, no citations
- "We demonstrate..." or "Here we show..." opening
- Results and Discussion combined into one section
- References: `\bibstyle{achemso}`, numbered superscript in text
- Equation numbering: only if referenced
- SI note at end: "Supporting Information Available: ..."
- Figures: TIFF/PDF, 300 dpi min, 3.25" (1-col) or 7" (2-col) wide

**Tone:** Direct, confident, results-first. First sentence of abstract states the key result.

---

## APS Journals (PRB, PRL)

**Template:** `revtex4-2` package

```latex
\documentclass[aps,prb,twocolumn,showpacs,preprintnumbers,amsmath,amssymb]{revtex4}
% For PRL: replace prb with prl
```

**Style notes:**
- American English
- Abstract as single paragraph, ≤600 words (PRB) / ≤600 chars (PRL)
- "We" is acceptable; passive voice also common
- Introduction should cite heavily
- Section headers: \section{}, numbered
- Figures float; caption with Fig. X (not Figure)
- Physical quantities: SI units required; Gaussian for EM if traditional
- References: numbered, [1] style in text
- Acknowledgments before references

**PRL specific:** 4 pages strict. Impact statement required. Lead paragraph must be self-contained.

---

## Nature Family (Nature, Nature Photonics, Nature Comms)

**Template:** Use `nature` class or just article with custom formatting

```latex
\documentclass[letterpaper, 10pt]{article}
\usepackage{natbib}
```

**Style notes:**
- Results section: no subheadings in Letter format
- Methods: at end (or SI for Letters)
- Abstract ≤200 words (Letters) — 3 sentences: context, result, implications
- No equation numbers unless referenced
- "Authors" anonymous in submitted version
- "Here we report..." / "We show..." opening
- Figures: print-quality, 180mm wide max, Helvetica/Arial font
- Extended Data: max 10 items (figures/tables)

---

## Writing Style Patterns by Journal

### Results paragraph template (universal)
```
[Topic sentence: what you measured/showed]
[Key result: number + units + comparison]  
[Interpretation: physical mechanism]
[Link to figure: as shown in Fig. X]
[Implication: why this matters]
```

### Introduction structure (universal)
1. Broad context (2–3 sentences)
2. Specific problem / gap (2–3 sentences, cite heavily)
3. Prior approaches and their limitations (3–5 sentences)
4. "Here we..." — what this paper does (2–3 sentences)
5. Brief outline of results / paper structure (optional, ACS-style)

### Abstract formula (ACS/APS)
1. Context sentence (why this field matters)
2. Problem sentence (what's missing)
3. Approach sentence (what we did)
4. Key result sentence (main number/finding)
5. Significance sentence (implications)

---

## ACS Photonics

**Template file:** `assets/templates/acs_photonics_template.tex`
**LaTeX class:** `achemso`, journal code `apchd5`

```latex
\documentclass[journal=apchd5,manuscript=article]{achemso}
% manuscript=letter for shorter communications
```

**Style notes:**
- Same achemso family as ACS Nano / Nano Letters
- Abstract ≤250 words; no citations, no uncommon abbreviations
- Title must NOT contain: New, Novel, First, Superb, Excellent, Exceptional, Outstanding
- No acronyms in title unless universally known
- TOC graphic required (5.5 cm × 5 cm); ≤50 words of caption
- Results and Discussion combined in one section
- Experimental Section placed after Conclusion
- Supporting Information uploaded as separate file
- Cover letter must explain novelty vs. state of the art and confirm no prior publication
- Figures: TIFF/PDF 300 dpi min; 3.25" (1-col) or 7" (2-col)

**Tone:** Optics/photonics community; more device/application oriented than ACS Nano;
highlight photonic mechanism + practical demonstration. Results-first abstract.

---

## APL (Applied Physics Letters)

**Template file:** `assets/templates/apl_template.tex`
**LaTeX class:** `revtex4-2` with `aip,apl` options (AIP Publishing template)

```latex
\documentclass[aip,apl,amsmath,amssymb,reprint,groupedaddress]{revtex4-2}
```

**Style notes:**
- Strict ≤4 published pages including figures and references
- Letter format: no separate Methods section; methods woven into narrative
- Abstract: single paragraph ≤250 words; no displayed equations, refs, or graphics
- Must present a "single clear point" — one central result
- Language: American English
- Figures: typically ≤3 for a 4-page letter
- Significance beyond narrow specialty must be clear in abstract and conclusion
- No dedicated Introduction/Results/Conclusion headers required; use narrative flow
- References: numerical [1] style

**Tone:** Concise, physics-forward. Every sentence must earn its place.
Cut anything that doesn't directly support the central result.

---

## Science Advances

**Template file:** `assets/templates/science_advances_template.tex`
**LaTeX class:** AAAS article class (download from Overleaf AAAS gallery)

```latex
\documentclass[10pt]{article}  % use official AAAS template for final submission
```

**Style notes:**
- Title: declarative phrase, no punctuation; 7–25 words; full ≤100 chars, short ≤40 chars
- Abstract: 200–400 words; single paragraph; no citations, no footnotes
- Section numbering: up to 3 levels (1. / 1.1. / 1.1.1.)
- Figures embedded in body; captions start with bold **Figure X.**; panels labeled lowercase (a, b, c)
- Conclusion section is optional
- Materials and Methods placed after Discussion
- Back matter: Acknowledgments → Author Contributions → Competing Interests → Data Availability → References
- Datasets should be cited in the reference list with a [dataset] tag
- SI units throughout; SI file uploaded separately
- Equations numbered at right (1), (2), ...
- Abbreviations defined in parentheses on first use (in abstract AND main text separately)

**Tone:** Broad interdisciplinary audience (Science family); frame significance widely.
Results should be clearly impactful beyond a narrow subfield. Data quality and reproducibility are closely scrutinized.

---

## eLight

**Template file:** `assets/templates/elight_template.tex`
**LaTeX class:** `sn-jnl` (Springer Nature journal class)

```latex
\documentclass[lineno]{sn-jnl}
% Download sn-jnl.cls: https://www.springernature.com/gp/authors/campaigns/latex-author-support
```

**Style notes:**
- Open access; co-published by Springer Nature + Light Publishing Group (CIOMP, Changchun)
- Double-blind peer review for initial submission: **remove all author info, funding, acknowledgments**
- Abstract ≤200 words; no citations; minimize abbreviations; keywords: 3–10
- Figures: ≥300 dpi; multi-panel combined into one composite file; uploaded separately through submission portal
- Figure panels labeled **a**, **b**, **c** (bold, not parenthesized)
- Competing interests section mandatory at end
- References: numbered [1] style
- Section structure: Introduction → Results → Discussion → Conclusion → Methods → Declarations
- Perspectives/Reviews by invitation; Research Articles are the primary type

**Tone:** High-impact photonics/optics journal. Aims for Nature Photonics-level work.
Emphasize novelty, physical insight, and broad relevance to the light-science community.
Strong preference for work combining theory, experiment, and applications.

---

## Advanced Functional Materials (AFM)

**Template file:** `assets/templates/afm_template.tex`
**LaTeX class:** standard `article` (Wiley accepts LaTeX but has no dedicated class)

**Style notes:**
- Two main article types:
  - **Full Paper** ≤10 published pages (~7,500–8,000 words + figures); abstract ≤200 words
  - **Communication** ≤5 published pages (~3,500–4,000 words + figures); **opening paragraph IS the abstract** (no separate abstract block)
- Exactly **5 keywords** required
- **Graphical abstract required**: separate file, 5 × 12.7 cm, 300 dpi, summarizes functional advance
- Title and abstract must explicitly state the functional advance and quantify performance improvement
- Double spacing + line numbers throughout for review submission
- Experimental Section placed **after Conclusion**
- References: numbered [1] style; use `\cite{}`
- CRediT author contributions recommended
- Data availability statement required
- Figures: TIFF/EPS/PDF ≥300 dpi; captions as **Figure X.** bold label
- Cover letter must address: (1) functional significance, (2) novelty, (3) why suitable for AFM

**Tone:** Materials science community; mechanistic explanations for functional improvements are essential.
Comparative performance data against literature benchmarks expected.
Avoid purely phenomenological papers without clear structure–property relationships.
