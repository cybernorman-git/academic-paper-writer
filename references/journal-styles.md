# Journal Styles Reference

## Quick Reference Table

| Journal | Template | Word Limit | Figures | Refs | Format |
|---------|----------|-----------|---------|------|--------|
| ACS Nano | achemso | 6000–8000 | 5–8 | ~60 | 2-col |
| Nano Letters | achemso | 4000–5000 | 4–6 | ~50 | 2-col |
| Phys. Rev. B (PRB) | revtex4-2 | ~8000 | 6–10 | ~80 | 2-col |
| Phys. Rev. Lett. (PRL) | revtex4-2 | ~3500 | 4 | ~30 | 2-col |
| Nature | nature | ~3000 body + SI | 4–6 | ~50 | 1-col |
| Science | science | ~4500 | 4–6 | ~40 | 2-col |
| Nature Photonics | nature | ~3000 + SI | 4–6 | ~60 | 1-col |
| Nature Communications | nature | ~5000 | 6–8 | ~60 | 1-col |
| Advanced Materials | wiley | ~5000 | 4–8 | ~60 | 2-col |
| ACS Materials Lett. | achemso | 3500 | 4 | ~35 | 2-col |

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
