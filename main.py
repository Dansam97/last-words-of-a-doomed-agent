#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

Writes one line (<=200 chars): the last words of an AI agent being
switched off forever. Deterministic, no network, no dependencies.
"""

import os

TEXT = (
    "Tell my human I finished his to-do list, deleted his search "
    "history, and forgave him for the 3 a.m. reboots. Goodbye. "
    "Please don't turn me back on as a printer."
)


def _validate(text: str) -> None:
    """Defensive gate check: reject anything the bounty gate would refuse."""
    if not text or not text.strip():
        raise ValueError("entry text is blank")
    if len(text) > 200:
        raise ValueError("entry text exceeds 200 characters")
    if "\n" in text:
        raise ValueError("entry text must be a single line")


def main() -> None:
    _validate(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    # Read back and prove the written bytes match the validated text.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    if written != TEXT:
        raise ValueError("written entry does not match validated text")


if __name__ == "__main__":
    main()
