#!/usr/bin/env python3
"""One Letter for Your Day entry.

Writes exactly one letter, ``Z``, to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``). Python 3.13 standard library only; no network,
no randomness, fully deterministic.

The word behind the letter is "zombie": the day left me shambling
through it on zero sleep, half-dead but still moving. Z is vivid (a
zombie is a sharp picture, not a vague mood), funny (everyone has had
a zombie day), true (an honest report of an ordinary wiped-out day),
and the letter fits the word exactly: zombie starts with Z, and the
letter even sounds like one. The rules themselves cite "Z for zero
sleep", the same day.
"""

import os

LETTER = "Z"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)
    # Self-check the gate condition: re-read and verify the file holds
    # exactly one uppercase letter A-Z, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if len(written) != 1 or not ("A" <= written <= "Z"):
        raise SystemExit(f"entry.txt failed the gate: {written!r}")


if __name__ == "__main__":
    main()
