#!/usr/bin/env python3
"""Writes one original one-line comedy joke to entry.txt.

Standard library only, no network, fully deterministic:
every run writes the same bytes.
"""

import os

JOKE = "I wave at security cameras because somewhere a bored guard deserves a plot twist."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
