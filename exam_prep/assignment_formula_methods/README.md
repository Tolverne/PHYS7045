# PHYS7045 — 2026 Assignment Formula and Methods Sheet

This five-page companion to the [past-exam method sheet](../formula_sheets/) is a *problem-solving map* for all three 2026 PHYS7045 assignments. It is written for the open-book examination, with explicit links from each assignment question to the relevant method.

**PDF:** [PHYS7045_Assignments_Formula_and_Methods_5pp.pdf](PHYS7045_Assignments_Formula_and_Methods_5pp.pdf)

| Page | Coverage |
|---|---|
| 1 | Assignment 1 Q1.1–1.2: Bloch/Pauli proofs, rotation gates, pulse timing, conditional $CZ$, no cloning |
| 2 | Assignment 1 Q1.3–1.4: Schmidt decomposition, partial trace, unambiguous discrimination, teleportation fidelity, Werner states |
| 3 | Assignment 2 Q1–2: driven Lindblad equations, thermal Kraus maps, Steane code, lookup decoding, failure probability, transversal CNOT |
| 4 | Assignment 3 Q1–2: controlled-Rydberg $U_x$, phase corrections, trapped-ion three- and five-pulse gates |
| 5 | Assignment 3 Q3–4: Cooper-pair box/transmon Hamiltonians and numerical spectra; photonic Bell/HOM/MZI calculations; question index |

## Compile locally

```bash
cd exam_prep/assignment_formula_methods
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`main.tex` imports the five page-specific `.tex` files. The GitHub Actions workflow compiles the PDF automatically on pushes.

## Notes on conventions

- $R_{\mathbf n}(\alpha)=\exp[-i\alpha\,\mathbf n\cdot\boldsymbol\sigma/2]$ is an **active** Bloch rotation. The inverse sign rotates in the opposite direction.
- The Rydberg assignment uses **control-on-zero** and the computational basis $|00\rangle,|01\rangle,|10\rangle,|11\rangle$.
- The thermal master equation uses basis $|g\rangle,|e\rangle$ and defines $Z=|g\rangle\langle g|-|e\rangle\langle e|$.
- The beam-splitter transformation is stated in the document; phase signs may differ under other port conventions without changing probabilities.
- This is a concise study guide, **not a verbatim replacement** for your submitted assignment solutions. The detailed original work remains under `source_material/assignments/my_solutions/`.