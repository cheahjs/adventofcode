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


def recurse_explode(pair, val, dir):
    if dir == LEFT:
        if isinstance(pair[LEFT], list):
            pair[LEFT], val = recurse_explode(
                pair[LEFT], val, LEFT)
            if val != 0:
                pair[RIGHT], val = recurse_explode(pair[RIGHT], val, LEFT)
            return pair, val
        else:
            print('Putting exploded', val, 'into left of pair', pair)
            pair[LEFT] += val
            return pair, 0
    elif dir == RIGHT:
        if isinstance(pair[RIGHT], list):
            pair[RIGHT], val = recurse_explode(pair[RIGHT], val, RIGHT)
            if val != 0:
                pair[LEFT], val = recurse_explode(pair[LEFT], val, RIGHT)
            return pair, val
        else:
            print('Putting exploded', val, 'into right of pair', pair)
            pair[RIGHT] += val
            return pair, 0


def recurse(pair, depth):
    ret = NONE

    if depth == 4:
        # explode
        print('Exploding', pair)
        return 0, EXPLODE, pair

    # Must explode/split leftmost first
    if isinstance(pair[LEFT], list):
        pair[LEFT], res, val = recurse(pair[LEFT], depth+1)
        ret = res
        if res == EXPLODE:
            # check if the right val is a regular number
            if val[RIGHT] > 0:
                if isinstance(pair[RIGHT], int):
                    print('Putting right exploded', val,
                          'into right of pair', pair)
                    pair[RIGHT] += val[RIGHT]
                    val[RIGHT] = 0
                else:
                    pair[RIGHT], val[RIGHT] = recurse_explode(
                        pair[RIGHT], val[RIGHT], LEFT)
            return pair, EXPLODE, val
        elif res == SPLIT:
            return pair, SPLIT, val
    else:
        # regular number
        if pair[LEFT] >= 10:
            # print('Splitting', pair[LEFT], 'in', pair)
            pair[LEFT] = [math.floor(pair[LEFT]/2), math.ceil(pair[LEFT]/2)]
            # print(pair)
            return pair, SPLIT, None

    if isinstance(pair[RIGHT], list):
        pair[RIGHT], res, val = recurse(pair[RIGHT], depth+1)
        ret = res
        if res == EXPLODE:
            # check if the left val is a regular number
            if val[LEFT] > 0:
                if isinstance(pair[LEFT], int):
                    print('Putting left exploded', val,
                          'into left of pair', pair)
                    pair[LEFT] += val[LEFT]
                    val[LEFT] = 0
                else:
                    pair[LEFT], val[LEFT] = recurse_explode(
                        pair[LEFT], val[LEFT], RIGHT)
            return pair, EXPLODE, val
        elif res == SPLIT:
            return pair, SPLIT, val
    else:
        # regular number
        if pair[RIGHT] >= 10:
            # print('Splitting', pair[RIGHT], 'in', pair)
            pair[RIGHT] = [math.floor(pair[RIGHT]/2), math.ceil(pair[RIGHT]/2)]
            # print(pair)
            return pair, SPLIT, None

    return pair, ret, None


def main():
    input = [json.loads(x)
             for x in open('test-2.txt').read().strip().split('\n')]

    while len(input) > 1:
        print('Adding')
        print(input[0])
        print(input[1])
        input[0] = [input[0], input[1]]
        print(input[0])
        del input[1]
        while True:
            input[0], res, _ = recurse(input[0], 0)
            print(f'after {res}: {input[0]}')
            if res == NONE:
                break
        print('Result:', input[0])

    print(input[0])


main()
