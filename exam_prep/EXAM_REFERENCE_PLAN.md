# PHYS7045 — Exam Reference Booklet: Plan and Source Audit

## Goal

Produce a **printable 20–24 page LaTeX reference**, readable before the exam and usable quickly during the open-book examination:

- **Part I (~10 pages):** a cohesive course overview explaining the big ideas, assumptions, physical interpretations and essential equations.
- **Part II (~10 pages):** fully worked exam-style problems with intermediate steps, state tracking, explanations, references to source questions and common pitfalls.
- Optional 1–2 pages for contents, keyword navigation and a compact formula/index sheet. Prioritise readability over an exact page count.

## Source inventory reviewed

- 22 lecture transcripts (filenames numbered 0 through 21; broad topics mapped below);
- Three PHYS7045 past exams, 2023–2025 (all questions indexed);
- Three 2026 assignment question sheets, plus the existing solutions PDF (to use during drafting).
- The original lecture PDFs are in `source_material/lectures/notes_to_identify/` and still require diagram-by-diagram matching to transcripts.

Searchable versions of the exam and assignment PDF text have been generated in `exam_prep/source_extractions/`. These are a convenience only: **verify notation, diagrams and signs against the PDFs**.

## Past exams: question-level audit

| Year | Q1 | Q2 | Q3 |
|---|---|---|---|
| 2023 | Trapped-ion Mølmer–Sørensen gate, red/blue sidebands | Six-qubit stabiliser code: syndrome, logical operators, distance | `Y⊗Y` Hamiltonian: derive unitary, entangle qubits, implement CNOT |
| 2024 | Five-qubit stabiliser code: syndrome, logical operators, distance | Dual-rail optical Hadamard; probabilistic teleportation | Rydberg blockade: simultaneous-pulse CNOT, Toffoli extension |
| 2025 | Nine-qubit stabiliser code: syndrome, logical operators, distance | Three-pulse trapped-ion gate: track states, determine matrix, CC extension | Remote state preparation, photonic implementation, compare with teleportation |

**Historical pattern:** stabiliser-based QEC is in **every exam**. Multi-qubit gate implementations are in **every exam**. Quantum information / photonics appears in two recent papers and entanglement is important throughout.

**Important cross-reference:** 2025 exam Q2 closely matches 2026 Assignment 3 Q2 (the red-sideband `π,2π,π` trapped-ion sequence). Reuse the verified assignment solution as a model worked example, ensuring all intermediate states and phase conventions are explicit.

2026 Assignment 2 also gives a full driven-dephasing Lindblad problem and a Steane-code problem; the past exams alone should not determine what is omitted. No guarantee is implied that historical patterns will repeat.

All three historical exams: 120 minutes, 10 minutes planning, three main questions with Part A (grade 1–5) and advanced Part B (potential additional grades). Check current year rules separately.

## Part I — Conceptual overview (indicative ~10 pages)

| Approx. space | Topic | Central concept |
|---|---|---|
| 1 page | States, measurements, Pauli matrices, Bloch sphere, rotations | How states and gates are represented |
| 1 page | Bell states, Schmidt, teleportation, remote preparation | How entanglement is used |
| 1 page | Density operators, partial trace, Kraus channels | How to describe mixed states and noise |
| 1 page | Lindblad master equation and Bloch dynamics | Dissipative and coherent evolution |
| 1.5 pages | QEC, stabilisers, syndrome measurements, logical operators, distance | Diagnosing errors without learning the logical state |
| 1 page | Spin/solid-state qubits, Hamiltonian control | Physical single- and two-qubit operations |
| 1 page | Superconducting circuits, Josephson junction, CPB/transmon | Quantising electrical circuits |
| 1 page | Polarisation and dual-rail photons, beam splitters, HOM | Interference and linear optics |
| 1 page | Neutral atoms and trapped ions, Rydberg blockade, sidebands | Physical entangling interactions |
| 0.5 page | Comparing platforms and approximations | Synthesis and recall |

## Part II — Worked examples (indicative ~10 pages)

| Approx. space | Worked-problem template | Sources |
|---|---|---|
| 1 page | Exponentiate a Pauli-product Hamiltonian, find entangling time, map to a gate | 2023 Q3; 2026 A1 |
| 1 page | Bell states, density matrices, teleportation/remote state preparation | 2025 Q3; 2026 A1 |
| 1 page | Lindblad equation → Bloch ODEs → steady state and purity | 2026 A2 Q1 |
| 2 pages | **General stabiliser code algorithm:** commutation, syndrome table, detect/correct, logical `X_L,Z_L`, distance | 2023–25 QEC questions; 2026 A2 Q2 |
| 1 page | Rydberg blockade CNOT, pulse areas and basis-state truth table | 2024 Q3; 2026 A3 Q1 |
| 1 page | Ion-trap red-sideband `π,2π,π` sequence: after each pulse for each computational basis input | 2025 Q2; 2026 A3 Q2 |
| 1 page | Photonic beamsplitter transformation, dual-rail Hadamard, HOM output probabilities | 2024 Q2; 2026 A3 Q4 |
| 1 page | Cooper-pair box Lagrangian → charge → Hamiltonian → harmonic approximation | 2026 A3 Q3 |
| 1 page | Mølmer–Sørensen, advanced gate constructions and conceptual checks | 2023 Q1; 2024 Q3 |

**Each solved example should follow:** recognise type → choose notation/convention → write governing equation → show state evolution/algebra → final answer → interpret physically → common mistake or check.

## Navigational design

- Clear contents page and **keyword-to-page index** (stabiliser, syndrome, Rydberg, sideband, Kraus, master equation, beam splitter, Bell state, Josephson).
- Explicit labels and ordering of computational bases.
- For pulse sequences, tabulate **input / after pulse 1 / after pulse 2 / after pulse 3 / measurement or final state**.
- Separate global from conditional/relative phases.
- Keep a consistent notation for `X_L` and `Z_L`, qubit ordering and sign conventions.
- Make Part A core methods easy to find before Part B advanced extensions.
- Check trace, positivity, unitarity, unique syndromes and dimensional consistency as relevant.

## Transcript topic map (initial pass)

| Download number | Main subjects |
|---|---|
| 0–2 | Information theory, density matrices, entanglement, Schmidt, teleportation |
| 3–8 | Mixed/thermal states, quantum channels, Lindblad and noise |
| 9–12 | Error correction, syndrome measurements, stabiliser codes |
| 13–15 | Charge/spin qubits, superconducting circuits |
| 16–17 | Photonic qubits and linear optical operations |
| 18–21 | Neutral atoms, Rydberg systems, trapped ions |

These numbers refer to **downloaded transcript filenames**, not a verified university lecture calendar. Topic mapping is preliminary and may be refined against PDFs.

## Proposed authoring structure

Write a single master LaTeX file importing separate `part1_overview.tex`, `part2_worked_examples.tex`, and `quick_reference.tex` chapters. Cross-reference equation and example numbers. Compile to PDF and inspect pages to verify equations, tables and diagrams are legible. Retain original documents in `source_material/`.
