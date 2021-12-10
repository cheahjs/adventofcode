#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

input = [x for x in open('test.txt').read().strip().split('\n')]

open_chars = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>',
}

close_chars = {
    ']': '[',
    ')': '(',
    '}': '{',
    '>': '<',
}

close_chars_points = {
    ']': 57,
    ')': 3,
    '}': 1197,
    '>': 25137,
}

score = 0

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
                print(line)
                print(f'{" "*(j)}^')
                print(
                    f'{" "*(j)}Expected {open_chars[prev_open]}, but found {char} instead.')
                corrupted = True
                score += close_chars_points[char]
                break
    if not corrupted and len(stack) > 0:
        print(f'Incomplete line')

print(f'Syntax error score: {score}')