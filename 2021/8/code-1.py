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
    'abcdefg': 8,
    'abcefg': 0,
    'abdefg': 6,
    'abcdfg': 9,
    'acdeg': 2,
    'acdfg': 3,
    'abdfg': 5,
    'bcdf': 4,
    'acf': 7,
    'cf': 1,
}

pairs = {}
sum = 0
for patterns, outputs in input:
    for output in outputs:
        if len(output) in [2,3,4,7]:
            sum += 1

print(sum)