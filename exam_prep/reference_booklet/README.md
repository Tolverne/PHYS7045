# PHYS7045 — Open-book exam companion

Two printable A4 booklets with editable LaTeX source, designed for the PHYS7045 Quantum Technologies exam. Source material remains unchanged in `source_material/`.

| Booklet | Purpose | PDF | LaTeX entry point | Content source |
| --- | --- | --- | --- | --- |
| **Part I — The Big Picture** | Course-wide conceptual overview, illustrated with Bloch spheres, quantum channels, stabilisers, and hardware diagrams | [PHYS7045_Part1_Course_Overview.pdf](PHYS7045_Part1_Course_Overview.pdf) | `main.tex` | `part1_overview.tex` |
| **Part II — Worked Problems and Exam Methods** | Fully explained examples modelled on 2023–2025 exams and 2026 assignments, with state-by-state tracking and exam checks | [PHYS7045_Part2_Worked_Examples.pdf](PHYS7045_Part2_Worked_Examples.pdf) | `part2_main.tex` | `part2_worked_examples.tex` |

Part I is **12 pages** with nine inline, editable vector diagrams created in TikZ, including the Bloch sphere, density matrices and Bloch vectors, channel dynamics, a stabiliser example, quantum dots, superconducting circuits, beam splitters, Rydberg levels, and ion sidebands. It retains the original course-overview narrative, with references added to the figures.

Part II is **10 pages** with detailed worked methods: Pauli-product evolution, Bell pairs and remote preparation, driven-dephasing Lindblad dynamics, stabiliser code syndromes/logicals/distance, Rydberg blockade, a three-pulse trapped-ion gate, photonic Hadamard/HOM, superconducting circuit quantisation, pulse timings, and the Mølmer–Sørensen mechanism. It closes with a short method index.

## Building locally

Using a TeX Live installation with `latexmk`, TikZ/PGF, Libertinus, and the packages listed in the preambles:

```bash
cd exam_prep/reference_booklet
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error part2_main.tex
```

You can upload the four `.tex` files in this folder to Overleaf to build either booklet. `main.tex` is the Part I entry point; `part2_main.tex` is the Part II entry point. All figures are self-contained TikZ drawings, so there are no external image dependencies.

The GitHub Actions workflow in `.github/workflows/build-reference-booklet.yml` builds both PDFs and commits the latest compiled versions to this directory whenever the `.tex` sources change.

## Source and verification notes

See [the assessment-source audit](../EXAM_REFERENCE_PLAN.md) and [the searchable extracted questions](../source_extractions/) for the original question mapping. **Always verify phases, operator labels, and diagram conventions against the source exam PDFs**. The worked examples are explanatory adaptations rather than facsimiles of official solutions. The 2026 assignment solutions are a guide to the level of mathematical detail; any example may require adaptation if the exam uses different state conventions.

The repository was public at setup. Check permissions or make it private before redistributing lecturer material and exam papers.