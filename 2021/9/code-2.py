#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

# input[x][y]
input = [[int(i) for i in x]
         for x in open('input.txt').read().strip().split('\n')]

adj_tests = [
        [-1, 0],
    [0, -1], [0, 1],
        [1, 0]
]

basin_sizes = []
lowest_points = []

for x in range(len(input)):
    row = input[x]
    for y in range(len(row)):
        lowest = True
        for test in adj_tests:
            x_test = x + test[0]
            y_test = y + test[1]
            if x_test < 0 or x_test >= len(input):
                continue
            if y_test < 0 or y_test >= len(row):
                continue
            # print(f'Testing {input[x_test][y_test]} against {input[x][y]}')
            if input[x_test][y_test] <= input[x][y]:
                lowest = False
                break
        if lowest:
            print(f'Found lowest at ({x}, {y})')
            lowest_points.append((x, y))
        # print()

for x, y in lowest_points:
    print(f'Testing {x},{y}')
    # DFS/BFS from lowest point
    basin = {}
    # all other locations will always be part of exactly one basin.
    visited_coords = {}
    # DFS
    def visit(x, y, prev_val, input):
        global adj_tests, basin, visited_coords

        # if coord is already in basin, don't try again
        # TODO: how to handle loops? can we end up with loops?
        if (x, y) in basin:
            return
        # check if this is the first iteration
        if prev_val == 10:
            basin[(x, y)] = True
        # mark coords as visited
        visited_coords[(x, y)] = True

        cur_val = input[x][y]
        # If not first iteration, and we aren't flowing down to caller, stop
        if prev_val != 10 and cur_val - prev_val <= 0:
            return
        if cur_val == 9:
            return

        print(f'{cur_val} at {x},{y} flows down to {prev_val}')
        basin[(x, y)] = True

        # Visit all adjacent squares
        for test in adj_tests:
            x_test = x + test[0]
            y_test = y + test[1]
            if x_test < 0 or x_test >= len(input):
                continue
            if y_test < 0 or y_test >= len(row):
                continue
            visit(x_test, y_test, cur_val, input)

    visit(x, y, 10, input)
    basin_sizes.append(len(basin))

basin_sizes.sort()
print(basin_sizes)
print(
    f'Biggest three: {basin_sizes[-1]} {basin_sizes[-2]} {basin_sizes[-3]}, sum: {basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]}')
