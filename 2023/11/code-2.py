#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
from collections import defaultdict

# -----> +y
# |
# |
# v +x

EXPANSION_MULTIPLIER = 1_000_000

def print_universe(universe):
    max_x = max([x for (x, y) in universe])
    max_y = max([y for (x, y) in universe])
    for x in range(max_x+1):
        for y in range(max_y+1):
            if (x, y) in universe:
                print('#', end='')
            else:
                print('.', end='')
        print()

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    universe = defaultdict()
    x_d = 0
    for x, row in enumerate(input):
        empty_row = True
        for y, val in enumerate(row):
            if val == '#':
                empty_row = False
                universe[(x+x_d, y)] = val
        if empty_row:
            x_d += EXPANSION_MULTIPLIER-1
    # Make another pass to expand columns
    for y in range(len(input[0])-1, 0, -1):
        filled_col = any(y2 == y for (_, y2) in universe)
        if not filled_col:
            # shift all columns > y to the right
            for (x2, y2) in list(universe):
                if y2 > y:
                    universe[(x2, y2+EXPANSION_MULTIPLIER-1)] = '#'
                    del universe[(x2, y2)]
    # print_universe(universe)
    path = 0
    # shortest path is manhattan distance
    galaxies = universe.keys()
    for combo in itertools.combinations(galaxies, 2):
        dist = abs(combo[0][0] - combo[1][0]) + abs(combo[0][1] - combo[1][1])
        path += dist
    print(path)

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
