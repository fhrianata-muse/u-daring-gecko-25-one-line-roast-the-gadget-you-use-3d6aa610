#!/usr/bin/env python3
"""Write one roast of a daily gadget to /output/entry.txt."""

import os

ROAST = "My charging cable only works if I hold it at exactly 37 degrees, so every night I go to bed performing microsurgery on a wire I already paid good money for."

# Gate (competition.yaml): /output/entry.txt must be UTF-8 text of
# 1 to 200 characters, not only white space. Fail loudly instead of
# ever writing an entry the gate would refuse.
assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} characters, gate is 1-200"
assert ROAST.strip(), "roast must not be only white space"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
