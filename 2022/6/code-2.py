#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def process(line: str):
    for i in range(len(line)-14):
        test = set(line[i:i+14])
        if len(test) != 14:
            continue
        print('start of message', test, 'at pos', i, 'processed', i+14)
        break

def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]

    for line in input:
        process(line)

main()
