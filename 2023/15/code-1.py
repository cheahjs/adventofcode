#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
from collections import defaultdict

def hash(input):
    value = 0
    for char in input:
        value += ord(char)
        value *= 17
        value = value % 256
    return value

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    steps = input[0].split(',')
    total = 0
    for step in steps:
        val = hash(step)
        total += val
    print(total)

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
