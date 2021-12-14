#!/usr/bin/env python3

import sys

def min_win_roll(player_roll: str) -> str:
    player_roll_split = player_roll.split(":")
    roll_sum = int(player_roll_split[0]) + int(player_roll_split[1])
    if (roll_sum < 12):
        return str(roll_sum + 1)
    return "-"
    

def main() -> int:
    first_line = sys.stdin.readline()
    cases = int(first_line.rstrip())
    for i in range(cases):
        line = sys.stdin.readline()
        player_roll = line.rstrip()
        print("Case #{}: {}".format(str(i + 1), min_win_roll(player_roll)))
    return 0

if __name__ == '__main__':
    sys.exit(main())
