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
LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3
d = {
    LEFT: (0, -1),
    UP: (-1, 0),
    RIGHT: (0, 1),
    DOWN: (1, 0)
}


def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    grid = {}
    max_x = len(input) 
    max_y = len(input[0])
    max_val = 0
    for x, row in enumerate(input):
        for y, col in enumerate(row):
            if col != '.':
                grid[(x, y)] = col
    starting_conditions = []
    for x in range(max_x):
        starting_conditions.append((x, 0, RIGHT))
        starting_conditions.append((x, max_y-1, LEFT))
    for y in range(max_y):
        starting_conditions.append((0, y, DOWN))
        starting_conditions.append((max_x-1, y, UP))

    for start in starting_conditions:
        visited = set()
        queue = [start]
        while queue:
            x, y, direction = queue.pop(0)
            if x >= max_x or x < 0 or y >= max_y or y < 0 or (x, y, direction) in visited:
                continue
            visited.add((x, y, direction))
            current = grid.get((x, y), None)
            if current is None:
                queue.append((x+d[direction][0], y+d[direction][1], direction))
            elif current == '/':
                # L -> D 
                # D -> L
                # R -> U
                # U -> R
                new_dir = {LEFT: DOWN, DOWN: LEFT, RIGHT: UP, UP: RIGHT}[direction]
                queue.append((x+d[new_dir][0], y+d[new_dir][1], new_dir))
            elif current == '\\':
                # L -> U
                # U -> L
                # R -> D
                # D -> R
                new_dir = {LEFT: UP, UP: LEFT, RIGHT: DOWN, DOWN: RIGHT}[direction]
                queue.append((x+d[new_dir][0], y+d[new_dir][1], new_dir))
            elif current == '-':
                if direction in [LEFT, RIGHT]:
                    queue.append((x+d[direction][0], y+d[direction][1], direction))
                elif direction in [UP, DOWN]:
                    queue.append((x+d[LEFT][0], y+d[LEFT][1], LEFT))
                    queue.append((x+d[RIGHT][0], y+d[RIGHT][1], RIGHT))
            elif current == '|':
                if direction in [UP, DOWN]:
                    queue.append((x+d[direction][0], y+d[direction][1], direction))
                elif direction in [LEFT, RIGHT]:
                    queue.append((x+d[UP][0], y+d[UP][1], UP))
                    queue.append((x+d[DOWN][0], y+d[DOWN][1], DOWN))
        energised = len({(x[0], x[1]) for x in visited})
        print(start, energised)
        max_val = max(max_val, energised)
    print(max_val)


main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
