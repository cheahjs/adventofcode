#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
from collections import defaultdict

LEFT = 2
UP = 3
RIGHT = 0
DOWN = 1
d = {
    LEFT: (0, -1),
    UP: (-1, 0),
    RIGHT: (0, 1),
    DOWN: (1, 0)
}

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    edge_nodes = [(0, 0)]
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
        _, _, color = line.split()
        color = color[2:-1]
        steps = int(color[:-1], 16)
        print(steps)
        dir = int(color[-1])
        for _ in range(steps):
            cur_pos = (cur_pos[0] + d[dir][0], cur_pos[1] + d[dir][1])
            edge_nodes.append(cur_pos)
    # print_debug()
    # shoelace formula, 2A = sum(x1y2 - y1x2)
    area = 0
    for i in range(len(edge_nodes)-1):
        x1, y1 = edge_nodes[i]
        x2, y2 = edge_nodes[i+1]
        area += y2*x1 - y1*x2
    area = abs(area)//2
    # pick's theorem
    perimeter = len(edge_nodes)
    interior_area = area - perimeter//2 # + 1
    total_area = interior_area + perimeter
    print(total_area)

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
