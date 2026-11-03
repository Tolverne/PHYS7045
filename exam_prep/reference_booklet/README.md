# PHYS7045 open-book exam companion

## Part I — The Big Picture

**Print-ready PDF:** [PHYS7045_Part1_Course_Overview.pdf](PHYS7045_Part1_Course_Overview.pdf)

This is a self-contained, approximately ten-page course overview written as a connected explanation rather than as a lecture-by-lecture slide summary. It covers:

1. Qubits, measurements, Pauli gates and Hamiltonian control
2. Entanglement, Schmidt decomposition and information protocols
3. Density matrices, thermal states and quantum channels
4. Lindblad master equations and coherence
5. Quantum error correction, stabilisers and the Steane code
6. Physical qubits: semiconductor spins/charge, superconducting circuits, photons, Rydberg atoms and trapped ions
7. Problem-recognition and exam-navigation guide

**Source:** `main.tex` inputs `part1_overview.tex`. The sources are editable and can be uploaded to Overleaf together. The GitHub Actions workflow builds and commits the PDF after changes to these files.

To compile locally:

```bash
cd exam_prep/reference_booklet
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The original source materials in `source_material/` remain unchanged. Mathematical expressions transcribed from source PDFs should always be checked against the originals, particularly signs, phases and diagram labels.

## Part II — Worked Examples

The worked-example companion has been scoped separately under [`EXAM_REFERENCE_PLAN.md`](../EXAM_REFERENCE_PLAN.md) and will be developed next. Part I deliberately uses the same modelling conventions and topic index to make that second part easy to navigate.