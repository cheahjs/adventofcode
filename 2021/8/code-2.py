#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

input = []
for x in open('input.txt').read().strip().split('\n'):
    parts = x.split(' | ')
    input.append((parts[0].split(), parts[1].split()))

digit_map = {
    'abcdefg': '8',
    'abcefg': '0',
    'abdefg': '6',
    'abcdfg': '9',
    'acdeg': '2',
    'acdfg': '3',
    'abdfg': '5',
    'bcdf': '4',
    'acf': '7',
    'cf': '1',
}

sum = 0
for patterns, outputs in input:
    patterns_5 = []
    patterns_6 = []
    swapped_map = {}
    for pattern in patterns + outputs:
        pattern = ''.join(sorted(pattern))
        if len(pattern) == 2:
            swapped_map[pattern] = '1'
        if len(pattern) == 3:
            swapped_map[pattern] = '7'
        if len(pattern) == 4:
            swapped_map[pattern] = '4'
        if len(pattern) == 7:
            swapped_map[pattern] = '8'

        if len(pattern) == 5:
            patterns_5.append(pattern)
        if len(pattern) == 6:
            patterns_6.append(pattern)

    def invert_map(m):
        return {v: k for k, v in m.items()}

    for pattern in patterns_5:
        # cf not a subset of:
        # * acdeg - 2
        # * abdfg - 5
        # * abdefg - 6
        # cf is a subset of:
        # * acdfg - 3
        # * abcefg - 0
        # * abcdfg - 9
        if set(invert_map(swapped_map)['1']).issubset(pattern):
            swapped_map[pattern] = '3'
            patterns_5.remove(pattern)
            break

    for pattern in patterns_6:
        if not set(invert_map(swapped_map)['1']).issubset(pattern):
            swapped_map[pattern] = '6'
        elif not set(invert_map(swapped_map)['3']).issubset(pattern):
            swapped_map[pattern] = '0'
        else:
            swapped_map[pattern] = '9'

    # diff between 2,5
    #  acdeg, abdfg
    # -bf    -ce
    c = (set('abcdefg') - set(invert_map(swapped_map)['6'])).pop()
    if c in patterns_5[0]:
        swapped_map[patterns_5[0]] = '2'
        swapped_map[patterns_5[1]] = '5'
    else:
        swapped_map[patterns_5[1]] = '2'
        swapped_map[patterns_5[0]] = '5'

    if len(swapped_map) != 10:
        print(f'Could not find full pair map, only found {swapped_map}')
        continue

    digits = ''

    for output in outputs:
        digits += swapped_map[''.join(sorted(output))]

    print(digits)
    sum += int(digits)

print(sum)