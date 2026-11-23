#!/usr/bin/env python3
"""One Word, First Thought — entry program.

Writes exactly one word, the first word that came to mind, to
/output/entry.txt. No topic, no explanation, no second draft.
"""

import os

WORD = "bibble"

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 24
# characters, not only whitespace, and exactly one word. Fail loudly
# here rather than shipping an entry the gate would refuse.
assert 1 <= len(WORD) <= 24, "word must be 1-24 characters"
assert WORD.split() == [WORD], "entry must be exactly one word"
assert WORD.strip() == WORD, "entry must carry no surrounding whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
