#!/usr/bin/env python3

import sys


def calculate_value(word: str, dictionary: dict) -> float:
    value = 0.0
    for char in word:
        if char in dictionary:
            value = value + dictionary[char]
    return value


def winning_antonym(line: str) -> str:
    words, letters = line.split("|")
    first_word, second_word = words.split("-")
    dictionary = eval("dict({})".format(letters))
    first_value = calculate_value(first_word, dictionary)
    second_value = calculate_value(second_word, dictionary)
    if first_value == second_value:
        return "-"
    elif first_value > second_value:
        return first_word
    return second_word


def main() -> int:
    first_line = sys.stdin.readline()
    cases = int(first_line.rstrip())
    for i in range(cases):
        line = sys.stdin.readline().rstrip()
        print("Case #{}: {}".format(str(i + 1), winning_antonym(line)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
