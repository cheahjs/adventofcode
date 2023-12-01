#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def main():
    b_l = -50
    b_h = 50
    input = []
    for l in open('input.txt').read().strip().split('\n'):
        state, raw_bounds = l.split(' ')
        x, y, z = [j.split('=')[1] for j in raw_bounds.split(',')]
        xl, xh = [int(j) for j in x.split('..')]
        yl, yh = [int(j) for j in y.split('..')]
        zl, zh = [int(j) for j in z.split('..')]
        if xl < b_l or xh > b_h or yl < b_l or yh > b_h or zl < b_l or zl > b_h:
            continue
        input.append((state, ((xl, xh), (yl, yh), (zl, zh))))

    # we all know this ain't working for part 2
    space = set()
    for command, (x_b, y_b, z_b) in input:
        for x in range(x_b[0], x_b[1]+1):
            for y in range(y_b[0], y_b[1]+1):
                for z in range(z_b[0], z_b[1]+1):
                    if command == 'on':
                        space.add((x,y,z))
                    else:
                        space.discard((x,y,z))

    print(len(space))

main()
