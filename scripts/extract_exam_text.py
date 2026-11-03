#!/usr/bin/env python3
"""Extract searchable text from PHYS7045 past exams and assignment prompts.

Run locally:
    python -m pip install pymupdf
    python scripts/extract_exam_text.py

The PDFs remain the authoritative versions for equations, figures and layouts.
"""
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIRS = [
    ROOT / "source_material" / "past_exams",
    ROOT / "source_material" / "assignments" / "questions",
]
DEST = ROOT / "exam_prep" / "source_extractions"

def main():
    DEST.mkdir(parents=True, exist_ok=True)
    for source in SOURCE_DIRS:
        for file in sorted(source.rglob("*.pdf")):
            name = ("exam_" + file.parent.name + "_" + file.stem if source.name == "past_exams"
                    else "assignment_" + file.stem)
            out = DEST / (name + ".txt")
            with fitz.open(file) as pdf:
                content = [
                    f"# Source: {file.relative_to(ROOT)}",
                    f"# Pages: {len(pdf)}",
                    "# Machine-extracted text: verify mathematical notation against original PDF.",
                    "",
                ]
                for i, page in enumerate(pdf):
                    content += [f"\n{'=' * 20} PAGE {i+1} {'=' * 20}\n", page.get_text("text")]
                out.write_text("\n".join(content), encoding="utf-8")
            print(f"Extracted {file.relative_to(ROOT)} -> {out.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
