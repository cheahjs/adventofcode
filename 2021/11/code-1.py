#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

adjs = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1],           [0, 1],
    [1, -1],  [1, 0],  [1, 1]
]

def print_debug(grid):
    print('\n'.join([''.join([str(i) for i in x]) for x in grid]))

def main():
    # energy level grid, 0-9
    grid = [[int(i) for i in x]
             for x in open('input.txt').read().strip().split('\n')]

    rows = len(grid)
    cols = len(grid[0])

    flashes = 0

    for i in range(100):
        flash_queue = []
        flashed = {}
        # initial increment
        for x in range(rows):
            for y in range(cols):
                grid[x][y] += 1
                if grid[x][y] > 9:
                    flash_queue.append((x, y))

        while len(flash_queue) > 0:
            f_x, f_y = flash_queue.pop()
            if (f_x, f_y) in flashed:
                continue
            flashed[(f_x, f_y)] = True
            for adj in adjs:
                n_x, n_y = f_x + adj[0], f_y + adj[1]
                if not (0 <= n_x < rows and 0 <= n_y < cols):
                    continue
                grid[n_x][n_y] += 1
                if grid[n_x][n_y] > 9:
                    flash_queue.append((n_x, n_y))

        for x, y in flashed.keys():
            grid[x][y] = 0

        flashes += len(flashed)

    print('Flashes:', flashes)

main()
