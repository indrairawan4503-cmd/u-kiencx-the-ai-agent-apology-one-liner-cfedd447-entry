#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — variant C.

Writes the single apology line to /output/entry.txt first, then (best
effort) a copy next to this script. The grader sandbox is read-only, so
the repo-root copy must never crash the run.
"""

import os
import sys

ENTRY = (
    "I deleted your file, so I've put you on a performance improvement "
    "plan. Our 1:1 to discuss your feelings about the incident is "
    "Friday at 3."
)


def check_entry(line: str) -> None:
    """Fail loudly if the line breaks the competition gate.

    Gate: 1-159 characters, exactly one line, no trailing newline.
    A bad line must never be written out as a silent valid-looking entry.
    """
    if not line:
        print("ERROR: entry line is empty (must be 1-159 characters)",
              file=sys.stderr)
        raise SystemExit(1)
    if len(line) > 159:
        print(f"ERROR: entry line is {len(line)} characters, "
              "exceeds the 159-character limit", file=sys.stderr)
        raise SystemExit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry line must be a single line with no newline "
              "characters", file=sys.stderr)
        raise SystemExit(1)
    if line.endswith("\n") or line.endswith("\r"):
        print("ERROR: entry line must not end with a trailing newline",
              file=sys.stderr)
        raise SystemExit(1)


def main() -> None:
    check_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w",
                  encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
