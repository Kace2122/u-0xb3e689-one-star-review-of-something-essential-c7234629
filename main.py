#!/usr/bin/env python3
"""One-star review of an everyday essential: sleep.

Writes a single deadpan one-star review (one line, at most 160
characters) to /output/entry.txt. Fully deterministic: the text is a
constant, so every run writes byte-identical output.
"""

import os

ENTRY = "One star. Sleep takes eight hours a day, offers no refund, and every morning I wake up still tired, as if it did the bare minimum and left early."


def main():
    text = ENTRY
    assert 1 <= len(text) <= 160, f"entry length {len(text)} outside 1-160"
    assert text == text.strip(), "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert "!" not in text, "deadpan: no exclamation marks"
    assert len(text.encode("utf-8")) <= 160, "entry exceeds 160 UTF-8 bytes"
    assert text.startswith("One star"), "entry must open as a one-star review"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
