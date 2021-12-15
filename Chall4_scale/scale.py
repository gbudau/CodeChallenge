#!/usr/bin/env python3

import sys


NOTES_SHARP = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
NOTES_FLAT = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]


def scale(scale_root: str, steps: str) -> str:
    if scale_root in NOTES_SHARP:
        offset = NOTES_SHARP.index(scale_root)
    else:
        offset = NOTES_FLAT.index(scale_root)

    new_scale = scale_root;
    start_offset = offset
    length = len(NOTES_SHARP)
    for i in range(len(steps)):
        if steps[i] == "T":
            offset = (offset + 2) % length
        elif steps[i] == "s":
            offset = (offset + 1) % length
        note = NOTES_SHARP[offset]
        if steps[i] == "T" and note == "C":
            note = "B#"
        elif steps[i] == "T" and note == "F":
            note = "E#"
        if i < len(steps) - 1:
            if note[0] in new_scale:
                note = NOTES_FLAT[offset]
        elif start_offset == offset:
            note = scale_root
        new_scale = new_scale + note
    return new_scale


def main() -> int:
    first_line = sys.stdin.readline()
    cases = int(first_line.rstrip())
    for i in range(cases):
        scale_root = sys.stdin.readline().rstrip()
        steps = sys.stdin.readline().rstrip()
        print("Case #{}: {}".format(str(i + 1), scale(scale_root, steps)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
