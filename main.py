#!/usr/bin/env python3
"""The One-Line Laugh — writes the entry to /output/entry.txt.

Stdlib only, no network, deterministic. The entry is a single
sentence of at most 200 characters.

Revision (recorded): the draft read "Adulthood is just googling ..."
— "just" was cut on revision because it earned nothing: the joke is
the gap between adult self-image and googling a boiled egg, and the
turn is the smoke alarm cheering. Shorter reads faster aloud and
lands the alarm sooner.
"""

import os
import sys

ENTRY = "Adulthood is googling how long to boil an egg while the smoke alarm cheers you on."


def self_check(entry: str) -> None:
    """Fail hard unless the entry meets the competition gate."""
    if not isinstance(entry, str):
        sys.exit("self-check failed: entry is not text")
    entry.encode("utf-8")  # raises on non-UTF-8-encodable text
    if not entry.strip():
        sys.exit("self-check failed: entry is only whitespace")
    chars = len(entry)
    if not 1 <= chars <= 200:
        sys.exit(f"self-check failed: {chars} characters, gate is 1-200")
    if "\n" in entry or "\r" in entry:
        sys.exit("self-check failed: entry must be a single line")
    # Judge brief: the line has to stand alone as a single sentence.
    if entry.count(".") + entry.count("!") + entry.count("?") != 1:
        sys.exit("self-check failed: entry must be exactly one sentence")
    if not entry.endswith((".", "!", "?")):
        sys.exit("self-check failed: entry must end with sentence punctuation")


def main() -> None:
    self_check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
