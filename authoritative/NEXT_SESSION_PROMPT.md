# S060 — FUTURE / UNEXECUTED — WRITE THE COMPLETE RESEARCH PAPER WITH MULTIPLE MATHEMATICAL FIGURES

**TARGET STATUS: INSTALLED BY OWNER. FUTURE / UNEXECUTED.**

Repository: https://github.com/jfairfaxball-348/ellipse-theorem  
Lean namespace: `ETSHTS`  
Owner direction (18 October 2026): Palomar registration is stalling; advance directly to writing the research paper now, with a placeholder for the eventual Palomar entry link. The paper MUST have multiple high-quality, mathematically faithful visuals.

## Execution authority and boundary

This file installs **S060 only**. A **new explicit owner invocation** by the owner (including “Run next session”) authorises execution of S060; do **not** execute S060 as part of installation. Do not execute S061. The next session is **paper production**, not a mathematics-discovery, Lean proof-rewriting, Palomar registration, or arXiv-upload session. Preserve the frozen five theorem statements, all Lean proof files, original definitions, `formalization.yaml`, Comparator, and the existing Palomar candidate source SHA unless separately required for non-mathematical documentation. Palomar registration is **not** a precondition to draft completion.

## Binding objective: a real paper, not an outline

Create a **complete, scholarly, readable, submission-quality first manuscript** with working LaTeX sources and reproducible mathematical figures in a clearly organised `paper/` (or another documented existing paper directory). Prefer a concise theorem-driven paper over a long dump of formal source. Use clean mathematical exposition, self-contained definitions and proofs, logically ordered lemmas, carefully checked formulae, accurate references and a substantial introduction that explains the problem's simplicity and its surprising noncircular all-cardinality answer. Do not stop at a skeleton, an abstract, a plan, or a list of future writing tasks. Work across multiple passes within this session: draft, validate mathematics against canonical sources, create figures, edit, typeset, proofread and package the full paper as far as tooling permits. If any part is blocked, mark the exact blocker and leave the largest truthful complete artifact possible.

### Title, authorship, theorem prominence

Use the title already agreed for the README and Palomar metadata **exactly**:

**Noncrossing Two-Nearest-Predecessor Orders on Nearly Circular Ellipses**

Use the authorised `formalization.yaml` authorship information (John Fairfax-Ball), without adding invented affiliations, endorsements or acknowledgements. Open the abstract with **“We prove that...”**, with the precise sufficient scope rather than a claim of optimality.

Near the beginning, display and prove the main result accurately:

\[
R=\sqrt{\frac{2}{\sin(2\pi/5)}-1}\approx 1.0502020988726573.
\]

For **all** `0<b≤a` with `a/b≤R` (including equality), and **every** finite set `S` of at least three distinct sites on `E(a,b)=\{(a\cos t,b\sin t):t\in\mathbb R\}`, there is an ordering starting with the complete triangle, after which every new site attaches to **exactly** its two Euclidean-nearest **earlier** sites, resolving equal-distance predecessors by Cartesian lexicographic order; all old edges persist and no two final straight edges properly cross. No cardinality bound, no minimum spacing, no replacement of predecessor-nearest with global-nearest. State explicitly that this is a **sufficient** closed ratio bound and not known here to be sharp. Include the all-cardinality **noncircular** `a/b=101/100` corollary, the complete 3/4-point theorem, the recursive metric-ear iff for strictly convex-position finite sets, and the signed chord derivative/strict short-arc extension result, with roles and scopes matching their original source declarations.

Use the paper-to-Palomar crosswalk in `sessions/S056/PAPER_REGISTRY_ALIGNMENT.md`, confirmed current `formalization.yaml`, and `sessions/S054/SEMANTIC_AUDIT.md`. Check all actual theorem scopes, not just colloquial summaries.

### Mandatory figure programme — multiple finished visuals

Include **at least four distinct, genuinely informative, publication-quality mathematical diagrams** (ideally five or more if useful), embedded and explicitly discussed/cross-referenced in the manuscript. Draw reproducibly from source (TikZ/PGFPlots, Asymptote, SVG/vector-to-PDF, or equivalent), include the individual source files and stable generated outputs; never substitute decorative images, blurry screenshots, ungrounded algorithm animations, or placeholder boxes.

Minimum coverage:

1. **Early and prominent headline figure**, on the first page or immediately adjacent to the introductory theorem: a nearly circular, genuinely nonround ellipse with an accurately plotted finite boundary sample, clearly distinguished arrival order and compulsory two-nearest-predecessor edges, and a **verified noncrossing** final retained drawing. Label how the construction differs from ordinary planar triangulation. If the plotted ordering is illustrative, validate every step computationally by exact/controlled high-precision Euclidean distance comparisons and the stated tie rule; do not assert it is a valid nearest-predecessor order merely because the drawing looks planar.
2. **Metric-ear recursion / reversible insertion figure**: a concrete cyclic hull illustrating a strict metric ear, its two cyclic neighbours and the removal/reinsertion step. Make the actual nearest-predecessor criterion visible; explain how this underlies the full recursive iff.
3. **Proof-geometry figure**: cyclic gaps, eligible two-step/skip chord, the \(\Lambda=4\arctan(b/a)\) short-arc cutoff and/or the forward/central/backward angular competitor bands. Every shown inequality must have the correct direction and exact equality/strictness convention.
4. **Small-cardinality figure** showing the nonconvex four-site (interior point) case versus a strictly convex quadrilateral and the correct seed/insertion choices; label that CLM0096 is not restricted to ellipse sites.
5. **Optional but strongly encouraged**: a small, clearly titled illustration of the S033 five-site **counterexample to the false minimum-adjacent-angular-two-gap ear-selection heuristic** at `a/b=101/100`. This counterexample **does not contradict the main ellipse theorem**. Draw the actual rational half-angle sites from `sessions/S033/MATHEMATICS.md`, and highlight the shorter non-neighbour distance. Place this figure in a proof-strategy/selection-subtlety discussion, **not** as an unexplained opening counterexample to the paper's principal claim. Include only if its geometric labels and source are accurate.

