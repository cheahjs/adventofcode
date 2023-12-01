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
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        num = int(''.join([digits[0], digits[-1]]))
        sum += num
    print(sum)

main()


