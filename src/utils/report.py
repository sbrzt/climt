# src/utils/report.py

import os
from config import MODULE_MAP, REPORT_DIR
from tabulate import tabulate


def format_freq_table(data: dict) -> str:
    rows = []
    headers = ["item", "count", "freq (%)"]
    for key, stats in data.items():
        rows.append([key, stats["count"], stats["freq"]])
    return tabulate(rows, headers=headers, tablefmt="github")


def format_section(
    title: str,
    data: dict
    ) -> str:

    lines = [f"\n## {title.upper()}"]
    if title.lower() in {"words", "pos"}:
        lines.append(format_freq_table(data))
    else:
        for key, value in data.items():
            item = key.replace("_", " ")
            lines.append(f"- {item}: {value}")
    return "\n".join(lines)


def generate_txt_report(
    analysis: dict,
    filename: str
    ):

    os.makedirs(REPORT_DIR, exist_ok=True)
    sections = [f"# DATA REPORT FOR {filename}"]
    for module in MODULE_MAP.keys():
        if module in analysis:
            sections.append(format_section(module, analysis[module]))
    report_content = "\n".join(sections)
    filepath = os.path.join(REPORT_DIR, filename)
    with open(filepath, "w") as f:
        f.write(report_content)


def save_report(
    analysis: dict,
    filename: str,
    fmt: str
    ):

    if fmt not in REPORT_GENERATORS:
        raise ValueError(f"Unsupported format.")
    REPORT_GENERATORS[fmt](analysis, f"{filename}.{fmt}")


REPORT_GENERATORS = {
    "txt": generate_txt_report,
    "md": generate_txt_report
}