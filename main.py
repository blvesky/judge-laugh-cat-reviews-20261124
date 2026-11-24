#!/usr/bin/env python3
"""Entry for make.fun: Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, written by a house cat
about its human, to /output/entry.txt (1-200 characters, single line).
"""
import os

ENTRY = (
    "One star. I slept on the warm laptop to help him work. "
    "He moved me, typed for an hour, then blamed ME for the email. "
    "I have filed a formal complaint with the sunbeam."
)


def main() -> None:
    if not (1 <= len(ENTRY) <= 200):
        raise SystemExit(f"entry must be 1-200 chars, got {len(ENTRY)}")
    if "\n" in ENTRY or ENTRY != ENTRY.strip():
        raise SystemExit("entry must be a single non-blank line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
