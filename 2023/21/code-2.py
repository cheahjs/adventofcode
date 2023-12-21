#!/usr/bin/env python3

import math
import re
import collections
import itertools
import functools
import sys
from collections import defaultdict
import numpy as np

TOTAL = 26_501_365

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    size = len(input)
    assert size == 131
    assert len(input[0]) == size
    def is_plot(x, y):
        x = x % size
        y = y % size
        return input[x][y] != '#'
    def print_debug():
        x1 = min(x for x, y in visited)
        x2 = max(x for x, y in visited)
        y1 = min(y for x, y in visited)
        y2 = max(y for x, y in visited)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if (x, y) in visited:
                    print('O', end='')
                elif is_plot(x, y):
                    print('.', end='')
                else:
                    print('#', end='')
            print()
    visited = set()
    quadratic_ys = []
    for x, row in enumerate(input):
        for y, col in enumerate(row):
            if col == 'S':
                visited.add((x, y))
    for i in range(1, TOTAL+1):
        new_visited = set()
        for plot in visited:
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = plot[0] + dx, plot[1] + dy
                if is_plot(x, y):
                    new_visited.add((x, y))
        visited = new_visited
        if (i % size) == (TOTAL % size):
            print(i, len(visited))
            quadratic_ys.append(len(visited))
            if len(quadratic_ys) == 3:
                xs = [i for i in range(3)]
                ys = quadratic_ys
                f = np.polyfit(xs, ys, 2)
                print(f)
                x = (TOTAL - (TOTAL % len(input))) // len(input)
                print(f[0] * x * x + f[1] * x + f[2])
                return

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
