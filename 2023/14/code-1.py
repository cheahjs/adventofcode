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

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    static_rocks = set()
    movable_rocks = set()
    for x, row in enumerate(input):
        for y, col in enumerate(row):
            if col == '#':
                static_rocks.add((x, y))
            elif col == 'O':
                movable_rocks.add((x, y))
    # Tilt north (negative x)
    # Iterate left to right, top to bottom to resolve conflicts
    for y in range(len(input[0])):
        for x in range(len(input)):
            if (x, y) in movable_rocks:
                x2 = x
                while x2 > 0 and (x2 - 1, y) not in static_rocks and (x2 - 1, y) not in movable_rocks:
                    x2 -= 1
                movable_rocks.remove((x, y))
                movable_rocks.add((x2, y))
    # Print for debugging
    # for x in range(len(input)):
    #     for y in range(len(input[0])):
    #         if (x, y) in static_rocks:
    #             print('#', end='')
    #         elif (x, y) in movable_rocks:
    #             print('O', end='')
    #         else:
    #             print('.', end='')
    #     print()
    # Calculate load
    load = 0
    max_load = len(input)
    for (x, y) in movable_rocks:
        load += max_load-x
    print(load)

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
