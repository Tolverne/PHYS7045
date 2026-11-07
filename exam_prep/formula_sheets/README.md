# PHYS7045 — Five-page Formula & Method Sheet

A concise, print-ready open-book exam reference. Unlike a conventional formula sheet, every section gives a reusable method for tackling questions, with 2023–2025 past-exam cross-references and 2026 assignment links.

## Files

- `main.tex` — shared preamble; assembles the five pages in order.
- `01_states_and_hamiltonians.tex` — gates, qubit rotations, the 2023 YY Hamiltonian and CNOT conversions.
- `02_stabiliser_codes.tex` — a repeatable six-step procedure for all three past-exam QEC questions.
- `03_ion_and_rydberg_gates.tex` — sidebands, MS interference, trapped-ion pulse tracing and Rydberg CNOT/Toffoli.
- `04_photonics_and_information.tex` — optical mode transforms, HOM, heralded teleportation, RSP and CV.
- `05_noise_and_circuits.tex` — quantum channels, Lindblad, Cooper-pair box and question-to-method index.
- `PHYS7045_Formula_and_Methods_5pp.pdf` — print-ready output, 5 A4 pages.

## Build

From this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cp main.pdf PHYS7045_Formula_and_Methods_5pp.pdf
```

The repository's `build-formula-sheet.yml` workflow will regenerate the PDF when its LaTeX sources change. The sheet is deliberately short: consult the longer worked-solutions book when a full derivation or a source-paper diagram is required.