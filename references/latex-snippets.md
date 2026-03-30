# LaTeX Snippets

## Standard Preamble (ACS — achemso)

```latex
\documentclass[journal=nalefd,manuscript=article]{achemso}
% nalefd = Nano Letters; ancac3 = ACS Nano; acsmfd = ACS Materials Lett.
\usepackage{amsmath,amssymb,bm}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{siunitx}
\usepackage{booktabs}
\usepackage[version=4]{mhchem}  % for chemical formulas

% Placeholder macro
\newcommand{\placeholder}[1]{%
  \begin{center}
    \fbox{\parbox{0.9\columnwidth}{\centering\textit{[FIGURE PLACEHOLDER: #1]}}}
  \end{center}
}
```

## Standard Preamble (APS — revtex4-2)

```latex
\documentclass[aps,prb,twocolumn,showpacs,amsmath,amssymb,floatfix]{revtex4-2}
% prb = PRB; prl = PRL
\usepackage{graphicx}
\usepackage{dcolumn}
\usepackage{bm}
\usepackage{hyperref}
\usepackage{siunitx}
\usepackage[version=4]{mhchem}

\newcommand{\placeholder}[1]{%
  \fbox{\parbox{0.9\columnwidth}{\centering\textit{[FIGURE: #1]}}}}
```

## Chemical Formulas

```latex
\ce{Fe3GaTe2}        % Fe₃GaTe₂
\ce{WS2}             % WS₂
\ce{MoS2}            % MoS₂
\ce{WSe2}            % WSe₂
\ce{CrI3}            % CrI₃
\ce{Fe3GeTe2}        % Fe₃GeTe₂
```

## Physics Symbols

```latex
% Valley polarization
$P = \frac{I_{\sigma^+} - I_{\sigma^-}}{I_{\sigma^+} + I_{\sigma^-}}$

% Valley Zeeman splitting
$\Delta E_Z = g_{\rm eff} \mu_B B$

% Effective g-factor
$g_{\rm eff} = -66$

% Degree of circular polarization
$\rho_c = \frac{I_{+} - I_{-}}{I_{+} + I_{-}}$

% Hamiltonian
$\hat{H} = \hat{H}_0 + \hat{H}_{\rm SOC} + \hat{H}_{\rm ex}$

% Exchange interaction
$\hat{H}_{\rm ex} = -J \sum_{\langle i,j \rangle} \hat{S}_i \cdot \hat{S}_j$

% Spin-orbit Hamiltonian (TMD)
$\hat{H}_{\rm SOC} = \frac{\lambda_{\rm SOC}}{2} \tau_z \sigma_z$
where $\tau_z = \pm 1$ is the valley index and $\sigma_z = \pm 1$ is the spin index.
```

## Figure Environments

```latex
% Single-column figure
\begin{figure}[htbp]
  \centering
  \includegraphics[width=\columnwidth]{figures/fig_01.pdf}
  \caption{\textbf{Short bold title.}
           (a) Description of panel a showing [quantity] as a function of [variable].
           (b) Description of panel b.
           Scale bar: \SI{1}{\micro\meter}.}
  \label{fig:valley_pol}
\end{figure}

% Double-column spanning figure (ACS/APS)
\begin{figure*}[htbp]
  \centering
  \includegraphics[width=\textwidth]{figures/fig_02.pdf}
  \caption{\textbf{Power-dependent optical response.}
           (a-d) PL spectra at excitation powers of
           \SI{25}{\micro\watt}, \SI{100}{\micro\watt},
           \SI{250}{\micro\watt}, and \SI{600}{\micro\watt}.}
  \label{fig:power_dep}
\end{figure*}

% Placeholder figure
\begin{figure}[htbp]
  \centering
  \placeholder{AFM topography confirming monolayer WS2 and FGaT thickness. 
               Optical micrograph of the heterostructure device.}
  \caption{\textbf{Device characterization.} [To be inserted].}
  \label{fig:device}
\end{figure}
```

## Tables

```latex
\begin{table}[htbp]
  \centering
  \caption{Summary of extracted optical features.}
  \label{tab:features}
  \begin{tabular}{llp{5cm}}
    \toprule
    Feature & Symbol & Physical origin \\
    \midrule
    A-exciton DOCP   & $P_A$     & Exciton valley polarization \\
    Trion DOCP       & $P_T$     & Trion valley polarization \\
    Exciton/trion ratio & $r_{AT}$ & Carrier density state \\
    Differential polarization & $\Delta P$ & Asymmetric intervalley scattering \\
    \bottomrule
  \end{tabular}
\end{table}
```

## SIunitx Usage

```latex
\SI{25}{\micro\watt}          % 25 μW
\SI{300}{\kelvin}             % 300 K
\SI{532}{\nano\meter}         % 532 nm
\SI{50}{\milli\tesla}         % 50 mT
\SI{10}{\nano\meter}          % 10 nm
\SI{87.5}{\percent}           % 87.5%
\SIrange{25}{600}{\micro\watt} % 25–600 μW
```

## Supplementary Information (ACS)

```latex
% At the end of main.tex, before references:
\begin{suppinfo}
  Figure S1: [Description]. Figure S2: [Description].
  This material is available free of charge via the Internet at http://pubs.acs.org.
\end{suppinfo}
```

## Common Abbreviations (define on first use)

```latex
two-dimensional (2D)
van der Waals (vdW)
transition metal dichalcogenide (TMD)
degree of circular polarization (DOCP)
photoluminescence (PL)
magnetic proximity effect (MPE)
perpendicular magnetic anisotropy (PMA)
spin-orbit coupling (SOC)
density functional theory (DFT)
chemical vapour deposition (CVD)
magneto-optical Kerr effect (MOKE)
```
