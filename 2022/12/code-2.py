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
    end = None
    q = []
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == -13:
                grid[y][x] = ord('a')-96
                q.append((x, y))
            elif val == -27:
                end = (x, y)
                grid[y][x] = ord('z')-96
            elif val == 1:
                q.append((x, y))
    # pathfinding
    dist = defaultdict(lambda: 1000000)
    for coord in q:
        dist[coord] = 0
    while len(q) > 0:
        x, y = q.pop(0)
        h = grid[y][x]
        # print(f'visiting {x, y}: {h}')
        for adj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_x, new_y = (x + adj[0], y + adj[1])
            # in range
            if not (0 <= new_y < rows and 0 <= new_x < cols):
                continue
            # viable visit
            new_h = grid[new_y][new_x]
            # print(f'  checking ({new_x}, {new_y}): {new_h}')
            if new_h - h > 1:
                continue
            # is end
            if (new_x, new_y) == end:
                print('Found end')
                print(dist[(x,y)]+1)
                return
            new_dist = dist[(x,y)] + 1
            if new_dist < dist[(new_x, new_y)]:
                q.append((new_x, new_y))
                dist[(new_x, new_y)] = new_dist
            

main()
