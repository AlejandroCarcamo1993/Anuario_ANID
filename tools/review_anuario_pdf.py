from __future__ import annotations

from pathlib import Path
import re

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / "Anuario 2024 - ANID 30.12 (5).pdf"
REPORT_DIR = ROOT / "reportes"
OUTPUT_MD = REPORT_DIR / "anuario_2024_pdf_extraccion.md"


def normalize_page_text(text: str) -> str:
    text = text.replace("\u00a0", " ")
    lines = [re.sub(r"[ \t]+", " ", line).rstrip() for line in text.splitlines()]

    cleaned: list[str] = []
    blank_streak = 0
    for line in lines:
        if line.strip():
            cleaned.append(line)
            blank_streak = 0
        else:
            blank_streak += 1
            if blank_streak == 1:
                cleaned.append("")

    while cleaned and not cleaned[0].strip():
        cleaned.pop(0)
    while cleaned and not cleaned[-1].strip():
        cleaned.pop()

    return "\n".join(cleaned)


def page_title(text: str, page_number: int) -> str:
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if len(line) > 120:
            continue
        return line
    return f"Página {page_number}"


def build_markdown(pdf_path: Path) -> str:
    doc = fitz.open(pdf_path)
    parts = [
        "# Extracción PDF: Anuario 2024 - ANID 30.12 (5)",
        "",
        f"- Archivo: `{pdf_path.name}`",
        f"- Páginas detectadas: `{doc.page_count}`",
        "- Método de extracción: texto digital con PyMuPDF (`fitz`)",
        "- Nota: el orden de lectura puede variar respecto de la diagramación visual del PDF.",
        "",
    ]

    for idx in range(doc.page_count):
        page_number = idx + 1
        text = normalize_page_text(doc.load_page(idx).get_text("text"))
        title = page_title(text, page_number)
        parts.extend(
            [
                f"## Página {page_number}: {title}",
                "",
                "```text",
                text if text else "[Sin texto extraíble]",
                "```",
                "",
            ]
        )

    return "\n".join(parts).rstrip() + "\n"


def main() -> None:
    REPORT_DIR.mkdir(exist_ok=True)
    OUTPUT_MD.write_text(build_markdown(PDF_PATH), encoding="utf-8")
    print(OUTPUT_MD)


if __name__ == "__main__":
    main()
