#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def main():
    input = [x.split(',') for x in open('input.txt').read().strip().split('\n')]
    overlap = 0
    for [a, b] in input:
        aa, ab = [int(x) for x in a.split('-')]
        ba, bb = [int(x) for x in b.split('-')]
        # check if fully enclosed
        if aa >= ba and ab <= bb:
            overlap += 1
            # print(a, b)
        elif ba >= aa and bb <= ab:
            overlap += 1
            # print(a,b)
    print(overlap)
main()
