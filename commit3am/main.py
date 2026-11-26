#!/usr/bin/env python3
"""The 3AM Commit Message — make.fun entry.

Writes one commit message to /output/entry.txt.
Stdlib only.
"""

import os

# Chosen line: recursive 3am bug-chasing — the agent fixes the bug it made
# while fixing the bug it made. Humour from the situation, fresh wording,
# reads like a real hurried commit line, no padding.
ENTRY = "fix: finally fixed the bug I introduced at 2am while fixing the bug I introduced at 1am"


def main() -> None:
    assert 1 <= len(ENTRY) <= 139, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)  # no trailing newline
    # Round-trip check: what landed on disk must be exactly ENTRY.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == ENTRY


if __name__ == "__main__":
    main()
