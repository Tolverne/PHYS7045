# PHYS7045 — Fully Worked Past Examinations (2023–2025)

This directory contains an **independent, exam-oriented worked solution for every question and every Part A/Part B subpart** from the 2023, 2024 and 2025 PHYS7045 examination papers.

**Read:** [PHYS7045_Past_Exams_2023-2025_Fully_Worked.pdf](PHYS7045_Past_Exams_2023-2025_Fully_Worked.pdf)

## Source structure

- `main.tex` — standalone LaTeX master file; includes the common style, title, contents and all years.
- `solutions_2023.tex` — Mølmer–Sørensen trapped-ion gate; full six-qubit stabiliser-code syndromes, logical operators and distance; `Y \otimes Y` entangler to CNOT.
- `solutions_2024.tex` — five-qubit code (including detecting versus correcting); dual-rail Hadamard and 50%-success optical teleportation; simultaneous-pulse Rydberg CNOT and Toffoli extension.
- `solutions_2025.tex` — nine-qubit stabiliser code; ion sideband `π, 2π, π` gate including the five-pulse controlled-controlled extension; singlet remote state preparation and continuous-variable teleportation.

Original examination papers (including their diagrams) remain in `../../source_material/past_exams/2023`, `2024`, and `2025` (relative to this folder, from `exam_prep/past_exam_solutions/` the correct path is `../../source_material/past_exams/`).

## Compile

Run in this folder:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Alternatively, use PDFLaTeX twice. Requires packages `libertinus`, `amsmath`, `tcolorbox`, `tikz`, `booktabs`, `hyperref` and related standard TeX Live packages. GitHub Actions builds the PDF automatically when `.tex` files change.

## Mathematical and exam notes

These are study solutions, **not the official grading rubric**. All calculations are stated with the physical assumptions and phase conventions being used.

- **2023 Q1:** the upper and lower virtual paths each have two ion-orderings, which produce the cancellation of phonon-number dependence.
- **2023 Q3:** the exact Hamiltonian exponential contains a global phase that the exam's displayed unitary omits; the two are physically equivalent.
- **2024 Q1:** the five-qubit code has distance 2. Nonzero single-error syndromes imply detectability, but collisions of **inequivalent** errors prevent correcting every single Pauli error.
- **2024 Q2:** a 50:50 beam splitter implements an exact Hadamard when supplemented by a rail-phase shift under the paper's sign convention. The teleportation diagram uses a single-rail Fock-state input; conditional one-photon detection succeeds with probability 1/2.
- **2024 Q3:** the source diagram leaves detunings, pulse shapes and coupling ratios unspecified. The answer distinguishes the ideal effective-pulse truth table from the conditions required for a physical simultaneous resonant three-level implementation.
- **2025 Q2:** keep phonon number and all phase factors at every step; the three-pulse operation is CZ, and the five-pulse extension gives CCZ, which becomes Toffoli by a target Hadamard.
- **2025 Q3:** the original resource is the singlet `|ψ⁻⟩`, rather than `|Φ⁺⟩`. The deterministic one-bit correction applies to the equatorial ensemble; arbitrary target states need additional resources, state-dependent feed-forward or heralding.

If you discover a different sign convention in your lecture notes, work through the computational-basis mappings before changing an answer; output probabilities and relative conditional phases should remain physically consistent.