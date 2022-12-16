#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict
import z3

MAX_COORD = 4_000_000

def dist(ax, ay, bx, by):
    return abs(ax-bx) + abs(ay-by)

def tuning(x, y):
    return x*4000000 + y

def z3_abs(a):
    return z3.If(a >= 0, a, -a)

def main():
    inp = [x for x in open('input.txt').read().strip().split('\n')]
    solver = z3.Solver()
    x = z3.Int('x')
    y = z3.Int('y')
    solver.add(0 <= x)
    solver.add(x <= MAX_COORD)
    solver.add(0 <= y)
    solver.add(y <= MAX_COORD)
    for line in inp:
        matches = re.match(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
        sx, sy = int(matches[1]), int(matches[2])
        bx, by = int(matches[3]), int(matches[4])
        d = dist(sx, sy, bx, by)
        print(f'{(bx, by)} is {d} away from {(sx, sy)}')
        solver.add(z3_abs(x - sx) + z3_abs(y - sy) > d)
    print(solver.check())
    m = solver.model()
    print(m)
    print(tuning(m[x].as_long(), m[y].as_long()))

main()
