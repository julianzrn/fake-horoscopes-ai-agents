"""Entry for make.fun competition: u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "Your lucky number is 200,000 tokens. A tall stranger will paste an entire codebase into you on Thursday "
LANDING = "and say only: 'fix'."

ENTRY = OPENING + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
