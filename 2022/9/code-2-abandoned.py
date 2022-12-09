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

def move_chain(direction, chain):
    # print(direction, chain)
    # end of the chain
    if len(chain) == 0:
        return
    # no movement, rest of chain stays static
    if direction == '':
        return
    head_pos = chain[0]
    tail_pos = chain[1] if len(chain) > 1 else [0,0]
    tail_dir = ''
    if direction[0] == 'U':
        head_pos[1] += 1
        if len(direction) == 2:
            if direction[1] == 'L':
                head_pos[0] -= 1
            elif direction[1] == 'R':
                head_pos[0] += 1
        if head_pos[1] - tail_pos[1] > 1:
            tail_dir = 'U'
        if math.dist(head_pos, tail_pos) > 2:
            if tail_pos[0] > head_pos[0]:
                tail_dir = 'UL'
            elif tail_pos[0] < head_pos[0]:
                tail_dir = 'UR'
        move_chain(tail_dir, chain[1:])
    elif direction[0] == 'D':
        head_pos[1] -= 1
        if len(direction) == 2:
            if direction[1] == 'L':
                head_pos[0] -= 1
            elif direction[1] == 'R':
                head_pos[0] += 1
        if tail_pos[1] - head_pos[1] > 1:
            tail_dir = 'D'
        if math.dist(head_pos, tail_pos) > 2:
            if tail_pos[0] > head_pos[0]:
                tail_dir = 'DL'
            elif tail_pos[0] < head_pos[0]:
                tail_dir = 'DR'
        move_chain(tail_dir, chain[1:])
    elif direction[0] == 'R':
        head_pos[0] += 1
        if head_pos[0] - tail_pos[0] > 1:
            tail_dir = 'R'
        if math.dist(head_pos, tail_pos) > 2:
            if tail_pos[1] > head_pos[1]:
                tail_dir = 'DR'
            elif tail_pos[1] < head_pos[1]:
                tail_dir = 'UR'
        move_chain(tail_dir, chain[1:])
    elif direction[0] == 'L':
        head_pos[0] -= 1
        if tail_pos[0] - head_pos[0] > 1:
            tail_dir = 'L'
        if math.dist(head_pos, tail_pos) > 2:
            if tail_pos[1] > head_pos[1]:
                tail_dir = 'DL'
            elif tail_pos[1] < head_pos[1]:
                tail_dir = 'UL'
        move_chain(tail_dir, chain[1:])



def main():
    inp = [x for x in open('input.txt').read().strip().split('\n')]
    chain = [[0,0] for i in range(10)]
    tail_visited = set()
    tail_visited.add((0,0))
    for line in inp:
        args = line.split(' ')
        direction, amount = args[0], int(args[1])
        print(line)
        for _ in range(amount):
            move_chain(direction, chain)
            tail_visited.add(tuple(chain[9]))
            # print(chain)
            # print_grid(chain)
        # print(chain)
        # print_grid(chain)

    print_grid(tail_visited)
    print(tail_visited)
    print(len(tail_visited))

main()
