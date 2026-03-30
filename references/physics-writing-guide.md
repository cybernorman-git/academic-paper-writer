# Physics / 2D Materials Writing Guide

## Voice and Style

- **Active voice** preferred for describing your work: "We demonstrate...", "We show...", "Our measurements reveal..."
- **Passive voice** acceptable for describing well-known results: "It has been shown that...", "Valley polarization was measured..."
- **Avoid hedging** in results: "We find X" not "It appears that X might be..."
- **Be quantitative**: always attach numbers + units to claims. "Large" → "4× enhancement". "Significant" → "12.7 percentage points"
- **First mention**: spell out all acronyms. Re-define in abstract AND body separately.

## Structure Conventions

### Title
- ≤15 words preferred
- Include material system + phenomenon + application: "[Phenomenon] in [Material] for [Application]"
- Example: "Neuromorphic Computing in Fe₃GaTe₂/WS₂ via Power-Tunable Exciton–Trion Dynamics"

### Keywords
- 5–8 keywords covering: material, phenomenon, technique, application
- Never repeat title words verbatim

### Introduction Structure
```
Para 1: Field context — why this area matters (2–3 citations per sentence)
Para 2: Specific problem — what is unsolved or suboptimal (cite gaps)
Para 3: Prior work — what others tried, why insufficient
Para 4: "Here we..." — your contribution in 3–4 sentences
(Para 5: Paper roadmap — optional for ACS; common for long PRB)
```

### Results and Discussion
- One subsection per figure (ACS style) or one per concept (Nature style)
- Subsection title: noun phrase summarizing the finding ("Valley Polarization Enhancement via Magnetic Proximity")
- First sentence of each section: states the question being answered
- Last sentence of each section: interprets the finding and/or links forward

### Conclusion
- 1–2 paragraphs
- Para 1: Summarize what was done and key numbers
- Para 2: Broader implications + outlook (1–2 sentences future work)
- Never introduce new data in conclusion

## Common Phrases by Section

### Introduction
```
"Two-dimensional (2D) van der Waals heterostructures have emerged as..."
"Among the properties of TMDs, the valley degree of freedom..."
"Despite these advances, achieving X without Y remains challenging."
"Here we demonstrate all-optical [X] in a [material] heterostructure,
where [mechanism] enables [outcome]."
```

### Results
```
"Figure 1 shows the [quantity]-dependent [measurement] of [system]."
"Two distinct emission features are resolved: [X] at [λ1] and [Y] at [λ2]."
"The degree of circular polarization (DOCP) is defined as..."
"Critically, [quantity] exhibits [behavior] — a signature of [mechanism]."
"This [X]-fold enhancement is consistent with [prior work]."
```

### Discussion / Interpretation
```
"The monotonic increase of [X] with [Y] reflects [physical mechanism]."
"This behavior is analogous to [prior work], where [similar mechanism] was reported."
"We attribute the observed [X] to [mechanism], as supported by [evidence]."
"These results establish [material] as a candidate for [application]."
```

### Conclusion
```
"In summary, we have demonstrated [what] in [system] by [how]."
"The [key result: number] improvement over [baseline] establishes [implication]."
"Our results open a route toward [future direction]."
```

## Equations

- Number only equations that are referenced in the text
- Define all symbols immediately after the equation
- Use consistent notation throughout (define in first use, stick to it)
- Common physics notation:
  - Valley polarization: $P = (I_{\sigma^+} - I_{\sigma^-})/(I_{\sigma^+} + I_{\sigma^-})$
  - Degree of circular polarization: DOCP or $\rho_c$
  - Hamiltonian: $\hat{H}$
  - Expectation value: $\langle \hat{O} \rangle$

## Units and Numbers

- SI units always; Gaussian only when field-standard (e.g., magnetic field in T for vdW magnets)
- Numbers < 10: spell out in prose ("three measurements"), use numeral with units ("3 mT")
- Ranges: "25–600 μW" not "25-600 μW" (use en-dash)
- Uncertainties: "87.5 ± 2.1%" or "(87.5 ± 2.1)%"
- Significant figures: match measurement precision

## References

- Cite 2–4 papers per factual claim
- Cite original discovery + recent reviews
- For materials/methods: cite synthesis paper + characterization paper
- Never cite only a review when the original paper exists
- Self-citations: ≤ 10–15% of total, only when directly relevant

## 2D Materials Specific Conventions

| Concept | Preferred notation |
|---------|-------------------|
| Monolayer | "monolayer WS₂" not "single-layer" |
| Heterostructure | "vdW heterostructure" or "van der Waals heterostructure" |
| Valley index | K and K' (or +K and −K) |
| Exciton species | X⁰ (neutral), X⁻ (trion), X_D (dark) |
| Magnetic anisotropy | "perpendicular magnetic anisotropy (PMA)" |
| PL peak attribution | "A-exciton" or "X⁰" not "exciton peak" |
| Curie temperature | T_C (not Tc or Tc) |
| Spin-orbit coupling | SOC |
| Degree of circular polarization | DOCP |
