#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def main():
    input = open('input.txt').read().strip().replace('target area: ', '')
    x_b, y_b = input.split(', ')
    x_min, x_max = [int(i) for i in x_b.replace('x=', '').split('..')]
    y_min, y_max = [int(i) for i in y_b.replace('y=', '').split('..')]

    # map of x_vel -> [steps in range]
    m = defaultdict(list)
    # x is always positive
    # find all initial x vel that lands in target area
    for x_v_i in range(1, x_max+1):
        x_v = x_v_i
        x = 0
        step = 0
        while x_v > 0:
            x += x_v
            x_v -= 1
            step += 1
            if x_min <= x <= x_max:
                m[x_v_i].append(step)

        # Add marker to indicate that it stops in bounds
        if x_min <= x <= x_max:
            m[x_v_i].append(-1)

    h = {}

    for x_v_i, steps in m.items():
        # lower bound for y_v_i is y_min
        # upper bound is constrained by steps (how?)
        for y_v_i in range(y_min-1, 500):
            # print('Testing', x_v_i, y_v_i)
            x, y = 0, 0
            x_v, y_v = x_v_i, y_v_i
            highest_y = 0
            while y >= y_min:
                x += x_v
                y += y_v
                if y > highest_y:
                    highest_y = y
                x_v = max(0, x_v-1)
                y_v -= 1
                # print(x, y, x_v, y_v)
                if x_min <= x <= x_max and y_min <= y <= y_max:
                    # print('HIT', x_v_i, y_v_i)
                    # print('At', x, y, 'Highest', highest_y)
                    h[(x_v_i, y_v_i)] = True

    print(len(h))

main()
