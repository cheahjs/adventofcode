#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def process(line: str):
    for i in range(len(line)-4):
        test = set(line[i:i+4])
        if len(test) != 4:
            continue
        print('start of marker', test, 'at pos', i, 'processed', i+4)
        break

def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]

    for line in input:
        process(line)

main()
