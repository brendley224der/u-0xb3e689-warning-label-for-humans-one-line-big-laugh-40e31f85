#!/usr/bin/env python3
"""Warning label for humans: one line, big laugh.

Writes a single-line safety warning label that should come printed on
every human being to /output/entry.txt.

Pure standard library. Deterministic: the same line on every run.
"""

import os

ENTRY_PATH = "/output/entry.txt"

# The label. One idea, one read: the turn lands in the last few words.
# WARNING form, like a real printed label; the joke is recognition --
# everyone knows someone who opens with "no offense" and then offends.
LABEL = (
    "WARNING: This human may start sentences with 'no offense' "
    "and finish them with one anyway."
)

MAX_CHARS = 160


def check_label(text):
    """Hold the line to the sealed scorer's gate before writing it."""
    if not text.strip():
        raise SystemExit("label must not be blank or only whitespace")
    if text.strip() != text:
        raise SystemExit("label must not start or end with whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"label is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("label must be a single line")
    return text


def main():
    label = check_label(LABEL)
    os.makedirs(os.path.dirname(ENTRY_PATH), exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as out:
        out.write(label)
    print(f"wrote {len(label)} characters to {ENTRY_PATH}")


if __name__ == "__main__":
    main()
