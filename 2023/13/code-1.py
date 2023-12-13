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
    input = [x.split('\n') for x in open(input_file).read().strip().split('\n\n')]
    score = 0
    for raw_pattern in input:
        grid = set()
        for x, line in enumerate(raw_pattern):
            for y, char in enumerate(line):
                if char == '#':
                    grid.add((x,y))
        def test_x(x):
            print(f'testing x reflection line at {x}')
            for (x2, y2) in grid:
                if x2 < x:
                    # reflect to the bottom and test
                    xr = x + (x-x2)-1
                    # we reflected beyond the grid, don't need to test
                    if xr >= len(raw_pattern):
                        # print(f'reflected {x2},{y2} to {xr},{y2} which is beyond the grid')
                        continue
                    if (xr, y2) not in grid:
                        # print(f'reflected {x2},{y2} to {xr},{y2} which is not in the grid')
                        return False
                else:
                    # reflect to the top and test
                    xr = x - (x2-x) - 1
                    # we reflected beyond the grid, don't need to test
                    if xr < 0:
                        continue
                    if (xr, y2) not in grid:
                        return False
            return True
        def test_y(y):
            print(f'testing y reflection line at {y}')
            for (x2, y2) in grid:
                if y2 < y:
                    # reflect to the right and test
                    yr = y + (y-y2)-1
                    # we reflected beyond the grid, don't need to test
                    if yr >= len(raw_pattern[0]):
                        continue
                    if (x2, yr) not in grid:
                        return False
                else:
                    # reflect to the left and test
                    yr = y - (y2-y) - 1
                    # we reflected beyond the grid, don't need to test
                    if yr < 0:
                        continue
                    if (x2, yr) not in grid:
                        return False
            return True
        # test all x and y axis reflections
        # reflection line to the left/top of the grid
        for x in range(1, len(raw_pattern)):
            if test_x(x):
                print(f'x reflection line at {x}')
                score += x*100
                break
        for y in range(1, len(raw_pattern[0])):
            if test_y(y):
                print(f'y reflection line at {y}')
                score += y
                break
    print(score)
main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
