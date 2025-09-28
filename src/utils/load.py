# src/utils/load.py

import PyPDF2
from pathlib import Path
from docx import Document


def load_files(path: str) -> str:
    suffix = Path(path).suffix.lower()
    if suffix == ".txt":
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    elif suffix == ".docx":
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs)
    elif suffix == ".pdf":
        text = []
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text.append(page.extract_text())
        return "\n".join(text)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")