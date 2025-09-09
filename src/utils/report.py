# src/utils/report.py

from config import MODULE_MAP


def format_section(
    title: str,
    data: dict
    ) -> str:
    lines = [f"\n## {title.upper()}"]
    for key, value in data.items():
        item = key.replace("_", " ").title()
        lines.append(f"- {item}: {value}")
    return "\n".join(lines)


def generate_txt_report(
    analysis: dict,
    filename: str
    ):
    sections = [f"# DATA REPORT FOR {filename}"]
    for module in MODULE_MAP.keys():
        if module in analysis:
            sections.append(format_section(module, analysis[module]))
    report_content = "\n".join(sections)
    with open(filename, "w") as f:
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
    "txt": generate_txt_report
}