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

def create_pred(x, y, d):
    return lambda nx, ny: dist(nx, ny, x, y) > d

def main():
    inp = [x for x in open('input.txt').read().strip().split('\n')]
    preds = []
    beacons = set()
    for line in inp:
        matches = re.match(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
        sx, sy = int(matches[1]), int(matches[2])
        bx, by = int(matches[3]), int(matches[4])
        beacons.add((bx, by))
        d = dist(sx, sy, bx, by)
        print(f'{(bx, by)} is {d} away from {(sx, sy)}')
        preds.append(create_pred(sx, sy, d))
    with tqdm(total=MAX_COORD**2) as p:
        for x in range(0, MAX_COORD):
            for y in range(0, MAX_COORD):
                p.update(1)
                break_outer = False
                for pred in preds:
                    if not pred(x, y):
                        break_outer = True
                        break
                if break_outer:
                    continue
                if (x, y) in beacons:
                    continue
                print(f'found {(x, y)}: {tuning(x, y)}')
main()
