#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second -- entry program.

Writes one sentence (at most 200 characters) pitching a bizarre startup
idea to /output/entry.txt. The program is fully deterministic: it writes
the same sentence on every run, uses only the Python standard library,
and touches no network, clock, or file outside this repository.
"""

import os

PITCH = (
    "We rent out actors to pose as your wildly successful cousin at family "
    "dinners, so your relatives finally stop asking when you'll get a real "
    "job \u2014 $200 a night, smugness included."
)


def main() -> None:
    # One sentence: a single terminal period, no newlines, 1-200 chars.
    if not 1 <= len(PITCH) <= 200:
        raise SystemExit("pitch must be 1 to 200 characters")
    if PITCH.count(".") != 1 or not PITCH.endswith(".") or "\n" in PITCH:
        raise SystemExit("pitch must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
