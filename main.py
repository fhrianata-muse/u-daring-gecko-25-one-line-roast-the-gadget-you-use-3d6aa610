"""Microsurgery at 37 Degrees — one-line roast entry.

Writes the roast to /output/entry.txt.
"""

from pathlib import Path

ROAST = "My charging cable only works if I hold it at exactly 37 degrees, so every night I go to bed performing microsurgery on a wire I already paid good money for."

assert 1 <= len(ROAST) <= 200
assert ROAST.strip()
# The entry must be a single line: no newline inside the roast itself.
assert "\n" not in ROAST


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ROAST + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
