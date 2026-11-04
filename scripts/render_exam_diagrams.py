#!/usr/bin/env python3
"""Render relevant diagram-bearing exam pages for source verification."""
from pathlib import Path
import fitz
ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "exam_prep" / "source_extractions" / "diagram_pages"
out.mkdir(parents=True, exist_ok=True)
for year, pages in [(2023, (2,3)), (2024,(3,4)), (2025,(4,))]:
    pdf = ROOT/"source_material"/"past_exams"/str(year)/f"Semester_Two_Examinations_{year}_PHYS7045.pdf"
    with fitz.open(pdf) as doc:
        for pg in pages:
            pix = doc[pg-1].get_pixmap(matrix=fitz.Matrix(1.6,1.6), alpha=False)
            name = out / f"{year}_page_{pg:02d}.png"
            pix.save(name)
            print(f"Rendered {name.relative_to(ROOT)}")
