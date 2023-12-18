#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
from collections import defaultdict

LEFT = 'L'
UP = 'U'
RIGHT = 'R'
DOWN = 'D'
d = {
    LEFT: (0, -1),
    UP: (-1, 0),
    RIGHT: (0, 1),
    DOWN: (1, 0)
}

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    edge_nodes = set([(0, 0)])
    def print_debug(visit):
        min_x = min(visit, key=lambda x: x[0])[0]
        max_x = max(visit, key=lambda x: x[0])[0]
        min_y = min(visit, key=lambda x: x[1])[1]
        max_y = max(visit, key=lambda x: x[1])[1]
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                if (x, y) in visit:
                    print('#', end='')
                else:
                    print('.', end='')
            print()
    cur_pos = (0, 0)
    for line in input:
        dir, steps, color = line.split()
        steps = int(steps)
        for _ in range(steps):
            cur_pos = (cur_pos[0] + d[dir][0], cur_pos[1] + d[dir][1])
            edge_nodes.add(cur_pos)
    # print_debug()
    min_x = min(edge_nodes, key=lambda x: x[0])[0]
    max_x = max(edge_nodes, key=lambda x: x[0])[0]
    min_y = min(edge_nodes, key=lambda x: x[1])[1]
    max_y = max(edge_nodes, key=lambda x: x[1])[1]
    # flood fill from the outside
    fill_start = (min_x - 1, min_y - 1)
    visit = set()
    q = [fill_start]
    while q:
        cur = q.pop(0)
        if cur in visit:
            continue
        visit.add(cur)
        for dir, dl in d.items():
            next = (cur[0] + dl[0], cur[1] + dl[1])
            if not (min_x-2 < next[0] < max_x+2 and min_y-2 < next[1] < max_y+2):
                continue
            if next not in visit and next not in edge_nodes:
                q.append(next)
    print_debug(visit)
    min_x = min(visit, key=lambda x: x[0])[0]
    max_x = max(visit, key=lambda x: x[0])[0]
    min_y = min(visit, key=lambda x: x[1])[1]
    max_y = max(visit, key=lambda x: x[1])[1]
    square_size = (max_x - min_x + 1) * (max_y - min_y + 1)
    print(square_size)
    print(square_size - len(visit))
main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
