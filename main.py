#!/usr/bin/env python3
"""Write one original one-line comedy joke to entry.txt.

Deterministic: standard library only, no network, no randomness,
no time or date dependence. Every run writes byte-identical output.
"""

import os

JOKE = (
    "My sourdough starter is the only thing in my kitchen that listens "
    "to me \u2014 and the only thing that rises to the occasion."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
