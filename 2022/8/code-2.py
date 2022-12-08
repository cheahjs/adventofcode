#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def main():
    grid = [[int(i) for i in x]
             for x in open('input.txt').read().strip().split('\n')]

    highest_score = -1
    for x, row in enumerate(grid):
        for y, tree in enumerate(row):
            # right, scan from y+1 -> edge (len(row))
            right = 0
            for new_y in range(y+1, len(row)):
                right += 1
                new_tree = grid[x][new_y]
                if tree <= new_tree:
                    # view blocked
                    break

            # left, scan from edge (0) -> y-1
            left = 0
            for i in range(0, y):
                new_y = y-1-i
                left += 1
                new_tree = grid[x][new_y]
                if tree <= new_tree:
                    # view blocked
                    break
            # down, scan from (x+1) -> edge (len(grid))
            down = 0
            for new_x in range(x+1, len(grid)):
                down += 1
                new_tree = grid[new_x][y]
                if tree <= new_tree:
                    # view blocked
                    break
            # up, scan from edge (0) -> (x-1)
            up = 0
            for i in range(0, x):
                new_x = x-i-1
                up += 1
                new_tree = grid[new_x][y]
                if tree <= new_tree:
                    # view blocked
                    break
            score = left*right*up*down
            # print((x,y), left, right, up, down, score)
            if score > highest_score:
                highest_score = score
    print(highest_score)


main()
