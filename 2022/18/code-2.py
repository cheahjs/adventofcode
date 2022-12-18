#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

SIDES = [
    # x-axis
    [1, 0, 0], [-1, 0, 0],
    # y-axis
    [0, 1, 0], [0, -1, 0],
    # z-axis
    [0, 0, 1], [0, 0, -1],
]

def main():
    cubes = set([tuple([int(a) for a in x.split(',')]) for x in open('input.txt').read().strip().split('\n')])
    area = 0
    for (x,y,z) in cubes:
        # check all sides for another cube
        for (dx, dy, dz) in SIDES:
            if (x+dx, y+dy, z+dz) not in cubes:
                area += 1
    print(area)

main()
