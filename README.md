# academic-paper-writer

An OpenClaw skill for end-to-end academic paper writing — targeted at physics, 2D materials, optics, and condensed matter research.

## What It Does

Full pipeline from idea to submission-ready package:

1. **Literature Collection** — Searches and adds ≥30 papers to Zotero
2. **Literature Synthesis** — Reads PDFs, extracts key claims, identifies research gaps
3. **Figure Generation** — Python/matplotlib scripts producing journal-quality figures
4. **LaTeX Writing** — Full paper in target journal style (ACS, APS, Nature, etc.)
5. **Compilation** — `latexmk` compile with error reporting
6. **Peer Review Simulation** — 3 realistic referee reports as PDF

## Supported Journals

| Journal | Key |
|---------|-----|
| Nano Letters | `nano-letters` |
| ACS Nano | `acs-nano` |
| Physical Review B | `prb` |
| Physical Review Letters | `prl` |
| Nature | `nature` |
| Nature Photonics | `nature-photonics` |
| Nature Communications | `nature-comms` |
| Advanced Materials | `advanced-materials` |

## Installation

### Via OpenClaw / ClawHub
```bash
clawhub install academic-paper-writer
```

### Manual
```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/cybernorman-git/academic-paper-writer
```
Then restart your OpenClaw gateway.

## Requirements

- [OpenClaw](https://openclaw.ai) agent framework
- [uv](https://github.com/astral-sh/uv) (Python runner)
- `latexmk` + LaTeX distribution (for compilation)
  - macOS: `brew install --cask mactex-no-gui`
  - Linux: `sudo apt install texlive-full`
- Zotero account with API key (set `ZOTERO_CREDENTIALS=userID:apiKey`)

## Usage

Just tell your OpenClaw agent:

> "I want to write a paper on [topic] targeting [journal]. Here's my data: [files]"

The skill activates automatically and guides you through each stage with human-in-the-loop checkpoints.

## Included Files

```
academic-paper-writer/
├── SKILL.md                         ← Main skill instructions (6-stage workflow)
├── references/
│   ├── journal-styles.md            ← Templates & style rules per journal
│   ├── figure-guidelines.md         ← matplotlib templates, color palettes
│   ├── physics-writing-guide.md     ← Academic writing conventions
│   └── latex-snippets.md            ← Ready-to-use LaTeX patterns
├── scripts/
│   ├── export_zotero_bib.py         ← Export Zotero collection → refs.bib
│   ├── compile_paper.sh             ← latexmk compile with error reporting
│   ├── check_journal_requirements.py ← Word/figure/ref count checker
│   └── package_output.sh            ← Zip final deliverables
└── assets/templates/
    ├── acs_template.tex             ← ACS Nano / Nano Letters
    ├── aps_template.tex             ← PRB / PRL
    └── review_template.tex          ← Peer review reports
```

## License

MIT
