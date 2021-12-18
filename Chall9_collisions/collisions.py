#!/usr/bin/env python3

import sys


class Bitmask:
    def __init__(self, bitarray, width, height):
        self.bitarray = bitarray
        self.width = width
        self.height = height


class Sprite:
    def __init__(self, bitmask, x, y):
        self.bitmask = bitmask
        self.x = x
        self.y = y
        self.xmax = x + bitmask.width
        self.ymax = y + bitmask.height
        self.pixels = set()
        self.__init_pixels()

    
    def __init_pixels(self):
        for y in range(self.bitmask.height):
            for x in range(self.bitmask.width):
                if self.bitmask.bitarray[y * self.bitmask.width + x] == 1:
                    self.pixels.add((self.x + x, self.y + y))


    def collides(self, other):
        return self.__intersects(other) and \
                any(p in self.pixels for p in other.pixels)


    def __intersects(self, other):
        return self.xmax >= other.x and self.ymax >= other.y and \
                other.xmax >= self.x and other.ymax >= self.y


def collisions(sprites):
    n = 0
    for i in range(len(sprites)):
        for j in range(i + 1, len(sprites)):
            if sprites[i].collides(sprites[j]):
                n += 1
    return str(n)


def main():
    cases = int(sys.stdin.readline().rstrip())

    bitmasks = []
    n = int(sys.stdin.readline().rstrip())
    for i in range(n):
        (width, height) = [int(s) for s in sys.stdin.readline().split()]
        bitarray = []
        for j in range(height):
            bitarray += list(map(int, (sys.stdin.readline().rstrip())))
        bitmasks.append(Bitmask(bitarray, width, height))

    for i in range(cases):
        sprites = []
        n = int(sys.stdin.readline().rstrip())
        for _ in range(n):
            (identifier, x, y) = [int(s) for s in sys.stdin.readline().split()]
            sprites.append(Sprite(bitmasks[identifier], x, y))
        print("Case #{}: {}".format(str(i + 1), collisions(sprites)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
