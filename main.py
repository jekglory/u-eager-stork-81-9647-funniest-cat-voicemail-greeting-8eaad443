"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes one original cat voicemail greeting (a single line, 115
characters, within the 120-character limit) as plain text to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure Python standard library only. Deterministic: the greeting is a
fixed string, so every run produces byte-identical output. The output
directory is treated as provided by the grader: it is created only if
missing and its contents are never deleted.
"""

import os

GREETING = "You've reached Miso. I'm sitting on the keyboard you need, so leave a message after the beep. I'll sit on that too."


def main():
    assert "\n" not in GREETING, "greeting must be a single line"
    assert len(GREETING) <= 120, "greeting must be at most 120 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(GREETING + "\n")


if __name__ == "__main__":
    main()
