#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

AIR = 0
ROCK = 1
SAND = 2

def main():
    inp = [x for x in open('input.txt').read().strip().split('\n')]
    grid = defaultdict(int)
    bottom = 0
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
    spawn = True
    while spawn:
        sx, sy = 500, 0
        # sand tick
        while sy <= bottom:
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
                        grid[(sx, sy)] = SAND
                        break
        if sy > bottom:
            spawn = False
    print(list(grid.values()).count(SAND))

main()
