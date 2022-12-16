#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

TEST_Y = 2000000

def dist(ax, ay, bx, by):
    return abs(ax-bx) + abs(ay-by)

def main():
    inp = [x for x in open('input.txt').read().strip().split('\n')]
    grid = set()
    beacons = set()
    for line in inp:
        matches = re.match(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
        sx, sy = int(matches[1]), int(matches[2])
        bx, by = int(matches[3]), int(matches[4])
        beacons.add((bx, by))
        d = dist(sx, sy, bx, by)
        for dx in range(-d, d+1):
            ty = TEST_Y
            tx = sx+dx
            if dist(sx, sy, tx, ty) > d:
                continue
            grid.add((tx, ty))
    ml = min(grid, key=lambda x: x[0])[0]
    mh = max(grid, key=lambda x: x[0])[0]
    print(f'scanning from {ml} to {mh}')
    cannot = 0
    for x in range(ml, mh+1):
        if (x, TEST_Y) in grid and (x, TEST_Y) not in beacons:
            cannot += 1
    print(cannot)

main()
