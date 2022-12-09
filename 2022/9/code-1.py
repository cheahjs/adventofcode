#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def distance(a, b):
    pass

def main():
    inp = [x for x in open('input.txt').read().strip().split('\n')]
    head_pos = [0, 0]
    tail_pos = [0, 0]
    tail_visited = set()
    tail_visited.add(tuple(tail_pos))
    for line in inp:
        args = line.split(' ')
        direction, amount = args[0], int(args[1])
        if direction == 'U':
            for _ in range(amount):
                head_pos[1] += 1
                if head_pos[1] - tail_pos[1] > 1:
                    tail_pos[1] += 1
                    tail_pos[0] = head_pos[0]
                    tail_visited.add(tuple(tail_pos))
        elif direction == 'D':
            for _ in range(amount):
                head_pos[1] -= 1
                if tail_pos[1] - head_pos[1] > 1:
                    tail_pos[1] -= 1
                    tail_pos[0] = head_pos[0]
                    tail_visited.add(tuple(tail_pos))
        elif direction == 'R':
            for _ in range(amount):
                head_pos[0] += 1
                if head_pos[0] - tail_pos[0] > 1:
                    tail_pos[0] += 1
                    tail_pos[1] = head_pos[1]
                    tail_visited.add(tuple(tail_pos))
        elif direction == 'L':
            for _ in range(amount):
                head_pos[0] -= 1
                if tail_pos[0] - head_pos[0] > 1:
                    tail_pos[0] -= 1
                    tail_pos[1] = head_pos[1]
                    tail_visited.add(tuple(tail_pos))

    print(tail_visited)
    print(len(tail_visited))

main()
