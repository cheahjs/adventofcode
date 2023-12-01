#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def main():
    scanners = []
    b_parsing = []
    for x in open('test-1.txt').read().strip().split('\n'):
        if x.strip() == '':
            scanners.append(b_parsing)
            continue
        if x.startswith('---'):
            b_parsing = []
            continue
        b_parsing.append([int(y) for y in x.split(',')])
    scanners.append(b_parsing)

    # Calculate relative positions (and each of the 6 rotations)
    relative_pos = []
    for scanner_idx, beacons in enumerate(range(scanners)):
        for combinations in itertools.combinations(enumerate(beacons), 2):
            pass

    scanner_pos = {0: (0, 0, 0)}

    # Have all points be relative to scanners[0]
    # abs_pos[0] = (0, 0, 0)
    # For every scanner pair,
    #   Test every beacon relative pos (tracking the rotation used)

main()
