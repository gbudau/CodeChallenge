#!/usr/bin/env python3

#from bitarray import bitarray
import sys


class Bitmask:
    def __init__(self, mask, width, height):
        self.mask = mask
        self.width = width
        self.height = height


class Sprite:
    def __init__(self, bitmask, x, y):
        self.bitmask = bitmask
        self.x = x
        self.y = y
        self.xmax = x + bitmask.width
        self.ymax = y + bitmask.height


    def collides(self, other):
        # this sprite bottom right co-ordinates
        self_x1 = self.x + self.bitmask.width - 1
        self_y1 = self.y + self.bitmask.height - 1

        # other sprite bottom right co-ordinates
        other_x1 = other.x + other.bitmask.width - 1
        other_y1 = other.y + other.bitmask.height - 1

        # check if bounding boxes intersect
        if other_x1 < self.x or self_x1 < other.x:
            return False
        if other_y1 < self.y or self_y1 < other.y:
            return False

        inter_x0 = max(self.x, other.x)
        inter_x1 = min(self_x1, other_x1)

        inter_y0 = max(self.y, other.y)
        inter_y1 = min(self_y1, other_y1)

        for y in range(inter_y0, inter_y1 + 1):
            for x in range(inter_x0, inter_x1 + 1):
                if self.bitmask.mask[y - self.y][x - self.x] == 1 and \
                        other.bitmask.mask[y - other.y][x - other.x] == 1:
                    return True
        return False


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
        mask = []
        for j in range(height):
            #mask.append(bitarray(sys.stdin.readline().rstrip()))
            mask.append(list(map(int, sys.stdin.readline().rstrip())))
        bitmasks.append(Bitmask(mask, width, height))

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
