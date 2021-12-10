#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

input = [x for x in open('input.txt').read().strip().split('\n')]

open_chars = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>',
}

open_chars_points = {
    '[': 2,
    '(': 1,
    '{': 3,
    '<': 4,
}

close_chars = {
    ']': '[',
    ')': '(',
    '}': '{',
    '>': '<',
}


scores = []

for i, line in enumerate(input):
    print(f'Testing line {i} {line}')
    stack = []
    corrupted = False
    for j, char in enumerate(line):
        if char in open_chars:
            stack.append(char)
        elif char in close_chars:
            prev_open = stack.pop()
            if close_chars[char] != prev_open:
                corrupted = True
                break
    if corrupted or len(stack) == 0:
        continue

    print(f'Incomplete line')
    stack.reverse()
    print(f'Completed by adding {"".join([open_chars[x] for x in stack])}')
    cur_score = 0
    for x in stack:
        cur_score *= 5
        cur_score += open_chars_points[x]
    print(f'Total points for line: {cur_score}')
    scores.append(cur_score)

scores.sort()
print(scores)
print(f'Autocomplete score: {scores[len(scores)//2]}')