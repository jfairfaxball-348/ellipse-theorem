# Research manuscript (S060)

**Noncrossing Two-Nearest-Predecessor Orders on Nearly Circular Ellipses**, John Fairfax-Ball.

## Build and reproduce

From this `paper/` directory, run:

```sh
python3 -m pip install mpmath  # only if not already installed
python3 scripts/make_figures.py
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The PDF is `main.pdf`. The bibliography is embedded in `main.tex` for BibTeX-free portability; matching reusable BibTeX entries are in `references.bib`. Requires TeX Live / `pdflatex` with packages `tikz`, `microtype`, `natbib`, `hyperref`, `caption`, `float`, `lmodern`, `geometry`. Five vector TikZ figures are included directly from editable `.tikz` sources. The Python generator deterministically recreates those sources from the stated parameters and writes `scripts/figure-validation.json`.

**Figure inventory:** `figures/headline.tikz` (validated ten-point compulsory nearest-two order), `figures/metric-ear.tikz` (strict ear and reversal), `figures/competitor-bands.tikz` (closed central competitor band), `figures/four-sites.tikz` (interior and convex 4-site cases), `figures/false-heuristic.tikz` (exact rational counterexample *only* to false angular-gap minimiser rule). Every plotted order has a strictly distinct nearest-two selection. The construction checker uses 80-decimal-digit mpmath, tests non-neighbour strict ear separations, actual predecessor rankings, exact edge count, and pairwise proper crossings; the smallest observed squared-distance comparison margin for the headline example is stored in the JSON. The fifth figure's key squared-distance inequality is validated in **exact rational arithmetic**. TikZ figure source is vector; a rendered PDF is not required to regenerate the diagrams.

## Constructive algorithm and cost model

The manuscript now contains an explicit algorithmic corollary (Proposition \\ref{prop:algorithm} in `main.tex`): given boundary sites on an ellipse satisfying the paper's closed aspect-ratio bound, construct a plane two-nearest-predecessor order in **O(n log n)** time and **O(n)** auxiliary space in the exact real-arithmetic comparison model. The construction cyclically sorts the sites, maintains eligible minimum **squared Euclidean skip chords** in a heap, removes an eligible minimum metric ear while updating only its two neighbouring candidate records, and reverses the deletion stack after the three-/four-site base case.

The algorithm is not the false shortest-angular-two-gap heuristic analysed in the manuscript. Eligibility can be decided without trigonometric or inverse-trigonometric oracles: for normalised ellipse coordinates `q=(x/a,y/b)`, test the oriented determinant of a candidate's two surviving neighbours and compare their dot product to `2((a^2-b^2)/(a^2+b^2))^2-1`. Strict equality at the cutoff is ineligible. Heap ties may be resolved by Cartesian coordinates; the underlying metric-ear proof guarantees strict separation from all non-neighbours.

The asymptotic bound is a **paper-level derivation of the proved constructive ear lemma**. It is not a separately formalised Lean running-time statement, not a floating-point numerical guarantee, and not a claim about the bit cost of arbitrary real arithmetic. The original five frozen Lean theorems and Palomar candidate are unchanged. The manuscript's `101/100` consequence is retained in abbreviated form.

## Palomar placeholder

No Palomar record or registration is claimed. In `main.tex`, `\PalomarRecordStatus` currently displays **Palomar verification record: pending registration** and `\PalomarRecordURL` is a single non-link placeholder `[PALOMAR RECORD URL PENDING]`. Once the owner actually receives a verified versioned entry URL, replace the macro definition with the real URL and update the sentence in the verification section to issue `\url{\PalomarRecordURL}`. Do not replace the placeholder with a speculative ID.

## Proof-to-source alignment

| Manuscript | Canonical maths | Exact Lean theorem / module |
|---|---|---|
| Proposition 2.2 | S021 A | `clm0096_exact` / `ETSHTS/ConvexFourClassification.lean` |
| Theorem 2.4 | S021 A | `clm0099_exact` / `ETSHTS/GenuineOuterplanarCap.lean` |
| Lemma 3.1 | S021 B | `clm0102_exact` / `ETSHTS/Cutoff.lean` |
| Main theorem 1.1 and strict ear proof | S020, S021 C | `clm0107_exact` / `ETSHTS/CyclicCompetitorExact.lean` |
| Noncircular corollary | S021 D | `clm0108_exact` / `ETSHTS/ExactNonround.lean` |
| Heuristic counterexample | S033 | S033 rational source and `sessions/S033/MATHEMATICS.md` |

Frozen original propositions in `ETSHTS/Targets.lean` and original definitions in `ETSHTS/Definitions.lean`; semantic check `sessions/S054/SEMANTIC_AUDIT.md` and title crosswalk `sessions/S056/PAPER_REGISTRY_ALIGNMENT.md`. Historical prior-art status remains `INDETERMINATE_ACCESS_GAP` (`sessions/S055/`). None of the frozen mathematical files is modified by this manuscript.

## Source provenance

References draw on publisher DOI records for Ágoston et al. (2026), Bose et al. (2004), Levcopoulos–Lingas (1987) and the author-hosted 1992 Finlayson–Bhattacharya paper. Source dossier: `sessions/S055/SOURCE_DOSSIER.md`. Bibliographic references are not a claim to have completed a full priority search.
