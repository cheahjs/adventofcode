#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def main():
    grid = [[int(i) for i in x]
             for x in open('input.txt').read().strip().split('\n')]

    visible = set()

    # left
    for x, row in enumerate(grid):
        min_height = -1
        for y in range(len(row)):
            tree = grid[x][y]
            # print('left', x, y, min_height, tree)
            if tree > min_height:
                # print('adding', x, y, 'with height', tree)
                min_height = tree
                visible.add((x, y))

    # right
    for x, row in enumerate(grid):
        min_height = -1
        for i in range(len(row)):
            y = len(row) - 1 - i
            tree = grid[x][y]
            # print('right', x, y, min_height, tree)
            if tree > min_height:
                # print('adding', x, y, 'with height', tree)
                min_height = tree
                visible.add((x, y))

    # top
    for y in range(len(grid[0])):
        min_height = -1
        for x in range(len(grid)):
            tree = grid[x][y]
            # print('top', x, y, min_height, tree)
            if tree > min_height:
                # print('adding', x, y, 'with height', tree)
                min_height = tree
                visible.add((x, y))

    # bottom
    for y in range(len(grid[0])):
        min_height = -1
        for i in range(len(grid)):
            x = len(grid) - i - 1
            tree = grid[x][y]
            # print('bottom', x, y, min_height, tree)
            if tree > min_height:
                # print('adding', x, y, 'with height', tree)
                min_height = tree
                visible.add((x, y))

    # for (x,y) in visible:
    #     if x == 0 or x == len(grid[0])-1 or y == 0 or y == len(grid)-1:
    #         continue
    #     print(x+1,y+1)
    print(visible)
    print(len(visible))

main()
