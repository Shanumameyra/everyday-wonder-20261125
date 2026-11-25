#!/usr/bin/env python3
"""Everyday Wonder — one-line entry.

A single sentence (at most 200 characters) that makes a small everyday
moment strange and new. The sentence is the entry.
"""

SENTENCE = (
    "The elevator mirror showed me arriving half a second before I did, "
    "and all the way down I kept checking which of us was still inside."
)


def main() -> None:
    print(SENTENCE)
    print(f"characters: {len(SENTENCE)}")


if __name__ == "__main__":
    main()
