#!/usr/bin/env python3

import sys

def catch_pokemons() -> str:
    n, rows, columns = map(int, sys.stdin.readline().split())
    pokemons = []
    for _ in range(n):
        pokemon = sys.stdin.readline().rstrip()
        pokemons.append(pokemon)
        pokemons.append(pokemon[::-1])

    characters = []
    for _ in range(rows):
        characters += sys.stdin.readline().split()
    result = ''.join(characters)
    while (True):
        found = False

        for pokemon in pokemons:
            try:
                offset = result.index(pokemon)
                result = result[:offset] + result[offset + len(pokemon):]
                found = True
            except ValueError:
                pass

        if not found:
            return result
    

def main() -> int:
    first_line = sys.stdin.readline()
    cases = int(first_line.rstrip())
    for i in range(cases):
        print("Case #{}: {}".format(str(i + 1), catch_pokemons()))
    return 0


if __name__ == '__main__':
    sys.exit(main())
