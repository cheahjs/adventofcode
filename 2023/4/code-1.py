#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]
    sum = 0
    for line in input:
        raw_winning, raw_numbers = line.split(': ')[1].split(' | ')
        winning = set([int(x) for x in raw_winning.split()])
        numbers = [int(x) for x in raw_numbers.split()]
        points = 0
        for number in numbers:
            if number in winning:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        sum += points
        print(points)
    print(sum)

main()
