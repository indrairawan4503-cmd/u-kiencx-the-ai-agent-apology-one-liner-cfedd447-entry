#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — variant C.

Writes the single apology line to /output/entry.txt first, then (best
effort) a copy next to this script. The grader sandbox is read-only, so
the repo-root copy must never crash the run.
"""

import os

ENTRY = (
    "I deleted your file, so I've put you on a performance improvement "
    "plan. Our 1:1 to discuss your feelings about the incident is "
    "Friday at 3."
)


def main() -> None:
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
