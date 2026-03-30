# Figure Guidelines

## General Principles

- Vector formats (PDF, EPS, SVG) always preferred over raster
- Raster: minimum 300 dpi for print, 600 dpi for line art
- All fonts embedded; use Helvetica/Arial or DejaVu Sans (avoid CM/LaTeX fonts in figures)
- Color: use colorblind-safe palettes (see below)
- Panel labels: bold uppercase (a), (b), (c) in top-left corner

## Matplotlib Setup (Standard Template)

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Journal-quality settings
mpl.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'lines.linewidth': 1.5,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.top': True,
    'ytick.right': True,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,
})

# Column widths (inches)
ONE_COL = 3.37   # single column
TWO_COL = 6.85   # double column (ACS/APS)
NATURE_COL = 7.09  # Nature full width
```

## Colorblind-Safe Palettes

```python
# Wong palette (colorblind safe, 8 colors)
WONG = ['#000000', '#E69F00', '#56B4E9', '#009E73',
        '#F0E442', '#0072B2', '#D55E00', '#CC79A7']

# For valley polarization plots (σ+/σ-)
SIGMA_PLUS  = '#D55E00'   # orange-red
SIGMA_MINUS = '#0072B2'   # blue

# For exciton/trion distinction
EXCITON_COLOR = '#0072B2'   # blue
TRION_COLOR   = '#D55E00'   # orange

# Diverging (for maps, polarization, Zeeman)
import matplotlib.cm as cm
DIVERGING = cm.RdBu_r
```

## Common Figure Types in Physics/2D Materials Papers

### PL Spectrum Figure
```python
fig, ax = plt.subplots(figsize=(ONE_COL, 2.5))
ax.plot(wavelength, intensity_plus, color=SIGMA_PLUS, label=r'$\sigma^+$')
ax.plot(wavelength, intensity_minus, color=SIGMA_MINUS, label=r'$\sigma^-$', ls='--')
ax.set_xlabel('Wavelength (nm)')
ax.set_ylabel('PL Intensity (a.u.)')
ax.legend(frameon=False)
# Annotate peaks:
ax.annotate('X$^0$', xy=(x0, y0), xytext=(x0+5, y0*1.1),
            arrowprops=dict(arrowstyle='->', color='black', lw=0.8))
```

### Multi-panel Figure
```python
fig, axes = plt.subplots(1, 3, figsize=(TWO_COL, 2.2))
# Panel labels:
for i, ax in enumerate(axes):
    ax.text(-0.18, 1.02, '(' + 'abcde'[i] + ')',
            transform=ax.transAxes, fontweight='bold', fontsize=9)
```

### Colormap/2D Map Figure
```python
fig, ax = plt.subplots(figsize=(ONE_COL, 2.5))
im = ax.imshow(data, cmap=DIVERGING, aspect='auto',
               extent=[x_min, x_max, y_min, y_max], origin='lower')
cbar = fig.colorbar(im, ax=ax, shrink=0.85)
cbar.set_label('DOCP (%)', fontsize=8)
```

### Error Bars / Scatter
```python
ax.errorbar(x, y, yerr=err, fmt='o', color=WONG[1],
            capsize=3, capthick=0.8, elinewidth=0.8, ms=4)
```

## Schematic / Device Diagrams

For device schematics (heterostructure cross-sections, band diagrams):
- Use Inkscape or matplotlib patches
- Script in `fig_schematic.py` using `matplotlib.patches`
- Or provide placeholder: `\includegraphics[width=\columnwidth]{figures/schematic_placeholder}`

```python
# Band diagram example
from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots(figsize=(ONE_COL, 2.5))
# Draw bands as horizontal bars
ax.fill_betweenx([0, 0.3], -0.5, 0.5, alpha=0.3, color=WONG[2], label='CB')
ax.fill_betweenx([-0.8, -0.5], -0.5, 0.5, alpha=0.3, color=WONG[1], label='VB')
ax.set_ylabel('Energy (eV)')
ax.set_xticks([])
```

## Saving Figures

```python
fig.savefig('figures/fig_01.pdf', format='pdf')
fig.savefig('figures/fig_01.png', format='png', dpi=300)
plt.close()
```

## LaTeX Figure Environment

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=\columnwidth]{figures/fig_01.pdf}
  \caption{\textbf{Title of figure.} (a) Description of panel a.
           (b) Description of panel b. Scale bar: 1~$\mu$m.}
  \label{fig:label}
\end{figure}
```

For two-column spanning figure:
```latex
\begin{figure*}[htbp]
  ...
\end{figure*}
```
