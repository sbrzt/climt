# src/utils/load.py

import PyPDF2
from pathlib import Path
from docx import Document
from config import SUPPORTED_EXTENSIONS


def load_file(path) -> str:
    path = Path(path) 
    suffix = path.suffix.lower()
    if suffix == ".txt":
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        text = "\n".join([p.strip() for p in text.splitlines() if p.strip()])
        return text
    elif suffix == ".docx":
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    elif suffix == ".pdf":
        text = []
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
        return "\n".join(text)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")


def collect_files(paths: list):
    collected = []
    for p in paths:
        path = Path(p)
        if path.is_dir():
            for f in path.iterdir():
                if f.suffix.lower() in SUPPORTED_EXTENSIONS:
                    collected.append(f)
        elif path.is_file():
            if path.suffix.lower() in SUPPORTED_EXTENSIONS:
                collected.append(path)
            else:
                raise ValueError(f"Unsupported file type: {path.suffix}")
        else:
            raise FileNotFoundError(f"Path not found: {p}")
    return collected


def load_files(
    paths: list,
    mode: str = "merge"
    ):

    files = collect_files(paths)
    if mode == "merge":
        texts = [load_file(f) for f in files]
        return texts
    elif mode == "separate":
        return {f.name: load_file(f) for f in files}
    else:
        raise ValueError("Mode must be 'merge' or 'separate'")
