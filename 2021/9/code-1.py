#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

# input[x][y]
input = [[int(i) for i in x] for x in open('input.txt').read().strip().split('\n')]

adj_tests = [
        [-1, 0],
    [0, -1], [0, 1],
        [1, 0]
]

risk_level_sum = 0

for x in range(len(input)):
    row = input[x]
    for y in range(len(row)):
        lowest = True
        for test in adj_tests:
            x_test = x + test[0]
            y_test = y + test[1]
            if x_test < 0 or x_test >= len(input):
                continue
            if y_test < 0 or y_test >= len(row):
                continue
            # print(f'Testing {input[x_test][y_test]} against {input[x][y]}')
            if input[x_test][y_test] <= input[x][y]:
                lowest = False
                break
        if lowest:
            print(f'Found lowest {input[x][y]}')
            risk_level_sum += input[x][y] + 1
        # print()

print('Risk level', risk_level_sum)