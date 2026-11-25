#!/usr/bin/env python3
"""Everyday Wonder — one-line entry.

Writes a single sentence (at most 200 characters) that makes a small everyday
moment strange and new to /output/entry.txt (the harness gate path), falling
back to ./output/entry.txt when /output is not writable locally.
"""

import os

SENTENCE = (
    "The elevator mirror showed me arriving half a second before I did, "
    "and all the way down I kept checking which of us was still inside."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"sentence is {len(text)} characters, must be 1-200"
    assert text.strip(), "sentence must not be only whitespace"
    written = []
    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            written.append(path)
            print(f"wrote {len(text)} characters to {path}")
        except OSError as exc:
            print(f"cannot write {path}: {exc}")
    if not written:
        raise SystemExit("no writable output path")
    print(text)
    print(f"characters: {len(text)}")


if __name__ == "__main__":
    main()
