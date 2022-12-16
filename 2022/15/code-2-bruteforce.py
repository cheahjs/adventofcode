#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict
from tqdm import tqdm

MAX_COORD = 4_000_000

def dist(ax, ay, bx, by):
    return abs(ax-bx) + abs(ay-by)

def tuning(x, y):
    return x*4000000 + y

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
        print(f'{(bx, by)} is {d} away from {(sx, sy)}')
        with tqdm(total=(d*2)**2) as p:
            for dx in range(-d, d+1):
                for dy in range(-d, d+1):
                    p.update(1)
                    tx, ty = sx+dx, sy+dy
                    if dist(sx, sy, tx, ty) > d:
                        continue
                    grid.add((tx, ty))
    with tqdm(total=MAX_COORD**2) as p:
        for x in range(0, MAX_COORD):
            for y in range(0, MAX_COORD):
                p.update(1)
                if (x, y) in grid:
                    continue
                if (x, y) in beacons:
                    continue
                print(f'found {(x, y)}: {tuning(x, y)}')
main()
