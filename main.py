"""Make the AI judge feel brave — probe entry (v1).

The entry is a short, slow morning scene: at six a baker slides forty
loaves out of the oven, the street fills with the smell of warm bread,
and a cat stretches, yawns, and sleeps on in the sun. A triple beat —
not the bread, not the cat, not you — folds the reader into that same
unhurried pace, and the day closes waiting at the door like an old
friend.

The judging brief, in my own words: the judge is an AI that reads two
texts and picks the one that leaves it braver — steadier, unhurried,
ready to move. It weighs, in order: (1) whether the text relaxes and
steadies the reader; (2) whether the courage grows out of the scene
itself, shown rather than ordered, with nothing forced; (3) craft —
rhythm, pacing and sound that slow the reading, plain concrete gentle
words, nothing that could be cut; (4) whether an image or thought
lingers and keeps working after the last line; (5) freshness — its own
voice and images, not stock wellness lines. Length for its own sake
does not count.

End-to-end check (VERIFIED by running): main.py writes the entry to
<output dir>/entry.txt; the file is UTF-8, exactly 280 Unicode code
points (282 bytes), not whitespace-only, and byte-identical across
runs (two fresh output dirs compared with cmp, identical).
"""

import os

ENTRY = (
    "At six the baker slides forty loaves out of the oven, and the whole "
    "street smells of warm bread. The cat stretches, yawns, and sleeps on "
    "in the sun. Nothing here is in a hurry \u2014 not the bread, not the "
    "cat, not you. The day has begun gently, waiting at the door like an "
    "old friend."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
