#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

RIGHT = 'right'
OUT = 'out'
CONTINUE = 'continue'

def compare(a, b):
    print('comparing', a, b)
    # both ints
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return RIGHT
        elif a > b:
            return OUT
        elif a == b:
            return CONTINUE
    # one int
    if isinstance(a, int):
        return compare([a], b)
    if isinstance(b, int):
        return compare(a, [b])
    # both lists
    if isinstance(a, list) and isinstance(b, list):
        while len(a) > 0 and len(b) > 0:
            ax = a.pop(0)
            bx = b.pop(0)
            comp = compare(ax, bx)
            if comp != CONTINUE:
                return comp
        # left list empty first
        if len(a) == 0 and len(b) > 0:
            # print('left list empty')
            return RIGHT
        # right list empty first
        elif len(b) == 0 and len(a) > 0:
            # print('right list empty')
            return OUT
        # both empty
        else:
            return CONTINUE

def main():
    pairs = [[eval(y) for y in x.split('\n')] for x in open('input.txt').read().strip().split('\n\n')]
    print(pairs)

    puzzle = 0
    for i, (a,b) in enumerate(pairs):
        print(a)
        print(b)
        res = compare(a, b)
        print(i+1, res)
        if res == RIGHT:
            puzzle += i + 1
    print(puzzle)

main()
