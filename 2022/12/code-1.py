#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict
from queue import PriorityQueue

def main():
    grid = [[ord(c)-96 for c in x] for x in open('input.txt').read().strip().split('\n')]
    rows = len(grid)
    cols = len(grid[0])
    start = None
    end = None
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == -13:
                start = (x, y)
                grid[y][x] = ord('a')-96
            if val == -27:
                end = (x, y)
                grid[y][x] = ord('z')-96
    print(start)
    print(end)
    # pathfinding
    # (x, y) -> [path]
    prevs = {start: []}
    q = [start]
    while len(q) > 0:
        x, y = q.pop(0)
        h = grid[y][x]
        print(f'visiting {x, y}: {h}')
        for adj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_x, new_y = (x + adj[0], y + adj[1])
            # in range
            if not (0 <= new_y < rows and 0 <= new_x < cols):
                continue
            # viable visit
            new_h = grid[new_y][new_x]
            print(f'  checking ({new_x}, {new_y}): {new_h}')
            if new_h - h > 1:
                continue
            # is end
            if (new_x, new_y) == end:
                print('Found end')
                print(prevs[(x, y)])
                print(len(prevs[(x, y)])+1)
                # print(len(prevs))
                return
            # we've already visited, check if this is a shorter route
            if (new_x, new_y) in prevs:
                prev_length = len(prevs[(new_x, new_y)])
                # shorter route, overwrite and update
                if len(prevs[(x, y)]) + 1 <  prev_length:
                    print(f'    found shorter route to {new_x, new_y} via {x, y}')
                    prevs[(new_x, new_y)] = prevs[(x, y)] + [(x, y)]
                    q.append((new_x, new_y))
                else:
                    print(f'    existing route to {new_x, new_y} is shorter')
                    # print(f'      {prevs[(x, y)]}')
                    # print(f'      {prevs[(new_x, new_y)]}')
            # never visited
            else:
                print(f'    added route to {new_x, new_y} via {x, y}')
                prevs[(new_x, new_y)] = prevs[(x, y)] + [(x, y)]
                q.append((new_x, new_y))
    print(prevs)
            

main()
