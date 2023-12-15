#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
from collections import defaultdict
from tqdm import tqdm


# -----> +y
# |
# |
# v +x

CYCLE_COUNT = 1000000000

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
    max_x = len(input)
    max_y = len(input[0])
    prev_seen = set()
    def run_cycle():
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
        # Tilt west (negative y)
        # Iterate left to right, top to bottom to resolve conflicts
        for y in range(len(input[0])):
            for x in range(len(input)):
                if (x, y) in movable_rocks:
                    y2 = y
                    while y2 > 0 and (x, y2-1) not in static_rocks and (x, y2-1) not in movable_rocks:
                        y2 -= 1
                    movable_rocks.remove((x, y))
                    movable_rocks.add((x, y2))
        # Tilt south (positive x)
        # Iterate left to right, bottom to top to resolve conflicts
        for y in range(len(input[0])):
            for x in reversed(range(len(input))):
                if (x, y) in movable_rocks:
                    x2 = x
                    while x2 < max_x-1 and (x2 + 1, y) not in static_rocks and (x2 + 1, y) not in movable_rocks:
                        x2 += 1
                    movable_rocks.remove((x, y))
                    movable_rocks.add((x2, y))
        # Tilt east (positive y)
        # Iterate right to left, top to bottom to resolve conflicts
        for y in reversed(range(len(input[0]))):
            for x in range(len(input)):
                if (x, y) in movable_rocks:
                    y2 = y
                    while y2 < max_y-1 and (x, y2+1) not in static_rocks and (x, y2+1) not in movable_rocks:
                        y2 += 1
                    movable_rocks.remove((x, y))
                    movable_rocks.add((x, y2))
    def debug_print():
        for x in range(len(input)):
            for y in range(len(input[0])):
                if (x, y) in static_rocks:
                    print('#', end='')
                elif (x, y) in movable_rocks:
                    print('O', end='')
                else:
                    print('.', end='')
            print()
    first_repeat = None
    i = 1
    while i <= CYCLE_COUNT:
        run_cycle()
        i += 1
        cur_state = frozenset(movable_rocks)
        if cur_state in prev_seen:
            print('Cycle detected at', i)
            prev_seen.clear()
            if first_repeat is None:
                first_repeat = i
            else:
                cycle = i - first_repeat
                print('Cycle length', cycle)
                remaining_cycles = ((CYCLE_COUNT-i) % cycle) + 1
                print(f'Remaining cycles: {remaining_cycles}')
                for _ in tqdm(range(remaining_cycles)):
                    run_cycle()
                break
        prev_seen.add(cur_state)
    # Calculate load
    load = 0
    max_load = len(input)
    for (x, y) in movable_rocks:
        load += max_load-x
    print(load)

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
