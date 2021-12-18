#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import json
import math
from collections import defaultdict

EXPLODE = 'explode'
SPLIT = 'split'
NONE = 'none'

LEFT = 0
RIGHT = 1

def flatten(input, path):
    flat = []
    left_path = path[:]
    left_path.append(LEFT)
    if isinstance(input[LEFT], list):
        flat.extend(flatten(input[LEFT], left_path))
    else:
        flat.append((input[LEFT], left_path))

    right_path = path[:]
    right_path.append(RIGHT)
    if isinstance(input[RIGHT], list):
        flat.extend(flatten(input[RIGHT], right_path))
    else:
        flat.append((input[RIGHT], right_path))

    return flat

def unflatten(input):
    output = [[], []]

    for val, path in input:
        cur_pair = output
        for dir in path[:-1]:
            cur_pair = cur_pair[dir]
            if len(cur_pair) < 2:
                cur_pair.extend([[], []])
        cur_pair[path[-1]] = val

    return output

def magnitude(input):
    if isinstance(input, int):
        return input
    return 3*magnitude(input[LEFT]) + 2*magnitude(input[RIGHT])

def main(test_file):
    input = [json.loads(x)
             for x in open(test_file).read().strip().split('\n')]

    while len(input) > 1:
        print('Adding')
        print(input[0], '+', input[1])
        input[0] = [input[0], input[1]]
        print(input[0])
        del input[1]

        flat = flatten(input[0], [])
        assert(input[0] == unflatten(flat))
        while True:
            more_ops = False
            # First pass for explosions
            for i, (val, path) in enumerate(flat):
                if len(path) == 5:
                    # explode
                    left_explode = flat[i]
                    right_explode = flat[i+1]
                    # replace
                    del flat[i+1]
                    flat[i] = (0, path[:-1])
                    # left side
                    if i-1 >= 0:
                        flat[i-1] = (flat[i-1][0] + left_explode[0], flat[i-1][1])
                    # right side
                    if i+1 < len(flat):
                        flat[i+1] = (flat[i+1][0] +
                                     right_explode[0], flat[i+1][1])
                    more_ops = True
                    # print('after explode:', unflatten(flat))
                    break
            if not more_ops:
                # Second pass for splits
                for i, (val, path) in enumerate(flat):
                    if val >= 10:
                        left_pair = (math.floor(val/2), path + [LEFT])
                        right_pair = (math.ceil(val/2), path + [RIGHT])
                        flat[i] = left_pair
                        flat.insert(i+1, right_pair)
                        more_ops = True
                        # print('after split:', unflatten(flat))
                        break

            if not more_ops:
                break
        input[0] = unflatten(flat)

        print('Result:', input[0])

    print(input[0])
    print('Magnitude:', magnitude(input[0]))


main('input.txt')