Require readable captions that state exactly what is pictured, precise labels, consistent line styles, accessible grayscale/print legibility, no visual crossing hidden by color, and minimal clutter. Prefer figures whose mathematics is independently checkable from stored coordinates/parameters and small scripts; include figure-generation/validation scripts where possible. A prominent counterexample is acceptable **only with its exact target specified**, so readers cannot confuse a refuted heuristic with the proved main theorem.

### Full paper structure (adapt where scholarly exposition improves it)

- Abstract and introduction: problem in plain language, background/related literature, contribution and limitations; formal main theorem and early headline diagram.
- Precise geometric, ordering, retained-edge and tie-breaking definitions; illustrative example.
- Three/four-site foundations and plane-graph/outerplanar counting; the **full iff** metric-ear certificate, not only its forward implication.
- Ellipse chord formula and **both** outward signed derivatives; strict short-arc extension with exact domain \(0<\Delta<\Lambda\).
- Cyclic-gap average \(\sum s_i=4\pi\), eligible set at **closed** endpoint \(r=R\), Euclidean skip-chord minimisation (not minimal angular two-gap), forward/central/backward competitor arguments including \(\Delta=\Lambda\) and \(2\pi-\Lambda\), strict nearer adjacent vertices, and iterative ear deletion/reinsertion through all cardinalities.
- The exact 101/100 corollary and discussion of scope, related work and limitations.
- Formal verification note with exact five Lean theorem names/modules; distinguish machine-checked proofs from independent mathematical or historical peer review.
- Accurate references/bibliography, acknowledgements, and nonfabricated Palomar placeholder.

Check the mathematical presentation line by line against **`sessions/S020/MATHEMATICS.md`**, **`sessions/S021/MATHEMATICS.md`**, **`sessions/S054/SEMANTIC_AUDIT.md`**, original `ETSHTS/Definitions.lean` and `ETSHTS/Targets.lean` and the exact proved declarations. Correct transcription errors in the *paper*, never quietly strengthen or weaken the locked theorem. The proof must be readable to a human referee, not only a pointer to Lean.

### Palomar link placeholder and scholarly candour

Include a single obvious, easily replaceable source macro or bibliography/footnote placeholder such as `\newcommand{\PalomarRecordURL}{[PALOMAR RECORD URL PENDING]}` (make the LaTeX syntax compilable and provide the actual displayed wording **“Palomar verification record: pending registration”**). Do not invent an ID, say registration exists, use a dead dummy URL, or treat successful private/local Comparator checking as an issued Palomar record. Leave written instructions for swapping in the real versioned URL after the owner registers it. The paper is allowed to be otherwise complete with this placeholder.

Cite real prior art with verified bibliographic data. S055's novelty verdict is **`INDETERMINATE_ACCESS_GAP`**, not historical priority certification. Avoid “first ever”, “new optimal bound”, “all ellipses”, “sharply determined”, “Palomar-verified/registered”, and unsupported claims of external peer review. Source investigation may be performed solely as needed for accurate scholarly citations; do not turn the session into a fresh unbounded novelty audit. Make it clear which familiar supporting geometric facts are not being claimed original.

### Production requirements and acceptance checks

Deliver:
- A complete standalone `paper/main.tex` (or clearly documented equivalent), reusable bibliography, all manuscript-required local assets, a short reproducible build/readme and a compiled PDF **if the session environment supports a TeX engine**.
- At least four **actual** embedded diagrams with vector-quality source and self-explanatory captions; figure paths resolve and figures are displayed (verify a rendered PDF/page images if tooling exists).
- A consistent paper title/theorem/abstract aligned to Palomar metadata and the five exact Lean declarations.
- A documented math check for every constructed nearest-two ordering figure, and an audit that no figure accidentally depicts a false statement.
- Source and bibliography provenance; no fabricated citations.
- A final manuscript review for notation, theorem references, page layout, figure legibility, malformed equations, unexplained symbols, English prose and submission readiness.
- Session evidence and closeout containing files changed, build result or exact environment limitation, figure inventory with paths, proof-to-source crosswalk, outstanding editorial issues and actual PR/CI/merge outcomes.

Use ordinary feature branch → PR → ordinary merge if possible; perform actual verification instead of claiming unobserved checks. Do **not** submit to a journal/arXiv, contact editors, create a Palomar registration or use a fake link. At session closure restore S061 as a neutral **FUTURE / UNEXECUTED — TARGET NOT INSTALLED** owner-steered placeholder, without recommending the next target. **Only S060 paper writing is authorised when separately invoked.**
