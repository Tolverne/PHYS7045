# PHYS7045 — Quantum Technologies Exam Study Repository

A structured home for original PHYS7045 course material and the revision resources developed from it.

## Start here: where to upload files

| What you have | Upload to |
| --- | --- |
| Lecture transcript text files (`.txt`) | `source_material/lectures/transcripts/` |
| Lecture notes/PDFs with unclear names | `source_material/lectures/notes_to_identify/` |
| Identified lecture slides and handouts | `source_material/lectures/slides_and_handouts/` |
| Assignment question sheets | `source_material/assignments/questions/` |
| Your completed assignment solutions | `source_material/assignments/my_solutions/` |
| Marker feedback or supplied solutions | `source_material/assignments/feedback_and_solutions/` |
| Past exam papers (2023–2025) | `source_material/past_exams/<year>/` |
| Course profile, assessment guidance, formula booklets | `source_material/course_information/` |

**Upload originals as they are.** In particular, do not spend time renaming unidentified lecture PDFs: drop them in `notes_to_identify/` and we can map them to lectures once their contents are reviewed.

## Revision workspace

- **`notes/`** — carefully rewritten, topic-based study notes (LaTeX/Markdown), distinct from the original lecture materials.
- **`exam_prep/`** — formula sheets, short summaries, practice problems, an error log and worked solutions to past exams.
- **`assets/`** — figures and diagrams generated for new notes.
- **`scripts/`** — optional utilities for indexing transcripts, building notes or processing source files.

The topic folders under `notes/` are **provisional working categories**, not a claim about the precise exam syllabus. They can be reorganised after we review the lectures and past papers.

## Suggested workflow for the week before the exam

1. Upload original transcripts, PDFs, assignments and exams to `source_material/`.
2. Build a lecture-to-topic index in `source_material/lectures/lecture_index.csv`; identify previously unlabelled PDFs.
3. Extract key concepts and derivations into `notes/`, noting where the source material came from.
4. Work through past exams in `exam_prep/worked_past_exams/` without changing the source papers.
5. Consolidate recurring equations, common question types and mistakes in `exam_prep/`.

## Filename conventions

Use predictable filenames for **newly created** notes, e.g. `04_lindblad_master_equation.tex` or `2025_q2_worked_solution.tex`. Preserve original filenames until materials have been indexed. Place figure files beside their source or in `assets/` and link to them with relative paths.

## Public repository warning

**This repository is currently public.** Lecture slides, transcripts, exam papers and assignment solutions may be copyrighted or otherwise not intended for public redistribution. Check permissions before uploading them here; consider changing the repository visibility to **private** in GitHub Settings before uploading course materials.

## Repository structure

```text
PHYS7045/
├── source_material/
│   ├── course_information/
│   ├── lectures/
│   │   ├── transcripts/
│   │   ├── notes_to_identify/
│   │   ├── slides_and_handouts/
│   │   └── lecture_index.csv
│   ├── assignments/
│   │   ├── questions/
│   │   ├── my_solutions/
│   │   └── feedback_and_solutions/
│   └── past_exams/
│       ├── 2023/
│       ├── 2024/
│       └── 2025/
├── notes/
│   ├── 01_states_measurement_and_density_matrices/
│   ├── 02_gates_hamiltonians_and_qubit_control/
│   ├── 03_entanglement_and_teleportation/
│   ├── 04_open_systems_and_quantum_noise/
│   ├── 05_quantum_error_correction/
│   ├── 06_hardware_and_physical_gates/
│   └── 07_photonic_interference/
├── exam_prep/
│   ├── formula_sheets/
│   ├── topic_summaries/
│   ├── practice_questions/
│   ├── worked_past_exams/
│   │   ├── 2023/
│   │   ├── 2024/
│   │   └── 2025/
│   └── mistakes_and_gaps/
├── assets/
│   ├── figures/
│   └── diagrams/
└── scripts/
```

Empty directories are kept visible in Git using `.gitkeep` files; you can leave or remove these when you add content.

## 2026 open-book exam reference project

- [Exam reference editorial plan and 2023–2025 past-exam audit](exam_prep/EXAM_REFERENCE_PLAN.md)
- [Lecture-to-topic index](source_material/lectures/lecture_index.csv)
- [Searchable exam and assignment text](exam_prep/source_extractions/) — verify maths/diagrams against the source PDFs

These study materials are organised to support a ~10-page course overview and ~10-page worked-example booklet.
