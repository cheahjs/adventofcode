#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

AIR = 0
ROCK = 1
SAND = 2

class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError( key )
        else:
            ret = self[key] = self.default_factory(key)
            return ret


def main():
    inp = [x for x in open('input.txt').read().strip().split('\n')]
    bottom = 0
    grid = keydefaultdict(lambda k: ROCK if k[1] == bottom else AIR)
    for line in inp:
        points = [[int(y) for y in x.split(',')] for x in line.split(' -> ')]
        for i in range(len(points)-1):
            xs, ys = points[i]
            xe, ye = points[i+1]
            if ys > bottom:
                bottom = ys
            if ye > bottom:
                bottom = ye
            if xs == xe:
                for y in range(min(ys, ye), max(ys, ye)+1):
                    grid[(xs, y)] = 1
            elif ys == ye:
                for x in range(min(xs, xe), max(xs, xe)+1):
                    grid[(x, ys)] = 1
    bottom += 2
    while True:
        sx, sy = 500, 0
        # sand tick
        while True:
            # attempt to fall by one
            if grid[(sx, sy+1)] == AIR:
                sy += 1
            else:
                if grid[(sx-1, sy+1)] == AIR:
                    sx -= 1
                    sy += 1
                else:
                    if grid[(sx+1, sy+1)] == AIR:
                        sx += 1
                        sy += 1
                    else:
                        print(f'sand resting at {(sx, sy)}')
                        grid[(sx, sy)] = SAND
                        break
        if sx == 500 and sy == 0:
            break
    print(list(grid.values()).count(SAND))

main()
