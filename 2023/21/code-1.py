#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
from collections import defaultdict

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    max_x = len(input)
    max_y = len(input[0])
    plots = set()
    visited = set()
    for x, row in enumerate(input):
        for y, col in enumerate(row):
            if col == '.':
                plots.add((x, y))
            elif col == 'S':
                plots.add((x, y))
                visited.add((x, y))
    def print_debug():
        for x in range(max_x):
            for y in range(max_y):
                if (x, y) in visited:
                    print('O', end='')
                elif (x, y) in plots:
                    print('.', end='')
                else:
                    print('#', end='')
            print()
    for i in range(64):
        print(i, len(visited))
        new_visited = set()
        for plot in visited:
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = plot[0] + dx, plot[1] + dy
                if x < 0 or x >= max_x or y < 0 or y >= max_y:
                    continue
                if (x, y) in plots:
                    new_visited.add((x, y))
        visited = new_visited
        # print_debug()
    print(len(visited))

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
