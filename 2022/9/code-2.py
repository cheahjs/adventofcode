#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import math
from collections import defaultdict

def print_grid(grid):
    if type(grid) == list:
        new_grid = set()
        for a in grid:
            new_grid.add(tuple(a))
        grid = new_grid
    lowest_x = min(grid, key=lambda p: p[0])[0]
    highest_x = max(grid, key=lambda p: p[0])[0]
    lowest_y = min(grid, key=lambda p: p[1])[1]
    highest_y = max(grid, key=lambda p: p[1])[1]
    lines = []
    for y in range(lowest_y, highest_y+1):
        line = ''
        for x in range(lowest_x, highest_x+1):
            line += '#' if (x, y) in grid else '.'
        lines.append(line)
    lines.reverse()
    for line in lines:
        print(line)

def main():
    dirs = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }
    inp = [x for x in open('input.txt').read().strip().split('\n')]
    chain = [[0,0] for i in range(10)]
    tail_visited = set()
    tail_visited.add((0,0))
    for line in inp:
        args = line.split(' ')
        direction, amount = dirs[args[0]], int(args[1])
        print(line)
        for _ in range(amount):
            chain[0][0] += direction[0]
            chain[0][1] += direction[1]
            for i in range(1, len(chain)):
                head = chain[i-1]
                tail = chain[i]
                dx = head[0] - tail[0]
                dy = head[1] - tail[1]
                # no diagonal movement
                if dx == 0 or dy == 0:
                    if abs(dx) >= 2:
                        tail[0] += 1 if dx > 0 else -1
                    if abs(dy) >= 2:
                        tail[1] += 1 if dy > 0 else -1
                elif (abs(dx),abs(dy)) != (1,1):
                    # no longer attached diagonally
                    tail[0] += 1 if dx > 0 else -1
                    tail[1] += 1 if dy > 0 else -1
            tail_visited.add(tuple(chain[-1]))

    print_grid(tail_visited)
    print(tail_visited)
    print(len(tail_visited))

main()
